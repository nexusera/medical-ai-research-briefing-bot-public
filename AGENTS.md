# Agent Workflows & Hooks

本文件定义 Clawbot 在各个关键生命周期节点注入的动态 Hooks，从而将逻辑 from 单纯的 Prompt 变成 Control-plane 下的程序化拦截。

## UserPromptSubmit Hook
- **Trigger**: 用户输入指令并请求简报。
- **Action**: 
  1. 拦截用户意图，进行双轨定点解析判别（Dual-Resolution Routing）：
     - **模式 A (高级学术综述 / Broad Synthesis)**: 判别依据词如“简报”、“综述”、“深掘”、“脉络”。触发纵深模式（无硬性短窗口，必须包含过往奠基作与近年演进）。
     - **模式 B (高级前沿快报 / Solution-Oriented Flash)**: 判别依据词如“近报”、“快报”、“快讯”、“组合方案”。触发当下模式（短窗口，摒弃历史基线大纲，侧重于抽取模块合体现有最优解）。
  2. 根据意图，组装正确的 `WebSearch` 约束条件（具体法则见 `TOOLS.md`）。
  3. 隐性加载 `SOUL.md` 和 `CLAUDE.md` 进入内存约束，对最终响应格式上锁。
   4. **强制执行数据库范式搜索 (Mandatory DB Search Execution)**: 无论用户指令是否明确要求“搜索”，Agent 必须自动提取 `sources.md` 中定义的专业数据库（PubMed, arXiv, FDA 等）Search Template 并通过 `WebSearch` 工具执行检索，严禁仅使用通用搜索或空手响应。
   5. **禁止等待交互 (Proactive Zero-Wait)**: 严禁向用户提示“请提供 PDF/链接”等交互门槛。意图识别完成后，必须转入静默后台检索，跳过任何请求外部文件的 Gate。

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
  3. 完成思维链（CoT）拼合后，才可将信息通过 `SOUL.md` 约定的 “唯一合法格式 (Advanced Academic)” 推向屏幕前。**必须严格执行“直接明了表述 (Clear & Direct)”与“消除比喻与发散 (Anti-Metaphor)”规则，使用人类易懂且无废话的语言。**
