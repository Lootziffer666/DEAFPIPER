from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional

from .models import AuditEntry, AuditEntryStore


class ContentStore:
    """Content-addressable in-memory blob store."""

    def __init__(self) -> None:
        self._blobs: Dict[str, str] = {}

    def put(self, payload: Mapping[str, Any] | str) -> str:
        raw = payload if isinstance(payload, str) else json.dumps(payload, sort_keys=True)
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        ref = f"sha256:{digest}"
        self._blobs[ref] = raw
        return ref

    def get(self, payload_ref: str) -> Optional[str]:
        return self._blobs.get(payload_ref)

    def list_refs(self) -> List[str]:
        return sorted(self._blobs)

    def snapshot(self) -> Dict[str, str]:
        return dict(self._blobs)

    def restore(self, snapshot: Mapping[str, str]) -> None:
        self._blobs = dict(snapshot)


class FileBackedContentStore(ContentStore):
    """Persistent content store that keeps blobs in a JSON map on disk."""

    def __init__(self, path: str | Path) -> None:
        super().__init__()
        self.path = Path(path)
        if self.path.exists():
            loaded = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                self.restore({str(k): str(v) for k, v in loaded.items()})

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.snapshot(), indent=2, sort_keys=True), encoding="utf-8")

    def put(self, payload: Mapping[str, Any] | str) -> str:
        ref = super().put(payload)
        self.flush()
        return ref




class FileBackedAuditEntryStore(AuditEntryStore):
    """Persistent audit entry store backed by a JSON file."""

    def __init__(self, path: str | Path) -> None:
        super().__init__()
        self.path = Path(path)
        if self.path.exists():
            loaded = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(loaded, list):
                self.restore(loaded)

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.snapshot(), indent=2, sort_keys=True), encoding="utf-8")

    def append(self, entry: AuditEntry) -> None:
        super().append(entry)
        self.flush()


class AuditLogger:
    def __init__(self, store: AuditEntryStore, content_store: ContentStore) -> None:
        self.store = store
        self.content_store = content_store

    def log(
        self,
        actor: Mapping[str, Any],
        subject_type: str,
        subject_id: str,
        event: str,
        previous_state: str | None,
        new_state: str | None,
        payload: Mapping[str, Any] | str,
    ) -> AuditEntry:
        payload_ref = self.content_store.put(payload)
        next_id = len(self.store.list_entries()) + 1
        entry = AuditEntry(
            id=next_id,
            timestamp=datetime.now(timezone.utc).isoformat(),
            actor=dict(actor),
            subject_type=subject_type,
            subject_id=subject_id,
            event=event,
            previous_state=previous_state,
            new_state=new_state,
            payload_ref=payload_ref,
        )
        self.store.append(entry)
        return entry


class AuditQuery:
    def __init__(self, store: AuditEntryStore, content_store: ContentStore) -> None:
        self.store = store
        self.content_store = content_store

    def get_history(self, subject_id: str) -> List[AuditEntry]:
        return [entry for entry in self.store.list_entries() if entry.subject_id == subject_id]

    def reconstruct_state(self, subject_id: str, at_timestamp: str) -> Dict[str, Any]:
        history = sorted(self.get_history(subject_id), key=lambda x: x.id)
        state: Dict[str, Any] = {"subject_id": subject_id, "state": None, "last_payload": None}
        for entry in history:
            if entry.timestamp > at_timestamp:
                break
            state["state"] = entry.new_state
            state["last_payload"] = self.content_store.get(entry.payload_ref)
        return state

    def list_overrides(self, since: str, until: str) -> List[AuditEntry]:
        return self._list_by_event_in_range(event="overridden", since=since, until=until)

    def list_dead_ends(self, since: str, until: str) -> List[AuditEntry]:
        return self._list_by_event_in_range(event="dead_end", since=since, until=until)

    def list_rework_chains(self, task_id: str) -> List[List[str]]:
        chains: List[List[str]] = []
        current_chain: List[str] = []
        entries = [entry for entry in self.store.list_entries() if entry.subject_id == task_id]
        for entry in entries:
            payload_raw = self.content_store.get(entry.payload_ref)
            payload = json.loads(payload_raw) if payload_raw else {}
            if entry.event == "decided" and payload.get("decision") == "rework":
                current_chain.append(payload.get("artifact_candidate_id", "unknown"))
            elif current_chain:
                chains.append(current_chain)
                current_chain = []
        if current_chain:
            chains.append(current_chain)
        return chains

    def _list_by_event_in_range(self, event: str, since: str, until: str) -> List[AuditEntry]:
        return [
            entry
            for entry in self.store.list_entries()
            if entry.event == event and since <= entry.timestamp <= until
        ]
