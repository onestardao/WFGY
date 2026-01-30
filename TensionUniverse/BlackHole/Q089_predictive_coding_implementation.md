<!-- QUESTION_ID: TU-Q089 -->
# Q089 · Implementation of predictive coding in biological brains

## 0. Header metadata

```txt
ID: Q089
Code: BH_NEURO_PREDICTIVE_CODE_L3_089
Domain: Neuroscience
Family: Systems neuroscience / theoretical neuroscience
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open problem (partial evidence, no implementation consensus)
Semantics: hybrid (discrete events summarized into continuous effective fields)
E_level: E1
N_level: N1
Last_updated: 2026-01-30
````

---

## 0. Effective layer disclaimer

All content in this entry is restricted to the **Tension Universe effective layer**.

* The goal is to specify an **effective-layer encoding** of Q089, including:

  * a state space for predictive coding implementations,
  * admissible encodings from data into that state space,
  * tension functionals and mismatch scores,
  * falsifiable experiment templates,
  * and reusable components for other BlackHole problems and AI systems.

* This document **does not**:

  * claim to prove or disprove the canonical statement of Q089,
  * assert that biological brains do or do not implement predictive coding in any deep or fundamental sense,
  * introduce new theorems beyond what is already established in the cited literature,
  * define or expose any Tension Universe bottom-level axiom system or generative rules.

* All objects in this entry (for example `M`, `E_PC`, observables, mismatch measures, `Tension_PC`, `T_ij`, counterfactual worlds) are:

  * effective constructs,
  * defined only up to the requirements stated in this file,
  * and interpreted as tools for structuring experiments and reasoning at the effective layer.

* Domain boundary:

  * Tension analysis is only defined on the regular domain `M_reg` introduced in Section 3.5.
  * States in the singular set `S_sing` are treated as **out of domain** for Q089 tension analysis.
  * Out-of-domain outcomes are not counted as evidence for or against predictive coding as an implementation hypothesis.

For the general rules governing effective-layer scope, encoding and fairness constraints, and tension scales, this page should be read together with the Tension Universe charters listed in the footer.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q089 can be phrased as follows:

> Predictive coding proposes that the brain implements a hierarchical generative model in which top down predictions are continuously compared with bottom up sensory signals, and only prediction errors are propagated forward. The open question is: **how, if at all, is this architecture concretely implemented in biological neural circuits?**

More precisely:

1. There are formal predictive coding (PC) schemes in theoretical neuroscience, which specify:

   * distinct populations encoding predictions and prediction errors,
   * specific patterns of feedforward and feedback connectivity,
   * precision weighting of errors,
   * local update rules that approximate Bayesian or variational inference.

2. There are also empirical observations in real brains:

   * layered cortical microcircuit structure,
   * long-range feedback and feedforward connections,
   * context and expectation effects on neural responses,
   * neuromodulatory control of gain and variance.

The canonical Q089 problem is to determine whether there exists a coherent mapping at the effective layer between:

* the formal predictive coding architecture, and
* the measurable properties of biological neural circuits,

such that we can reasonably claim that predictive coding (or a close approximation of it) is implemented in the brain, rather than being merely a useful metaphor or high-level description.

### 1.2 Status and difficulty

Current knowledge at the effective layer can be summarized as:

* There is strong conceptual appeal and some empirical support for predictive coding and more general predictive processing theories, including:

  * contextual modulation of sensory responses,
  * mismatch responses and prediction error signals,
  * hierarchical and feedback-rich cortical anatomy.

* However, the precise **implementation details** remain controversial:

  * It is not fully agreed which neurons encode predictions versus errors.
  * It is unclear how closely biological local microcircuits implement the update equations of standard PC algorithms.
  * Alternative interpretive frameworks (for example efficient coding, attractor dynamics, energy-based models, or other forms of hierarchical inference) can sometimes explain similar data.

As a result, there is no consensus that predictive coding, in the strict algorithmic form proposed by canonical models, is literally implemented by cortical microcircuits. The problem is widely regarded as deep and structurally hard, because it sits at the intersection of:

* systems neuroscience,
* computational neuroscience,
* cognitive science and philosophy of mind.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q089 plays several roles:

1. It is a central **neuro-cognitive implementation** problem, connecting abstract theories of brain computation to circuit-level realizations.
2. It is a key bridge between:

   * Q083 (neural coding and population codes),
   * Q085 (learning and plasticity rules),
   * Q086 (functions of sleep and offline processing),
   * Q087 (neurodegenerative and psychiatric disorders as failures of prediction and error handling).
3. It provides a reference pattern for how Tension Universe handles:

   * algorithmic theories of brain function,
   * their possible biological instantiations,
   * and consistency tension between the two.

### References

1. K. Friston, “A theory of cortical responses,” Philosophical Transactions of the Royal Society B, 360(1456), 815–836, 2005.
2. R. P. N. Rao and D. H. Ballard, “Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects,” Nature Neuroscience, 2(1), 79–87, 1999.
3. A. Clark, “Whatever next? Predictive brains, situated agents, and the future of cognitive science,” Behavioral and Brain Sciences, 36(3), 181–253, 2013.
4. M. Spratling, “A review of predictive coding algorithms,” Brain and Cognition, 112, 92–97, 2017.

---

## 2. Position in the BlackHole graph

This block records how Q089 is positioned among Q001–Q125. Each edge includes a one line reason tied to concrete components or tension types.

### 2.1 Upstream problems

These provide prerequisites, tools, or general frameworks for Q089.

* Q083 (BH_NEURO_CODE_L3_083)
  Reason: Supplies general frameworks for population codes and representational formats that are reused to describe predictive and error-coding populations.

* Q085 (BH_NEURO_PLASTICITY_RULES_L3_085)
  Reason: Provides candidate synaptic update rules and local learning operators used to instantiate predictive coding algorithms in biological synapses.

* Q088 (BH_NEURO_DEV_PATTERN_L3_088)
  Reason: Describes developmental patterning and constraints that shape which predictive coding architectures are even realizable in real brains and which geometries are permitted for hierarchical maps.

### 2.2 Downstream problems

These use Q089 components or depend on its tension structure.

* Q081 (BH_NEURO_CONSCIOUS_HARD_L3_081)
  Reason: Reuses Q089 predictive_implementation_tension components to examine whether conscious experiences correlate with predictive coding regimes.

* Q086 (BH_NEURO_SLEEP_FUNC_L3_086)
  Reason: Uses Q089 offline_prediction_update patterns to analyze whether sleep supports predictive model refinement.

* Q087 (BH_NEURO_DEGEN_DISEASE_L3_087)
  Reason: Applies Q089 error_precision_mismatch descriptors to characterize how neurodegenerative and psychiatric conditions might involve mis-weighted prediction errors.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q082 (BH_NEURO_MEMORY_CONSOL_L3_082)
  Reason: Both Q089 and Q082 deal with long-range consistency between representational dynamics and behavioral outcomes under consistency_tension.

* Q090 (BH_NEURO_DEFAULT_MODE_L3_090)
  Reason: Both examine large-scale neural dynamics as implementations of internal generative activity, one via predictive coding, the other via default mode network structure.

### 2.4 Cross-domain edges

Cross-domain nodes reuse Q089 components in other domains.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses predictive_implementation_tension ideas to study algorithmic implementations of prediction and compression in artificial systems under resource constraints.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Reuses predictive_coding_block templates as interpretability modules for artificial neural networks.

* Q124 (BH_AI_AGENT_MODELS_L3_124)
  Reason: Uses Q089 hierarchical_prediction_descriptor to define agent architectures based on internal predictive models.

---

## 3. Tension Universe encoding (effective layer)

All content in this block stays strictly at the effective layer. We describe:

* state space,
* observables and effective fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden TU generative rules or any mapping from raw biological data to internal TU bottom-level fields.

### 3.1 State space and admissible encodings

We assume a semantic state space

```txt
M
```

with the following interpretation:

* Each element `m` in `M` represents a **predictive-coding configuration** for a given brain system and time window, including:

  * a coarse-grained description of hierarchical neural populations,
  * effective variables for prediction signals and prediction error signals,
  * effective synaptic strength patterns for feedforward and feedback connections,
  * effective variables representing precision or gain on error signals,
  * coarse resource usage measures such as metabolic cost proxies.

We introduce an admissible encoding class `E_PC` with the following properties:

1. Each encoding `E` in `E_PC` maps raw experimental data (for example spikes, voltages, imaging signals) plus task metadata to states `m` in `M`.

2. The map is fixed before any evaluation of predictive coding tension and does not adapt per dataset to minimize tension. Formally:

   ```txt
   For all E in E_PC and for all datasets D,
   m = E(D) is determined without access to Tension_PC(m).
   ```

3. Each encoding `E` in `E_PC` uses a finite library of features and scales:

   * a finite set `L_reg` of region definitions (for example cortical areas or laminar compartments),
   * a finite set `L_time` of time window templates,
   * a finite set `L_feature` of summary statistics (for example averages, variances, cross-correlations).

4. For practical use, there is a **finite encoding registry**:

   * For any specific experimental program, the investigator pre-registers a finite set of concrete encodings
     `Registry_PC = {E_1, E_2, ..., E_K} ⊂ E_PC`.
   * For each analysis, one `E_k` is selected from this registry and its identity is logged.
   * New encodings added after seeing data define a **new versioned registry**, not a silent update of the old one.

5. All observables and mismatch measures defined below depend only on:

   * the outputs of `E`,
   * the finite libraries that are declared for Q089,
   * and the fixed parameters of this entry.

This prevents free adjustment of the encoding to match desired tension values.

We do not specify how elements of `E_PC` are implemented. We only assume that at least some elements are empirically realizable with current or future experimental techniques.

### 3.2 Effective fields and observables

Given a state `m` in `M`, we define the following observables. All observables are interpreted with the **hybrid semantics** from the header metadata: discrete neural events and micro signals are summarized into continuous effective fields.

1. Hierarchical representation field

```txt
R_level(m; l, r)
```

* Input: state `m`, level index `l` (for example cortical hierarchy level), region `r` in `L_reg`.
* Output: an effective vector summarizing the representational activity at level `l` in region `r` during the time window of `m`.

2. Prediction error field

```txt
E_level(m; l, r)
```

* Input: state `m`, level index `l`, region `r`.
* Output: an effective scalar or vector summarizing the strength of prediction error signals at that level and region.

3. Precision or gain field on errors

```txt
Pi_level(m; l, r)
```

* Input: state `m`, level index `l`, region `r`.
* Output: an effective scalar summarizing the gain or precision weighting applied to error signals.

4. Connectivity pattern descriptors

```txt
C_ff(m; l, r_src, r_tgt)
C_fb(m; l, r_src, r_tgt)
```

* Inputs: state `m`, level index `l`, source region `r_src`, target region `r_tgt`.
* Outputs: nonnegative scalars summarizing effective feedforward (`C_ff`) and feedback (`C_fb`) connectivity strengths.

5. Metabolic cost observable

```txt
A_energy(m; r)
```

* Input: state `m`, region `r`.
* Output: a nonnegative scalar summarizing effective metabolic cost or activity for that region over the relevant time window.

All these observables are assumed to be well defined and finite for states in the regular subset `M_reg` defined in Section 3.5.

### 3.3 Mismatch measures and finite libraries

We define three mismatch measures, each based on a fixed finite library of reference patterns and scales. These libraries are fixed once at the level of this Q089 entry and reused across all experiments. They are **not** tuned after examining individual datasets.

1. Error balance mismatch

Let `L_ref_err` be a finite library of **predictive-coding-consistent error patterns**, specifying expected relationships between `E_level` and `R_level` across levels and regions when predictive coding holds approximately.

We define:

```txt
DeltaS_err(m) >= 0
```

as a scalar measuring the deviation of the observed relationship between `E_level` and `R_level` in `m` from the library `L_ref_err`. It is zero if and only if the observed relationships match one of the library patterns within prescribed tolerance.

2. Hierarchical connectivity mismatch

Let `L_ref_hier` be a finite library of **hierarchical connectivity patterns** expected under predictive coding, specifying qualitative and quantitative relationships among `C_ff` and `C_fb` across levels and regions.

We define:

```txt
DeltaS_hier(m) >= 0
```

as a scalar measuring the deviation between the observed `C_ff`, `C_fb` patterns in `m` and this library. It is zero when connectivity is consistent with at least one library pattern within tolerance.

Where appropriate, these patterns can reuse geometric constraints defined in Q088, so that predictive coding hierarchies respect known map geometries.

3. Energy-efficiency mismatch

Let `L_ref_energy` be a finite library of **energy versus prediction-efficiency tradeoff profiles** expected for predictive coding implementations, given task complexity and input statistics.

We define:

```txt
DeltaS_energy(m) >= 0
```

as a scalar measuring deviation between the observed `A_energy` versus performance profile and these tradeoff curves.

These mismatch measures are constructed so that they:

* depend only on the observable fields,
* use finite libraries fixed prior to evaluation,
* and do not change per dataset.

### 3.4 Combined predictive coding mismatch and tension tensor

We now define the combined predictive coding mismatch:

```txt
DeltaS_PC(m) = w_err * DeltaS_err(m)
             + w_hier * DeltaS_hier(m)
             + w_energy * DeltaS_energy(m)
```

with fixed nonnegative weights:

```txt
w_err   = 0.5
w_hier  = 0.3
w_energy = 0.2
w_err + w_hier + w_energy = 1
```

These weights are part of the **Q089 tension scale specification** and are not adjusted per dataset or experiment. Any alternative weight triplet should be treated as a different versioned configuration, not as a silent change of this entry.

We define an effective tension tensor, consistent with the TU core decision:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_PC(m) * lambda(m) * kappa
```

where:

* `S_i(m)` represents source-like factors (for example the strength of particular task demands or sensory drives),
* `C_j(m)` represents receptivity-like factors (for example susceptibility of cognitive functions to predictive coding failures),
* `lambda(m)` is a convergence-state factor from the TU core,
* `kappa` is a coupling constant setting the overall scale of predictive-coding implementation tension.

The exact index sets for `i` and `j` are not specified at the effective layer, only that `T_ij(m)` is finite for all relevant indices in `M_reg`.

### 3.5 Singular set and domain restrictions

Some observables or mismatch measures may be undefined or non-finite, for example if data are incomplete or encodings violate admissibility constraints.

We define the singular set:

```txt
S_sing = { m in M : DeltaS_PC(m) is undefined or not finite }
```

and the regular domain:

```txt
M_reg = M \ S_sing
```

All Q089-related tension analysis is restricted to `M_reg`.

* States in `S_sing` are treated as **out of domain**.
* Out-of-domain outcomes are used to diagnose data or encoding issues, not as evidence for or against predictive coding implementation.
* Experiments that produce a high fraction of states in `S_sing` must be reported as violating Q089 domain assumptions rather than falsifying Q089 itself.

---

## 4. Tension principle for this problem

### 4.1 Core tension functional

We define the **predictive coding implementation tension functional**:

```txt
Tension_PC(m) = G(DeltaS_err(m), DeltaS_hier(m), DeltaS_energy(m))
```

For E1 purposes, we choose a simple linear form:

```txt
Tension_PC(m) = DeltaS_PC(m)
```

so that:

* `Tension_PC(m) >= 0` for all `m` in `M_reg`,
* `Tension_PC(m)` is small only when error patterns, hierarchy, and energy tradeoffs are all close to predictive-coding-consistent libraries,
* `Tension_PC(m)` becomes large when any of the three mismatch components is large.

### 4.2 Implementation hypothesis as a low-tension principle

At the effective layer, the **predictive coding implementation hypothesis** can be expressed as:

> For appropriate brain regions and tasks, there exist empirically reachable states `m` in `M_reg` such that the predictive coding implementation tension `Tension_PC(m)` lies in a narrow, stable low-tension band across relevant scales.

More concretely, for a chosen admissible encoding `E` in `E_PC` and fixed reference libraries, there should exist states `m_true` representing real cortico-thalamic configurations such that:

```txt
Tension_PC(m_true) <= epsilon_PC
```

for some small threshold `epsilon_PC` that does not diverge as more precise or higher-resolution data are incorporated, provided the encoding remains in `E_PC` and the finite libraries are unchanged.

### 4.3 Alternative architectures as persistent high tension

If biological neural circuits implement some **alternative architecture** in place of predictive coding (for example a purely feedforward scheme or an algorithm with qualitatively different error handling), then in any encoding that remains faithful to the true circuit structure and dynamics, world-representing states `m_alt` would eventually exhibit **persistent high tension**:

```txt
Tension_PC(m_alt) >= delta_PC
```

for some strictly positive `delta_PC` that cannot be reduced arbitrarily by:

* refining spatial or temporal resolution,
* collecting more data,
* or switching among admissible encodings in `E_PC`.

In this view, Q089 is not claiming a proof that the brain implements predictive coding. Instead, it frames the question as a structured comparison between low-tension (predictive-coding-like) and high-tension (non-predictive-coding) worlds at the effective layer.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds strictly at the effective layer.

* World T: brains implement predictive coding to a good approximation in relevant circuits.
* World F: brains implement qualitatively different architectures that cannot be reconciled with predictive coding under admissible encodings.

### 5.1 World T (predictive coding implemented, low tension)

In World T:

1. Error and representation patterns

   * There exist states `m_T` in `M_reg` such that `DeltaS_err(m_T)` is small across a wide range of regions and tasks.
   * Error signals are segregated or at least functionally distinguishable from representation signals in ways matching library `L_ref_err`.

2. Hierarchical connectivity

   * `DeltaS_hier(m_T)` remains small when connectivity patterns are projected into `L_ref_hier`.
   * Feedforward and feedback strengths across levels and laminae respect characteristic predictive-coding patterns, such as error-driven forward projections and prediction-carrying feedback.

3. Energy-efficiency profile

   * `DeltaS_energy(m_T)` remains small when measured against `L_ref_energy`.
   * The system exhibits energy savings and robustness patterns consistent with predictive-coding-style redundancy reduction and efficient inference.

4. Stability across scales

   * As data quality and resolution increase, `Tension_PC(m_T)` remains within a controlled band bounded by `epsilon_PC`, rather than growing or fluctuating wildly.

### 5.2 World F (alternative architecture, high tension)

In World F:

1. Error patterns

   * There exist states `m_F` representing real circuits such that `DeltaS_err(m_F)` remains bounded away from zero even as measurement resolution improves.
   * No plausible segregation or functional role assignment of populations matches the library `L_ref_err`.

2. Hierarchical connectivity

   * Observed connectivity patterns produce large `DeltaS_hier(m_F)` across many regions and levels.
   * Feedback and feedforward strengths do not align with predictive-coding expectations, even after accounting for known anatomical constraints.

3. Energy-efficiency mismatch

   * The relationship between `A_energy` and performance systematically deviates from `L_ref_energy`.
   * Either excessive energy is used for a given predictive performance, or performance remains poor despite energy patterns that would be expected to support predictive coding.

4. Persistent high tension

   * For any sequence of refined encodings within `E_PC`, `Tension_PC(m_F)` does not drop below some `delta_PC > 0`.

### 5.3 Interpretive note

These counterfactual worlds do not specify how raw neural data are transformed into `M`. They only state that:

* if predictive coding is implemented, then low-tension configurations consistent with library patterns should be observable;
* if not, all faithful encodings will show persistent high tension.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

* falsify particular choices of predictive coding encodings,
* distinguish predictive-coding-like implementations from alternatives,
* test the stability of `Tension_PC` under refinement.

Falsifying an encoding does not solve the canonical problem but constrains which implementation stories remain plausible.

### Experiment 1: Laminar physiology and error signal segregation

**Goal**
Test whether cortical laminar activity under sensory prediction tasks is consistent with library patterns for error and prediction segregation encoded in `DeltaS_err` and `DeltaS_hier`.

**Setup**

* Data: multi-laminar recordings or high-resolution imaging from sensory cortex (for example visual cortex) during tasks that contrast predictable versus surprising stimuli.
* Regions: select a finite set of cortical columns or areas as `L_reg`.
* Time windows: select task-aligned windows (for example stimulus onset, sustained response, post-stimulus period) as `L_time`.
* Encoding: fix an admissible encoding `E` in `E_PC` that maps raw signals to `R_level`, `E_level`, `Pi_level`, `C_ff`, `C_fb` using a finite feature set and a registered entry in `Registry_PC`.

**Protocol**

1. For each dataset and task condition, apply `E` to obtain a state `m_data` in `M`.
2. If the resulting state falls into `S_sing`, label it as out-of-domain for Q089 and use it only for encoding diagnostics, not for tension analysis.
3. For `m_data` in `M_reg`, compute `DeltaS_err(m_data)` and `DeltaS_hier(m_data)` using the fixed libraries `L_ref_err` and `L_ref_hier`.
4. Aggregate `Tension_PC(m_data)` across tasks, regions, and time windows.
5. Compare tension distributions between:

   * conditions where predictive coding should be most active (for example predictable sequences),
   * and control or randomized conditions.

**Metrics**

* Distribution of `DeltaS_err` and `DeltaS_hier` across all `m_data` in `M_reg`.
* Fraction of states with `Tension_PC(m_data) <= epsilon_PC`.
* Stability of these fractions when resolution or recording quality is improved.

**Falsification conditions**

* If, for any reasonable choice of finite libraries and encoding `E` in `E_PC`, `Tension_PC(m_data)` is consistently large in conditions where predictive coding is theoretically expected to be strong, and remains large under refinement, then the current encoding of predictive-coding implementation for those circuits is considered falsified at the effective layer.
* If small changes in the encoding that preserve admissibility lead to arbitrarily different tension profiles with no principled reason, the encoding is considered unstable and rejected.

**Semantics note**
All observables are treated with the hybrid semantics: discrete events and spikes are summarized into continuous rate and correlation descriptors. No additional semantic regime is introduced.

**Domain note**
States in `S_sing` are explicitly excluded from tension statistics. A high fraction of `S_sing` outcomes indicates a failure of encoding assumptions or data quality, not evidence about predictive coding itself.

**Boundary note**
Falsifying this TU encoding does not solve the canonical statement. This experiment can reject specific predictive coding encodings but does not prove or disprove that biological brains implement predictive coding in general.

---

### Experiment 2: Precision weighting and neuromodulation

**Goal**
Assess whether changes in uncertainty or neuromodulatory state produce error gain modulations consistent with predictive coding precision weighting as captured by `Pi_level` and `DeltaS_energy`.

**Setup**

* Data: recordings or imaging during tasks that manipulate uncertainty (for example cue reliability) and neuromodulatory systems (for example pharmacological or behavioral manipulations).
* Regions: select a finite set of sensory and association regions as `L_reg`.
* Encoding: fix an admissible encoding `E` in `E_PC` that extracts `E_level`, `Pi_level`, and `A_energy` from the data, with the encoding pre-registered in `Registry_PC`.

**Protocol**

1. For each combination of uncertainty and neuromodulatory condition, construct states `m_cond` via `E`.
2. Discard states in `S_sing` from tension statistics and report their frequency separately as a domain-violation indicator.
3. For states in `M_reg`, compute `DeltaS_err(m_cond)`, `DeltaS_energy(m_cond)`, and `Tension_PC(m_cond)`.
4. Examine how `Pi_level` and `A_energy` co-vary with uncertainty and with prediction error magnitudes.
5. Compare observed patterns to the fixed library `L_ref_energy` and expected precision-weighting patterns.

**Metrics**

* Correlation between uncertainty manipulations and `Pi_level` changes.
* Changes in `DeltaS_err` and `DeltaS_energy` across conditions.
* Frequency with which `Tension_PC(m_cond)` falls within the low-tension band in conditions where predictive coding should provide an advantage.

**Falsification conditions**

* If across multiple tasks and regions, manipulations of uncertainty and neuromodulatory state fail to produce any consistent relationship between `Pi_level`, error signals, and performance compatible with `L_ref_energy`, then the specific encoding of precision weighting and energy tradeoffs is falsified.
* If in all admissible encodings, `Tension_PC(m_cond)` remains high or behaves inversely to predictive coding expectations, the predictive-coding implementation hypothesis for those circuits becomes significantly weakened at the effective layer.

**Semantics note**
The same hybrid semantics is used: discrete neural events are summarized into continuous variables for error magnitude, gain, and energy proxies.

**Domain note**
States in `S_sing` are out of domain. A robust conclusion about predictive coding requires that a substantial fraction of states lie in `M_reg` under the chosen encoding.

**Boundary note**
Even consistent neuromodulation patterns do not prove predictive coding; they only support specific implementation stories at the effective layer.

---

## 7. AI and WFGY engineering spec

This block describes how Q089 can be used to design and evaluate AI systems within WFGY, without exposing any deep TU generative rules.

### 7.1 Training signals

We define several training signals for AI models.

1. `signal_pred_error_balance`

   * Definition: a scalar penalty proportional to `DeltaS_err(m_model)` for internal states `m_model` representing model activity during prediction tasks.
   * Role: encourages architectures and activations where prediction error signals are appropriately segregated and balanced with representations.

2. `signal_hierarchy_consistency`

   * Definition: a penalty based on `DeltaS_hier(m_model)` computed from effective connectivity or influence measures between layers.
   * Role: promotes hierarchical relationships consistent with predictive-coding-like top down and bottom up pathways.

3. `signal_energy_efficiency`

   * Definition: a cost based on `DeltaS_energy(m_model)` that compares computational resource usage with predictive performance.
   * Role: pushes the model toward energy-efficient prediction regimes analogous to the biological predictive coding story.

4. `signal_pc_stability`

   * Definition: a signal that evaluates variability of `Tension_PC(m_model)` when the same inputs are processed under small perturbations.
   * Role: encourages robust predictive coding behavior rather than brittle implementation that only appears under finely tuned conditions.

### 7.2 Architectural patterns

We outline module patterns that reuse Q089 components.

1. `PC_Block`

   * Role: a module with distinct units for predictions and prediction errors, connected in a way that approximates predictive coding updates.
   * Interface:

     * Inputs: previous predictions, current sensory-like features.
     * Outputs: updated predictions, prediction error estimates, local tension estimates.

2. `Hierarchical_PC_Stack`

   * Role: a stack of PC_Blocks forming a multi-level hierarchy.
   * Interface:

     * Inputs: sensory-level features.
     * Outputs: high-level predictions, error summaries at each level, overall `Tension_PC` trace.

3. `Precision_Controller`

   * Role: a module that modulates gains on error units based on uncertainty estimates.
   * Interface:

     * Inputs: uncertainty summaries or attention-like signals.
     * Outputs: precision weights applied to prediction error units, plus an estimate of `DeltaS_energy`.

### 7.3 Evaluation harness

We propose an evaluation harness for AI models integrating Q089 components.

1. Task design

   * Sequence prediction, sensorimotor control, and noisy perception tasks where predictive coding suggests advantages, such as robust handling of partial observations and fast adaptation to prediction errors.

2. Conditions

   * Baseline model: standard deep network without explicit PC blocks.
   * PC-enhanced model: architecture with `PC_Block`, `Hierarchical_PC_Stack`, and `Precision_Controller` modules and access to `signal_*` tension regularizers.

3. Metrics

   * Predictive performance (accuracy, negative log-likelihood).
   * Resource usage (compute proxies, latency, approximate energy).
   * Internal consistency: stability of internal `Tension_PC` signals across similar inputs and perturbations.

### 7.4 60-second reproduction protocol

A minimal protocol for external users to see Q089 impact on AI explanatory behavior.

* Baseline setup

  * Prompt: ask an AI model to explain predictive coding and its possible implementation in the brain, without any mention of TU or WFGY.
  * Observation: record whether the explanation mixes metaphorical and implementation-level claims, or leaves the mapping to circuits vague.

* TU encoded setup

  * Prompt: same question, but instruct the AI to:

    * separate theoretical predictive coding equations from biological implementation,
    * talk in terms of observables like error units, feedback connectivity, and energy costs,
    * and articulate an effective-layer tension between theory and data.
  * Observation: record whether the explanation becomes more structured, with clear statements about what would count as support or disconfirmation.

* Comparison metric

  * Use a simple rubric to rate:

    * clarity of separation between theory and implementation,
    * explicitness of measurable predictions,
    * mention of error patterns, hierarchy, and energy.

* Logging

  * Store full prompts and responses.
  * If available, log internal `Tension_PC` estimates to illustrate how the model organizes its explanation.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. Component name: `PredictiveCodingImplementation_Tension`

   * Type: functional
   * Minimal interface:

     * Inputs: effective fields representing representation activity, error activity, precision, connectivity, and energy usage.
     * Output: scalar `Tension_PC_value`.
   * Preconditions: inputs must be derived from an admissible encoding consistent with `E_PC` and the finite libraries defined for Q089.

2. Component name: `PC_Hierarchy_Descriptor`

   * Type: field
   * Minimal interface:

     * Inputs: summarized connectivity matrices and laminar-level indices, possibly constrained by map geometries from Q088.
     * Output: a compact descriptor of hierarchical structure suitable for reuse in other problems.
   * Preconditions: connectivity summaries must be available across multiple levels or regions.

3. Component name: `ErrorPrecision_Experiment_Template`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: descriptions of tasks, uncertainty manipulations, and available measurement modalities.
     * Output: a protocol for measuring error and precision observables and computing `DeltaS_err` and `DeltaS_energy`.
   * Preconditions: tasks must support uncertainty or gain manipulations.

### 8.2 Direct reuse targets

1. Q086 (functions of sleep and offline processing)

   * Reused components: `PC_Hierarchy_Descriptor` and `ErrorPrecision_Experiment_Template`.
   * Why it transfers: offline replay and consolidation can be studied as modifications to predictive hierarchies and error weighting.
   * What changes: experiments are performed during sleep or rest states rather than active perception, and observables emphasize offline activity.

2. Q087 (neurodegenerative and psychiatric disorders)

   * Reused component: `PredictiveCodingImplementation_Tension`.
   * Why it transfers: many disorders can be framed as chronic mis-weighting of prediction errors or breakdowns in predictive hierarchy integrity.
   * What changes: input data now include clinical and pathological measures, and tension is interpreted as a marker of disease-related architecture changes.

3. Q123 (AI interpretability of internal representations)

   * Reused component: `PC_Hierarchy_Descriptor`.
   * Why it transfers: internal layers of artificial networks can be analyzed using the same descriptor to see whether they resemble predictive coding hierarchies.
   * What changes: empirical data come from artificial units and activations rather than biological neurons.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * An effective encoding of predictive coding implementation has been specified via mismatch measures and `Tension_PC`.
  * Experimental templates are defined but not yet instantiated as a full empirical program.

* N_level: N1

  * The narrative separates predictive coding theory, biological implementation, and tension between them.
  * Counterfactual worlds and reuse patterns are articulated but not yet extensively cross-validated.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented:

1. A concrete analysis pipeline that:

   * takes real laminar or imaging data,
   * applies a specified `E` in `E_PC`,
   * computes `DeltaS_err`, `DeltaS_hier`, `DeltaS_energy`, and `Tension_PC`,
   * publishes resulting tension profiles and their dependence on task conditions.

2. A set of artificial neural network experiments where:

   * PC-inspired architectures are built and instrumented with Q089 components,
   * tension profiles are compared to those from real neural data,
   * similarities and differences are systematically documented.

### 9.3 Long-term role in the TU program

In the long run, Q089 is expected to serve as:

* a canonical example of how TU handles implementation questions in neuroscience,
* a calibration point for linking abstract inference theories to biological or artificial circuits,
* a reusable template for structuring debates about whether any given circuit-level model really implements a proposed algorithm or only mimics some of its high-level signatures.

---

## 10. Elementary but precise explanation

Predictive coding is the idea that the brain works a bit like a prediction machine. It constantly tries to guess what will happen next in the senses and only pays special attention to the parts it did not predict well. Those are the prediction errors.

In simple language:

* some neurons carry predictions,
* some carry the differences between what was predicted and what actually came in,
* and the brain keeps adjusting itself to make those differences smaller and more useful.

The hard question is not just “is prediction important for the brain”. Most scientists agree that it is. The hard question is:

> Does the brain actually use circuits that match the specific predictive coding algorithms from theory?

In this document, we do not try to answer that by fiat. Instead, we:

1. Describe what we would see in the brain if predictive coding really were implemented:

   * special patterns of activity for prediction errors,
   * special patterns of connections between layers,
   * reasonable energy use for the quality of prediction achieved.

2. Define a single number `Tension_PC` that becomes:

   * small when what we see in the data looks like predictive coding,
   * large when it does not.

3. Consider two kinds of worlds:

   * In a predictive-coding world, we should be able to find situations where `Tension_PC` is small and stays small as we look more closely.
   * In a non-predictive-coding world, no matter how we look at the data, `Tension_PC` stays big.

We then design experiments that measure error signals, connectivity, and energy use, and we compute this tension number. If many careful experiments keep showing high tension, that weakens the idea that predictive coding is really implemented in those circuits. If instead we find low tension in the right places and tasks, that strengthens the case.

Q089 therefore does not declare “yes, the brain implements predictive coding” or “no, it does not”. It gives a precise way to:

* talk about what that claim would mean in measurable terms,
* test specific implementation stories,
* and reuse these tools when we study related questions about memory, sleep, disease, and artificial neural networks.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective-layer encoding of **Q089 · Implementation of predictive coding in biological brains**.
* It does not claim to prove or disprove the canonical predictive coding statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here (state spaces `M`, observables, invariants, tension scores, counterfactual worlds) live at the Tension Universe effective layer.
* No claim is made about the uniqueness or fundamentality of these objects at the level of physics or deep axioms.
* Domain restrictions are enforced via `M_reg` and `S_sing`. States in `S_sing` are treated as out of domain and are not used to support or refute predictive coding implementation.

### Encoding and fairness

* Encodings from data to states must belong to an admissible class `E_PC` and a pre-registered finite encoding registry.
* Reference libraries for mismatch measures (`L_ref_err`, `L_ref_hier`, `L_ref_energy`) are finite and fixed at the level of this entry. They are not tuned per dataset.
* Tension weights (`w_err`, `w_hier`, `w_energy`) are fixed as part of the Q089 tension scale configuration. Different weights define different versioned proposals.
* Any implementation that violates these constraints may still be scientifically useful, but it should not be presented as an implementation of this Q089 effective-layer entry.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

