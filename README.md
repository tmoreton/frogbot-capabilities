# FrogBot Capabilities

This repository is the reviewed publishing source for FrogBot skills and external tool schemas.

- `skills/` contains instruction-only Agent Skills. Community skills may not include executable scripts.
- `tools/` contains narrowly scoped OpenAPI schemas deployed behind Amazon Bedrock AgentCore Gateway.
- `catalog.json` is the machine-readable catalog consumed by FrogBot.

The catalog also contains a reviewed runtime binding for every tool. Gateway-backed tools can be
added or changed without an app release; FrogBot discovers their permitted operation names from
the catalog. Stan features and local utilities use a deliberately small runtime allowlist.

FrogBot loads skill releases by immutable Git tag. Updating a skill requires a version bump and a new release tag, so existing bots keep the behavior they were shared with.

## Add a skill

1. Copy an existing directory under `skills/`.
2. Write a concise `SKILL.md` with `name` and `description` frontmatter.
3. Add its metadata to `catalog.json` and increment the integer version.
4. Run `python3 scripts/validate_catalog.py`.
5. Open a pull request.

Shared and official skills are immutable releases. In FrogBot, a user can customize any skill by
creating a private editable copy, so published behavior stays stable while personal variations are
fully editable and versioned.

Executable integrations belong in AgentCore Gateway, not in a skill package. Skills may declare the reviewed tool IDs they expect through `allowed-tools`.
