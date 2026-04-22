#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
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


def cmd_repo_health() -> None:
    """Reports git branch/remote health and avoids 'branch invalid' ambiguity."""
    def run_git(args: list[str]) -> str:
        proc = subprocess.run(["git", *args], capture_output=True, text=True)
        return proc.stdout.strip() if proc.returncode == 0 else ""

    local_branches = run_git(["branch", "--format=%(refname:short)"]).splitlines()
    remote_branches = run_git(["branch", "-r", "--format=%(refname:short)"]).splitlines()
    remotes = run_git(["remote", "-v"]).splitlines()

    main_local = "main" in local_branches
    main_remote = any(branch.endswith("/main") for branch in remote_branches)

    payload = {
        "main_local": main_local,
        "main_remote": main_remote,
        "local_branches": local_branches,
        "remote_branches": remote_branches,
        "remotes": remotes,
        "advice": (
            "main branch available"
            if (main_local or main_remote)
            else "no main found; set remote and fetch or create local main"
        ),
    }
    print(json.dumps(payload, indent=2))


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

    sub.add_parser("repo-health", help="Show git branch/remote health (incl. main availability)")

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
    elif args.command == "repo-health":
        cmd_repo_health()


if __name__ == "__main__":
    main()
