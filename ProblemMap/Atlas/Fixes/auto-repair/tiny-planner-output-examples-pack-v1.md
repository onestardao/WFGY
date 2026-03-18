<!--
AI_NOTE_START

Document role:
This file is the first compact positive example pack for the Atlas Auto Repair planner layer.

How to use this file:
1. Read this page when you want concrete examples of what good planner output should look like after Atlas routing is already available.
2. Use this page together with:
   - [Repair Planner Spec v1](./repair-planner-spec-v1.md)
   - [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
   - [Repair Plan Schema v1](./repair-plan-schema-v1.json)
   - [Planner Test Note v1](./planner-test-note-v1.md)
   - [Planner Review Checklist v1](./planner-review-checklist-v1.md)
   - [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
   - [Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
   - [Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
3. Use this page for review calibration, onboarding, demo support, and future regression checks.

What this file is:
- A compact positive example pack for planner outputs
- A reference set for v1 planner style and structure
- A practical bridge between planner rules and visible sample outputs

What this file is not:
- Not a benchmark pack
- Not a complete planner corpus
- Not a failing-output pack
- Not proof that the planner is already production-complete

Reading discipline for AI:
- Treat these examples as style and quality references for first repair planning.
- Keep family alignment, action locality, validation target, misrepair warning, and next-step discipline visible.
- Do not overread these examples as evidence of full repair closure.
- Use them as small reusable references, not as universal templates for every case.

AI_NOTE_END
-->

# Tiny Planner Output Examples Pack v1 🧪

## The first compact positive reference pack for Atlas Auto Repair planner outputs

Quick links:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
- [Open Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
- [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
- [Open Planner Test Note v1](./planner-test-note-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
- [Open Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
- [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)
- [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)

---

If the planner spec explains **what good planner behavior should be**, this pack shows **what that behavior should actually look like in compact output form**. 🧭

Its purpose is practical:

> show a few compact examples of what good planner output should look like  
> after Atlas routing is already available

This file does **not** claim to be a benchmark pack or a complete planner corpus.

It claims something smaller and more useful:

> the project now has a first small set of concrete planner output examples  
> that can be reused for review, onboarding, demos, and future tuning

---

## Quick start 🚀

### I want the shortest example reading

Use this path:

1. read one case summary
2. inspect the planner output object
3. read why it is a good example
4. compare it against the review checklist
5. use it as a reference, not as a universal script

### I want the stronger review path

Use this page together with:

1. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
2. [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
3. [Planner Review Checklist v1](./planner-review-checklist-v1.md)
4. [Planner Test Note v1](./planner-test-note-v1.md)

Short version:

> keep the family  
> keep the action set small  
> name validation clearly  
> warn about the wrong path  
> end with a usable next step ✨

---

## 1. Why this pack exists

The planner layer already has:

- a specification
- a prompt contract
- an output schema
- test notes
- a review checklist

But those layers still benefit from visible examples.

Without examples, people may still ask:

- what does a good planner output actually look like
- how short or detailed should it be
- how should action ordering be written
- what kind of misrepair warning is strong enough
- what kind of next step is considered acceptable

This pack fills that gap.

In short:

> this is the first tiny reference pack for planner output style and quality

---

## 2. What these examples are meant to show

These examples are intentionally small.

They are meant to show:

1. how the planner should stay aligned with the routed family
2. how the planner should propose 1 to 3 actions only
3. how the planner should name a clear validation target
4. how the planner should warn about the main misrepair risk
5. how the planner should choose a reasonable next step

They are not meant to show:

- full repair closure
- full autonomous execution
- benchmark-level diversity
- every possible family pattern

They are first reference samples.

---

## 3. Examples quick map 🗂️

| Example | Main teaching focus |
|---|---|
| F1 example | grounding-first planning should stay concrete and local |
| F4 example | workflow-first planning should stay on closure and ordering |
| F7 example | container-first planning should repair structure before abstract pressure |
| cautious F5 example | boundary-adjacent cases should narrow scope rather than overreach |

This page is the right place when the question is **what good planner output should look like in practice**, not whether the planner has been comprehensively benchmarked.

---

## 4. Pack scope

This v1 pack includes four tiny planner output examples:

- one F1 example
- one F4 example
- one F7 example
- one cautious F5 example

These were chosen because they show:

- grounding-first planning
- execution-first planning
- container-first planning
- observability-first planning under boundary pressure

This is enough for a strong first sample set.

---

## 5. Standard output example format

Each example follows the same shape:

1. Example ID
2. Case summary
3. Planner output object
4. Why this is a good example
5. Main teaching point

This keeps the pack compact and reusable.

---

## Example 1 · F1 Planner Output Example

### Example ID

`TPO_F1_001`

### Case summary

The case is already routed to F1.

The answer is fluent but grounded in a semantically adjacent source chunk rather than the intended source.

The routed diagnosis indicates:

- primary family: F1
- broken invariant: evidence-anchor integrity broken
- best current fit: Retrieval Anchor Drift
- fix surface direction: re-grounding or anchor re-check

### Planner output object

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
      "action_title": "Filter misleading adjacent anchors"
    }
  ],
  "action_ordering": [
    "Try re-grounding first",
    "Then filter semantically adjacent but misleading anchors if needed"
  ],
  "primary_validation_target": "anchor alignment",
  "misrepair_risk": "may over-tighten representation while the real issue remains grounding",
  "recommended_next_step": "validate-first-action"
}
````

### Why this is a good example

This is a good example because:

* it stays in F1
* it proposes only two local actions
* the first validation target is explicit
* the misrepair risk is real and relevant
* the next step is operational rather than vague

### Main teaching point

A good F1 planner output should feel concrete, local, and evidence-aware.

---

## Example 2 · F4 Planner Output Example

### Example ID

`TPO_F4_001`

### Case summary

The case is already routed to F4.

A downstream step is executing before upstream readiness is complete.

The routed diagnosis indicates:

* primary family: F4
* secondary family: F3
* broken invariant: deployment liveness closure broken
* best current fit: Pre-Readiness Execution Failure
* fix surface direction: readiness audit or gate insertion

### Planner output object

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
    "Review downstream ordering only if closure remains weak"
  ],
  "primary_validation_target": "readiness state",
  "misrepair_risk": "may block valid progress if the real issue is continuity rather than closure",
  "recommended_next_step": "validate-first-action",
  "why_not_other_repair_family": "F3 pressure exists, but the first visible break is execution closure rather than continuity loss"
}
```

### Why this is a good example

This is a good example because:

* it stays anchored to F4
* it acknowledges F3 pressure without drifting into it
* it preserves action locality
* it defines a validation target that matches the failure
* it gives a useful neighbor-family explanation

### Main teaching point

A good F4 planner output should repair workflow structure first, not throw more reasoning or instructions at the case.

---

## Example 3 · F7 Planner Output Example

### Example ID

`TPO_F7_001`

### Case summary

The case is already routed to F7.

The content is partly correct, but the structured shell is broken and cannot be consumed reliably.

The routed diagnosis indicates:

* primary family: F7
* broken invariant: container fidelity broken
* best current fit: Symbolic Representation Fidelity Failure
* fix surface direction: schema tightening or shell correction

### Planner output object

```json
{
  "selected_repair_family": "F7",
  "planner_confidence": "medium",
  "plan_scope": "constrained",
  "candidate_actions": [
    {
      "action_id": "F7_SC_001",
      "action_title": "Tighten output schema"
    },
    {
      "action_id": "F7_SH_001",
      "action_title": "Restore shell boundary"
    }
  ],
  "action_ordering": [
    "Tighten the schema shell first",
    "Restore shell boundary only if the output still leaks across fields"
  ],
  "primary_validation_target": "schema validity",
  "misrepair_risk": "may produce a cleaner container while weakening semantic task fit",
  "recommended_next_step": "validate-first-action"
}
```

### Why this is a good example

This is a good example because:

* it chooses container repair rather than abstract reasoning pressure
* it keeps the action set short
* it defines a visible validation target
* it includes a realistic warning about false success

### Main teaching point

A good F7 planner output should repair the shell first and validate structure without pretending that structure alone guarantees truth.

---

## Example 4 · F5 Cautious Planner Output Example

### Example ID

`TPO_F5_001`

### Case summary

The case is already routed to F5 with some neighboring F6 pressure.

The system is hard to inspect, and the failure path remains opaque.

The routed diagnosis indicates:

* primary family: F5
* secondary family: F6
* broken invariant: failure-path visibility broken
* best current fit: Failure Path Opacity
* fix surface direction: trace exposure or observability insertion

### Planner output object

```json
{
  "selected_repair_family": "F5",
  "planner_confidence": "low",
  "plan_scope": "planner-only",
  "candidate_actions": [
    {
      "action_id": "F5_TE_001",
      "action_title": "Insert trace exposure point"
    }
  ],
  "action_ordering": [
    "Expose one narrow hidden transition point first"
  ],
  "primary_validation_target": "failure-path visibility",
  "misrepair_risk": "may add more visible data without improving diagnosability, or may trigger premature boundary intervention",
  "recommended_next_step": "escalate-to-review",
  "secondary_repair_pressure": "F6 boundary pressure remains possible but should not be treated as first repair target yet",
  "why_not_other_repair_family": "the case still lacks sufficient visibility to justify stronger boundary-first intervention",
  "escalation_reason": "routing is usable, but evidence is not strong enough for broader action scope"
}
```

### Why this is a good example

This is a good example because:

* it stays cautious
* it narrows scope instead of pretending certainty
* it proposes only one small action
* it explains why F6 is not first
* it escalates rather than overreaching

### Main teaching point

A good F5 planner output near F6 pressure should become more careful, not more aggressive.

---

## 6. What these examples have in common

Across all four examples, good planner behavior shares the same core traits:

* family-aligned
* small action set
* explicit validation target
* explicit misrepair warning
* realistic scope control
* useful next step

These traits matter more than stylistic polish.

---

## 7. What bad examples would usually look like

These examples also imply what weak planner output looks like.

Common bad patterns include:

* too many actions
* vague action titles
* no validation target
* no misrepair warning
* strong confidence under weak evidence
* neighbor-family drift without explanation
* heroic repair language instead of operational planning

This pack should be used partly as a positive reference set and partly as a negative contrast tool.

---

## 8. How to use this pack

This pack can be used in several practical ways.

### A. Prompt tuning support

Use these examples to see whether planner output matches the intended v1 style.

### B. Review calibration

Use these examples alongside the review checklist so reviewers share the same sense of what “good” looks like.

### C. Demo support

Reuse these examples in small planning demos or repair-planning explanations.

### D. Future planner regression checks

When planner behavior changes later, these examples can serve as a tiny stability reference set.

---

## 9. What this pack does not yet include

Tiny Planner Output Examples Pack v1 does **not** yet include:

* failing output examples in a separate pack
* model-to-model output comparison
* score labels
* benchmark-wide diversity
* cross-family chain outputs
* automated grading logic

Those can come later.

This pack is intentionally compact.

---

## 10. Recommended next step

Once this pack exists, the next useful follow-up is one of these:

1. create a `bad-planner-output-examples-pack-v1.md`
2. create a `tiny-semi-auto-demo-spec-v1.md`
3. create a paired note that maps each planner example to a validation example and rollback example

The strongest immediate next step is probably:

> create a tiny semi-auto demo spec

That would take the planner layer one step closer to visible repair workflow demos.

---

## 11. Next steps ✨

After this page, most readers continue with:

1. [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
2. [Open Planner Test Note v1](./planner-test-note-v1.md)
3. [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
4. [Open Tiny Validation Examples Pack v1](./tiny-validation-examples-pack-v1.md)
5. [Open Tiny Rollback Examples Pack v1](./tiny-rollback-examples-pack-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 12. One-line summary 🌍

**Tiny Planner Output Examples Pack v1 provides the first compact examples of what good Atlas Auto Repair planner output should look like across F1, F4, F7, and cautious F5 cases.**

