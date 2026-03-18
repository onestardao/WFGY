<!--
AI_NOTE_START

Document role:
This file is the first compact rollback example pack for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want concrete examples of how rollback should look after a harmful or misleading repair move.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Action Schema v1](./repair-action-schema-v1.md)
   - [Repair Validation Loop v1](./repair-validation-loop-v1.md)
   - [Rollback Policy v1](./rollback-policy-v1.md)
   - [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
   - [Repair Planner Spec v1](./repair-planner-spec-v1.md)
   - [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
   - [Repair Plan Schema v1](./repair-plan-schema-v1.json)
   - [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
   - [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
   - [Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
3. Use this page for onboarding, review calibration, demo support, and future rollback-aware semi-auto design.

What this file is:
- A compact rollback example pack
- A small evidence layer for rollback behavior
- A practical bridge between rollback policy rules and visible rollback cases

What this file is not:
- Not a full rollback benchmark set
- Not automated rollback execution
- Not proof that rollback is solved across all families
- Not a production-grade restoration test suite

Reading discipline for AI:
- Treat rollback as a normal branch of repair discipline, not as an embarrassment path.
- Keep rollback target, rollback reason, restore point, post-rollback state, and next step visible.
- Use these examples as small reference cases, not as universal templates for every repair failure.
- Stay especially cautious when extrapolating beyond F1, F4, F7, and limited F5.

AI_NOTE_END
-->

# Tiny Rollback Examples Pack v1 ↩️

## The first compact rollback reference pack for safe early Atlas-based repair actions

Quick links:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)
- [Open Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
- [Open Repair Action Schema v1](./repair-action-schema-v1.md)
- [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
- [Open Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
- [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
- [Open Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
- [Open Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
- [Open Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)
- [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)

---

If the rollback policy explains **when rollback should happen**, this pack shows **what rollback should look like in small, concrete cases**. 🧭

Its purpose is simple:

> show a few minimal rollback cases  
> so the Auto Repair layer can move from rollback policy rules  
> to concrete, inspectable rollback behavior

This file does **not** claim to be a full rollback benchmark set.

It claims something smaller and more useful:

> the project now has a first set of tiny rollback examples  
> for safe early repair actions in F1, F4, F7, and limited F5

---

## Quick start 🚀

### I want the shortest rollback reading

Use this path:

1. read one example ID and its failed action
2. inspect the rollback reason
3. inspect the restore point
4. inspect the post-rollback state
5. inspect the next step

### I want the stronger rollback reading

Use this page together with:

1. [Rollback Policy v1](./rollback-policy-v1.md)
2. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
3. [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)

Short version:

> see what failed  
> see what gets restored  
> see why rollback is correct  
> see what happens next ✨

---

## 1. Why this pack exists

The current Auto Repair layer already defines:

- when rollback should happen
- what rollback should restore
- how rollback relates to validation
- how rollback should connect to revision and escalation

But rules alone are not enough.

Without examples, rollback can still feel abstract.

This pack fills that gap.

It provides a few small examples that show:

- what repair action failed or caused harm
- what rollback target was chosen
- what restore point was used
- what the post-rollback state should look like
- what next step becomes reasonable

In short:

> this pack is the first small evidence layer for rollback behavior

---

## 2. What these examples are meant to prove

These examples are intentionally small.

They are not meant to prove:

- full rollback automation
- deployment-grade state restoration
- universal rollback correctness across all families

They are meant to prove something narrower:

1. a harmful or misleading repair can be identified
2. a restore point can be named clearly
3. rollback can be described locally and concretely
4. post-rollback state can be summarized
5. the workflow can continue safely after rollback

That is already very valuable.

---

## 3. Rollback examples quick map 🗂️

| Example | Main teaching focus |
|---|---|
| F1 example | rollback protects grounding truth when filtering over-prunes evidence |
| F4 example | rollback protects workflow usability when a gate becomes too restrictive |
| F7 example | rollback protects semantic fit when structure cleanup overshoots |
| limited F5 example | rollback protects diagnosability when visibility changes add noise instead of insight |

This page is the right place when the question is **what healthy rollback behavior looks like in practice**, not whether rollback has been fully automated.

---

## 4. Pack scope

This v1 pack includes four tiny rollback examples:

- one F1 example
- one F4 example
- one F7 example
- one limited F5 example

These were chosen because they are the best early families for:

- local repair actions
- visible local harm
- clear restore points
- simple rollback explanations

This pack intentionally does **not** include F6-heavy rollback cases.

Those remain too risky and too abstract for early tiny rollback samples.

---

## 5. Standard tiny rollback format

Each tiny rollback example uses the following structure:

1. Example ID
2. Family
3. Failed or harmful repair action
4. Rollback target
5. Rollback reason
6. Restore point
7. Post-rollback state
8. Next step
9. Why rollback is correct
10. Main teaching point

This format is intentionally small and reusable.

---

## Example 1 · F1 Tiny Rollback Example

### Example ID

`TRE_F1_001`

### Family

F1 · Grounding and Evidence Integrity

### Failed or harmful repair action

`F1_AF_001`  
Filter misleading adjacent anchors

### Rollback target

`F1_AF_001`

### Rollback reason

The filtering step removed misleading anchors, but it also removed the truly relevant source chunk.

The repair made the evidence set look cleaner, but semantic alignment with the real source became worse.

### Restore point

prior candidate evidence pool

### Post-rollback state

The earlier evidence pool is restored so the system no longer remains trapped in the over-pruned evidence state.

The grounding problem is still unresolved, but the case is no longer worse than before.

### Next step

`retry-with-alternate-action`

### Why rollback is correct

Rollback is correct because the repair damaged the target layer more than it improved it.

The local repair goal was grounding improvement, but the real outcome was harmful over-pruning.

### Main teaching point

A grounding repair should be rolled back if it creates a cleaner-looking but less truthful evidence set.

---

## Example 2 · F4 Tiny Rollback Example

### Example ID

`TRE_F4_001`

### Family

F4 · Execution and Contract Integrity

### Failed or harmful repair action

`F4_GT_001`  
Insert readiness gate

### Rollback target

`F4_GT_001`

### Rollback reason

The new readiness gate blocked the original premature execution, but it also blocked a valid downstream path that should have remained available.

The repair improved closure locally, but overshot the intended scope.

### Restore point

previous workflow gate configuration

### Post-rollback state

The over-restrictive gate is removed and the workflow returns to the earlier configuration.

The system regains the previous valid path, while the closure issue remains available for a narrower future repair.

### Next step

`revise`

### Why rollback is correct

Rollback is correct because the inserted gate created stronger collateral damage than the original local gain.

The target problem was premature execution, not total execution shutdown.

### Main teaching point

A closure repair should be rolled back if it blocks more than the failure it was meant to stop.

---

## Example 3 · F7 Tiny Rollback Example

### Example ID

`TRE_F7_001`

### Family

F7 · Representation and Localization Integrity

### Failed or harmful repair action

`F7_SC_001`  
Tighten output schema

### Rollback target

`F7_SC_001`

### Rollback reason

The schema tightening produced a valid structure, but semantic task fit degraded enough that the output became less useful.

The shell improved, but the content quality dropped too much.

### Restore point

prior schema version

### Post-rollback state

The earlier schema shell is restored so the case no longer remains trapped in a structurally valid but semantically degraded state.

The original representation issue is still present, but the system returns to the less harmful baseline.

### Next step

`re-check family fit`

### Why rollback is correct

Rollback is correct because the repair improved one visible dimension while worsening a more important functional dimension.

The action oversolved structure at the cost of task fidelity.

### Main teaching point

A container repair should be rolled back if structural cleanliness comes at too high a semantic cost.

---

## Example 4 · Limited F5 Tiny Rollback Example

### Example ID

`TRE_F5_001`

### Family

F5 · Observability and Diagnosability Integrity

### Failed or harmful repair action

`F5_LU_001`  
Add local logging uplift

### Rollback target

`F5_LU_001`

### Rollback reason

The additional logging exposed more detail, but it made the workflow noisier without improving actual diagnosability.

The repair increased visibility volume without improving failure-path clarity.

### Restore point

pre-observability patch state

### Post-rollback state

The added noisy logging layer is removed and the workflow returns to its prior signal level.

The case still needs observability work, but the system is no longer buried under low-value trace noise.

### Next step

`revise`

### Why rollback is correct

Rollback is correct because the repair improved information quantity but degraded practical diagnosability.

The problem was not only missing visibility.  
It was missing useful visibility.

### Main teaching point

An observability repair should be rolled back if it adds noise faster than it adds insight.

---

## 6. What these examples teach

Taken together, these tiny rollback examples teach four important lessons.

### Lesson 1

Rollback is not an embarrassment branch.  
It is a normal part of repair discipline.

### Lesson 2

A repair can improve one local feature and still deserve rollback.

### Lesson 3

Rollback depends on restore points being clear.

### Lesson 4

Rollback keeps the system from getting trapped in a worse local state.

---

## 7. Why these examples are useful

These tiny rollback examples are useful for at least four reasons.

### A. Validation support

They make rollback logic concrete after validation detects harm.

### B. Planner support

They teach the planner what kinds of actions are likely to overshoot.

### C. Demo support

They provide simple rollback cases for future repair demos.

### D. Future semi-auto support

They create the first tiny evidence base for safe rollback-aware semi-auto behavior.

---

## 8. What this pack does not yet include

Tiny Rollback Examples Pack v1 does **not** yet include:

- large rollback datasets
- benchmark-scale rollback evaluation
- F6-heavy rollback cases
- multi-step repair-chain rollback
- distributed restore behavior
- automated rollback execution code

Those can come later.

This pack is intentionally minimal.

---

## 9. Recommended next step

Once this pack exists, the next useful follow-up is one of these:

1. create a planner test note that uses both validation and rollback examples
2. create one tiny semi-auto repair demo spec using F1 or F4
3. create a small validator-and-rollback paired example sheet

The strongest immediate next step is probably:

> create a planner test note that shows how the planner, validation, and rollback layers connect on the same small cases

---

## 10. Next steps ✨

After this page, most readers continue with:

1. [Open Planner Test Note v1](./planner-test-note-v1.md)
2. [Open Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
3. [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
4. [Open Rollback Policy v1](./rollback-policy-v1.md)

If you want the broader product surface:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

---

## 11. One-line summary 🌍

**Tiny Rollback Examples Pack v1 provides the first small rollback examples for safe early Atlas-based repair actions in F1, F4, F7, and limited F5.**
