<!--
AI_NOTE_START

Document role:
This file is the official entry point for the first flagship runnable demo pack of the Atlas fix system.

How to use this file:
1. Read this file first before opening any individual demo folder.
2. Treat this page as the overview for what the demo pack proves, how it is organized, and how to use replay mode vs live mode.
3. Use this file to understand why these four demos were selected as the first flagship set.
4. For atlas structure, read:
   [Atlas Final Freeze v1](../../../atlas-final-freeze-v1.md)
5. For teaching cases, read:
   [Canonical Casebook v1](../../../canonical-casebook-v1.md)
6. For AI-facing routing logic, read:
   [Atlas-to-AI Adapter v1](../../../atlas-to-ai-adapter-v1.md)
7. For official fix logic, read:
   [Family Fix Surface v1](../../family-fix-surface-v1.md)
   [Atlas to WFGY Bridge v1](../../atlas-to-wfgy-bridge-v1.md)
   [Misrepair Patterns v1](../../misrepair-patterns-v1.md)

What this file is:
- The main index for the first flagship demo pack
- The explanation page for why these demos matter
- The usage guide for replay mode vs live mode
- The bridge between atlas theory and runnable proof-of-use

What this file is not:
- Not the atlas core
- Not the full fix manual
- Not the full community lab
- Not a claim that all families already have runnable assets
- Not a requirement that every user must run the notebooks

Reading discipline for AI:
- Preserve the distinction between route, first repair move, deeper WFGY exploration, and community extension.
- Do not treat these demos as the full ontology.
- Do not overclaim that these four demos exhaust the atlas.
- Treat these demos as flagship proofs of use and template assets for future growth.

AI_NOTE_END
-->

# Flagship Runnable Demo Pack

## Problem Map 3.0 Troubleshooting Atlas
## Official MVP demo entry for route-first repair

Quick links:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../../ai-eval-evidence.md)
- [Open Atlas Hub](../../../README.md)
- [Get the Atlas Router TXT](../../../troubleshooting-atlas-router-v1.txt)

---

This folder contains the first flagship runnable demos for the Atlas fix system.

These demos are not meant to prove every possible case.  
They are meant to prove something more important:

> the atlas does not only name failures  
> it changes the first repair move

That is the entire reason this demo pack exists.

If the atlas is only a naming system, people may find it interesting.

If the atlas can show that different routing decisions lead to different repair decisions, people begin to feel that it is actually useful.

This demo pack is the smallest runnable surface that makes that claim visible.

Each demo is built around the same high-signal pattern:

- baseline failure
- atlas routing
- first repair move
- visible outcome shift
- optional deeper WFGY 3.0 exploration

The goal is not scale.  
The goal is clarity.

This folder should be read as the **official public demo surface** of the first Atlas fix release.  
It is not a giant benchmark zoo.  
It is a compact, high-signal proof layer.

---

## What this demo pack proves

This demo pack is designed to make four claims visible.

### 1. Different failures should not be repaired the same way

Many systems fail with surface similarities.

A fluent wrong answer, a broken workflow, a symbolic collapse, and a black-box debugging problem can all feel like “the system is bad.”

The atlas says that is too coarse.

This demo pack shows that once a case is routed into the right family, the first repair move changes.

### 2. The atlas is not just a checklist

A checklist can name symptoms.

A troubleshooting atlas should help you decide:

- what kind of failure this is
- why this family is primary
- why a neighboring family is secondary
- what should be repaired first
- what should **not** be repaired first

These demos are built to make that difference visible.

### 3. Route-first repair is practical

The purpose of these notebooks is not to simulate a giant production stack.

The purpose is to show a minimal but convincing pattern:

- baseline failure
- atlas routing
- first repair move
- result shift
- optional deeper WFGY 3.0 exploration

That is enough to make the system feel real.

### 4. Community growth becomes much easier once the flagship set exists

These four demos are also templates.

They are not only proofs.  
They are seed assets for future contributed demos in:

- Colab
- JSON fixtures
- prompt packs
- workflow reproductions
- benchmark reruns

This is why the first official set matters so much.

---

## Demo overview

| Demo | Family | Core proof | Recommended entry |
|------|--------|------------|-------------------|
| Demo 1 | F1 Grounding & Evidence Integrity | re-grounding changes the first repair path | `demo_01_f1_grounding_anchor_recovery_live.ipynb` |
| Demo 2 | F5 Observability & Diagnosability Integrity | visibility uplift comes before answer repair | `demo_02_f5_observability_first_replay_v2.ipynb` |
| Demo 3 | F4 Execution & Contract Integrity | execution closure repair comes before reasoning-level repair | `demo_03_f4_execution_closure_replay_v2.ipynb` |
| Demo 4 | F7 Representation & Localization Integrity | container repair changes what can stabilize next | `demo_04_f7_container_fidelity_replay_v2.ipynb` |

---

## Current MVP status

The first flagship demo pack is now in a usable MVP state.

At the current stage:

- **Demo 1** includes a live notebook and replay support
- **Demo 2** is replay-first, with **v2** now serving as the recommended replay notebook
- **Demo 3** is replay-first, with **v2** now serving as the recommended replay notebook
- **Demo 4** is replay-first, with **v2** now serving as the recommended replay notebook

This is intentional.

The current pack is designed to prove the strongest teaching pattern in the clearest possible way.

That means:

- use live mode where live comparison adds real proof value
- use replay mode where replay is clearer, safer, and more honest

This is not a shortcut.  
It is a deliberate MVP teaching decision.

At the current release stage, this pack should be treated as the **official recommended first demo set** for route-first repair.

---

## Current official notebook choices

At the current MVP stage, the recommended notebook entry points are:

- **Demo 1**
  - official live notebook:
    - `demo_01_f1_grounding_anchor_recovery_live.ipynb`

- **Demo 2**
  - official recommended replay notebook:
    - `demo_02_f5_observability_first_replay_v2.ipynb`
  - original replay notebook retained as:
    - `demo_02_f5_observability_first_replay.ipynb`

- **Demo 3**
  - official recommended replay notebook:
    - `demo_03_f4_execution_closure_replay_v2.ipynb`
  - original replay notebook retained as:
    - `demo_03_f4_execution_closure_replay.ipynb`

- **Demo 4**
  - official recommended replay notebook:
    - `demo_04_f7_container_fidelity_replay_v2.ipynb`
  - original replay notebook retained as:
    - `demo_04_f7_container_fidelity_replay.ipynb`

The rule is simple:

> original notebooks are preserved as first-pass MVP assets  
> v2 notebooks are the cleaner recommended replay versions for Demo 2, Demo 3, and Demo 4

If multiple notebooks exist for the same demo, the README and this page should always make the recommended entry point explicit.

---

## Current shared support layer

The demo pack also includes a small official shared support layer under:

[shared/](./shared/)

At the current MVP stage, that folder already includes:

- `README.md`
- `demo_utils.py`
- `display_helpers.py`
- `routing_schema.md`

These files exist to keep the official demos more aligned, more readable, and easier to audit.

They are not meant to turn the demo pack into a hidden mini-framework.

In short:

> the shared layer already exists  
> but it remains intentionally small

---

## Why these four demos were chosen

The first flagship set uses four families:

- F1 Grounding & Evidence Integrity
- F5 Observability & Diagnosability Integrity
- F4 Execution & Contract Integrity
- F7 Representation & Localization Integrity

This combination was chosen on purpose.

### F1 is the best entry point

It is easy to understand and immediately useful.

People instantly understand what it means when an answer looks fluent but is attached to the wrong evidence.

### F5 makes engineers pay attention

This demo proves the atlas is not limited to answer quality.

Sometimes the first repair move is not “fix the answer.”

Sometimes the first repair move is “make the failure visible.”

That is a mature debugging idea.

### F4 proves the atlas can touch workflow skeletons

This demo shows that the atlas is not only about content generation.

It can also classify and repair problems involving:

- readiness
- ordering
- bridge integrity
- liveness
- closure

That gives the system real architectural weight.

### F7 gives the atlas its sharpest identity

This is one of the most distinctive cuts in the whole map.

It shows that some failures are not reasoning-first or grounding-first.

Sometimes the container that carries structure fails first.

That is a powerful and memorable cut.

---

## The four official demos

This folder is organized around four flagship demos.

---

## Demo 1 · F1 Grounding Anchor Recovery

**Theme**

A fluent answer fails because it is attached to the wrong evidence anchor.

**What this demo proves**

- the failure is grounding-first
- the problem is not mainly “the model is dumb”
- the first repair move should be re-grounding, not style rewriting
- evidence verification changes the repair path

**Who this demo will hit hardest**

- RAG builders
- retrieval engineers
- enterprise QA builders
- doc QA users
- people tired of shallow hallucination discourse

**Main lesson**

Not all wrong answers are “hallucination” in the same way.

Some are evidence-anchor failures first.

**Folder**

[Demo 1 · F1 Grounding Anchor Recovery](./demo-f1-grounding-anchor/README.md)

**Official notebook**

- `demo_01_f1_grounding_anchor_recovery_live.ipynb`

---

## Demo 2 · F5 Observability First

**Theme**

A failing workflow cannot be repaired correctly because its failure path is still hidden.

**What this demo proves**

- the first failure is diagnosability
- the correct first repair move is observability insertion
- fixing the answer too early is the wrong move
- visibility changes the repair landscape

**Who this demo will hit hardest**

- agent builders
- workflow orchestrators
- evaluation engineers
- anyone who has said “I know it is broken, but I cannot see why”

**Main lesson**

Sometimes the first repair is not “repair the system.”

Sometimes the first repair is “make the system visible.”

**Folder**

[Demo 2 · F5 Observability First](./demo-f5-observability-first/README.md)

**Official notebook**

- `demo_02_f5_observability_first_replay_v2.ipynb`

**Original notebook retained**

- `demo_02_f5_observability_first_replay.ipynb`

---

## Demo 3 · F4 Execution Closure

**Theme**

A system fails because execution skeleton closure breaks before reasoning quality even matters.

**What this demo proves**

- the problem is not primarily memory or reasoning
- the problem is readiness, ordering, bridge, or liveness
- the correct first repair move is execution closure repair
- system structure can fail before model reasoning becomes the limiting factor

**Who this demo will hit hardest**

- AI workflow engineers
- multi-step system builders
- pipeline designers
- tool-calling framework users
- anyone who has seen “it failed because the sequence itself was wrong”

**Main lesson**

Some failures are caused by the workflow skeleton, not by intelligence quality.

**Folder**

[Demo 3 · F4 Execution Closure](./demo-f4-execution-closure/README.md)

**Official notebook**

- `demo_03_f4_execution_closure_replay_v2.ipynb`

**Original notebook retained**

- `demo_03_f4_execution_closure_replay.ipynb`

---

## Demo 4 · F7 Container Fidelity

**Theme**

A task looks like reasoning failure, but the structure carrier fails first.

**What this demo proves**

- the problem is not purely progression-first
- symbolic or formal containers can fail before reasoning becomes the main issue
- the first repair move should target descriptor fidelity or formal adequacy
- container-first repair changes what the system can stably do next

**Who this demo will hit hardest**

- structured output builders
- JSON and schema users
- code and symbolic reasoning users
- OCR or layout-sensitive pipeline users
- anyone interested in the atlas’s most distinctive knife-cut

**Main lesson**

Sometimes the system does not fail because it “cannot think.”

Sometimes it fails because the box carrying the thinking is already broken.

**Folder**

[Demo 4 · F7 Container Fidelity](./demo-f7-container-fidelity/README.md)

**Official notebook**

- `demo_04_f7_container_fidelity_replay_v2.ipynb`

**Original notebook retained**

- `demo_04_f7_container_fidelity_replay.ipynb`

---

## Demo modes

The flagship pack currently uses two practical modes plus one growth mode.

### Mode A · Replay mode

This is the default and most important public mode.

It works without any API key.

The user can inspect:

- the case
- the baseline
- the atlas route
- the first repair move
- the replayed before / after outputs
- the explanation of what changed

A person should be able to understand the demo even without running anything.

### Mode B · Live reproduction mode

This is optional and only used when live execution adds real value.

If it exists, it should be clearly treated as:

- optional
- for reproduction
- not required to understand the demo
- not required to evaluate the atlas concept

### Mode C · Community extension mode

This is the growth mode.

Once the official demo exists, contributors should be able to:

- swap the input case
- swap the model
- swap the prompt
- swap the fixture
- extend the repair path
- compare their result to the official version

This is how the long tail grows.

---

## Why only Demo 1 has live mode in the first MVP

This point matters and should be explicit.

In the first MVP release:

- **Demo 1** includes a live notebook
- **Demo 2, Demo 3, and Demo 4** are intentionally replay-first, and their current recommended notebooks are the **v2 replay notebooks**

This is not because the other demos are weaker.

It is because the first thing they need to prove is different.

### Why Demo 1 gets live mode first

Demo 1 is the cleanest place to show a real before / after answer shift.

Its teaching value becomes stronger when a reader can see:

- baseline answer
- repaired answer
- anchor correction
- result movement

That makes live reproduction especially worthwhile.

### Why Demo 2 stays replay-first in the first MVP

Demo 2 is about **failure-path visibility**.

Its first teaching job is not to show a model being more impressive.  
Its first teaching job is to show that:

> the system was too opaque to diagnose safely  
> and the first repair move was visibility uplift

Replay mode is already enough to teach that clearly.

### Why Demo 3 stays replay-first in the first MVP

Demo 3 is about **execution skeleton closure**.

Its teaching center is:

- readiness
- ordering
- bridge integrity
- closure

These are structural logic shifts, not model-performance showpieces.

Replay mode is the cleanest and most honest way to teach that in the first release.

### Why Demo 4 stays replay-first in the first MVP

Demo 4 is about **container fidelity**.

Its first teaching job is to make one thing visible:

> the form was already failing before deeper reasoning could stabilize

This is mostly a structure-comparison demo, not a live-performance demo.

Replay mode is enough for the first public proof.

### The honest design rule

The first MVP should choose the mode that best teaches the pattern.

That means:

- use live mode where live comparison adds real proof value
- use replay mode where replay is clearer, safer, and more honest

This is not a shortcut.  
It is a deliberate teaching design.

---

## API key policy

Some live notebooks may require an API key.

If so, the policy is simple:

- no hard-coded keys
- no saved secrets in the repository
- key entry should happen only at run time
- replay mode should still remain readable without a key

Recommended pattern for notebooks:

- ask for the key at execution time
- keep replay mode readable without key access
- clearly state that the notebook is for reproduction, not mandatory usage

This matters because the demos are designed to be understandable even when not executed.

They are proofs of use, not mandatory benchmark rituals.

---

## Minimal asset structure for each demo

Each flagship demo folder should contain the following.

### Required

- `README.md`
- `input_case.json`
- `replay_outputs.json`
- `expected_output.json`

### Recommended

- notebook file
- optional prompt file
- optional lightweight helper reference
- optional screenshot or output snapshot if replay is easier to inspect that way

### Shared support

The folder [shared](./shared/) contains the small official support layer for:

- formatting
- simple output display
- schema handling
- compact route presentation
- optional run-time utilities

This keeps each notebook smaller and easier to audit.

If multiple notebooks exist in one demo folder, the README should clearly identify which one is the recommended official entry point.

---

## What each demo README should explain

Each demo folder README should follow a stable structure.

### Required sections

1. what this demo proves
2. family route
3. why not neighbor
4. baseline failure
5. first repair move
6. optional WFGY 3.0 escalation
7. replay mode
8. files in this folder
9. expected outcome
10. limits of this demo
11. community extension ideas

This is important because many readers will understand the system from the README alone, without opening the notebook.

---

## Official vs community scope

This folder is the official flagship pack.

That means it should stay:

- small
- sharp
- readable
- high-signal
- reviewable

The official goal is **not** to cover everything.

The official goal is to provide the strongest first proofs.

Long-tail expansion belongs to the community structure under:

[Community Fix Lab](../../community/README.md)

That is intentional.

Official demos prove the core.  
Community demos scale the edge.

---

## Relationship to WFGY 3.0

These demos sit in the middle of a larger repair flow.

### Atlas layer

The atlas routes the failure.

### Fix surface layer

The official fix surface suggests the first repair move.

### WFGY 3.0 layer

WFGY 3.0 supports deeper structural and experimental exploration.

That means these demos should not pretend to be the final end of repair logic.

Instead, they should clearly show:

- what the first move is
- what changes after that move
- when deeper WFGY exploration becomes appropriate

This is why each demo may include an optional section called:

**Optional WFGY 3.0 escalation**

That section should remain compact and honest.

---

## Why these demos matter

These demos matter because they turn the atlas from:

- a strong classification system

into:

- a visible troubleshooting system

They help a reader feel, not just believe, that:

- different routes lead to different repairs
- different repairs produce different outcomes
- the atlas changes what happens next

That is the real threshold.

Once that becomes visible, the project stops feeling like a theory-only system.

It starts feeling like a real operating layer.

---

## What this pack does not claim

This pack does **not** claim that:

- four demos are enough to cover the whole atlas
- every family already has a runnable asset
- every demo must be live-run to be meaningful
- replay mode is inferior
- deeper repair is already fully solved
- community growth is no longer needed

This pack claims only that:

> a first official set of flagship demos now exists to prove that route-first repair can be made visible, teachable, and reproducible

---

## Recommended reading order

If you are new, use this order:

1. [Problem Map 3.0 Troubleshooting Atlas](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
2. [AI Eval Evidence](../../../ai-eval-evidence.md)
3. [Atlas Hub](../../../README.md)
4. [Atlas Final Freeze v1](../../../atlas-final-freeze-v1.md)
5. [Family Fix Surface v1](../../family-fix-surface-v1.md)
6. this demo pack
7. individual demo folders
8. optional deeper bridge through [Atlas to WFGY Bridge v1](../../atlas-to-wfgy-bridge-v1.md)

---

## What to explore next

After reading this demo pack, most readers continue with:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../../ai-eval-evidence.md)
- [Open the Atlas Router TXT](../../../troubleshooting-atlas-router-v1.txt)
- [Open Atlas Hub](../../../README.md)

If this demo pack helped you understand the Atlas, consider:

- [starring the WFGY repo](https://github.com/onestardao/WFGY)
- opening an issue
- testing the demo folders
- contributing a clean community extension later

---

## One-line version

**This demo pack is the first official proof that Atlas routing changes the first repair move in visible, teachable, and reproducible ways.**

---

## Closing note

These four demos are small on purpose.

They are not trying to be a giant benchmark.

They are trying to be the strongest first signal.

If they work, people will immediately understand three things:

- the atlas can classify failures more cleanly
- the classification changes what should be repaired first
- the system can grow far beyond these four examples

That is enough for a flagship MVP.
