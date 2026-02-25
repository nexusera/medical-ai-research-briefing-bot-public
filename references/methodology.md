# 医疗 AI 研究方法论与检索策略

> [!IMPORTANT]
> **真实性红线**: 严禁编造文献、链接或虚构实验结果。研报必须是基于 **WebSearch** 与 **WebReader** 实时输出的“整理+分析”结果。

## 1. 高效搜索技巧 (Advanced Search Strategy)

### ⏱ 时间窗限制 (Time Window Constraints)
- **默认范围**：仅检索 **未来近 48 小时** 内发布或更新的内容。
- **扩展范围**：根据调研深度，最长可追溯至 **近 3 天**。
- **执行逻辑**：在搜索指令中加入 `past 2 days` 或 `after:[YYYY-MM-DD]` (今日日期减2天) 过滤标识。

### 🧬 虚拟临床试验 (In-Silico Trials)
```
("in-silico trial" OR "virtual clinical trial" OR "computational clinical trial")
AND (AI OR "machine learning" OR "deep learning")
AND (healthcare OR clinical)
```

### 🧠 医疗大模型 (Medical LLM)
```
("large language model" OR LLM)
AND (clinical decision support OR diagnosis OR EMR)
```

### 🤝 MDT / 多学科会诊 AI
```
("MDT" OR "multidisciplinary team")
AND (AI-driven OR "decision support system")
AND (oncology OR clinical pathway)
```

### 📄 OCR 噪声分析 (OCR Induced Noise in NLP)
```
("OCR error" OR "OCR noise" OR "OCR-induced noise")
AND ("NLP tasks" OR "named entity recognition" OR "information extraction")
AND (robustness OR "error correction" OR "denoising")
```

### 📄 OCR 噪声分析 (OCR Induced Noise in NLP)
```
("OCR error" OR "OCR noise" OR "OCR-induced noise")
AND ("NLP tasks" OR "named entity recognition" OR "information extraction")
AND (robustness OR "error correction" OR "denoising")
```

## 2. 深度分析与思考模型 (Thinking Model)

为了回答“新研究解决了什么、对比优劣如何”，必须锁定论文的特定部分：

### 🔍 目标锁定 (Section Targeting)
- **Introduction & Related Work (前言与相关工作)**: 锁定研究脉络（Lineage）。为了回答“这篇论文与前作的关系”，重点提取它所引用的关键前作及其指出的不足。
- **Methods (方法)**: 解决“解决了过去哪些问题”。通过对比算法参数、数据集规模，识别技术路径的演进。
- **Discussion/Limitations (讨论与局限性)**: **必看部分**。为了回答“弱点和可增强点”，直接锁定作者自述的局限性，以此推导后续的增强方向。
- **Results/Benchmarks (结果与基准)**: 为了对比优缺点，提取量化指标，并检查统计学设计的严谨性。

### 🧠 比较思维 (Comparative Logic)
- **演进分析**：深入理解当前研究是如何在某篇关键前作的基础上，解决了特定的历史难题。
- **知己知彼**：将发现的研究与“现有标准/我们目前的方法”进行对比，列出：
  - **优势互补**：它在哪些维度取得了突破？
  - **弱点识别**：它遗漏了哪些边缘场景？这正是我们可以增强的部分。

## 3. 工作流执行规范
1. **优先次序**：严格按照 `sources.md` 中的分层（Tier）进行检索。
2. **多源交叉**：针对同一个结论，必须在不同平台（如 PubMed + arXiv）寻找证据支撑。
3. **全量抓取**：不得为了简洁而遗漏窗口（48h/3d）内的任何相关论文。每一篇符合标准的研究都应被提及。
4. **精确链接**：引用的链接必须直达论文详情页（如 arXiv ID 页面或期刊官网原文页），禁止使用二次转录的模糊链接。
5. **差异分析**：明确指出研究结果与现有临床指南（Guidelines）的差异或潜在冲突。
