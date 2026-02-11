<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q101 (Equity Premium Puzzle).
Role: MVP experiment log for Q101 at the effective layer. Focus on tiny
      consumption based models and tension observables between predicted and observed premia.
Use: When a user asks about TU Q101 equity premium experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q101 MVP: toy equity premium tension

_Status: work in progress. This page records early MVP designs and will be updated after the first notebooks run._

> This page sketches toy experiments for TU Q101.  
> The goal is to encode the equity premium puzzle as a tension between
> simple models and simple observed targets, not to resolve real markets.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q101 looks at the equity premium puzzle as a structured mismatch between

- predicted premia from simple asset pricing models, and
- empirical target bands for long run equity premia.

The MVP here uses small simulated economies with:

- consumption processes,
- risk free and risky assets,
- representative agents with utility functions,

and tracks tension observables when the model cannot match observed premia without extreme parameters.

---

## 1. Experiment A: simple consumption based asset pricing model

### 1.1 Research question

If we build a minimal consumption based asset pricing model, can we define a scalar observable T_premium that

- is small when predicted equity premia and volatility sit inside a plausible band,
- and increases as the model requires extreme risk aversion or unrealistic parameters.

### 1.2 Setup

The notebook will:

- Simulate a simple consumption growth process over many periods.
- Define two assets:

  - a risk free asset with fixed return,
  - a risky asset with return tied to consumption growth.

- Use a basic power utility or similar to compute implied prices.
- From these, derive

  - the implied equity premium,
  - volatility of returns,
  - required risk aversion parameter to match a chosen target premium.

Define T_premium using:

- the squared deviation between implied and target equity premium,
- penalties for risk aversion parameters outside a reasonable range,
- penalties when volatility patterns are inconsistent with empirical targets.

### 1.3 Expected pattern

We expect:

- toy configurations that generate plausible premia with reasonable parameters to have lower T_premium,
- toy configurations that only match observed premia with extreme risk aversion to have higher T_premium.

The point is to show an explicit tension between model structure and target bands, even in a simple setup.

### 1.4 How to reproduce

After `Q101_A.ipynb` is created:

1. Open the notebook.
2. Read the header comments describing the consumption process, assets and parameter ranges.
3. Run the simulation and compute T_premium across parameter sweeps.
4. Inspect the table of results and plots.

---

## 2. Experiment B: narrative models versus numerical models

### 2.1 Research question

Can we use a language model to evaluate narrative explanations for the equity premium
and compare them against the toy numerical model, defining a narrative tension observable T_narrative.

### 2.2 Setup

The notebook will:

- Generate a small set of narrative hypotheses, for example

  - rare disasters,
  - habit formation,
  - institutional constraints.

- For each configuration of the toy numerical model, produce a short summary describing its mechanism.
- Ask a language model to judge which narrative hypothesis best fits the numerical summary.
- Extract consistency scores.

Define T_narrative as a function of:

- mismatch between assigned narrative and true simulated mechanism,
- low consistency scores.

### 2.3 Expected pattern

We expect:

- lower T_narrative when numerical mechanisms and selected narratives match,
- higher T_narrative when narratives and numerical structure disagree.

This bridges TU Q101 with narrative level explanations at the effective layer.

### 2.4 How to reproduce

Once `Q101_B.ipynb` exists:

- open the notebook,
- inspect the narrative set and prompt format,
- run the evaluation and compare T_narrative across scenarios.

---

## 3. How this MVP fits into Tension Universe

TU Q101 treats the equity premium puzzle as a tension between

- simple asset pricing models,
- empirical target bands,
- and narrative explanations.

This MVP page provides:

- a minimal numerical experiment with T_premium,
- a minimal narrative experiment with T_narrative.

Both are meant as starting points, not as final economic models.

For the broader project:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

The design of this MVP follows:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
