# Contributing to Free AI Tools Router

Thanks for helping make this skill better. This guide explains how to propose changes so they can be reviewed and merged safely.

## What we welcome

- 🔄 **Corrections** when a provider changes its free plan, features or pricing page.
- 🧩 **Better prompt templates** for real tasks (English, Roman Urdu, Urdu).
- 🧪 **New evaluation cases** that show where the skill gives a wrong or weak answer.
- 📝 **README and docs fixes**: typos, unclear steps, broken links.

## Ground rules

1. **Never add a number as fact.** Free limits, prices and quotas change often. Link to the provider's official page and tell users to check it.
2. **No rate-limit evasion.** Do not propose multiple accounts, shared accounts or any method that breaks provider terms.
3. **Cite official sources** for every tool claim. Third-party blogs can be used for leads, but not as the final source.
4. **Keep the skill short.** `SKILL.md` should stay focused on what the agent needs at runtime. Put long background in the README.
5. **Respect privacy.** Do not add examples that include real names, student data or private messages.

## How to propose a change

1. **Open an issue first** for big changes (new tools, new steps, new behaviour). Describe the problem and the expected result.
2. **Fork the repo** and create a branch, for example `fix/gemini-link` or `feat/urdu-templates`.
3. **Make the change.** Update `CHANGELOG.md` under an `Unreleased` heading.
4. **Check the links** by running:
   ```bash
   python3 scripts/check_links.py
   ```
   Paste the result into your pull request.
5. **Open a pull request** with:
   - What changed and why
   - Which official source supports any new claim
   - How you tested it (which tasks you ran, and what happened)

## Testing a change to the skill

- Install the skill locally with `npx skills add <your-fork> -g`, or copy the `free-ai-tools-router/` folder into your agent's skills folder.
- Run at least 3 real tasks in the agent you use, one of which should involve a handoff.
- Note any answer that gives an unverified limit, or that skips the privacy reminder when it should appear.

## Releasing a skill change

1. Run the cases in `evals/evals.md` and record the results.
2. Re-check links with `python3 scripts/check_links.py`.
3. Rebuild the Claude.ai ZIP from the `free-ai-tools-router/` folder only (it should contain `SKILL.md` and `references/`).
4. Update `CHANGELOG.md` and the version badge in the README.

## Review process

- Maintainers check that claims have official sources and that no rule in *Ground rules* is broken.
- Pull requests that add a limit or price number without an official link are not merged.
- Once merged, a change is listed in `CHANGELOG.md` and the version is updated.

## Versioning

We use [Semantic Versioning](https://semver.org/):

- **Patch** (1.0.1): wording fixes, broken link fixes, typo fixes.
- **Minor** (1.1.0): new steps, new tools in the table, new templates.
- **Major** (2.0.0): changes to the skill's behaviour that break how users rely on it.

## Code of conduct

Be respectful and specific. Critique the change, not the person.

## Questions

Open an issue with the label `question`.
