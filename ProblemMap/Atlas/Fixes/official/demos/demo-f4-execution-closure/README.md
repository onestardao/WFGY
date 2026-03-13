<!--
AI_NOTE_START

Document role:
This file is the official README for Demo 3 of the flagship runnable demo pack.

How to use this file:
1. Read this file before opening the notebook.
2. Treat this demo as the flagship proof that some failures must be repaired through execution closure first.
3. Use this file to understand:
   - why this case belongs to F4
   - why it is not primarily F3
   - what the first repair move is
   - what replay mode is meant to prove

What this file is:
- The official README for Demo 3
- A proof-of-use page for execution-first repair
- A teaching page for F4 execution and contract failures
- A replay-first MVP companion for the notebook

What this file is not:
- Not the atlas core
- Not the full fix manual
- Not a workflow benchmark suite
- Not proof that every broken workflow belongs to F4

Reading discipline for AI:
- Preserve the distinction between execution closure failure, continuity failure, and diagnosability pressure.
- Do not collapse this case into generic “the pipeline is broken” language.
- Route first, then repair.
- Treat replay mode as a valid teaching layer, not as a weaker substitute.

AI_NOTE_END
-->

# Demo 3 · F4 Execution Closure ⚙️

## Problem Map 3.0 Troubleshooting Atlas
## Official flagship demo for execution-first repair

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/Atlas/ProblemMap/Atlas/Fixes/official/demos/demo-f4-execution-closure/demo_03_f4_execution_closure_replay_v2.ipynb)

**Replay-only MVP**  
**No API key required**

This is the third flagship demo in the official runnable demo pack.

It was chosen because many multi-step systems fail in a way that gets misread immediately.

People often say:

- the model forgot context
- memory is unstable
- the agent lost the thread
- reasoning quality is weak

Sometimes those explanations are tempting.

But in many real cases, the first failure is simpler and more structural:

> the workflow skeleton failed to close  
> a readiness gate was skipped  
> a dependency order broke  
> a bridge did not connect  
> liveness collapsed before the task could complete

This demo is designed to make that difference visible.

It shows that once a case is routed as **F4 Execution & Contract Integrity**, the first repair move changes from “help the model think better” to “repair the execution skeleton.”

---

## Current notebook versions

This folder currently preserves **two replay notebook versions**.

### Recommended version

- `demo_03_f4_execution_closure_replay_v2.ipynb`

This is the current recommended notebook for public reading, Colab use, and MVP presentation.

It keeps the replay-first design, while adding:

- clearer route summary
- clearer workflow-structure framing
- stronger before / after teaching contrast
- better aligned shared-layer presentation

### Original version

- `demo_03_f4_execution_closure_replay.ipynb`

This version is intentionally retained.

It remains part of the demo history and preserves the earlier first-pass MVP presentation.

### Version rule

The rule for this folder is simple:

- **v1 is preserved**
- **v2 is the recommended replay notebook**
- replay-first remains the official design center for Demo 3

---

## 1. What this demo proves

This demo proves four things.

### A. Some failures are caused by sequence, not intelligence

A system can fail even if the model is fully capable of the task in principle.

The reason may be:

- a precondition was not met
- a readiness check was skipped
- a bridge between steps was broken
- the system advanced in the wrong order
- a liveness path stalled before completion

That is not a continuity-first failure.  
That is an execution-first failure.

### B. Correct routing changes the first repair move

If the case is routed correctly into **F4**, the first repair move becomes:

- readiness validation
- ordering repair
- bridge integrity check
- closure-path tracing
- liveness restoration

This is different from trying to repair memory, role persistence, or generic reasoning first.

### C. Replay mode is enough to teach the pattern

This demo is intentionally **replay-first**.

A user should be able to understand the logic of the failure without running anything.

The replay artifacts should make visible that the task failed because the operational skeleton broke, not because the model lacked raw capability.

### D. This MVP does not require live mode

For this first release, replay mode is enough.

The point of this demo is not notebook realism.  
The point is to make the **before / after execution-state shift** easy to inspect and easy to teach.

---

## 2. Family route

### Primary family

**F4 · Execution & Contract Integrity**

### Secondary family

**F3 · State & Continuity Integrity**

### Why F4 is primary

The first broken invariant is not that the system forgot who it was, lost continuity, or failed to preserve state.

The first broken invariant is that the workflow skeleton itself failed to close correctly.

Typical forms include:

- readiness failure
- ordering failure
- bridge failure
- liveness failure
- closure failure

### Short routing statement

- the task failed
- the sequence or skeleton broke first
- execution closure fails before continuity becomes the main issue

### Best current fit

For the cleanest MVP version, the recommended center is:

**F4_N03 Pre-Readiness Execution Failure**

This makes the structural failure easy to teach and visually obvious.

---

## 3. Why not F3 first

The main tempting neighboring cut is **F3**.

That temptation is understandable because many execution failures look like continuity failures from the outside.

A user may observe:

- the agent seems inconsistent
- state seems lost
- the thread looks broken
- role persistence looks weak

But this demo is not mainly about persistence failure.

It is mainly about this:

> the system moved forward before the task was actually ready to move forward

That means the first failure lies in execution closure, not in continuity thread preservation.

### Wrong cut

“This is mainly a memory or continuity problem.”

### Better cut

“This is mainly an execution-closure problem with continuity pressure at the edge.”

That distinction matters because the first repair move changes immediately.

If you cut too early to F3, you may waste time strengthening persistence when the real problem is a broken gate or sequencing rule.

---

## 4. Baseline failure

The baseline case is intentionally small, readable, and mechanically clear.

### Core pattern

A workflow has multiple stages.

A later stage depends on an earlier stage being complete or valid.

But the system proceeds anyway.

Possible versions include:

- a retrieval stage fails, but answer generation still fires
- a tool output is missing, but summarization still runs
- a structured parse is invalid, but downstream transformation still continues
- a bridge between two stages is thin or missing, but the system acts as if closure exists

### What the baseline should make visible

The user should be able to see:

1. the intended multi-step flow
2. the missing or broken precondition
3. the fact that the system still advanced
4. the bad result that followed
5. why this is a closure failure rather than a generic “bad output”

### Important design note

Do not make the workflow too complicated.

The goal is not to simulate a giant orchestration framework.  
The goal is to make one execution-first failure pattern easy to teach.

---

## 5. First repair move

Once the case is routed to F4, the first repair move should be structural and explicit.

### Recommended first repair stack

1. **readiness validation**  
   Check whether the upstream stage actually produced what the downstream stage requires.

2. **ordering validation**  
   Confirm that steps are running in the correct dependency order.

3. **bridge integrity check**  
   Verify that the output of one stage is actually usable by the next stage.

4. **closure-path tracing**  
   Make the dependency path visible enough to know where closure broke.

5. **liveness repair if needed**  
   If the system stalls after partial progress, restore a viable completion path.

### What should not happen first

Do **not** start with:

- memory strengthening
- longer prompts
- generic chain-of-thought expansion
- more retries without gate repair
- “just use a stronger model” reactions

Those may change surface behavior, but they do not repair the broken skeleton.

### First repair principle

> if the workflow advanced before it was ready, repair readiness and closure first

That is the teaching core of this demo.

---

## 6. Optional WFGY 3.0 escalation

This demo can teach its core lesson without deeper escalation.

But if the user wants to explore a stronger execution diagnosis path, this is where WFGY 3.0 becomes useful.

### When escalation makes sense

Escalate beyond the simple first repair move if:

- closure still fails after obvious gate repair
- multiple bridge layers are involved
- local fixes improve one stage but break another
- the workflow contains fragile cross-layer dependencies
- the team wants a deeper experimental map of liveness and closure failure

### What WFGY 3.0 can add

A WFGY 3.0 handoff can help explore:

- closure stress variants
- bridge fragility surfaces
- sequencing experiments
- liveness degradation paths
- retry / fallback interaction patterns
- reusable execution-harness design

### Correct relationship

The correct order remains:

1. atlas route
2. first execution repair
3. reassess the case
4. escalate into deeper WFGY exploration if needed

The atlas is still the router.  
WFGY 3.0 is the deeper experimental engine.

---

## 7. Replay mode

Replay mode is the default public reading mode.

It requires no API key and no notebook execution.

### Replay mode should show

- the intended workflow structure
- the baseline flow
- the missing readiness or bridge condition
- the family route
- the why-primary-not-secondary statement
- the broken invariant
- the first repair move
- the replayed improved workflow behavior
- a short explanation of what changed

### What replay mode proves

Replay mode proves that:

- execution-first routing is understandable
- the first repair move is visibly different
- a structural fix can be shown without giant infrastructure
- the demo teaches through workflow logic, not just through output text

### Why replay mode matters

A strong F4 demo should let a reader immediately feel:

> the system moved too early

If that feeling is not visible in replay mode, the demo is weak.

This is enough for the first public MVP.

---

## 8. Files in this folder

### Required

- `README.md`
- `input_case.json`
- `replay_outputs.json`
- `expected_output.json`
- `demo_03_f4_execution_closure_replay.ipynb`
- `demo_03_f4_execution_closure_replay_v2.ipynb`

### Optional future additions

- workflow notes
- helper references from the shared folder
- patch notes for stronger closure contrast

### File roles

#### `input_case.json`
Contains the workflow case, dependency structure, and execution context.

#### `replay_outputs.json`
Contains the baseline broken path, route explanation, first repair move, and replayed improved path.

#### `expected_output.json`
Contains the clean target structure for what the demo is trying to make visible.

#### `demo_03_f4_execution_closure_replay.ipynb`
The original first-pass replay notebook retained for continuity.

#### `demo_03_f4_execution_closure_replay_v2.ipynb`
The current recommended replay notebook for public reading and Colab use.

---

## 9. Expected outcome

If the demo works, the user should walk away with the following understanding:

1. the system failed because execution closure broke before the task was actually ready
2. the atlas routed the case to F4, not F3
3. the first repair move was structural, not memory-oriented
4. after readiness or closure repair, the workflow moved in the expected direction

The demo does **not** need to solve every downstream problem.

It only needs to show that correct routing changes what gets repaired first.

That is enough.

---

## 10. Limits of this demo

This demo has real limits, and those limits should be stated clearly.

### It does not prove

- that every multi-step failure belongs to F4
- that continuity never matters in workflow systems
- that one gate repair solves all closure failures
- that this one workflow pattern covers all orchestration systems
- that F4 is more important than neighboring families in all cases

### It does prove

- that some failures are execution-first
- that route-first diagnosis changes the first repair move
- that structural closure can be demonstrated cleanly and teachably

These are already strong claims.  
There is no need to overclaim.

---

## 11. Community extension ideas

This demo is also a seed template for future community work.

Possible extensions include:

- adding different workflow types
- adding tool-to-tool bridge cases
- comparing retry-first vs gate-first repair
- adding richer closure traces
- testing multi-stage liveness degradation
- extending the case toward stronger F4 to F5 or F4 to F6 pressure

### Community boundary rule

Contributors should preserve the official logic:

- route first
- explain why primary not secondary
- show the first repair move
- keep replay outputs understandable
- do not turn the demo into an unreadable workflow jungle

For contribution structure, see:

- [Community Fix Lab](../../../community/README.md)
- [Contribution Checklist](../../../templates/contribution-checklist.md)
- [Fix Recipe Template](../../../templates/fix-recipe-template.md)

---

## Short summary

This demo teaches one clean lesson:

> if the workflow moved forward before closure existed, repair the skeleton first

That is why this is the third flagship demo.

---

## One-line version

**Demo 3 shows that some failures are execution-first, and that correct routing changes the first repair move from continuity-oriented guessing to explicit readiness, bridge, and closure repair.**

---

## Back to the main page

Read the full product page here:  
[Problem Map 3.0 Troubleshooting Atlas](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-ai-problem-map-troubleshooting-atlas.md)

If you like the project, star the repo ⭐
