#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import quote


BADGE_START = "<!-- QUALITY_BADGE_START -->"
BADGE_END = "<!-- QUALITY_BADGE_END -->"


def load_assessment(json_path: Path) -> dict:
    if not json_path.exists():
        raise FileNotFoundError(f"Assessment file not found: {json_path}")

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    checks = data.get("checks")
    if not isinstance(checks, list):
        raise ValueError("Invalid JSON: missing 'checks' list")

    return data


def summarize_checks(checks: list[dict]) -> tuple[int, int, int]:
    passed = failed = errors = 0

    for check in checks:
        output = str(check.get("output", "")).strip().lower()
        if output == "true":
            passed += 1
        elif output == "false":
            failed += 1
        else:
            errors += 1

    return passed, failed, errors


def compute_score(passed: int, failed: int) -> int:
    total = passed + failed
    if total == 0:
        return 0
    return round((passed / total) * 100)


def badge_color(score: int) -> str:
    if score >= 90:
        return "brightgreen"
    if score >= 75:
        return "green"
    if score >= 60:
        return "yellow"
    if score >= 40:
        return "orange"
    return "red"


def build_badge_url(score: int) -> str:
    color = badge_color(score)
    label = quote("quality")
    message = quote(f"{score}%")
    return f"https://img.shields.io/badge/{label}-{message}-{color}"


def build_badge_markdown(url: str, score: int, passed: int, failed: int, errors: int) -> str:
    title = f"score: {score}% | passed: {passed} | failed: {failed} | errors: {errors}"
    return (
        f"{BADGE_START}\n"
        f'![Software quality]({url} "{title}")\n'
        f"{BADGE_END}"
    )


def replace_or_insert_badge(readme: str, badge_block: str) -> str:
    if BADGE_START in readme and BADGE_END in readme:
        start = readme.index(BADGE_START)
        end = readme.index(BADGE_END) + len(BADGE_END)
        return readme[:start] + badge_block + readme[end:]

    lines = readme.splitlines()
    if lines and lines[0].startswith("# "):
        return lines[0] + "\n\n" + badge_block + "\n\n" + "\n".join(lines[1:]).lstrip()

    return badge_block + "\n\n" + readme


def update_readme(readme_path: Path, project_name: str, badge_block: str) -> None:
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        updated = replace_or_insert_badge(content, badge_block)
    else:
        updated = f"# {project_name}\n\n{badge_block}\n"

    readme_path.write_text(updated, encoding="utf-8")


def main() -> int:
    json_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rsfc_assessment.json")
    readme_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("README.md")

    data = load_assessment(json_path)

    project_name = data.get("assessedSoftware", {}).get("name", "Project")
    passed, failed, errors = summarize_checks(data["checks"])
    score = compute_score(passed, failed)

    badge_url = build_badge_url(score)
    badge_block = build_badge_markdown(badge_url, score, passed, failed, errors)

    update_readme(readme_path, project_name, badge_block)

    print("README updated successfully")
    print(f"Score: {score}%")
    print(f"Badge URL: {badge_url}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())