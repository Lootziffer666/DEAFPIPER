#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from deafpiper.audit import AuditQuery, ContentStore
from deafpiper.models import AuditEntryStore


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect task history from in-memory audit store snapshot.")
    parser.add_argument("task_id")
    args = parser.parse_args()

    # Placeholder local stores; in real usage these would be loaded from persistence.
    query = AuditQuery(AuditEntryStore(), ContentStore())
    history = query.get_history(args.task_id)
    print(json.dumps([entry.to_dict() for entry in history], indent=2))


if __name__ == "__main__":
    main()
