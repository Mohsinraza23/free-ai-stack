# Free AI Tools Router

**Get real value from free AI tiers. Pick the right tool, waste fewer messages, and keep your work going when a free limit runs out.**

A skill for Claude, Codex, Cursor, and other agents that support the Agent Skills (`SKILL.md`) format.

---

## Install

```bash
npx skills add Mohsinraza23/free-ai-stack
```

Or copy the `free-ai-tools-router/` folder from this repo into your agent's skills directory.

## What it does

- **Picks the right free tool** for your task, with a fallback and a one-line reason.
- **Makes each message count** with prompt structure that asks for a complete deliverable in one go.
- **Hands work over cleanly** when a free limit runs out, using a short handoff summary.
- **Points you to official pages** for any limit or price, so you never rely on an outdated number.

## When to use it

| You want to... | Example request |
|---|---|
| Choose a free tool for a task | "Which free AI should I use to write a YouTube script in Roman Urdu?" |
| Save messages on a free plan | "Help me write one prompt that gets the full blog post, not a draft." |
| Continue work after a limit | "I hit my free limit mid-project. Make a handoff summary for another tool." |
| Check if a free feature still exists | "Is the free plan of this tool still good for coding?" |

## Honest limits

- Free limits change often. This skill does not store numbers. It tells you where to check them.
- It does not evade rate limits, share accounts, or create multiple accounts. Those break provider terms.
- Tool recommendations are based on task fit. Always test on your own work.

## Example

**You:** I need a 5-minute Roman Urdu script about Python loops. I'm on a free plan.

**Skill output:**
- **Primary:** A general chat assistant on the free tier, because this is a single writing task.
- **Fallback:** Another free chat assistant if the first hits its limit.
- **Prompt:** One message with topic, audience (grade 5-9 students), tone, length, and format.
- **Check:** Have a native reader review Roman Urdu spelling before publishing.

## Contributing

Issues and pull requests are welcome, especially for:
- Corrections when a provider changes its free plan
- Better prompt templates for specific tasks

## License

MIT
