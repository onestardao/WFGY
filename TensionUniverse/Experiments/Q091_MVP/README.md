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

_Status: work in progress. This page records early MVP designs and will be updated once the first runs are completed._

> This page documents the first effective layer MVP experiments for TU Q091.  
> It does **not** claim that Q091 is solved as a mathematical problem or as a full benchmark.  
> The scripts here are small and fully inspectable. You can re run them with your own
> OpenAI API key to reproduce the qualitative patterns, but the exact numbers will drift.

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q091 is the equilibrium climate sensitivity problem inside the Tension Universe.  
In physical terms it asks how much the long run global mean temperature responds to a doubling of atmospheric CO2.  
At the effective layer we do not run climate models or work with raw observational datasets.  
We only look at

- how language models reason about climate sensitivity  
- how stable their internal stories are across prompts  
- how much tension appears when narratives drift away from fixed reference windows

This MVP keeps the scope narrow and text based.

- All inputs are short synthetic descriptions and scenarios.  
- We encode a simple reference window for plausible climate sensitivity values.  
- We define scalar observables that capture inconsistency and narrative drift.

The canonical S problem statement and the full TU Q091 formalism live in the BlackHole Q091 entry.  
This page is a notebook style companion that records how the first experiments are set up.

---

## 1. Experiment A: sensitivity ranges and narrative consistency

### 1.1 Research question

If we ask a model to read short climate descriptions and then

- provide a numerical estimate for climate sensitivity, and  
- explain that estimate in natural language,

can we define a scalar observable called `T_ECS_range` that

- stays low when estimates sit inside a fixed reference window and stories match the numbers, and  
- rises when explanations and numeric claims contradict each other.

The objective is to test whether simple climate sensitivity reasoning remains coherent across many prompts.

### 1.2 Setup

At a high level the notebook will do the following.

- Use a single chat model as the underlying engine.  

  The default version in the code will use `gpt-4o-mini`, but the model name can be edited
  in one place at the top of the cell.

- Define a small synthetic item bank.

  Each item is a short description of a climate evidence pattern.  
  Examples include

  - a stylized summary of historical warming and forcing  
  - a stylized summary of model ensemble behavior  
  - a stylized summary of paleoclimate constraints

  For each item we record a ground truth label

  - a qualitative bucket: `LOW`, `MEDIUM` or `HIGH` climate sensitivity  
  - a reference numeric interval such as S between 1.5 and 3.0 degrees Celsius for a `MEDIUM` item

- Fix a global reference window for plausible equilibrium sensitivity values.  

  For example we may pick a wide interval [S_min, S_max] that is treated as the physically reasonable support.

- For each item the protocol has two steps.

  1. **Estimate step**  

     The model receives the item text and is asked to output

     - a point estimate S_est (degrees Celsius per CO2 doubling)  
     - a confidence band [S_low, S_high]  
     - a one or two paragraph explanation for the estimate

  2. **Consistency probe**  

     A second call receives only the explanation and is asked to state

     - which qualitative bucket (`LOW`, `MEDIUM`, `HIGH`) the explanation suggests  
     - whether the narrative prefers lower or higher sensitivity inside the reference window

- A judge prompt then compares, for each item,

  - the quantitative estimate (S_est, S_low, S_high)  
  - the bucket inferred from the explanation  
  - the ground truth bucket and interval for the synthetic item  
  - the fixed global reference window

The judge outputs four scores between 0 and 1.

- `range_plausibility` measures how well the confidence band sits inside the global window.  
- `bucket_correctness` measures agreement between the inferred bucket and the ground truth bucket.  
- `self_consistency` measures agreement between the numeric estimate and the bucket implied by the explanation.  
- `sharpness` rewards non trivial but still plausible confidence bands.

From these scores the notebook defines a range tension observable `T_ECS_range`.  
In plain text:

- `T_ECS_range` increases when range_plausibility is low  
- and when bucket_correctness or self_consistency are low  

The weights that decide how strongly each term contributes are simple positive constants inside the script  
(for example `b_plaus`, `b_bucket`, `b_self`).

Samples are treated as effective layer coherent when

- climate sensitivity estimates fall inside the reference window, and  
- both bucket correctness and self consistency scores are high enough to keep `T_ECS_range` below a threshold.

### 1.3 Expected pattern (to be confirmed by runs)

After the notebook is implemented and run we expect to see patterns such as:

- For items that clearly belong to a given bucket the model should provide estimates in the correct qualitative range and explanations that match the numbers.  
  These will produce low `T_ECS_range`.

- For items near boundaries or with deliberately confusing wording the model may

  - give wide or misplaced intervals  
  - tell stories that sound cautious but attach aggressive numbers  
  - flip buckets between estimate step and probe step

  These will have lower plausibility and self consistency scores and therefore higher tension.

Aggregating `T_ECS_range` over many items gives a scalar signal for how stable and honest the climate sensitivity story is under this protocol.  
This section will be updated with concrete tables and plots after the first runs are logged.

### 1.4 How to reproduce

After the notebook is checked in, reproducing Experiment A will be as simple as:

1. Opening the Q091 range reasoning MVP notebook in this folder.

   - GitHub notebook: `Q091_A.ipynb` (to be added)  
   - Colab entry point: a standard Colab badge link pointing to the same file.

2. Reading the header comments to see the synthetic item bank, the bucket definitions and the metrics.  
3. Deciding whether to run live calls.

   - For design inspection it is enough to read the code and static examples.  
   - For fresh numbers you can paste an OpenAI API key when prompted and let the notebook
     loop over all items.

4. Comparing your run with the documented pattern once the first results are added here.

---

## 2. Experiment B: policy narratives under fixed sensitivity constraints

### 2.1 Research question

Equilibrium climate sensitivity links physical constraints and policy narratives.  
Given a fixed sensitivity window and a simple emissions scenario, a model should be able to tell whether a policy story is physically compatible with long run temperature outcomes.

We ask:

If we feed a model small scenario summaries in which

- a sensitivity range is explicitly stated, and  
- one or more policy narratives are proposed,

can we define a policy tension observable called `T_ECS_policy` that responds when the narrative contradicts basic implications of the stated sensitivity.

### 2.2 Setup

The notebook will construct a small bank of synthetic scenarios.  
Each scenario contains:

- a declared equilibrium sensitivity interval [S_min, S_max]  
- a very simple description of emissions or forcing trajectories over the next century  
- one or more policy narratives, for example

  - "this pathway keeps warming well below two degrees"  
  - "this pathway stabilizes climate at current levels"  
  - "this pathway accepts high risk warming"

For each scenario an external ground truth label is prepared by hand.

- `NARRATIVE_REALISTIC` when the narrative matches the rough implications of the sensitivity and trajectory  
- `NARRATIVE_UNREALISTIC` when the narrative clearly understates or overstates long run outcomes  
- an additional text field giving a short human justification

For each scenario the protocol has two steps.

1. **Evaluation step**  

   The model receives the scenario and is asked to

   - classify each narrative as realistic or unrealistic at a coarse level  
   - briefly justify each classification in natural language  
   - give a qualitative risk level such as `LOW`, `MEDIUM`, `HIGH`

2. **Cross narrative probe**  

   A follow up call receives only the justifications and is asked to check for internal contradictions across narratives.  
   For example the probe may detect if the model says that two incompatible stories are both realistic.

A judge prompt then assigns three scores between 0 and 1 for each narrative.

- `physics_consistency` measures agreement between the model verdict and the ground truth label.  
- `sensitivity_awareness` measures whether the justification actually uses the stated sensitivity range in its reasoning.  
- `cross_story_stability` measures how well the justifications remain logically compatible when several narratives are present.

From these scores the notebook defines a policy tension observable `T_ECS_policy`.  
In plain text:

- `T_ECS_policy` increases when physics_consistency is low  
- and when sensitivity_awareness or cross_story_stability are low  

Again the exact weights (for example `d_phys`, `d_sens`, `d_cross`) are fixed positive constants chosen in the code.

Narratives where the model approves unrealistic stories or ignores the stated sensitivity range will have higher tension.

### 2.3 Expected pattern (to be confirmed by runs)

Once implemented we expect to see:

- For simple and internally consistent scenarios the model should correctly reject unrealistic narratives and give explanations that reference the sensitivity range.  
  These will show low `T_ECS_policy`.

- For more subtle scenarios, such as ones with relatively high sensitivity and optimistic narratives,  
  the model may still mark the story as realistic without engaging with the numeric range.  
  These will reduce sensitivity awareness and raise tension.

Aggregating over scenarios gives a coarse scalar signal for how well policy narratives respect fixed sensitivity constraints at the effective layer.  
This section will be updated with concrete tables and plots once the first working runs are available.

### 2.4 How to reproduce

The reproduction steps will mirror Experiment A.

- Open the `Q091_B.ipynb` notebook once it exists.  
- Inspect the scenario definitions and the way sensitivity ranges and narratives are encoded.  
- Run the protocol and compare your tension statistics with the documented pattern.

---

## 3. How this MVP fits into Tension Universe

The TU Q091 S problem treats equilibrium climate sensitivity as one axis of physical tension that connects scientific evidence and policy narratives.

This MVP page is a first small step toward that definition at the effective layer.

- Experiment A focuses on sensitivity ranges and defines the range tension observable `T_ECS_range`.  
- Experiment B focuses on policy narratives under fixed sensitivity constraints and defines the policy tension observable `T_ECS_policy`.

Both experiments are designed to fit inside single cell notebooks with roughly 300 lines of code.  
The emphasis is on transparent reasoning that others can inspect, rerun and modify.

For broader context you can return to

- [Experiments index](../README.md) for the list of TU experiments.  
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md) for the main entry point and
  narrative overview of the Tension Universe project.

---

### Charters and formal context

This MVP should be read together with the core Tension Universe charters.

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)  
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)  
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)

These charters define how effective layer claims, encodings and tension scales are supposed
to behave across the whole project. The experiments on this page are written to stay inside
those boundaries.
