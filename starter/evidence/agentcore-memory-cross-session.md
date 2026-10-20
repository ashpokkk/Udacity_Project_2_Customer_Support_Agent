# AgentCore Memory — Cross-Session Test Evidence

**Status:** PASSED

## Test objective
Verify that customer information saved in one session can be recalled in a different session using the same customer ID.

## Customer information saved
- Name: Sara
- Communication preference: Email updates instead of phone calls

## Session 1
- Customer ID: `memory-test-sara-001`
- Session ID: `memory-session-001`
- Action: Asked the agent to remember the customer's name and communication preference.

## Session 2
- Customer ID: `memory-test-sara-001`
- Session ID: `memory-session-006`
- Action: Asked, "What is my name, and how do I prefer to receive updates?"

## Result
The agent correctly recalled:
- Name: Sara
- Communication preference: Email updates instead of phone calls

## Conclusion
Cross-session customer memory was successfully demonstrated using the same customer ID and a different session ID.

## Verification notes
Memory records were also verified independently through the AgentCore Memory retrieval API. The deployed implementation retrieves customer memories before invoking the agent and includes the retrieved context in its prompt.
