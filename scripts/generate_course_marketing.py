#!/usr/bin/env python3
"""Build the offline Course Marketing navigator from the bilingual Markdown files."""
from html import escape
from pathlib import Path
import json
import re

from generate_webpage import parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = Path('08-ai-marketing/course-marketing')


def load_entries():
    entries = []
    for path in (ROOT / 'prompts' / COLLECTION).glob('*.md'):
        if path.name == 'README.md':
            continue
        entry = {'slug': path.stem}
        for lang, directory in [('zh', 'prompts'), ('en', 'prompts-en')]:
            source = ROOT / directory / COLLECTION / path.name
            fm, body = parse_frontmatter(source)
            prompt = re.search(r'\n## Prompt\s+```text\n(.*?)\n```\s*$', body, re.S)
            if not prompt or not fm.get('book_chapter'):
                raise ValueError(f'Invalid course prompt: {source.relative_to(ROOT)}')
            entry[lang] = {
                'title': fm['title'], 'chapter': fm['book_chapter'],
                'stage': int(fm['book_chapter'].split('.')[0]),
                'inputs': fm['inputs'], 'output': fm['output'],
                'followup': fm['followup'], 'prompt': prompt[1],
                'path': source.relative_to(ROOT).as_posix(),
            }
        if entry['zh']['chapter'] != entry['en']['chapter']:
            raise ValueError(f'Chapter mismatch: {path.name}')
        entries.append(entry)
    entries.sort(key=lambda entry: tuple(map(int, entry['zh']['chapter'].split('.'))))
    if len(entries) != 17 or len({e['zh']['prompt'] for e in entries}) != 17:
        raise ValueError('Expected 17 distinct source prompts')
    if [sum(e['zh']['stage'] == stage for e in entries) for stage in range(1, 5)] != [4, 6, 4, 3]:
        raise ValueError('Unexpected stage counts')
    return entries


def main():
    entries = load_entries()
    template = (ROOT / 'templates/course-marketing.html').read_text(encoding='utf-8')
    # Escape HTML delimiters so prompt text cannot close the JSON script element.
    data = json.dumps(entries, ensure_ascii=False).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
    fallback = '\n'.join(
        f'<details><summary>{escape(e["zh"]["chapter"] + " " + e["zh"]["title"])}</summary>'
        f'<pre>{escape(e["zh"]["prompt"])}</pre></details>' for e in entries
    )
    output = template.replace('<!-- PROMPT_DATA -->', data).replace('<!-- NO_SCRIPT_PROMPTS -->', fallback)
    target = ROOT / 'docs/course-marketing.html'
    target.write_text(output, encoding='utf-8')
    print(f'Generated {target.relative_to(ROOT)} with 17 bilingual templates (offline).')


if __name__ == '__main__':
    main()
