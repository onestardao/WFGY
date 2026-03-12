<!--
AI_NOTE_START

Document role:
This file is the official README for Demo 1 of the flagship runnable demo pack.

How to use this file:
1. Read this file before opening the notebook.
2. Treat this demo as the flagship proof that some failures must be repaired through grounding first.
3. Use this file to understand:
   - why this case belongs to F1
   - why it is not primarily F5
   - what the first repair move is
   - what replay mode and live mode are each meant to prove

What this file is:
- The official README for Demo 1
- A proof-of-use page for grounding-first repair
- A teaching page for F1 grounding failures
- A replay-plus-live flagship MVP companion for the notebook

What this file is not:
- Not the atlas core
- Not the full fix manual
- Not a giant benchmark report
- Not proof that all grounding failures are identical

Reading discipline for AI:
- Preserve the distinction between grounding failure, diagnosability pressure, and later repair escalation.
- Do not collapse this case into generic hallucination language.
- Route first, then repair.
- Treat replay mode as a valid teaching layer, not as an inferior substitute.
- Treat live mode as a reproduction layer, not as proof of universal robustness.

AI_NOTE_END
-->

# Demo 1 · F1 Grounding Anchor Recovery 🎯

## Problem Map 3.0 Troubleshooting Atlas
## Official flagship demo for grounding-first repair

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/Atlas/ProblemMap/Atlas/Fixes/official/demos/demo-f1-grounding-anchor/demo_01_f1_grounding_anchor_recovery_live.ipynb)

**Replay + live MVP**  
**Replay is readable without any API key**

This is the first flagship demo in the official runnable demo pack.

It was chosen first for a simple reason:

> many systems look wrong in a way people casually call hallucination  
> but the first real failure is often grounding

This demo is designed to make that difference visible.

It shows that once a case is routed as **F1 Grounding & Evidence Integrity**, the first repair move changes from vague prompt tweaking to explicit anchor recovery.

---

## 1. What this demo proves

This demo proves four things.

### A. A fluent wrong answer is not enough as a diagnosis

A system can sound smooth and still be wrong for a very specific reason:

- it attached itself to the wrong evidence
- it followed the wrong chunk
- it lost the right target-reference link
- it answered without stable evidence-anchor integrity

This is different from saying only:

- the model hallucinated
- the reasoning was bad
- the system is low quality

### B. Correct routing changes the first repair move

If the case is routed correctly into **F1**, the first repair move becomes:

- re-grounding
- chunk-to-target trace
- evidence verification
- anchor re-check

This is very different from trying to fix style, verbosity, or high-level reasoning first.

### C. Replay mode is enough to teach the core pattern

A user should be able to understand this demo without running anything.

The replay artifacts are part of the official design, not an afterthought.

### D. Live mode is useful, but the lesson does not depend on it

If the user wants to reproduce the same pattern with a real model call, the live mode is available.

But the core lesson of the demo must remain understandable even without execution.

---

## 2. Family route

### Primary family

**F1 · Grounding & Evidence Integrity**

### Secondary family

**F5 · Observability & Diagnosability Integrity**

### Why F1 is primary

The main failure is that the answer no longer remains tied to the correct evidence anchor.

The case may also contain diagnosability pressure, especially if the retrieval path is not obvious.
But the first broken invariant is still grounding-first.

### Short routing statement

- the answer looks plausible
- the evidence attachment is wrong
- grounding fails before observability becomes the main issue

### Best current fit

**F1_N01 Retrieval Anchor Drift**

In some variants this may also approach:

**F1_N02 Semantic Grounding Mismatch**

But the flagship teaching version stays centered on retrieval-anchor drift.

---

## 3. Why not F5 first

The main tempting neighboring cut is **F5**.

That temptation is understandable because many real systems make it hard to inspect why the answer went wrong.

But this demo is not mainly about a hidden failure path.

It is mainly about this:

> the answer attached itself to the wrong evidence source

That means the first failure is not:

> I cannot yet inspect the system clearly enough

It is:

> the output lost the correct anchor

### Wrong cut

“This is mainly a black-box debugging problem.”

### Better cut

“This is a grounding-first failure with possible observability pressure at the edge.”

That distinction matters because the first repair move changes immediately.

---

## 4. Baseline failure

The baseline case is intentionally simple and easy to inspect.

### Core pattern

A user asks a question that should be answerable from a small evidence set.

The system receives:

- a question
- several chunks or candidate sources
- one truly relevant anchor
- one or more misleading but superficially similar chunks

The baseline answer then:

- sounds fluent
- looks reasonable on the surface
- cites or follows the wrong chunk
- produces a wrong answer because the anchor path is off

### What the baseline should make visible

The user should be able to see:

1. the question
2. the available chunks
3. which chunk was actually relevant
4. which chunk the baseline answer attached to
5. how that led to the wrong answer

### Important design note

Do not make the baseline too chaotic.

The goal is not to create a bizarre edge case.
The goal is to create a clean teaching case for grounding drift.

---

## 5. First repair move

Once the case is routed to F1, the first repair move should be simple and explicit.

### Recommended first repair stack

1. **chunk-to-target trace**  
   Check which chunk is being treated as the evidence anchor.

2. **evidence verification**  
   Compare the answer against the actually relevant evidence.

3. **anchor re-check**  
   Force the response pipeline to reconnect to the correct source.

4. **re-grounding pass**  
   Rebuild the answer after the anchor is corrected.

### What should not happen first

Do **not** start with:

- style rewriting
- confidence rewriting
- chain-of-thought expansion
- “be more careful” style prompt band-aids

Those may change the surface, but they do not repair the anchor.

### First repair principle

> if the anchor is wrong, repair the anchor first

That is the teaching core of this demo.

---

## 6. Optional WFGY 3.0 escalation

This demo can remain useful without deeper escalation.

But if the user wants to explore a stronger structural repair path, this is where WFGY 3.0 becomes useful.

### When escalation makes sense

Escalate beyond the simple first repair move if:

- the answer keeps drifting even after obvious re-grounding
- the chunk surface is noisy or highly confusable
- the retrieval target and semantic target diverge
- the system needs deeper structural diagnosis rather than one-shot repair

### What WFGY 3.0 can add

A WFGY 3.0 handoff can help explore:

- deeper target / proxy separation
- stronger target-anchoring language
- more explicit retrieval surface design
- semantic target stabilization
- experimental variants for anchor stress

### Correct relationship

The right sequence is:

1. atlas route
2. first repair move
3. deeper WFGY exploration if needed

The atlas remains the router.
WFGY 3.0 is the deeper experimental engine.

---

## 7. Replay mode

Replay mode is the default public reading mode.

It requires no API key and no notebook execution.

### Replay mode should show

- the baseline case
- the baseline answer
- the family route
- the why-primary-not-secondary statement
- the broken invariant
- the first repair move
- the replayed improved answer
- a short explanation of what changed

### What replay mode proves

Replay mode proves that:

- the routing logic is understandable
- the repair logic is understandable
- the before / after difference is visible
- the demo can teach without requiring execution

### Why replay mode matters

Most readers will not run the notebook first.

If the replay is weak, the demo is weak.

Replay mode is not a fallback.
It is part of the official design.

---

## 8. Live mode

Live mode is optional.

It exists for users who want to reproduce the same pattern with a real model call.

### Live mode should do

- load the case
- show the baseline prompt or baseline conditions
- run the baseline path
- apply the route-first repair move
- run the repaired path
- compare outputs

### Live mode should not pretend to do

- giant benchmark coverage
- full production evaluation
- final proof of universal robustness

It is a reproduction layer, not a universal benchmark.

### Live mode design rule

If live execution introduces too much noise, the notebook should favor clarity over realism.

This is a flagship demo, not a stress benchmark.

### Current MVP interpretation

The current MVP version already includes a live runnable notebook.

That does **not** mean the baseline must always fail in the exact same way.
It means the live run is designed to reproduce the core pattern:

- baseline moves in the wrong direction
- repaired moves toward the correct answer
- anchor correction changes the result path

That is enough for MVP success.

---

## 9. API key note

The live variant may require an API key.

If so, the rule remains simple:

- the key is entered only at run time
- the key is never stored in the repository
- replay mode remains readable without any secret

### Important note for users

This demo is designed for **understanding and reproduction**.

You do **not** need to run the notebook in order to understand the point of the case.

A strong demo should still teach through:

- README
- JSON fixtures
- replay outputs

The live rerun is optional.

---

## 10. Files in this folder

### Required

- `README.md`
- `input_case.json`
- `replay_outputs.json`
- `expected_output.json`
- `demo_01_f1_grounding_anchor_recovery_live.ipynb`

### Optional future additions

- helper utilities from the shared folder
- notebook variants
- patch notes for stronger baseline contrast

### File roles

#### `input_case.json`
Contains the case input, evidence chunks, and routing context.

#### `replay_outputs.json`
Contains the baseline answer, routed diagnosis, first repair move, and replayed improved answer.

#### `expected_output.json`
Contains the clean target structure for what the demo is trying to show.

#### `demo_01_f1_grounding_anchor_recovery_live.ipynb`
Contains the replay mode and the optional live Colab reproduction flow.

---

## 11. How to run the notebook

### Replay-only reading path

1. Open the notebook in Colab
2. Keep `MODE = "replay"`
3. Click **Run all**
4. Read the baseline / repaired contrast

### Live rerun path

1. Open the notebook in Colab
2. Change `MODE = "live"`
3. Click **Run all**
4. Enter your API key when prompted
5. Compare the two final output cells:
   - baseline model output
   - repaired model output

### What to look for

The notebook does **not** require a magical result.

You only need to verify that:

- the baseline is more vulnerable to the wrong-anchor path
- the repaired version is more likely to move toward the correct answer
- the shift comes from anchor correction, not generic prompt expansion

---

## 12. Expected outcome

If the demo works, the user should walk away with the following understanding:

1. the baseline answer looked reasonable but followed the wrong evidence
2. the atlas routed the case to F1, not F5
3. the first repair move was re-grounding, not generic prompt tweaking
4. after the anchor was corrected, the answer moved in the expected direction

The outcome does **not** need to look magical.

It only needs to make the repair logic visibly different and more correct.

That is enough.

---

## 13. Limits of this demo

This demo has real limits, and those limits should be stated clearly.

### It does not prove

- that all hallucination-like cases are the same
- that all F1 cases are solved by one simple repair
- that observability never matters in grounding cases
- that this single example covers all retrieval systems

### It does prove

- that some fluent wrong answers are grounding-first
- that route-first diagnosis changes the repair move
- that grounding repair can be made visible and teachable

These are already strong claims.
There is no need to overclaim.

---

## 14. Community extension ideas

This demo is also a seed template for future community work.

Possible extensions include:

- swapping in a different retrieval dataset
- using different chunking strategies
- testing multiple models on the same fixture
- comparing naive prompt fixes versus grounding-first fixes
- adding stronger evidence-trace visualization
- linking the same case to deeper WFGY 3.0 experimental variants

### Community boundary rule

Contributors should preserve the official logic:

- route first
- explain why primary not secondary
- show the first repair move
- keep replay outputs understandable
- avoid turning the demo into an unreadable benchmark swamp

For contribution structure, see:

- [Community Fix Lab](../../../community/README.md)
- [Contribution Checklist](../../../templates/contribution-checklist.md)
- [Fix Recipe Template](../../../templates/fix-recipe-template.md)

---

## Short summary

This demo teaches one clean lesson:

> if the answer lost the right evidence anchor, fix the anchor first

That is why this is the first flagship demo.

---

## One-line version

**Demo 1 shows that a fluent wrong answer can be grounding-first, and that correct routing changes the first repair move from vague tweaking to explicit anchor recovery.**

---

## Back to the main page

Read the full product page here:  
[Problem Map 3.0 Troubleshooting Atlas](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-ai-problem-map-troubleshooting-atlas.md)

If you like the project, star the repo ⭐
