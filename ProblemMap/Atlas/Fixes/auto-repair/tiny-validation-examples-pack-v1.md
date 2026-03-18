<!--
AI_NOTE_START

Document role:
This file is the first compact validation example pack for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want small concrete examples of how Atlas-based repair should be validated after a local action.
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
3. Use this page for onboarding, planner calibration, demo support, and future validator-oriented review.

What this file is:
- A compact validation example pack
- A small evidence layer for before-and-after repair validation
- A practical bridge between validation rules and visible validation behavior

What this file is not:
- Not a full benchmark set
- Not automated validator code
- Not a full repair benchmark corpus
- Not proof that every repair action is already validated at scale

Reading discipline for AI:
- Treat these examples as local validation references, not as universal templates for all repair cases.
- Keep target action, validation target, before state, after state, verdict, and rationale visible.
- Prefer concrete before-and-after reasoning over vague success language.
- Distinguish clearly between accept-style and revise-style validation outcomes.

AI_NOTE_END
-->

# Tiny Validation Examples Pack v1 🔍

## The first compact before-and-after validation reference pack for Atlas-based repair

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
- [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)
- [Open Tiny Semi-Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
- [Open Tiny Semi-Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)

---

If the validation loop explains **how repair should be judged**, this pack shows **what a few compact validation judgments should actually look like in practice**. 🧭

Its purpose is simple:

> show a few minimal before/after validation examples  
> so the Auto Repair layer can move from abstract rules  
> to concrete, inspectable validation behavior

This file does **not** claim to be a full benchmark set.

It claims something smaller and more useful:

> the project now has a first set of tiny validation examples  
> for safe early repair actions in F1, F4, F7, and one cautious F7 revise case

---

## Quick start 🚀

### I want the shortest validation reading

Use this path:

1. read one example ID
2. inspect the target action and validation target
3. compare the before state and after state
4. inspect the validation verdict
5. read why the verdict is correct

### I want the stronger validation reading

Use this page together with:

1. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
2. [Repair Action Schema v1](./repair-action-schema-v1.md)
3. [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
4. [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)

Short version:

> check what action was tried  
> check what changed  
> check what the verdict is  
> check why that verdict makes sense ✨

---

## 1. Why this pack exists

The current Auto Repair layer already has:

- architecture
- action schema
- planner logic
- validation logic
- rollback logic
- scope discipline
- safe early action catalog

But without concrete examples, those layers can still feel too abstract.

This pack fills that gap.

It provides a few small examples that show:

- what action was selected
- what was validated
- what changed before and after
- what verdict was reached
- why the verdict makes sense

In short:

> this pack is the first small evidence layer for Auto Repair validation

---

## 2. What these examples are meant to prove

These examples are intentionally small.

They are not meant to prove:

- full autonomous repair
- full benchmark performance
- universal repair correctness

They are meant to prove something narrower:

1. a small repair action can be selected cleanly
2. a clear validation target can be named
3. before and after states can be compared
4. the system can produce a usable verdict
5. the repair logic can be explained without ambiguity

That is already very valuable.

---

## 3. Validation examples quick map 🗂️

| Example | Main teaching focus |
|---|---|
| F1 example | grounding repair should be judged by anchor alignment |
| F4 example | execution repair should be judged by closure correctness |
| F7 accept-style example | structure repair can earn accept when local container fidelity clearly improves |
| F7 revise-style example | cleaner structure does not always justify full accept |

This page is the right place when the question is **what small good validation examples should look like**, not whether the whole repair layer is already benchmarked.

---

## 4. Pack scope

This v1 pack includes four tiny examples:

- one F1 example
- one F4 example
- one F7 accept-style example
- one F7 revise-style example

These were chosen because they are the best early families for:

- local actions
- visible changes
- simple validation targets
- reversible repair moves

This pack intentionally does **not** include F6-heavy examples.

Those remain too risky for early tiny validation samples.

---

## 5. Standard tiny example format

Each tiny validation example uses the following structure:

1. Example ID
2. Family
3. Target action
4. Validation target
5. Before state
6. After state
7. Validation verdict
8. Why this verdict is correct
9. Main teaching point

This format is intentionally small and reusable.

---

## Example 1 · F1 Tiny Validation Example

### Example ID

`TVE_F1_001`

### Family

F1 · Grounding and Evidence Integrity

### Target action

`F1_RG_001`  
Re-ground evidence set

### Validation target

anchor alignment

### Before state

The answer is fluent and plausible, but it is grounded in a semantically adjacent source chunk rather than the intended source.

The local failure looks like:

- evidence is nearby
- wording looks reasonable
- source alignment is wrong

### After state

The evidence set is replaced with a better-aligned source group.

The answer is now tied to the intended source target.

The local state now looks like:

- evidence anchor is corrected
- source alignment improves
- answer is more tightly attached to the right support

### Validation verdict

`accept`

### Why this verdict is correct

The target invariant improved:

- evidence-anchor integrity is stronger
- no meaningful collateral damage is visible
- the action remained local and reversible

### Main teaching point

A grounding repair should be judged by **anchor alignment**, not by style or fluency alone.

---

## Example 2 · F4 Tiny Validation Example

### Example ID

`TVE_F4_001`

### Family

F4 · Execution and Contract Integrity

### Target action

`F4_GT_001`  
Insert readiness gate

### Validation target

readiness state

### Before state

A downstream action is available and is executed before upstream readiness is complete.

The local failure looks like:

- a draft exists
- approval is incomplete
- execution still moves forward

### After state

A local readiness gate is inserted.

The downstream step is now blocked until upstream readiness is satisfied.

The local state now looks like:

- execution no longer starts too early
- the workflow respects readiness order
- closure becomes more stable

### Validation verdict

`accept`

### Why this verdict is correct

The target invariant improved:

- closure integrity is stronger
- premature execution is prevented
- rollback remains clear because the gate can be removed if needed

### Main teaching point

Execution repair should be judged by **closure correctness**, not by whether the system appears more active.

---

## Example 3 · F7 Tiny Validation Example

### Example ID

`TVE_F7_001`

### Family

F7 · Representation and Localization Integrity

### Target action

`F7_SC_001`  
Tighten output schema

### Validation target

schema validity

### Before state

The content is partly correct, but the structured shell is broken.

The local failure looks like:

- field boundaries leak
- object shape is invalid
- output cannot be reliably consumed downstream

### After state

The schema shell is tightened and the output boundary is restored.

The local state now looks like:

- structure is valid
- field boundaries hold
- downstream consumption becomes possible

### Validation verdict

`accept`

### Why this verdict is correct

The target invariant improved:

- container fidelity is stronger
- the repaired structure is clearly more usable
- the change is inspectable and reversible

### Main teaching point

A container repair should be judged by **structural validity**, not by content plausibility alone.

---

## Example 4 · F7 Partial Validation Example

### Example ID

`TVE_F7_002`

### Family

F7 · Representation and Localization Integrity

### Target action

`F7_DR_001`  
Repair descriptor shell

### Validation target

descriptor fidelity

### Before state

The output task descriptor is weak and under-specified.

This causes unstable structured output.

### After state

The descriptor becomes stricter and the structure becomes cleaner.

However, the semantic fit to the original task appears weaker.

### Validation verdict

`revise`

### Why this verdict is correct

The repair improved one dimension:

- descriptor structure became cleaner

But it also introduced possible collateral damage:

- semantic fit may have weakened

So the right early verdict is not full accept.

It is `revise`.

### Main teaching point

A cleaner container is not always a fully successful repair if semantic fit drops.

---

## 6. What these examples teach

Taken together, these tiny examples teach four important lessons.

### Lesson 1

A repair should be judged against its declared validation target.

### Lesson 2

A local improvement can be strong enough for `accept`.

### Lesson 3

A mixed result should often become `revise`, not forced success.

### Lesson 4

Validation is what turns repair from intuition into disciplined workflow.

---

## 7. Why these examples are useful

These tiny examples are useful for at least four reasons.

### A. Planner support

They help test whether a repair planner is choosing actions that can actually be validated.

### B. Validation support

They show what before and after validation is supposed to look like.

### C. Demo support

They are small enough to reuse in future repair demos.

### D. Future semi-auto support

They provide the first tiny evidence base for safe early semi-auto repair behavior.

---

## 8. What this pack does not yet include

Tiny Validation Examples Pack v1 does **not** yet include:

- large validation datasets
- cross-family repair chains
- F6-heavy intervention examples
- benchmark-scale scoring
- automated validator code
- full rollback examples in the same file

Those can come later.

This pack is intentionally minimal.

---

## 9. Recommended next step

Once this pack exists, the next useful follow-up is one of these:

1. create [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
2. create [Planner Test Note v1](./planner-test-note-v1.md) using these examples
3. create [Tiny Semi-Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md) that consumes these examples

The strongest immediate next step is probably:

> create a tiny rollback examples pack

because validation and rollback naturally belong close together.

---

## 10. Next steps ✨

After this page, most readers continue with:

1. [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
2. [Open Planner Test Note v1](./planner-test-note-v1.md)
3. [Open Tiny Semi-Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
4. [Open Tiny Semi-Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)

If you want the broader product surface:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

---

## 11. One-line summary 🌍

**Tiny Validation Examples Pack v1 provides the first small before-and-after validation examples for safe early Atlas-based repair actions in F1, F4, and F7.**

