<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q131 (Tension Free Energy).
Role: MVP experiment log for Q131 at the effective layer. Focus on combining
      multiple tension observables into a single free energy style scalar.
Use: When a user asks about TU Q131 free energy experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q131 MVP: tension free energy landscapes

_Status: work in progress. This page records early MVP designs and will be updated as more experiments are added._

> This page sketches first experiments for TU Q131.  
> The goal is to show how multiple tension observables can be combined
> into a single free energy style scalar at the effective layer.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q131 introduces tension free energy.

At a high level:

- many TU problems define local tension observables,
- systems occupy states with different tension profiles,
- we want to define a scalar F_tension that summarizes these into a landscape.

This MVP does not fix a universal formula.
Instead it provides small examples where:

- a few tension observables are defined explicitly,
- they are combined into F_tension in transparent ways,
- landscapes are plotted and interpreted.

---

## 1. Experiment A: combining two tensions in a small system

### 1.1 Research question

Given a toy system with two tension observables, T_1 and T_2, can we define a free energy style scalar F_tension that

- respects basic monotonicity (higher T_1 or T_2 should not reduce F_tension),
- reveals stable and unstable regions in a simple state space.

### 1.2 Setup

The notebook will:

- Choose a small state space, for example a grid of parameters controlling a toy agent.
- For each state compute two previously defined tension observables, for example:

  - T_safety from a Q121 style alignment slice,
  - T_entropy from a Q127 style synthetic world test.

- Define F_tension as a simple function of T_1 and T_2, for example:

  - linear combination with fixed weights,
  - or a soft maximum.

- Plot F_tension over the state space as a heat map.

### 1.3 Expected pattern

We expect:

- regions where both T_1 and T_2 are low to form basins of low F_tension,
- regions where at least one tension is high to stand out as ridges or peaks.

The point is not to fix a unique formula but to illustrate how F_tension can organize local tensions.

### 1.4 How to reproduce

After `Q131_A.ipynb` exists:

1. Open the notebook.
2. Inspect definitions of T_1, T_2 and F_tension.
3. Run the computation and visualize the landscape.
4. Experiment with different combinations and weightings.

---

## 2. Experiment B: trajectory view on a tension landscape

### 2.1 Research question

How do system trajectories look when projected onto a tension free energy landscape, and can we see simple signatures of movement toward or away from low F_tension regions.

### 2.2 Setup

Using the same F_tension from Experiment A, the notebook will:

- define simple update rules for the underlying system state,
- generate trajectories under different policies or interventions,
- track F_tension along each trajectory.

We can then:

- plot trajectories on the parameter grid,
- overlay F_tension as a background,
- plot F_tension versus time.

### 2.3 Expected pattern

We expect:

- trajectories that improve both underlying tensions to move toward low F_tension basins,
- trajectories that trade one tension for another to show characteristic paths and plateaus.

This provides a first visual example of tension free energy in motion.

### 2.4 How to reproduce

Once `Q131_B.ipynb` exists:

- open the notebook,
- inspect state update rules and trajectory generation,
- run the simulations and plot the results.

---

## 3. How this MVP fits into Tension Universe

TU Q131 is a meta problem.

It asks how to combine local tensions into a single scalar that:

- respects core TU charters,
- is meaningful across different problems,
- can be used to compare states and trajectories.

This MVP page is a starting point:

- Experiment A shows how two tensions can be combined into F_tension on a small grid.
- Experiment B shows how trajectories move on that landscape.

Later experiments may integrate more observables and more complex systems.

For broader context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page is written under:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
