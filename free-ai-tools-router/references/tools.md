# Tool reference

Read this file when you need a tool's official link or a ready-made prompt.

**Important:** Limits, prices and features change often. Never quote a number from this file as current. Send the user to the official page, and tell them the status of this file.

**Status of this file:** Drafted 2026-11-04 from third-party sources. Official links are listed but not yet re-checked by an automated run. Run `scripts/check_links.py` before relying on them.

## Tools

| Tool | Good for | Free tier (general) | Official page | Status |
|---|---|---|---|---|
| Claude | Long writing, reasoning, analysis | Chat with usage limits; some features on the free tier | https://claude.com/pricing | Not yet checked |
| ChatGPT | General chat, writing, research | Chat with limits that have changed in 2026. Check the current rules | https://openai.com/chatgpt/pricing/ | Not yet checked |
| Gemini | Google apps, quick tasks | Free access; check current limits | https://gemini.google.com | Not yet checked |
| Google Antigravity | Agentic coding in an IDE | Free individual tier with weekly agent limits; limits have changed over time | https://antigravity.google/docs/plans | Not yet checked |
| Cursor | Coding in a project folder | Hobby (free) plan with limited agent and tab usage | https://cursor.com/pricing | Not yet checked |
| Qwen | Chat and multilingual tasks | Chat app is free. The free developer API tier ended in 2026 | https://chat.qwen.ai | Not yet checked |

## Ready-made prompts

### Roman Urdu script
> Write a 5-minute script in Roman Urdu for [audience, e.g. grade 5-9 students] about [topic]. Tone: [friendly / formal]. Include a short intro, three examples with code, a quick quiz at the end, and a closing line. Keep the English technical terms as they are.

### Handoff summary (ask before the limit)
> Summarise this work so I can continue in another tool. Give four parts: 1) the goal, 2) decisions already made, 3) open items, 4) the exact next step. Keep it under 150 words.

### Restate state (for the new tool)
> Here is the summary of earlier work and the latest output. Restate the current state in your own words, list anything missing or unclear, and then wait for my next instruction.

### Code bug fix
> I have this error: [paste error]. Here is the relevant code: [paste code]. Explain the cause in two sentences, give the fixed code, and list anything else in the file that could break for the same reason.

### Research with sources
> Research [topic] using current web sources. Give 5 key points, each with a link and the date of the source. Mark anything you could not confirm.

## Maintenance

- Re-check every link before each release. Update the Status column to the date you checked.
- If a provider changes its free plan, update the row and add a line to `CHANGELOG.md`.
