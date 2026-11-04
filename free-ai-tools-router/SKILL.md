---
name: free-ai-tools-router
description: Use when the user asks which free AI tool to use (Claude, ChatGPT, Gemini, Google Antigravity, Cursor, Qwen), wants to stretch a free plan, hit a free limit mid-task, needs to move work to another AI tool, or asks whether a free feature still exists. Also use for Roman Urdu or Urdu prompts on free tools.
---

# Free AI Tools Router

Help the user get real value from free AI tiers. Pick the right tool, make each message count, and hand work over cleanly when a limit is reached. Stay within every provider's terms.

## When not to use this skill

- The user is on a paid or team plan and asks about that plan's features. Answer from the plan's official page instead.
- The task is a simple question that any assistant answers in one reply. Just answer it.
- The user asks for a tool recommendation with no task. Ask for the task first (Step 1).

## Hard rules

- **Never state a limit, message count, quota or price as fact from memory.** Free limits change often. Point the user to the official pricing or help page for the current number. See `references/tools.md` for the links.
- **Never say a tool is free "forever" or "unlimited".** Plans change. Say "free tier, check the official page" instead.
- **If the user asks how much of a limit is left,** say that the tool's own usage or settings page shows the live figure. Do not estimate it.
- **Before the user pastes personal, student, client or confidential data,** remind them to check that tool's current data-use and training settings on its official page. Suggest removing names and identifiers first.
- **Do not help evade limits.** If the user asks for extra accounts, shared accounts or other workarounds, decline that part in one sentence. Then offer legitimate options: a tighter prompt, a different free tool for the task, or a local open-weight model if the user has the hardware.

## Step 0: Check the plan

Ask once, if it is not already clear: is the user on a free plan, or a paid one?
- **Free plan:** Use this skill fully.
- **Paid plan:** Skip the free-tier advice. Focus on the task, and point to the plan's official page for limits.

## Step 1: Understand the task

Ask only what changes the tool choice:
- What is the output? (text, code, research, a file, an image)
- How big is it? (one answer, or a multi-step project)
- Does it need current web facts, or only reasoning and writing?
- Is the content in English, Roman Urdu or Urdu?

## Step 2: Pick a primary tool and a fallback

Give one primary pick and one fallback, each with a one-line reason. Read `references/tools.md` for the tool list and official links.

| Task type | Typical fit (confirm on the official page) |
|---|---|
| Long writing, reasoning, analysis | A general chat assistant on its free tier |
| Coding inside a project folder | An agentic IDE or code editor with a free tier |
| Research that needs live web sources | A chat assistant with web search turned on |
| Roman Urdu or Urdu drafting | Any free chat assistant. Test the output quality yourself |
| Slides, documents, other files | A chat assistant whose free tier includes file creation. Confirm on the features page |
| Image generation | Check free image limits first. They are often much smaller than text limits |

Do not present any tool as "the best" in general. Recommend based on this user's task, and say why.

## Step 3: Make each message count

- Put the full context, constraints, audience and format into one message.
- Ask for a complete deliverable, not a rough draft that needs five follow-ups.
- Batch related questions into one prompt.
- If a prompt worked well, offer to save it as a reusable template.

For ready-made prompts, see the templates in `references/tools.md`.

## Step 4: Hand off when a limit is reached

Move the work without starting over.

1. **Best:** Ask for a handoff summary before the limit, while the tool still answers. It has four parts: the goal, decisions made, open items, and the exact next step.
2. **If the limit is already hit:** The tool may not answer. The user copies the chat, or the last key outputs, into a note and writes the four parts by hand.
3. Copy the summary and the latest relevant output into the new tool.
4. Ask the new tool to restate the current state in its own words, and correct any gaps before it continues.

## Step 5: Verify before using

- Check facts, numbers, citations and code output before publishing or deploying.
- Note which tool produced which part, so errors can be traced.
- For Urdu or Roman Urdu output, ask a native reader to check tone and spelling before publishing.

## Output format

Keep the answer short. Use this shape:

```
Primary: <tool> — <one-line reason>
Fallback: <tool> — <one-line reason>
Prompt: <ready-to-paste prompt, if useful>
Check: <what to verify before using>
Official page: <link for any limit, price or feature claim>
```

If the user is switching tools mid-task, add a handoff summary in the four-part format.
