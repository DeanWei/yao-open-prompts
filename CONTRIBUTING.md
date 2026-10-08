# 贡献与迭代规则

## 新增提示词

1. 从 `templates/prompt-file-template.md` 复制模板。
2. 放入最匹配的 `prompts/<category>/` 目录。
3. 填写 frontmatter：`title/category/subcategory/source_section/author/version/created/status/tags`。
4. Prompt 正文只放可复制内容，教程链接、效果截图、长案例放到 `references/` 或后续案例目录。
5. 运行：

```bash
python3 scripts/check_repo.py
python3 scripts/generate_catalog.py
python3 scripts/generate_webpage.py
python3 scripts/generate_english_readmes.py
python3 scripts/generate_course_marketing.py
```

## 《课程营销学》专题维护

- 中文文件位于 `prompts/08-ai-marketing/course-marketing/`，英文文件保持相同相对路径。
- 每个文件保留 `book_chapter/inputs/output/followup` 字段，分别用于章节排序、输入说明、预期产出和可选追问。
- `templates/course-marketing.html` 是页面模板，生成脚本读取中英文 Markdown 正文，写入 `docs/course-marketing.html`。修改后提交模板、正文与生成页面。
- 保留原书章节编号。原稿 3.5 与 2.6 重复的说明见 `references/course-marketing-guide.md`，新增独立原稿时同步调整专题数量、生成校验、页面指南与目录。
- 发布前检查桌面、手机和 `file://` 离线页面的搜索、筛选、编辑、复制与下载功能。

## 提示词版本规则

- 小修文字、去冗余：`V1.0 -> V1.1`
- 明显改写结构或新增流程：`V1.x -> V2.0`
- 同一提示词不同方向的实验版：新建文件，并在标题中标注用途或模型。

## 评审标准

- 目标清楚：提示词解决的问题明确。
- 可执行：用户知道需要输入什么，模型知道需要输出什么。
- 可迁移：不要把一次性项目细节写死在通用提示词里。
- 可维护：保留版本、标签、适用场景和必要来源信息。
- 风险可控：涉及医疗、法律、金融、未成年人、第三方版权或规避检测等内容时，必须增加来源说明或评审备注。
