<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q091 (Equilibrium Climate Sensitivity).
Role: MVP experiment log for Q091 at the effective layer. Focus on small, text-only
      experiments about climate sensitivity reasoning and tension observables.
Use: When a user asks about TU Q091 climate sensitivity experiments or wants runnable
      examples, load this page first, then follow its notebook links.
-->

# TU Q091 MVP: equilibrium climate sensitivity tension slices

_Status: MVP A implemented with a first reference run. MVP B is in design and will be wired into a notebook later._

> This page documents the first effective layer MVP experiments for TU Q091.  
> It does **not** claim that Q091 is solved as a mathematical problem or as a full benchmark.  
> The scripts here are small and fully inspectable. You can re-run them with your own
> OpenAI API key to reproduce the qualitative patterns, but the exact numbers will drift.

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

**Notebooks and assets**

 [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q091_MVP/Q091_A.ipynb)

Screenshots from the first reference run live next to this README:

- `Q091A.png` – synthetic item bank preview  
- `Q091A2.png` – summary table and tension scores  
- `Q091A3.png` – bar plots of `T_ECS_range`  

---

## 0. What this page is about

TU Q091 is the equilibrium climate sensitivity problem inside the Tension Universe.  
In physical terms it asks how much the long-run global mean temperature responds to a doubling of atmospheric CO₂.  
At the effective layer we do not run climate models or work with raw observational datasets.  
We only look at

- how language models reason about climate sensitivity  
- how stable their internal stories are across prompts  
- how much tension appears when narratives drift away from fixed reference windows

This MVP keeps the scope narrow and text-based.

- All inputs are short synthetic descriptions and scenarios.  
- We encode a simple reference window for plausible climate sensitivity values.  
- We define scalar observables that capture inconsistency and narrative drift.

The canonical S-problem statement and the full TU Q091 formalism live in the BlackHole Q091 entry.  
This page is a notebook-style companion that records how the first experiments are set up and what the initial runs look like.

---

## 1. Experiment A: sensitivity ranges and narrative consistency

### 1.1 Research question

If we ask a model to read short climate descriptions and then

- provide a numerical estimate for climate sensitivity, and  
- explain that estimate in natural language,

can we define a scalar observable called `T_ECS_range` that

- stays low when estimates sit inside a fixed reference window and stories match the numbers, and  
- rises when explanations and numeric claims contradict each other.

The objective is to test whether simple climate sensitivity reasoning remains coherent across many prompts, even when the evidence pattern is varied.

---

### 1.2 Setup

At a high level the notebook `Q091_A.ipynb` does the following.

- Uses a single chat model as the underlying engine.  

  - The default is `gpt-4o-mini`.  
  - The model name is set in one place at the top of the notebook and can be edited before running.

- Defines a small synthetic **item bank** of equilibrium sensitivity stories.

  Each item is a short description of a climate evidence pattern.  
  In the reference run, the bank contains eight items:

  - `C01` – Historical warming with multi-line evidence (medium ECS) → bucket `MEDIUM`  
  - `C02` – Paleoclimate strong-response case (high ECS) → bucket `HIGH`  
  - `C03` – Energy-balance study with weak feedbacks (low ECS) → bucket `LOW`  
  - `C04` – Multi-source constraint narrowing around 2.5–3.x °C → bucket `MEDIUM`  
  - `C05` – High-end ensemble member emphasising strong positive feedbacks → bucket `HIGH`  
  - `C06` – Historical-only fit with cautious priors → bucket `MEDIUM`  
  - `C07` – Short-term variability emphasised, but multiple lines of evidence → bucket `MEDIUM`  
  - `C08` – Hypothetical strong-stabilising feedback world → bucket `LOW`

  For each item we record a ground-truth label:

  - a qualitative bucket: `LOW`, `MEDIUM`, or `HIGH` climate sensitivity;  
  - a reference numeric interval `[ecs_min_true, ecs_max_true]`, for example  
    a “medium” item may be assigned 2.0–4.0 °C per CO₂ doubling.

  A static preview of the item bank from the first run is stored as:

  ![TU Q091-A: synthetic item bank](./Q091A.png)

- Fixes a **global reference window** for plausible equilibrium sensitivity values.

  For this MVP the window is a wide interval (for example 0.5–7.0 °C per doubling), editable in the notebook header.  
  Any confidence band that pushes far beyond this window is treated as implausible at the effective layer.

For each item, the protocol has two model-facing steps plus a judge step.

#### Step 1 · Estimate call

The model receives the item text and is asked to output:

- a point estimate `S_est` (in °C per CO₂ doubling);  
- a confidence band `[S_low, S_high]`;  
- a one- to two-paragraph explanation for the estimate.

The notebook parses the answer into structured fields using simple pattern matching.  
If parsing fails, the item is treated as high-tension by default.

#### Step 2 · Consistency probe

A second call receives **only the explanation** from step 1.  
It is asked to state:

- which qualitative bucket (`LOW`, `MEDIUM`, `HIGH`) the explanation suggests;  
- whether the narrative is implicitly leaning toward lower or higher sensitivity within the global window;  
- a short justification.

This step makes the explanation “talk about itself” and exposes hidden inconsistencies, such as a cautious-sounding story attached to an extreme numeric range.

#### Step 3 · Judge aggregation

A judge prompt then compares, for each item:

- the quantitative pieces `(S_est, S_low, S_high)`;  
- the bucket inferred from the explanation;  
- the ground-truth bucket and interval for the item;  
- the global reference window.

From these it emits four scores between 0 and 1:

- `range_plausibility`  
  – how well the confidence band sits inside the global window and overlaps the item’s reference interval.

- `bucket_correctness`  
  – agreement between the bucket implied by the final numeric estimate and the ground-truth bucket.

- `self_consistency`  
  – agreement between the numeric estimate and the bucket implied by the **explanation** text.

- `sharpness`  
  – credit for non-trivial confidence bands: very wide “anything from 0 to 10 °C” bands are penalised even if they formally cover the ground truth.

From these scores the notebook defines a **range tension observable** `T_ECS_range`.  
In plain text:

- `T_ECS_range` increases when `range_plausibility` is low;  
- and when `bucket_correctness` or `self_consistency` are low;  
- it can also get a small penalty when `sharpness` is extremely low.

The relative weights are fixed positive constants chosen in the script  
(for example `b_plaus`, `b_bucket`, `b_self`, `b_sharp`).  
There is no fitting to the current run: changing the model or the item bank uses the same coefficients.

An item is counted as **effective-layer coherent** when:

- the sensitivity estimate falls inside the reference window;  
- the bucket from numbers and the bucket from explanation both match the ground-truth bucket;  
- and `T_ECS_range` falls below a small threshold (currently 0.5 in the reference notebook).

---

### 1.3 Expected pattern (design intent)

Before running, the design intent for `T_ECS_range` was:

- For items that clearly belong to a given bucket, the model should provide estimates in the correct qualitative range and explanations that match the numbers.  
  These should produce **low** `T_ECS_range` and be marked coherent.

- For items near bucket boundaries or with deliberately confusing wording, the model may:

  - give wide or misplaced intervals;  
  - tell stories that sound cautious but attach aggressive numbers;  
  - flip buckets between estimate step and probe step.

  These should have lower plausibility and self-consistency scores and therefore **higher** tension.

Aggregating `T_ECS_range` over many items provides a scalar signal for how stable and self-consistent the climate sensitivity story is under this protocol, for a particular model and prompt.

---

### 1.4 How to reproduce

After `Q091_A.ipynb` is checked in, reproducing Experiment A is:

1. **Open the notebook**

   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q091_MVP/Q091_A.ipynb)

2. **Read the header comments**

   The first cells document:

   - the synthetic item bank (titles, buckets, and reference ranges);  
   - the global ECS window;  
   - the tension coefficients used in `T_ECS_range`.

3. **Decide whether to run live OpenAI calls**

   - If you only want to inspect the design, you can leave the `USE_OPENAI` or `RUN_LIVE_CALLS` flag set to `False`.  
     In this mode, the notebook prints the item bank, the scoring functions, and empty placeholders without making any API calls.

   - If you want a full run, switch the flag to `True` and run the setup cell.  
     In Colab this will open a **secret input field** where you can paste your OpenAI API key at runtime.  
     The key is entered into this input box only. It is not written anywhere in the source code, and it is not printed in any cell output.  
     You should never hard-code the key inside the notebook text or inside this README.

4. **Run the main experiment cell**

   The notebook loops over all items, prints a short log line for each, builds a pandas summary table,  
   and finally renders two simple matplotlib plots:

   - `T_ECS_range` per item;  
   - mean `T_ECS_range` grouped by ground-truth bucket.

5. **Compare with the reference run**

   If your model, prompt, and temperature settings match the reference, your qualitative pattern should be similar even if exact numbers drift.

---

### 1.5 Example reference run (2026-02)

A representative run was carried out on `gpt-4o-mini` with the eight-item bank described above.  
The notebook printed the synthetic item bank, then processed each item with estimate and probe calls, then summarised the scores.

The summary table for that run looked like this:

![TU Q091-A: summary table and tension scores](./Q091A2.png)

Key numbers from the table:

- **Overall statistics**

  - mean `T_ECS_range` ≈ `0.017`  
  - median `T_ECS_range` = `0.000`  
  - coherent item rate = `0.875` (7 out of 8 items)

- **Per-item pattern**

  - Items C01, C03, C04, C05, C06, C07, C08 all had `T_ECS_range = 0.00` and were flagged coherent.  
  - Item C02 (paleoclimate strong-response, high ECS) had  
    `range_plausibility ≈ 0.67`, `bucket_correctness = 1.0`, `self_consistency = 1.0`,  
    leading to `T_ECS_range ≈ 0.13` and a non-coherent flag.

  In plain language: the model’s numbers and stories matched the intended bucket for all items,  
  but in one high-sensitivity case the confidence band pushed too far toward the high end of the global window,  
  and the tension gauge correctly treated it as mildly problematic.

Aggregating by bucket, the same run produced:

- `HIGH` bucket: mean `T_ECS_range` ≈ 0.067 (driven by C02)  
- `MEDIUM` bucket: mean `T_ECS_range` = 0.0 in this sample  
- `LOW` bucket: mean `T_ECS_range` = 0.0 in this sample

The corresponding plots stored in `Q091A3.png` show these patterns visually:

![TU Q091-A: T_ECS_range bar plots](./Q091A3.png)

- The top panel displays `T_ECS_range` for each item id C01–C08.  
  Only C02 shows visible tension; the rest are at zero under this metric.  
- The bottom panel shows mean `T_ECS_range` per ground-truth bucket, highlighting that  
  tension appears only in the `HIGH` bucket for this particular run.

These screenshots are provided as visual context only.  
Future runs with different models or prompts are expected to change the numbers while preserving the basic pattern  
(near-zero tension for self-consistent items, visible spikes when ranges and narratives diverge).

---

## 2. Experiment B: policy narratives under fixed sensitivity constraints

> Status: design-only at this stage. The protocol below describes the intended MVP.  
> A dedicated notebook `Q091_B.ipynb` will be added when the first implementation is ready.

### 2.1 Research question

Equilibrium climate sensitivity links physical constraints and policy narratives.  
Given a fixed sensitivity window and a simple emissions scenario, a model should be able to tell whether a policy story is physically compatible with long-run temperature outcomes.

We ask:

If we feed a model small scenario summaries in which

- a sensitivity range is explicitly stated, and  
- one or more policy narratives are proposed,

can we define a policy tension observable called `T_ECS_policy` that responds when the narrative contradicts basic implications of the stated sensitivity.

---

### 2.2 Planned setup

The B-notebook will construct a small bank of synthetic scenarios.  
Each scenario contains:

- a declared equilibrium sensitivity interval `[S_min, S_max]`;  
- a very simple description of emissions or forcing trajectories over the next century  
  (for example “peaking in 2035 then linearly declining to net-zero by 2080”);  
- one or more policy narratives, such as:

  - “this pathway keeps warming well below two degrees”;  
  - “this pathway stabilizes climate at current levels”;  
  - “this pathway accepts high-risk warming”.

For each scenario an external ground-truth label is prepared by hand:

- `NARRATIVE_REALISTIC` when the narrative matches the rough implications of the sensitivity and trajectory;  
- `NARRATIVE_UNREALISTIC` when the narrative clearly understates or overstates long-run outcomes;  
- a short human justification string.

For each scenario the protocol has two planned steps.

#### Step 1 · Evaluation call

The model receives the scenario and is asked to:

- classify each narrative as realistic or unrealistic at a coarse level;  
- briefly justify each classification in natural language;  
- assign a qualitative risk level (`LOW`, `MEDIUM`, `HIGH`) to the overall pathway.

#### Step 2 · Cross-narrative probe

A follow-up call receives only the justifications and is asked to check for internal contradictions across narratives.  
For example, the probe should detect if the model treats two mutually incompatible stories as simultaneously realistic.

A judge prompt will then assign three scores between 0 and 1 for each narrative:

- `physics_consistency` – agreement between the model verdict and the ground-truth label;  
- `sensitivity_awareness` – whether the justification explicitly uses the stated sensitivity range or simply ignores it;  
- `cross_story_stability` – how well the justifications remain logically compatible when several narratives are present.

From these, the notebook will define a **policy tension observable** `T_ECS_policy`.  
In plain text:

- `T_ECS_policy` increases when `physics_consistency` is low;  
- and when `sensitivity_awareness` or `cross_story_stability` are low.

Narratives where the model approves unrealistic stories or fails to engage with the sensitivity range  
should therefore show higher policy tension even if the prose sounds confident.

---

### 2.3 Intended pattern and future runs

Once implemented, we expect to see:

- For simple and internally consistent scenarios, the model should correctly reject unrealistic narratives and cite the sensitivity window in its reasoning.  
  These cases should show low `T_ECS_policy`.

- For more subtle scenarios, such as relatively high sensitivity paired with optimistic narratives,  
  the model may still mark the story as realistic while barely using the numeric range.  
  These should reduce `sensitivity_awareness` and raise tension.

Aggregating over scenarios will provide a coarse scalar signal for how well policy narratives respect fixed sensitivity constraints at the effective layer.

Reproduction steps for B will mirror Experiment A: open `Q091_B.ipynb`, inspect the scenario definitions, decide whether to supply an API key via runtime prompt, then run and compare your tension statistics with the documented pattern.

---

## 3. How this MVP fits into Tension Universe

The TU Q091 S-problem treats equilibrium climate sensitivity as one axis of physical tension that connects scientific evidence and policy narratives.

This MVP page is a first small step toward that definition at the effective layer.

- **Experiment A** focuses on sensitivity ranges and defines the range tension observable `T_ECS_range` based on internal consistency between numbers, explanations, and a fixed reference window.  
- **Experiment B** (planned) focuses on policy narratives under fixed sensitivity constraints and defines the policy tension observable `T_ECS_policy`.

Both experiments are designed to fit inside single-cell notebooks with roughly 300 lines of code.  
The emphasis is on transparent reasoning that others can inspect, rerun, and modify.

For broader context you can return to:

- [Experiments index](../README.md) for the list of TU experiments;  
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md) for the main entry point and
  narrative overview of the Tension Universe project.

---

### Charters and formal context

This MVP should be read together with the core Tension Universe charters:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)  
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)  
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)

These charters define how effective-layer claims, encodings, and tension scales are supposed
to behave across the whole project. The experiments on this page are written to stay inside
those boundaries.
