<!--
AI_NOTE_START

Document role:
This file defines the first small catalog of safe early repair actions for the Auto Repair layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want a controlled shelf of early repair actions that are suitable for planning, validation, demos, and later constrained semi-auto use.
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

What this file is:
- The first safe early action shelf for Auto Repair v1
- A practical catalog of local, inspectable, reversible, and validation-ready repair actions
- A bridge between planner logic and later constrained semi-auto behavior

What this file is not:
- Not the full repair library
- Not a broad multi-step execution pack
- Not proof that all families are equally ready for early semi-auto use
- Not a license to apply actions without validation or rollback discipline

Reading discipline for AI:
- Treat this catalog as an early controlled action shelf, not as the full repair universe.
- Prefer one action first, validate after each move, and keep rollback possible.
- Stay cautious near family boundaries, especially F1/F7, F3/F4, and F5/F6.
- Do not overread limited early F5 actions as permission for broad boundary-heavy intervention.

AI_NOTE_END
-->

# Safe Early Action Catalog v1 🧩

## The first controlled shelf of local, inspectable, reversible, and validation-ready repair actions

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

---

If the planner layer decides **which first repair moves are plausible**, this catalog defines **which early actions are safe enough to put on the shelf for planning, validation, demos, and later constrained semi-auto use**. 🧭

Its purpose is practical:

> before building broader semi-auto repair behavior,  
> define a small set of actions that are local, inspectable, reversible, and validation-friendly

This document does **not** claim that the full repair library already exists.

It claims something narrower and more useful:

> the project now has a first controlled catalog of early repair actions  
> that are suitable for planning, validation, demos, and later constrained semi-auto use

---

## Quick start 🚀

### I want the shortest catalog reading

Use this path:

1. read the catalog use rules
2. inspect the F1, F4, and F7 action groups first
3. check each action’s validation target and rollback hint
4. use only one action first
5. validate before moving to anything else

### I want the stronger system reading

Use this page together with:

1. [Repair Action Schema v1](./repair-action-schema-v1.md)
2. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
3. [Rollback Policy v1](./rollback-policy-v1.md)
4. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
5. [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)

Short version:

> keep the action local  
> make validation clear  
> keep rollback possible  
> stay conservative near boundaries ✨

---

## 1. Why this catalog exists

The current Auto Repair layer already has:

- architecture
- repair action schema
- validation logic
- rollback logic
- planner logic
- semi-auto scope discipline

But without a small action catalog, the system still lacks a practical middle layer between:

- abstract repair planning  
  and
- actual candidate repair moves

This catalog fills that gap.

It gives the system a first set of repair actions that are:

- simple enough to inspect
- small enough to validate
- narrow enough to rollback
- stable enough for demos and future constrained execution

In short:

> this is the first usable action shelf for Auto Repair

---

## 2. Design rule for v1 catalog

This catalog only includes actions that satisfy the early safety rule:

> local, inspectable, reversible, and validation-ready

That means the catalog intentionally prioritizes:

- F1
- F4
- F7

These are the best early families for safe, auditable repair action design.

This catalog does **not** yet aim to cover all families equally.

That is intentional.

---

## 3. Catalog quick map 🗂️

| Family group | Why it appears early | Typical action style |
|---|---|---|
| F1 | concrete grounding fixes are easier to inspect and compare | re-grounding, anchor filtering, source re-check |
| F4 | workflow-structural fixes are often visible and testable | gate insertion, ordering correction, closure hardening |
| F7 | container-level fixes are often directly inspectable in outputs | schema tightening, descriptor repair, shell correction |
| F5 limited set | useful but should stay narrow and caution-heavy | trace exposure, local logging uplift |

This page is the right place when the question is **which early repair actions are safe enough to put into practical use first**, not how to build the full long-term repair library.

---

## 4. Catalog structure

Each action entry in this file follows the same compact structure:

1. Action ID
2. Action Title
3. Target Family
4. Target Region
5. Repair Type
6. Intended Effect
7. Allowed Scope
8. Validation Target
9. Rollback Hint
10. Typical Use Case
11. Main Misrepair Risk
12. When Not To Use

This is a practical catalog format, not a full schema file.

The full schema contract still lives in:

- [Repair Action Schema v1](./repair-action-schema-v1.md)
- [Repair Plan Schema v1](./repair-plan-schema-v1.json)

---

# Part I

# F1 Safe Early Actions

These actions target **Grounding and Evidence Integrity**.

They are usually good early candidates because they are concrete and comparatively easy to inspect.

---

## F1 Action 1

### Action ID
`F1_RG_001`

### Action Title
Re-ground evidence set

### Target Family
F1

### Target Region
F1_N01 Retrieval Anchor Drift

### Repair Type
re-grounding

### Intended Effect
Restore evidence-anchor alignment by replacing the current evidence set with a better-aligned one.

### Allowed Scope
minimal

### Validation Target
anchor alignment

### Rollback Hint
restore prior evidence set

### Typical Use Case
The current answer appears to rely on semantically adjacent but incorrect source chunks.

### Main Misrepair Risk
The repair may hide a deeper representation issue if the real problem is not anchor drift.

### When Not To Use
Do not use as the first move if the main problem is clearly malformed structure or broken container fidelity.

---

## F1 Action 2

### Action ID
`F1_AF_001`

### Action Title
Filter misleading adjacent anchors

### Target Family
F1

### Target Region
F1_N02 Semantic Grounding Mismatch

### Repair Type
anchor filtering

### Intended Effect
Remove candidate evidence that is semantically close but misaligned with the true task target.

### Allowed Scope
minimal

### Validation Target
semantic target fit

### Rollback Hint
restore prior candidate evidence pool

### Typical Use Case
The system keeps choosing near-match references that sound plausible but are not actually target-correct.

### Main Misrepair Risk
The repair may over-prune and remove useful evidence.

### When Not To Use
Do not use when the real issue is missing evidence rather than misleading evidence.

---

## F1 Action 3

### Action ID
`F1_SR_001`

### Action Title
Force source-target recheck

### Target Family
F1

### Target Region
F1_E02 OOD World Grounding Failure

### Repair Type
anchor re-check

### Intended Effect
Require an explicit source-to-target verification step before accepting the current grounding.

### Allowed Scope
constrained

### Validation Target
source match

### Rollback Hint
remove added recheck step

### Typical Use Case
The system appears to answer with decent fluency, but the output is not reliably tied to the correct source target.

### Main Misrepair Risk
The repair may create extra checking without improving true grounding.

### When Not To Use
Do not use if the case has no inspectable source target.

---

# Part II

# F4 Safe Early Actions

These actions target **Execution and Contract Integrity**.

They are strong early candidates because the repair region is often workflow-visible.

---

## F4 Action 1

### Action ID
`F4_GT_001`

### Action Title
Insert readiness gate

### Target Family
F4

### Target Region
F4_N03 Pre-Readiness Execution Failure

### Repair Type
gate insertion

### Intended Effect
Prevent downstream execution from starting before upstream readiness conditions are satisfied.

### Allowed Scope
constrained

### Validation Target
readiness state

### Rollback Hint
remove inserted gate

### Typical Use Case
A step is executing too early because the system treats draft availability as if it were true readiness.

### Main Misrepair Risk
The repair may block valid flow if the gate condition is too broad.

### When Not To Use
Do not use if the real problem is continuity drift rather than closure breakdown.

---

## F4 Action 2

### Action ID
`F4_OC_001`

### Action Title
Correct downstream ordering

### Target Family
F4

### Target Region
F4_N01 Bootstrap Ordering Failure

### Repair Type
ordering correction

### Intended Effect
Restore the correct order of operations so later steps only run after prerequisite steps finish.

### Allowed Scope
constrained

### Validation Target
ordering correctness

### Rollback Hint
restore previous step ordering

### Typical Use Case
A pipeline is failing because one module is consuming incomplete or not-yet-approved upstream outputs.

### Main Misrepair Risk
The repair may reorder visible steps while leaving hidden dependency problems untouched.

### When Not To Use
Do not use if the problem is actually missing observability rather than wrong ordering.

---

## F4 Action 3

### Action ID
`F4_CL_001`

### Action Title
Harden local closure rule

### Target Family
F4

### Target Region
F4_E01 Institutional Enforcement Drift

### Repair Type
closure hardening

### Intended Effect
Strengthen a local closure condition so rule-to-action execution cannot bypass required checks.

### Allowed Scope
requires-review

### Validation Target
closure path stability

### Rollback Hint
restore prior closure rule

### Typical Use Case
A process nominally has a policy or rule, but execution keeps slipping through incomplete enforcement paths.

### Main Misrepair Risk
The repair may produce a stricter-looking closure rule that reduces usability without fixing the underlying enforcement gap.

### When Not To Use
Do not use as an automatic first move in high-ambiguity institutional or boundary-heavy cases.

---

# Part III

# F7 Safe Early Actions

These actions target **Representation and Localization Integrity**.

They are good early targets because the repaired region is often visible in the output container itself.

---

## F7 Action 1

### Action ID
`F7_SC_001`

### Action Title
Tighten output schema

### Target Family
F7

### Target Region
F7_N01 Symbolic Representation Fidelity Failure

### Repair Type
schema tightening

### Intended Effect
Restore valid container structure by explicitly enforcing a tighter schema shell.

### Allowed Scope
constrained

### Validation Target
schema validity

### Rollback Hint
revert schema constraint

### Typical Use Case
The content is partially right, but the output breaks the required structured format.

### Main Misrepair Risk
The repair may improve container validity while silently reducing semantic fit.

### When Not To Use
Do not use before checking whether the real issue is grounding rather than container structure.

---

## F7 Action 2

### Action ID
`F7_DR_001`

### Action Title
Repair descriptor shell

### Target Family
F7

### Target Region
F7_N01_A Logic Descriptor Fidelity Failure

### Repair Type
descriptor correction

### Intended Effect
Make the formal or symbolic descriptor more faithful to the intended reasoning structure.

### Allowed Scope
constrained

### Validation Target
descriptor fidelity

### Rollback Hint
restore prior descriptor wording

### Typical Use Case
The system output keeps drifting because the formal container describing the task is underspecified or structurally weak.

### Main Misrepair Risk
The repair may over-specify the descriptor and force unnatural output behavior.

### When Not To Use
Do not use if the container is already stable and the true problem is progression-first.

---

## F7 Action 3

### Action ID
`F7_SH_001`

### Action Title
Restore shell boundary

### Target Family
F7

### Target Region
F7_E01 Explanation Fidelity Distortion

### Repair Type
shell correction

### Intended Effect
Repair broken object, array, or field boundary so the output shell can hold the intended content correctly.

### Allowed Scope
minimal

### Validation Target
shell integrity

### Rollback Hint
restore prior shell version

### Typical Use Case
The answer content exists, but the structure leaks across fields or breaks object boundaries.

### Main Misrepair Risk
The repair may produce a cleaner shell that still carries the wrong content.

### When Not To Use
Do not use if the shell is valid and the deeper issue is evidence or logic drift.

---

# Part IV

# F5 Limited Early Actions

These actions are included with extra caution.

They are useful, but should mostly remain in suggest-only or narrow apply-and-check mode.

---

## F5 Action 1

### Action ID
`F5_TE_001`

### Action Title
Insert trace exposure point

### Target Family
F5

### Target Region
F5_N01 Failure Path Opacity

### Repair Type
trace exposure

### Intended Effect
Expose one previously hidden step or path so the failure becomes more diagnosable.

### Allowed Scope
minimal

### Validation Target
failure-path visibility

### Rollback Hint
remove added trace point

### Typical Use Case
A workflow is failing, but the hidden transition point cannot currently be inspected.

### Main Misrepair Risk
The repair may add more visible output without making the true bottleneck easier to identify.

### When Not To Use
Do not use if the workflow already has enough visibility and the real problem is execution or boundary failure.

---

## F5 Action 2

### Action ID
`F5_LU_001`

### Action Title
Add local logging uplift

### Target Family
F5

### Target Region
F5_E02 Early Warning Deficit

### Repair Type
logging uplift

### Intended Effect
Increase the observability of a narrow failure region by adding a focused local logging layer.

### Allowed Scope
constrained

### Validation Target
probe usefulness

### Rollback Hint
remove noisy logging layer

### Typical Use Case
The system needs one additional logging or probe layer to identify a pre-failure transition.

### Main Misrepair Risk
The repair may increase noise and reduce practical diagnosability.

### When Not To Use
Do not use as a blanket instrumentation move across the whole system.

---

# Part V

# Catalog use rules 📌

This catalog should be used under the following rules.

## Rule 1

Prefer one action first.

Do not start by throwing multiple categories of repair at the case.

## Rule 2

Validate after each local action.

Do not assume that a seemingly reasonable repair already helped.

## Rule 3

Rollback must stay possible.

If rollback is unclear, the action should not be treated as safe early action.

## Rule 4

Do not treat this catalog as a full repair library.

This is an **early action catalog**, not the final repair universe.

## Rule 5

Use caution near family boundaries.

Especially:

- F1 and F7
- F3 and F4
- F5 and F6

The planner should remain conservative in these regions.

---

# Part VI

# What this catalog does not yet include

Safe Early Action Catalog v1 does **not** yet include:

- large multi-step repair chains
- high-risk F6 intervention actions
- deep continuity mutation actions
- broad workflow redesign actions
- autonomous cross-family repair bundles
- optimizer scoring over action sets

Those belong to later phases, not this v1 catalog.

---

# Part VII

# Recommended next step

Once this catalog exists, the next logical move is one of these:

1. create a small validator example pack for these actions
2. create a small demo spec for one F1, one F4, and one F7 semi-auto action
3. create a planner test note showing how these actions are selected

The strongest immediate next step is probably:

> turn 2 or 3 of these actions into tiny repair planner examples and tiny validation examples

That would make the catalog feel operational very quickly.

---

## Next steps ✨

After this page, most readers continue with:

1. [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
2. [Open Rollback Policy v1](./rollback-policy-v1.md)
3. [Open Planner Test Note v1](./planner-test-note-v1.md)
4. [Open Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)

If you want the broader product surface:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

---

## One-line summary 🌍

**Safe Early Action Catalog v1 defines the first controlled set of local, inspectable, reversible, and validation-ready repair actions for Atlas-based Auto Repair.**
