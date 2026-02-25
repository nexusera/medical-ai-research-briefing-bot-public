# 结构化学习与升级 (Structured Learning & Promotion)

本目录存储此 Agent 在交互中捕获到的边界问题、修正反馈与升级经验。

我们遵循 Clawbot 核心定律：
**❌ 绝不自动修改 System Prompt (Self-healing)**
**❌ 绝不做黑箱在线学习 (Online RL)**
**✅ 仅在生命周期中进行结构化的错误捕获，通过人工/规则驱动版本更新。**

## 经验捕获模板 (Capture Schema)

每次捕获错误或有效微调时，在此记录 `.md` 格式的经验，必须包含以下结构：

```markdown
### [Bug / Correction ID]
- **时间**: YYYY-MM-DD
- **现象 (Signal)**: [例如：生成 OCR 简报时，返回结果包含闲聊，且格式降级]
- **根因分析 (Root Cause)**: [由于大模型被自身的“助手人设”覆盖，且没有内联格式模板导致格式猜测]
- **结构化升级 (Promotion / Fix)**: [在 `SOUL.md` 和 `AGENTS.md` 注入 Control-plane 拦截器并强化 `CLAUDE.md` 约束]
- **状态 (Status)**: [Pending / Promoted to Asset / Closed]
```
