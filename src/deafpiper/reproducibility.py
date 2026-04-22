from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import dataclass
from typing import Any, Dict, Mapping, Sequence


@dataclass(frozen=True)
class EnvironmentFingerprint:
    python_version: str
    platform: str
    implementation: str
    executable: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "python_version": self.python_version,
            "platform": self.platform,
            "implementation": self.implementation,
            "executable": self.executable,
        }


class ReproducibilitySurface:
    """Canonical hashing helpers for runtime environment and task inputs."""

    @staticmethod
    def runtime_fingerprint() -> EnvironmentFingerprint:
        return EnvironmentFingerprint(
            python_version=sys.version.split()[0],
            platform=platform.platform(),
            implementation=platform.python_implementation(),
            executable=sys.executable,
        )

    @staticmethod
    def hash_payload(payload: Mapping[str, Any] | Sequence[Any] | str) -> str:
        if isinstance(payload, str):
            raw = payload
        else:
            raw = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        return f"sha256:{digest}"

    @classmethod
    def build_environment_ref(cls, extra: Mapping[str, Any] | None = None) -> str:
        data: Dict[str, Any] = {"runtime": cls.runtime_fingerprint().to_dict()}
        if extra:
            data["extra"] = dict(extra)
        return cls.hash_payload(data)
