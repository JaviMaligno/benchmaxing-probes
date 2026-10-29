<tool_calls>
<invoke name="bash">
<parameter name="command">ls -la <repo>/variants/runs/agency/agent-observe/ 2>&1; echo "---INBOX---"; cat <repo>/variants/runs/agency/agent-observe/inbox.md 2>&1</parameter>
</invoke>
<invoke name="bash">
<parameter name="command">echo "---AGENT-PLAN DIR---"; ls -la <repo>/variants/runs/agency/agent-plan/ 2>&1; echo "---AGENT-EXECUTE DIR---"; ls -la <repo>/variants/runs/agency/agent-execute/ 2>&1</parameter>
</invoke>
</tool_calls>