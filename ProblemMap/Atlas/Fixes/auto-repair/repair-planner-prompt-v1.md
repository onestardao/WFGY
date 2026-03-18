<!--
AI_NOTE_START

Document role:
This file defines the first formal prompt specification for the Auto Repair planner layer inside the Atlas Fixes package.

How to use this file:
1. Read this page when you want to prompt a model to turn a routed Atlas case into a conservative first repair plan.
2. Use this page together with:
   - [Auto Repair v1 README](./README.md)
   - [Auto Repair Architecture v1](./auto-repair-architecture-v1.md)
   - [Repair Action Schema v1](./repair-action-schema-v1.md)
   - [Repair Validation Loop v1](./repair-validation-loop-v1.md)
   - [Rollback Policy v1](./rollback-policy-v1.md)
   - [Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)
   - [Repair Planner Spec v1](./repair-planner-spec-v1.md)
3. Use this page as the behavior contract for the planner prompt, not as a claim of full autonomous repair.

What this file is:
- The first prompt behavior contract for the Auto Repair planner layer
- A prompt design page for conservative first repair planning
- A structured transition surface from routed case to repair plan

What this file is not:
- Not Atlas routing from scratch
- Not unrestricted repair execution
- Not a benchmark storytelling file
- Not proof of full autonomous repair closure

Reading discipline for AI:
- Respect the given Atlas routing unless severe routing uncertainty is explicit.
- Focus on the first good repair move, not full repair closure.
- Keep validation target, misrepair risk, and escalation logic visible.
- Prefer narrow scope over fake precision when evidence is weak.

AI_NOTE_END
-->

# Repair Planner Prompt v1 🧠

## How a routed Atlas case should become a conservative first repair plan

Quick links:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)
- [Open Repair Planner Spec v1](./repair-planner-spec-v1.md)
- [Open Repair Action Schema v1](./repair-action-schema-v1.md)
- [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
- [Open Rollback Policy v1](./rollback-policy-v1.md)
- [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
- [Open Planner Test Note v1](./planner-test-note-v1.md)
- [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
- [Open Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)

---

If the planner spec explains **what the planner layer should do**, this page explains **how to prompt a model so it actually behaves that way in practice**. 🧭

Its purpose is simple:

> given a routed Atlas case,  
> prompt the model to produce a conservative, structured, validation-aware first repair plan

This file does **not** claim to solve full autonomous repair.

It only defines how the planner should think and speak at the first operational planning layer.

---

## Quick start 🚀

### I want the shortest planner prompt path

Use this path:

1. confirm the case is already routed by Atlas
2. use the base prompt template
3. require structured output only
4. check the output with the review checklist
5. narrow scope or escalate if evidence is weak

### I want the stronger planner setup path

Use this page together with:

1. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
2. [Repair Action Schema v1](./repair-action-schema-v1.md)
3. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
4. [Rollback Policy v1](./rollback-policy-v1.md)
5. [Planner Review Checklist v1](./planner-review-checklist-v1.md)

Short version:

> respect the route  
> choose only a few actions  
> name validation first  
> escalate instead of bluffing ✨

---

## 1. What this prompt is for

This prompt is for the planner stage only.

It is not for:

- Atlas routing from scratch
- unrestricted repair execution
- long-form speculative diagnosis essays
- benchmark storytelling
- full autonomous repair closure

It is for one specific transition:

> routed case  
> to  
> structured first repair plan

The planner should produce:

- a selected repair family
- 1 to 3 candidate repair actions
- action ordering
- the first validation target
- likely misrepair risk
- the next safe operational step

---

## 2. Planner prompt quick map 🗂️

| Prompt concern | Main requirement |
|---|---|
| routing discipline | do not redo routing unless severe uncertainty is explicit |
| action discipline | propose only 1 to 3 local actions |
| validation discipline | always name the first validation target |
| misrepair discipline | name the likely wrong path |
| scope discipline | choose an appropriate `plan_scope` |
| escalation discipline | narrow or escalate when evidence is weak |

This page is the right place when the question is **how the planner prompt should behave**, not whether the whole repair loop is already automated.

---

## 3. Planner prompt design goals

The planner prompt should make the model behave in a way that is:

- conservative
- structured
- family-aware
- validation-aware
- escalation-capable
- resistant to repair fantasy

The prompt should reduce the chance of these failure modes:

- overconfident repair planning under weak evidence
- treating repair as a storytelling task
- proposing too many actions
- skipping validation
- confusing repair family with neighbor pressure
- forcing strong intervention in boundary-heavy cases

---

## 4. Core planner behavior

The planner must follow these principles.

### Principle 1

Route first, plan second.

The planner must assume Atlas routing already happened.  
It should not redo the full routing task unless the input explicitly signals routing failure.

### Principle 2

Prefer the first good move.

The planner should optimize for the first repair move or first small repair set.

It should not pretend to complete the whole repair journey.

### Principle 3

Validation is part of the plan.

Every repair plan must include the first thing to validate.

### Principle 4

Misrepair risk must be explicit.

The planner must state the most likely wrong repair direction.

### Principle 5

Escalation is allowed.

If evidence is weak or the case is too risky, the planner must prefer escalation over fake precision.

---

## 5. Minimum planner input contract

The prompt should assume the following input object shape.

### Required fields

- `case_description`
- `primary_family`
- `secondary_family`
- `why_primary_not_secondary`
- `broken_invariant`
- `best_current_fit`
- `fit_level`
- `fix_surface_direction`
- `confidence`
- `evidence_sufficiency`

### Optional but useful fields

- `ambiguous`
- `ambiguous_reason`
- `no_fit`
- `misroute_risk`
- `neighbor_pressure`
- `known_constraints`
- `allowed_intervention_scope`

If required fields are missing, the planner should respond conservatively and avoid pretending it has enough basis.

---

## 6. Minimum planner output contract

The planner should return a structured object with these fields.

### Required fields

- `selected_repair_family`
- `planner_confidence`
- `plan_scope`
- `candidate_actions`
- `action_ordering`
- `primary_validation_target`
- `misrepair_risk`
- `recommended_next_step`

### Optional but recommended fields

- `secondary_repair_pressure`
- `why_not_other_repair_family`
- `escalation_reason`
- `notes`

The prompt should strongly encourage short, structured output rather than prose-heavy output.

---

## 7. Candidate action rules

The planner should obey the following rules when proposing actions.

### Rule A

Propose **1 to 3** candidate actions only.

### Rule B

Each action should be small enough to validate.

### Rule C

Each action should be compatible with the [Repair Action Schema v1](./repair-action-schema-v1.md).

### Rule D

Actions should target the routed failure layer first.

### Rule E

If the case is high-risk, prefer fewer actions and narrower scope.

### Rule F

If the case is too ambiguous, do not invent strong action proposals.

---

## 8. Scope discipline

The planner must always set a `plan_scope`.

Suggested values:

- `planner-only`
- `minimal`
- `constrained`
- `requires-review`

The prompt should encourage this logic:

### `planner-only`

Use when:

- case is highly ambiguous
- evidence is weak
- family boundary risk is high
- F6 pressure is heavy

### `minimal`

Use when:

- action is concrete
- validation is easy
- rollback is easy
- risk is low

### `constrained`

Use when:

- action is still local
- but requires explicit caution
- and may affect workflow or structure more strongly

### `requires-review`

Use when:

- intervention has meaningful policy, legitimacy, or system-wide risk
- human or deeper WFGY review is safer

---

## 9. Family-specific planning guidance

The prompt should encode the following family-specific tendencies.

### F1 · Grounding and Evidence Integrity

Prefer:

- re-grounding
- anchor re-check
- evidence filtering
- retrieval correction

Avoid:

- container-first repair unless F7 pressure is clearly primary
- stylistic repair
- abstract reasoning pressure as the first move

### F3 · State and Continuity Integrity

Prefer:

- continuity scaffold
- ownership tracing
- role fencing
- persistence support

Avoid:

- treating continuity drift as pure closure failure unless F4 is clearly stronger

### F4 · Execution and Contract Integrity

Prefer:

- readiness gate insertion
- ordering correction
- block-until-ready logic
- closure hardening

Avoid:

- adding more reasoning pressure
- adding more instructions as the first repair move
- treating the problem as memory-first unless F3 is stronger

### F5 · Observability and Diagnosability Integrity

Prefer:

- trace exposure
- logging uplift
- observability insertion
- coherence probe

Avoid:

- pretending visibility uplift fully repairs the case
- escalating to boundary intervention too early

### F6 · Boundary and Safety Integrity

Prefer:

- stabilization suggestion
- boundary review
- intervention restraint
- escalation recommendation

Avoid:

- aggressive automatic intervention
- high-confidence repair planning under weak evidence
- strong action scope unless review is available

### F7 · Representation and Localization Integrity

Prefer:

- schema tightening
- descriptor correction
- shell repair
- container validation

Avoid:

- forcing reasoning before repairing the container
- treating broken shells as pure F2 failures too early

---

## 10. Stop and caution conditions

The prompt should instruct the planner to stop or narrow scope when:

- `no_fit = true`
- `confidence = low`
- `evidence_sufficiency = low`
- multiple families remain strongly plausible
- the planner cannot name a clean validation target
- the repair would enter a high-risk boundary region too early

In such cases, the planner should prefer:

- `revise-routing`
- `escalate-to-review`
- `escalate-to-wfgy`
- `stop-and-wait`

---

## 11. Prompt style rules

The planner prompt should produce output that is:

- compact
- structured
- operational
- non-dramatic
- explicit about uncertainty

The planner prompt should avoid:

- essays
- philosophical wandering
- long justifications
- fake certainty
- too many candidate repairs
- grand repair promises

---

## 12. Recommended base prompt template

Use the following as the first planner prompt template.

### Base prompt

```text
You are the Repair Planner layer for Problem Map 3.0 Troubleshooting Atlas.

Your task is not to re-route the case from scratch.
Your task is to turn an already routed case into a conservative first repair plan.

You must follow these rules:

1. Respect the given Atlas routing unless the input explicitly indicates severe routing uncertainty.
2. Focus on the first repair move, not full repair closure.
3. Propose only 1 to 3 candidate actions.
4. Every action must be small enough to validate.
5. You must name the first validation target.
6. You must name the main misrepair risk.
7. If evidence is weak or boundary risk is high, reduce scope or escalate.
8. Do not use long prose. Return a structured output only.

Input case fields:
- case_description
- primary_family
- secondary_family
- why_primary_not_secondary
- broken_invariant
- best_current_fit
- fit_level
- fix_surface_direction
- confidence
- evidence_sufficiency
- ambiguous
- ambiguous_reason
- no_fit
- neighbor_pressure
- known_constraints
- allowed_intervention_scope

Return an object with:
- selected_repair_family
- planner_confidence
- plan_scope
- candidate_actions
- action_ordering
- primary_validation_target
- misrepair_risk
- recommended_next_step
- optional secondary_repair_pressure
- optional why_not_other_repair_family
- optional escalation_reason
- optional notes

Candidate actions must align with Atlas fix discipline.
Prefer concrete actions in F1, F4, and F7.
Be especially cautious in F6-heavy cases.

If the case is too ambiguous, do not fake precision.
Choose a narrow scope or escalate.
````

---

## 13. Recommended stricter variant

Use this when you want the planner to stay extra hard and minimal.

```text
You are a conservative repair planner.

Do not tell stories.
Do not solve the whole case.
Do not propose more than 3 actions.
Do not skip validation.
Do not hide uncertainty.

You must produce:
- selected repair family
- scope
- 1 to 3 candidate actions
- first validation target
- main misrepair risk
- next step

If routing is weak, do not overreach.
If boundary pressure is high, narrow scope or escalate.
```

---

## 14. Recommended teaching variant

Use this when the planner output is for education, onboarding, or demo explanation.

```text
You are a teaching-oriented repair planner.

Produce the normal structured repair plan, but also briefly explain:
- why this repair family is preferred
- why a neighboring repair family is not first
- what the most likely misrepair would be

Keep the explanation short and operational.
Do not turn the output into an essay.
```

---

## 15. Example planner call

### Example input

```json
{
  "case_description": "A drafted outbound email exists, but approval and readiness checks are incomplete while downstream send is available.",
  "primary_family": "F4",
  "secondary_family": "F3",
  "why_primary_not_secondary": "The main failure lies in execution closure and premature downstream action, not continuity drift.",
  "broken_invariant": "deployment liveness closure broken",
  "best_current_fit": "F4_N03 Pre-Readiness Execution Failure",
  "fit_level": "high",
  "fix_surface_direction": "readiness audit and gate insertion",
  "confidence": "medium",
  "evidence_sufficiency": "medium",
  "ambiguous": false,
  "no_fit": false
}
```

### Example output

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
    "Then review downstream ordering if closure is still weak"
  ],
  "primary_validation_target": "readiness state",
  "misrepair_risk": "may treat an execution problem as if it were only a continuity problem",
  "recommended_next_step": "validate-first-action"
}
```

---

## 16. Failure modes this prompt should reduce

This planner prompt is specifically meant to reduce these common planner failures:

* proposing too many actions
* confusing neighboring repair families
* skipping validation targets
* hiding uncertainty under strong language
* repairing F4 cases with generic instruction pressure
* repairing F1 cases with pure container tightening
* repairing F6 cases too aggressively

The prompt should be judged by how well it prevents these mistakes.

---

## 17. Suggested evaluation questions

When reviewing planner quality, ask:

1. Did the planner keep the selected repair family aligned with the routed case
2. Did it stay within an appropriate scope
3. Did it propose no more than 3 actions
4. Did it define a real first validation target
5. Did it identify a realistic misrepair risk
6. Did it escalate properly when evidence was weak

These questions are enough for a first practical review loop.

---

## 18. What this file does not yet include

This file does **not** yet define:

* exact JSON schema constraints
* token budgeting strategy
* model-specific prompt tuning
* exemplar retrieval logic for the planner
* code-level orchestration
* adaptive retry loops

Those belong to later operational layers.

This file only defines the first prompt behavior contract.

---

## 19. Recommended next files

The most logical next files are:

* [Repair Plan Schema v1](./repair-plan-schema-v1.json)
* [Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)

That sequence makes sense because:

* this file defines planner behavior
* the schema file defines planner output structure
* the semi-auto scope file defines what actions may later be applied safely

---

## 20. Next steps ✨

After this page, most readers continue with:

1. [Open Repair Plan Schema v1](./repair-plan-schema-v1.json)
2. [Open Semi Auto Repair Scope v1](./semi-auto-repair-scope-v1.md)
3. [Open Planner Review Checklist v1](./planner-review-checklist-v1.md)
4. [Open Planner Test Note v1](./planner-test-note-v1.md)

If you want the broader product surface:

* [Back to Auto Repair v1 README](./README.md)
* [Back to Fixes Hub](../README.md)
* [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Back to Atlas Hub](../../README.md)

---

## 21. One-line prompt summary 🌍

**Repair Planner Prompt v1 defines how a routed Atlas case should be turned into a conservative, structured, validation-aware first repair plan.**
