<!--
AI_NOTE_START

Document role:
This file is the main entry page for the Auto Repair v1 package inside the Atlas Fixes layer.

How to use this file:
1. Read this page before using or extending any Auto Repair v1 document.
2. Use this page to understand what Auto Repair v1 does, what it does not do, and where it sits in the larger Atlas system.
3. Use this page as the primary navigation hub for the Auto Repair package.
4. After reading this page, readers will usually continue into:
   - architecture
   - repair schemas
   - planner layer
   - validation and rollback
   - demo and bridge materials

What this file is:
- The package-level hub for Auto Repair v1
- A positioning document for controlled repair after Atlas routing
- A navigation page for the main Auto Repair documents
- A boundary page between Atlas diagnosis, controlled repair, and deeper WFGY continuation

What this file is not:
- Not proof that full autonomous repair is solved
- Not the official Atlas routing layer
- Not a production-grade closed-loop repair executor
- Not a replacement for WFGY 3.0 deeper continuation

Reading discipline for AI:
- Preserve the distinction between Atlas routing, Fix Surface, Auto Repair, and WFGY continuation.
- Do not overclaim autonomous repair from this package.
- Treat this folder as a controlled-repair layer that starts after routing.
- Keep validation, rollback, and escalation logic visible.

AI_NOTE_END
-->

# Auto Repair v1 🛠️

## Controlled repair planning after Atlas routing

Quick links:

- [Back to Fixes Hub](../README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)
- [Open Family Fix Surface v1](../official/family-fix-surface-v1.md)
- [Open Misrepair Patterns v1](../official/misrepair-patterns-v1.md)
- [Open Atlas to WFGY Bridge v1](../official/atlas-to-wfgy-bridge-v1.md)

---

If the Atlas is the layer that decides **where the failure lives**, Auto Repair v1 is the next layer that turns that diagnosis into a **controlled repair workflow**. 🧭

This folder does **not** claim that fully autonomous repair is already solved.

What it does claim is narrower and more useful:

> the Atlas now has a clear path from  
> **route → first repair direction → repair planning → validation → rollback or escalation**

This folder exists to define that path clearly, safely, and in a way that can grow without silently breaking the current system.

---

## Quick start 🚀

### I am new here

Use this path:

1. read this README first
2. open the architecture page
3. inspect the repair action schema
4. inspect the validation loop and rollback policy
5. inspect the planner layer
6. inspect the worked bridge into deeper WFGY continuation

### I already know the Atlas and want the shortest route

Start here:

1. [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
2. [Repair Action Schema v1](./repair-action-schema-v1.md)
3. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
4. [Rollback Policy v1](./rollback-policy-v1.md)
5. [Repair Planner Spec v1](./repair-planner-spec-v1.md)

Short version:

> route first  
> repair second  
> validate always  
> rollback or escalate when needed ✨

---

## What Auto Repair means here

In this project, **auto repair** does **not** mean:

- an AI blindly changing prompts
- an AI guessing random fixes
- an AI claiming full root-cause closure by itself
- a magic one-shot repair engine
- unrestricted autonomous intervention

Instead, Auto Repair means:

> a structured repair layer that starts **after Atlas routing**  
> and turns diagnosis into a controlled repair workflow

In practical terms, the intended flow is:

1. route the case with the Atlas
2. identify the likely failure family and broken invariant
3. choose the most appropriate first repair family
4. generate a constrained repair plan
5. validate whether the repair improved the case
6. accept, revise, rollback, or escalate if needed

So this folder is not a replacement for the Atlas.

It is the **next layer** that depends on Atlas routing being correct first.

---

## Where this sits in the full system 🧩

The current system can be understood like this:

```text
Problem Map 3.0
→ Troubleshooting Atlas
→ Canonical Casebook
→ Atlas-to-AI Adapter
→ Fix Surface
→ Auto Repair
→ WFGY 3.0 deeper continuation
````

The key distinction is:

* **Atlas** decides where the failure belongs
* **Fix Surface** suggests the first repair direction
* **Auto Repair** turns that into a structured repair workflow
* **WFGY 3.0** remains the deeper repair and experiment grammar for harder or more structurally unresolved cases

This means Auto Repair is a **bridge layer**, not the final repair engine.

Short version:

> Atlas finds where the failure lives.
> Auto Repair decides the first controlled move.
> WFGY 3.0 continues when local repair is not enough.

---

## Auto Repair quick map 🗂️

| Layer       | Main job                                        | Typical output                                                  |
| ----------- | ----------------------------------------------- | --------------------------------------------------------------- |
| Atlas       | classify the failure                            | route, family, broken invariant hypothesis                      |
| Fix Surface | suggest the first repair direction              | first repair family or move                                     |
| Auto Repair | turn diagnosis into controlled workflow         | repair plan, validation path, rollback or escalation            |
| WFGY 3.0    | continue deeper when local repair is not enough | deeper continuation, stronger restructuring, harder experiments |

This folder is the right place when the goal is **controlled repair planning after routing**, not just diagnosis and not full autonomous execution.

---

## Current status of v1 📌

**Current status: first formal controlled-repair package established**

Auto Repair v1 is no longer just a vague planning note.

At this stage, this folder already defines and includes:

* architecture
* repair action schema
* validation loop
* rollback discipline
* planner specification
* planner prompt
* repair plan schema
* semi-auto repair scope
* safe early action catalog
* tiny validation examples
* tiny rollback examples
* planner test and review notes
* tiny planner output examples
* tiny semi-auto demo spec
* tiny semi-auto demo pack
* Atlas-to-WFGY bridge
* worked escalation examples
* quickstart for WFGY deeper continuation
* integrated handoff
* freeze boundary note

So v1 is still intentionally limited, but it is no longer just future idea space.

It is now a real structured package.

---

## What this folder already delivers ✅

### A. Core structure layer

This layer defines what Auto Repair is and how it should grow.

Files include:

* [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
* [Repair Action Schema v1](./repair-action-schema-v1.md)
* [Repair Validation Loop v1](./repair-validation-loop-v1.md)
* [Rollback Policy v1](./rollback-policy-v1.md)
* [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)

### B. Planner and scope layer

This layer defines how diagnosis becomes first repair planning.

Files include:

* [Repair Planner Spec v1](./repair-planner-spec-v1.md)
* [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
* [Repair Plan Schema v1](./repair-plan-schema-v1.json)
* [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
* [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)

### C. Example and review layer

This layer makes the planner, validation, and rollback logic visible and testable.

Files include:

* [Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
* [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
* [Planner Test Note v1](./planner-test-note-v1.md)
* [Planner Review Checklist v1](./planner-review-checklist-v1.md)
* [Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)

### D. Demo and bridge layer

This layer shows how the system becomes visible, teachable, and bridgeable into deeper WFGY continuation.

Files include:

* [Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
* [Tiny Semi Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)
* [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
* [Worked Escalation Example v1](./worked-escalation-example-v1.md)
* [Worked Escalation Example F4 v1](./worked-escalation-example-f4-v1.md)
* [WFGY 3.0 Deeper Continuation Quickstart v1](./wfgy-3-0-deeper-continuation-quickstart-v1.md)

### E. Package boundary and handoff layer

This layer defines how the package should be read, handed off, and frozen.

Files include:

* [Auto Repair Integrated Handoff v1](./auto-repair-integrated-handoff-v1.md)
* [Auto Repair Freeze Note v1](./auto-repair-freeze-note-v1.md)

---

## Why this folder matters

The Atlas already does something very important:

* it classifies failures
* it distinguishes neighboring failure regions
* it suggests the first repair move

But there is still a gap between:

> this is probably an F4 failure

and

> here is a safe, structured, validation-aware repair workflow for that F4 failure

This folder exists to close that gap.

It is the place where the project begins to move from:

* diagnosis only

toward:

* diagnosis plus controlled repair planning

That shift is a big deal, so it needs its own clear layer.

---

## Scope of Auto Repair v1

### Included in v1 ✅

Auto Repair v1 currently covers:

* system positioning
* architecture explanation
* planner layer
* repair action schema direction
* validation loop direction
* rollback discipline
* semi-auto repair scope
* safe early action catalog
* tiny example packs
* tiny demo packs
* Atlas-to-WFGY bridge logic
* worked escalation examples
* quickstart continuation guidance
* freeze and handoff boundary

### Not included in v1 ⏳

Auto Repair v1 does **not** yet include:

* full executable repair engine
* broad autonomous patch generation
* broad automated verification across all families
* full closed-loop autonomous repair
* aggressive high-risk intervention for F6-heavy regions
* benchmark-scale repair orchestration
* production-grade executor logic
* notebook-grade or live execution for all demo paths

So this README describes a **real v1 package**, but not a final autonomous repair engine.

---

## Best early candidate families

For early Auto Repair development, the safest and strongest starting regions remain:

### F1 · Grounding and Evidence Integrity

Good early targets:

* re-grounding
* evidence filtering
* anchor re-check
* chunk-to-target correction

Why it is a good first target:

* the repair surface is relatively concrete
* before and after comparison is easier
* misrepair is easier to detect

### F4 · Execution and Contract Integrity

Good early targets:

* readiness gate insertion
* ordering validation
* block-until-ready logic
* closure-path hardening

Why it is a good first target:

* many failures are workflow-structural
* repair actions are often explicit
* success conditions are often clear

### F7 · Representation and Localization Integrity

Good early targets:

* schema tightening
* JSON shell correction
* descriptor tightening
* container validation

Why it is a good first target:

* structure is often visible
* repair outcomes are inspectable
* replay demos are easier to build

---

## Higher-risk regions ⚠️

Some areas should still be treated much more carefully.

### F5

Auto Repair can help with:

* observability uplift
* trace insertion
* logging suggestions

But there is risk in mistaking visibility improvement for full repair.

### F3

Some continuity scaffolds may be possible, but deeper continuity repair can get complicated quickly.

### F6

This is **not** a good place for aggressive early auto repair.

Boundary-heavy cases often require:

* judgment
* intervention restraint
* explicit escalation
* stronger human review

Early F6 work should lean toward:

* planner mode
* warning mode
* stabilization suggestions

not broad automatic execution.

---

## Relationship to WFGY 3.0 🌊

Auto Repair should not be misread as replacing WFGY 3.0.

The correct relationship is:

* **Atlas** handles diagnosis
* **Auto Repair** handles the first controlled repair move
* **WFGY 3.0** handles deeper continuation when local repair is insufficient

This usually happens when:

* local repair helps only partially
* the deeper effective-layer encoding remains weak
* stronger observables are needed
* mismatch logic remains too shallow
* the case keeps returning revise, rollback, or escalate
* local fixes improve symptoms without stabilizing structure

### Official WFGY 3.0 TXT

Use this official TXT as the deeper continuation asset:

* [WFGY 3.0 Singularity Demo TXT](https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt)

Shortest practical reading:

> Start with Atlas.
> Try the first controlled Auto Repair move.
> If local repair is not enough, continue with WFGY 3.0.

---

## Recommended reading order 📚

If you are new to this folder, read in this order.

### Step 1 · Foundation

1. [README](./README.md)
2. [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
3. [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)

### Step 2 · Operational core

4. [Repair Action Schema v1](./repair-action-schema-v1.md)
5. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
6. [Rollback Policy v1](./rollback-policy-v1.md)

### Step 3 · Planner layer

7. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
8. [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
9. [Repair Plan Schema v1](./repair-plan-schema-v1.json)

### Step 4 · Scope and action shelf

10. [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
11. [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)

### Step 5 · Tiny evidence layer

12. [Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
13. [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
14. [Planner Test Note v1](./planner-test-note-v1.md)
15. [Planner Review Checklist v1](./planner-review-checklist-v1.md)
16. [Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)

### Step 6 · Demo and bridge layer

17. [Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
18. [Tiny Semi Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)
19. [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
20. [Worked Escalation Example v1](./worked-escalation-example-v1.md)
21. [Worked Escalation Example F4 v1](./worked-escalation-example-f4-v1.md)
22. [WFGY 3.0 Deeper Continuation Quickstart v1](./wfgy-3-0-deeper-continuation-quickstart-v1.md)

### Step 7 · Freeze and handoff layer

23. [Auto Repair Integrated Handoff v1](./auto-repair-integrated-handoff-v1.md)
24. [Auto Repair Freeze Note v1](./auto-repair-freeze-note-v1.md)

---

## Safety boundary 🚧

Auto Repair must stay disciplined.

The following rules remain non-negotiable:

1. **Route first, repair second**
   Auto Repair should never skip Atlas routing.

2. **First controlled move only**
   Early versions should focus on the first repair move, not pretend to solve everything.

3. **Validation is mandatory**
   A repair proposal without a validation path is incomplete.

4. **Rollback must exist**
   If a repair makes the system worse, the workflow must support backing out.

5. **Not all families are equally safe for early semi-auto repair**
   F1, F4, and F7 remain the best early targets.

6. **No silent WFGY escalation**
   If a case escalates into WFGY 3.0, that transition should be explicit and justified.

---

## What future work should not do

Future work should **not** do the following:

* silently rewrite the core workflow
* overclaim autonomous repair
* treat tiny demos as proof of full repair power
* push F6-heavy intervention too early
* blur Atlas, Auto Repair, and WFGY 3.0 into one vague layer

The layered relationship is one of the most valuable parts of the whole design.

---

## What future work should do

Recommended next directions include:

* thicken the action library
* add more worked escalation examples
* improve WFGY continuation guidance
* grow from tiny markdown demos toward replay, JSON, or notebook demos
* define a future constrained executor boundary without pretending it already exists

---

## Official v1 interpretation

The correct interpretation of Auto Repair v1 is:

> the first formal controlled-repair package for Atlas-based repair has now been established,
> but broad autonomous repair execution remains future work.

This wording is strong, honest, and safe.

---

## Next steps ✨

After this page, most readers continue with:

1. [Open Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
2. [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
4. [Open Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)

If you want the broader product surface:

* [Back to Fixes Hub](../README.md)
* [Back to Official Fixes](../official/README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## One-line status 🌍

**Auto Repair v1 is now established as the first controlled repair layer between Atlas diagnosis and deeper WFGY 3.0 continuation.**
