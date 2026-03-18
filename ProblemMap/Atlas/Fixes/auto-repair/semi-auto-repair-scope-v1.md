<!--
AI_NOTE_START

Document role:
This file defines the first formal scope boundary for semi-auto repair inside the Auto Repair layer of the Atlas Fixes package.

How to use this file:
1. Read this page when deciding whether a repair action is safe enough for early constrained semi-auto use.
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

What this file is:
- The scope boundary page for early semi-auto repair
- A safety contract for deciding which actions may enter constrained semi-auto use
- A bridge between planner-only behavior and later bounded apply-and-check behavior

What this file is not:
- Not proof that broad autonomous repair is already available
- Not a permission slip for unrestricted repair execution
- Not a replacement for validation, rollback, or planner discipline
- Not the full long-term execution policy for all repair families

Reading discipline for AI:
- Treat this file as a boundary contract, not as a maturity claim about broad automation.
- Keep local scope, inspectability, reversibility, and validation-readiness visible.
- Prefer planner-only or review-bound handling when evidence is weak or family pressure is ambiguous.
- Stay especially cautious in F6-heavy, multi-family, or broad-mutation cases.

AI_NOTE_END
-->

# Semi-Auto Repair Scope v1 🛡️

## The first formal boundary for early constrained semi-auto repair

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
- [Open Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)

---

If the planner layer decides **which repair move is plausible**, this scope document decides **which kinds of repair moves are safe enough to enter early semi-auto use**. 🧭

Its purpose is to answer one practical question:

> which repair actions are safe enough to be partially automated in early phases,  
> and which repair actions should remain planner-only, review-bound, or explicitly delayed?

This document does **not** claim that broad autonomous repair is already available.

It defines something narrower and safer:

> the first controlled scope for limited, auditable, reversible semi-auto repair

---

## Quick start 🚀

### I want the shortest scope reading

Use this path:

1. check whether the case is already routed
2. check whether the action is local, inspectable, reversible, and validation-ready
3. check whether the action belongs to an allowed early category
4. check whether any stop condition is present
5. only then allow semi-auto apply-and-check behavior

### I want the stronger system reading

Use this page together with:

1. [Repair Planner Spec v1](./repair-planner-spec-v1.md)
2. [Repair Validation Loop v1](./repair-validation-loop-v1.md)
3. [Rollback Policy v1](./rollback-policy-v1.md)
4. [Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)

Short version:

> route first  
> keep the action small  
> make validation explicit  
> keep rollback possible  
> stop early when boundary risk is high

---

## 1. What semi-auto repair means here

Semi-auto repair does **not** mean unrestricted self-directed repair.

It means:

> the system may generate, apply, or suggest a narrowly bounded repair action  
> when the action is local, inspectable, reversible, and validation-ready

This is an intentionally limited concept.

The system is allowed to help with a repair action only when:

- the case has already been routed
- the repair family is clear enough
- the action is small enough to validate
- the rollback path is explicit
- the risk is low enough for controlled trial

So semi-auto repair sits between:

- repair planning only

and

- fully autonomous repair execution

It is a middle layer.

---

## 2. Why this scope document is needed

Without a scope boundary, Auto Repair would drift too quickly into unsafe territory.

Some repair actions are naturally suited to early semi-auto use.

Others are not.

For example:

- replacing an evidence subset may be reasonable
- inserting a readiness gate suggestion may be reasonable
- tightening a broken output schema may be reasonable

But:

- making high-impact boundary interventions
- mutating broad workflow logic under uncertainty
- applying strong legitimacy or policy changes
- performing deep repair on ambiguous multi-family cases

should not be treated as early semi-auto operations.

So this document exists to keep growth disciplined.

---

## 3. Core scope principle

The scope rule is simple:

> only actions that are local, inspectable, reversible, and validation-ready  
> may enter early semi-auto repair

If an action fails one or more of those tests, it should remain:

- planner-only
- review-bound
- escalation-only
- or future-stage work

This is the main protective rule for v1.

---

## 4. Scope quick map 🗂️

| Tier or region | Early reading |
|---|---|
| Tier 1 suggest-only | safest starting point |
| Tier 2 controlled apply-and-check | main early semi-auto target |
| Tier 3 bounded iterative repair | possible later, do not rush |
| F1 / F4 / F7 | best early family targets |
| F5 | limited and caution-heavy |
| F3 | possible but more subtle |
| F6-heavy cases | planner-only or review-bound |

This page is the right place when the question is **what may safely enter constrained semi-auto use now**, not whether the whole repair stack is ready for broad automation.

---

## 5. Semi-auto repair tiers

Semi-auto repair should be understood in three operational tiers.

### Tier 1 · Suggest-only

The system proposes a repair action, but does not apply it automatically.

This is the safest tier.

Typical use:

- high-risk family pressure
- ambiguous cases
- human-in-the-loop workflows
- early repair demos

### Tier 2 · Controlled apply-and-check

The system applies a small local action in a tightly bounded context and immediately checks the result.

This is the main target tier for early semi-auto repair.

Typical use:

- swap evidence set
- add a readiness gate in a toy workflow
- tighten a schema in a replayable output shell

### Tier 3 · Bounded iterative repair

The system may try a small action, validate, and either keep, revise, or rollback under strict local limits.

This tier is possible later, but should not be rushed.

It requires stronger validation and rollback discipline.

---

## 6. What qualifies as in-scope for v1

A repair action is in scope for early semi-auto use when all of the following are true.

### Condition 1 · Routed case exists

The case must already have:

- primary family
- broken invariant
- best current fit
- fix surface direction
- usable confidence and evidence status

No semi-auto repair should happen on an unrouted or weakly defined case.

### Condition 2 · Action is local

The action must target a narrow region.

Examples:

- evidence set
- output schema
- readiness gate
- trace insertion point
- descriptor shell

The action must not require broad undefined system mutation.

### Condition 3 · Action is inspectable

The before and after difference must be understandable.

If nobody can tell what changed, the action is too loose for early semi-auto use.

### Condition 4 · Action is reversible

A restore point or rollback path must be available.

If the system cannot explain how to back out, the action is not ready.

### Condition 5 · Validation target is explicit

The planner must be able to name the first validation target.

Examples:

- anchor alignment
- readiness state
- schema validity
- trace usefulness

If the validation target is vague, the action is too immature.

---

## 7. Best early family targets

Not all families are equally suitable for early semi-auto work.

### F1 · Grounding and Evidence Integrity

This is one of the best early targets.

Why:

- actions are often concrete
- validation is easier
- rollback is usually manageable
- local scope is often clear

Good early examples:

- replace wrong evidence subset with a corrected evidence subset
- filter semantically adjacent but misleading anchors
- force re-check against a declared source target
- narrow retrieval candidates for a replayable case

Good early validation targets:

- anchor alignment
- source match
- semantic target fit

Good early rollback targets:

- restore previous evidence selection
- restore previous candidate set

### F4 · Execution and Contract Integrity

This is also a strong early target.

Why:

- workflow errors are often structurally visible
- gates and ordering logic can often be stated clearly
- before and after comparison is practical

Good early examples:

- insert a readiness gate in a toy workflow
- block downstream execution until upstream state is satisfied
- reorder a local workflow step in a replayable demonstration
- harden a closure rule in a constrained example

Good early validation targets:

- readiness state
- gate behavior
- ordering correctness
- closure path stability

Good early rollback targets:

- remove inserted gate
- restore previous ordering rule

### F7 · Representation and Localization Integrity

This is another excellent early target.

Why:

- structure is visible
- repairs are often local
- many actions are schema-like and easy to inspect
- replay demos work very well here

Good early examples:

- tighten JSON schema
- correct field shell shape
- restore array or object boundary
- strengthen formal descriptor wording

Good early validation targets:

- schema validity
- shell integrity
- descriptor fidelity

Good early rollback targets:

- restore prior schema
- remove tightened descriptor
- revert shell correction

---

## 8. Medium-scope families

Some families can support semi-auto work, but only carefully.

### F5 · Observability and Diagnosability Integrity

Possible early actions:

- suggest trace insertion
- add logging layer in replayable or synthetic workflows
- expose candidate path visibility
- add coherence probe markers

Why medium-risk:

- better visibility is useful
- but visibility improvement is not the same as true repair
- noise can increase quickly
- over-instrumentation can reduce clarity

Good use mode:

- suggest-only
- limited apply-and-check in small replay settings

Bad use mode:

- broad instrumentation without a narrow probe target

### F3 · State and Continuity Integrity

Possible early actions:

- continuity scaffold suggestion
- ownership trace suggestion
- role fence suggestion
- local persistence marker proposal

Why medium-risk:

- continuity problems often look simple but become complex quickly
- state and ownership can drift in subtle ways
- rollback may be harder than it first appears

Good use mode:

- planner-heavy
- toy examples
- constrained replay use

Bad use mode:

- aggressive live mutation of broad state behavior

---

## 9. Out of scope for early semi-auto use

The following areas should remain out of scope for v1 semi-auto execution.

### F6-heavy intervention

Boundary and safety cases should not become early semi-auto execution targets.

Why:

- the risk of wrong intervention is high
- the evidence is often incomplete
- planner-only or review-bound handling is safer
- the cost of false confidence is too high

Allowed early use:

- planner-only
- stabilization suggestion
- review recommendation
- escalation marker

Not allowed early use:

- aggressive automatic intervention
- strong policy-like changes
- legitimacy or incentive restructuring
- unsafe autonomous boundary action

### Multi-family ambiguity under weak evidence

If the case is sitting in strong ambiguity, semi-auto execution should not proceed.

Examples:

- F1 and F7 ambiguity under synthetic structure pressure
- F3 and F4 ambiguity under workflow-memory interaction
- F5 and F6 ambiguity under abstract governance pressure

In such cases, the correct move is:

- revise routing
- reduce scope
- escalate
- stop and wait

### Broad system mutation

Actions that touch too much system surface at once are out of scope.

Examples:

- broad prompt system rewrites
- large multi-step repair sequences
- cross-module mutation without a local restore point
- unrestricted configuration rewrites

These are too large for early semi-auto discipline.

---

## 10. Allowed early action categories

The following action categories are good early semi-auto candidates.

### Category A · Evidence-local actions

Examples:

- re-ground evidence set
- filter anchors
- restore correct evidence source
- narrow candidate evidence range

### Category B · Gate-local actions

Examples:

- insert readiness gate
- block downstream step until upstream ready
- enforce minimal closure rule
- restore local ordering check

### Category C · Schema-local actions

Examples:

- tighten schema shell
- restore missing object boundary
- correct descriptor format
- constrain a field structure

### Category D · Probe-local actions

Examples:

- add a local trace probe
- expose one hidden workflow stage
- add one candidate trace line
- insert one visibility checkpoint

This category should remain more cautious than A, B, and C.

---

## 11. Disallowed early action categories

The following should remain outside early semi-auto scope.

### Category X · Full workflow redesign

Too broad.

### Category Y · High-abstraction policy intervention

Too risky.

### Category Z · Multi-step repair chains without checkpoints

Too hard to validate and rollback.

### Category W · Boundary-heavy autonomous intervention

Too dangerous for early phases.

---

## 12. Required safety checks before semi-auto apply

Before any in-scope action is applied, the system should confirm:

1. the case has a valid routed basis
2. the selected repair family is not weakly guessed
3. the action is in an allowed category
4. the plan scope is compatible with semi-auto use
5. the first validation target is explicit
6. the rollback target is explicit
7. no major stop condition is present

If these checks fail, the system should not auto-apply.

It should revert to:

- planner-only
- review-bound
- escalation
- or stop-and-wait

---

## 13. Required stop conditions

Semi-auto repair should stop immediately when:

- `no_fit = true`
- family confidence is too weak
- evidence sufficiency is too weak
- the restore point is unclear
- the first validation target is unclear
- the action would enter F6-heavy intervention space
- the action would affect multiple major layers at once
- the planner cannot distinguish between local gain and likely collateral damage

These conditions are not edge cases.

They are core protections.

---

## 14. Example in-scope actions

### Example A · F1 local semi-auto action

Case:  
retrieval anchor drift in a replayable benchmark case

Action:  
replace evidence subset with a better-aligned subset

Why in scope:

- local
- easy to compare
- rollback possible
- validation target is explicit

Recommended tier:

- Tier 2

### Example B · F4 local semi-auto action

Case:  
downstream send step executes before upstream readiness is complete

Action:  
insert a local readiness gate in the replay workflow

Why in scope:

- narrow workflow change
- visible before and after
- rollback is clear
- validation target is explicit

Recommended tier:

- Tier 2

### Example C · F7 local semi-auto action

Case:  
output content is partially correct but the JSON shell is invalid

Action:  
tighten schema shell and restore object boundary

Why in scope:

- strongly local
- highly inspectable
- validation is straightforward
- rollback is simple

Recommended tier:

- Tier 2

---

## 15. Example out-of-scope actions

### Example A · F6 boundary intervention

Case:  
high-pressure alignment and legitimacy ambiguity

Action:  
apply a strong autonomous stabilization rule

Why out of scope:

- high-risk boundary region
- low tolerance for false confidence
- review and escalation are safer

### Example B · broad workflow rewrite

Case:  
multi-step workflow occasionally fails under mixed memory and closure pressure

Action:  
rewrite the whole workflow plan automatically

Why out of scope:

- too broad
- too hard to validate locally
- rollback would be unstable

### Example C · abstract coherence intervention

Case:  
value, knowledge, or probability coherence case under F5 and F6 boundary pressure

Action:  
apply a strong abstract corrective rewrite

Why out of scope:

- high abstraction
- hard to validate locally
- planner-only or escalation is safer

---

## 16. Semi-auto success condition

Early semi-auto repair should be considered successful only when:

- the action stays in scope
- the local target improves
- collateral damage is absent or clearly acceptable
- rollback remains available
- the action does not silently widen into a larger mutation

This is the right early success standard.

Not:

- impressive-looking output
- aggressive intervention
- speculative repair story
- broad but untestable change

---

## 17. Relationship to future phases

This scope document is mainly for the transition between:

- Stage 1 · Repair planner  
  and
- Stage 2 · Constrained semi-auto repair

It should remain conservative until:

- validation examples become stronger
- rollback discipline is more battle-tested
- action libraries become cleaner
- family-specific patterns are better understood

So this document is not the end state.

It is the safe doorway into the next phase.

---

## 18. Recommended immediate next step

Once this file exists, the next useful step is likely one of these:

- create a small action catalog for F1, F4, and F7
- create one minimal semi-auto demo spec
- create one validator example pack for semi-auto cases

The best immediate move is probably:

> start with a tiny catalog of safe early actions

That would make the semi-auto layer much more concrete.

---

## 19. Next steps ✨

After this page, most readers continue with:

1. [Open Safe Early Action Catalog v1](./safe-early-action-catalog-v1.md)
2. [Open Repair Validation Loop v1](./repair-validation-loop-v1.md)
3. [Open Rollback Policy v1](./rollback-policy-v1.md)
4. [Open Auto Repair Roadmap v1](./auto-repair-roadmap-v1.md)

If you want the broader product surface:

- [Back to Auto Repair v1 README](./README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

---

## 20. One-line scope summary 🌍

**Semi-Auto Repair Scope v1 defines which Atlas-based repair actions are safe enough for early constrained semi-auto use, and which actions must remain planner-only, review-bound, or delayed.**
