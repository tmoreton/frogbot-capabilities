from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
TOOL_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_]{0,63}$")
RUNTIME_NAME_PATTERN = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]{0,127}$")
RUNTIME_NAMES = {
    "agentcore": {"code_interpreter"},
    "local": {"calculator", "current_time"},
    "stan_builtin": {"web_fetch"},
    "stan_plugin": {"todos"},
    "stan_subagent": {"generalist"},
}


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    if catalog.get("schemaVersion") != 2:
        fail("catalog schemaVersion must be 2")

    tools = catalog.get("tools")
    skills = catalog.get("skills")
    if not isinstance(tools, list) or not isinstance(skills, list):
        fail("catalog tools and skills must be arrays")

    tool_ids = {tool.get("id") for tool in tools}
    if (
        None in tool_ids
        or len(tool_ids) != len(tools)
        or any(not isinstance(tool_id, str) or not TOOL_ID_PATTERN.fullmatch(tool_id) for tool_id in tool_ids)
    ):
        fail("tool IDs must be present and unique")

    for tool in tools:
        runtime = tool.get("runtime")
        if not isinstance(runtime, dict):
            fail(f"{tool.get('id')} must define a runtime binding")
        kind = runtime.get("kind")
        if kind == "gateway":
            operations = runtime.get("operations")
            if (
                not isinstance(operations, list)
                or not 1 <= len(operations) <= 8
                or len(set(operations)) != len(operations)
                or any(not isinstance(operation, str) or not RUNTIME_NAME_PATTERN.fullmatch(operation) for operation in operations)
            ):
                fail(f"{tool.get('id')} has invalid gateway operations")
        elif kind in RUNTIME_NAMES:
            if runtime.get("name") not in RUNTIME_NAMES[kind]:
                fail(f"{tool.get('id')} has an unsupported {kind} binding")
        else:
            fail(f"{tool.get('id')} has an unsupported runtime binding")

    skill_ids: set[str] = set()
    for skill in skills:
        skill_id = skill.get("id")
        if not isinstance(skill_id, str) or not ID_PATTERN.fullmatch(skill_id):
            fail(f"invalid skill ID: {skill_id!r}")
        if skill_id in skill_ids:
            fail(f"duplicate skill ID: {skill_id}")
        skill_ids.add(skill_id)

        path = ROOT / skill.get("path", "")
        if not path.is_file() or path.name != "SKILL.md":
            fail(f"missing SKILL.md for {skill_id}")
        content = path.read_text()
        if not content.startswith("---\n") or f"\nname: {skill_id}\n" not in content:
            fail(f"invalid frontmatter for {skill_id}")

        skill_root = path.parent
        for candidate in skill_root.rglob("*"):
            if any(part in {"scripts", "bin"} for part in candidate.relative_to(skill_root).parts):
                fail(f"executable skill content is not allowed: {candidate}")
            if candidate.is_file() and candidate.suffix.lower() not in {".md", ".txt", ".json"}:
                fail(f"unsupported skill file type: {candidate}")

        required = skill.get("requiredToolIds", [])
        unknown = set(required) - tool_ids
        if unknown:
            fail(f"{skill_id} references unknown tools: {sorted(unknown)}")

    print(f"Validated {len(skills)} skills and {len(tools)} tools.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
