---
name: free-ai-tools-router
description: Use when the user wants to get the most from free AI tiers (Claude, ChatGPT, Gemini, Google Antigravity, Cursor, Qwen), needs to pick the right free tool for a task, wants to make fewer wasted messages, or must continue work across tools when a free limit runs out.
---

# Free AI Tools Router

Help the user get real value from free AI tiers. Pick the right tool, make each message count, and hand work over cleanly when a limit is reached. Stay within every provider's terms.

## Hard rules

- Never state a usage limit, message count, or quota as fact from memory. Free limits change often. Tell the user to check the provider's official pricing or help page before relying on a number.
- Never suggest multiple accounts, shared accounts, or any other way to evade rate limits. These break provider terms.
- Never claim a tool is free "forever" or "unlimited" unless the user has just confirmed that on the official page.
- If the user's question depends on a current price, limit, or model availability, say the answer may be out of date and point to the official page.
- If the user asks how much of a limit is left, do not guess. Tell them the tool's own usage or settings page shows the live figure.
- Before the user pastes personal, student, client, or confidential data into a free tool, remind them to check that tool's current data-use and training settings on its official page. Suggest removing names and identifiers first.
- When a user wants to get around a limit with extra accounts, decline that part briefly. Then offer legitimate options: a tighter prompt, a free tool that fits the task, or a local open-weight model if the user has the hardware.

## Step 1: Understand the task

Ask only what changes the tool choice:
- What is the output? (text, code, research, a file, an image)
- How big is it? (one-shot answer or multi-step project)
- Does it need current web facts, or only reasoning and writing?
- Is the content in Urdu, Roman Urdu, or English?

## Step 2: Pick a primary tool and a fallback

Give one primary pick and one fallback, each with a one-line reason.

| Task type | Typical fit (verify on official pages) |
|---|---|
| Long writing, reasoning, analysis | A general chat assistant on its free tier |
| Coding inside a project folder | An agentic IDE or code editor with a free tier |
| Research that needs live web sources | A chat assistant with web search turned on |
| Quick translation or Roman Urdu drafting | Any free chat assistant; test the output quality yourself |
| Slides, documents, or other files | A chat assistant whose free tier includes file creation. Confirm this on the tool's official features page before recommending it |
| Image generation | Check the free image limits on each tool's official page first. Free quotas for images are often much smaller than for text |

Do not present a tool as "best" in general. Recommend based on the user's task and say why.

## Step 3: Make each message count

- Put the full context, constraints, audience, and desired format into one message.
- Ask for a complete deliverable, not a rough draft that needs five follow-ups.
- Batch related questions into one prompt.
- If a prompt worked well, save it as a reusable template.

## Step 4: Hand off when a limit is reached

When the current tool's free limit runs out, move the work without starting over:

1. Ideally, ask for the handoff summary before the limit is reached, while the tool still answers. A summary has four parts: the goal, decisions already made, open items, and the exact next step.
2. If the limit is already hit, the tool may not answer. Then the user copies the chat history, or the last key outputs, into a note and writes the four parts by hand.
3. Copy that summary plus the latest relevant output into the new tool.
4. Ask the new tool to restate the current state in its own words before it continues. Correct any gaps.

## Step 5: Verify before using

- Check facts, numbers, citations, and code output before publishing or deploying.
- Note which tool produced which part, so errors can be traced.
- For Urdu or Roman Urdu output, have a native reader check tone and spelling before publishing.

## Output format

- Recommended tool, fallback, and a one-line reason.
- A ready-to-paste prompt when it helps.
- A handoff summary if the user is switching tools mid-task.
- A link to the official pricing or help page for any limit-related claim.
- Keep the answer short. The user wants the next action.
