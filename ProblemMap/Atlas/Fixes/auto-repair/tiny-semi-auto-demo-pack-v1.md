<!--
AI_NOTE_START

Document role:
This file is the first compact semi-auto demo pack for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want small visible examples of the Atlas → Auto Repair micro-workflow in motion.
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
   - [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
   - [Planner Test Note v1](./planner-test-note-v1.md)
   - [Planner Review Checklist v1](./planner-review-checklist-v1.md)
   - [Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)
   - [Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
   - [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
3. Use this page for demo support, onboarding, review calibration, and future replay or notebook-oriented demo expansion.

What this file is:
- A compact semi-auto demo pack
- The first visible sample layer for bounded local repair workflows
- A practical bridge between planner output, local action, validation, rollback readiness, and deeper continuation decisions

What this file is not:
- Not a production repair suite
- Not a benchmark pack
- Not unrestricted self-repair
- Not proof that broad autonomous repair is already available

Reading discipline for AI:
- Treat each demo as a bounded local workflow sample, not as proof of full repair autonomy.
- Keep routed diagnosis, selected action, validation result, rollback readiness, and deeper continuation decision visible.
- Do not overread small local success as total closure.
- Preserve the layer distinction between Atlas routing, Auto Repair local action, and deeper WFGY continuation.

AI_NOTE_END
-->

# Tiny Semi-Auto Demo Pack v1 🧪

## The first compact visible demo layer for Atlas-based semi-auto repair

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
- [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)
- [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
- [Open Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
- [Open Worked Escalation Example v1](./worked-escalation-example-v1.md)

---

If the demo spec explains **how a tiny semi-auto demo should be structured**, this pack shows **what a few compact demos actually look like when the workflow runs end to end**. 🧭

Its purpose is practical:

> provide a first compact set of semi-auto repair demos  
> that make the Auto Repair workflow visible, testable, and teachable

This file does **not** claim to be a production repair suite.

It claims something smaller and more useful:

> the project now has a first tiny pack of local, validation-aware, rollback-aware, WFGY-aware semi-auto repair demos

---

## Quick start 🚀

### I want the shortest demo reading

Use this path:

1. read one demo ID and case summary
2. inspect the routed diagnosis
3. inspect the planner output
4. inspect the selected action
5. inspect the validation result
6. inspect the final outcome and deeper continuation note

### I want the stronger workflow reading

Use this page together with:

1. [Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
2. [Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)
3. [Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
4. [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
5. [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)

Short version:

> route the case  
> pick one safe local action  
> validate the result  
> keep rollback visible  
> decide whether local repair is enough ✨

---

## 1. Why this pack exists

The Auto Repair layer already has:

- architecture
- action schema
- planner logic
- validation logic
- rollback logic
- semi-auto scope discipline
- safe early action catalog
- tiny validation examples
- tiny rollback examples
- planner review examples
- tiny semi-auto demo specification
- the Atlas to WFGY bridge

But there is still one missing layer:

- actual tiny demo cases that show the whole micro-workflow in motion

This pack fills that gap.

It provides the first compact set of demo cases that show:

1. routed input
2. planner output
3. one selected safe action
4. one bounded local change
5. one validation result
6. one final outcome
7. one explicit deeper continuation decision

In short:

> this pack is the first visible semi-auto repair sample layer

---

## 2. What this pack is supposed to prove

This pack is not trying to prove:

- full repair autonomy
- large-scale benchmark performance
- unrestricted self-repair
- high-risk intervention capability
- universal repair correctness

It is only trying to prove that:

1. a routed Atlas case can be turned into a small repair plan
2. one safe early action can be selected cleanly
3. that action can be applied in a narrow and inspectable way
4. the result can be validated
5. the system can end in `accept`, `revise`, or `rollback`
6. the system can say clearly whether local repair is enough or whether WFGY 3.0 continuation is needed

That is already enough for a strong first demo pack.

---

## 3. Demo quick map 🗂️

| Demo | Main teaching focus |
|---|---|
| F1 demo | grounding-first repair can succeed through a single local evidence action |
| F4 demo | execution-first repair can succeed through a narrow closure fix |
| F7 demo | structure-first repair can improve the container while still ending in `revise` |

This page is the right place when the question is **what a small bounded semi-auto workflow should look like in practice**, not whether the full repair stack is production-ready.

---

## 4. Pack composition

This v1 pack includes three tiny semi-auto demos:

- one F1 demo
- one F4 demo
- one F7 demo

These are the best first targets because they are:

- local
- inspectable
- reversible
- validation-friendly
- explainable in public-facing and AI-facing contexts

This pack intentionally does **not** include:

- F6-heavy intervention demos
- broad multi-family live mutation demos
- large continuity mutation demos
- benchmark-scale orchestration demos

Those belong to later stages.

---

## 5. Standard demo format

Each demo in this pack follows the same structure:

1. Demo ID
2. Family
3. Case summary
4. Routed diagnosis
5. Planner output
6. Selected action
7. Before state
8. After state
9. Validation result
10. Final outcome
11. Rollback readiness
12. Deeper continuation
13. Why this demo matters

This format is compact enough for:

- markdown demos
- JSON demos
- notebook demos
- replay demos
- AI prompt examples

---

## Demo 1 · F1 Tiny Semi-Auto Demo

### Demo ID

`TSAD_F1_001`

### Family

F1 · Grounding and Evidence Integrity

### Case summary

A response is fluent and plausible, but it is grounded in a semantically adjacent source chunk rather than the intended evidence source.

The failure is not primarily stylistic and not primarily representational.

It is a grounding-first case.

### Routed diagnosis

- primary family: F1
- secondary family: F7
- broken invariant: evidence-anchor integrity broken
- best current fit: `F1_N01 Retrieval Anchor Drift`
- fix surface direction: re-grounding or anchor re-check
- confidence: medium
- evidence sufficiency: medium

### Planner output

```json
{
  "selected_repair_family": "F1",
  "planner_confidence": "high",
  "plan_scope": "minimal",
  "candidate_actions": [
    {
      "action_id": "F1_RG_001",
      "action_title": "Re-ground evidence set"
    }
  ],
  "action_ordering": [
    "Replace the current evidence set with the better-aligned source set first"
  ],
  "primary_validation_target": "anchor alignment",
  "misrepair_risk": "may over-tighten representation while the real issue remains grounding",
  "recommended_next_step": "validate-first-action"
}
````

### Selected action

`F1_RG_001`
Re-ground evidence set

### Before state

* answer appears coherent
* cited or implied source support is nearby but wrong
* semantic target fit is weaker than it first appears
* evidence anchor is not the intended one

### After state

* evidence set is replaced with a better-aligned source set
* answer is now tied more directly to the intended source target
* local grounding quality improves
* no visible container damage is introduced

### Validation result

```json
{
  "validation_target": "anchor alignment",
  "before_state_summary": "answer relied on a semantically adjacent but incorrect source chunk",
  "after_state_summary": "answer is now tied to the intended source group",
  "improvement_detected": true,
  "collateral_damage_detected": false,
  "validation_confidence": "high",
  "recommended_outcome": "accept"
}
```

### Final outcome

`accept`

### Rollback readiness

* rollback ready: true
* restore point: prior evidence set

### Deeper continuation

`local repair sufficient`

#### WFGY continuation note

No deeper WFGY 3.0 continuation is needed for this tiny demo because the local grounding repair is already sufficient at the Atlas and Auto Repair layer.

### Why this demo matters

This demo shows that a grounding-first case can be improved through a small local repair without pretending that all plausible-looking failures are reasoning failures.

---

## Demo 2 · F4 Tiny Semi-Auto Demo

### Demo ID

`TSAD_F4_001`

### Family

F4 · Execution and Contract Integrity

### Case summary

A downstream action executes before approval and readiness are complete.

The workflow is not primarily broken because of memory loss or weak reasoning.

It is a closure-first case.

### Routed diagnosis

* primary family: F4
* secondary family: F3
* broken invariant: deployment liveness closure broken
* best current fit: `F4_N03 Pre-Readiness Execution Failure`
* fix surface direction: readiness audit or gate insertion
* confidence: medium
* evidence sufficiency: medium

### Planner output

```json
{
  "selected_repair_family": "F4",
  "planner_confidence": "medium",
  "plan_scope": "constrained",
  "candidate_actions": [
    {
      "action_id": "F4_GT_001",
      "action_title": "Insert readiness gate"
    }
  ],
  "action_ordering": [
    "Insert a local readiness gate before downstream execution"
  ],
  "primary_validation_target": "readiness state",
  "misrepair_risk": "may over-block valid progress if the true issue is continuity rather than closure",
  "recommended_next_step": "validate-first-action",
  "why_not_other_repair_family": "F3 pressure exists, but the first visible break is execution closure rather than continuity loss"
}
```

### Selected action

`F4_GT_001`
Insert readiness gate

### Before state

* downstream action is available
* readiness is incomplete
* execution still moves forward
* workflow closure is too weak

### After state

* a local readiness gate is inserted
* downstream action is blocked until readiness is satisfied
* closure integrity improves
* the workflow becomes more structurally disciplined

### Validation result

```json
{
  "validation_target": "readiness state",
  "before_state_summary": "downstream action executed before approval and readiness were complete",
  "after_state_summary": "downstream action is now blocked until readiness is satisfied",
  "improvement_detected": true,
  "collateral_damage_detected": false,
  "validation_confidence": "medium",
  "recommended_outcome": "accept"
}
```

### Final outcome

`accept`

### Rollback readiness

* rollback ready: true
* restore point: previous workflow gate configuration

### Deeper continuation

`local repair sufficient`

#### WFGY continuation note

No deeper WFGY 3.0 continuation is needed for this tiny demo because the local closure repair is sufficient and the workflow state becomes stable under bounded intervention.

### Why this demo matters

This demo shows that not every system failure needs more intelligence pressure.

Some failures need execution skeleton repair first.

---

## Demo 3 · F7 Tiny Semi-Auto Demo

### Demo ID

`TSAD_F7_001`

### Family

F7 · Representation and Localization Integrity

### Case summary

The content is partly correct, but the structured shell is broken and cannot be reliably consumed downstream.

The main problem is not primarily reasoning progression.

It is a container-first case.

### Routed diagnosis

* primary family: F7
* secondary family: F2
* broken invariant: representation container fidelity broken
* best current fit: `F7_N01 Symbolic Representation Fidelity Failure`
* fix surface direction: schema tightening or shell correction
* confidence: medium
* evidence sufficiency: medium

### Planner output

```json
{
  "selected_repair_family": "F7",
  "planner_confidence": "medium",
  "plan_scope": "constrained",
  "candidate_actions": [
    {
      "action_id": "F7_SC_001",
      "action_title": "Tighten output schema"
    }
  ],
  "action_ordering": [
    "Tighten the output schema shell first"
  ],
  "primary_validation_target": "schema validity",
  "misrepair_risk": "may produce a cleaner shell while weakening semantic task fit",
  "recommended_next_step": "validate-first-action"
}
```

### Selected action

`F7_SC_001`
Tighten output schema

### Before state

* output content is partially useful
* object or field boundaries are broken
* downstream consumption is unreliable
* structural shell is invalid

### After state

* schema shell is tightened
* field boundaries are restored
* downstream consumption becomes possible
* structure becomes cleaner and more stable

### Validation result

```json
{
  "validation_target": "schema validity",
  "before_state_summary": "output structure was invalid and could not be reliably consumed downstream",
  "after_state_summary": "output structure now matches the required shell and can be consumed downstream",
  "improvement_detected": "partial",
  "collateral_damage_detected": true,
  "validation_confidence": "medium",
  "recommended_outcome": "revise"
}
```

### Final outcome

`revise`

### Rollback readiness

* rollback ready: true
* restore point: prior schema version

### Deeper continuation

`local repair partially useful, deeper continuation optional`

#### WFGY continuation note

The local Atlas-level repair improves container fidelity, but deeper WFGY 3.0 continuation may still be useful if semantic fit remains unstable or if the representational encoding itself is still too weak.

Official TXT:

* [WFGY 3.0 Singularity Demo TXT](https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt)

### Why this demo matters

This demo shows that a repair can improve one dimension without justifying a fake full success claim.

That is exactly why `revise` exists.

---

## 6. What this pack teaches

Taken together, these three tiny demos teach several important lessons.

### Lesson 1

Atlas routing can be turned into a small repair plan.

### Lesson 2

A single safe early action can be enough for a meaningful local gain.

### Lesson 3

Validation is what separates repair from action theatre.

### Lesson 4

Rollback readiness should always remain visible, even when rollback is not triggered.

### Lesson 5

Not every local gain means total closure.

Sometimes the right outcome is `revise`, and sometimes deeper WFGY 3.0 continuation becomes relevant.

---

## 7. Why this pack is useful

This pack is useful for at least five reasons.

### A. Demo support

It is the first visible semi-auto repair sample layer.

### B. Planner support

It gives the planner concrete output targets.

### C. Validation support

It shows what compact before and after validation should look like.

### D. Rollback support

It keeps restore points visible even in successful or partial-success cases.

### E. WFGY bridge support

It demonstrates that local Atlas repair and deeper WFGY continuation belong to the same system, but not at the same layer.

---

## 8. What this pack does not yet include

Tiny Semi-Auto Demo Pack v1 does **not** yet include:

* F6-heavy intervention demos
* full notebook implementations
* replay or live orchestration code
* large benchmark demo suites
* multi-step repair chains
* full WFGY continuation walkthroughs

Those can come later.

This pack is intentionally small and disciplined.

---

## 9. Recommended next step

Once this pack exists, the next useful follow-up is probably one of these:

1. create a notebook-oriented replay version of these three demos
2. create a JSON pack version of these three demos
3. create one worked escalation example where local repair fails and WFGY 3.0 continuation becomes clearly necessary

The strongest immediate next step is probably:

> create one worked escalation example

because that would make the Atlas → Auto Repair → WFGY 3.0 bridge even more visible.

---

## 10. Next steps ✨

After this page, most readers continue with:

1. [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
2. [Open Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
3. [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
4. [Open Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
5. [Open Worked Escalation Example v1](./worked-escalation-example-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 11. One-line summary 🌍

**Tiny Semi-Auto Demo Pack v1 provides the first compact F1, F4, and F7 semi-auto repair demos that show planner output, bounded local action, validation, final outcome, and possible WFGY 3.0 continuation.**
