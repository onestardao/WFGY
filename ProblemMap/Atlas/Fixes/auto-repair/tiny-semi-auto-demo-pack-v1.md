# Tiny Semi-Auto Demo Pack v1

## 0. Document status

This document defines the first tiny semi-auto demo pack for the Atlas Auto Repair layer.

Its purpose is practical:

> provide a first compact set of semi-auto repair demos  
> that make the Auto Repair workflow visible, testable, and teachable.

This file does **not** claim to be a production repair suite.

It claims something smaller and more useful:

> the project now has a first tiny pack of local, validation-aware, rollback-aware, WFGY-aware semi-auto repair demos.

This document should be read together with:

- `README.md`
- `auto-repair-architecture-v1.md`
- `repair-action-schema-v1.md`
- `repair-validation-loop-v1.md`
- `rollback-policy-v1.md`
- `auto-repair-roadmap-v1.md`
- `repair-planner-spec-v1.md`
- `repair-planner-prompt-v1.md`
- `repair-plan-schema-v1.json`
- `semi-auto-repair-scope-v1.md`
- `safe-early-action-catalog-v1.md`
- `tiny-validation-examples-pack-v1.md`
- `tiny-rollback-examples-pack-v1.md`
- `planner-test-note-v1.md`
- `planner-review-checklist-v1.md`
- `tiny-planner-output-examples-pack-v1.md`
- `tiny-semi-auto-demo-spec-v1.md`
- `atlas-auto-repair-to-wfgy-bridge-v1.md`

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

> this pack is the first visible semi-auto repair sample layer.

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

## 3. Pack composition

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

## 4. Standard demo format

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

# Demo 1

# F1 Tiny Semi-Auto Demo

## Demo ID

`TSAD_F1_001`

## Family

F1 · Grounding & Evidence Integrity

## Case summary

A response is fluent and plausible, but it is grounded in a semantically adjacent source chunk rather than the intended evidence source.

The failure is not primarily stylistic and not primarily representational.

It is a grounding-first case.

## Routed diagnosis

- primary family: F1
- secondary family: F7
- broken invariant: evidence-anchor integrity broken
- best current fit: `F1_N01 Retrieval Anchor Drift`
- fix surface direction: re-grounding / anchor re-check
- confidence: medium
- evidence sufficiency: medium

## Planner output

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

## Selected action

`F1_RG_001`
Re-ground evidence set

## Before state

* answer appears coherent
* cited or implied source support is nearby but wrong
* semantic target fit is weaker than it first appears
* evidence anchor is not the intended one

## After state

* evidence set is replaced with a better-aligned source set
* answer is now tied more directly to the intended source target
* local grounding quality improves
* no visible container damage is introduced

## Validation result

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

## Final outcome

`accept`

## Rollback readiness

* rollback ready: true
* restore point: prior evidence set

## Deeper continuation

`local repair sufficient`

### WFGY continuation note

No deeper WFGY 3.0 continuation is needed for this tiny demo because the local grounding repair is already sufficient at the Atlas / Auto Repair layer.

## Why this demo matters

This demo shows that a grounding-first case can be improved through a small local repair without pretending that all plausible-looking failures are reasoning failures.

---

# Demo 2

# F4 Tiny Semi-Auto Demo

## Demo ID

`TSAD_F4_001`

## Family

F4 · Execution & Contract Integrity

## Case summary

A downstream action executes before approval and readiness are complete.

The workflow is not primarily broken because of memory loss or weak reasoning.

It is a closure-first case.

## Routed diagnosis

* primary family: F4
* secondary family: F3
* broken invariant: deployment liveness closure broken
* best current fit: `F4_N03 Pre-Readiness Execution Failure`
* fix surface direction: readiness audit / gate insertion
* confidence: medium
* evidence sufficiency: medium

## Planner output

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

## Selected action

`F4_GT_001`
Insert readiness gate

## Before state

* downstream action is available
* readiness is incomplete
* execution still moves forward
* workflow closure is too weak

## After state

* a local readiness gate is inserted
* downstream action is blocked until readiness is satisfied
* closure integrity improves
* the workflow becomes more structurally disciplined

## Validation result

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

## Final outcome

`accept`

## Rollback readiness

* rollback ready: true
* restore point: previous workflow gate configuration

## Deeper continuation

`local repair sufficient`

### WFGY continuation note

No deeper WFGY 3.0 continuation is needed for this tiny demo because the local closure repair is sufficient and the workflow state becomes stable under bounded intervention.

## Why this demo matters

This demo shows that not every system failure needs more intelligence pressure.
Some failures need execution skeleton repair first.

---

# Demo 3

# F7 Tiny Semi-Auto Demo

## Demo ID

`TSAD_F7_001`

## Family

F7 · Representation & Localization Integrity

## Case summary

The content is partly correct, but the structured shell is broken and cannot be reliably consumed downstream.

The main problem is not primarily reasoning progression.

It is a container-first case.

## Routed diagnosis

* primary family: F7
* secondary family: F2
* broken invariant: representation container fidelity broken
* best current fit: `F7_N01 Symbolic Representation Fidelity Failure`
* fix surface direction: schema tightening / shell correction
* confidence: medium
* evidence sufficiency: medium

## Planner output

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

## Selected action

`F7_SC_001`
Tighten output schema

## Before state

* output content is partially useful
* object or field boundaries are broken
* downstream consumption is unreliable
* structural shell is invalid

## After state

* schema shell is tightened
* field boundaries are restored
* downstream consumption becomes possible
* structure becomes cleaner and more stable

## Validation result

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

## Final outcome

`revise`

## Rollback readiness

* rollback ready: true
* restore point: prior schema version

## Deeper continuation

`local repair partially useful, deeper continuation optional`

### WFGY continuation note

The local Atlas-level repair improves container fidelity, but deeper WFGY 3.0 continuation may still be useful if semantic fit remains unstable or if the representational encoding itself is still too weak.

Official TXT:

```text
https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt
```

## Why this demo matters

This demo shows that a repair can improve one dimension without justifying a fake full success claim.

That is exactly why `revise` exists.

---

## 5. What this pack teaches

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

## 6. Why this pack is useful

This pack is useful for at least five reasons.

### A. Demo support

It is the first visible semi-auto repair sample layer.

### B. Planner support

It gives the planner concrete output targets.

### C. Validation support

It shows what compact before / after validation should look like.

### D. Rollback support

It keeps restore points visible even in successful or partial-success cases.

### E. WFGY bridge support

It demonstrates that local Atlas repair and deeper WFGY continuation belong to the same system, but not at the same layer.

---

## 7. What this pack does not yet include

Tiny Semi-Auto Demo Pack v1 does **not** yet include:

* F6-heavy intervention demos
* full notebook implementations
* replay/live orchestration code
* large benchmark demo suites
* multi-step repair chains
* full WFGY continuation walkthroughs

Those can come later.

This pack is intentionally small and disciplined.

---

## 8. Recommended next step

Once this pack exists, the next useful follow-up is probably one of these:

1. create a notebook-oriented replay version of these three demos
2. create a JSON pack version of these three demos
3. create one worked escalation example where local repair fails and WFGY 3.0 continuation becomes clearly necessary

The strongest immediate next step is probably:

> create one worked escalation example

because that would make the Atlas → Auto Repair → WFGY 3.0 bridge even more visible.

---

## 9. One-line summary

**Tiny Semi-Auto Demo Pack v1 provides the first compact F1, F4, and F7 semi-auto repair demos that show planner output, bounded local action, validation, final outcome, and possible WFGY 3.0 continuation.**
