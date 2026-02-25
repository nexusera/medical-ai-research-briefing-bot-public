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

## 工作流概览 (Workflow Overview)

本技能遵循四阶段调研流程：

```
阶段 1: 专业信息采集
  ├─ 检索优先级最高的医学期刊 (Tier 1)
  ├─ 查询技术类预印本 (arXiv/MedRxiv)
  └─ 获取工业界实验室动态 (Google/NVIDIA/MSFT)
      ↓
阶段 2: 证据筛选
  ├─ 基于临床有效性（Clinical Validity）进行加权
  └─ 剔除低信号或纯商业宣传内容
      ↓
阶段 3: 领域知识合成
  └─ 整合文本、图像及结构化数据洞察
      ↓
阶段 4: 结果生成
  ├─ 按照请求的方向生成独立研报
  └─ **必须包含窗口内所有相关论文，禁止忽略任何高质量来源**
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
1. **全量覆盖**: 必须列出搜索结果中匹配时间窗口（48h/3d）的**所有**相关论文。
2. **精确溯源**: 每一条研究必须带有**原文标题**作为二级/三级标题，并紧随其后提供**原文链接**。
3. **关键证据**: 基于 `methodology.md`，深度分析每篇论文的演进脉络与技术弱点。

### 默认报告模板 (深度学术综述):

```markdown
# 🏥 深度医学综述: [方向]
## 摘要 (Abstract)
[概述研究问题、方法、主要发现及结论]

## 检索策略 (Search Methodology)
[使用的数据库、布尔查询串、日期范围]

## 技术深度调研 (In-depth Findings)
### [技术方向 A]
[基于 Methods 部分的深度分析与量化数据对比]

## 临床证据质量评价 (Evidence Quality)
[偏倚风险评估、FDA/NIH 相关监管政策对标]

## 讨论与结论
[技术脉络总结、未来可增强方向的详细推导]

## 参考文献 (References)
[详尽的索引列表]
```

## 自定义深度与格式 (Customization)

用户可以要求不同的深度级别：
- **简报/快报 (Brief)**：使用 `Executive Briefing` 格式，只看核心价值。
- **标准 (Standard)**：标准晨报格式，包含技术脉络与优劣思考。
- **综述 (Comprehensive)**：**默认选项**，使用 `Academic` 格式，包含完整的方法论与偏倚分析。
- **草稿 (Working Notes)**：适合内部查看检索日志。

---

## 使用方法 (Usage)

### 手动执行
直接输入关键词或自然语言即可。

### 定时任务配置 (Cron / Scheduled Push)
在定时任务的 `payload.message` 中，建议使用：

> **推荐指令**：`请使用 medical-ai-research 技能，针对 [方向] 执行 [近48小时/近3天] 的深度研报播报，并将结果发送到当前频道。`

## 故障与降级
- 医疗顶刊抓取失败时，会自动降级至 `MedRxiv` 或 `BioRxiv` 等预印本平台。
- 若所有实时源不可达，将基于已有知识库生成“近期重点回顾”。

---

*参考文件: `methodology.md`, `sources.md`, `output-formats.md`, `example.md`*
