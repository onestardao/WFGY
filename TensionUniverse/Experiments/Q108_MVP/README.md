<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q108 (Political Polarization).
Role: MVP experiment log for Q108 at the effective layer. Focus on simple
      opinion dynamics models and tension observables for polarization.
Use: When a user asks about TU Q108 polarization experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q108 MVP: toy political polarization

_Status: Experiment A implemented and reproducible. Experiment B planned._

> This page contains the first effective layer MVPs for TU Q108.  
> The goal is to make polarization tension visible in small, fully inspectable models.

**Navigation**

- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q108 looks at political polarization.

Instead of full media ecosystems, we use:

- opinion dynamics on simple graphs,
- modeled exposure to messages,
- and basic update rules that can be inspected line by line.

The MVP experiments define observables that track:

- clustering of opinions,
- distance between groups,
- and mismatch with declared goals like "pluralistic but not polarized".

Experiment A is implemented and runnable.  
Experiment B is a planned extension for information filter design.

---

## 1. Experiment A: bounded confidence on different networks

### 1.1 Question

Can a single bounded confidence model, with the same people and the same update rule, behave very differently **only** because of network structure?

In other words:

- if we fix the initial opinions and the bounded confidence rule,
- and only change the social graph,
- can a scalar observable T_polar clearly separate:

  - a world that de-polarizes into a shared center, from
  - a world that stays locked in two opposing camps.

### 1.2 Model setup

Experiment A uses a deliberately simple toy world.

**Agents**

- N = 200 agents.
- Each agent holds a scalar opinion x in the range [-1, 1].

**Initial opinions (two mild camps)**

- Population is split into two labels: group 0 and group 1.
- Group 0 starts near -0.25 (normal noise, then clipped).
- Group 1 starts near +0.25 (same noise, same clipping).
- So the world begins with a mild left / right split, not full extremes.

**Networks**

We build two social graphs over the same agents:

1. `well_mixed`

   - Erdos–Renyi random graph with edge probability about 0.20.
   - Edges ignore the group labels.
   - Intuition: everyone mixes reasonably freely.

2. `two_communities`

   - Stochastic block model with two communities.
   - High internal linking probability (p_in ≈ 0.40).
   - Very low cross–community probability (p_out ≈ 0.01).
   - Intuition: two tightly knit echo chambers with few bridges.

Every other setting is identical between the two worlds.

**Bounded confidence dynamics**

Time is discrete, t = 0, 1, …, T.

- At each step, for each agent i:

  1. Pick a random neighbor j on the graph (if any).
  2. If the opinion distance |x_j − x_i| is less than or equal to epsilon:

     - move x_i towards x_j by a factor mu.

- Update is asynchronous: agents are visited in random order.
- Parameters in this MVP:

  - T_steps = 120 time steps,
  - mu = 0.5 (halfway step towards the neighbor),
  - epsilons explored: 0.15, 0.25, 0.35, 0.60.

**Polarization observable T_polar**

We partition agents into three groups, using a fixed center threshold:

- left group: opinion < -center_thresh,
- center group: absolute opinion <= center_thresh,
- right group: opinion > center_thresh,

where center_thresh = 0.15 in this MVP.

From this partition we compute:

- p_L: fraction of agents in the left group,
- p_C: fraction of agents in the center,
- p_R: fraction of agents in the right group,
- mu_L: mean opinion in the left group (if non-empty),
- mu_R: mean opinion in the right group (if non-empty),
- gap = absolute difference between mu_R and mu_L.

The scalar polarization tension T_polar is then constructed as

- T_raw = (p_L + p_R) * gap * (1 − p_C),
- T_polar is T_raw capped into the range [0, 1].

Interpretation:

- T_polar is large when

  - many agents sit in the extremes (large p_L + p_R),
  - the two camps are far apart (large gap),
  - the center is small (small p_C).

- T_polar is close to zero when

  - most agents sit near the center,
  - any remaining extremes carry little mass or little separation.

For diagnostics we also store:

- p_center_final = p_C,
- p_extreme_final = p_L + p_R.

### 1.3 Colab notebook (one-click run)

The Experiment A notebook is a single cell script, fully offline, designed for a one-click run.

[![Run Q108_A in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q108_MVP/Q108_A.ipynb)

The notebook will:

1. Build both networks (`well_mixed` and `two_communities`).
2. Initialize opinions with the same two-camp configuration.
3. Run bounded confidence dynamics for each epsilon and each network.
4. Compute T_polar, p_center_final, and p_extreme_final for every run.
5. Save all raw results to:

   - `Q108_A_results.csv`

6. Generate two PNG figures:

   - `Q108_A_polarization_vs_epsilon.png`
   - `Q108_A_opinion_distributions_examples.png`

No API key is required. All randomness is seeded for reproducibility.

### 1.4 Results

#### 1.4.1 Summary table

The table below shows the aggregated statistics (mean over runs) for each network and epsilon.  
T_polar_final_mean is the mean final T_polar. p_center_mean and p_extreme_mean are mean center and extreme fractions.

| network_type   | epsilon | T_polar_final_mean | p_center_mean | p_extreme_mean |
|----------------|---------|--------------------|---------------|----------------|
| two_communities | 0.15   | 0.4712             | 0.037         | 0.963          |
| two_communities | 0.25   | 0.5122             | 0.003         | 0.997          |
| two_communities | 0.35   | 0.5016             | 0.000         | 1.000          |
| two_communities | 0.60   | 0.0000             | 1.000         | 0.000          |
| well_mixed      | 0.15   | 0.4786             | 0.051         | 0.949          |
| well_mixed      | 0.25   | 0.4895             | 0.040         | 0.960          |
| well_mixed      | 0.35   | 0.0508             | 0.895         | 0.105          |
| well_mixed      | 0.60   | 0.0000             | 1.000         | 0.000          |

Key observations:

- At epsilon 0.15 and 0.25, both networks stay in a strongly polarized regime.

  - T_polar around 0.47–0.51.
  - Almost everyone in the extremes, with p_extreme near 0.95–1.00.

- At epsilon 0.35, the networks diverge dramatically:

  - `well_mixed`

    - T_polar drops to about 0.05.
    - Around 89.5 percent of agents return to the center (p_center ≈ 0.895).
    - Only about 10.5 percent remain in the extremes.

  - `two_communities`

    - T_polar remains near 0.50.
    - Center is essentially empty (p_center ≈ 0).
    - All agents stay in extremes (p_extreme = 1.0).

- At epsilon 0.60, both networks fully de-polarize:

  - T_polar returns to 0.
  - Everyone sits in the center.

This means that at epsilon 0.35 we have:

- same agents,
- same initial two-camp opinions,
- same bounded confidence rule,
- same epsilon value,

but the final tension differs by an order of magnitude solely because of network structure.

#### 1.4.2 T_polar as a function of epsilon

The figure below plots T_polar_final_mean versus epsilon for both networks.

![Q108_A · Polarization vs epsilon](./Q108_A_polarization_vs_epsilon.png)

Reading the figure:

- For both networks, small epsilons around 0.15–0.25 keep the world in a high-tension state.
- As epsilon grows, the `well_mixed` network de-polarizes first.

  - T_polar collapses at epsilon 0.35.

- The `two_communities` network remains locked in a strongly polarized state until epsilon is extremely large.

  - Only when epsilon reaches 0.60 does it finally collapse into the center.

In the language of Tension Universe:

- epsilon is a control knob,
- network modularity decides how far that knob actually moves the world.

#### 1.4.3 Opinion distributions at the critical point

The second figure shows final opinion histograms at epsilon 0.35 for both networks.

![Q108_A · Example final opinion distributions](./Q108_A_opinion_distributions_examples.png)

Interpretation:

- `well_mixed, epsilon = 0.35`

  - Almost everyone has moved into a sharp central peak near 0.
  - The histogram is a single narrow spike, matching p_center ≈ 0.895 and T_polar ≈ 0.05.

- `two_communities, epsilon = 0.35`

  - The population remains split into two distinct peaks near -0.25 and +0.25.
  - The center is empty, matching p_center ≈ 0 and T_polar ≈ 0.50.

This figure visualizes the "same rules, different graph" story:

- In a well mixed world, slightly expanding tolerance leads to a shared center.
- In a modular world, the same tolerance leaves everyone locked in two opposing camps.

### 1.5 Interpretation and limitations

**What Experiment A shows**

- A single bounded confidence model, with a fixed set of agents and initial opinions, can produce very different polarization patterns purely by changing network structure.
- T_polar acts as an effective layer observable that:

  - distinguishes between high-tension and low-tension regimes, and
  - makes the effect of epsilon and modularity directly comparable.

At epsilon 0.35:

- well_mixed: low tension, center-heavy world,
- two_communities: high tension, fully polarized world.

This gives TU Q108 a concrete, runnable example of "same world description at the micro level, different effective universe at the tension level".

**Limitations and next knobs**

- The current experiment focuses on mild initial separation (±0.25). More extreme starting points could explore even higher tension regimes.
- Only two network families are used here. Additional topologies (lattices, hubs, random geometric graphs) would extend the coverage.
- T_polar uses one center threshold (0.15). Other thresholds or multi-peak metrics could refine the observable for more complex landscapes.
- Time series of T_polar are logged only for illustrative runs. A full time-resolved analysis is left for future iterations.

---

## 2. Experiment B: information filter design tension (planned)

Experiment B is not yet implemented. It will reuse the same base model and T_polar, but focus on **information filters** as interventions.

### 2.1 Question

Given a social graph and initial opinions, can we treat content feed designs as separate "world builders" and define a tension observable T_filter that captures when a design meant to reduce polarization actually increases it?

The intent is to represent:

- diversity-boosting feeds,
- similarity-boosting feeds,
- random or noise-injecting feeds,

and compare how they move T_polar over time relative to a neutral baseline.

### 2.2 Planned setup

Using the same kind of networks and opinion initialization as Experiment A, the planned notebook `Q108_B.ipynb` will:

- introduce feed filters that bias which neighbors or messages an agent sees,
- run the same bounded confidence dynamics under each filter,
- track T_polar(t) over time.

A candidate T_filter would be:

- T_filter = T_polar(filter) − T_polar(neutral),

optionally weighted by the stated design goal ("reduce polarization", "increase diversity", and so on).

High positive T_filter would indicate a design that secretly amplifies tension despite its stated goal.

### 2.3 Status

- Notebook not yet implemented.
- This section is a placeholder for future work once Q108_B is promoted to MVP.

---

## 3. How TU Q108 fits into Tension Universe

TU Q108 treats political polarization as a tension between:

- individual opinion dynamics,
- network structure and media filters,
- declared goals for pluralism.

Experiment A provides:

- a minimal but fully runnable world,
- a scalar tension observable (T_polar),
- and a clean contrast between "well mixed" and "modular" universes.

Experiment B will extend this by treating filter design itself as a source of tension.

For broader context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page is written under:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
