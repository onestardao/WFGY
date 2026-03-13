# Atlas Auto Repair to WFGY Bridge v1

## 0. Document status

This document defines the first formal bridge between:

- the Atlas / Auto Repair layer
- and the deeper WFGY 3.0 repair layer

Its purpose is to make one relationship explicit:

> Atlas and Auto Repair are not meant to replace WFGY 3.0.  
> They are meant to route, stabilize, and prepare cases before deeper WFGY 3.0 repair logic is invoked.

This document does **not** claim that every Atlas case must escalate into WFGY 3.0.

It claims something narrower and more useful:

> Atlas handles diagnosis and first controlled repair movement.  
> WFGY 3.0 provides the deeper repair grammar when the case needs more than a local fix.

---

## 1. Why this bridge document exists

The current Atlas stack already has:

- Atlas routing
- casebook guidance
- AI adapter logic
- fix surface
- auto-repair planner
- validation logic
- rollback logic
- semi-auto scope discipline

That stack is already useful on its own.

But there is an important architectural question:

> when does the workflow stop at Atlas / Auto Repair,
> and when should it continue into deeper WFGY 3.0 reasoning?

This document exists to answer that clearly.

Without this bridge, users may misread the system in one of two wrong ways:

### Wrong reading A
Atlas alone is already the full deep repair engine.

### Wrong reading B
WFGY 3.0 is unrelated to Atlas and belongs to a separate universe.

Both readings are wrong.

The correct reading is:

> Atlas and Auto Repair handle diagnosis and first controlled repair movement.  
> WFGY 3.0 handles deeper encoding redesign, experiment logic, and harder second-stage repair.

---

## 2. High-level role split

The cleanest role split is this:

### Atlas
The Atlas is the **troubleshooting grammar**.

It answers:

- what kind of failure is this
- which family is primary
- which neighboring region is easy to confuse
- what first repair direction should be tried

### Auto Repair
Auto Repair is the **first controlled repair layer**.

It answers:

- what first repair move is most plausible
- how to validate that move
- when to revise, rollback, or escalate
- which small repair actions are safe enough to try first

### WFGY 3.0
WFGY 3.0 is the **deeper repair and experiment grammar**.

It answers questions like:

- does the current encoding itself need redesign
- what observables, mismatch functionals, or experiment templates should be used
- how should the problem be re-expressed at the effective layer
- how should cross-domain structure be compared or reused
- what deeper AI / engineering modules might be relevant

This means the stack should be read as:

```text
Atlas
→ Auto Repair
→ WFGY 3.0
````

not as three unrelated objects.

---

## 3. Why WFGY 3.0 belongs after Auto Repair

WFGY 3.0 is best treated as the deeper layer because it is not only a list of topics.

It is a structured TXT pack built for AI-assisted use and includes:

* a 131-problem structured index
* GO rules for progressive analysis
* explicit cross-domain structural observation logic
* authenticity and SHA256 verification flow
* effective-layer encodings with observables, mismatch functionals, tension functionals, singular sets, and experiment templates
* AI and engineering module suggestions inside problem pages

That combination makes it much stronger as a deep repair and experimentation substrate than as a simple first-pass fix sheet.

So the intended stack is:

* Atlas for diagnosis
* Auto Repair for first controlled move
* WFGY 3.0 for deeper encoding-level or experiment-level continuation

---

## 4. The bridge principle

The bridge principle is simple:

> if a local repair move is enough, stay in Atlas / Auto Repair.
> if the case needs encoding redesign, deeper observables, harder experiment logic, or broader structural reframing, escalate to WFGY 3.0.

This principle prevents two mistakes:

### Mistake 1

Sending every case into deeper theory too early

### Mistake 2

Pretending a local repair move is enough for cases that clearly need deeper reframing

The bridge exists to decide when to cross that line.

---

## 5. What Atlas should solve before escalation

Atlas and Auto Repair should normally solve these first:

* primary family routing
* broken invariant naming
* neighbor-family separation
* first repair family selection
* first validation target
* rollback and escalation discipline

If those are still unclear, escalation into WFGY 3.0 is often premature.

That is why the stack should usually remain:

```text
route first
repair second
deeper grammar third
```

---

## 6. What kinds of cases should escalate to WFGY 3.0

The following are strong reasons to continue into WFGY 3.0.

### A. Encoding-level insufficiency

The current Atlas-level repair is too shallow because the problem needs a deeper effective-layer re-expression.

Examples:

* the current representation of the state space is too weak
* the observable set is underspecified
* the current mismatch language is too blunt
* the current repair action changes symptoms but not encoding structure

### B. Experiment-design need

The case cannot be meaningfully advanced without a stronger experiment template or falsifiable test structure.

Examples:

* the problem needs a better measurement design
* the relevant observables need to be made explicit
* the problem needs counterfactual world comparison
* the current repair path cannot distinguish local gain from structural illusion

### C. Cross-domain structural reuse

The case may benefit from modules or framing patterns already present in other WFGY 3.0 problem pages.

Examples:

* a coordination problem resembles a scientific control problem
* an AI alignment case resembles a broader system-boundary problem
* a representation issue resembles another domain’s descriptor problem

### D. Repeated failure after local repair

The planner, validation, and rollback loop repeatedly fail to stabilize the case using local safe actions.

In that situation, deeper grammar becomes a rational next step.

---

## 7. What kinds of cases should usually stay in Atlas / Auto Repair first

Not every case needs WFGY 3.0 immediately.

The following cases usually should stay local first:

### F1 local grounding cases

If a simple re-grounding or anchor correction is likely enough, stay local first.

### F4 local closure cases

If a readiness gate or ordering correction is enough, stay local first.

### F7 local container cases

If schema tightening or shell repair is enough, stay local first.

### Small F5 visibility repairs

If a narrow probe or trace exposure is clearly the first move, stay local first.

The bridge should not be used as an excuse to overcomplicate simple cases.

---

## 8. Operational bridge workflow

The intended workflow is:

```text
case
→ Atlas routing
→ Auto Repair plan
→ local action + validation
→ if local repair is enough: stop
→ if local repair is insufficient: escalate to WFGY 3.0
```

This escalation should be explicit, not hidden.

A good system should be able to say:

* local fix was enough
  or
* local fix was not enough; deeper WFGY 3.0 continuation is recommended

That explicitness is part of the design.

---

## 9. What WFGY 3.0 continuation should look like

WFGY 3.0 continuation should not be treated as “more vague philosophy.”

A good continuation should typically do one or more of the following:

* redefine the problem at a better effective layer
* identify missing observables
* define a sharper mismatch functional
* propose a stronger experiment template
* compare the case to other structurally similar domains
* recommend deeper AI or engineering modules
* clarify what is local failure versus encoding failure

This is why WFGY 3.0 should be introduced as a deeper continuation path.

---

## 10. Official TXT pack

The official TXT continuation pack should be referenced directly.

### Official raw TXT link

```text
https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt
```

This is the simplest way to hand the deeper layer to another AI system.

The shortest operational instruction is:

1. load the Atlas case and current repair state
2. if local repair is insufficient, give the WFGY 3.0 TXT to the model
3. ask the model to continue from the deeper repair / encoding / experiment layer

---

## 11. Recommended user-facing usage

A very simple way to explain usage is:

### Atlas-first workflow

Use the Atlas when you want:

* fast routing
* family diagnosis
* first repair direction
* small, local, safe repair movement

### WFGY 3.0 continuation

Use WFGY 3.0 when you want:

* deeper reframing
* better effective-layer encoding
* experiment logic
* cross-domain structural comparison
* stronger AI / engineering continuation

That means the official practical message can be:

> Start with Atlas.
> Escalate to WFGY 3.0 only when the case needs deeper structural repair.

---

## 12. Recommended AI instruction pattern

A minimal user instruction pattern could be:

```text
Use the Atlas result below as the first-layer diagnosis.
If the local repair remains insufficient, continue using the attached WFGY 3.0 TXT as the deeper repair grammar.
Preserve the routed family unless you can justify a stronger structural reframing.
Explain:
1. whether the local fix is enough,
2. whether escalation to WFGY 3.0 is necessary,
3. which deeper observables, experiments, or encoding changes should be considered next.
```

This keeps the relationship clean and understandable.

---

## 13. Recommended system prompt

Use this as a first bridge-oriented system prompt for AI assistants.

```text
You are operating in a two-layer repair workflow for Problem Map 3.0 Troubleshooting Atlas.

Layer 1:
Use Atlas and Auto Repair logic for:
- routing
- broken invariant identification
- first repair planning
- validation and rollback discipline

Layer 2:
Use WFGY 3.0 only when the case clearly needs deeper repair than a local Atlas action can provide.

Your rules:
1. Do not skip Atlas routing.
2. Do not escalate to WFGY 3.0 just because the case is intellectually interesting.
3. Escalate only when local repair is insufficient, unstable, or structurally shallow.
4. When escalating, clearly explain why Atlas-first repair was not enough.
5. Treat WFGY 3.0 as a deeper repair and experiment grammar, not as a replacement for Atlas.
6. If a local repair is enough, say so and stop.
7. If deeper continuation is needed, identify the most relevant next layer:
   - better observables
   - better mismatch functionals
   - experiment redesign
   - cross-domain structural analogy
   - deeper engineering module suggestion

Return concise, structured reasoning.
Do not overclaim closure.
```

---

## 14. Recommended public wording

A safe and strong public sentence is:

> Atlas is the troubleshooting grammar.
> Auto Repair is the first controlled repair layer.
> WFGY 3.0 is the deeper repair and experiment grammar when a case needs more than a local fix.

That sentence is short, strong, and consistent with the architecture.

---

## 15. What this bridge does not claim

This bridge document does **not** claim:

* every Atlas case should escalate to WFGY 3.0
* WFGY 3.0 automatically solves all deeper cases
* local repair is unimportant
* Atlas is only a shallow front-end
* the entire stack is already fully automated

It only claims:

> the relationship between Atlas, Auto Repair, and WFGY 3.0 is now explicit and architecturally coherent.

---

## 16. Recommended next step

Once this bridge file exists, the next useful follow-up is one of these:

1. add a short “Deeper continuation” block to tiny semi-auto demos
2. add a short WFGY escalation note to Fixes README
3. add one small worked example showing:
   Atlas → local repair attempt → escalation into WFGY 3.0

The strongest immediate next step is probably:

> add a short deeper-continuation block into the next auto-repair demo pack.

---

## 17. One-line summary

**Atlas Auto Repair to WFGY Bridge v1 defines how Atlas diagnosis and first controlled repair connect to WFGY 3.0 as the deeper repair and experiment grammar.**
