# 医疗 AI 研报专用信息源 (High-Fidelity Sources)

## ⚖️ 总体原则 (General Principles)
- **预印本优先于期刊延迟**：在 LLM 与 Trial 方向，确保时效性（Speed）。
- **顶会/顶刊优先于普通期刊**：确保信噪比（SNR）。
- **医学方向**：临床合法性 (Clinical Validity) > 方法新颖性。
- **AI 方向**：方法新颖性 > 临床落地。

---

## 🔗 一、MDT (多学科会诊 / 临床决策支持)
### 一级优先 (Tier 1 - 必须先查)
- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/ (临床“最终裁决层”)
    - *检索重点*: `multidisciplinary team AND (AI OR decision support)`
    - *排序*: 系统综述 / 指南 / 前瞻性研究 > 回顾性研究。

### 二级优先 (Tier 2 - 前沿探索)
- **medRxiv**: https://www.medrxiv.org/ (新 MDT 系统、AI 辅助决策)
    - *过滤规则*: 排除无真实临床数据、仅谈概念的文章。

### 优先级总结: `PubMed > medRxiv > 会议`
*原因：MDT 方案若不进入同行评审期刊，其实操参考价值极低。*

---

## 🔗 二、计算临床试验 / 虚拟临床试验 (In-silico Trial)
### 一级优先 (Tier 1 - 分秒必争)
- **medRxiv**: 针对 `in silico trial`, `virtual clinical trial`, `digital twin`。
    - *强过滤*: 必须有 Simulation / RWE / Causal 设计。
- **arXiv**: https://arxiv.org/ (分类: stat.ML, cs.LG, cs.AI)
    - *关注*: Causal inference, treatment policy, trial simulation.

### 二级优先 (Tier 2 - 方法积淀)
- **Nature Digital Medicine** / **npj Digital Medicine**
- **Statistics in Medicine**

### 三级优先 (Tier 3 - 方法论会议)
- **NeurIPS / ICML / AAAI**
- **ISPOR** (侧重 RWE 方向)

### 优先级总结: `medRxiv ≈ arXiv > 顶会 > 期刊`
*原因：虚拟临床试验是方法论快速演进领域，预印本是主战场。*

---

## 🔗 三、医疗大模型 (Clinical LLM / Foundation Models)
### 一级优先 (Tier 1 - 绝对核心)
- **arXiv**: (分类: cs.CL, cs.LG, cs.AI)
    - *强制关键词*: `clinical LLM`, `medical foundation model`, `EHR/EMR automation`.

### 二级优先 (Tier 2 - 医学验证)
- **bioRxiv**: 重点看：评测、Benchmark、Bias 及安全性研究。

### 三级优先 (Tier 3 - 顶会/顶刊执行确认)
- **顶会**: NeurIPS, ICML, ICLR, ACL, EMNLP。
- **顶刊**: Nature Medicine, The Lancet Digital Health, JAMIA。

### 优先级总结: `arXiv > 顶会 > 期刊`
*原因：大模型创新几乎 90% 优先在 arXiv 亮相。*

---

## 🛡️ 跨方向统一“降噪规则” (Signal-to-Noise Rules)
### ✅ 优先收录 (Signals)
1. **多机构数据**: 证明了泛化能力。
2. **明确实验设计**: 有对照组 (Control) 或消融实验 (Ablation)。
3. **临床有效性**: 提供了量化的临床指标（如 F1, AUC, CER 降低）。

### ❌ 降级或忽略 (Noise)
1. **单中心小样本**: 无外部验证且样本量不足。
2. **纯概念讨论**: 缺乏代码或实证数据的“Vision”类稿件。
3. **Marketing 式宣传**: 缺乏方法论透明度的商业“赋值”论文。

---

## 🚀 全局检索执行顺序 (Execution Flow)
本项目遵循 **“预印本抓前沿，期刊做确认，会议判方法价值”** 的原则，Clawdbot 自动执行逻辑：
1. **arXiv** (LLM / 方法创新捕获)
2. **medRxiv** (医疗方法 / Trial / MDT 捕获)
3. **PubMed** (临床合法性确认)
4. **顶会论文集** (深度贡献评估)
5. **顶级期刊** (加权背书确认)
