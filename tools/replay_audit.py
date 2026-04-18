#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from deafpiper.audit import AuditQuery, ContentStore
from deafpiper.models import AuditEntryStore


def main() -> None:
    parser = argparse.ArgumentParser(description="Reconstruct task state at timestamp.")
    parser.add_argument("subject_id")
    parser.add_argument("timestamp", help="ISO-8601 UTC timestamp")
    args = parser.parse_args()

    query = AuditQuery(AuditEntryStore(), ContentStore())
    state = query.reconstruct_state(args.subject_id, args.timestamp)
    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
