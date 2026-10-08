#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_EN = ROOT / "prompts-en"

CATEGORY_DESCRIPTIONS = {
    "AI Methods": "Prompt engineering, reverse engineering, meta-prompting, and reusable AI methods.",
    "AI Work": "Business research, contracts, sales, customer service, product prototypes, PPT, and web workflows.",
    "AI Learning": "Learning methods, memory techniques, questioning methods, habits, and learning coaching.",
    "AI Life": "Health, family, and daily-life prompt scenarios.",
    "AI Education": "Children education, interactive learning pages, and educational games.",
    "AI Content": "Writing, copywriting, platform operations, industry content, image prompts, and content review.",
    "AI Coding": "Architecture design and AI-assisted software engineering.",
    "AI Marketing": "Course positioning, design, sales, operations, GEO, source authority, metrics, growth diagnosis, and compliance.",
    "AI Thinking": "Critical thinking, memory palaces, title thinking, and reasoning tools.",
}
CATEGORY_ORDER = list(CATEGORY_DESCRIPTIONS)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    data = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data, text[end + 5 :]


def extract_overview(body: str) -> str:
    match = re.search(r"## Overview\s+(.+?)(?:\n## |\Z)", body, re.S)
    if not match:
        return ""
    text = " ".join(line.strip() for line in match.group(1).splitlines() if line.strip())
    text = re.sub(r"\s+", " ", text)
    return text[:140] + ("..." if len(text) > 140 else "")


def main() -> None:
    files = sorted(p for p in PROMPTS_EN.rglob("*.md") if p.name != "README.md")
    by_category: dict[str, list[Path]] = {category: [] for category in CATEGORY_ORDER}
    for path in files:
        fm, _ = parse_frontmatter(path)
        by_category.setdefault(fm.get("category", "Other"), []).append(path)

    root_lines = [
        "# English Prompts",
        "",
        "This directory mirrors the Chinese `prompts/` library one-to-one. Every Chinese prompt file has a matching English file at the same relative path under `prompts-en/`.",
        "",
        f"Current English prompt files: **{len(files)}**.",
        "",
        "[Course Marketing: 17 companion prompts](08-ai-marketing/course-marketing/README.md) · [Interactive navigator](https://yaojingang.github.io/yao-open-prompts/course-marketing.html?lang=en)",
        "",
        "## Categories",
        "",
        "| Category | Count | Description |",
        "| --- | ---: | --- |",
    ]
    for category in CATEGORY_ORDER:
        items = by_category.get(category, [])
        if not items:
            continue
        first_dir = items[0].relative_to(PROMPTS_EN).parts[0]
        root_lines.append(
            f"| [{category}]({first_dir}/README.md) | {len(items)} | {CATEGORY_DESCRIPTIONS[category]} |"
        )
    root_lines.extend(
        [
            "",
            "## Maintenance",
            "",
            "- Keep the same relative path as the Chinese source file.",
            "- Set `source_section` to the matching `prompts/...` path.",
            "- Run `python3 scripts/check_repo.py` before publishing.",
        ]
    )
    (PROMPTS_EN / "README.md").write_text("\n".join(root_lines) + "\n", encoding="utf-8")

    for category_dir in sorted(p for p in PROMPTS_EN.iterdir() if p.is_dir()):
        dir_files = sorted(p for p in category_dir.rglob("*.md") if p.name != "README.md")
        if not dir_files:
            continue
        first_fm, _ = parse_frontmatter(dir_files[0])
        category = first_fm.get("category", category_dir.name)
        lines = [
            f"# {category}",
            "",
            CATEGORY_DESCRIPTIONS.get(category, "English prompt category."),
            "",
            f"Prompt files: **{len(dir_files)}**.",
            "",
            "| Prompt | Subcategory | Source |",
            "| --- | --- | --- |",
        ]
        if category_dir.name == "08-ai-marketing":
            lines[6:6] = [
                "[Course Marketing: 17 companion prompts](course-marketing/README.md) · [Interactive navigator and usage guide](https://yaojingang.github.io/yao-open-prompts/course-marketing.html?lang=en)",
                "",
            ]
        for path in dir_files:
            fm, body = parse_frontmatter(path)
            rel = path.relative_to(category_dir).as_posix()
            title = fm.get("title", path.stem)
            source = fm.get("source_section", "")
            lines.append(f"| [{title}]({rel}) | {fm.get('subcategory', '')} | `{source}` |")
        (category_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated English README files for {len(files)} prompts.")


if __name__ == "__main__":
    main()
