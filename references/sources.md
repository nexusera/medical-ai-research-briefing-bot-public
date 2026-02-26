# Medical AI Research Briefing – Sources Configuration

本文件定义 Medical AI Research Briefing Bot 的**唯一信息源配置**。
遵循原则：**信噪比优先、前沿优先、临床合法性分层确认**。

---

## Global Rules

* 权重（weight）范围：1–10，越高代表越优先
* 预印本用于"前沿捕捉"，期刊用于"结论确认"
* 不在本文件中的来源，默认不抓取

---

## 0. Mandatory Execution Protocol: Matrix Search & Deduplication

**⚠️ 强制全源地毯式检索与去重 (Exhaustive Matrix Search)**
* **平行查询拦截 (No Short-Circuit)**: 严禁使用单一 `site:` 过滤词一次性完成检索或搜到几篇就停止。必须**并发或循环调用** WebSearch，确保【预印本阵地 (arXiv/medRxiv)】和【权威期刊阵地 (PubMed/Nature等)】都被独立覆盖。
* **跨库身份识别与去重 (Cross-Database Deduplication)**: 合并阶段必须自我审视。若预印本文献已在期刊发表（作者与核心机制高度重合），**严禁分列两条**，必须强行合并为一张 Paper Card。格式标定为：`来源: [期刊名/PubMed] 首发于 [预印本库]`。

## 0.5. Source-Specific Extraction Tactics

* **Tactic 1: Pre-prints (arXiv / medRxiv)**
    * *主攻*: 最新算法架构、开源代码/权重、数据集清洗脚本。
    * *捷径*: 直接正则扫描首尾 `github.com` 等链接及 `Implementation Details` 锁定 ✅ `What you can reuse`。在 `Our Contributions` 抓取 `Core contribution`。
* **Tactic 2: Medical Databases (PubMed)**
    * *主攻*: 结构化定量数据与试验结果。
    * *捷径*: 跳过铺垫，锁定 `RESULTS:` 标签获取 `Key Evidence` (如 F1, CI)。看 `CONCLUSIONS:` 最后一句提炼 `Verdict`。
* **Tactic 3: Top Tier Journals (Nature / The Lancet etc.)**
    * *主攻*: 真实世界缺陷与批判性评价。
    * *捷径*: 直接拉到底部 `Discussion / Limitations` 抓取最致命的 ⚠️ `Failure boundary`。读 `Introduction` 末段抓取 `Why you should care`。

---

## I. MDT（多学科会诊 / 临床决策支持）

### Primary Sources

* name: PubMed
  url: https://pubmed.ncbi.nlm.nih.gov/
  weight: 10
  role: 临床最终确认层

* name: medRxiv
  url: https://www.medrxiv.org/
  weight: 8
  role: 新型 MDT 系统与临床决策方法首发

### Secondary Sources

* name: AMIA Proceedings
  url: https://amia.org/education-events/amia-conferences
  weight: 6
  role: 医疗信息学会议论文

### Search Template (MDT)

* "multidisciplinary team"
* "clinical decision support system"
* "AI-assisted MDT"
* "multidisciplinary oncology decision"

---

## II. In-silico Trial / 计算临床试验

### Primary Sources

* name: medRxiv
  url: https://www.medrxiv.org/
  weight: 9
  role: 虚拟临床试验与真实世界证据前沿

* name: arXiv
  url: https://arxiv.org/
  weight: 9
  categories: [stat.ML, cs.LG, cs.AI]
  role: 建模、仿真、因果推断方法

### Secondary Sources (Journals)

* name: Nature Digital Medicine
  url: https://www.nature.com/natdigimed/
  weight: 7

* name: npj Digital Medicine
  url: https://www.nature.com/npjdigitalmed/
  weight: 7

* name: Statistics in Medicine
  url: https://onlinelibrary.wiley.com/journal/10970258
  weight: 6

### Search Template (In-silico Trial)

* "in silico trial"
* "virtual clinical trial"
* "digital twin healthcare"
* "treatment policy simulation"
* "causal inference clinical trial"

---

## III. Medical Large Language Models（医疗大模型）

### Primary Sources

* name: arXiv
  url: https://arxiv.org/
  weight: 10
  categories: [cs.CL, cs.LG, cs.AI]
  role: 医疗大模型首发源

### Secondary Sources

* name: bioRxiv
  url: https://www.biorxiv.org/
  weight: 7
  role: 模型评测、安全性与医学验证

### Conference Sources

* name: NeurIPS
  url: https://papers.nips.cc/
  weight: 8

* name: ICML
  url: https://proceedings.mlr.press/
  weight: 8

* name: ICLR
  url: https://openreview.net/group?id=ICLR.cc
  weight: 8

* name: ACL / EMNLP
  url: https://aclanthology.org/
  weight: 7

### Journal Confirmation

* name: Nature Medicine
  url: https://www.nature.com/nm/
  weight: 6

* name: The Lancet Digital Health
  url: https://www.thelancet.com/journals/landig
  weight: 6

* name: JAMIA
  url: https://academic.oup.com/jamia
  weight: 6

### Search Template (Medical LLM)

* "clinical large language model"
* "medical foundation model"
* "LLM for electronic health records"
* "multimodal medical AI"
* "clinical NLP transformer"

---

## IV. Global De-noising Rules

### Prefer

* 多中心 / 多机构数据
* 明确实验设计与对照
* 有消融或误差分析

### Deprioritize

* 单中心小样本 + 无对照
* 概念性或 marketing 式论文
* 无真实医疗数据验证的 demo

---

## V. Unified Crawling Priority

执行顺序（从高到低）：

1. arXiv
2. medRxiv
3. PubMed
4. Top Conferences
5. Top Journals

---

## End of Sources Configuration
