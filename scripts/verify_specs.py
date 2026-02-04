from __future__ import annotations

from pathlib import Path
import sys


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    required = [
        repo_root / "AGENTS.md",
        repo_root / "SOUL.md",
        repo_root / "specs" / "_meta.md",
        repo_root / "specs" / "functional.md",
        repo_root / "specs" / "technical.md",
        repo_root / "research" / "architecture_strategy.md",
        repo_root / "research" / "tooling_strategy.md",
        repo_root / "skills" / "README.md",
        repo_root / "tests" / "test_trend_fetcher.py",
        repo_root / "tests" / "test_skills_interface.py",
        repo_root / "Dockerfile",
        repo_root / "Makefile",
        repo_root / ".github" / "workflows" / "main.yml",
        repo_root / ".cursor" / "rules",
    ]

    missing = [str(p.relative_to(repo_root)) for p in required if not p.exists()]
    if missing:
        print("Missing required spec files:")
        for m in missing:
            print(f"- {m}")
        return 2

    print("Spec-check OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
