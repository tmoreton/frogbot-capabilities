# Contributing

FrogBot skills are portable instructions, not executable plugins.

Submissions must:

- contain a single `SKILL.md` and optional static references or templates;
- avoid scripts, binaries, secrets, access tokens, and hidden remote instructions;
- use only tool IDs already present in `catalog.json`;
- explain when the skill should and should not be used;
- avoid requesting broader access than the skill needs.

## Submit a skill

1. Fork this repository and copy the closest example in `skills/`.
2. Keep the package instruction-only: `SKILL.md` plus optional Markdown, text, or JSON references.
3. Add the skill to `catalog.json` with a category, author, up to six tags, and only the reviewed tools it needs.
4. Run `python3 scripts/validate_catalog.py`.
5. Open a pull request using the checklist. Review covers usefulness, clarity, safety, and least-privilege tool access.

Not ready to write the skill? Open a skill request from the repository’s Issues tab.

## Propose a tool

Tools are actions backed by FroggyBot-controlled runtime bindings. Start with a tool request describing
the user outcome, exact actions, data accessed, authentication method, and whether it can change external
state. A tool is listed only after its server-side binding and permissions are reviewed and deployed.

Public submissions are reviewed before appearing in the store. A rejected submission remains usable as a private or link-only skill in the creator's FrogBot account.

New tools must include a runtime binding in `catalog.json`. Gateway bindings list exact operation
IDs from a reviewed target. Stan and local bindings are restricted by the validator and require a
runtime review before a new executable implementation can be selected.
