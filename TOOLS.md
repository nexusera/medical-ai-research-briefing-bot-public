# 工具使用真相 (Tool Use Ground Truth)

技能唯一依赖且授权的外部数据入口：`scripts/academic_fetcher.py` (纯 Python 零 API-Key 跨库检索引擎)

## 本地爬虫引擎使用指南 (academic_fetcher.py)
1. **多层查准逻辑**:
   - 必须通过 `academic_fetcher.py` 一次性并发聚合来自权威信息源（arXiv, medRxiv, PubMed, PMC, Nature, NEJM 等 Europe PMC 索引库）的学术原件。
   - 遇到学术界黑话或新型专有缩写，必须在 Query 中加上原名词的变体展开形。
2. **绝对禁用旧版 WebSearch**:
   - 严禁调用内置的商业版 `WebSearch` 工具（会触发 API Key 缺失或限流的幻觉报错）。
   - 任何需要向外求索的时刻，只能使用：`python scripts/academic_fetcher.py "your boolean query" --max 10`。
3. **相关模式软性回溯 (Related Strategy)**:
   - 如果用户的 Query 包含“对比基线”、“近年代表作”、“脉络”等词态，大模型在阅读爬虫返回的代码时必须自行筛除低价值小文章。
   - 转移到“按相关性与来源权重排序”，且针对大龄基准模型（>3年前），在返回时自行打上 `[Seminal / Baseline]` 标签。
