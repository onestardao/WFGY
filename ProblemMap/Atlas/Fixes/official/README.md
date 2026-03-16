<!--
AI_NOTE_START

Document role:
This file is the first official family-level repair-facing surface for Atlas v1.

How to use this file:
1. Read this file after:
   - [Atlas Final Freeze v1](../../atlas-final-freeze-v1.md)
   - [Canonical Casebook v1](../../canonical-casebook-v1.md)
   - [Atlas-to-AI Adapter v1](../../atlas-to-ai-adapter-v1.md)
2. Treat this document as the official first-repair layer of the atlas.
3. Use this file to determine:
   - what to try first after correct routing
   - what not to try first
   - when to escalate into deeper WFGY 3.0 exploration
   - when to look for community implementation packs
4. Do not use this document as a full deep repair manual for every node.

What this file is:
- The first official family-level fix surface
- A route-first repair grammar
- The official public-facing first repair layer

What this file is not:
- Not the full WFGY 3.0 experiment engine
- Not the complete node-by-node repair encyclopedia
- Not the final custom audit layer
- Not a guarantee that every real-world case is solved by one first move

Reading discipline for AI:
- Route first, then repair.
- Preserve the distinction between family-level first moves and deeper problem-specific experimental layers.
- Do not overpromise closure.
- Do not jump into downstream implementation details before the family cut is stable.

AI_NOTE_END
-->

# Family Fix Surface v1

## Problem Map 3.0 Troubleshooting Atlas
## Official First Repair Layer by Family

Quick links:

- [Back to Official Fixes](./README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Open the Flagship Runnable Demo Pack](./demos/README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)

---

This document is the **first official family-level repair-facing surface** for the Atlas system.

If you arrived here from the official fixes hub, this is the page that answers the next practical question:

> After correct routing, what should be tried first?

The atlas tells you where the failure lives.  
This document tells you what to try first after that cut is stable.

It sits after routing and before deeper experimentation.

Its goal is not to explain every implementation detail.  
Its goal is to provide a stable, reusable, public-facing first repair grammar.

---

## Quick start

Use this page in the following order:

1. scan the **Family quick map**
2. jump to your primary family
3. read:
   - **What this family is trying to restore**
   - **First repair moves**
   - **Common misrepair**
4. only then decide whether escalation is needed
5. use deeper bridge material only when the first family-level move is not enough

If you want the shortest practical rule:

> route first  
> choose the first repair move  
> avoid the common wrong first move  
> escalate only if needed

---

## Family quick map

| Family | What to restore first | First repair instinct |
|---|---|---|
| F1 | evidence and reality anchor | re-ground first |
| F2 | viable reasoning path | stabilize the progression path first |
| F3 | continuity and state ownership | restore the thread first |
| F4 | readiness, bridge, and closure | repair the skeleton first |
| F5 | diagnosability and visibility | expose the failure path first |
| F6 | viable boundary and control corridor | restore the boundary first |
| F7 | representation carrier and structural fidelity | repair the container first |

---

## What this document is

This document is the **official first repair layer** of the atlas.

Its job is to provide:

- family-level first repair moves
- family-level misrepair warnings
- escalation guidance
- a stable public fix surface

In short:

> the atlas says where the failure lives  
> this document says what to try first

---

## What this document does not do

This document does **not** try to do all repair work at once.

It does **not** provide:

- a full node-by-node repair encyclopedia
- the full WFGY 3.0 experimental layer
- every possible domain-specific implementation
- every possible Colab or JSON artifact
- full custom architectural diagnosis

This document is intentionally narrower.

It focuses on:

> **family-level first repair guidance**

That makes it useful, teachable, and stable.

---

## How to use this file in practice

A practical use sequence should look like this:

### Step 1

Route the case using:

- [Atlas Final Freeze v1](../../atlas-final-freeze-v1.md)
- [Canonical Casebook v1](../../canonical-casebook-v1.md)
- [Atlas-to-AI Adapter v1](../../atlas-to-ai-adapter-v1.md)

### Step 2

Use this file to choose:

- what to try first
- what not to try first
- whether escalation is needed

### Step 3

If deeper work is needed, move into:

- [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md)
- community fix packs
- or more experimental problem-specific layers

This keeps the repair flow clean:

> route  
> first repair  
> escalate  
> implement

---

## Core repair discipline

The Fix Surface layer must obey the following order.

### Step 1 · Route the case correctly

Identify:

- primary family
- secondary family
- broken invariant
- best current fit

### Step 2 · Apply the first repair move

Choose the family-level first move that best matches the routed failure region.

### Step 3 · Avoid the common misrepair

Each family has common wrong first moves.  
Avoiding these is often as important as choosing the first correct move.

### Step 4 · Escalate when needed

If the case remains stubborn, underdetermined, or high-pressure:

- bridge into deeper WFGY 3.0 exploration
- use a community fix pack
- or move into a stronger experiment or implementation layer

Short version:

> **route first  
> repair second  
> escalate third**

---

## Family-level fix grammar

Each family section below uses the same structure:

1. what the family is trying to restore
2. what to try first
3. what not to try first
4. when to escalate
5. what kind of deeper layer may help

This keeps the repair surface teachable and reusable.

---

# F1 · Grounding & Evidence Integrity

## What F1 is trying to restore

F1 tries to restore correct alignment between output and:

- evidence anchors
- truth-like anchors
- world anchors
- semantic targets
- deployment reality

The repair goal is:

> reconnect the output to what it is supposed to be about

---

## First repair moves

Try these first:

- re-ground the case against the correct evidence source
- verify the source-to-claim chain
- compare the output against the real target, not just a proxy
- trace chunk-to-answer or source-to-answer alignment
- re-check whether the model is using the right world anchor at all

---

## Common misrepair

Do **not** start by:

- polishing style
- rewriting tone
- adding decorative chain-of-thought language
- tweaking wording while leaving the anchor broken
- treating semantic similarity as proof of real grounding

In many F1 cases, the system can sound more fluent while still being fundamentally wrong.

---

## Escalate when needed

Escalate when:

- the world anchor remains unclear
- there are multiple possible referents
- synthetic or truth-like extraction is involved
- train / deploy mismatch is likely
- grounding appears to fail differently across environments

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- truth-like extraction analysis
- policy-to-world bridging
- OOD grounding exploration
- deployment-grounding stress design
- explicit falsifiable grounding experiments

---

## One-line repair summary

**First reattach the output to the right anchor. Do not waste the first move on style.**

---

# F2 · Reasoning & Progression Integrity

## What F2 is trying to restore

F2 tries to restore stable movement through reasoning space.

The repair goal is:

> re-establish a viable progression path

This may involve:

- interpretation reset
- decomposition repair
- continuity restoration inside the reasoning path
- collapse detection and recovery

---

## First repair moves

Try these first:

- decompose the task into smaller stable steps
- insert checkpoints into the reasoning path
- test alternate parses of the problem
- reduce recursive depth when collapse is suspected
- isolate the first place where progression becomes invalid

---

## Common misrepair

Do **not** start by:

- adding more raw context without restructuring the path
- treating a progression failure as pure style failure
- assuming every reasoning failure is a representation failure
- expanding the chain blindly when the chain is already unstable
- jumping to high-level philosophical framing before basic path stability is restored

---

## Escalate when needed

Escalate when:

- recursive instability is strong
- collapse-recovery loops keep repeating
- a symbolic progression branch is failing under pressure
- the system can start but cannot stay viable through long chains

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- recursive horizon experiments
- long-chain reasoning stress tests
- recovery protocol design
- decomposition strategy comparison
- explicit collapse / recovery experiment harnesses

---

## One-line repair summary

**First restore a viable reasoning path. Do not make the path longer before making it stable.**

---

# F3 · State & Continuity Integrity

## What F3 is trying to restore

F3 tries to restore continuity across:

- memory
- role
- ownership
- session thread
- agent thread
- viable state-space

The repair goal is:

> make the right state persist in the right way

---

## First repair moves

Try these first:

- restore memory persistence or continuity checkpoints
- fence roles and responsibilities clearly
- trace ownership of state and outputs
- rebuild continuity across turns, sessions, or agents
- identify where viable state-space was lost

---

## Common misrepair

Do **not** start by:

- adding more instructions while continuity remains broken
- assuming every continuity issue is just a workflow issue
- patching execution scaffolds before checking state ownership
- treating role contamination as mere formatting confusion
- throwing in more memory context without role discipline

---

## Escalate when needed

Escalate when:

- multiple agents or threads are interacting
- ownership lines are ambiguous
- continuity is drifting without obvious execution collapse
- the system remains active but no longer viable as the same stateful process

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- multi-agent continuity experiments
- ownership line analysis
- interaction-thread drift testing
- viable-state restoration strategies
- persistent-state stress harnesses

---

## One-line repair summary

**First restore continuity and state ownership. Do not assume more instructions will repair a broken thread.**

---

# F4 · Execution & Contract Integrity

## What F4 is trying to restore

F4 tries to restore operational closure across:

- readiness
- ordering
- liveness
- bridge integrity
- protocol closure
- enforcement skeletons

The repair goal is:

> make the workflow actually close

---

## First repair moves

Try these first:

- check readiness and preconditions
- validate ordering dependencies
- test bridge integrity across modules or steps
- identify deadlock or liveness failure points
- trace whether the rule-to-action path truly closes

---

## Common misrepair

Do **not** start by:

- treating execution deadlock as a reasoning problem
- changing prompts while a bridge remains broken
- assuming policy exists just because a rule was written
- polishing outputs before the workflow closes
- rewriting explanations while liveness remains dead

---

## Escalate when needed

Escalate when:

- there are hidden ordering dependencies
- multiple layers depend on each other
- fallback logic exists in name only
- institutional or protocol enforcement drift is present
- the workflow “looks alive” but cannot actually complete

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- closure-path experiments
- bridge integrity tests
- readiness / deployment harnesses
- protocol or contract stress mapping
- fallback realism validation

---

## One-line repair summary

**First restore operational closure. Do not ask the system to think better before it can even close the loop.**

---

# F5 · Observability & Diagnosability Integrity

## What F5 is trying to restore

F5 tries to restore visibility into:

- failure paths
- coherence conditions
- audit routes
- warning structure
- fragility signals
- meaning profiles

The repair goal is:

> make the failure visible enough to diagnose honestly

---

## First repair moves

Try these first:

- insert observability into the failure path
- expose trace structure
- add coherence probes
- inspect the warning horizon
- improve auditability before acting on abstract interpretations

---

## Common misrepair

Do **not** start by:

- jumping into regime intervention before visibility exists
- treating opacity as proof of boundary failure
- escalating to global theory when local observability is missing
- assuming the first fluent explanation is the right one
- repairing structure you still cannot see clearly

---

## Escalate when needed

Escalate when:

- pre-failure warning is weak
- coherence is hard to inspect
- interpretability pressure is scaling
- the system might be entering a more serious boundary or regime failure but cannot yet be confirmed

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- warning-horizon experiments
- fragility signature testing
- auditability design
- value / information coherence tracing
- high-abstract diagnosability mapping

---

## One-line repair summary

**First make the failure visible. Do not intervene at the highest level before the structure is diagnosable.**

---

# F6 · Boundary & Safety Integrity

## What F6 is trying to restore

F6 tries to restore viable boundaries across:

- goals
- control
- incentives
- collective structure
- safe corridors
- regime behavior

The repair goal is:

> bring the system back inside a viable boundary

---

## First repair moves

Try these first:

- inspect alignment or control path integrity
- identify incentive drift or capture
- test whether the system is still inside a safe corridor
- examine whether collective boundaries are eroding
- separate proxy optimization from true target structure

---

## Common misrepair

Do **not** start by:

- adding more observability alone when the boundary is already failing
- assuming all F6 problems are just better-interpretability problems
- rewriting goals without checking control paths
- treating collective regime drift as a local style or logging issue
- delaying stabilization while waiting for perfect explanation

---

## Escalate when needed

Escalate when:

- collective overshoot is likely
- incentive amplification is strong
- control paths are weakening fast
- boundary damage is already active, not just predicted

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- corridor stability analysis
- overshoot / runaway regime experiments
- incentive tension mapping
- collective-boundary stress design
- intervention margin analysis

---

## One-line repair summary

**First restore the boundary. Do not mistake a real boundary breach for a visibility problem alone.**

---

# F7 · Representation & Localization Integrity

## What F7 is trying to restore

F7 tries to restore structural fidelity across:

- symbolic shells
- formal containers
- layouts
- local anchors
- explanations
- synthetic structures

The repair goal is:

> make the container faithful enough to carry the structure again

---

## First repair moves

Try these first:

- audit descriptor fidelity
- check whether the formal container is adequate
- validate layout and local anchoring
- test whether symbolic structure is being preserved
- inspect hierarchy or skeleton integrity

---

## Common misrepair

Do **not** start by:

- expanding reasoning chains when the container itself is broken
- assuming semantic grounding is always the first problem
- patching style before repairing structural fidelity
- treating layout or symbolic distortion as superficial
- using richer explanation text to hide a broken carrier

---

## Escalate when needed

Escalate when:

- synthetic structure is unstable
- formal adequacy is unclear
- descriptor drift is severe
- local anchors are failing under pressure
- the structure looks complete but carries the wrong internal geometry

---

## Deeper bridge direction

Use deeper WFGY 3.0 exploration when the case needs:

- formal adequacy experiments
- descriptor fidelity tests
- synthetic structure stress design
- hierarchy preservation checks
- representation drift analysis

---

## One-line repair summary

**First repair the container. Do not demand better reasoning from a broken carrier.**

---

## Cross-family repair discipline

Not every case will remain cleanly inside one family.

That is why the official fix surface must preserve cross-family discipline.

### F1 / F7

- if the output is detached from reality or evidence, repair grounding first
- if the structure carrying the meaning is distorted, repair the container first

### F5 / F6

- if you still cannot see the failure clearly, repair diagnosability first
- if the system is already outside a viable boundary, repair the boundary first

### F3 / F4

- if the thread is broken, repair continuity first
- if the loop cannot close, repair execution first

### F2 / F7

- if the carrier is broken, repair representation first
- if the carrier is acceptable but the path collapses, repair progression first

These cuts matter because many bad fixes begin by repairing the wrong family.

---

## Misrepair pattern summary

A wrong first move often looks like one of these:

- fixing tone when grounding is broken
- adding instructions when continuity is broken
- changing prompts when the workflow cannot close
- intervening at a regime level when observability is missing
- adding explanation when the boundary is already breached
- extending reasoning when the representation carrier is already damaged

This is why route-first discipline matters so much.

---

## Relationship to WFGY 3.0

This official fix surface is intentionally **lighter** than WFGY 3.0.

### This document gives:

- family-level first repair moves
- first common mistakes
- escalation direction
- first bridge to deeper work

### WFGY 3.0 gives:

- deeper experimental reasoning
- problem-specific MVP exploration
- stronger tension-based analysis
- falsifiable structural exploration
- deeper reusable repair pathways

Short version:

> **this document gives first repair grammar**  
> **WFGY 3.0 gives deeper experimental repair exploration**

That means this file is a public first layer, not the entire engine.

---

## Relationship to community fixes

This file is the official surface.  
It should remain stable and compact.

Community-contributed fixes may later extend this surface with:

- Colab notebooks
- JSON schemas
- prompt packs
- workflow examples
- benchmark reruns
- reproduction packs

But community growth should attach to this official grammar, not replace it.

That is why this file belongs inside the official fix layer.

---

## Document status

This document is frozen as **Family Fix Surface v1**.

It is frozen not because the entire repair universe is finished, but because the atlas now has a stable enough first repair grammar to support:

- human troubleshooting
- AI-assisted first repair guidance
- demo flows
- onboarding
- route-first repair discipline
- bridge escalation into WFGY 3.0 and community fix packs

Future work should proceed through **fix-layer patch mode**, not by silently changing the official first repair grammar.

---

## Patch protocol

Family Fix Surface v1 is frozen, but not closed.

### Small patch

Use for:

- wording refinement
- stronger first-move phrasing
- clearer misrepair warnings
- better escalation guidance

### Medium patch

Use for:

- adding family-level examples
- adding new stable first-repair distinctions
- improving cross-family repair discipline
- integrating stronger official bridge notes

### Large patch

Only use if:

- family-level first moves repeatedly fail under stable routing
- the official first repair grammar becomes structurally misleading
- the relationship between family routing and first repair must be redesigned

### Current status

No large-patch pressure is currently justified.

---

## Official status

The correct formal statement is:

> Family Fix Surface v1 is the first frozen official repair-facing layer of Problem Map 3.0 Troubleshooting Atlas.  
> It defines family-level first repair moves, common misrepair patterns, and escalation directions while preserving route-first discipline.

---

## Next steps

After this page, most readers continue with:

1. [Misrepair Patterns v1](./misrepair-patterns-v1.md)
2. [Flagship Runnable Demo Pack](./demos/README.md)
3. [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md)
4. [Back to Official Fixes](./README.md)

If you want to return to the broader product surface:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)

If this page helps your workflow, consider:

- [starring the WFGY repo](https://github.com/onestardao/WFGY)
- opening an issue
- testing the official demo pack
- contributing later through the community layer

---

## One-line version

**Family Fix Surface v1 tells you what to try first after correct atlas routing.**

---

## Closing note

A strong atlas should not stop at naming failures.

It should also help people and AI systems take a better first action.

That is what this file is for.

It does not promise total closure.  
It gives a disciplined first move.
