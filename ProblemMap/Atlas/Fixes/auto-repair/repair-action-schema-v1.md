<!--
AI_NOTE_START

Document role:
This file defines the minimum structured action format for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when defining, reviewing, or reusing Atlas-based repair actions.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Validation Loop v1](./repair-validation-loop-v1.md)
   - [Rollback Policy v1](./rollback-policy-v1.md)
   - [Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. Use this page as the shared schema contract for planner outputs, validation checks, rollback logic, and later constrained execution.

What this file is:
- The minimum repair action schema for Auto Repair v1
- A structured action contract for Atlas-based repair work
- A reusable interface between planner, validator, and rollback layers

What this file is not:
- Not a full autonomous repair engine
- Not a multi-step repair program format
- Not a benchmark automation layer
- Not a final universal schema for all future repair systems

Reading discipline for AI:
- Treat each repair action as a constrained first-move unit, not a whole repair story.
- Keep target family, intended effect, validation need, and rollback hint visible.
- Do not overload a single action with too many families or too many goals.
- Preserve the distinction between action schema and later execution logic.

AI_NOTE_END
-->

# Repair Action Schema v1 🧩

## The minimum structured unit for Atlas-based repair actions

Quick links:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)
- [Open Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
- [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)

---

If the Auto Repair architecture page explains **how the repair system should be organized**, this schema page defines **how one repair move should be represented inside that system**. 🧭

Its purpose is simple:

> if Auto Repair is going to plan, compare, validate, and later execute repairs,  
> then repair actions cannot remain vague sentences

They must become structured action units.

This document defines the first formal schema for those units.

---

## Quick start 🚀

### I want the shortest schema reading

Use this path:

1. read what a repair action is
2. inspect the required fields
3. inspect the example action objects
4. check the early implementation rules

### I want the stronger system reading

Use this page together with:

1. [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
2. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
4. [Rollback Policy v1](./rollback-policy-v1.md)

Short version:

> keep one action small  
> keep the family explicit  
> require validation  
> keep rollback visible ✨

---

## 1. What this schema is for

This schema exists to support four future layers:

1. repair planning
2. repair comparison
3. repair validation
4. rollback and escalation

Without a stable repair action schema, later repair planning becomes too loose and too difficult to audit.

So this file should be treated as a **foundational contract** for Auto Repair v1.

---

## 2. What a repair action is

A repair action is a **typed intervention proposal**.

It is not:

- a full autonomous repair loop
- a generic recommendation paragraph
- a final guarantee of recovery

It is:

> a structured candidate move that targets a specific failure layer,  
> with a specific intended effect,  
> under a constrained scope,  
> with explicit validation needs and risk notes

In short:

- Atlas tells us where the failure is
- Fix Surface tells us where to push first
- Repair Action Schema tells us how that push should be represented

---

## 3. Design goals

Repair Action Schema v1 is designed to be:

- compact enough for repeated use
- explicit enough for engineering review
- structured enough for AI systems
- flexible enough for family-specific actions
- strict enough to support later validation

This schema is not trying to capture every future detail.

It is trying to establish a clean and reusable minimum.

---

## 4. Action schema quick map 🗂️

| Part of the action | Main job |
|---|---|
| identity fields | tell us what the action is |
| target fields | tell us where the action is aimed |
| mechanism fields | tell us how the action works |
| safety fields | tell us how far it can go and how risky it is |
| validation fields | tell us how to judge the action afterward |
| rollback and escalation fields | tell us what to do if the action fails |

This page is the right place when the question is **how a repair move should be encoded as a reusable object**, not whether the whole repair workflow is already automated.

---

## 5. Minimal action unit

Every repair action in v1 should contain the following core fields.

### Required fields

- `action_id`
- `action_title`
- `target_family`
- `target_region`
- `repair_type`
- `intended_effect`
- `allowed_scope`
- `risk_level`
- `validation_needed`
- `rollback_hint`

### Optional but recommended fields

- `secondary_pressure`
- `misrepair_risk`
- `preconditions`
- `escalation_if_failed`
- `notes`

This gives us a stable first schema without making the object too heavy.

---

## 6. Field definitions

### `action_id`

A stable identifier for the action.

Example:

- `F1_RG_001`
- `F4_GT_002`
- `F7_SC_001`

This field is for tracking, referencing, validation, and patch evolution.

### `action_title`

A short human-readable name.

Example:

- `Re-ground evidence set`
- `Insert readiness gate`
- `Tighten output schema`

This field should be short and practical.

### `target_family`

The primary family this action is intended to repair.

Allowed examples:

- `F1`
- `F3`
- `F4`
- `F5`
- `F6`
- `F7`

An action may later interact with neighboring families, but it must still declare its primary target family.

### `target_region`

The more specific target area inside the family.

Examples:

- `F1_N01 Retrieval Anchor Drift`
- `F4_N03 Pre-Readiness Execution Failure`
- `F7_N01_A Logic Descriptor Fidelity Failure`

If a node is not yet fully frozen, a stable branch or family entry label may be used.

### `repair_type`

The repair mechanism type.

Suggested early values include:

- `re-grounding`
- `gate insertion`
- `ordering correction`
- `trace exposure`
- `schema tightening`
- `descriptor correction`
- `continuity scaffold`
- `logging uplift`
- `anchor filtering`
- `constraint hardening`

This field helps planners group actions by mechanism rather than only by family.

### `intended_effect`

A short statement of what the action is supposed to improve.

Examples:

- `restore evidence-anchor alignment`
- `prevent downstream execution before readiness`
- `restore valid container fidelity`
- `increase failure-path visibility`

This field should describe the intended repair effect, not implementation details.

### `allowed_scope`

Defines how far the action is allowed to go.

Suggested early values:

- `minimal`
- `constrained`
- `planner-only`
- `safe-suggestion`
- `requires-review`

Examples:

- `minimal` for simple re-grounding
- `constrained` for schema tightening
- `planner-only` for high-risk F6 cases
- `requires-review` for risky structural or policy-sensitive actions

This field is important for safety.

### `risk_level`

A coarse early risk label.

Suggested values:

- `low`
- `medium`
- `high`

This is not the only safety control, but it is a useful first signal.

### `validation_needed`

Defines what kind of check is required after applying the repair.

Suggested early values:

- `output comparison`
- `anchor verification`
- `schema validation`
- `trace visibility check`
- `workflow readiness check`
- `human review`

An action without validation is incomplete.

### `rollback_hint`

A short statement of how to back out if the repair makes things worse.

Examples:

- `restore prior evidence set`
- `remove inserted gate`
- `revert schema constraint`
- `remove added trace layer`

This field can be short in v1, but it must exist.

---

## 7. Optional fields

These are not mandatory in the smallest action unit, but are strongly recommended.

### `secondary_pressure`

Used when the action targets one family but is near another.

Example:

- F1 action near F7 pressure
- F5 action near F6 pressure

This field helps later planner logic.

### `misrepair_risk`

Describes the most likely wrong repair pattern.

Examples:

- `may over-tighten container and hide a grounding issue`
- `may increase observability without repairing the actual failure`
- `may treat continuity failure as an execution failure`

This field is highly valuable for planner quality.

### `preconditions`

Lists what must already be true before the action is safe or meaningful.

Examples:

- `case has confirmed routing confidence >= medium`
- `required schema already exists`
- `readiness state can be checked explicitly`

This prevents premature repair behavior.

### `escalation_if_failed`

Defines what to do if the action does not improve the case.

Examples:

- `switch to alternate F1 action`
- `escalate to human review`
- `escalate to WFGY deep repair`
- `re-check primary family fit`

This field supports later repair workflows.

### `notes`

Free-form short note field.

Use sparingly.

---

## 8. Recommended family-specific action style

Different families tend to prefer different action shapes.

### F1

Usually concrete and anchor-oriented.

Common action styles:

- evidence filtering
- anchor re-check
- re-grounding
- retrieval correction

### F3

Usually continuity-oriented.

Common action styles:

- continuity scaffold
- ownership trace support
- role fencing
- persistence guard

### F4

Usually workflow-structural.

Common action styles:

- gate insertion
- ordering correction
- block-until-ready rule
- closure hardening

### F5

Usually visibility-oriented.

Common action styles:

- trace exposure
- logging uplift
- observability insertion
- coherence probe

### F6

Usually planner-heavy and safety-sensitive.

Common action styles:

- stabilization suggestion
- boundary review
- escalation recommendation
- intervention restraint marker

### F7

Usually container-oriented.

Common action styles:

- schema tightening
- descriptor repair
- shell correction
- structure preservation

This section is not a hard rule set.

It is a practical guide for early consistency.

---

## 9. Example action objects

### Example A · F1 grounding action

```json
{
  "action_id": "F1_RG_001",
  "action_title": "Re-ground evidence set",
  "target_family": "F1",
  "target_region": "F1_N01 Retrieval Anchor Drift",
  "repair_type": "re-grounding",
  "intended_effect": "restore evidence-anchor alignment",
  "allowed_scope": "minimal",
  "risk_level": "low",
  "validation_needed": "anchor verification",
  "rollback_hint": "restore prior evidence set",
  "misrepair_risk": "may hide a representation problem if the real issue is container fidelity",
  "preconditions": [
    "retrieval candidates are available",
    "case routing confidence is at least medium"
  ],
  "escalation_if_failed": "re-check F1 versus F7 boundary"
}
````

### Example B · F4 execution action

```json
{
  "action_id": "F4_GT_001",
  "action_title": "Insert readiness gate",
  "target_family": "F4",
  "target_region": "F4_N03 Pre-Readiness Execution Failure",
  "repair_type": "gate insertion",
  "intended_effect": "prevent downstream execution before upstream readiness is satisfied",
  "allowed_scope": "constrained",
  "risk_level": "medium",
  "validation_needed": "workflow readiness check",
  "rollback_hint": "remove inserted gate",
  "misrepair_risk": "may block useful execution if the true issue is continuity rather than closure",
  "preconditions": [
    "upstream readiness state is inspectable"
  ],
  "escalation_if_failed": "re-check F3 versus F4 cut"
}
```

### Example C · F7 container action

```json
{
  "action_id": "F7_SC_001",
  "action_title": "Tighten output schema",
  "target_family": "F7",
  "target_region": "F7_N01 Symbolic Representation Fidelity Failure",
  "repair_type": "schema tightening",
  "intended_effect": "restore valid container fidelity",
  "allowed_scope": "constrained",
  "risk_level": "low",
  "validation_needed": "schema validation",
  "rollback_hint": "revert schema constraint",
  "misrepair_risk": "may over-constrain the output and hide an upstream grounding issue",
  "preconditions": [
    "a target schema exists"
  ],
  "escalation_if_failed": "re-check F7 versus F1 or F2 boundary"
}
```

---

## 10. What this schema does not yet include

Repair Action Schema v1 does **not** yet try to encode:

* full multi-step repair programs
* execution engine logic
* optimizer scoring
* benchmark automation
* repair success metrics across all domains
* cross-action dependency graphs
* family-specific policy engines

Those may appear later, but should not be forced into v1 too early.

---

## 11. Relationship to planner, validator, and rollback

This schema is meant to become the shared language across three later components:

### Planner

Selects or proposes action objects.

### Validator

Checks whether an action improved the targeted failure.

### Rollback layer

Uses the rollback hint and action identity to back out harmful changes.

This means the action schema is not just a static catalog.

It is the interface contract between later layers.

---

## 12. Early implementation guidance

For early practical use, follow these rules:

1. keep actions small
2. prefer first-move actions
3. avoid overloading one action with multiple families
4. require validation on every action
5. keep rollback hints explicit
6. mark F6-heavy actions as higher caution
7. prefer concrete actions in F1, F4, and F7 first

These rules will make later automation much safer.

---

## 13. Recommended next step

Once this schema is accepted, the most logical next file is:

* [Repair Validation Loop v1](./repair-validation-loop-v1.md)

because a repair action without a clear validation path is still incomplete.

After that, the system will have:

* architecture
* action schema
* validation direction

which is enough to support the first real repair planner draft.

---

## 14. Next steps ✨

After this page, most readers continue with:

1. [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
2. [Open Rollback Policy v1](./rollback-policy-v1.md)
3. [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
4. [Back to Auto Repair Architecture v1](./auto-repair-architecture-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 15. One-line schema summary 🌍

**Repair Action Schema v1 defines the minimum structured unit for Atlas-based repair planning, validation, rollback, and later constrained execution.**
