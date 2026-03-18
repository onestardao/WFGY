<!--
AI_NOTE_START

Document role:
This file defines the first formal rollback policy for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when a proposed or applied repair may need to be backed out.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Action Schema v1](./repair-action-schema-v1.md)
   - [Repair Validation Loop v1](./repair-validation-loop-v1.md)
   - [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
3. Use this page as the rollback policy contract for deciding what should be restored, how far rollback should go, and what the next safe step should be.

What this file is:
- The rollback policy page for Auto Repair v1
- A contract for backing out of harmful or unhelpful repair actions
- A stability-preserving decision layer after failed validation

What this file is not:
- Not full rollback automation
- Not a deployment-grade restoration engine
- Not proof that every rollback can be executed automatically
- Not a replacement for planner or validation logic

Reading discipline for AI:
- Treat rollback as a normal branch of the repair workflow, not as an embarrassment case.
- Keep rollback target, rollback reason, restore point, and next step visible.
- Prefer explicit safety and stability over rhetorical confidence.
- Distinguish clearly between rollback and escalation.

AI_NOTE_END
-->

# Rollback Policy v1 ↩️

## How Atlas-based repair should back out safely after harmful or unhelpful repair moves

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
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
- [Open Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)

---

If the validation loop decides **whether a repair helped enough to keep**, this rollback policy defines **what should happen when the repair should not be kept**.

This document does **not** claim that full rollback automation already exists.

Instead, it defines the first formal policy for a simple but critical requirement:

> if a repair makes the case worse,  
> or repairs the wrong layer,  
> or creates stronger collateral damage,  
> the system must be able to stop, back out, and recover safely

Without rollback policy, Auto Repair becomes too fragile to trust.

---

## Quick start

### I want the shortest rollback reading

Use this path:

1. identify the failed or harmful repair action
2. identify the rollback reason
3. identify the restore point
4. choose rollback scope
5. decide the next step after rollback

### I want the stronger workflow reading

Use this page together with:

1. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
2. [Repair Action Schema v1](./repair-action-schema-v1.md)
3. [Repair Planner Spec v1](./repair-planner-spec-v1.md)

Short version:

> detect the harm  
> restore the safer prior state  
> then revise or escalate

---

## 1. What this document is for

This file defines the rollback layer for Auto Repair v1.

Its purpose is to explain:

- when rollback should be considered
- when rollback should be required
- what rollback is supposed to restore
- what rollback should not pretend to solve
- how rollback relates to validation and escalation

This document should be read together with:

- [README](./README.md)
- [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
- [Repair Action Schema v1](./repair-action-schema-v1.md)
- [Repair Validation Loop v1](./repair-validation-loop-v1.md)

Together, those files define:

- what Auto Repair is
- how repair actions are represented
- how repairs are validated
- how failed or harmful repairs are reversed

---

## 2. Why rollback must exist

A repair proposal can be directionally correct and still fail in practice.

Examples:

- a grounding repair may remove useful evidence while trying to re-anchor the answer
- a readiness gate may prevent harmful execution but also block valid execution paths
- a schema repair may improve structure while degrading semantics
- an observability uplift may flood the workflow with noise
- a boundary-focused intervention may destabilize a case that first needed diagnosability

So Auto Repair cannot be trusted unless it includes a formal way to back out of harm.

Rollback is not a sign of weakness.

It is a sign that the system understands that repair is reversible, local, and evidence-sensitive.

---

## 3. Placement in the workflow

The intended workflow is:

```text
case
→ atlas routing
→ fix surface
→ repair planner
→ candidate repair action
→ validation loop
→ {accept / revise / rollback / escalate}
````

Rollback is therefore not a separate side system.

It is one of the normal outcomes of validation.

This means:

* validation decides whether rollback is needed
* rollback restores or removes the harmful repair move
* the workflow then either stops, revises, or escalates

---

## 4. Rollback quick map

| Rollback concern     | Main question                                   |
| -------------------- | ----------------------------------------------- |
| rollback target      | what action or patch are we reversing           |
| rollback reason      | why is rollback necessary                       |
| rollback scope       | how much of the change should be reversed       |
| restore point        | what prior state should we return to            |
| post-rollback status | what state should exist after rollback          |
| next step            | what should happen after the rollback completes |

This page is the right place when the question is **how to back out safely from a bad repair move**, not how to validate the repair in the first place.

---

## 5. Core rollback principle

Rollback should answer one question clearly:

> what should be restored or removed so that the system does not remain trapped in a worse local state?

This means rollback is not meant to solve the whole case.

It is meant to:

* undo harmful local change
* restore prior workable state
* preserve evidence for later review
* create a safer next step

Rollback is therefore a **stability-preserving operation**, not a victory condition.

---

## 6. Minimal rollback contract

Every rollback decision in v1 should aim to produce these outputs.

### Required outputs

* `rollback_target`
* `rollback_reason`
* `rollback_scope`
* `restore_point`
* `post_rollback_status`
* `next_step`

### Optional but recommended outputs

* `collateral_damage_summary`
* `failed_invariant_target`
* `retry_allowed`
* `escalation_needed`
* `notes`

This creates a reusable rollback object for later planner and validator integration.

---

## 7. Field definitions

### `rollback_target`

The action, patch, or change being reversed.

Examples:

* `F1_RG_001`
* `F4_GT_001`
* `F7_SC_001`

This field ties rollback back to the repair action identity.

### `rollback_reason`

A short statement of why rollback is necessary.

Examples:

* `repair worsened semantic alignment`
* `repair blocked valid execution`
* `repair improved visibility but increased noise too much`
* `repair targeted the wrong family layer`

This field should be explicit and local.

### `rollback_scope`

How much of the repair is being reversed.

Suggested early values:

* `full`
* `partial`
* `last-step-only`
* `planner-level-only`

Examples:

* `full` when the entire action should be removed
* `partial` when only part of the patch caused damage
* `last-step-only` when a multi-part repair should back out only its final move
* `planner-level-only` when the system should cancel the proposed action before execution

### `restore_point`

The state the rollback should attempt to return to.

Examples:

* `prior evidence set`
* `previous gate configuration`
* `prior schema version`
* `pre-observability patch state`

This field is essential because rollback without a restore point becomes vague.

### `post_rollback_status`

A short summary of the expected state after rollback.

Examples:

* `returned to prior evidence configuration`
* `removed blocking gate and restored previous workflow path`
* `restored earlier schema shell`
* `removed noisy trace expansion`

This field should describe the recovery target, not the entire system.

### `next_step`

What the system should do after rollback.

Suggested values:

* `revise`
* `retry with alternate action`
* `re-check family fit`
* `escalate`
* `human review`

Rollback should never end in silence.

It should always lead to a clear next step.

---

## 8. When rollback should be considered

Rollback should be considered whenever validation shows one or more of the following:

1. the target invariant did not improve
2. the repair made the target state worse
3. the repair created stronger collateral damage
4. the repair changed the wrong layer first
5. the repair increased opacity or instability
6. the repair crossed a safety-sensitive boundary too early

These do not always force rollback, but they should trigger serious review.

---

## 9. When rollback should be required

Rollback should be treated as required in v1 when:

### Case A · clear degradation

The repair produces a worse result than the pre-repair state.

Examples:

* grounding becomes less accurate
* execution becomes more blocked than intended
* schema validity improves but task usefulness collapses

### Case B · wrong-layer repair

The action clearly attacked the wrong layer first.

Examples:

* style-level rewrite applied to a grounding problem
* reasoning pressure applied to a closure problem
* schema tightening applied before checking grounding

### Case C · stronger collateral damage than local gain

The action improved one local feature, but introduced greater damage elsewhere.

Examples:

* valid JSON but degraded semantic truth
* more logs but less diagnosability
* stronger gate but broken workflow usability

### Case D · safety boundary crossing

The action enters a higher-risk region without sufficient justification or review.

This is especially important for:

* F6-heavy cases
* F5 and F6 edge cases
* complex multi-family cases with weak evidence

---

## 10. Rollback is not failure by embarrassment

Rollback must be treated as a normal and legitimate branch of the repair workflow.

It does **not** mean:

* the system is useless
* the planner was illegitimate
* the whole atlas route was wrong
* the case is impossible

It means:

> the proposed repair did not hold under validation,
> so the system preserved stability by backing out safely

That is healthy behavior.

---

## 11. Relationship to validation

Validation and rollback are tightly linked.

Validation asks:

* did the action improve the target invariant
* was there collateral damage
* what outcome is recommended

Rollback responds when the recommended outcome is:

* `rollback`

This means rollback is not an emotional judgment.

It is a policy response to failed or harmful repair validation.

In practical terms:

* validation detects
* rollback restores
* planner or escalation decides what comes next

---

## 12. Relationship to escalation

Rollback and escalation are different.

### Rollback

Undo the harmful or unhelpful local move.

### Escalation

Move the case upward into:

* alternate repair family
* deeper WFGY repair
* human review
* more cautious planner logic

A case may require both:

1. rollback first
2. then escalate

This is common when the system learns that the current repair layer is not sufficient.

---

## 13. Recommended rollback sequence

The recommended early rollback sequence is:

1. identify the failed or harmful repair action
2. identify the restore point
3. reverse the local action
4. confirm the post-rollback state
5. choose the next step
6. record the rollback reason for future learning

This keeps rollback auditable and reusable.

---

## 14. Family-specific rollback examples

Different families often need different rollback logic.

### F1 · Grounding and Evidence Integrity

Common rollback targets:

* revert evidence set
* restore prior anchor selection
* restore prior retrieval candidate set

Typical rollback trigger:

* new grounding is cleaner-looking but less aligned with the true source

Typical next step:

* retry alternate grounding action
* re-check F1 versus F7 boundary

### F4 · Execution and Contract Integrity

Common rollback targets:

* remove inserted gate
* restore prior ordering rule
* restore previous workflow routing

Typical rollback trigger:

* closure became safer locally but blocked valid downstream progress

Typical next step:

* revise the gate condition
* re-check F3 versus F4 cut
* escalate if workflow state is ambiguous

### F7 · Representation and Localization Integrity

Common rollback targets:

* revert schema constraint
* restore prior descriptor
* undo shell tightening

Typical rollback trigger:

* structure improves but content fidelity drops too much

Typical next step:

* revise schema
* re-check F7 versus F1 or F2 boundary

### F5 · Observability and Diagnosability Integrity

Common rollback targets:

* remove noisy trace expansion
* restore simpler logging layer
* remove low-signal instrumentation

Typical rollback trigger:

* more information appears, but diagnosability becomes worse

Typical next step:

* redesign observability uplift
* narrow the probe target

### F6 · Boundary and Safety Integrity

Early rollback in F6 should be highly cautious.

Typical rollback target:

* undo overly aggressive intervention proposal
* revert premature stabilization logic
* remove unjustified constraint tightening

Typical rollback trigger:

* intervention changed the case without sufficient evidence
* the repair entered policy or legitimacy space too early

Typical next step:

* escalate
* move to planner-only mode
* require stronger review

---

## 15. Rollback and confidence discipline

Rollback decisions should also carry confidence discipline.

Confidence should be lower when:

* before and after comparison is weak
* multiple families remain plausible
* restore point is unclear
* collateral damage is suspected but not well measured
* the case sits in a high-abstract or multi-family zone

In those cases, rollback may still be the safest action,
but the system should say so with appropriate caution.

---

## 16. Example rollback objects

### Example A · F1 rollback

```json
{
  "rollback_target": "F1_RG_001",
  "rollback_reason": "re-grounded evidence reduced semantic alignment with the true source",
  "rollback_scope": "full",
  "restore_point": "prior evidence set",
  "post_rollback_status": "restored prior retrieval anchor configuration",
  "next_step": "retry with alternate action"
}
```

### Example B · F4 rollback

```json
{
  "rollback_target": "F4_GT_001",
  "rollback_reason": "inserted readiness gate blocked valid downstream execution beyond intended scope",
  "rollback_scope": "partial",
  "restore_point": "previous workflow gate configuration",
  "post_rollback_status": "removed over-restrictive gate condition",
  "next_step": "revise"
}
```

### Example C · F7 rollback

```json
{
  "rollback_target": "F7_SC_001",
  "rollback_reason": "schema tightening improved structure but degraded semantic task fit",
  "rollback_scope": "full",
  "restore_point": "prior schema version",
  "post_rollback_status": "restored earlier output shell",
  "next_step": "re-check family fit"
}
```

---

## 17. What v1 does not yet include

Rollback Policy v1 does **not** yet include:

* full automated rollback execution code
* deployment-grade state restoration engines
* distributed rollback orchestration
* family-wide rollback metrics
* rollback optimization policies
* full repair history memory integration

Those can come later.

v1 only aims to define the rollback logic clearly enough for safe staged growth.

---

## 18. Recommended next step

Once this file exists, the next logical file is:

* [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)

because the folder will then already contain:

* README
* architecture
* action schema
* validation loop
* rollback policy

At that point, the next best move is to state clearly:

* what is already established
* what comes in Phase 1
* what comes later
* what is intentionally delayed

That roadmap will make the folder feel complete as a first-stage system.

---

## 19. Next steps

After this page, most readers continue with:

1. [Open Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
2. [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
3. [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
4. [Back to Auto Repair Architecture v1](./auto-repair-architecture-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 20. One-line rollback summary

**Rollback Policy v1 defines when Atlas-based repair should back out, what should be restored, and how the system should safely continue through revision or escalation.**
