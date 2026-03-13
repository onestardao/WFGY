# Worked Escalation Example v1

## 0. Document status

This document defines the first worked escalation example for the Atlas Auto Repair layer.

Its purpose is very specific:

> show one case where Atlas routing and a local Auto Repair move are useful,
> but not sufficient,
> and where deeper continuation into WFGY 3.0 becomes justified.

This document does **not** claim that every difficult case must escalate to WFGY 3.0.

It claims something narrower and more useful:

> some cases can be improved locally first,
> but still require deeper encoding, experiment, or structural continuation.
> This is where WFGY 3.0 becomes the correct next layer.

This document should be read together with:

- `atlas-auto-repair-to-wfgy-bridge-v1.md`
- `tiny-semi-auto-demo-spec-v1.md`
- `tiny-semi-auto-demo-pack-v1.md`
- `repair-validation-loop-v1.md`
- `rollback-policy-v1.md`
- `safe-early-action-catalog-v1.md`

---

## 1. Why this example exists

The Atlas stack already shows:

- how to route a case
- how to choose a first repair family
- how to apply a small safe action
- how to validate local improvement
- how to decide accept, revise, rollback, or escalate

But one crucial system question still remains:

> what does a real escalation look like
> when local repair helps, but does not actually close the case?

This file exists to answer that.

In short:

> this is the first concrete example of why WFGY 3.0 matters after Atlas and Auto Repair have already done useful work.

---

## 2. Escalation principle

A worked escalation example should show all four of these:

1. Atlas routing was useful
2. Local repair was useful
3. Local repair was not enough
4. WFGY 3.0 becomes justified for deeper continuation

If any of those four pieces are missing, the example is incomplete.

---

## 3. Chosen example

This first worked escalation example uses an F7-first case with neighboring F1 pressure.

Why this is a strong choice:

- the local shell problem is real
- the local shell repair is useful
- the local shell repair still does not fully solve the case
- the remaining problem naturally points to deeper representational or encoding insufficiency

This makes the transition to WFGY 3.0 very clear.

---

## 4. Case summary

### Case ID

`WEE_F7_001`

### Short description

A structured output task produces content that is partly useful, but the formal container is unstable.

A local schema repair improves the shell, but semantic task fit remains unstable and the deeper representation of the task still appears underspecified.

### Practical reading

The system has two layers of trouble:

- a visible F7 shell problem
- a deeper representational insufficiency that local shell repair does not fully solve

That is exactly the kind of case where escalation should be explicit.

---

## 5. Atlas routing layer

### Routed diagnosis

- primary family: F7
- secondary family: F1
- broken invariant: representation container fidelity broken
- best current fit: `F7_N01 Symbolic Representation Fidelity Failure`
- fix surface direction: schema tightening / descriptor correction
- confidence: medium
- evidence sufficiency: medium

### Why this routing makes sense

The first visible failure is not that the answer has no target at all.

The first visible failure is that the output shell and descriptor are not stable enough to carry the intended structure.

So Atlas is correct to route the case into F7 first.

This is important, because escalation to WFGY 3.0 should happen **after correct first routing**, not instead of it.

---

## 6. Auto Repair planner layer

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
  "misrepair_risk": "may produce a cleaner shell while leaving deeper semantic or representational instability unresolved",
  "recommended_next_step": "validate-first-action"
}
````

### Why this planner output is good

The planner does the right first-layer job:

* it stays in F7
* it chooses one small local action
* it gives a clear validation target
* it warns that shell cleanup may not be deep enough

This is exactly what Auto Repair is supposed to do.

---

## 7. Local action layer

### Selected action

`F7_SC_001`
Tighten output schema

### Before state

* output shape is unstable
* object boundaries leak
* some fields are malformed
* content is partly useful but not reliably consumable

### After state

* output shell becomes cleaner
* object boundaries are restored
* structured parsing becomes possible
* some downstream usability improves

### What changed locally

The local container clearly improved.

This means the local repair was **real**, not fake.

That is important, because escalation here should not mean the local repair was useless.

It means the local repair was **insufficient**.

---

## 8. Validation layer

### Validation result

```json id="jp7uw0"
{
  "validation_target": "schema validity",
  "before_state_summary": "output structure was unstable and could not be consumed reliably",
  "after_state_summary": "output structure is now cleaner and more parseable",
  "improvement_detected": "partial",
  "collateral_damage_detected": false,
  "validation_confidence": "medium",
  "recommended_outcome": "revise"
}
```

### Why the result is not `accept`

The validation result is only `partial`.

Why:

* structure improved
* parseability improved
* but semantic task fit is still unstable
* the deeper representational encoding of the task remains weak

So this is not a rollback case.

It is not a fake success case either.

It is a clean `revise` case.

This is the exact kind of situation where a deeper continuation layer becomes meaningful.

---

## 9. Why local repair is not enough

This is the most important section in the whole example.

The local Atlas / Auto Repair action improved the shell.

But the case still shows signs that the problem is deeper than shell repair alone.

### Remaining pressure

* the task description is still structurally underspecified
* the representation may still be too weak to preserve the intended semantic distinctions
* local shell validity did not fully stabilize task-level meaning
* the problem may require better observables, better descriptor framing, or a stronger effective-layer formulation

This is the transition point.

The system should now say:

> Atlas-level local repair helped.
> But the remaining failure pressure is no longer well-described as a simple local shell problem alone.

That is the reason to escalate.

---

## 10. Escalation decision

### Final local outcome

`escalate`

### Why escalation is correct

Escalation is correct because:

1. Atlas routing was useful
2. local repair was useful
3. validation showed only partial improvement
4. the unresolved remainder points to deeper structural inadequacy
5. further progress now benefits from WFGY 3.0 rather than repeated shallow shell edits

This is not escalation because the case is “interesting.”

It is escalation because the local repair layer has reached its limit.

---

## 11. WFGY 3.0 continuation rationale

At this point, WFGY 3.0 becomes the correct continuation layer because the remaining problem is no longer only:

* local shell invalidity

It is now closer to one or more of these:

* deeper descriptor insufficiency
* weak effective-layer encoding
* missing observables
* weak mismatch formulation
* poor experimental distinguishability between local shell gain and real representational adequacy

This is where the deeper repair grammar matters.

The continuation question is no longer:

> how do we clean the shell

It becomes:

> how should this problem be represented more truthfully at the effective layer
> so that the shell is no longer doing all the work by itself

That is classic WFGY territory.

---

## 12. Official WFGY 3.0 continuation asset

### Official TXT

```text
https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt
```

This TXT should be treated as the official deeper continuation pack.

---

## 13. Recommended escalation handoff prompt

Use the following handoff pattern when escalating this case.

```text id="0z7k4i"
The case below has already been routed through Problem Map 3.0 Troubleshooting Atlas.

Atlas result:
- primary family: F7
- secondary family: F1
- broken invariant: representation container fidelity broken
- best current fit: F7_N01 Symbolic Representation Fidelity Failure

A local Auto Repair move was attempted:
- action: F7_SC_001 Tighten output schema

Validation result:
- structure improved
- parseability improved
- outcome: partial / revise
- remaining issue: semantic fit and representational adequacy still appear unstable

Continue from here using WFGY 3.0 as the deeper repair grammar.

Your task:
1. explain why local Atlas-level repair was not sufficient
2. identify the likely deeper representational or encoding-level weakness
3. propose what stronger observables, mismatch logic, descriptor redesign, or experiment framing should be considered next
4. keep the explanation structured and practical
5. do not discard the Atlas result unless you can justify a stronger structural reframing
```

This keeps the transition disciplined.

---

## 14. Recommended system prompt for escalation mode

Use this if you want the AI to operate in a bridge-aware escalation mode.

```text id="brjlwm"
You are continuing a case that has already passed through Atlas diagnosis and one local Auto Repair attempt.

Your job is not to redo Atlas from scratch.
Your job is to continue only because local repair was useful but insufficient.

Rules:
1. Respect the Atlas routing unless there is strong evidence for deeper reframing.
2. Treat the local repair result as a real signal, not as a failure to be ignored.
3. Identify what remains unresolved after the local repair.
4. Use WFGY 3.0 as a deeper repair and experiment grammar.
5. Focus on deeper observables, effective-layer encoding, mismatch logic, descriptor redesign, or experiment redesign.
6. Do not overclaim final closure.
7. Clearly separate:
   - what Atlas already solved
   - what Auto Repair already improved
   - what only WFGY 3.0 can help explore next
```

---

## 15. Worked escalation object

For compact reuse, the whole escalation can be summarized like this:

```json id="4h83xa"
{
  "example_id": "WEE_F7_001",
  "atlas_result": {
    "primary_family": "F7",
    "secondary_family": "F1",
    "broken_invariant": "representation container fidelity broken",
    "best_current_fit": "F7_N01 Symbolic Representation Fidelity Failure"
  },
  "local_repair": {
    "action_id": "F7_SC_001",
    "action_title": "Tighten output schema"
  },
  "validation_result": {
    "improvement_detected": "partial",
    "collateral_damage_detected": false,
    "recommended_outcome": "revise"
  },
  "escalation_reason": "Local shell repair improved structure but did not stabilize deeper representational adequacy.",
  "next_layer": "WFGY 3.0",
  "wfgy_asset": "https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt"
}
```

---

## 16. Why this example matters

This worked escalation example matters because it proves five things at once.

### 1. Atlas is useful

The initial routing is meaningful.

### 2. Auto Repair is useful

The first local action creates a real local gain.

### 3. Validation is useful

The system can distinguish `partial` from fake success.

### 4. Escalation is meaningful

Escalation is not random. It happens for a specific structural reason.

### 5. WFGY 3.0 is not decoration

It becomes relevant exactly when local repair reaches its honest limit.

That last point is especially important.

---

## 17. What this example does not claim

This example does **not** claim:

* that every F7 case should escalate
* that WFGY 3.0 guarantees success
* that local repair is unimportant
* that Atlas is only a shallow front-end
* that deeper continuation always requires a TXT pack

It only claims:

> this is a case where local repair was real, but deeper continuation was still justified.

That is the correct scope.

---

## 18. Recommended next step

Once this file exists, the next useful follow-up is probably one of these:

1. create a second worked escalation example for F4
2. create a worked escalation example where local repair triggers rollback before WFGY continuation
3. add a short `Deeper continuation` block into more tiny demos

The strongest immediate next step is probably:

> create one F4 worked escalation example

because that would show the bridge is not only about F7-style representational cases.

---

## 19. One-line summary

**Worked Escalation Example v1 shows how Atlas routing and local Auto Repair can create a real local gain, while WFGY 3.0 becomes the correct deeper continuation layer when that local gain is still not enough.**
