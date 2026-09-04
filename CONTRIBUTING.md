# Contributing

FrogBot skills are portable instructions, not executable plugins.

Submissions must:

- contain a single `SKILL.md` and optional static references or templates;
- avoid scripts, binaries, secrets, access tokens, and hidden remote instructions;
- use only tool IDs already present in `catalog.json`;
- explain when the skill should and should not be used;
- avoid requesting broader access than the skill needs.

Public submissions are reviewed before appearing in the store. A rejected submission remains usable as a private or link-only skill in the creator's FrogBot account.

New tools must include a runtime binding in `catalog.json`. Gateway bindings list exact operation
IDs from a reviewed target. Stan and local bindings are restricted by the validator and require a
runtime review before a new executable implementation can be selected.
