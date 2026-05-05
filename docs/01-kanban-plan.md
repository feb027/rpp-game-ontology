# Kanban Execution Plan

Board: `rpp-game-ontology`
Project path: `/home/aqua/rpp-game-ontology`
Dashboard: `http://100.75.24.117:9119`

## Task Graph

```text
T0 pm          lock scope + Methontology deliverable plan
├─ T1 researcher  research Protégé install/environment + ontology examples
├─ T2 analyst     design ontology specification + competency questions
│  └─ T3 backendeng implement ontology + demo app using Codex
│     └─ T4 reviewer review ontology/app correctness
├─ T5 writer      create slide content/deck for points a-e
│  └─ T6 writer   create video tutorial script/storyboard
└─ T7 reviewer    final packaging QA across slides/app/video script
```

## Deliverable Acceptance Criteria

- `ontology/` contains OWL/RDF or documented Protégé-compatible ontology artifacts.
- `app/` contains runnable demo application.
- `slides/` contains slide source/deck.
- `video/` contains tutorial script/storyboard.
- `docs/` contains planning/research/review notes.
- Final review confirms all assignment points a–f are covered.
