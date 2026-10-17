#!/usr/bin/env python3
"""Run the real Hermes Agent skill linter + install security scanner on every skill under skills/.
Usage: HERMES_SRC=/path/to/hermes-agent python3 tests/hermes_scan.py
Fails if the scanner would block a community install, or the linter reports an error."""
import os
import sys
from pathlib import Path

src = os.environ.get("HERMES_SRC")
if not src or not Path(src, "tools", "skills_guard.py").is_file():
    sys.exit("set HERMES_SRC to a hermes-agent checkout")
sys.path.insert(0, src)
from tools.skill_linter import lint_skill  # noqa: E402
from tools.skills_guard import format_scan_report, scan_skill, should_allow_install  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
bad = 0
for md in sorted((ROOT / "skills").glob("*/SKILL.md")):
    for f in lint_skill(md):
        print(f"LINT {f.severity} {f.rule}: {f.message}")
        bad += f.severity == "error"
    result = scan_skill(md.parent, "community")
    print(format_scan_report(result))
    ok, why = should_allow_install(result)
    print("install allowed:", ok, "-", why)
    bad += not ok
sys.exit(1 if bad else 0)
