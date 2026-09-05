(async () => {
  try {
    const response = await fetch('/catalog.json', { cache: 'no-cache' });
    if (!response.ok) return;
    const catalog = await response.json();
    const tools = catalog.tools.filter((tool) => tool.enabled !== false);
    const toolIds = new Set(tools.map((tool) => tool.id));
    const skills = catalog.skills.filter((skill) =>
      (skill.requiredToolIds || []).every((id) => toolIds.has(id)),
    );
    document.querySelectorAll('[data-skill-count]').forEach((node) => { node.textContent = skills.length; });
    document.querySelectorAll('[data-tool-count]').forEach((node) => { node.textContent = tools.length; });
  } catch {
    // Counts are progressive enhancement; the page remains complete without them.
  }
})();
