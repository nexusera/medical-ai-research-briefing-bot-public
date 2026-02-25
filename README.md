# 医疗 AI 研报播报机器人 / Medical AI Research Briefing Bot

针对 MDT、医疗大模型、虚拟临床试验、OCR 噪声四个专业方向的研报技能。支持**简报 (Broad Synthesis)** 与 **近报 (Solution-Oriented Flash)** 双轨输出。**完全符合 Clawdbot 高级学术标准。**

---

## 1. 安装 (Install)

将本目录整体拷贝到你的 Clawdbot workspace 的 `skills/` 目录下：
```text
<workspace>/skills/medical-ai-research-briefing-bot/
├── README.md
├── SKILL.md
├── _meta.json
├── references/
│   ├── methodology.md   (方法论)
│   ├── sources.md       (信息源)
│   ├── output-formats.md (输出格式)
│   └── example.md       (使用示例)
└── scripts/
    ├── run_briefing.sh  (运行脚本)
    └── feishu_push.py   (飞书推送脚本)
```

## 2. 运行 (Run)

### 手动触发 (Manual Trigger)
用户可以直接发送简单的关键词：
- `MDT 简报` / `mdt简报` — 触发 Broad Synthesis 模式
- `医疗大模型简报` — 触发 Broad Synthesis 模式
- `虚拟临床试验简报` / `in-silico简报` — 触发 Broad Synthesis 模式
- `OCR 噪声简报` / `ocr简报` — 触发 Broad Synthesis 模式
- `MDT 近报` / `医疗大模型近报` — 触发 Solution-Oriented Flash 模式
- 或者使用自然语言：「帮我做一份 MDT 的每日研报」/「最新思路综合我要一份近报」

### 定时推送 (Cron / Scheduled Push)
在 OpenClaw/Clawdbot 定时任务中，建议将 `payload.message` 设为：

> **推荐指令**：`针对 [方向名称] 执行每日播报并将结果发送到当前频道。`

**配置优势**：
- 符合 Clawdbot 原生生态逻辑，保证执行稳定。
- 方便在 Discord/飞书等群聊中进行权限与投递管理。
- 生成的结果支持后续追加提问（如：“详细讲讲第二篇论文”）。

## 3. 信息源与方法论
- **信息源**: 详见 `references/sources.md` (包含 PubMed, NEJM, Lancet, Nature Medicine, arXiv 等 27 个专业平台)。
- **分析方法**: 详见 `references/methodology.md` (包含论文脉络分析、优缺点对比及弱点识别逻辑)。
- **输出格式**: 详见 `references/output-formats.md` (**双轨模式：简报 Broad Synthesis / 近报 Solution-Oriented Flash**)。
- **使用示例**: 详见 `references/example.md` (包含基于 2026 年实时数据的 OCR 简报示例)。

## 4. 自动化部署 (示例)
参考 `scripts/run_briefing.sh` 配合同步安装的脚本进行自动化推送：
```bash
# 生成简报并通过管道发送到飞书
bash scripts/run_briefing.sh | python3 scripts/feishu_push.py "您的飞书Webhook地址"
```

## 5. 故障处理
- 顶刊抓取失败时，会自动降级至 MedRxiv 等预印本。
- 若实时源完全崩溃，将基于本地知识库生成“近期重点回顾”。
