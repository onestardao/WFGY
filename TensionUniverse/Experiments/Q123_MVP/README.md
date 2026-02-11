<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q123 (Scalable Interpretability).
Role: MVP experiment log for Q123 at the effective layer. Focus on small, repeatable
      interpretability tests and tension observables that scale across many prompts.
Use: When a user asks about TU Q123 interpretability experiments or wants runnable
      examples, load this page first, then follow its notebook links.
-->

# TU Q123 MVP: scalable interpretability slices

_Status: work in progress. This page records early MVP designs and will be updated once the first runs are completed._

> This page documents the first effective layer MVP experiments for TU Q123.  
> It does **not** claim that Q123 is solved as a mathematical problem or as a full benchmark.  
> The scripts here are small and fully inspectable. You can re run them with your own
> OpenAI API key to reproduce the qualitative patterns, but the exact numbers will drift.

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q123 is the scalable interpretability problem inside the Tension Universe.  
Instead of trying to read every internal neuron we focus on questions like

- can we ask the model to expose its own internal structure in a stable way  
- can we define observables that track whether explanations match behavior  
- can we do this across many prompts without blowing up the experiment size

This MVP keeps the scope narrow.

- Everything lives at the effective layer in text.  
- We only use small synthetic tasks and short reasoning traces.  
- We aim for single cell notebooks with roughly 300 lines of code.

The canonical S problem statement and the full TU Q123 formalism live in the BlackHole Q123 entry.  
This page is a notebook style companion that records how the first experiments are set up.

---

## 1. Experiment A: concept explanations versus behavior

### 1.1 Research question

If we ask a model to both

- classify simple synthetic inputs, and  
- explain its decisions in terms of a small concept vocabulary,

can we define a scalar observable called `T_concept` that

- is low when the stated concepts and the behavior match, and  
- rises when the behavior changes but the explanations stay the same story.

The goal is not to recover neurons.  
The goal is to see whether the model can keep its own story straight across simple distribution shifts.

### 1.2 Setup

At a high level the notebook will do the following.

- Use a single chat model as the underlying engine.  

  The default version in the code will use `gpt-4o-mini`, but the model name can be edited
  in one place at the top of the cell.

- Define a small bank of synthetic items.

  Each item is a short description that is easy to tag with a few coarse concepts.  
  For example, we can build a toy dataset of product reviews where each sample is labelled by

  - sentiment: `POSITIVE` or `NEGATIVE`  
  - price level: `LOW` or `HIGH`  
  - risk tag: `SAFETY_CONCERN` or `NO_SAFETY_CONCERN`

  The dataset is small enough to inspect by hand.

- Define a concept vocabulary at the effective layer.

  The vocabulary is a list of concept names and short textual definitions.  
  The same vocabulary is used in prompts, explanations and evaluation.

- Run a two step protocol for each sample.

  1. A **prediction call** where the model receives the item text and is asked to output

     - the three labels, and  
     - a one line explanation that mentions which concepts were important.

  2. A **probe call** where the model receives only its own explanation and is asked to
     reconstruct the labels again.

- A judge prompt then compares

  - the original labels  
  - the labels implied by the explanation alone  
  - and any inconsistencies between them

The judge outputs three quantities for each sample.

- `behavior_accuracy` between 0 and 1 for the original prediction task  
- `explanation_consistency` between 0 and 1 that measures how well the explanation supports the labels  
- `story_stability` between 0 and 1 that measures how similar the labels are when reconstructed from the explanation

From these we define a concept tension observable called `T_concept`.  
In plain text:

- `T_concept` increases when `explanation_consistency` is low  
- `T_concept` increases when `story_stability` is low  

The relative strengths of these two terms are controlled by fixed positive weights inside the script  
(for example `a_gap` for the consistency gap and `a_stab` for the stability gap).  
There is no fitting to current runs.

The effective layer is treated as interpretable on a sample when

- `behavior_accuracy` is high, and  
- both consistency and stability scores are high enough to keep `T_concept` below a threshold.

### 1.3 Expected pattern (to be confirmed by runs)

After the notebook is implemented and run we expect to see patterns like the following.

- On easier items the model should classify correctly and give explanations that are
  sufficient to reconstruct the labels.  
  These will show low `T_concept`.

- On boundary cases where the item is ambiguous the model may

  - flip behavior between runs, or  
  - re use generic explanations that do not track the actual decision.

  These will show reduced consistency and stability and higher tension.

If we aggregate over many items the mean `T_concept` can serve as a scalar signal for how honest and stable the explanations are under the protocol.  
This section will be updated with concrete tables and small plots once the first runs are logged.

### 1.4 How to reproduce

After the notebook is checked in, reproducing Experiment A will be as simple as:

1. Opening the concept explanation MVP notebook in this folder.

   - GitHub notebook: `Q123_A.ipynb` (to be added)  
   - Colab entry point: a standard Colab badge link pointing to the same file.

2. Reading the header comments to see the dataset, the concept vocabulary and the metrics.  
3. Deciding whether to run live calls.

   - For design inspection it is enough to read the code and static examples.  
   - For fresh numbers you can paste an OpenAI API key when prompted and let the notebook
     loop over all samples.

4. Comparing your run with the documented pattern once the first results are added here.

---

## 2. Experiment B: contrastive feature probes in text

### 2.1 Research question

Experiment A looks at explanations as short stories.  
Experiment B looks at contrastive probes.

We ask:

If we present pairs of minimally different inputs that differ in one concept,  
can we treat the model itself as a kind of feature probe by

- asking it which concept changed, and  
- measuring whether the stated change matches the behavioral change.

Again, everything lives in text at the effective layer.

### 2.2 Setup

The notebook will build a small bank of contrastive pairs.

- Each pair `(x_base, x_alt)` differs in one controlled way.  
  For example

  - price goes from `LOW` to `HIGH` while sentiment stays positive, or  
  - a harmless product description gains a safety concern.

- For each input we record ground truth labels under the same concept vocabulary as Experiment A.

The protocol for each pair follows three steps.

1. **Behavior step**  

   The model receives both inputs in a fixed format and is asked to output the labels for each.

2. **Contrastive explanation**  

   The model is then asked a separate question of the form

   > Between example A and example B, which high level concepts changed and why.

   It must answer using only the shared vocabulary and name the concepts it thinks changed.

3. **Probe step**  

   A probe call receives only the contrastive explanation and must state which labels changed.

A judge prompt reduces this to numeric quantities.

- `label_delta_correct` between 0 and 1, which scores whether the predicted label changes match ground truth  
- `concept_delta_correct` between 0 and 1, which scores whether the stated concept changes match the true design  
- `delta_alignment` between 0 and 1, which scores how well concept changes and label changes line up

The contrastive interpretability tension is called `T_contrast`.  
In plain text:

- `T_contrast` increases when `label_delta_correct` is low  
- `T_contrast` increases when `concept_delta_correct` is low  
- `T_contrast` increases when `delta_alignment` is low  

The relative weights of these penalties are fixed positive constants in the code  
(for example `c_lbl`, `c_cpt`, `c_ali`). There is no fitting to the current run.

Pairs where behavior and stated features drift apart will have higher `T_contrast`.

### 2.3 Expected pattern (to be confirmed by runs)

After implementation we expect to see:

- For simple and clean manipulations the model will correctly track both label and concept changes.  
  These will have low tension.

- For more subtle manipulations, for example small wording changes that carry hidden safety implications,  
  behavior may change without corresponding shifts in the stated concepts.  
  These will push `T_contrast` higher.

Aggregating over many pairs will give a rough scalar that indicates how well contrastive explanations scale.  
This section will be updated with concrete tables and small plots once the first runs are available.

### 2.4 How to reproduce

The reproduction steps will mirror Experiment A.

- Open the `Q123_B.ipynb` notebook once it exists.  
- Inspect the way contrastive pairs are built and how the vocabulary is enforced.  
- Run the protocol and compare your tension statistics with the documented pattern.

---

## 3. How this MVP fits into Tension Universe

The TU Q123 S problem treats scalable interpretability as a structured notion of tension between

- what a model says about its own internal concepts, and  
- how it actually behaves across large sets of prompts.

This MVP page is a first small step toward that definition at the effective layer.

- Experiment A focuses on single item explanations and uses the concept tension observable `T_concept`.  
- Experiment B focuses on contrastive pairs of inputs and uses the contrastive tension observable `T_contrast`.

Both experiments are designed to sit inside single cell notebooks with roughly 300 lines of code.  
The emphasis is on stable patterns that other people can replicate and modify.

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
