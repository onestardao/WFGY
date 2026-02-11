<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q098 (Anthropocene System Dynamics).
Role: MVP experiment log for Q098 at the effective layer. Focus on tiny coupled
      human–Earth toy models and tension observables for Anthropocene trajectories.
Use: When a user asks about TU Q098 Anthropocene experiments or wants runnable
      examples, load this page first, then follow its notebook links.
-->

# TU Q098 MVP: toy Anthropocene trajectories

_Status: work in progress. This page records early MVP designs and will evolve as the TU Q098 program develops._

> This page sketches simple effective layer experiments for TU Q098.  
> The goal is not to predict the real Earth.  
> The goal is to show how tiny coupled human–Earth models can carry
> explicit Anthropocene trajectories and tension observables.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q098 studies Anthropocene system dynamics inside the Tension Universe.

We build tiny coupled systems of:

- human activity variables,
- biophysical state variables,
- and simple feedback rules,

then track how trajectories move relative to declared safe operating spaces.

The MVP experiments here are deliberately small.

- State spaces are low dimensional and fully observable.
- Dynamics are defined by explicit difference equations.
- Tension observables track when trajectories cross declared boundaries or approach critical regions.

---

## 1. Experiment A: three variable Anthropocene toy model

### 1.1 Research question

Can we design a minimal three variable Anthropocene model where:

- one variable represents economic production or energy use,
- one variable represents environmental load,
- one variable represents adaptive capacity,

and define a scalar observable T_anthro that is:

- small when the trajectory stays inside a simple safe operating region,
- larger when it drifts into high load and low capacity combinations.

### 1.2 Setup

The notebook will:

- Define discrete time update rules for three variables, for example

  - X_t: economic output or energy use,
  - E_t: environmental load or cumulative impact,
  - C_t: adaptive capacity or governance strength.

- Include simple feedbacks, such as

  - growth of X_t depends on C_t and environmental damage,
  - E_t accumulates as a function of X_t with partial decay,
  - C_t improves under moderate conditions but degrades under extreme stress.

- Define a rectangular or curved safe operating region in the (E, C) plane.

- Simulate trajectories under different parameter choices:

  - growth focused, regulation weak,
  - balanced policy,
  - overshoot then correction.

- Define a tension observable T_anthro that combines:

  - time spent outside the safe region,
  - maximum distance from the safe region,
  - rate of change when near boundaries.

### 1.3 Expected pattern

Once implemented, we expect to see:

- low T_anthro for trajectories that remain near the safe region or gently return to it,
- higher T_anthro for trajectories that overshoot and stay in high load, low capacity zones.

Plots of trajectories and T_anthro values will be added once the first runs are logged.

### 1.4 How to reproduce

Reproduction steps:

1. Open `Q098_A.ipynb` in this folder.
2. Read the header comments describing the state variables, update rules and safe region.
3. Run the notebook to generate trajectories and compute T_anthro.
4. Compare different policy parameter settings and their tension values.

---

## 2. Experiment B: scenario comparison and narrative tension

### 2.1 Research question

Given a fixed toy model, can we define a narrative level tension observable T_story that captures when a declared scenario narrative is clearly inconsistent with the actual trajectory.

### 2.2 Setup

Using the same model as Experiment A, the notebook will:

- Define simple narrative labels for parameter sets, such as

  - "green growth",
  - "managed descent",
  - "runaway exploitation".

- For each simulated trajectory, build a short textual summary of key events.

- Ask a language model to judge consistency between:

  - the declared narrative label,
  - the observed summary.

- Extract a consistency score in the range 0 to 1.

Define T_story as a function of:

- misclassification between declared label and judged label,
- low consistency scores when the narrative does not fit the trajectory.

### 2.3 Expected pattern

We expect:

- low T_story when labels and trajectories match,
- higher T_story when labels claim stability but trajectories show collapse or overshoot.

This creates a bridge between numerical trajectories and narrative claims at the effective layer.

### 2.4 How to reproduce

Once `Q098_B.ipynb` exists:

- open the notebook,
- inspect how summaries and labels are defined,
- run the narrative evaluation and compare T_story across scenarios.

---

## 3. How this MVP fits into Tension Universe

TU Q098 treats Anthropocene dynamics as a structured tension between

- human driven trajectories,
- planetary boundaries and adaptive capacity,
- and the narratives used to justify or deny those trajectories.

This MVP provides:

- a small three variable model for toy Anthropocene trajectories,
- simple observables T_anthro and T_story that track physical and narrative tension.

The emphasis is on transparency and reproducibility rather than realism.

For more context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page is written under:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
