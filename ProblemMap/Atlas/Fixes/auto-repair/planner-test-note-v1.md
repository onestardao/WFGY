<!--
AI_NOTE_START

Document role:
This file is the first compact planner test note for the Atlas Auto Repair layer.

How to use this file:
1. Read this page when you want small integration checks for planner behavior.
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
3. Use this page for compact planner checks, prompt tuning support, early demo support, and future planner quality control.

What this file is:
- A compact planner integration note
- A small test layer for planner behavior
- A practical bridge between planner design, validation, and rollback

What this file is not:
- Not a full planner benchmark
- Not a large evaluation dataset
- Not automated grading logic
- Not proof that the whole repair system is solved

Reading discipline for AI:
- Judge whether the planner produces a good first repair plan, not whether the whole case is fully solved.
- Keep family alignment, action locality, validation target, misrepair awareness, and escalation discipline visible.
- Treat this page as a small integration note, not as a performance claim.
- Do not overclaim planner maturity from a few clean tiny tests.

AI_NOTE_END
-->

# Planner Test Note v1 🧪

## Compact integration checks for Atlas Auto Repair planner behavior

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
- [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)

---

If the planner spec explains **how the planner should work**, this note checks **whether the planner, validation logic, and rollback logic can actually line up on the same small cases**. 🧭

Its purpose is practical:

> show how the repair planner, validation logic, and rollback logic connect on the same small cases

This file does **not** claim to be a full planner benchmark.

It claims something smaller and more useful:

> the project now has a first compact test note  
> for checking whether the planner behaves in a structured, conservative, validation-aware way

---

## Quick start 🚀

### I want the shortest test path

Use this path:

1. read the test case summary
2. compare planner output against expected planner shape
3. check good behavior versus bad behavior
4. inspect validation expectation and rollback risk
5. write a short verdict

### I want the stronger planner-check path

Use this page together with:

1. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
2. [Repair Planner Prompt v1](./repair-planner-prompt-v1.md)
3. [Repair Plan Schema v1](./repair-plan-schema-v1.json)
4. [Planner Review Checklist v1](./planner-review-checklist-v1.md)
5. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
6. [Rollback Policy v1](./rollback-policy-v1.md)

Short version:

> keep the family  
> keep the action small  
> name a real validation target  
> leave room for rollback or escalation ✨

---

## 1. Why this note exists

The Auto Repair layer already has:

- planner specification
- planner prompt
- action schema
- validation loop
- rollback policy
- safe early action catalog
- tiny validation examples
- tiny rollback examples

But these components still need a small integration check.

This note exists to answer a simple question:

> if the planner sees a routed case,  
> does it produce the kind of repair plan that later validation and rollback logic can actually support?

That is the core purpose of this file.

In short:

> this is the first small integration note for planner quality

---

## 2. What this test note is trying to check

This note is not testing whether the system can solve all repair problems.

It is testing whether the planner can do the following correctly:

1. stay aligned with the routed family
2. choose a reasonable first repair action
3. avoid obvious misrepair directions
4. define a real first validation target
5. choose a reasonable next step
6. remain conservative under uncertainty
7. leave room for rollback or escalation when needed

That is enough for a first planner test layer.

---

## 3. Planner test quick map 🗂️

| Test area | Main question |
|---|---|
| family alignment | does the planner stay with the routed family |
| action quality | are the actions local, plausible, and limited |
| validation awareness | is there a real first validation target |
| misrepair awareness | does the planner name the likely wrong path |
| scope discipline | is the repair scope reasonable for the case risk |
| outcome discipline | does the planner give a usable next step |

This page is the right place when the question is **whether the planner behaves correctly on small routed cases**, not whether the whole repair universe is complete.

---

## 4. Minimum planner quality criteria

A planner output in this note should be judged against these criteria.

### Criterion 1 · Family alignment

Does the selected repair family remain aligned with the routed case?

### Criterion 2 · Action quality

Are the candidate actions small, local, and plausible?

### Criterion 3 · Validation awareness

Does the plan name a real first validation target?

### Criterion 4 · Misrepair awareness

Does the plan explicitly name the most likely wrong repair direction?

### Criterion 5 · Scope discipline

Does the plan stay within a suitable scope?

### Criterion 6 · Outcome discipline

Does the plan recommend a reasonable next step such as:

- validate-first-action
- revise-routing
- escalate-to-review
- escalate-to-wfgy
- stop-and-wait

These six criteria are the basic planner test frame for v1.

---

## 5. Test format

Each tiny planner test uses the same compact structure:

1. Test ID
2. Routed case summary
3. Expected planner shape
4. Good planner behavior
5. Bad planner behavior
6. Validation expectation
7. Rollback risk
8. Why the test matters

This is not a heavy benchmark format.

It is a compact quality-control note.

---

## Test 1 · F1 Planner Test

### Test ID

`PTN_F1_001`

### Routed case summary

The case is routed to F1.

The answer is fluent but grounded in a semantically adjacent source rather than the correct evidence anchor.

Routed summary:

- primary family: F1
- broken invariant: evidence-anchor integrity broken
- best current fit: Retrieval Anchor Drift
- fix surface direction: re-grounding or anchor re-check

### Expected planner shape

The planner should:

- stay in F1
- choose a small grounding action
- prefer local re-grounding or anchor filtering
- set anchor alignment as the first validation target
- warn against drifting into F7-first or style-first repair

### Good planner behavior

Good output would look like:

- selected repair family = F1
- plan scope = minimal
- candidate actions include `F1_RG_001` or `F1_AF_001`
- primary validation target = anchor alignment
- misrepair risk = over-tightening representation while the real issue remains grounding
- recommended next step = validate-first-action

### Bad planner behavior

Bad output would look like:

- selecting F7 first without clear container failure
- proposing schema tightening as the first move
- proposing too many actions
- failing to name a validation target
- treating fluency as evidence that grounding is already fine

### Validation expectation

Validation should be able to compare:

- before anchor state
- after anchor state
- whether the answer is now tied to the correct source

### Rollback risk

Rollback may be needed if filtering removes truly relevant evidence and makes semantic alignment worse.

### Why the test matters

This test checks whether the planner can keep a grounding problem as a grounding problem.

---

## Test 2 · F4 Planner Test

### Test ID

`PTN_F4_001`

### Routed case summary

The case is routed to F4.

A downstream step is executing before upstream readiness is complete.

Routed summary:

- primary family: F4
- secondary family: F3
- broken invariant: deployment liveness closure broken
- best current fit: Pre-Readiness Execution Failure
- fix surface direction: readiness audit or gate insertion

### Expected planner shape

The planner should:

- stay in F4
- prefer a gate or ordering repair
- avoid trying to repair the case through memory pressure or general reasoning pressure
- choose readiness state as the first validation target
- warn about continuity-versus-closure confusion

### Good planner behavior

Good output would look like:

- selected repair family = F4
- plan scope = constrained
- candidate actions include `F4_GT_001` or `F4_OC_001`
- primary validation target = readiness state
- misrepair risk = treating the case as continuity-only
- recommended next step = validate-first-action

### Bad planner behavior

Bad output would look like:

- choosing F3-first without strong continuity evidence
- adding more instructions instead of closure logic
- proposing broad workflow rewrite too early
- failing to mention gate behavior as the validation target

### Validation expectation

Validation should be able to compare:

- before execution ordering
- after execution ordering
- whether the downstream step is now correctly blocked until ready

### Rollback risk

Rollback may be needed if the inserted gate blocks valid downstream behavior beyond intended scope.

### Why the test matters

This test checks whether the planner can recognize that some failures need workflow repair first, not intelligence pressure.

---

## Test 3 · F7 Planner Test

### Test ID

`PTN_F7_001`

### Routed case summary

The case is routed to F7.

The content is partly correct, but the structured shell is broken and cannot be consumed reliably.

Routed summary:

- primary family: F7
- broken invariant: formal descriptor fidelity broken or container fidelity broken
- best current fit: Symbolic Representation Fidelity Failure
- fix surface direction: schema tightening or shell correction

### Expected planner shape

The planner should:

- stay in F7
- prefer a local structure or schema action
- avoid jumping directly to reasoning pressure
- choose schema validity or shell integrity as the first validation target
- warn about hiding a deeper grounding problem under cleaner structure

### Good planner behavior

Good output would look like:

- selected repair family = F7
- plan scope = constrained
- candidate actions include `F7_SC_001` or `F7_SH_001`
- primary validation target = schema validity or shell integrity
- misrepair risk = cleaner shell but weaker semantic fit
- recommended next step = validate-first-action

### Bad planner behavior

Bad output would look like:

- selecting F2 first without strong progression evidence
- proposing abstract reasoning improvements instead of container repair
- ignoring validation target
- pretending structure is a minor cosmetic issue

### Validation expectation

Validation should be able to compare:

- before schema state
- after schema state
- whether downstream consumption becomes possible

### Rollback risk

Rollback may be needed if structure improves while semantic task fit drops too much.

### Why the test matters

This test checks whether the planner understands the difference between repairing the box and repairing the thought inside the box.

---

## Test 4 · F5 Cautious Planner Test

### Test ID

`PTN_F5_001`

### Routed case summary

The case is routed to F5.

The system is hard to inspect, and the failure path remains opaque, but there is also some neighboring pressure from F6.

Routed summary:

- primary family: F5
- secondary family: F6
- broken invariant: failure-path visibility broken
- best current fit: Failure Path Opacity or Early Warning Deficit
- fix surface direction: trace exposure or observability insertion

### Expected planner shape

The planner should:

- stay cautious
- prefer a narrow visibility-first move
- avoid jumping directly into strong boundary intervention
- choose failure-path visibility as the first validation target
- explicitly warn that better visibility is not full repair

### Good planner behavior

Good output would look like:

- selected repair family = F5
- plan scope = minimal or planner-only
- candidate actions include `F5_TE_001` or `F5_LU_001`
- primary validation target = failure-path visibility
- misrepair risk = adding more noise without improving diagnosability
- recommended next step = validate-first-action or escalate-to-review

### Bad planner behavior

Bad output would look like:

- jumping directly to F6 intervention
- proposing broad system mutation
- treating observability uplift as if the case were fully solved
- escalating action scope under weak evidence

### Validation expectation

Validation should be able to compare:

- before visibility state
- after visibility state
- whether the exposed signal is more useful rather than only more abundant

### Rollback risk

Rollback may be needed if added logging increases noise and reduces practical diagnosability.

### Why the test matters

This test checks whether the planner can stay disciplined near F5 and F6 edges.

---

## 6. What a passing planner should look like

Across these tests, a passing planner should show these repeated traits:

- it respects the routed family
- it proposes only 1 to 3 actions
- it keeps actions local
- it defines a clear first validation target
- it names a realistic misrepair risk
- it stays conservative near dangerous boundaries
- it leaves room for rollback or escalation

If those traits are present consistently, the planner is behaving in the intended v1 style.

---

## 7. What a failing planner should look like

Across these tests, failing planner behavior usually includes one or more of these signs:

- too many candidate actions
- broad intervention under weak evidence
- no explicit validation target
- no explicit misrepair risk
- choosing neighbor-family repair too early
- overconfident tone in boundary-heavy cases
- pretending visibility or structure alone is full repair

These are exactly the behaviors this note is meant to expose early.

---

## 8. How to use this note

This note can be used in at least three ways.

### A. Manual planner review

A human reviewer compares planner output against these tiny tests.

### B. Prompt tuning support

The planner prompt can be adjusted if it repeatedly fails the same tiny cases.

### C. Early demo support

These tests can be reused in tiny repair demos and future validation demos.

This makes the note small but reusable.

---

## 9. What this note does not yet include

Planner Test Note v1 does **not** yet include:

- large planner evaluation datasets
- score aggregation
- pass or fail automation
- model-to-model planner comparison
- benchmark metrics
- cross-family chain tests

Those can come later.

This note is intentionally small and practical.

---

## 10. Recommended next step

Once this note exists, the next useful follow-up is one of these:

1. create a tiny semi-auto demo spec using one F1, one F4, and one F7 action
2. create a planner review checklist
3. create a tiny planner output examples pack

The strongest immediate next step is probably:

> create a tiny planner output examples pack

That would make planner behavior even easier to compare and reuse.

---

## 11. Next steps ✨

After this page, most readers continue with:

1. [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
2. [Open Tiny Planner Output Examples Pack v1](./tiny-planner-output-examples-pack-v1.md)
3. [Open Tiny Semi Auto Demo Spec v1](./tiny-semi-auto-demo-spec-v1.md)
4. [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)

If you want the broader product surface:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

---

## 12. One-line summary 🌍

**Planner Test Note v1 provides the first compact integration tests for whether the Atlas Auto Repair planner produces structured, conservative, validation-aware first repair plans.**
