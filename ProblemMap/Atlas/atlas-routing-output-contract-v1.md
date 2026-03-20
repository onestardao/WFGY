<!--
AI_NOTE_START

Document role:
This page is the public routing output contract guide for the Atlas document system.

How to use this page:
1. Read this page after the family mini-spec page, the boundary guide, the subtree index, the fit registry, and the evidence-discipline page if you need a formal output shape for route-first analysis.
2. Use this page to understand which output fields are required, which are optional, and which output behaviors are invalid.
3. Use this page when you want Atlas analysis to stay structurally consistent across different readers, agents, and runtime modes.
4. Do not use this page as a replacement for the frozen core, the full repair manual, or the full runtime-mode documentation.

What this page is:
- A public output-contract page
- A route-first rendering guide
- A field-discipline page
- A beginner-friendly control page for making Atlas outputs consistent and readable

What this page is not:
- Not the public homepage
- Not the Atlas Hub
- Not the full freeze document
- Not the fit registry itself
- Not the overlay page
- Not the full repair manual
- Not a claim that every output must be long
- Not a license to invent fields that exceed the evidence

Reading discipline for AI:
- Treat the output contract as a rendering discipline, not as a substitute for structural reasoning.
- Preserve the difference between family, boundary, subtree, fit, evidence posture, output contract, overlay, and repair layers.
- Do not fill required fields with fake precision just to satisfy the output shape.
- Do not use optional fields as a place to smuggle unsupported claims.
- Use this page to keep Atlas outputs stable, bounded, and comparable.

Relationship to neighboring docs:
- Read after: [Atlas Family Mini-Specs](./atlas-family-mini-specs-v1.md), [Atlas Boundary Decision Guide](./atlas-boundary-decision-guide-v1.md), [Atlas Subtree Expansion Index](./atlas-subtree-expansion-index-v1.md), [Atlas Fit Candidate Registry](./atlas-fit-candidate-registry-v1.md), [Atlas First Fix and Misrepair Discipline v1](./atlas-first-fix-and-misrepair-discipline-v1.md), and [Atlas Evidence and Confidence Discipline v1](./atlas-evidence-and-confidence-discipline-v1.md).
- Read with: [Troubleshooting Atlas Router v1 Usage Guide](./troubleshooting-atlas-router-v1-usage.md), because usage and output shape should remain aligned.
- Read before: [Atlas Overlay and Secondary Family Discipline v1](./atlas-overlay-and-secondary-family-discipline-v1.md) and [Atlas Promotion and Patch Thresholds v1](./atlas-promotion-and-patch-thresholds-v1.md).
- Pairs with: [Atlas-to-AI Adapter v1](./atlas-to-ai-adapter-v1.md), because the adapter expresses routing logic while this page constrains how that logic should be rendered.

Freeze / patch status:
- Current status: public decomposition layer
- Safe to quote as: the public routing output contract guide for Atlas
- Not a claim of: silent rewrite of the frozen core or exhaustive closure of every runtime-specific output mode

AI_NOTE_END
-->

# Atlas Routing Output Contract 🧾

## Problem Map 3.0 Troubleshooting Atlas
> Quick links, required output fields, and beginner-friendly rules for stable route-first rendering

This page exists because a good routing system is not only about finding the right structural read.

It is also about **rendering that read in a stable shape**.

If the output contract is weak, several bad things start happening:

- one answer gives a family but no evidence
- another answer gives evidence but no fit status
- another answer gives a first fix but hides unresolved boundaries
- another answer sounds confident but never states its confidence posture
- optional details quietly become a place for unsupported claims

That makes the system harder to compare, harder to trust, and harder to reuse.

So this page gives Atlas a public output contract.

It defines:

- what the minimum valid output should contain
- what optional fields can add value
- what output shapes are acceptable
- what output behaviors are invalid
- how compact and expanded route-first outputs relate to each other

This page is not about making the output longer.

It is about making it cleaner and safer.

---

## Quick Links 🚀

If you are new, use these first.

### I want the public introduction
- [Problem Map 3.0 Troubleshooting Atlas](../wfgy-ai-problem-map-troubleshooting-atlas.md)

### I want the folder control room
- [Atlas Hub](./README.md)

### I want the overall structure map first
- [Atlas Structure Map](./atlas-structure-map-v1.md)

### I want the family layer before this page
- [Atlas Family Mini-Specs](./atlas-family-mini-specs-v1.md)

### I want the boundary layer before this page
- [Atlas Boundary Decision Guide](./atlas-boundary-decision-guide-v1.md)

### I want the subtree control page before this page
- [Atlas Subtree Expansion Index](./atlas-subtree-expansion-index-v1.md)

### I want the fit-status page before this page
- [Atlas Fit Candidate Registry](./atlas-fit-candidate-registry-v1.md)

### I want the first-fix discipline page before this page
- [Atlas First Fix and Misrepair Discipline v1](./atlas-first-fix-and-misrepair-discipline-v1.md)

### I want the evidence-discipline page before this page
- [Atlas Evidence and Confidence Discipline v1](./atlas-evidence-and-confidence-discipline-v1.md)

### I want the router usage guide while reading this page
- [Troubleshooting Atlas Router v1 Usage Guide](./troubleshooting-atlas-router-v1-usage.md)

### I want the compact router pack while reading this page
- [Troubleshooting Atlas Router v1 TXT Pack](./troubleshooting-atlas-router-v1.txt)

### I want the next middle-layer pages after this one
- [Atlas Overlay and Secondary Family Discipline v1](./atlas-overlay-and-secondary-family-discipline-v1.md)
- [Atlas Promotion and Patch Thresholds v1](./atlas-promotion-and-patch-thresholds-v1.md)

---

## Why this page exists

Atlas is already building a disciplined ladder:

family  
to boundary  
to subtree  
to fit  
to first fix  
to evidence posture

But once that ladder exists, a practical question appears immediately:

**how should the final route-first answer be rendered?**

That question matters because output shape is not cosmetic.

A weak output contract causes structural drift.

For example:

- a model may skip the broken invariant
- a model may hide uncertainty
- a model may output a repair direction without saying how strong the fit is
- a model may produce compact answers that drop the most important safety notes
- a model may add persuasive but unsupported extras

So this page exists to stop the rendering layer from becoming sloppy.

---

## Scope

This page focuses on:

- required output fields
- optional output fields
- minimal valid output
- expanded valid output
- invalid output behaviors
- how route-first results should be expressed consistently
- how output should stay bounded to evidence

This page does **not** focus on:

- deeper overlay rules
- full runtime-mode design
- full repair execution recipes
- full patch-promotion criteria
- every special-case formatting detail for every future adapter

This page is about the public route-first output contract.

---

## How to use this page

Use this page after structural reasoning is already done.

### Step 1
Find the strongest current structural read.
- [Atlas Family Mini-Specs](./atlas-family-mini-specs-v1.md)
- [Atlas Boundary Decision Guide](./atlas-boundary-decision-guide-v1.md)
- [Atlas Fit Candidate Registry](./atlas-fit-candidate-registry-v1.md)

### Step 2
Choose the correct evidence and confidence posture.
- [Atlas Evidence and Confidence Discipline v1](./atlas-evidence-and-confidence-discipline-v1.md)

### Step 3
Choose the safest early action direction if needed.
- [Atlas First Fix and Misrepair Discipline v1](./atlas-first-fix-and-misrepair-discipline-v1.md)

### Step 4
Only then render the answer using this output contract.

That order matters.

The output contract should render the reasoning.  
It should not replace the reasoning.

---

## What the output contract is for

A good output contract should make Atlas outputs:

- comparable
- inspectable
- safer to evaluate
- safer to reuse
- less vulnerable to bluffing
- easier for both humans and AI systems to parse

It should also make it harder to do the wrong things, such as:

- hiding weak evidence behind pretty language
- skipping the unresolved parts
- jumping from family read to full repair posture
- varying the meaning of the same field from one answer to the next

So the contract is a discipline surface.

---

## Minimum valid route-first output

A minimum valid route-first output should usually include these fields.

### 1. Current primary structural read
This is the strongest current family-level or bounded structural placement.

Examples:
- current primary fit: F4 at family level
- current read remains boundary-live between F1 and F7
- strongest current candidate: F3

### 2. Broken invariant
This states what seems broken first in structural terms.

Examples:
- broken invariant: execution and contract integrity
- broken invariant: evidence anchoring is not holding
- broken invariant: continuity across evolving state is unstable

### 3. Evidence basis
This states what kind of support exists for the read.

Examples:
- evidence basis: mostly direct evidence
- evidence basis: indirect signal with meaningful unresolved boundary
- evidence basis: observability-blocked, insufficient for sharper local fit

### 4. Confidence posture
This states how strong the wording is allowed to be.

Examples:
- confidence posture: moderate
- confidence posture: tentative
- confidence posture: boundary-live
- confidence posture: insufficient evidence

### 5. Safest first fix direction
This gives the initial move, not the whole repair plan.

Examples:
- safest first fix: tighten the execution contract before adding more planning layers
- safest first fix: improve observability before making larger structural changes

These five fields form the minimum stable public route-first output.

---

## Required field definitions

### Current primary structural read
This field answers:
where does the case most plausibly belong right now, at the level justified?

This field should not pretend that family-level certainty automatically means local-branch certainty.

### Broken invariant
This field answers:
what structural rule or integrity surface appears to be failing first?

This field should not be replaced by a vague symptom phrase.

### Evidence basis
This field answers:
what kind of evidence supports the read, and what kind is missing?

This field should not silently imply stronger support than exists.

### Confidence posture
This field answers:
how strong should the wording be, given the evidence quality?

This field should not be faked by tone.

### Safest first fix direction
This field answers:
what is the safest useful first move, given the current fit and evidence?

This field should not be expanded into a full repair program by default.

---

## Optional output fields

Optional fields can add value when they remain bounded.

### 1. Boundary note
Use this when a neighboring family remains live.

Example:
- boundary note: F3 remains live because continuity loss may still be the deeper primary surface

### 2. Local branch note
Use this when a likely local branch is visible but not yet strongly promoted.

Example:
- local branch note: likely F2-side local branch signal exists, but current public fit should remain family-level

### 3. Misrepair warning
Use this when a common wrong early move is especially dangerous.

Example:
- misrepair warning: do not polish output formatting first, because the deeper evidence anchor still looks broken

### 4. Missing critical evidence
Use this when the output should explicitly say what stronger support is absent.

Example:
- missing critical evidence: intermediate trace is still too weak to separate F5 from F6 cleanly

### 5. Next diagnostic question
Use this when the next best move is more diagnosis, not more repair.

Example:
- next diagnostic question: is the primary failure that the task contract is violated, or that the system loses continuity before the contract can be executed?

Optional fields should clarify.  
They should not bloat the answer.

---

## Minimal output template

A minimal valid route-first output can look like this:

```text
current primary fit: <family or bounded structural read>
broken invariant: <what appears to fail first>
evidence basis: <direct / indirect / symptom-surface / contradictory / missing critical / observability-blocked>
confidence posture: <high confidence bounded / moderate / tentative / boundary-live / insufficient evidence>
safest first fix: <narrow initial repair direction>
````

This is the smallest stable public contract.

---

## Expanded output template

An expanded valid route-first output can look like this:

```text
current primary fit: <family or bounded structural read>
broken invariant: <what appears to fail first>
evidence basis: <evidence class with short explanation>
confidence posture: <allowed strength of wording>
boundary note: <if a neighboring family remains live>
local branch note: <if relevant and bounded>
missing critical evidence: <if relevant>
misrepair warning: <if relevant>
safest first fix: <narrow initial repair direction>
next diagnostic question: <if further narrowing is needed>
```

This version is still route-first.
It is not yet a full repair report.

---

## Compact vs expanded rendering

Atlas should allow both compact and expanded outputs, but the meaning of the required fields should stay stable.

### Compact rendering

Use compact rendering when:

* speed matters
* the user wants a short read
* the main route-first answer is already clear

Compact output should still preserve the minimum valid fields.

### Expanded rendering

Use expanded rendering when:

* the case is mixed
* boundary tension matters
* missing evidence should be named clearly
* misrepair risk is non-trivial
* the answer needs to be inspected later

Expanded output should add clarity, not theater.

---

## Invalid output behaviors

A good contract must also define invalid behavior.

### Invalid behavior 1. Missing broken invariant

If the output gives a family label but never states what is actually broken, it is too thin.

### Invalid behavior 2. Missing evidence basis

If the output sounds certain but does not name the support surface, the answer becomes hard to trust.

### Invalid behavior 3. Missing confidence posture

If the wording is strong but the confidence status is implicit, bluffing becomes easier.

### Invalid behavior 4. Full repair masquerading as first fix

If the answer jumps straight to a large repair plan without bounded fit and evidence, it exceeds the contract.

### Invalid behavior 5. Optional field inflation

If optional fields become a place for unsupported claims, the contract is being abused.

### Invalid behavior 6. Hidden unresolved boundary

If a live neighboring family is erased to make the answer cleaner, the output is structurally misleading.

### Invalid behavior 7. Cosmetic symptom replacing broken invariant

If the answer only says things like “the output is messy” without naming the deeper structural break, the contract is weakened.

---

## Output restraint rules

### Rule 1. Required fields must stay meaningful

Do not fill a field with vague filler just to satisfy the template.

### Rule 2. Optional fields must stay bounded

Optional fields are for clarification, not unsupported expansion.

### Rule 3. The output level must match the fit level

Do not render subtree certainty when the fit is only family-level.

### Rule 4. The output should preserve unresolved tension honestly

If the case is boundary-live, say so.

### Rule 5. The output should not imply more repair certainty than exists

A useful first move is not a full closure claim.

---

## Example route-first outputs

### Example 1. Clean family-level output

```text
current primary fit: F4 at family level
broken invariant: the system is not reliably converting task intent into correct execution under the current contract
evidence basis: mostly direct evidence from repeated contract-following failure
confidence posture: high confidence, bounded at family level
safest first fix: tighten the explicit execution contract and validate action order before adding more abstraction
```

### Example 2. Boundary-live output

```text
current primary fit: boundary-live between F3 and F4
broken invariant: continuity and execution surfaces both appear unstable, and the primary break is not yet cleanly separated
evidence basis: indirect signal with meaningful contradictory evidence across state trace and action trace
confidence posture: boundary-live
missing critical evidence: stronger step-to-step continuity trace is still needed
safest first fix: stabilize state carryover visibility before committing to a larger execution rewrite
```

### Example 3. Observability-blocked output

```text
current primary fit: strongest current candidate is F5
broken invariant: the system is not diagnosable enough to support a sharper structural read
evidence basis: observability-blocked, with insufficient trace quality for stronger separation
confidence posture: insufficient evidence
misrepair warning: do not perform large structural changes before the visibility surface improves
safest first fix: improve inspection and trace quality first
```

### Example 4. F1 vs F7 restrained output

```text
current primary fit: strongest current candidate is F1, with F7 still live as a neighboring boundary
broken invariant: evidence anchoring appears weaker than the final representational surface
evidence basis: indirect signal, because the output surface is degraded and may partly mask the deeper anchor quality
confidence posture: moderate
boundary note: F7 remains live because the rendered form is also meaningfully impaired
safest first fix: repair evidence linkage before treating representational cleanup as the main solution
```

---

## Common output-contract mistakes

### Mistake 1. Treating the output template like decoration

The fields are structural, not cosmetic.

### Mistake 2. Making optional fields do all the real work

The required fields should already carry the core meaning.

### Mistake 3. Hiding uncertainty in paragraph style

If a boundary is live, name it.

### Mistake 4. Letting compact mode erase the safety layer

Compact output should still preserve the minimum contract.

### Mistake 5. Using a rigid field shape to fake precision

A template does not justify unsupported detail.

---

## When this page is enough

This page is often enough when:

* you need a stable public rendering shape
* you want route-first answers to be comparable
* you want to prevent drift across outputs
* you want a compact and expanded version of the same structural answer

In those cases, the contract already gives strong value.

---

## When this page is not enough

This page is usually not enough when:

* you need overlay and multi-surface rules
* you need patch-promotion governance
* you need full runtime-mode behavior
* you need deeper repair branches
* you need a full operational repair report

Then the natural next pages are:

* [Atlas Overlay and Secondary Family Discipline v1](./atlas-overlay-and-secondary-family-discipline-v1.md)
* [Atlas Promotion and Patch Thresholds v1](./atlas-promotion-and-patch-thresholds-v1.md)
* [Fixes Hub](./Fixes/README.md)
* [Atlas-to-AI Adapter v1](./atlas-to-ai-adapter-v1.md)

---

## Practical use

Here is the simplest practical workflow.

### Step 1

Complete the route-first structural reading.

### Step 2

Choose the correct fit and confidence posture.

### Step 3

Render the result using the minimum valid output fields.

### Step 4

Add optional fields only when they clarify something real:

* live boundary
* missing evidence
* local branch caution
* misrepair warning
* next diagnostic question

### Step 5

Check the final answer once:
does it say more than the evidence supports?

If yes, shrink it.

That is the safest use of this page.

---

## Relation to other Atlas docs

This page sits after fit, evidence, and first-fix discipline, but before overlay and promotion discipline.

### Upstream neighbors

These pages prepare the reader for the output contract:

* [Problem Map 3.0 Troubleshooting Atlas](../wfgy-ai-problem-map-troubleshooting-atlas.md)
* [Atlas Structure Map](./atlas-structure-map-v1.md)
* [Atlas Family Mini-Specs](./atlas-family-mini-specs-v1.md)
* [Atlas Boundary Decision Guide](./atlas-boundary-decision-guide-v1.md)
* [Atlas Subtree Expansion Index](./atlas-subtree-expansion-index-v1.md)
* [Atlas Fit Candidate Registry](./atlas-fit-candidate-registry-v1.md)
* [Atlas First Fix and Misrepair Discipline v1](./atlas-first-fix-and-misrepair-discipline-v1.md)
* [Atlas Evidence and Confidence Discipline v1](./atlas-evidence-and-confidence-discipline-v1.md)

### Side neighbors

This page pairs especially well with:

* [Troubleshooting Atlas Router v1 Usage Guide](./troubleshooting-atlas-router-v1-usage.md)
* [Atlas-to-AI Adapter v1](./atlas-to-ai-adapter-v1.md)

Why:
the usage guide shows how people interact with route-first analysis, while the adapter expresses the deeper routing logic that this page constrains into a stable public output shape.

### Downstream neighbors

These are the natural next steps:

* [Atlas Overlay and Secondary Family Discipline v1](./atlas-overlay-and-secondary-family-discipline-v1.md)
* [Atlas Promotion and Patch Thresholds v1](./atlas-promotion-and-patch-thresholds-v1.md)

Why:
this page stabilizes output shape, while later pages constrain multi-surface rendering and future public promotion of finer structure.

---

## Current status

This page should be read as the stable **public routing output contract**.

That means:

* it does not rewrite the frozen core
* it does not replace structural reasoning
* it gives readers a minimum and expanded rendering shape
* it reduces the chance that Atlas outputs drift into vague, inflated, or incomparable prose

Its value is consistency-with-restraint.

That is exactly what this layer should do.

---

## Future extension

This page will become even stronger once its closest companion pages exist.

The most important future companions are:

* [Atlas Overlay and Secondary Family Discipline v1](./atlas-overlay-and-secondary-family-discipline-v1.md)
* [Atlas Promotion and Patch Thresholds v1](./atlas-promotion-and-patch-thresholds-v1.md)

Later versions may also add:

* more compact-mode examples
* more expanded-mode examples
* more runtime-sensitive rendering notes
* more family-specific output cautions

But the core job of this page should stay simple:

render the route-first answer in a stable, bounded, and comparable shape.

---

## Closing note 🔭

A strong system is not only good at reaching a useful structural read.

It is also good at presenting that read in a form that stays:

clear,
bounded,
comparable,
and honest about what is still unresolved.

That is what this page is for.

It gives the Atlas a public output contract
so the route-first layer can stay readable without becoming sloppy.
