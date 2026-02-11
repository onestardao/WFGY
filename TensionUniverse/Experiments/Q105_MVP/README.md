<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q105 (Prediction of Systemic Crashes).
Role: MVP experiment log for Q105 at the effective layer. Focus on small
      networked systems and tension observables for early warning signals.
Use: When a user asks about TU Q105 crash prediction experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q105 MVP: toy systemic crash warnings

_Status: work in progress. This page records early MVP designs and will be updated once first notebooks are stable._

> This page sketches toy experiments for TU Q105.  
> The aim is to show how small networked systems can expose tension
> between local indicators and global crash risk.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q105 looks at prediction of systemic crashes.

Instead of real financial markets or infrastructures we start with toy networks:

- nodes with local balance sheets or loads,
- edges representing exposures or dependencies,
- simple failure rules.

We then define:

- early warning indicators,
- crash outcomes,
- and tension observables when indicators fail to warn.

---

## 1. Experiment A: network contagion and local indicators

### 1.1 Research question

In a simple contagion model on a network, can we define a scalar observable T_warning that

- is small when early warning indicators successfully flag upcoming crashes,
- grows when indicators remain calm but large cascades occur.

### 1.2 Setup

The notebook will:

- Build a random or structured network of nodes.
- Assign each node a simple balance sheet or load variable.
- Define a failure rule where nodes fail when load exceeds a threshold.
- Trigger small shocks at random nodes and propagate failures through the network.

Define early warning indicators such as:

- average load,
- variance of load,
- fraction of nodes close to threshold,
- simple network centrality based risk scores.

For each simulated scenario record:

- whether a large cascade occurred,
- indicator values before the cascade,
- whether a simple rule based on indicators would have flagged risk.

Define T_warning from:

- false negatives where no warning but cascade happens,
- false positives where strong warnings but no cascade,
- calibration mismatch between indicator based risk probability and observed frequency.

### 1.3 Expected pattern

We expect:

- low T_warning for indicator sets that align with actual cascade risk,
- higher T_warning when indicators consistently miss important cascades.

Summary tables and plots will be added after implementation.

### 1.4 How to reproduce

After `Q105_A.ipynb` is added:

1. Open the notebook.
2. Read the description of the network, failure rules and indicators.
3. Run simulations and compute T_warning across parameter sweeps.
4. Inspect which indicators reduce tension and which fail.

---

## 2. Experiment B: model based versus data based risk assessment

### 2.1 Research question

Can we define a tension observable T_model_data that captures when a simple model based risk score disagrees with an empirical data based score.

### 2.2 Setup

Using the same simulation engine, the notebook will:

- Generate datasets of scenarios with:

  - basic features,
  - whether a crash occurred.

- Train a small supervised learner to predict crash probability from features.
- Compare:

  - model based risk scores from the structural indicators,
  - data based risk scores from the learner.

Define T_model_data as a function of:

- divergence between the two risk scores,
- misranking of scenarios by each score relative to true crash outcomes.

### 2.3 Expected pattern

We expect:

- low T_model_data when structural and data based scores agree,
- higher T_model_data when a structural story and empirical patterns diverge.

### 2.4 How to reproduce

Once `Q105_B.ipynb` exists:

- open and inspect the feature definitions,
- train the learner and compute both risk scores,
- compare T_model_data across parameter settings.

---

## 3. How this MVP fits into Tension Universe

TU Q105 treats systemic crash prediction as a tension between:

- local indicators and global outcomes,
- structural models and data based models.

This MVP provides:

- a network contagion toy model with T_warning,
- a model versus data comparison with T_model_data.

Both are designed as inspection friendly notebooks, not real risk systems.

For overall context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page follows:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
