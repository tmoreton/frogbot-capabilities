# Contributing

FroggyBot Skills accepts small, reviewable additions that help a person or group reach a concrete outcome.

## Choose the right contribution

- **Skill:** readable instructions that shape how a FroggyBot approaches work.
- **Tool request:** a proposal for reading from or acting in another service.
- **Website or documentation:** a focused improvement to `site/`, `README.md`, or `docs/`.

Do not put executable integrations inside a skill. Tool execution, credentials, and permissions belong in FroggyBot’s reviewed server-side runtime.

## Add a skill

1. Search `catalog.json`, open pull requests, and the [live library](https://froggybot.com/library/) for overlap.
2. Copy the closest existing skill folder and rename it with a lowercase, hyphenated ID.
3. Keep the package instruction-only: one `SKILL.md` plus optional `.md`, `.txt`, or `.json` references.
4. Write a description that states the outcome and when the skill applies.
5. Include only guidance that changes the quality, safety, or consistency of the result.
6. Add the catalog entry and run the checks.

A minimal `SKILL.md`:

```markdown
---
name: example-skill
description: Turn a specific input into a useful, clearly bounded outcome.
---

# Example Skill

Use this skill when ...

1. Confirm the inputs that materially affect the result.
2. Produce the outcome in the shortest useful form.
3. State any uncertainty or action that needs approval.

Do not ...
```

Its matching `catalog.json` entry:

```json
{
  "id": "example-skill",
  "version": 1,
  "name": "Example Skill",
  "description": "Turn a specific input into a useful, clearly bounded outcome.",
  "category": "Planning",
  "author": "Your GitHub name",
  "tags": ["example", "outcome"],
  "path": "skills/example-skill/SKILL.md",
  "requiredToolIds": []
}
```

Use at most six meaningful tags. Add `featured: true` only when maintainers have chosen the skill as a primary starting point. A skill may name only tool IDs already present in `catalog.json`.

## Change an existing skill

Preserve its ID. If instructions change behavior, increment its integer `version` and update the catalog release. Existing tagged versions remain available to bots that already selected them.

## Propose a tool

Open the tool request before writing an OpenAPI definition. Include:

- the user outcome and exact actions;
- what information is read, stored, created, or changed;
- the authentication method and where credentials will live;
- whether actions are read-only, sandboxed, or interactive;
- rate limits, cost, and failure behavior; and
- the smallest permissions that support the outcome.

Tool proposals are listed only after their server-side binding has been security-reviewed, deployed, and tested. Community pull requests never add secrets.

## Run the checks

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests
python3 scripts/build_site.py
```

Open `dist/index.html` through a local HTTP server when changing the site:

```bash
python3 -m http.server 8000 --directory dist
```

Then check the homepage, library search and filters, mobile layout, contribution links, legal pages, and invite forwarding.

## Review checklist

Reviewers check that the contribution is useful, distinct, concise, safe, least-privilege, and understandable without private context. Broad catch-all skills, duplicated behavior, hidden instructions, and tools without a deployed binding are not accepted into the public catalog.
