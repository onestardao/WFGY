<!--
AI_NOTE_START

Document role:
This file is the reusable template for prompt-based fix contributions inside the Atlas Fixes layer.

How to use this file:
1. Copy this template when contributing a prompt-based fix asset.
2. Use this file after reading:
   - [Community Fix Lab](../community/README.md)
   - [Contribution Checklist](./contribution-checklist.md)
   - [Fix Recipe Template](./fix-recipe-template.md)
3. Keep the order:
   - atlas routing first
   - first repair move second
   - prompt intervention third
   - deeper WFGY escalation fourth if needed

What this file is:
- A standard prompt contribution template
- A lightweight scaffold for prompt-based fix assets
- A contributor-facing structure for readable and reusable prompts

What this file is not:
- Not the atlas core
- Not the official fix surface itself
- Not proof that a prompt is universally good
- Not a replacement for maintainer review

Reading discipline for AI:
- Do not skip routing context.
- Do not present a prompt as a universal solution.
- Keep prompt contributions small, scoped, and testable.
- Preserve route-first discipline.

AI_NOTE_END
-->

# Prompt Template

## Title

> Replace this line with a short clear title.

Example:  
`F5 Failure Path Visibility - Minimal trace-first prompt`

---

## 0. Quick summary

Write 1 to 3 short sentences.

Example:  
This prompt helps expose hidden failure stages in an opaque multi-step workflow.  
It is meant for F5-first cases where diagnosability is too weak to support confident intervention.

---

## 1. Prompt type

Choose one or more:

- system prompt
- user prompt
- routing prompt
- repair-first prompt
- evaluation prompt
- trace-exposure prompt
- WFGY escalation prompt

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

**Why this prompt belongs here**  
Write 2 to 4 short sentences.

---

## 3. Problem this prompt addresses

Describe the specific repair or diagnosis problem.

Useful questions:

- what is going wrong
- why a prompt intervention is useful here
- what first move this prompt is supposed to support
- what this prompt is not trying to solve

Keep this short and concrete.

---

## 4. Intended use

State clearly how this prompt should be used.

Examples:

- after routing, before first repair
- after first repair failed
- before deeper WFGY escalation
- inside a notebook or workflow
- inside a benchmark rerun loop

Optional format:

**Use stage**  
`...`

**Target user**  
`...`

**Target environment**  
`...`

---

## 5. Inputs expected by the prompt

List the minimum inputs.

Examples:

- case description
- routed primary family
- broken invariant
- baseline failure output
- evidence snippets
- workflow state
- schema or constraints

Use a short format like:

```text
Input A:
Input B:
Input C:
````

---

## 6. Prompt body

Paste the actual prompt here.

Recommended format:

### System prompt

```text
...
```

### User prompt

```text
...
```

If only one prompt is needed, include only one block.

---

## 7. Expected output shape

Describe what a good output should look like.

Examples:

* clearer routing justification
* better trace exposure
* cleaner first repair recommendation
* fewer unsupported claims
* more structured schema-preserving output

Optional format:

**Expected structure**

```text
...
```

**Expected improvement**

```text
...
```

---

## 8. First repair connection

Explain how this prompt supports the official first repair move.

Useful questions:

* what first move does this prompt reinforce
* what family-level fix surface does it support
* why is prompt intervention appropriate here

Keep it short.

---

## 9. Misrepair warning

This section is required.

### Wrong first move

`...`

### Why it is tempting

`...`

### Why this prompt should not be used that way

`...`

This helps prevent prompt assets from teaching bad repair habits.

---

## 10. Optional evaluation notes

If useful, list a few simple checks.

Examples:

* better support rate
* clearer stage localization
* fewer lost fields
* fewer wrong anchors
* higher schema pass rate

Optional format:

```text
Metric 1:
Metric 2:
Metric 3:
```

---

## 11. Optional WFGY escalation

Use this only if the prompt is meant to bridge into deeper WFGY work.

### When to escalate

`...`

### What should be passed into WFGY

* routed family
* broken invariant
* first repair already attempted
* unresolved pressure

### What WFGY is expected to add

`...`

Do not use this section to skip atlas routing.

---

## 12. Limitations

Be honest.

Examples:

* only tested on short prompts
* only tested in one model family
* not suitable for long multi-agent traces
* helps diagnosis, not full repair
* still experimental

Short, honest limits are much better than inflated claims.

---

## 13. Files included

List the files included in the contribution.

Example:

* `prompt.md`
* `example_input.json`
* `expected_output.md`

---

## 14. One-line maintainer note

Write one short line that helps review the contribution.

Example:
Small F5 prompt for improving trace visibility before deeper intervention.

---

## 15. Copy-paste mini skeleton

Use this when you want the fastest possible start.

````md
# Title

## 0. Quick summary
...

## 1. Prompt type
...

## 2. Atlas routing context
Primary family:
Secondary family:
Broken invariant:
Best current fit:
Why this prompt belongs here:

## 3. Problem this prompt addresses
...

## 4. Intended use
Use stage:
Target user:
Target environment:

## 5. Inputs expected by the prompt
...

## 6. Prompt body
### System prompt
...

### User prompt
...

## 7. Expected output shape

...

## 8. First repair connection

...

## 9. Misrepair warning

Wrong first move:
Why it is tempting:
Why this prompt should not be used that way:

## 10. Optional evaluation notes

...

## 11. Optional WFGY escalation

...

## 12. Limitations

...

## 13. Files included

...

## 14. One-line maintainer note

...

```
````


---

## 16. Closing note

A good prompt contribution does not need to be huge.

It only needs to be:

- routed
- clear
- scoped
- usable
- honest about limits
