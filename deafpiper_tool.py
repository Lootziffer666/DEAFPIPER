#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from deafpiper.audit import AuditQuery, ContentStore
from deafpiper.models import AuditEntryStore


def cmd_inspect_task(task_id: str) -> None:
    query = AuditQuery(AuditEntryStore(), ContentStore())
    history = query.get_history(task_id)
    print(json.dumps([entry.to_dict() for entry in history], indent=2))


def cmd_replay_audit(subject_id: str, timestamp: str) -> None:
    query = AuditQuery(AuditEntryStore(), ContentStore())
    state = query.reconstruct_state(subject_id, timestamp)
    print(json.dumps(state, indent=2))


def cmd_list_known_issues(path: str = "docs/KNOWN_ISSUES.md") -> None:
    issue_file = Path(path)
    if not issue_file.exists():
        print(f"Known issues file not found: {path}")
        return
    print(issue_file.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified DeafPiper CLI tool")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_cmd = sub.add_parser("inspect-task", help="Show audit history for a task")
    inspect_cmd.add_argument("task_id")

    replay_cmd = sub.add_parser("replay-audit", help="Reconstruct state at timestamp")
    replay_cmd.add_argument("subject_id")
    replay_cmd.add_argument("timestamp", help="ISO-8601 UTC timestamp")

    known_cmd = sub.add_parser("list-known-issues", help="Print KNOWN_ISSUES.md")
    known_cmd.add_argument("--path", default="docs/KNOWN_ISSUES.md")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "inspect-task":
        cmd_inspect_task(args.task_id)
    elif args.command == "replay-audit":
        cmd_replay_audit(args.subject_id, args.timestamp)
    elif args.command == "list-known-issues":
        cmd_list_known_issues(args.path)


if __name__ == "__main__":
    main()
