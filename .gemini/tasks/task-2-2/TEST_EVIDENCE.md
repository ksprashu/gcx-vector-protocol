# Test Evidence for Task 2.2

## Command Executed
`npm test -w @google/gemini-cli-core -- src/agents/agent-tool.test.ts`

## Result
FAILED

## Output
```
> @google/gemini-cli-core@0.41.0-nightly.20260423.gaa05b4583 test
> vitest run src/agents/agent-tool.test.ts


 RUN  v3.2.4 /Users/ksprashanth/code/github/gemini-cli/packages/core
      Coverage enabled with v8

 ❯ src/agents/agent-tool.test.ts (4 tests | 1 failed) 11ms
   ✓ AgentTool > should map prompt to objective for local agent 6ms
   ✓ AgentTool > should map prompt to query for remote agent 1ms
   ✓ AgentTool > should throw error for unknown subagent 1ms
   × AgentTool > should map prompt to task and use BrowserAgentInvocation for browser agent 3ms
     → Prompt is too short ("Open page"). You must provide clear, detailed instructions for the subagent to succeed.

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ Failed Tests 1 ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯

 FAIL  src/agents/agent-tool.test.ts > AgentTool > should map prompt to task and use BrowserAgentInvocation for browser agent
Error: Prompt is too short ("Open page"). You must provide clear, detailed instructions for the subagent to succeed.
 ❯ AgentTool.createInvocation src/agents/agent-tool.ts:99:13
     97|     const normalizedPrompt = params.prompt.trim();
     98|     if (normalizedPrompt.length < 10) {
     99|       throw new Error(
       |             ^
    100|         `Prompt is too short ("${normalizedPrompt}"). You must provide clear, detailed instructions for the subagent to succeed.`,
    101|       );
 ❯ src/agents/agent-tool.test.ts:131:47

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/1]⎯


 Test Files  1 failed (1)
      Tests  1 failed | 3 passed (4)
   Start at  11:32:15
   Duration  3.67s (transform 1.03s, setup 30ms, collect 2.52s, tests 11ms, environment 0ms, prepare 42ms)
```
