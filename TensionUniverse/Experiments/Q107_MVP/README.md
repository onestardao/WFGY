<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q107 (Large Scale Collective Action).
Role: MVP experiment log for Q107 at the effective layer. Focus on simple
      public goods and coordination games and associated tension observables.
Use: When a user asks about TU Q107 collective action experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q107 MVP: toy large scale collective action

_Status: work in progress. This page records early MVP designs and may change as the TU Q107 program evolves._

> This page sketches simple game based experiments for TU Q107.  
> The aim is to capture collective action tension in transparent toy models.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q107 studies large scale collective action.

We work with toy models such as:

- public goods games,
- threshold contribution games,
- simple coordination games,

with many agents and simple rules.

The MVP experiments here define observables that track tension between:

- individual incentives,
- group outcomes,
- and declared norms or agreements.

---

## 1. Experiment A: public goods game with tension scores

### 1.1 Research question

In a repeated public goods game, can we define a scalar observable T_collective that

- is small when group outcomes and declared norms align,
- grows when individual best responses erode collective provision.

### 1.2 Setup

The notebook will:

- Simulate many agents playing a simple public goods game.

  - Each round, agents decide how much to contribute.
  - Contributions are multiplied and shared.

- Implement different strategy types, for example:

  - unconditional cooperators,
  - free riders,
  - conditional cooperators.

- Define a group norm, such as a target contribution level.

For each simulation record:

- average contribution and variance,
- fraction of free riders,
- distance from the norm.

Define T_collective from:

- the gap between observed contributions and norms,
- group payoff shortfall relative to maximum possible payoff.

### 1.3 Expected pattern

We expect:

- low T_collective when norms are respected and provision is high,
- higher T_collective when free riding dominates and norms fail.

### 1.4 How to reproduce

After `Q107_A.ipynb` is created:

1. Open the notebook.
2. Inspect the definition of strategies and norms.
3. Run simulations for different mixes of agent types.
4. Compare T_collective across scenarios.

---

## 2. Experiment B: coordination with misaligned narratives

### 2.1 Research question

Can we expose coordination failure tension by comparing:

- numerical game outcomes,
- narrative claims about cooperation.

### 2.2 Setup

The notebook will:

- Implement a simple coordination game where agents choose actions that are better when aligned.
- Simulate multiple rounds under different information and communication structures.
- For each scenario produce:

  - numerical measures such as coordination rate,
  - a short textual description.

Ask a language model to:

- assess whether the scenario fits a narrative like "successful large scale cooperation" or "fragmented coordination".

Define T_coord as a function of:

- mismatch between numerical outcomes and narrative labels,
- frequency of coordination failures in scenarios claimed to be cooperative.

### 2.3 Expected pattern

We expect:

- low T_coord when narratives and outcomes align,
- higher T_coord when large scale collective failure hides behind cooperative language.

### 2.4 How to reproduce

Once `Q107_B.ipynb` exists:

- open the notebook and inspect prompts and metrics,
- run scenarios and evaluate T_coord.

---

## 3. How this MVP fits into Tension Universe

TU Q107 treats large scale collective action as a tension between:

- individual and group payoffs,
- norms and actual behavior,
- numerical and narrative views of cooperation.

This MVP provides:

- a public goods game experiment with T_collective,
- a coordination narrative experiment with T_coord.

Both are small and transparent starting points.

For more context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page follows:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
