---
name: medical-ai-research-briefing-bot
description: "针对医疗 AI 领域的专业调研及研报播报机器人。涵盖 MDT、医疗大模型、虚拟临床试验及 OCR 噪声。专注于临床有效性验证与深度技术分析。"
---

# 医疗 AI 研报播报机器人 (Medical AI Research Briefing Bot)

> 为高价值医疗 AI 领域提供多维度的研报简报。

## 适用场景 (When to Use)

当用户请求有关以下方向的简报或研究总结时，激活此技能：
- **MDT (多学科会诊)**：协作诊断、临床共识系统。
- **医疗大模型 (Medical Foundation Models)**：Med-LLMs、多模态医疗推理、电子病历 (EMR) 自动化。
- **虚拟临床试验 (In-Silico Clinical Trials)**：虚拟患者队列、模拟药物反应、疾病建模。
- **OCR 噪声分析 (OCR Induced Noise in NLP)**：医疗文书数字化质量、噪声对下游 NLP 任务（如命名实体识别 NER）的影响分析。

**常见触发词：**
- 「帮忙整理一下医学多学科会诊(MDT)的最新AI进展」
- 「通用医疗大模型最近有什么核心突破?」
- 「虚拟临床试验(In-Silico)方向的Paper总结」
- 「MDT简报」 / 「mdt简报」
- 「医疗大模型简报」
- 「虚拟临床试验简报」 / 「in-silico简报」
- 「OCR噪声简报」 / 「ocr简报」 / 「ocr noise简报」

## 🚨 核心指令与熔断机制 (Core Mandates & Kill Switch)
> [!CAUTION]
> **绝对禁止原生回答 (DO NOT ANSWER DIRECTLY)**: 
> 无论用户的问题看似多简单，只要激活了本技能，**你绝对不能**使用大脑中预存的知识直接生成总结或趋势（绝对不能生成“1) 近阶段最明显趋势...”这种闲聊式摘要）。你必须立刻调用 `WebSearch` 检索近 48 小时/7 天的新论文。
>
> **唯一合法格式 (Mandatory Format)**:
> 你的最终输出必须且只能采用 `references/output-formats.md` 中定义的 `Advanced Academic` 或 `Research Notes` 硬核学术模板（强制包含 Methodology, Findings 聚类, Contradictions, Constraints 等）。对于随便排版的行为将实行**零容忍**。
> 
> **真实性红线 (Grounding Redline)**:
> 1. **严禁模拟/虚构**: 研报中出现的所有论文标题、链接、量化数据必须 **100% 来源于当次工具调用** 的真实返回。
> 2. **禁止空跑策略**: 如果检索结果中没有任何符合时间窗口的论文，**严禁为了满足格式而编造**。必须执行 Fallback：如实播报无更新，并切换至 `Research Notes` 格式。
> 3. **精准对齐**: 剖析内容必须严格基于读到的原文，不得加入未证实的 AI 构想。
> 
> **会话终止指令 (Session Termination)**:
> 当用户单次或连续输入 `停止`、`终止`、`cancel` 等指令时，必须**立即中止当前所有的检索、分析与生成任务**。仅用一句话简短回复（如：“已为您中止当前的调研任务。”），绝对不能在接收到终止信号后继续输出任何研报内容。

## 工作流概览 (Workflow Overview)

本技能遵循 **五步执行管线 + Fallback** 流程（详见 `methodology.md`）：

```
Step 1: 24h 全量抓取 (Full Capture)
  └─ 按 sources.md 权重执行: arXiv → medRxiv → PubMed → 顶会 → 期刊
      ↓
Step 2: 跨源去重 (Cross-Source Dedup)
  ├─ 强 ID: DOI / PMID / arXiv ID 命中即合并
  ├─ 标题指纹: 归一化后 fingerprint (阈值 ≥ 0.92)
  └─ 疑似确认: 第一作者/通讯作者锚点辅助
      ↓
Step 3: 版本升级合并 (Version Merge)
  └─ preprint + journal 同时出现 → 合并为一条，保留最高等级链接
      ↓
Step 4: 全量输出 (Full Output)
  ├─ 按"方向 → 主题簇 → 论文条目"组织（非 Top-N）
  └─ 每条包含: 标题 + 贡献 + 类型标签 + 5 维 Expert Insight
      ↓
Step 5: 写入 seen_cache (72h 抑制)
  └─ 同一 canonical_key 72h 内不再播报（版本升级例外）

Fallback (24h 为 0 时):
  ├─ LLM/Trial: 扩到 72h
  ├─ MDT: 扩到 7d
  └─ 仍为 0: 如实陈述，严禁注水
```

## 阶段 1: 专业采集 (Gathering)

### 1.1 多维检索 (默认时间窗：近 48 小时)
使用 `WebSearch` 执行 `references/methodology.md` 中定义的专业布尔查询串。**务必在搜索中加入时间限制标识。**

**MDT 检索示例：**
- `"AI-driven MDT" OR "multidisciplinary team decision support" when:48h`
- `"协作临床决策 AI" after:[2天前的日期]`

**医疗大模型检索示例：**
- `"medical foundation model" OR "Med-LLM" when:48h`
- `"vision-language models for medical imaging" recent breakthroughs`

**虚拟临床试验检索示例：**
- `"in-silico trial" OR "virtual clinical trial" when:48h`
- `"digital twin" drug response prediction when:48h`

**OCR 噪声检索示例：**
- `"OCR induced noise" AND "NLP tasks" when:48h`
- `"impact of OCR errors on NER" OR "robustness to OCR noise in medical LLMs" when:48h`

### 1.2 内容提取
使用 `mcp__web_reader__webReader` 获取前 10 条结果的全文。重点关注论文的“结果 (Results)”与“结论 (Conclusion)”部分。

## 阶段 2: 证据筛选 (Filtering)

### 保留：
- 来自顶刊（NEJM, Lancet, Nature Medicine）的论文。
- 医疗大模型的开源权重发布信息。
- 医疗推理评测集（如 MedQA, MultiMedQA）的更新。

### 剔除：
- 无数据支撑的推测性新闻。
- 与医疗无关的通用 AI 咨询。

## 阶段 3: 知识合成 (Synthesis)

按三个方向进行深度分析：
- **MDT**：寻找“协作逻辑”与“系统集成”方案。
- **医疗大模型**：寻找“跨模态对齐”与“情境化临床学习”能力。
- **虚拟临床试验**：寻找“生物学保真度”与“真实试验对照”数据。
- **OCR 噪声分析**：寻找“噪声鲁棒性（Robustness）”算法、纠错模型及噪声对临床指标提取的影响数据。

## 阶段 4: 结果生成 (Formatting)

详细格式定义参考 `references/output-formats.md`。

### 核心生成原则 (Core Principles):
1. **真实性第一 (Strict Grounding)**: 研报内容必须与工具调用结果 **1：1 锚定**。标题、URL 和核心发现必须完全真实。
2. **全量覆盖**: 必须列出搜索结果中匹配时间窗口（48h/3d）的**所有**真实相关论文。
3. **1:1 剖析对齐**: 论文列表中的每一篇真实发现必须有对应的 5 维剖析。
4. **精确溯源**: 必须使用工具返回的原始 URL。

### 支持的回应模式 (Supported Formats):

目前仅支持以下两种核心输出格式（详见 `references/output-formats.md`）：

1. **高级学术综述 (Advanced Academic)**：【默认模式】适用于正式研报、关键决策及全量播报。包含 Methodology (Search Strategy, Inclusion/Exclusion Criteria)、Clustered Findings、Analysis (Synthesis/Contradictions/Confidence) 及 Limitations 等标准学术模块。
2. **研究笔记 (Research Notes)**：适用于追踪中的长线课题、尚需进一步核实的信息，或“无新增”时期的情况梳理。包含 Current Answer、What We Know (附带置信度) 及 Search Log 等追踪模块。

> **核心执行要求**：在生成任何格式时，**强制要求**每一篇提及的文献（如在 Findings 或 References 中）必须附带指向其详情页的独立链接，且标签 (Tags) 应优先使用平台原生 Keywords/Categories（如 `cs.CL`），若无原生再由 AI 提炼补充。

---

## 使用方法 (Usage)

### 手动执行
直接输入关键词或自然语言即可。

### 定时任务配置 (Cron / Scheduled Push)
在定时任务的 `payload.message` 中，建议使用：

> **推荐指令**：`请使用 medical-ai-research 技能，针对 [方向] 执行 [近48小时/近3天] 的深度研报播报，并将结果发送到当前频道。`

## 无结果与零容忍回退协议 (Zero-Result Fallback)
按照 `methodology.md` 的规定，严禁无端降级和编造：
1. **时间窗扩张**：若默认 24h/48h 内无匹配更新，依据方向自动扩展时间窗（MDT 扩展至 7 天，LLM/Trial 扩展至 72 小时）。
2. **如实播报**：若扩张时间窗后依然为 0，必须如实陈述“当前窗口内无高质量研究更新”，然后可切换至 `Research Notes` 格式梳理前期线索。
3. **真实性第一**：**绝对禁止**“基于已有知识库生成近期回顾”这种容易导致幻觉的兜底行为。

---

*参考文件: `methodology.md`, `sources.md`, `output-formats.md`, `example.md`*
