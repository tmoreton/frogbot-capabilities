# Capability audit

Updated September 5, 2026.

## Product lens

FroggyBot should not compete by having the longest generic catalog. Its useful niche is group coordination: invite people easily, preserve editable shared memory, reach a decision, and automatically produce the itinerary, budget, list, brief, or file everyone can use.

External usage research supports a compact foundation around practical guidance, information seeking, and writing. OpenAI reports that those three categories make up roughly three-quarters of consumer conversations. Zapier’s largest integration categories emphasize calendar, email, files, spreadsheets, project management, task management, scheduling, and team collaboration. These are stronger signals for FroggyBot than adding more social-media search variants.

Sources:

- [How people are using ChatGPT](https://openai.com/index/how-people-are-using-chatgpt/)
- [Zapier app and integration categories](https://zapier.com/apps)
- [Anthropic Economic Index: evolving agentic work](https://www.anthropic.com/research/economic-index-june-2026-report)

## Current decision

### Keep as the general foundation

- Planner, Researcher, Deep Research, Fact Checker
- Writer, Editor, Summarizer
- Analyst, Data Analyst
- Brainstormer and Teacher
- Meeting Prep, Product Manager, and Project Manager

These cover the dominant guidance, information, writing, analysis, learning, and structured-work use cases without requiring one skill per prompt variation.

### Make group outcomes the featured layer

- Group Trip Planner
- Group Decision Helper
- Event Planner
- Shared Budget

These new skills directly express FroggyBot’s niche and naturally produce its strongest outputs: itineraries, budgets, checklists, and shared decisions.

### Retire or defer

- **Browser Research:** retired from the current catalog because Researcher and Deep Research already choose the browser when navigation is required. It described an implementation method rather than a user outcome.
- **X / Twitter Research and YouTube Research:** definitions remain in the repository, but their tools stay disabled until reviewed credentials and gateway targets are deployed. They should not appear as available in the website or app before then.

No other skill should be removed until selection and completion telemetry can show persistent low value. Similar names alone are not enough evidence: Writer versus Editor and Analyst versus Data Analyst lead to meaningfully different outputs.

## Tool audit

### Keep enabled

- Web Search and Web Reader: discovery plus inspection of primary pages
- Calculator: exact lightweight math
- World Clock: time-zone coordination
- Task Tracker: maintained lists for longer group work
- Focused Delegate: internal support for decomposed research
- Code Interpreter: data analysis and generated tables or charts in a sandbox
- Interactive Browser: multi-page and interactive research with approval before actions

### Keep disabled until deployed

- X / Twitter Search
- YouTube Research

### Highest-value additions

1. **Calendar availability:** read free/busy time and propose options; creating or changing events must require confirmation.
2. **Maps and places:** find travel times, accessible venues, and nearby options with source timestamps.
3. **Weather:** read forecasts for trip and event planning, with location and forecast-time clarity.
4. **Shared documents and spreadsheets:** create or update the group’s chosen output in Google Drive or Microsoft 365 with explicit write approval.
5. **Email and invitations:** draft first; sending must always require confirmation of recipients and content.
6. **Forms and polls:** collect structured preferences from invited participants and write results into group memory.

Calendar, maps, and weather should come before broad social integrations because they strengthen the core group-planning loop. Documents and email come next because they turn decisions into artifacts and communication. Financial transfers, purchasing, and account-management tools should remain out of the base catalog until stronger transaction policies and confirmations exist.

## Measurement before the next pruning pass

Track only privacy-preserving product events: skill selected, skill completed, user retained or removed it, output type created, tool failure, and explicit approval outcome. Review after enough real sessions exist to avoid optimizing around the starter catalog or internal testing.
