# 医疗 AI 研究方法论与执行管线 (Pipeline & Methodology)

> [!IMPORTANT]
> **真实性红线**: 严禁编造文献、链接或虚构实验结果。研报必须是基于 **WebSearch** 与 **WebReader** 实时输出的"整理+分析"结果。

---

## 主流程：24h 全量新增 → 去重 → 梳理（默认模式）

### Step 1: 抓取候选集合 (24h Full Capture)

按 `sources.md` 的 Unified Crawling Priority **全量抓取**：

**执行顺序**: arXiv → medRxiv → PubMed → 顶会论文集 → 期刊

- 时间窗以**平台的公开时间**为准（posted / published / online date）
- 默认窗口：**过去 24 小时**
- 使用 `sources.md` 中对应方向的 Search Template 构建布尔查询

### Step 2: 跨源去重 (Cross-Source Dedup)

由于同一研究可能同时出现在 arXiv + PubMed 等多个平台，需按强 ID 进行去重：

| 层级 | 方法 | 规则 |
|------|------|------|
| **强 ID** | DOI / PMID / arXiv ID | 命中即合并 |

### Step 3: 版本升级合并 (Version Upgrade Merge)

同一研究在 24h 内同时出现 preprint + journal/PMID 版本时：
- **合并为一条记录**（不重复播报）
- **保留最高等级版本链接**：期刊 > 会议 > 预印本
- 在条目中标注："✅ 已出现期刊/PMID/DOI（版本升级）"

### Step 4: 全量输出 (Full Output - 非 Top-N)

输出按 **"方向 → 主题簇 → 论文条目"** 组织，而不是按来源堆列表。

每条至少包含：
1. **标题 + 一句话贡献** (Headline)
2. **来源与链接**（保留最高等级版本）
3. **研究类型标签**：`benchmark` / `RCT` / `causal` / `agent` / `multimodal` / `dataset` …
4. **5 维 Expert Insight**：主题关联、痛点解决、优缺点、现有对比、改进建议

### Step 5: 写入 seen_cache (72h 抑制)

**目的**：防止连续两天播报同一批论文（arXiv daily batch 特别容易重复）。

| 参数 | 值 | 说明 |
|------|------|------|
| `SUPPRESS_WINDOW_HOURS` | 72 | 同一 canonical_key 72h 内不再播报 |
| `MAX_ITEMS_PER_DIRECTION` | 50 | 单方向防爆上限，全量不设总上限 |

**例外**：如果同一研究在抑制窗口内出现"版本等级提升"（如 preprint → journal），仍可再次播报并标注升级。

---

## Fallback：24h 为 0 时的明确处理策略

> 严禁为满足格式而灌水或编造。

### Fallback A：扩大窗口但保持"新增"语义（推荐默认）

| 方向 | 扩展窗口 | 理由 |
|------|----------|------|
| 医疗大模型 / 计算临床试验 | 72h | 方法快迭代，3 天仍有时效 |
| MDT | 7d | 临床验证周期长，一周内仍有参考价值 |

**输出开头必须明确标注**：
> ⚠️ 近 24h 无新增，以下为近 72h（或 7d）更新。

### Fallback B：无任何结果

如果扩展窗口后仍为 0：
- 如实陈述："在过去 [72h/7d] 内未检索到符合质量要求的最新研究"
- 可输出该方向的"当前研究热点概览"或"待关注事件"（如即将截稿的共享任务）
- **严禁虚构论文或注水**

---

## 布尔查询模板 (Search Templates)

### 🤝 MDT / 多学科会诊 AI
```
("MDT" OR "multidisciplinary team")
AND (AI-driven OR "decision support system")
AND (oncology OR clinical pathway)
```

### 🧠 医疗大模型 (Medical LLM)
```
("large language model" OR LLM)
AND (clinical decision support OR diagnosis OR EMR)
```

### 🧬 虚拟临床试验 (In-Silico Trials)
```
("in-silico trial" OR "virtual clinical trial" OR "computational clinical trial")
AND (AI OR "machine learning" OR "deep learning")
AND (healthcare OR clinical)
```

### 📄 OCR 噪声分析 (OCR Induced Noise in NLP)
```
("OCR error" OR "OCR noise" OR "OCR-induced noise")
AND ("NLP tasks" OR "named entity recognition" OR "information extraction")
AND (robustness OR "error correction" OR "denoising")
```

---

## 深度分析模型 (Thinking Model)

### 🔍 目标锁定 (Section Targeting)
- **Introduction & Related Work**: 锁定研究脉络（Lineage），提取关键前作及其不足。
- **Methods**: 对比算法参数、数据集规模，识别技术演进。
- **Discussion/Limitations**: **必看**。锁定作者自述的局限性，推导增强方向。
- **Results/Benchmarks**: 提取量化指标，检查统计学严谨性。

### 🧠 比较思维 (Comparative Logic)
- **演进分析**：当前研究如何在前作基础上解决了特定历史难题。
- **优势互补**：它在哪些维度取得了突破？
- **弱点识别**：它遗漏了哪些边缘场景？这是可增强的部分。

---

## 全局降噪规则 (Signal-to-Noise Rules)

### ✅ 优先收录 (Signals)
1. **多机构数据**: 跨中心验证具有更高置信度。
2. **明确实验设计**: 有对照组或消融实验。
3. **量化临床指标**: 必须提供具体数值。

### ❌ 降级或忽略 (Noise)
1. **单中心小样本**: 无外部验证且样本量不足。
2. **纯概念讨论**: 缺乏代码或实证的 Vision 类文章。
3. **Marketing 宣传**: 缺乏方法论透明度的商业推销。

---

## 工作流执行规范
1. **优先次序**：严格按照 `sources.md` 中的权重（weight）进行检索。
2. **多源交叉**：同一结论必须在不同平台寻找证据支撑。
3. **全量抓取**：不得遗漏窗口内任何符合标准的研究。
4. **精确链接**：必须直达论文详情页，禁止二次转录链接。
5. **差异分析**：指出研究结果与现有临床指南的差异或冲突。
