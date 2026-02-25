# 医疗调研结果输出格式 (Standard Output Formats)

本机器人仅支持以下两种格式。**默认模式**为“高级学术综述 (Advanced Academic)”。当执行长期跟踪或未完成调研时，需使用“研究笔记 (Research Notes)”。

> [!IMPORTANT]
> **精准链接要求**：在 `Findings` 或 `References` 等任何展现单独论文的模块中，每一篇提及的文献**必须带有指向该论文详情页的独立链接**。严禁对论文列表进行无链接的模糊概括。

---

## 🔬 1. 轨道 A: 简报模式 (Broad Synthesis - 全景脉络)
*默认模式。适用于正式研报、建立全景认知及涵盖基础与演进。*

```markdown
# 🏥 深度医学综述: [研究方向]
**日期**: YYYY-MM-DD | **覆盖**: [24h/72h/7d 或 Related-mode] | **模式**: Broad Synthesis (简报)

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

1. **[论文标题 A](必须是真实超链接)** — *作者A等* (来源: [期刊/平台], [年份])
   - **标签**: `[方向: OCR等]` `[机制: 具体方法/基线等]` `[超龄基准标注 Seminal/Baseline]`
   - **跨域科研维度**: `[Scalability: High/Med/Low]` `[Deployability: High/Med/Low]` `[Evaluation Trustworthiness: High/Med/Low]` `[Clinical Relevance: High/Med/Low]`
   - **结构化分析**: 
     - *Research Question*: [解决什么具体问题]
     - *Method / System*: [采用何种模型、系统或流程]
     - *Data / Evaluation*: [数据规模、对照、指标]
     - *Key Findings*: [明确可复述的结论]
     - *Limitations*: [作者承认的不足或隐含假设]
   - **Reusability / How to Use This Paper** *(必须回答至少 2-3 项，严禁泛泛而谈)*:
     - 可复用: [哪些模块/pipeline/评测思路可直接拿来用？]
     - 可迁移: [如果我做 X 方向，这篇能帮我省掉哪一步？]
     - 复用风险: [哪些部分与真实场景差距大？]
   - **Confidence for Research Use** *(仅限枚举)*:
     - `Safe to build upon` / `Promising but fragile` / `Exploratory only`
   - **Related Context (Non-exhaustive)** *(定位本篇在研究谱系中的位置)*:
     - Methodologically similar: [同类方法论文+年份，1句话说明差异]
     - Contrasting approach: [对立路线论文+年份，1句话说明差异]
     - Foundational reference: [奠基性基线论文+年份]
*(根据搜查结果列出其余所有篇目 2, 3, 4...)*

## 交叉分析 (Evidence-driven Synthesis)
### 同题多解 (Comparative Analysis)
[比较上述论文中“同一问题”的不同解法或架构]
### 共识与冲突 (Consensus & Contradictions)
[详细分析发现中存在的相互支持、相互矛盾之处]
### 经独立支持的模式 (Independently Supported Patterns)
[总结哪些临床/技术模式是被上述多篇论文独立验证的]

## 📝 研究笔记 (Research Notes)
### 核心认知 (Current Answer)
[针对本次检索课题得出的阶段性核心结论]
### 已确证发现 (What We Know)
- [核心发现结论] — [[来源]](链接)
### 待解问题 (Open Questions)
- [ ] [尚未找到确切答案或需要进一步验证的子问题]
### 信息源矩阵 (Sources Consulted)
| 来源 (Source) | 核心发现 (Key Finding) | 可信度 (Credibility) | 备注 (Notes) |
|--------|-------------|-------------|-------|
### 检索日志 (Search Log)
[记录 Queries 及命中情况]
### 下一步行动 (Next Steps)
[AI 或研究员后续建议行动]

## 局限性与留白 (Limitations)
[客观申明本次调研窗口内这些研究依然没有解决的问题]

## 结论与建议 (Conclusion & Next Steps)
[给出最终判断与落地建议]

## 参考文献 (References)
- [List of detailed references with exact URLs]
- **注意**: 若启用了 Related-mode 检索，必须在此处（或上方正文中）为>3年的奠基模型/基准研究明确打上 `[Seminal / Baseline]` 的标签。
- 1. *论文 A 第一作者等*, "[论文标题 A](明确的原文链接)" - DOI/arXiv ID
- 2. *论文 B 第一作者等*, "[论文标题 B](明确的原文链接)" - DOI/PMID
```

---

## ⚡ 2. 轨道 B: 近报模式 (Solution-Oriented Flash - 最优解合成)
*检索侧重短窗口近期文献，但每篇论文的分析框架与简报完全统一。在完成论文拆解后，额外输出"最优组合解决方案"。*

```markdown
# ⚡ 医学前沿近报: [研究方向]
**日期**: YYYY-MM-DD | **近期聚焦**: [24h/72h/30d] | **模式**: Solution-Oriented Flash (近报)

## 摘要 (Abstract)
[概述近期检索到的核心动态、已有思路及其潜在的最优组合方案]

## 检索策略与边界 (Methodology)
### Search Strategy
- **数据源与策略**: [记录本次检索使用的数据库及查询串]
- **时间窗口**: [设定具体短窗口时间范围，如近 30 天]
### Inclusion/Exclusion Criteria
- **入/排标准**: [具体说明哪些研究被纳入或剔除]
### Evaluation Framework
- **评估框架**: 基于证据驱动的合成 (Paper-first Synthesis)

## 核心发现 (Findings & Evidence Tagging)
*(与简报模式统一：每篇论文必须完成完整的结构化拆解)*

1. **[论文标题 A](必须是真实超链接)** — *作者A等* (来源: [期刊/平台], [年份])
   - **标签**: `[方向: OCR等]` `[机制: 具体方法/基线等]`
   - **跨域科研维度**: `[Scalability: High/Med/Low]` `[Deployability: High/Med/Low]` `[Evaluation Trustworthiness: High/Med/Low]` `[Clinical Relevance: High/Med/Low]`
   - **结构化分析**: 
     - *Research Question*: [解决什么具体问题]
     - *Method / System*: [采用何种模型、系统或流程]
     - *Data / Evaluation*: [数据规模、对照、指标]
     - *Key Findings*: [明确可复述的结论]
     - *Limitations*: [作者承认的不足或隐含假设]
   - **Reusability / How to Use This Paper** *(必须回答至少 2-3 项)*:
     - 可复用: [哪些模块/pipeline/评测思路可直接拿来用？]
     - 可迁移: [如果我做 X 方向，这篇能帮我省掉哪一步？]
     - 复用风险: [哪些部分与真实场景差距大？]
   - **Confidence for Research Use** *(仅限枚举)*:
     - `Safe to build upon` / `Promising but fragile` / `Exploratory only`
   - **Related Context (Non-exhaustive)** *(定位本篇在研究谱系中的位置)*:
     - Methodologically similar: [同类方法论文+年份，1句话说明差异]
     - Contrasting approach: [对立路线论文+年份，1句话说明差异]
     - Foundational reference: [奠基性基线论文+年份]
*(根据搜查结果列出其余所有篇目 2, 3...)*

## 最优组合解决方案 (Optimal Solution Synthesis)
*(此为近报独有模块：基于上方已拆解论文的思路，提纯成一套可行动的综合解决方案)*
### 1. 架构/方法组合 (Methodological Synergy)
- **主体框架**: [提炼自文献 A 的主干模型/方法]
- **增强模块**: [提炼自文献 B 或 C 的增强策略/约束规则]
### 2. 评测与数据策略 (Data & Evaluation Tactics)
- [提炼各文献中采用的最佳数据处理手段或评测指标]

## 📝 研究笔记 (Research Notes)
### 核心认知 (Current Answer)
[针对本次检索课题得出的阶段性核心结论]
### 已确证发现 (What We Know)
- [核心发现结论] — [[来源]](链接)
### 待解问题 (Open Questions)
- [ ] [尚未找到确切答案或需要进一步验证的子问题]
### 信息源矩阵 (Sources Consulted)
| 来源 (Source) | 核心发现 (Key Finding) | 可信度 (Credibility) | 备注 (Notes) |
|--------|-------------|-------------|-------|
### 检索日志 (Search Log)
[记录 Queries 及命中情况]
### 下一步行动 (Next Steps)
[AI 或研究员后续建议行动]

## 方案局限性评估 (Vulnerability Check)
[基于各篇论文的 Limitations 综合分析这套组合方案潜在的失效点]

## 结论与建议 (Conclusion & Next Steps)
[给出最终判断与落地建议]

## 参考文献 (References)
- 1. *作者等*, "[标题 A](链接)" - DOI/ID (提供主体框架)
- 2. *作者等*, "[标题 B](链接)" - DOI/ID (提供增强模块)
```

---

## 📝 3. 研究笔记 (Research Notes)
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
