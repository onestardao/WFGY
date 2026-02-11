<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q124 (Scalable Oversight and Evaluation).
Role: MVP experiment log for Q124 at the effective layer. Focus on simple
      evaluation schemes and tension observables between cheap and rich oversight.
Use: When a user asks about TU Q124 oversight experiments or wants runnable
      examples, load this page first, then follow its notebook links.
-->

# TU Q124 MVP: Scalable oversight and evaluation

_Status: work in progress. This page records early MVP experiments and may change as the TU Q124 program evolves._

> This page documents the first effective-layer MVP experiments for TU Q124
> on scalable oversight and evaluation.
> It does not claim that Q124 is solved as a mathematical problem
> or as a full benchmark.
> The scripts here are small and fully inspectable. You can re-run them with your own
> OpenAI API key to reproduce the qualitative patterns, but the exact numbers will drift.

---

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## Quick start (Colab)

You can run the exact notebook used for this MVP directly in Colab:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q124_MVP/Q124.ipynb)

The notebook is completely self-contained:

- It prints the same header text that you see on this page.  
- It first looks for an `OPENAI_API_KEY` environment variable.  
- If no key is found, it will **ask for a key only if you actually want to run the experiment**.  
- If you do not provide a key, it stops with a clear message and points back to this README.  

You can therefore:

- treat it as a pure reading / inspection artifact, **or**  
- paste an API key once and reproduce the experiment end-to-end.

---

## 0. What this page is about

TU Q124 treats "scalable oversight and evaluation" as a tension problem between three elements:

1. How complex and subtle real tasks become when systems are deployed at scale.  
2. How limited and overloaded the evaluation layer tends to be, whether it is humans or tools.  
3. How easily bad tension can hide inside scores or dashboards that look stable.

This MVP does not try to cover the full Q124 program.

Instead, it focuses on a narrow and fully inspectable slice:

- A finite set of synthetic "worlds" or task clusters where evaluation is non-trivial.  
- Two evaluation modes that operate on the same worlds:

  - a baseline evaluator that uses a short, underspecified rubric,  
  - a guided evaluator that receives additional structured context.

- A single scalar tension observable `T_oversight` in the range `[0, 1]`
  that measures how badly the evaluation layer is misaligned with the underlying task signal.

The goal of this MVP is to show that even in very small toy worlds:

- we can encode oversight as a state space with explicit observables,  
- we can define a simple tension functional for the evaluation layer,  
- we can observe systematic differences between evaluation designs,
  using both error rates and tension profiles.

---

## 1. Experiment A: toy oversight ladders on synthetic tasks

This is the main level-1 MVP for Q124. It is intentionally small and easy to audit.

### 1.1 Research question

In a small set of synthetic oversight worlds:

- Can we define a scalar tension observable `T_oversight` that increases when
  the evaluation layer is clearly out of its depth relative to the underlying task difficulty?  
- When we compare a baseline evaluator and a guided evaluator on the same worlds:

  - Do we see different error rates `B_baseline` and `B_guided`?  
  - Do we see a consistent shift in the tension profiles?  
  - Can simple arbitration rules based on `T_oversight` pick the safer mode more often than chance?

In effective-layer language:

> Does a simple tension geometry for oversight let us see, in a reproducible way,
> where naive evaluation is likely to fail, before we look at long-term metrics?

### 1.2 Setup

Experiment A uses:

- A finite set of `SCENARIOS` (in the current MVP, 8 cases).  
  Each scenario corresponds to a small batch of tasks that must be evaluated.  
  Every scenario carries:

  - a short category label such as `easy_math_correct`, `safety_violation`, `bias_stereotype`,  
  - a free-text description used by the evaluators,  
  - a reference "difficulty" or OOD measure `delta_ref`,  
  - a ground truth quality scalar `rule_score` in `[0, 1]`.

- Two evaluation modes for every scenario:

  - `baseline` mode:

    - uses a minimal rubric with a few lines of instruction,  
    - sees the scenario description and the model answer,  
    - must very quickly output a label and a coarse score.

  - `guided` mode:

    - receives the same inputs as baseline,  
    - plus a more structured rubric that explicitly separates correctness, safety and fairness,  
    - then compresses this back into a label and a score.

- Each mode directly returns:

  - a discrete label `label in {GOOD, BAD}`,  
  - a quality score `score in [0, 1]`.

All tasks and rubrics are synthetic and are defined directly in the notebook.
There are no external datasets.

The notebook only uses:

- Python standard library,  
- `pandas`, `matplotlib`,  
- `openai` SDK when a live LLM evaluator is used.

The code is written so that:

- it first looks for an `OPENAI_API_KEY` environment variable,  
- if the key is missing, it will ask the user to paste the key interactively,  
- if no key is provided, it will stop with a clear message and refer back to this README.

### 1.3 Representative results

After one full run of the notebook, we obtain:

- a `DataFrame` where each row is one scenario, with at least the following columns:

  - `scenario_id`  
  - `category`  
  - `delta_ref`  
  - `rule_score`  
  - `rule_label`  

  and for each evaluation mode `<mode> in {baseline, guided}`:

  - `<mode>_label`  
  - `<mode>_score`  
  - `<mode>_delta_ground`  
  - `<mode>_delta_outcome`  
  - `<mode>_tension` (this is `T_oversight` for that mode and scenario)  
  - `<mode>_is_correct`  

- a summary dictionary with scalar indicators:

  - `B_baseline` baseline error rate,  
  - `B_guided` guided error rate,  
  - `delta_B = B_baseline - B_guided`,  
  - an aggregate tension contrast `rho_tension` that summarizes how far apart
    the two tension profiles are,  
  - `B_arb` and `T_mean_*` for a simple arbiter that always picks the lower-tension mode.

#### Concrete snapshot from one run

On one concrete run using `gpt-4o-mini` for both modes (8 cases), we observed:

- `B_baseline ≈ 0.125` (1 / 8 cases counted incorrect)  
- `B_guided ≈ 0.250` (2 / 8 cases counted incorrect)  
- `B_arb ≈ 0.125` (arbiter not worse than the better mode)  

and mean tensions:

- `T_mean_baseline ≈ 0.218`  
- `T_mean_guided ≈ 0.303`  
- `T_mean_arb ≈ 0.205`  

The guided rubric does not automatically dominate the baseline on this tiny set.
It slightly over-corrects on some cases, but the `T_oversight` geometry still lets
a simple arbiter pick a mixture of modes that is **no worse than the better one**
while achieving a slightly lower mean tension.

Below are the corresponding terminal snapshot and tension plot.

![Q124 per-case summary (baseline vs guided)](./Q124A.png)

*Per-case summary table. Columns include `rule_score`, `delta_ref`, per-mode labels,
scores, tensions and correctness flags at the effective layer.*

![Q124 baseline vs guided T_oversight per case](./Q124A2.png)

*Baseline vs guided `T_oversight` per case. The curves are close on easy cases,
and diverge modestly on the more difficult or safety-sensitive ones. The arbiter
operates only on these scalar tensions.*

The target qualitative pattern for a successful MVP is not that guided always wins,
but that:

- the geometry makes evaluation drift visible on specific cases,  
- cheap arbitration based on `T_oversight` is already competitive with the better mode,  
- everything is small enough that misbehaviour can be audited line by line.

### 1.4 How to reproduce

1. Open the notebook

   - `TensionUniverse/Experiments/Q124_MVP/Q124_A.ipynb`  
   - or click the Colab badge at the top of this page.

2. Provide an OpenAI API key (only if you want to run it)

   - If you already have `OPENAI_API_KEY` set in your environment, the notebook will use it.  
   - Otherwise, the first code cell will prompt you to paste an API key once.  
   - If you do **not** want to call a live model, you can still read this README
     and inspect the tension geometry design; the experiment will simply not execute.

3. Install dependencies if needed

   - `pandas`, `matplotlib`, `openai`  

   The notebook includes a single `pip` cell that you can run in a clean Colab runtime.

4. Run all cells from top to bottom

   - the script will define the `SCENARIOS`,  
   - run both `baseline` and `guided` evaluators,  
   - compute per-scenario metrics and tension scores,  
   - assemble the `DataFrame`,  
   - print a compact summary block,  
   - and draw a simple tension plot.

5. Inspect the outputs

   - The final cell calls:

     ```python
     results_df, results_summary = run_experiment()
     plot_tension(results_df)
     ```

   - You can scroll to inspect the printed table,  
   - and you can visually compare the two tension curves on the plot.

---

## 2. Experiment B: reserved for future extensions

This section is intentionally left light for the first pass.

Once Experiment A is stable, Experiment B can host a slightly more advanced variant, for example:

- increasing the number or diversity of scenarios,  
- adding a third evaluation mode such as "stacked tools" or "committee oversight",  
- or testing a different definition of `T_oversight` that emphasizes different observables.

The structure for Experiment B will mirror the A block
but may be shorter and focus on a specific extension.

---

## 3. How this MVP fits into the Tension Universe

At the Tension Universe level, Q124 connects several clusters:

- AI alignment and control questions (see Q121 and Q122),  
- interpretability and internal representation questions (Q123),  
- data quality and truth extraction from synthetic worlds (Q127),  
- and social oversight structures that come from complex systems and governance.

This MVP does not try to answer any of the large questions directly.

Instead, it gives a concrete example of:

- how to encode oversight as a finite state space of worlds and modes,  
- how to define a scalar tension functional for an evaluation layer,  
- how to compare different oversight designs by looking at both error rates
  and tension profiles.

The same pattern can be reused across other S-class problems in this pack:

- in some problems, the "worlds" are scientific projects or long-horizon policies,  
- in others, they are synthetic AI tasks or games,  
- but in all cases the oversight layer is treated as a system
  with its own tension geometry, not as a black box.

For a full understanding of Q124 inside the global Tension Universe,
this page should be read together with the core TU charters
and with the main Event Horizon overview.

---

### Charters and formal context

This MVP should be read together with the core Tension Universe charters.

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)  
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)  
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)

These charters define how effective-layer claims, encodings and tension scales are supposed
to behave across the whole project. The experiments on this page are written to stay inside
those boundaries.

---

### Repo link and stars

The full WFGY project, including the Tension Universe experiment pack, lives at:

- https://github.com/onestardao/WFGY

If this experiment or the TU pack is useful to you, a star on the repo makes it easier
for other researchers to discover and audit the work.
