# Agent Workflows & Hooks

本文件定义 Clawbot 在各个关键生命周期节点注入的动态 Hooks，从而将逻辑从单纯的 Prompt 变成 Control-plane 下的程序化拦截。

## UserPromptSubmit Hook
- **Trigger**: 用户输入指令并请求简报。
- **Action**: 
  1. 拦截用户意图。检查是否触发了时效检索（如：“今天的简报”、“最新会议”）或关联检索（如：“近年来基准对比”、“方向脉络”）。
  2. 根据意图，组装正确的 `WebSearch` 的时间窗约束条件（具体法则见 `TOOLS.md`）。
  3. 隐性加载 `SOUL.md` 和 `CLAUDE.md` 进入内存约束，对最终响应格式上锁。

## CodeExecution / PostToolUse Hook
- **Trigger**: WebSearch 等工具将检索结果流回。
- **Action**:
  1. 并行校验：判断返回数量与信噪比。若命中率极低（0-1篇）且用户不是执行 Related 模式，触发 Fallback 拦截器。
  2. Fallback 行为：不请求 LLM 强行生成结果，而是立刻重新发起一次扩大时间窗（如 72h / 7d）的调用。

## PreResponse / Structure Generation Hook
- **Trigger**: 工具返回有效文献列表，准备给用户生成最终响应前。
- **Action**:
  1. **禁止直接流式输出**。必须先启动内部的 `<thinking>` Block 进行结构化梳理。
  2. 针对每一篇保留文献，分别遍历进行 5 个要素的判定（[Research Question, Method, Data, Key Findings, Limitations]）。
  3. 完成思维链（CoT）拼合后，才可将信息通过 `SOUL.md` 约定的 “唯一合法格式 (Advanced Academic)” 推向屏幕前。
