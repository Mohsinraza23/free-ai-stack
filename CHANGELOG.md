# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-11-04

### Added
- `free-ai-tools-router` skill (`SKILL.md`) for picking free AI tools, writing efficient prompts, handing work over when a free limit runs out, and verifying output.
- Hard rules: no stated limit numbers from memory, no rate-limit evasion, privacy reminder before pasting personal or student data.
- Tool table covering Claude, ChatGPT, Gemini, Google Antigravity, Cursor and Qwen, with official pricing links.
- `free-ai-tools-router.zip` for direct upload to Claude.ai.
- README with install steps for Claude.ai, Claude Code and other agents, diagrams for the routing and handoff flows, FAQ and honest limits.
- MIT `LICENSE`.
- `CONTRIBUTING.md` with contribution rules and the review process.
- `assets/banner.svg` and `assets/demo.svg` (illustrative example output).
- `scripts/check_links.py` to check the official links in the README.

### Notes
- Desk-checked against 11 sample tasks. A live test on real tasks is still pending.
- Link checks in this release were not automated. Run `scripts/check_links.py` before relying on the links.
