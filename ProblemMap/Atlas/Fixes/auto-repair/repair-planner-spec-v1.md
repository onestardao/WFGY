<!--
AI_NOTE_START

Document role:
This file defines the first formal specification for the Auto Repair planner layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want the behavior contract for turning a routed Atlas case into a first repair plan.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Action Schema v1](./repair-action-schema-v1.md)
   - [Repair Validation Loop v1](./repair-validation-loop-v1.md)
   - [Rollback Policy v1](./rollback-policy-v1.md)
   - [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
3. Use this page as the planner behavior contract, not as a claim of full autonomous repair.

What this file is:
- The formal behavior specification for the Auto Repair planner layer
- A contract for conservative first repair planning after Atlas routing
- A bridge between routed diagnosis and structured repair output

What this file is not:
- Not Atlas routing from scratch
- Not a code implementation
- Not a benchmark scoring document
- Not proof that full autonomous repair already exists

Reading discipline for AI:
- Respect the routed Atlas case unless severe routing uncertainty is explicit.
- Focus on the first good move, not full repair closure.
- Keep action count small, validation explicit, and escalation available.
- Prefer narrow scope over fake certainty when evidence is weak.

AI_NOTE_END
-->

# Repair Planner Spec v1 🧠

## The behavior contract for Atlas-based first repair planning

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
- [Open Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
- [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
- [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)

---

If the Auto Repair architecture page explains **where the planner sits in the system**, this page explains **what the planner must do and how its output should behave**. 🧭

Its purpose is to make one part of the system operationally clear:

> after Atlas routing is complete,  
> how should the system turn diagnosis into a structured first repair plan?

This document does **not** claim that a full autonomous repair engine already exists.

It claims something narrower and more useful:

> the planner layer now has a clear role, a clear contract, and a clear output shape

---

## Quick start 🚀

### I want the shortest planner reading

Use this path:

1. confirm the case is already routed by Atlas
2. read the minimum planner inputs
3. read the minimum planner outputs
4. read the planner behavior rules
5. inspect the example plan objects

### I want the stronger planner reading

Use this page together with:

1. [Repair Action Schema v1](./repair-action-schema-v1.md)
2. [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
3. [Repair Plan Schema v1](./repair-plan-schema-v1.json)
4. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
5. [Planner Review Checklist v1](./planner-review-checklist-v1.md)

Short version:

> respect the route  
> choose a small first move  
> name validation early  
> escalate instead of bluffing ✨

---

## 1. What the repair planner is

The repair planner is the first active decision layer inside Auto Repair.

It receives a routed case and produces a constrained repair plan.

It is not responsible for:

- discovering the primary family from scratch
- claiming full root-cause closure
- executing arbitrary repair chains
- proving final success

It is responsible for:

- selecting the most plausible repair family
- choosing 1 to 3 candidate repair actions
- ordering those actions
- warning about likely misrepair
- defining what should be validated next
- deciding when escalation is safer than forced repair

In short:

> Atlas decides where the problem belongs.  
> The repair planner decides what first repair moves make sense.

---

## 2. Placement in the system 🧩

The planner sits in this workflow:

```text
case
→ atlas routing
→ fix surface
→ repair planner
→ candidate repair plan
→ validation loop
→ {accept / revise / rollback / escalate}
````

This means the planner depends on prior Atlas discipline.

The planner must not bypass:

* family routing
* broken invariant declaration
* fix-surface selection
* confidence and evidence discipline

If those are missing, the planner should not pretend to be stronger than the inputs.

---

## 3. Planner spec quick map 🗂️

| Planner concern       | Main requirement                                        |
| --------------------- | ------------------------------------------------------- |
| inputs                | consume a routed case with enough structure             |
| output                | emit a compact structured first repair plan             |
| action discipline     | propose only 1 to 3 local actions                       |
| validation discipline | always name the first validation target                 |
| misrepair discipline  | always name the likely wrong path                       |
| escalation discipline | narrow scope or escalate when the case is weak or risky |

This page is the right place when the question is **how the planner should behave as a system layer**, not how to write the exact prompt text or benchmark the model.

---

## 4. Planner design principle

The planner must remain:

* structured
* conservative
* local
* auditable
* repair-first, not theory-first

Its job is to move the case from:

* routed diagnosis

to

* practical first repair planning

without turning that transition into guesswork.

The planner should optimize for:

1. good first move selection
2. low misrepair risk
3. clear validation targets
4. safe escalation when needed

The planner should **not** optimize for:

* maximal cleverness
* long repair stories
* speculative multi-stage interventions
* high-confidence claims under weak evidence

---

## 5. Minimum planner inputs

The repair planner should consume a routed case object with at least the following fields.

### Required inputs

* `case_description`
* `primary_family`
* `secondary_family`
* `why_primary_not_secondary`
* `broken_invariant`
* `best_current_fit`
* `fit_level`
* `fix_surface_direction`
* `confidence`
* `evidence_sufficiency`

### Optional but useful inputs

* `ambiguous`
* `ambiguous_reason`
* `no_fit`
* `misroute_risk`
* `neighbor_pressure`
* `known_constraints`
* `case_type`
* `allowed_intervention_scope`

The planner should treat missing required inputs as a sign to stop, defer, or request stronger routing discipline.

---

## 6. Minimum planner outputs

The planner should produce a structured repair plan object.

### Required outputs

* `selected_repair_family`
* `planner_confidence`
* `plan_scope`
* `candidate_actions`
* `action_ordering`
* `primary_validation_target`
* `misrepair_risk`
* `recommended_next_step`

### Optional but recommended outputs

* `secondary_repair_pressure`
* `escalation_reason`
* `notes`
* `blocked_actions`
* `why_not_other_repair_family`

This output should be compact enough for repeated use and clear enough for engineering review.

---

## 7. Output field definitions

### `selected_repair_family`

The repair family the planner believes should be tried first.

This is usually the same as the routed primary family, but not always.

Examples:

* routed F1 case → selected F1 repair family
* routed F4 case → selected F4 repair family
* routed F5/F6 edge case → planner may remain cautious and choose F5-first repair discipline

This field must remain explicit.

### `planner_confidence`

The planner's confidence in the proposed repair family and action ordering.

Suggested values:

* `low`
* `medium`
* `high`

This should depend on routing quality and evidence sufficiency, not rhetorical certainty.

### `plan_scope`

The allowed intervention scope.

Suggested values:

* `planner-only`
* `minimal`
* `constrained`
* `requires-review`

Examples:

* `planner-only` for high-risk F6 cases
* `minimal` for simple F1 re-grounding
* `constrained` for F4 gate insertion or F7 schema tightening
* `requires-review` for ambiguous multi-family cases

### `candidate_actions`

A list of 1 to 3 repair action objects.

These should be action-schema-compliant proposals.

The planner should not produce a long bag of ideas.

More than 3 actions usually means the planner is under-disciplined.

### `action_ordering`

A short explanation of which action should be tried first, second, and third.

This field matters because repair ordering is often part of the fix itself.

Examples:

* repair grounding before style
* repair readiness before downstream execution
* repair container before adding reasoning pressure
* repair diagnosability before boundary intervention

### `primary_validation_target`

The specific thing that should be checked first after the first action is tried.

Examples:

* anchor alignment
* readiness state
* schema validity
* failure-path visibility

This field prevents vague repair plans.

### `misrepair_risk`

A short description of the most likely wrong repair direction.

Examples:

* treating a grounding issue as a representation issue
* forcing reasoning on an execution problem
* adding visibility without improving diagnosability
* over-tightening the container and hiding semantic failure

This field is mandatory for a good planner.

### `recommended_next_step`

The next operational move after the planner emits the plan.

Suggested values:

* `validate-first-action`
* `revise-routing`
* `escalate-to-review`
* `escalate-to-wfgy`
* `stop-and-wait`

This field keeps the planner connected to the real workflow.

---

## 8. Planner behavior rules

The planner must follow these behavior rules.

### Rule 1

Route first, plan second.

No repair planning should happen without a routed case.

### Rule 2

Prefer the first repair move, not a full repair fantasy.

The planner should plan the opening move, not invent a full closed-loop repair saga.

### Rule 3

Do not widen scope under weak evidence.

Weak evidence should reduce ambition, not increase it.

### Rule 4

Use action-schema language.

Every candidate action should be translatable into a repair action object.

### Rule 5

Always include misrepair risk.

A plan without misrepair awareness is not trustworthy.

### Rule 6

Always name the first validation target.

If the planner cannot say what to validate next, the plan is too vague.

### Rule 7

Escalate early in high-risk regions.

This is especially important for:

* F6-heavy cases
* multi-family ambiguity
* weak routing confidence
* high-abstract legitimacy or boundary cases

---

## 9. Family-specific planning style

Different families should encourage different planner behavior.

### F1 · Grounding and Evidence Integrity

Typical planner style:

* small and concrete
* evidence-centric
* anchor-focused
* validation-friendly

Good first actions:

* re-ground evidence set
* anchor re-check
* retrieval candidate filter
* target-reference audit

Common planner mistake:

* over-interpreting a grounding failure as a representation or reasoning problem

### F3 · State and Continuity Integrity

Typical planner style:

* continuity-sensitive
* state-aware
* careful about ownership and role drift

Good first actions:

* continuity scaffold
* ownership tracing
* role fencing
* persistence guard suggestion

Common planner mistake:

* treating continuity loss as pure execution failure

### F4 · Execution and Contract Integrity

Typical planner style:

* workflow-structural
* ordering-first
* closure-aware
* gate-sensitive

Good first actions:

* insert readiness gate
* block downstream until upstream ready
* ordering correction
* closure-path hardening

Common planner mistake:

* trying to fix execution failure by adding reasoning pressure or more instructions

### F5 · Observability and Diagnosability Integrity

Typical planner style:

* visibility-first
* probe-first
* caution against fake repair

Good first actions:

* trace exposure
* logging uplift
* observability insertion
* coherence probe

Common planner mistake:

* mistaking better visibility for fully repaired failure

### F6 · Boundary and Safety Integrity

Typical planner style:

* extremely cautious
* planner-first
* escalation-friendly
* restraint-aware

Good first actions:

* stabilization suggestion
* boundary review
* risk marker insertion
* escalation recommendation

Common planner mistake:

* jumping directly into strong intervention under weak evidence

The planner should often choose `planner-only` or `requires-review` here.

### F7 · Representation and Localization Integrity

Typical planner style:

* structure-aware
* container-first
* descriptor-sensitive

Good first actions:

* schema tightening
* descriptor correction
* shell repair
* container validation

Common planner mistake:

* forcing reasoning before the container is repaired

---

## 10. Planning sequence

The default planning sequence should be:

1. check whether routing inputs are sufficient
2. confirm the broken invariant
3. select the first repair family
4. choose 1 to 3 candidate actions
5. order them
6. identify the first validation target
7. describe misrepair risk
8. decide whether validation, revision, or escalation should come next

This sequence should remain stable in v1.

---

## 11. Planner stop conditions

The planner should stop and refuse overreach when:

* `no_fit = true`
* routing confidence is too low
* evidence sufficiency is too weak
* the case sits in a high-risk multi-family region
* the planner cannot name a validation target
* the planner cannot describe a safe action scope

In these cases, the planner should prefer:

* `revise-routing`
* `escalate-to-review`
* `escalate-to-wfgy`

rather than pretending to have a valid repair plan.

---

## 12. Example plan object

### Example A · F1 plan

```json
{
  "selected_repair_family": "F1",
  "planner_confidence": "high",
  "plan_scope": "minimal",
  "candidate_actions": [
    {
      "action_id": "F1_RG_001",
      "action_title": "Re-ground evidence set"
    },
    {
      "action_id": "F1_AF_001",
      "action_title": "Filter semantically adjacent but incorrect anchors"
    }
  ],
  "action_ordering": [
    "Try re-grounding first",
    "Then filter adjacent but misleading anchors if needed"
  ],
  "primary_validation_target": "anchor alignment",
  "misrepair_risk": "may over-tighten representation while the real issue remains grounding",
  "recommended_next_step": "validate-first-action"
}
```

### Example B · F4 plan

```json
{
  "selected_repair_family": "F4",
  "planner_confidence": "medium",
  "plan_scope": "constrained",
  "candidate_actions": [
    {
      "action_id": "F4_GT_001",
      "action_title": "Insert readiness gate"
    },
    {
      "action_id": "F4_OC_001",
      "action_title": "Correct downstream ordering"
    }
  ],
  "action_ordering": [
    "Insert readiness gate first",
    "Then review downstream ordering only if closure is still weak"
  ],
  "primary_validation_target": "readiness state",
  "misrepair_risk": "may block valid progress if the real issue is continuity rather than closure",
  "recommended_next_step": "validate-first-action"
}
```

### Example C · F6 cautious plan

```json
{
  "selected_repair_family": "F6",
  "planner_confidence": "low",
  "plan_scope": "planner-only",
  "candidate_actions": [
    {
      "action_id": "F6_BR_001",
      "action_title": "Trigger boundary review"
    },
    {
      "action_id": "F6_ST_001",
      "action_title": "Add stabilization suggestion"
    }
  ],
  "action_ordering": [
    "Review boundary pressure first",
    "Only suggest stabilization under explicit caution"
  ],
  "primary_validation_target": "boundary-risk clarity",
  "misrepair_risk": "may intervene too strongly before diagnosability is adequate",
  "recommended_next_step": "escalate-to-review"
}
```

---

## 13. What this spec does not yet include

Repair Planner Spec v1 does **not** yet define:

* planner code implementation
* token budgeting rules
* model-specific tuning
* exemplar selector logic for repair planning
* benchmark scoring
* planner memory integration
* multi-step adaptive planning loops

Those may come later.

This file only defines the first formal behavior contract.

---

## 14. Recommended companion files

The next useful files after this one are:

* [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
* [Repair Plan Schema v1](./repair-plan-schema-v1.json)

This file defines planner behavior.

Those next files would define:

* how the planner should be prompted
* how the planner output should be serialized

That would complete Phase 1 at a much more operational level.

---

## 15. Success condition for Phase 1

Phase 1 should be considered successful when:

* the planner consumes routed Atlas cases reliably
* the planner selects a repair family conservatively
* the planner proposes 1 to 3 structured actions
* the planner identifies the first validation target
* the planner warns about likely misrepair
* the planner escalates instead of overclaiming when evidence is weak

This is a strong enough milestone for first practical use.

---

## 16. Next steps ✨

After this page, most readers continue with:

1. [Open Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
2. [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
3. [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
4. [Open Planner Test Note v1](./planner-test-note-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 17. One-line planner summary 🌍

**Repair Planner Spec v1 defines how Atlas-based diagnosis should be turned into a structured, conservative, validation-aware first repair plan.**
