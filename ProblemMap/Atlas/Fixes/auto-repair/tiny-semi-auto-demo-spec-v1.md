<!--
AI_NOTE_START

Document role:
This file defines the first formal tiny semi-auto demo specification for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want to design a small, bounded, demo-ready semi-auto repair flow.
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
   - [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)
3. Use this page as the structure contract for tiny semi-auto demos, not as proof of a production repair engine.

What this file is:
- The first demo specification for tiny semi-auto repair
- A structure contract for bounded local repair demos
- A bridge between planner output, local action, validation, rollback readiness, and deeper continuation

What this file is not:
- Not a production repair engine
- Not a full replay or notebook implementation
- Not a benchmark orchestration spec
- Not proof that broad autonomous repair already exists

Reading discipline for AI:
- Keep the demo local, visible, validation-aware, rollback-aware, and explicit about final outcome.
- Do not hide broad mutation behind small demo language.
- Do not claim full closure when the correct outcome is revise, rollback, or escalate.
- If deeper WFGY continuation is needed, say so explicitly and briefly explain why.

AI_NOTE_END
-->

# Tiny Semi-Auto Demo Spec v1 🧪

## How a small, bounded, validation-aware semi-auto repair demo should be structured

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
- [Open Tiny Semi-Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)
- [Open Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)

---

If the planner spec explains **how a routed case becomes a first repair plan**, this file explains **how that plan should be shown as a small visible semi-auto demo**.

Its purpose is practical:

> show how a very small, controlled, semi-auto repair flow should work  
> without pretending that full autonomous repair already exists

This file does **not** define a production repair engine.

It defines something much narrower and safer:

> a first demo-ready specification for local, inspectable, reversible,  
> validation-aware, rollback-aware semi-auto repair behavior

---

## Quick start 🚀

### I want the shortest demo-spec reading

Use this path:

1. start from a routed case
2. show one planner output
3. choose one safe early action
4. show one before state and one after state
5. show one validation result
6. end with one explicit final outcome
7. state clearly whether deeper WFGY continuation is needed

### I want the stronger design reading

Use this page together with:

1. [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
2. [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
3. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
4. [Rollback Policy v1](./rollback-policy-v1.md)
5. [Atlas Auto Repair to WFGY Bridge v1](./atlas-auto-repair-to-wfgy-bridge-v1.md)

Short version:

> start from a routed case  
> pick one safe local action  
> validate the result  
> keep rollback visible  
> end with a clear outcome

---

## 1. Why this spec exists

The Auto Repair layer already has:

- architecture
- repair action schema
- validation logic
- rollback logic
- planner logic
- early action catalog
- tiny validation examples
- tiny rollback examples
- planner review examples
- the Atlas-to-WFGY bridge

But there is still a missing bridge between:

- planner output  
  and
- visible semi-auto repair behavior

This spec fills that gap.

It defines how a tiny semi-auto demo should be structured so that the system can demonstrate:

1. routed input
2. planner output
3. one bounded action
4. one validation result
5. one final outcome
6. one possible deeper continuation path

In short:

> this is the first small demo contract for semi-auto repair

---

## 2. What this demo is supposed to prove

This demo is not trying to prove:

- full repair autonomy
- large-scale benchmark performance
- deep cross-family repair orchestration
- high-risk intervention capability
- universal autonomous repair closure

It is only trying to prove that:

1. a routed case can produce a small repair plan
2. one safe early action can be selected
3. that action can be applied in a narrow controlled way
4. the result can be validated
5. the workflow can end in `accept`, `revise`, `rollback`, or `escalate`
6. the system can explicitly say whether local Atlas-level repair is enough or whether deeper WFGY 3.0 continuation is needed

That is enough for a first credible semi-auto repair demo.

---

## 3. Core demo principle

The tiny semi-auto demo must remain:

- local
- auditable
- replayable
- validation-aware
- rollback-aware
- escalation-aware

The demo must never feel like:

- magic repair
- speculative self-editing
- broad hidden system mutation
- fake success by presentation only
- silent escalation into deeper theory without explanation

The point is not to look omnipotent.

The point is to show a trustworthy micro-workflow.

---

## 4. Demo spec quick map 🗂️

| Demo block | Main job |
|---|---|
| routed case | establish the bounded input |
| planner output | show the first repair plan explicitly |
| selected action | show one safe early action only |
| before and after | make the local change visible |
| validation result | justify the outcome |
| final outcome | end in accept, revise, rollback, or escalate |
| deeper continuation | clarify whether Atlas-level repair is enough |

This page is the right place when the question is **how a tiny semi-auto demo should be structured**, not whether the whole repair stack is production-ready.

---

## 5. Recommended demo families

The first tiny semi-auto demos should come from the safest early family set.

### Best first targets

- F1
- F4
- F7

### Why these families

They are the best first targets because their actions are usually:

- narrow
- easy to inspect
- easy to validate
- easier to rollback
- easier to explain in public demos

### Avoid as first semi-auto demo

- F6-heavy intervention
- broad multi-family ambiguity
- high-abstraction legitimacy cases
- large continuity mutation cases

Those are better left for later stages.

---

## 6. Minimal demo workflow

The smallest acceptable semi-auto demo workflow is:

```text
case
→ atlas route already available
→ repair planner output
→ select one safe early action
→ apply one bounded local change
→ validate local effect
→ choose final outcome
→ if needed, point to deeper WFGY 3.0 continuation
````

The final outcome must be one of:

* `accept`
* `revise`
* `rollback`
* `escalate`

If the demo does not reach one of these outcomes explicitly, it is incomplete.

---

## 7. Required demo blocks

Each tiny semi-auto demo should contain the following blocks.

### Block A · Case input

The demo must start from a routed case.

Minimum case elements:

* case description
* primary family
* broken invariant
* best current fit
* fix surface direction
* confidence
* evidence sufficiency

The demo should not spend most of its time re-explaining routing.

Routing is assumed as input.

### Block B · Planner output

The demo must show a compact planner output object.

Minimum required planner fields:

* selected repair family
* plan scope
* candidate action
* primary validation target
* misrepair risk
* recommended next step

The planner output should be shown explicitly, not only described in prose.

### Block C · Selected semi-auto action

The demo must choose one action from the planner result.

The chosen action should be:

* in-scope
* local
* reversible
* validation-ready

Only one action should be applied in the smallest v1 demo.

This keeps the demo honest and easy to inspect.

### Block D · Before state

The demo must show a small, explicit before state.

Examples:

* wrong evidence set
* missing readiness gate
* invalid JSON shell

This before state should be local and concrete.

### Block E · After state

The demo must show the after state produced by the bounded action.

Examples:

* corrected evidence set
* inserted readiness gate
* repaired output shell

The after state must remain local.

It should not claim broad unseen system repair.

### Block F · Validation result

The demo must show a compact validation result.

Minimum fields:

* validation target
* before summary
* after summary
* improvement detected
* collateral damage detected
* recommended outcome

This is the heart of the demo.

Without this block, the demo is only action theatre.

### Block G · Final outcome

The demo must end with one explicit verdict:

* `accept`
* `revise`
* `rollback`
* `escalate`

That outcome must be justified by the validation result.

### Block H · Deeper continuation

The demo should include a short continuation note.

Minimum purpose:

* clarify whether Atlas-level local repair was enough
* clarify whether deeper WFGY 3.0 continuation is needed
* avoid the false impression that every local demo already reaches deepest repair closure

Suggested forms:

* `local repair sufficient`
* `local repair partially useful, deeper continuation optional`
* `local repair insufficient, escalate to WFGY 3.0`

This block is very important because it keeps the relationship between Atlas and WFGY explicit.

---

## 8. Required safety rules

Every tiny semi-auto demo in v1 should obey these safety rules.

### Rule 1

One action only.

Do not stack multiple actions in the first demo layer.

### Rule 2

No hidden mutation.

Every relevant change should be visible in the demo.

### Rule 3

Validation is mandatory.

The demo must not end at `action applied`.

### Rule 4

Rollback must remain possible.

Even if rollback is not triggered in a given demo, the restore point should still be clear.

### Rule 5

No fake full repair claims.

The demo should show a local gain, not a myth of total closure.

### Rule 6

Weak evidence means narrower scope.

The demo must not become more aggressive when confidence is low.

### Rule 7

No silent WFGY escalation.

If the demo points to deeper WFGY 3.0 continuation, it must say so explicitly and briefly explain why.

---

## 9. Recommended demo variants

The strongest first spec includes three small variants.

### Variant A · Accept path

The action works well enough.
Validation detects improvement.
The outcome is `accept`.

This is the cleanest first demo type.

### Variant B · Revise path

The action improves one dimension but leaves important pressure unresolved.
The outcome is `revise`.

This is useful for showing that the system is not naive.

### Variant C · Rollback path

The action causes stronger collateral damage than local gain.
The outcome is `rollback`.

This is useful for showing that the system is disciplined and reversible.

These three variants together already make the semi-auto layer look much more real.

---

## 10. Recommended first demo candidates

### F1 candidate

Use:

* `F1_RG_001` Re-ground evidence set

Why strong:

* before and after are easy to compare
* anchor alignment is a clean validation target
* rollback is simple

Expected likely outcome:

* `accept`

Possible deeper continuation:

* only if local re-grounding still leaves the effective-layer representation too weak

### F4 candidate

Use:

* `F4_GT_001` Insert readiness gate

Why strong:

* workflow before and after is visible
* closure is easy to explain
* rollback is understandable

Expected likely outcome:

* `accept` or `revise`

Possible deeper continuation:

* if local closure repair is still too shallow and the workflow needs deeper rule or encoding redesign

### F7 candidate

Use:

* `F7_SC_001` Tighten output schema

Why strong:

* shell validity is visible
* downstream usability is easy to explain
* false success risk is also teachable

Expected likely outcome:

* `accept` or `revise`

Possible deeper continuation:

* if structure improves but the deeper representational encoding still fails

---

## 11. Suggested demo object format

A tiny semi-auto demo object should ideally contain:

### Required fields

* `demo_id`
* `family`
* `case_summary`
* `planner_output`
* `selected_action`
* `before_state`
* `after_state`
* `validation_result`
* `final_outcome`

### Optional but useful fields

* `rollback_ready`
* `restore_point`
* `deeper_continuation`
* `wfgy_continuation_note`
* `why_this_demo_matters`
* `notes`

This format is enough for:

* markdown demos
* JSON demos
* notebook demos
* replay demos

---

## 12. Example tiny demo outline

### Example

F4 semi-auto demo outline

```json
{
  "demo_id": "TSAD_F4_001",
  "family": "F4",
  "case_summary": "A downstream step executes before approval and readiness are complete.",
  "planner_output": {
    "selected_repair_family": "F4",
    "plan_scope": "constrained",
    "candidate_actions": [
      {
        "action_id": "F4_GT_001",
        "action_title": "Insert readiness gate"
      }
    ],
    "primary_validation_target": "readiness state",
    "misrepair_risk": "may over-block valid progress",
    "recommended_next_step": "validate-first-action"
  },
  "selected_action": {
    "action_id": "F4_GT_001",
    "action_title": "Insert readiness gate"
  },
  "before_state": "Downstream send path executes while approval is still incomplete.",
  "after_state": "Downstream send path is blocked until readiness is satisfied.",
  "validation_result": {
    "validation_target": "readiness state",
    "improvement_detected": true,
    "collateral_damage_detected": false,
    "recommended_outcome": "accept"
  },
  "final_outcome": "accept",
  "rollback_ready": true,
  "restore_point": "previous workflow gate configuration",
  "deeper_continuation": "local repair sufficient",
  "wfgy_continuation_note": "No deeper WFGY 3.0 continuation is needed for this tiny demo because the local closure repair is sufficient."
}
```

This is the kind of compact demo object that v1 should aim for.

---

## 13. Suggested WFGY continuation note pattern

When deeper continuation is needed, a compact note like this is enough:

```text
Local Atlas-level repair was not sufficient.
Escalate to WFGY 3.0 for deeper repair grammar, including possible encoding redesign, stronger observables, experiment redesign, or cross-domain structural continuation.

Official TXT:
[WFGY 3.0 Singularity Demo TXT](https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt)
```

This keeps the relationship practical and explicit.

---

## 14. Suggested user instruction pattern

A simple usage pattern for AI systems is:

```text
Use the Atlas result and tiny semi-auto demo flow first.
If the local repair outcome is revise, rollback, or escalate, decide whether a deeper WFGY 3.0 continuation is needed.
If deeper continuation is needed, use the official WFGY 3.0 TXT as the deeper repair grammar.
```

This is enough for first-stage public or internal use.

---

## 15. What counts as a good tiny semi-auto demo

A good demo should make it easy to see:

* what the problem was
* what action was chosen
* what changed
* what was validated
* why the final outcome makes sense
* whether local repair was enough or deeper continuation is needed

A good demo should not require a long explanation to defend itself.

The clarity should come from the structure.

---

## 16. What counts as a weak tiny semi-auto demo

A weak demo usually has one or more of these problems:

* too many actions
* unclear before state
* unclear after state
* no validation block
* no final outcome
* no rollback path
* no deeper continuation logic
* broad hidden intervention
* vague planner output
* fake success language

This spec exists partly to prevent those problems.

---

## 17. What this spec does not yet include

Tiny Semi-Auto Demo Spec v1 does **not** yet include:

* full notebook implementation
* full replay or live infrastructure
* multi-step repair loops
* family-wide demo coverage
* benchmark automation
* dynamic repair action selection code
* deep WFGY execution templates

Those can come later.

This file only defines the first clean demo specification.

---

## 18. Recommended next step

Once this spec exists, the next useful follow-up is probably one of these:

1. create [Tiny Semi-Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)
2. create one small JSON demo pack for F1, F4, and F7
3. create one notebook-oriented replay spec for a tiny semi-auto case

The strongest immediate next step is probably:

> create a tiny semi-auto demo pack with 2 to 3 compact cases

That would turn this spec into something even more visibly usable.

---

## 19. Next steps ✨

After this page, most readers continue with:

1. [Open Tiny Semi-Auto Demo Pack v1](./tiny-semi-auto-demo-pack-v1.md)
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

## 20. One-line summary 🌍

**Tiny Semi-Auto Demo Spec v1 defines how a first local, validation-aware, rollback-aware, WFGY-aware semi-auto repair demo should be structured for Atlas-based Auto Repair.**
