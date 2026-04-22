import json
import unittest
from datetime import datetime, timedelta, timezone

from deafpiper.audit import AuditLogger, AuditQuery, ContentStore
from deafpiper.models import AuditEntryStore


class Phase5AuditTests(unittest.TestCase):
    def test_content_store_is_content_addressable(self):
        store = ContentStore()
        ref1 = store.put({"a": 1, "b": 2})
        ref2 = store.put({"b": 2, "a": 1})
        self.assertEqual(ref1, ref2)

    def test_logger_and_query_reconstruct_state(self):
        entry_store = AuditEntryStore()
        content_store = ContentStore()
        logger = AuditLogger(entry_store, content_store)
        query = AuditQuery(entry_store, content_store)

        logger.log(
            actor={"type": "agent", "id": "a1"},
            subject_type="Task",
            subject_id="task-1",
            event="created",
            previous_state=None,
            new_state="draft",
            payload={"task": "created"},
        )
        logger.log(
            actor={"type": "agent", "id": "a1"},
            subject_type="Task",
            subject_id="task-1",
            event="transitioned",
            previous_state="draft",
            new_state="ready",
            payload={"task": "ready"},
        )

        future = (datetime.now(timezone.utc) + timedelta(seconds=5)).isoformat()
        state = query.reconstruct_state("task-1", future)
        self.assertEqual(state["state"], "ready")
        self.assertEqual(json.loads(state["last_payload"])["task"], "ready")

    def test_override_dead_end_and_rework_queries(self):
        entry_store = AuditEntryStore()
        content_store = ContentStore()
        logger = AuditLogger(entry_store, content_store)
        query = AuditQuery(entry_store, content_store)

        logger.log(
            actor={"type": "human", "id": "u1"},
            subject_type="Task",
            subject_id="task-2",
            event="overridden",
            previous_state="compared",
            new_state="decided",
            payload={"note": "approved override"},
        )
        logger.log(
            actor={"type": "agent", "id": "a1"},
            subject_type="Task",
            subject_id="task-2",
            event="dead_end",
            previous_state="running",
            new_state="blocked",
            payload={"category": "validation_loop"},
        )
        logger.log(
            actor={"type": "agent", "id": "a1"},
            subject_type="Task",
            subject_id="task-2",
            event="decided",
            previous_state="compared",
            new_state="decided",
            payload={"decision": "rework", "artifact_candidate_id": "a-01"},
        )

        since = "2000-01-01T00:00:00+00:00"
        until = "2100-01-01T00:00:00+00:00"

        self.assertEqual(len(query.list_overrides(since, until)), 1)
        self.assertEqual(len(query.list_dead_ends(since, until)), 1)
        self.assertEqual(query.list_rework_chains("task-2"), [["a-01"]])


if __name__ == "__main__":
    unittest.main()
