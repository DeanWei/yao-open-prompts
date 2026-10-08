# Release Checklist

- [ ] 确认仓库名、简介、许可证。
- [ ] 确认 `third-party-review` 文件是否发布，或移至 references。
- [ ] 运行 `python3 scripts/check_repo.py`。
- [ ] 运行 `python3 scripts/generate_catalog.py`。
- [ ] 运行 `python3 scripts/generate_webpage.py`。
- [ ] 运行 `python3 scripts/generate_english_readmes.py` 与 `python3 scripts/generate_course_marketing.py`。
- [ ] 检查《课程营销学》专题的中英文入口、移动端、复制下载与离线使用。
- [ ] 检查 `CATALOG.md` 链接。
- [ ] 检查 `docs/index.html` 页面渲染。
- [ ] 更新 `CHANGELOG.md`。
- [ ] 打 tag，建议格式：`vYYYY.MM.N`。
- [ ] 发布后检查 GitHub README 和目录链接渲染。
