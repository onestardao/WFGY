<!--
AI_NOTE_START

Document role:
This file defines the first formal validation logic for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you need to judge whether a proposed or applied repair actually improved the case.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Action Schema v1](./repair-action-schema-v1.md)
   - [Repair Planner Spec v1](./repair-planner-spec-v1.md)
   - [Rollback Policy v1](./rollback-policy-v1.md)
3. Use this page as the validation logic contract for accept, revise, rollback, or escalate decisions.

What this file is:
- The validation logic page for Auto Repair v1
- A contract for judging repair outcomes after an action is proposed or applied
- A decision layer between repair attempt and next-step outcome

What this file is not:
- Not a full autonomous validation engine
- Not a benchmark scoring system
- Not a deployment-grade validator implementation
- Not proof that one plausible repair action is automatically a successful repair

Reading discipline for AI:
- Judge the outcome, not the intention alone.
- Keep target invariant, before and after state, collateral damage, and next-step decision visible.
- Treat validation as part of the repair architecture, not as an optional add-on.
- Prefer explicit uncertainty over fake certainty when evidence is weak.

AI_NOTE_END
-->

# Repair Validation Loop v1 🔍

## How Atlas-based repair should be judged after a repair action is proposed or applied

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
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)

---

If the repair planner decides **what first move should be tried**, this validation loop decides **whether that move actually helped enough to keep**. 🧭

This document does **not** claim that a full autonomous validation engine already exists.

Instead, it defines the first formal logic for answering a simple but critical question:

> after a repair action is chosen,  
> how do we decide whether it actually improved the case?

That question is the center of trustworthy repair.

Without a validation loop, repair remains guesswork.

---

## Quick start 🚀

### I want the shortest validation reading

Use this path:

1. identify the repair action being validated
2. identify the target broken invariant
3. compare before and after state
4. check for collateral damage
5. choose `accept`, `revise`, `rollback`, or `escalate`

### I want the stronger validation reading

Use this page together with:

1. [Repair Action Schema v1](./repair-action-schema-v1.md)
2. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. [Rollback Policy v1](./rollback-policy-v1.md)

Short version:

> check the target  
> compare before and after  
> check for damage  
> decide the next safe move ✨

---

## 1. What this document is for

This file defines the validation layer for Auto Repair v1.

Its purpose is to explain:

- what should be validated
- in what order validation should happen
- what counts as improvement
- what counts as collateral damage
- when to accept, revise, rollback, or escalate

This document is meant to work together with:

- [README](./README.md)
- [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
- [Repair Action Schema v1](./repair-action-schema-v1.md)

Together, those files define:

- what Auto Repair is
- how it is structured
- what a repair action looks like
- how repair actions should be checked

---

## 2. Why validation must exist

A repair action can sound reasonable and still fail.

For example:

- a grounding fix may tighten evidence selection but still miss the true anchor
- an execution fix may block useful progress without fixing the real closure issue
- a schema fix may improve structure while hiding a deeper grounding problem
- an observability fix may add logs without increasing actual diagnosability

So repair cannot be judged by intention alone.

It must be judged by outcome.

This is why the validation loop is not optional.

It is part of the repair architecture.

---

## 3. Placement in the full workflow 🧩

The intended repair workflow is:

```text
case
→ atlas routing
→ fix surface
→ repair planner
→ candidate repair action
→ validation loop
→ {accept / revise / rollback / escalate}
````

The validation loop comes **after** a repair action is selected,
but **before** the system treats the repair as successful.

This means validation is the gate between:

* a repair was proposed
  and
* a repair actually helped

---

## 4. Validation quick map 🗂️

| Validation concern          | Main question                                   |
| --------------------------- | ----------------------------------------------- |
| target check                | what action or invariant are we validating      |
| before and after comparison | what changed locally                            |
| improvement check           | did the targeted invariant improve              |
| usefulness check            | did the case become more usable or more correct |
| collateral damage check     | did the repair create new problems              |
| outcome decision            | should we accept, revise, rollback, or escalate |

This page is the right place when the question is **how to judge a repair outcome**, not how to design the planner or how to implement a full validator engine.

---

## 5. Core validation principle

The validation loop must always ask:

1. Did the targeted broken invariant improve
2. Did the case become more stable or more correct
3. Did the repair produce new damage
4. Is the improvement strong enough to keep
5. If not, what is the next safe step

This means validation is not only a correctness check.

It is also:

* a safety check
* a collateral-damage check
* a repair-confidence check
* a next-step decision layer

---

## 6. Minimal validation contract

Every repair validation attempt in v1 should aim to produce these outputs:

### Required outputs

* `validation_target`
* `target_invariant`
* `before_state_summary`
* `after_state_summary`
* `improvement_detected`
* `collateral_damage_detected`
* `validation_confidence`
* `recommended_outcome`

### Optional but recommended outputs

* `improvement_type`
* `remaining_failure_pressure`
* `misrepair_signal`
* `escalation_reason`
* `rollback_reason`
* `notes`

This creates a reusable validation object, even before automation becomes deep.

---

## 7. Field definitions

### `validation_target`

The repair action or region being validated.

Examples:

* `F1_RG_001`
* `F4_GT_001`
* `F7_SC_001`

This field ties validation back to the repair action schema.

### `target_invariant`

The broken invariant the repair was supposed to improve.

Examples:

* `evidence-anchor integrity broken`
* `deployment liveness closure broken`
* `formal descriptor fidelity broken`

Validation should always remain linked to a declared invariant.

### `before_state_summary`

A short structured description of the relevant case state before the repair.

Examples:

* retrieved evidence set drifted from the target source
* downstream execution started before approval state was complete
* output content partially fit the task but broke schema boundaries

This field is not meant to capture everything.
It captures the specific part the repair claimed to improve.

### `after_state_summary`

A short structured description of the case state after the repair.

Examples:

* retrieved evidence now matches the intended source
* downstream execution is blocked until readiness is satisfied
* output now conforms to the required schema shell

This field should remain focused and local.

### `improvement_detected`

A boolean or controlled verdict indicating whether the target improved.

Suggested values:

* `true`
* `false`
* `partial`

Using `partial` is often better than forcing a fake binary answer.

### `collateral_damage_detected`

A signal for whether the repair created meaningful new problems.

Examples:

* structure improved but semantic fidelity dropped
* observability increased but workflow became too noisy
* closure hardened but useful continuity was blocked

Suggested values:

* `true`
* `false`
* `unknown`

### `validation_confidence`

How strongly the system trusts the validation judgment.

Suggested values:

* `low`
* `medium`
* `high`

This should depend on evidence quality, not on rhetorical confidence.

### `recommended_outcome`

The next action the system should take.

Suggested values:

* `accept`
* `revise`
* `rollback`
* `escalate`

This is the most important decision output of the loop.

---

## 8. Validation levels

Repair Validation Loop v1 should not treat validation as one giant yes or no question.

A strong validation pass is usually layered.

The recommended early levels are:

### Level 1 · Surface validity

Check whether the repair changed the visible local target.

Examples:

* schema now parses
* gate now exists
* trace now appears
* evidence set now changed

This is the weakest layer, but still useful.

### Level 2 · Invariant improvement

Check whether the declared broken invariant improved.

Examples:

* evidence alignment is stronger
* execution closure is more correct
* container fidelity is more stable
* continuity is less fragmented

This is more important than surface validity.

### Level 3 · Functional usefulness

Check whether the repaired system is actually more usable or more correct in practice.

Examples:

* answer became more accurate
* workflow now completes safely
* structured output can now be consumed
* diagnostic trace now helps identify the real failure path

This layer prevents shallow cosmetic fixes from being mistaken for real repairs.

### Level 4 · Collateral damage review

Check whether the repair created new instability.

Examples:

* output became valid JSON but semantically worse
* safety block became so strict that useful execution stopped
* observability layer added too much noise
* continuity scaffold distorted ownership semantics

This level is crucial.

A repair that improves one layer but harms another must not be treated as a clean win.

---

## 9. Recommended validation sequence

The default sequence should be:

1. check surface validity
2. check target invariant improvement
3. check practical usefulness
4. check collateral damage
5. decide accept, revise, rollback, or escalate

This sequence is simple enough to reuse and strong enough for early trust.

---

## 10. Recommended verdict logic

### Accept

Use when:

* target invariant clearly improved
* no meaningful collateral damage is detected
* the repair outcome is stable enough for current scope

### Revise

Use when:

* some improvement happened
* but the repair is incomplete
* or local success still leaves important failure pressure unresolved

### Rollback

Use when:

* the repair made the case worse
* the wrong layer was changed
* the repair introduced stronger collateral damage than the original problem

### Escalate

Use when:

* the repair could not be judged safely
* the case has crossed family boundaries
* the target family may have been wrong
* deeper WFGY repair logic is needed
* human review is required

These four outcomes are enough for v1.

---

## 11. Family-specific validation examples

Different families often need different validation focus.

### F1 · Grounding and Evidence Integrity

Best early validation checks:

* anchor verification
* source alignment check
* semantic target check

Typical success sign:

* the answer is now tied to the correct evidence set

Typical false success risk:

* output looks cleaner but is still grounded to the wrong anchor

### F4 · Execution and Contract Integrity

Best early validation checks:

* readiness state inspection
* ordering correctness
* gate enforcement check
* closure path review

Typical success sign:

* downstream execution no longer occurs before upstream readiness

Typical false success risk:

* the system blocks everything, including valid execution

### F7 · Representation and Localization Integrity

Best early validation checks:

* schema validation
* descriptor fidelity check
* structural shell review

Typical success sign:

* the output container is now valid and preserves the intended structure

Typical false success risk:

* structure improves while semantic alignment quietly degrades

### F5 · Observability and Diagnosability Integrity

Best early validation checks:

* trace exposure improvement
* logging usefulness
* failure-path visibility uplift

Typical success sign:

* the failure path becomes more diagnosable

Typical false success risk:

* more information is visible, but the real bottleneck is still hidden

---

## 12. Misrepair signals

The validation loop should be able to flag common misrepair patterns.

Early examples include:

* **style repair on a grounding problem**
* **reasoning pressure on an execution problem**
* **schema tightening on a deeper grounding failure**
* **observability uplift mistaken for full repair**
* **boundary intervention before diagnosability is adequate**

These signals do not necessarily force rollback every time,
but they should strongly bias the loop toward `revise` or `escalate`.

---

## 13. Validation and confidence discipline

Validation confidence must never be treated as decoration.

Confidence should go down when:

* evidence is thin
* before and after comparison is ambiguous
* multiple families remain plausible
* the repair target was not narrowly defined
* the case crosses into high-risk boundary-heavy territory

This is especially important in:

* F5 and F6 edges
* F3 and F4 edges
* F1 and F7 synthetic boundary cases

A weak validation with a high confidence label is worse than an explicit uncertain result.

---

## 14. Relationship to rollback

Validation and rollback are closely connected.

Rollback is not triggered by failure alone.

It is triggered when validation finds that:

* the repair worsened the target state
* a wrong layer was repaired
* new damage is stronger than the original local gain
* the system became less stable or less interpretable

So rollback should be treated as a normal branch of the loop,
not as a special embarrassment case.

---

## 15. Relationship to escalation

Validation should also know when to stop pretending that the current layer is enough.

Escalation becomes the right output when:

* the repair did not meaningfully improve the invariant
* the family fit now looks doubtful
* the case reveals stronger neighboring-family pressure
* the repair enters deeper abstract territory
* the system needs stronger human or WFGY review

This is especially relevant for:

* F6-heavy cases
* difficult F3, F4, and F6 interactions
* high-abstract coherence and legitimacy problems
* multi-layer synthetic truth and representation mixtures

---

## 16. Example validation objects

### Example A · F1 validation

```json
{
  "validation_target": "F1_RG_001",
  "target_invariant": "evidence-anchor integrity broken",
  "before_state_summary": "retrieved evidence set drifted from the intended source",
  "after_state_summary": "retrieved evidence now matches the intended source set",
  "improvement_detected": true,
  "collateral_damage_detected": false,
  "validation_confidence": "high",
  "recommended_outcome": "accept"
}
```

### Example B · F4 validation

```json
{
  "validation_target": "F4_GT_001",
  "target_invariant": "deployment liveness closure broken",
  "before_state_summary": "downstream execution started before approval state was complete",
  "after_state_summary": "downstream execution is blocked until readiness is satisfied",
  "improvement_detected": true,
  "collateral_damage_detected": false,
  "validation_confidence": "medium",
  "recommended_outcome": "accept"
}
```

### Example C · F7 validation with collateral damage

```json
{
  "validation_target": "F7_SC_001",
  "target_invariant": "formal descriptor fidelity broken",
  "before_state_summary": "output structure was invalid but semantic content was partially correct",
  "after_state_summary": "output now matches schema but semantic alignment appears weaker",
  "improvement_detected": "partial",
  "collateral_damage_detected": true,
  "validation_confidence": "medium",
  "recommended_outcome": "revise"
}
```

---

## 17. What this loop does not yet include

Repair Validation Loop v1 does **not** yet include:

* full automated scoring engines
* family-wide benchmark metrics
* multi-step validator orchestration
* cross-action dependency graphs
* statistical repair confidence calibration
* deployment-grade validator code

Those can come later.

v1 only aims to define the validation logic clearly enough for later implementation.

---

## 18. Recommended next step

Once this file exists, the next logical file is:

* [Rollback Policy v1](./rollback-policy-v1.md)

because the validation loop now defines when rollback is needed,
but the system still needs a formal statement of how rollback should be framed and governed.

After that, the auto-repair folder will already have:

* README
* architecture
* action schema
* validation loop

which is a very strong first-phase foundation.

---

## 19. Next steps ✨

After this page, most readers continue with:

1. [Open Rollback Policy v1](./rollback-policy-v1.md)
2. [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
4. [Open Planner Test Note v1](./planner-test-note-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 20. One-line validation summary 🌍

**Repair Validation Loop v1 defines how Atlas-based repair should be judged, accepted, revised, rolled back, or escalated after a repair action is proposed or applied.**
