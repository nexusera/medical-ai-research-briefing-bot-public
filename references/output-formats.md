# 医疗调研结果输出格式 (Standard Output Formats)

本机器人仅支持以下两种格式。**默认模式**为“高级学术综述 (Advanced Academic)”。当执行长期跟踪或未完成调研时，需使用“研究笔记 (Research Notes)”。

> [!IMPORTANT]
> **精准链接要求**：在 `Findings` 或 `References` 等任何展现单独论文的模块中，每一篇提及的文献**必须带有指向该论文详情页的独立链接**。严禁对论文列表进行无链接的模糊概括。

---

## 🔬 1. 高级学术综述 (Advanced Academic) 
*默认模式。适用于正式研报、关键决策及全量播报。*

```markdown
# 🏥 深度医学综述: [研究方向]
**日期**: YYYY-MM-DD | **覆盖**: [24h/72h/7d] | **模式**: Advanced Academic

## 摘要 (Abstract)
[完整概述检索到的核心动态、主要方法、核心发现及对该领域的影响结论]

## 检索策略与边界 (Methodology)
### Search Strategy
- **数据源与策略**: [记录本次检索使用的数据库及查询串]
- **时间窗口**: [设定具体时间范围。若启用 Related 检索则标明 "Related-mode" 并写出"近 3 年优先"约束。]

### Inclusion/Exclusion Criteria
- **入/排标准**: [具体说明哪些研究被纳入或剔除]

### Evaluation Framework
- **评估框架**: 基于证据驱动的合成 (Paper-first Synthesis: 结构化分析、严格标签化、跨论文对齐)

## 核心发现 (Findings & Evidence Tagging)
*(不预先设定主题簇，直接进行单篇论文的五要素拆解)*

1. **[论文标题 A](必须是真实超链接)** (来源: [期刊/平台])
   - **标签**: `[方向: OCR等]` `[机制: 具体方法/基线等，超龄基准需标注 Seminal/Baseline]`
   - **结构化分析**: 
     - *Research Question*: [解决什么具体问题]
     - *Method / System*: [采用何种模型、系统或流程]
     - *Data / Evaluation*: [数据规模、对照、指标]
     - *Key Findings*: [明确可复述的结论]
     - *Limitations*: [作者承认的不足或隐含假设]
*(根据搜查结果列出其余所有篇目 2, 3, 4...)*

## 交叉分析 (Evidence-driven Synthesis)
### 同题多解 (Comparative Analysis)
[比较上述论文中“同一问题”的不同解法或架构]
### 共识与冲突 (Consensus & Contradictions)
[详细分析发现中存在的相互支持、相互矛盾之处]
### 经独立支持的模式 (Independently Supported Patterns)
[总结哪些临床/技术模式是被上述多篇论文独立验证的]

## 局限性与留白 (Limitations)
[客观申明本次调研窗口内这些研究依然没有解决的问题]

## 结论与建议 (Conclusion & Next Steps)
[给出最终判断与落地建议]

## 参考文献 (References)
- [List of detailed references with exact URLs]
- **注意**: 若启用了 Related-mode 检索，必须在此处（或上方正文中）为>3年的奠基模型/基准研究明确打上 `[Seminal / Baseline]` 的标签。
- 1. *论文 A 第一作者等*, "[论文标题 A](明确的原文链接)" - DOI/arXiv ID
- 2. *论文 B 第一作者等*, "[论文标题 B](明确的原文链接)" - DOI/PMID

---
## 研究与追踪总结 (Research Tracking)

### 已确证发现 (What We Know)
- [核心发现结论] — [[来源]](链接)

### 待解问题 (Open Questions)
- [ ] [该领域/方向仍然未解决的关键问题]
- [ ] [需要进一步临床试验验证的假设]

### 信息源矩阵 (Sources Consulted)
| 来源 (Source) | 核心发现 (Key Finding) | 可信度 (Credibility) | 备注 (Notes) |
|--------|-------------|-------------|-------|
| [[期刊/平台名]](平台链接) | [简述该平台贡献的核心信息] | [High/Medium/Low] | [如：高等级 RCT 证据] |
```

---

## 📝 2. 研究笔记 (Research Notes)
*适用于追踪中的长线课题、尚需进一步核实的信息，或“无新增”时期的情况梳理。*

```markdown
# [研究方向/具体主题] — Research Notes

**Status:** [In progress / Complete / Needs more]
**Last updated:** [YYYY-MM-DD]
**Confidence:** [High / Medium / Low]

## 核心认知 (Current Answer)
[针对当前课题，目前得出的最佳、最可靠的阶段性结论]

## 已确证发现 (What We Know)
- [核心发现结论 A] — [来源与链接] — [置信度: High]
- [核心发现结论 B] — [来源与链接] — [置信度: Medium]

## 待解问题 (Open Questions)
- [ ] [尚未找到确切答案的子问题]
- [ ] [发现了线索但亟需通过其他来源（如需 PubMed 确认的 arXiv 文章）进行 Verification 的点]

## 信息源矩阵 (Sources Consulted)
| 来源 (Source) | 核心发现 (Key Finding) | 可信度 (Credibility) | 备注 (Notes) |
|--------|-------------|-------------|-------|
| [[平台名](链接)] | [简述] | [High/Mid/Low] | [如：需要等待同行评审] |

## 检索日志 (Search Log)
[记录尝试了哪些 Queries，哪些返回了噪音，哪些成功命中了信号]

## 下一步行动 (Next Steps)
[为了完善这份笔记，AI 或人类研究员接下来应该采取什么行动？如：需等待下周某学术会议发布最终 Proceeding]
```
