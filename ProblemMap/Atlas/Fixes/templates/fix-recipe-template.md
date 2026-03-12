<!--
AI_NOTE_START

Document role:
This file is the reusable template for community or official fix recipes inside the Atlas Fixes layer.

How to use this file:
1. Copy this template when creating a new fix recipe.
2. Fill only the sections that are relevant and keep the scope small.
3. Use this template after reading:
   - [Community Fix Lab](../community/README.md)
   - [Contribution Checklist](./contribution-checklist.md)
   - [Family Fix Surface v1](../official/family-fix-surface-v1.md)
4. Keep route-first discipline:
   - atlas routing first
   - first repair move second
   - deeper WFGY exploration third

What this file is:
- A standard fix recipe template
- A contribution scaffold
- A lightweight documentation structure for runnable or semi-runnable repair assets

What this file is not:
- Not a full style guide
- Not a mandatory proof that the recipe is officially correct
- Not a replacement for maintainer review

Reading discipline for AI:
- Preserve the distinction between routing, first repair, deeper WFGY exploration, and implementation detail.
- Do not skip routing context.
- Do not present partial fixes as universal solutions.
- Prefer small, clear, reproducible recipes.

AI_NOTE_END
-->

# Fix Recipe Template

## Title

> Replace this line with a short clear title.

Example:
`F1 Retrieval Anchor Drift - Minimal reranking fix recipe`

---

## 0. Quick summary

**What this recipe does**

Write 1 to 3 short sentences.

Example:
This recipe improves a grounding-first failure by adding a lightweight source-to-answer verification step after retrieval.  
It is meant for cases where the answer looks fluent but is weakly anchored.

---

## 1. Artifact type

Choose one or more:

- Colab notebook
- JSON fixture
- prompt pack
- workflow recipe
- benchmark rerun
- reproduction pack
- implementation note

---

## 2. Atlas routing context

**Primary family**  
`F?`

**Secondary family**  
`F?` or `None`

**Broken invariant**  
Write one short sentence.

**Best current fit**  
Write the nearest node, family entry, or edge-fit wording.

**Why this belongs here**  
Write 2 to 4 sentences explaining why this recipe belongs in this region.

---

## 3. Problem being fixed

Describe the specific problem this recipe targets.

Useful questions:

- what is going wrong
- what does the broken baseline look like
- what symptom is visible
- why is this a good target for a fix recipe

Keep this section short and concrete.

---

## 4. Baseline failure

Describe the broken version first.

Include things like:

- baseline setup
- broken behavior
- common visible symptom
- known weakness

Optional mini format:

**Baseline input**  
`...`

**Baseline behavior**  
`...`

**Baseline failure note**  
`...`

---

## 5. First repair move

Describe the first repair move this recipe applies.

Useful questions:

- what is the first intervention
- why this move comes before other moves
- what this move is trying to restore

Optional mini format:

**Repair action**  
`...`

**Why this is first**  
`...`

**Expected improvement**  
`...`

---

## 6. Misrepair warning

State at least one common wrong first move.

### Wrong first move

`...`

### Why it is tempting

`...`

### Why it is wrong

`...`

This section is required.
A good fix recipe should not only say what to do.
It should also say what not to do first.

---

## 7. Inputs

List the inputs needed.

Examples:

- query
- corpus
- prompt
- JSON config
- workflow state
- notebook parameters
- expected schema
- environment assumptions

Use a short format like:

```text
Input A:
Input B:
Input C:
````

---

## 8. Procedure

Write the actual steps.

Keep them small and numbered.

### Example format

1. Load the baseline input.
2. Run the broken baseline.
3. Record the failure output.
4. Apply the first repair move.
5. Run the repaired version.
6. Compare before and after.

If this recipe is runnable, the steps should be easy to follow without guessing.

---

## 9. Expected output or result

State what should improve.

Examples:

* better anchor alignment
* fewer missing fields
* clearer trace visibility
* successful workflow closure
* fewer deadlocks
* higher schema pass rate

Optional mini format:

**Before**
`...`

**After**
`...`

**Success signal**
`...`

---

## 10. Optional evaluation fields

List simple fields or checks if helpful.

Examples:

* `support_rate`
* `schema_pass_rate`
* `closure_success`
* `trace_completeness`
* `wrong_anchor_rate`
* `field_loss_count`

Only include fields that are actually useful.

---

## 11. Optional WFGY escalation

Use this section only if deeper WFGY exploration is relevant.

### When to escalate

`...`

### What to pass into WFGY

* routed family
* broken invariant
* first repair move already tried
* unresolved pressure

### What WFGY is expected to add

`...`

Keep this clean.
Do not use this section to skip atlas routing.

---

## 12. Files included

List the files included in the contribution.

Example:

* `demo.ipynb`
* `input.json`
* `expected_output.json`
* `README.md`

---

## 13. Limitations

Be honest.

Examples:

* only tested on a toy corpus
* only works for a narrow schema
* not yet benchmarked broadly
* assumes a simple notebook environment
* partial recipe, not a full solution

This section is strongly recommended.

---

## 14. One-line maintainer note

Write one short line that helps review the contribution.

Example:
Small F1 grounding recipe with runnable JSON fixture and clear before/after support check.

---

## 15. Copy-paste mini skeleton

Use this when you want the fastest possible start.

```md
# Title

## 0. Quick summary
...

## 1. Artifact type
...

## 2. Atlas routing context
Primary family:
Secondary family:
Broken invariant:
Best current fit:
Why this belongs here:

## 3. Problem being fixed
...

## 4. Baseline failure
...

## 5. First repair move
...

## 6. Misrepair warning
Wrong first move:
Why it is tempting:
Why it is wrong:

## 7. Inputs
...

## 8. Procedure
1.
2.
3.

## 9. Expected output or result
...

## 10. Optional evaluation fields
...

## 11. Optional WFGY escalation
...

## 12. Files included
...

## 13. Limitations
...

## 14. One-line maintainer note
...
```

---

## 16. Closing note

A good fix recipe does not need to be huge.

It only needs to be:

* routed
* clear
* scoped
* usable
* honest

