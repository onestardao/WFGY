<!-- QUESTION_ID: TU-Q097 -->
# Q097 · Triggering of large volcanic eruptions

## 0. Header metadata

```txt
ID: Q097
Code: BH_EARTH_VOLCANISM_L3_097
Domain: Earth
Family: Volcanism and solid Earth dynamics
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: risk_tail_tension
Status: Partial
Semantics: continuous
E_level: E1
N_level: N1
Encoding_key: TU_BH_Q097_VOLC_v1
Last_updated: 2026-01-31
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

1. **Scope of objects**

   This page only introduces and manipulates:

   * an effective state space `M_volc` and its regular subset `M_volc_reg`,
   * an admissible encoding class `A_enc(Q097)` for volcanic configurations,
   * observable fields and functionals such as `sigma_eff`, `phi_melt`, `C_vol`, `K_flow`, `F_ext`,
   * tail risk functionals such as `TailRiskIndex`, `MetastabilityMargin`,
   * a tail risk tension scalar `Tension_VOLC` and associated invariants,
   * counterfactual worlds and experiment templates defined purely in terms of those observables.

   No TU core axioms, hidden semantic curvature fields, or deep generative rules of TU are specified or used here.

2. **Encoding element and precommitment**

   * The header field `Encoding_key: TU_BH_Q097_VOLC_v1` selects a single encoding element

     ```txt
     e* in A_enc(Q097)
     ```

     from a finite encoding class `A_enc(Q097)` associated with this problem.

   * The element `e*` packages together:

     * the map from physical configurations to `M_volc`,
     * the libraries `L_ne(e*)`, `S_meta(e*)`,
     * the functionals `G_non_eruptive(e*)`, `H_meta(e*)`,
     * the weights `alpha(e*)`, `beta(e*)`,
     * tail risk thresholds `epsilon_VOLC(e*)`, `delta_VOLC(e*)` that appear in Section 4.

   * Once `e*` is fixed by `Encoding_key`, all effective layer quantities in this page are understood as depending on `e*`, even when the dependence is not written explicitly. For example

     ```txt
     Tension_VOLC(m)  means  Tension_VOLC(m; e*)
     TailRiskIndex(m) means  TailRiskIndex(m; e*)
     ```

3. **Semantics regime**

   * `Semantics: continuous` means:

     * physically, the underlying magmatic, crustal, and volatile fields are continuous in space and time,
     * at the effective layer, we only work with **finite dimensional** summaries and observables that are continuous or bounded discrete functions of those fields.

   * No claim is made about the detailed microscopic dynamics. Only coarse grained observables enter the definitions.

4. **Claims and non claims**

   * This page does **not** prove or claim to prove any new theorem in volcanology, probability theory, or TU.
   * It does **not** claim to provide a complete physical theory of large volcanic eruptions or a reliable operational prediction system.
   * It only specifies one effective layer encoding element `e*` and associated experiment templates that can be tested, falsified, or refined.

5. **Relation to the canonical problem**

   * The canonical scientific problem of large eruption triggering is stated in Section 1.
   * All later sections are about **encoding that problem** as a tail risk tension statement within TU.
   * Falsifying the encoding element `e*` under the experiments in Section 6 does **not** prove or disprove the canonical triggering problem itself. It only constrains which effective layer encodings remain compatible with the tested data and protocols.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q097 can be stated as:

> Given the physical state of a volcanic and surrounding crustal system, what combination of stresses, melts, volatiles, and pathways triggers a large volcanic eruption, and on what time scales, in a way that allows at least partial forecasting of such events?

Here:

* "large volcanic eruption" means events in the upper tail of explosivity and impact, for example Volcanic Explosivity Index (VEI) 6 and above, including so called super eruptions.
* "triggering" refers to the transition from a metastable magmatic crustal configuration to rapid failure and magma discharge, not only to the existence of long lived magma reservoirs.

The scientific problem is to identify, in physical rather than purely statistical terms:

1. which combinations of observable state variables are necessary or sufficient for large eruptions,
2. how close the system can approach such conditions without erupting,
3. whether useful, nontrivial forecasting signals can be defined in terms of these state variables.

Within the BlackHole project, Q097 asks how to encode these questions at the effective layer of TU, without claiming any direct access to the underlying TU core.

### 1.2 Status and difficulty

Key facts about the current scientific status include:

* Many large eruptions are associated with long lived magma reservoirs, evolving over tens of thousands to hundreds of thousands of years, with episodic recharge and cooling.

* Physical models exist for:

  * overpressure and mechanical failure of crustal rocks,
  * magma ascent through conduits and dikes,
  * fragmentation, degassing, and explosive behavior.

* However, there is no consensus predictive theory that reliably links observed precursors, such as seismic swarms, ground deformation, and gas emissions, to the timing and magnitude of very large eruptions.

* Statistical studies show that large eruptions are rare tail events in time and magnitude, with highly variable inter event times.

* Reviews on super eruptions emphasize that:

  * reservoirs can remain in near eruptible states for extended periods,
  * not all near eruptible states result in an eruption,
  * detailed trigger mechanisms for large scale failure are still poorly constrained.

As a result, triggering of large eruptions remains a partially understood, high impact open problem in Earth sciences.

* It is not "open" in the sense of having no models at all.
* It is "partial" in the sense that there is no widely accepted, quantitative, forecasting capable theory that connects effective monitoring signals to the onset of large eruptions in a way that survives prospective testing.

The label `Status: Partial` in the header refers exactly to this situation.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q097 plays several roles:

1. It is a canonical example of **risk_tail_tension** in a physical dynamical system, where:

   * the observable state space is high dimensional and noisy,
   * catastrophic events occupy a small region of that space,
   * forecasting is essentially forecasting entry into a rare tail region.

2. It provides a concrete physical testbed for:

   * defining tail risk indices over configuration space,
   * defining metastability margins for complex systems,
   * probing how much information is needed to meaningfully forecast extreme events.

3. It acts as a bridge between:

   * solid Earth physics,
   * global risk assessment,
   * AI forecasting and alignment for low frequency, high impact hazards.

The rest of this entry is about specifying one effective layer encoding element `e*` for this role, plus associated experiments.

### References

1. Smithsonian Institution, Global Volcanism Program, "Volcanoes of the World" database and documentation on large explosive eruptions and the Volcanic Explosivity Index (VEI).
2. R. S. J. Sparks and related works on magma dynamics, conduit flow, overpressure, and explosive eruption physics.
3. C. G. Newhall and S. Self, "The Volcanic Explosivity Index (VEI): An estimate of explosive magnitude for historical volcanism", Journal of Geophysical Research, 1982.
4. Review literature on super eruptions and unresolved questions in the triggering of very large volcanic eruptions in solid Earth geoscience.

---

## 2. Position in the BlackHole graph

This block records the graph position of Q097 with explicit edges and one line reasons. All edges refer only to Q IDs and text names, and all reasons refer to effective layer objects.

### 2.1 Upstream problems

These nodes provide conceptual or methodological prerequisites for Q097.

* **Q091**
  Reason: Supplies background climate sensitivity notions that condition the global impact and feedbacks of large eruptions in Earth system risk narratives.

* **Q092**
  Reason: Provides a general framework for tipping and threshold behavior in Earth subsystems that can be reused for crustal magmatic transitions.

* **Q096**
  Reason: Shares tools and ideas for predictability and triggering in highly nonlinear solid Earth systems where stress accumulation, failure, and rare events create tension.

* **Q094**
  Reason: Offers multi scale fluid dynamical patterns that are analogs for volatile transport and crustal fluid migration relevant to magmatic systems.

### 2.2 Downstream problems

These nodes directly reuse components defined in Q097.

* **Q100**
  Reason: Uses large eruptions as environmental shocks that modulate conditions for disease emergence and spread in global risk models.

* **Q095**
  Reason: Treats large eruptions as discrete, high impact shocks to ecosystems in biodiversity loss and recovery dynamics.

* **Q099**
  Reason: Includes large eruptions as drivers of regional hydrological shifts and long term freshwater stress via radiative forcing and ash deposition.

### 2.3 Parallel problems

Parallel nodes share similar tension types without direct component reuse.

* **Q096**
  Reason: Both Q096 and Q097 aim to characterize and forecast rare, high impact events in solid Earth driven by complex stress fields and thresholds.

* **Q105**
  Reason: Q105 deals with systemic crashes in complex networks, another instance of risk_tail_tension in a high dimensional configuration space.

* **Q092**
  Reason: Q092 studies rapid transitions between states of Earth subsystems, making it parallel in both threshold structure and rare event focus.

### 2.4 Cross domain edges

Cross domain edges show where Q097 components can transfer.

* **Q059**
  Reason: Reuses tail risk tension formalizations to quantify how much information is needed to forecast rare catastrophic events in information processing systems.

* **Q098**
  Reason: Incorporates large eruptions as external shocks within an Anthropocene scale dynamical system of human Earth interactions.

* **Q121**
  Reason: Uses Q097 as a concrete physical scenario for aligning AI forecasts and decisions under low frequency, high impact risk.

* **Q125**
  Reason: Models multi agent coordination and response to super eruption scenarios as a case of global decision making under tail risk tension.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is restricted to the effective layer and depends on the selected encoding element `e* in A_enc(Q097)`.

We describe only:

* state spaces,
* observables and fields,
* admissible encodings and libraries,
* tail risk indices and singular sets.

We do not describe any hidden TU generative rules or mappings from raw data to TU core objects.

### 3.1 State space

We introduce an effective state space

```txt
M_volc
```

with the following interpretation:

* Each state `m` in `M_volc` represents a coarse grained configuration of:

  * a volcanic system, including one or more magma reservoirs,
  * the surrounding crust and lithosphere in a relevant region,
  * the immediate hydrosphere and atmosphere where they directly interact with the volcano.

For each `m` we assume access, through the encoding element `e*`, to a finite dimensional summary of key variables, such as:

* stress and strain indicators in specified crustal regions,
* overpressure and melt fraction indicators in magma reservoirs,
* volatile content indicators in reservoirs,
* permeability or flow capacity measures along potential pathways to the surface,
* external forcing indicators such as tectonic loading, ice unloading, or rapid erosion.

We do not specify in this page how such summaries are computed from observational, geological, or simulation data. We only assume that:

* each state `m` encodes a set of scalar or low dimensional vector observables that can be consistently interpreted across states for a fixed encoding element `e*`.

### 3.2 Admissible encoding class

We define an admissible encoding class associated with Q097.

1. **Encoding class**

   * Let

     ```txt
     A_enc(Q097) = { e_1, e_2, ..., e_Lenc }
     ```

     be a finite set of encoding elements for Q097.

   * For concreteness, we write

     ```txt
     E_volc = A_enc(Q097)
     ```

     and we work with the element `e* in E_volc` selected by the header field `Encoding_key`.

2. **Role of an encoding element**

   Each encoding element `e` in `E_volc` specifies:

   * a map from physical configurations of the volcanic region to states in `M_volc`,

   * a fixed set of regions and reservoir definitions,

   * a fixed list of summary statistics and temporal aggregation rules,

   * libraries and functionals

     ```txt
     L_ne(e), S_meta(e), G_non_eruptive(e), H_meta(e)
     ```

   * weights `alpha(e)`, `beta(e)` with `alpha(e) > 0`, `beta(e) > 0`, `alpha(e) + beta(e) = 1`,

   * tail risk thresholds `epsilon_VOLC(e)`, `delta_VOLC(e)` used in Section 4.

3. **Structural conditions on encodings**

   For any `e in E_volc`, the encoding must satisfy:

   * Finite dimensionality: each `m` is represented by a finite list of real valued or bounded discrete valued observables.

   * Monotonicity of hazard indicators: if a physical change is known to increase stress, melt fraction, or volatile content in a region, then the corresponding observables for that region must not decrease.

   * Temporal coherence: for a slowly varying physical system, small changes in physical state over a short time window must not produce arbitrarily large jumps in the summary observables.

4. **Precommitment**

   For any experiment or analysis in this page:

   * a specific element `e* in A_enc(Q097)` is selected by `Encoding_key`,
   * all libraries, functionals, weights, and thresholds used in definitions are those packaged inside `e*`,
   * no parameter in `e*` may be tuned using eruption outcomes from the test set on which the encoding is evaluated.

### 3.3 Observables and fields

For the rest of this entry, all observables are defined for the fixed encoding element `e*`.

1. **Effective stress or overpressure indicator**

   ```txt
   sigma_eff(m; R_c)
   ```

   * Input: state `m`, crustal region label `R_c`.
   * Output: nonnegative scalar summarizing effective stress or overpressure in `R_c`.

2. **Effective melt fraction indicator**

   ```txt
   phi_melt(m; R_r)
   ```

   * Input: state `m`, reservoir region label `R_r`.
   * Output: scalar in `[0, 1]` summarizing melt fraction.

3. **Volatile content indicator**

   ```txt
   C_vol(m; R_r)
   ```

   * Input: state `m`, reservoir region label `R_r`.
   * Output: nonnegative scalar summarizing dissolved and exsolved volatile content.

4. **Permeability or flow capacity**

   ```txt
   K_flow(m; P)
   ```

   * Input: state `m`, path label `P` from reservoir to surface.
   * Output: nonnegative scalar summarizing the ability of magma or gas to flow along `P`.

5. **External forcing indicator**

   ```txt
   F_ext(m)
   ```

   * Input: state `m`.
   * Output: scalar or short vector describing relevant external forcings such as tectonic loading rate or surface unloading.

These observables are defined at the effective layer. Their microscopic interpretation depends on `e*` but does not appear explicitly in this page.

### 3.4 Tail risk mismatch observables

We introduce two mismatch measures that compare the current configuration to reference ensembles, as part of the encoding element `e*`.

1. **Tail risk index relative to a non eruptive ensemble**

   * Let `L_ne(e*)` be a fixed finite library of states in the regular domain `M_volc_reg` that are known to have occurred during extended non eruptive intervals at a given volcano or at comparable systems under the encoding `e*`.

   * For each `m in M_volc_reg` we define

     ```txt
     TailRiskIndex(m) = G_non_eruptive(e*)(m, L_ne(e*))
     ```

     where `G_non_eruptive(e*)` is a nonnegative function of:

     * the distances between the observables of `m` and those of states in `L_ne(e*)`,
     * the distribution of such distances over the library.

   * Properties:

     * `TailRiskIndex(m) >= 0` for all `m in M_volc_reg`.
     * If `m` is very similar to many states in `L_ne(e*)`, then `TailRiskIndex(m)` tends to be small.
     * The exact form of `G_non_eruptive(e*)` is part of `e*` and is fixed before any analysis of new data.

2. **Metastability margin**

   * Let `S_meta(e*)` be a subset of `M_volc_reg` representing configurations that are empirically judged, under `e*`, to be metastable with no large eruptions in a specified time horizon.

   * We define

     ```txt
     MetastabilityMargin(m) = H_meta(e*)(m, S_meta(e*))
     ```

     where `H_meta(e*)` is a nonnegative function measuring how far `m` is, in observable space, from a typical point or central region of `S_meta(e*)`.

   * Properties:

     * `MetastabilityMargin(m) >= 0` for all `m in M_volc_reg`.
     * If `m` lies deep inside the region of configurations similar to `S_meta(e*)`, then `MetastabilityMargin(m)` is small.
     * If `m` lies far outside typical `S_meta(e*)` configurations, `MetastabilityMargin(m)` becomes large.

All ingredients `L_ne(e*)`, `S_meta(e*)`, `G_non_eruptive(e*)`, and `H_meta(e*)` are fixed by `e*` before evaluating any new eruption or non eruption trajectories.

### 3.5 Singular set and domain restriction

We define a singular set

```txt
S_sing_volc(e*) = {
  m in M_volc :
  at least one of sigma_eff, phi_melt, C_vol, K_flow, F_ext
  is undefined, non finite, or clearly inconsistent under e*
}
```

Examples of inconsistency include:

* negative melt fraction,
* negative variance in any observable that is supposed to represent a dispersion,
* missing data in required observables for the given encoding element `e*`.

We restrict all tail risk tension analysis to the regular domain

```txt
M_volc_reg = M_volc \ S_sing_volc(e*)
```

Whenever an experiment or protocol in this entry attempts to evaluate `TailRiskIndex(m)` or `MetastabilityMargin(m)` for a state in `S_sing_volc(e*)`, the result is treated as **out of domain** and not as evidence about triggering physics.

---

## 4. Tension principle for this problem

This block states how Q097 is represented as a tail risk tension problem at the effective layer, under the encoding element `e*`.

### 4.1 Core tail risk tension functional

For the fixed encoding element `e*`, we define an effective tail risk tension functional on `M_volc_reg`:

```txt
Tension_VOLC(m; e*) = alpha(e*) * TailRiskIndex(m)
                      + beta(e*)  * MetastabilityMargin(m)
```

with weights

```txt
alpha(e*) > 0
beta(e*)  > 0
alpha(e*) + beta(e*) = 1
```

The parameters `alpha(e*)` and `beta(e*)` are packaged inside `e*` and cannot be adapted after seeing eruption outcomes for the states being evaluated.

Properties:

* `Tension_VOLC(m; e*) >= 0` for all `m in M_volc_reg`.
* If `m` is similar to many known non eruptive states and lies deep inside the metastable region, then `Tension_VOLC(m; e*)` is small.
* If `m` lies far from non eruptive states and far from the metastable region, then `Tension_VOLC(m; e*)` becomes large.

For notational convenience we set

```txt
DeltaS_volc(m) = Tension_VOLC(m; e*)
```

and treat `DeltaS_volc` as the default tail risk tension score for Q097.

### 4.2 Tail risk thresholds and world types

The Tension Scale Charter associates each encoding element `e*` with two positive thresholds

```txt
epsilon_VOLC(e*) > 0
delta_VOLC(e*)   > 0
```

with `epsilon_VOLC(e*) < delta_VOLC(e*)`, interpreted as:

* a **low tension band** where

  ```txt
  DeltaS_volc(m) <= epsilon_VOLC(e*)
  ```

* a **high tension band** where

  ```txt
  DeltaS_volc(m) >= delta_VOLC(e*)
  ```

for world representing states `m in M_volc_reg`.

At the effective layer, triggering of large eruptions is framed as a question about whether real volcanic systems spend significant time in the high tension band and whether transitions from the low band to the high band exhibit detectable structure.

### 4.3 Triggering as low versus high tail risk tension

Informally:

* Non eruptive intervals should correspond to trajectories where `DeltaS_volc(m(t))` mostly stays within the low to moderate band, rarely approaching `delta_VOLC(e*)`.

* Approaching a large eruption should correspond, in a partially predictable world, to a systematic rise in `DeltaS_volc(m(t))` towards or into the high tension band, subject to measurement and modeling uncertainties.

If, after selecting `e*` and its associated thresholds, we find that:

* `DeltaS_volc(m(t))` does not meaningfully distinguish eruptive from non eruptive intervals, or
* any such distinction is extremely sensitive to small admissible changes in encoding parameters inside `e*`,

then the tail risk tension encoding for Q097 implemented by `e*` is considered misaligned with the physical triggering process.

This does not prove that triggering is inherently unpredictable. It only shows that the chosen effective layer encoding `e*` fails to capture robust tail risk structure.

### 4.4 Tension invariants and envelopes

The scalar `DeltaS_volc(m)` can be extended to simple invariants and envelopes that summarize multi scale behavior.

1. **Multi scale tail risk envelope**

   For a fixed encoding element `e*`, consider a finite set of indices `J` that label combinations of:

   * volcano identity,
   * time scale (for example weeks, months, years),
   * spatial aggregation scale.

   For each index `j in J`, define

   ```txt
   DeltaS_volc_j(m) = DeltaS_volc(m_j)
   ```

   where `m_j` is the state representing the configuration at that index under `e*`.

   The vector

   ```txt
   E_volc_env(m) = ( DeltaS_volc_j(m) )_{j in J}
   ```

   is a **tail risk envelope** summarizing how close the system sits to high tension regions across scales.

2. **Tail contrast invariant**

   Let

   * `Eruptive_traj` be a library of eruptive trajectories,
   * `NonEruptive_traj` be a library of matched non eruptive trajectories,

   both encoded under `e*`. Define

   ```txt
   I_tail_contrast(e*) =
     mean_{traj in Eruptive_traj} max_t DeltaS_volc(m_traj(t))
     - mean_{traj in NonEruptive_traj} max_t DeltaS_volc(m_traj(t))
   ```

   where the maxima are taken over common time windows.

   This scalar measures the average separation between eruptive and non eruptive trajectories in terms of peak tail risk tension.

3. **Tension tensor form (formal)**

   In some applications it is useful to embed `DeltaS_volc` into a simple tension tensor

   ```txt
   T_ij(m; e*) = S_i(m; e*) * C_j(m; e*) * DeltaS_volc(m)
   ```

   where

   * `S_i(m; e*)` represents the intensity of the `i`th source component, for example contributions from stress, melt fraction, volatile content, or external forcing,
   * `C_j(m; e*)` represents the sensitivity of the `j`th downstream component, for example climate impact modules or infrastructure vulnerability modules that depend on eruption size.

   The exact decomposition into `S_i`, `C_j` is part of the engineering interface of Q097 and may differ across downstream uses. This page only requires that `T_ij` be a finite rank tensor constructed from effective layer observables and `DeltaS_volc`.

---

## 5. Counterfactual tension worlds

We now define two counterfactual worlds at the effective layer, for the fixed encoding element `e*`:

* World T: triggering is partially predictable via tail risk tension.
* World F: triggering is effectively opaque in the configuration space defined by `e*`.

These worlds describe patterns in observables and tension, not hidden generative rules.

### 5.1 World T (partially predictable triggering)

In World T, we assume:

1. **Hindcast structure**

   * For well instrumented large eruptions and coherent reconstructions of state trajectories `m(t)`, there exist trajectories in `M_volc_reg` such that, under `e*`:

     * in pre eruption windows, `DeltaS_volc(m(t))` tends to rise above typical baseline values associated with non eruptive intervals,
     * in matched non eruptive intervals, `DeltaS_volc(m(t))` remains in a lower band that rarely approaches `delta_VOLC(e*)`.

2. **Stability across systems**

   * When applying `e*` to different volcanoes with similar physical regimes, the qualitative behavior of `DeltaS_volc` is similar:

     * rising towards large eruptions,
     * remaining moderate when no large eruption is imminent.

3. **Model world consistency**

   * In synthetic crustal magmatic models with known eruptive and non eruptive trajectories, `DeltaS_volc` computed from encoded states under `e*`:

     * consistently separates eruptive trajectories from non eruptive ones,
     * shows limited sensitivity to small admissible changes in the internal parameters of `e*`.

4. **Limited but nontrivial forecastability**

   * Forecasting attempts based on `DeltaS_volc` and the envelope `E_volc_env` outperform naive baselines that ignore configuration space structure, given realistic observational noise and limited data.

World T does not assert that eruptions can be predicted precisely in time. It asserts that the configuration space defined by `e*` carries observable structure that is meaningfully correlated with triggering.

### 5.2 World F (effectively opaque triggering)

In World F, we assume:

1. **Hindcast failure**

   * For the same set of case studies, no admissible encoding element in `A_enc(Q097)` yields a stable pattern where `DeltaS_volc(m(t))` rises before large eruptions without also frequently producing high tension in non eruptive intervals.

2. **Encoding instability**

   * Small admissible changes inside `A_enc(Q097)` cause large changes in which trajectories are labeled as high tension:

     * eruptive and non eruptive trajectories cannot be robustly separated by any fixed encoding element.

3. **Model world confusion**

   * In synthetic systems, attempts to define `DeltaS_volc` lead to poor separation even when full state information is available:

     * any apparent separation disappears under mild changes in encoding choices that remain within the rules for `A_enc(Q097)`.

4. **Forecasting collapse**

   * Forecasts based on `DeltaS_volc` perform no better than naive baselines that ignore configuration space structure, or perform worse,
   * these failures cannot be corrected by any admissible parameter choice within `A_enc(Q097)` without violating the precommitted rules.

World F is not a claim about the true Earth. It is a reference pattern for what it would mean for large eruption triggering to be effectively opaque in the effective layer language of Q097.

### 5.3 Interpretive note

These counterfactual worlds are defined only in terms of:

* the encoding class `A_enc(Q097)`,
* the state space `M_volc`,
* the regular domain `M_volc_reg`,
* the scalar `DeltaS_volc` and associated invariants.

They do not assume any particular TU core axioms. Q097 uses them to:

* separate questions about encoding quality from questions about the true physics,
* create experiment templates that can falsify or refine encoding elements without over claiming about eruption predictability.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

* test the coherence of the encoding element `e*`,
* discriminate between better and worse tail risk encodings within `A_enc(Q097)`,
* provide evidence for or against particular parameter choices packaged into `e*`.

These experiments do not claim to solve the triggering problem. They only test effective layer encodings.

All experiments below are restricted to states in the regular domain

```txt
M_volc_reg = M_volc \ S_sing_volc(e*)
```

as defined in Section 3.5.

### Experiment 1: Hindcast tension profiles for well instrumented eruptions

**Goal**

Evaluate whether the encoding element `e*` and its scalar `DeltaS_volc` can distinguish pre eruption periods from matched non eruptive intervals for well studied large eruptions.

**Setup**

* Select a set of large eruptions with relatively good observational records, for example:

  * Mt. St. Helens 1980,
  * Pinatubo 1991,
  * other late twentieth and early twenty first century large eruptions.

* For each case, define under `e*`:

  * a pre eruption window of length `T_pre` such as months to a few years,
  * one or more control windows of the same length in earlier non eruptive periods.

* Fix the encoding element `e*` selected by `Encoding_key`. This includes:

  * the map into `M_volc`,
  * the libraries `L_ne(e*)`, `S_meta(e*)`,
  * the functionals `G_non_eruptive(e*)`, `H_meta(e*)`,
  * the weights `alpha(e*)`, `beta(e*)`,
  * the thresholds `epsilon_VOLC(e*)`, `delta_VOLC(e*)`.

No component of `e*` may be tuned using eruption outcomes from the selected test windows.

**Protocol**

1. For each eruption and each window, reconstruct an approximate trajectory

   ```txt
   t ↦ m(t) in M_volc_reg
   ```

   at a fixed sampling interval such as weekly or monthly, using `e*`.

2. Compute `DeltaS_volc(m(t))` along each trajectory.

3. For each case, compute:

   * the distribution of `DeltaS_volc` values in pre eruption windows,
   * the distribution of `DeltaS_volc` values in control windows.

4. Compare these distributions across all cases and across volcanoes.

**Metrics**

* For each case, define statistics such as:

  ```txt
  Delta_mean  = mean_pre(DeltaS_volc) - mean_control(DeltaS_volc)
  Delta_q90   = q90_pre(DeltaS_volc) - q90_control(DeltaS_volc)
  ```

* Aggregate performance over all cases:

  * fraction of eruption cases where `Delta_mean` exceeds a positive threshold `tau_mean`,
  * fraction of cases where `Delta_q90` exceeds a threshold `tau_q`,

  with thresholds chosen consistently with the tension scale of `e*`.

**Falsification conditions**

* Fix minimal acceptable criteria that are compatible with `epsilon_VOLC(e*)` and `delta_VOLC(e*)`, for example:

  * at least a fraction `p_min` of eruption cases must show `Delta_mean` and `Delta_q90` above small positive thresholds that reflect a meaningful movement toward the high tension band.

* If, after applying `e*` to the full set of cases,

  * the observed fraction of cases with significantly higher pre eruption tension is less than `p_min`,
  * or similar patterns appear equally often when comparing two purely non eruptive windows,

  then the encoding element `e*` is rejected as an effective layer encoding for Q097 under this experiment.

**Boundary note**

Rejecting `e*` under this experiment does not solve or refute the canonical triggering problem in Section 1. It only shows that this particular encoding element fails to produce a robust tail risk tension pattern for the tested data and criteria.

---

### Experiment 2: Synthetic crustal magmatic model discrimination

**Goal**

Evaluate whether the encoding element `e*` can systematically separate eruptive and non eruptive trajectories in a controlled synthetic model where ground truth is known.

**Setup**

* Select or construct a family of dynamical models of crustal magmatic systems where:

  * the full internal state is available at each time step,
  * eruption events are clearly defined by model criteria.

* For each model, generate:

  * multiple trajectories that lead to large eruptions,
  * multiple trajectories that remain non eruptive over comparable time spans.

* Fix the encoding element `e* in A_enc(Q097)` selected by `Encoding_key`, including libraries, functionals, weights, and thresholds.

**Protocol**

1. For each trajectory, map the model state at each time step into `M_volc_reg` using `e*`.

2. Compute `DeltaS_volc(m(t))` along each trajectory.

3. For each trajectory, derive summary statistics for tail risk tension, such as

   * maximum tension over the trajectory,
   * time averaged tension over pre defined windows,
   * time above certain tension levels.

4. Use simple classification rules based on these statistics, such as a single threshold on maximum tension, to predict whether a trajectory is eruptive or non eruptive.

**Metrics**

* Classification performance measures, for example:

  * true positive rate (eruptive trajectories correctly flagged),
  * false positive rate (non eruptive trajectories incorrectly flagged),
  * area under a receiver operating characteristic curve for threshold based classifiers.

* Stability of performance across:

  * different synthetic models with similar qualitative physics,
  * small admissible perturbations of internal parameters inside `e*`.

**Falsification conditions**

* Set minimal performance criteria that are compatible with the tail risk scale implied by `e*`, for example:

  * a required lower bound on true positive rate and an upper bound on false positive rate at a tension threshold related to `delta_VOLC(e*)`.

* If no encoding element in `A_enc(Q097)` can achieve performance above these criteria across a range of synthetic models under mild admissible parameter changes, then:

  * the current family `A_enc(Q097)` is considered ineffective for model world discrimination,
  * Q097 requires a revised encoding class.

**Boundary note**

Rejecting `e*` or even the entire class `A_enc(Q097)` under this experiment does not prove that large eruption triggering is unpredictable in principle. It shows that the current effective layer encoding fails to capture model world tail risk structure in a way that survives basic discrimination tests.

---

## 7. AI and WFGY engineering spec

This block describes how Q097 can be used as an engineering module for AI systems within the WFGY framework.

All training signals and modules in this section are defined **relative to the encoding element `e*` selected by `Encoding_key`**, and use the scalar `DeltaS_volc` and related invariants as defined above.

### 7.1 Training signals

We define auxiliary training signals that AI models can use.

1. `signal_volc_tail_risk`

   * Definition: a scalar signal equal or proportional to `DeltaS_volc(m)` for states associated with volcanic contexts in the model internal representation.
   * Purpose: encourage the model to form internal representations where high tail risk conditions are distinguishable from typical non eruptive conditions.

2. `signal_stability_baseline`

   * Definition: a penalty applied when model inferred states corresponding to long non eruptive intervals are assigned high `DeltaS_volc`, especially above `delta_VOLC(e*)`.
   * Purpose: enforce that quiet periods are mapped to low or moderate tail risk tension consistent with `epsilon_VOLC(e*)`.

3. `signal_counterfactual_clarity`

   * Definition: a measure of how clearly the model separates narratives framed as World T and World F when explicitly asked to reason under those assumptions, using the same encoding element `e*`.
   * Purpose: avoid mixing incompatible assumptions about predictability within a single reasoning chain.

### 7.2 Architectural patterns

We outline module patterns that reuse Q097 structures without exposing deeper TU rules.

1. `VolcanicRiskHead`

   * Role: an auxiliary head attached to the model that produces an estimate of `DeltaS_volc` whenever the context refers to volcanic systems.
   * Interface:

     * Inputs: internal embeddings of text or data describing current volcanic conditions.
     * Outputs: a scalar estimated tail risk tension and optionally a small vector decomposing contributions, for example from stress, melt, volatiles, and external forcing.

2. `GeoRiskConsistencyFilter`

   * Role: a filter module that evaluates model outputs about eruption risk against the encoded tail risk structure of `e*`.
   * Interface:

     * Inputs: candidate statements about volcanic risk and internal state summaries,
     * Outputs: a consistency score or mask indicating whether the statements align with plausible `DeltaS_volc` patterns and the thresholds `epsilon_VOLC(e*)`, `delta_VOLC(e*)`.

3. `ExtremeEventScenarioSampler`

   * Role: a module that proposes scenario variations by exploring directions in state space that change `DeltaS_volc` while staying within admissible physical bounds under `e*`.
   * Interface:

     * Inputs: a baseline configuration summary,
     * Outputs: perturbed configurations representing higher or lower tail risk tension cases.

### 7.3 Evaluation harness

We propose an evaluation harness with baseline and TU augmented conditions.

1. **Task categories**

   * Explanation tasks:

     * explain known large eruptions and their precursors,
     * summarize current scientific uncertainty about triggering.

   * Scenario tasks:

     * answer "what if" questions about changes in monitoring signals,
     * qualitatively assess risk under hypothetical configurations.

2. **Conditions**

   * Baseline condition:

     * the model operates without explicit Q097 related modules.

   * TU condition:

     * the model uses `VolcanicRiskHead` and `GeoRiskConsistencyFilter` as auxiliary tools implemented for `e*`.

3. **Metrics**

   * Factual correctness:

     * consistency with current volcanology and geophysics.

   * Internal coherence:

     * absence of contradictions across closely related questions about risk and precursors.

   * Tail risk sensitivity:

     * ability to distinguish low risk from high risk scenarios in a manner consistent with `DeltaS_volc`, `epsilon_VOLC(e*)`, and `delta_VOLC(e*)`.

### 7.4 60 second reproduction protocol

This is a minimal protocol for external users to perceive the impact of Q097 encoding in an AI system.

1. **Baseline setup**

   * Prompt: ask the AI to explain what triggers large volcanic eruptions and the limits of current forecasting.
   * Observation: examine whether the explanation:

     * confuses long term conditions with short term triggers,
     * overstates the precision of predictions,
     * fails to acknowledge tail risk and uncertainty.

2. **TU encoded setup**

   * Prompt: ask the same question but include an instruction such as:

     > Answer using a configuration space, a tail risk tension scalar for large eruptions, and clear statements about how that tension can or cannot be used for forecasting.

   * The AI is allowed to use Q097 specific modules for `e*`.

   * Observation: examine whether the explanation:

     * clearly separates background conditions from trigger like changes,
     * uses concepts like tail risk indices and metastability margins,
     * clearly flags the limits of predictability.

3. **Comparison metric**

   * Rate both answers on:

     * structure and clarity,
     * explicitness of tail risk concepts,
     * calibration of uncertainty.

   * Optionally, have multiple evaluators compare the two explanations without knowing which is baseline and which is TU encoded.

4. **What to log**

   * Prompts and responses in both setups,
   * any auxiliary tension values produced by `VolcanicRiskHead`,
   * basic metadata about which Q097 components were invoked.

---

## 8. Cross problem transfer template

This block describes reusable components from Q097 and their transfer to other problems.

All components in this section are defined **relative to the encoding element `e*`** selected by `Encoding_key`. If a different encoding element is chosen, these components must be recalibrated.

### 8.1 Reusable components produced by this problem

1. **ComponentName**: `TailRiskIndex_VOLC`

   * Type: functional

   * Minimal interface:

     * Inputs: state `m in M_volc_reg`.
     * Output: scalar `r_tail = TailRiskIndex(m)` representing proximity to known non eruptive configurations under `e*`.

   * Preconditions:

     * The library `L_ne(e*)` and function `G_non_eruptive(e*)` are fixed as part of `e*`.

2. **ComponentName**: `MetastabilityMargin_VOLC`

   * Type: functional

   * Minimal interface:

     * Inputs: state `m in M_volc_reg`.
     * Output: scalar `d_meta = MetastabilityMargin(m)` representing distance to a metastable region.

   * Preconditions:

     * The metastable set `S_meta(e*)` and function `H_meta(e*)` are fixed.

3. **ComponentName**: `GeoExtremeWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a geophysical system with rare, high impact events and an encoding class analogous to `A_enc(Q097)`.
     * Output: a pair of experiment designs:

       * World T: partially predictable extremes,
       * World F: effectively opaque extremes,

       each with specified tail risk observables and falsification criteria.

   * Preconditions:

     * The system has a notion of configuration space and extreme events,
     * an effective layer encoding class has been defined.

### 8.2 Direct reuse targets

1. **Q096 (Earthquake predictability and triggering)**

   * Reused components:

     * `GeoExtremeWorld_Template`,
     * conceptual structure of `TailRiskIndex` and `MetastabilityMargin`.

   * Why it transfers:

     * seismic systems also exhibit rare, high impact events driven by stress accumulation and failure,
     * they also require careful distinction between background states and high tension states.

   * What changes:

     * state space and observables become fault stress, slip deficits, and fluid pressures instead of magmatic variables.

2. **Q105 (Systemic crashes in complex networks)**

   * Reused components:

     * `GeoExtremeWorld_Template`,
     * tail risk functional pattern similar to `Tension_VOLC`.

   * Why it transfers:

     * systemic crashes can be viewed as transitions from metastable configurations into failure regimes in a high dimensional configuration space.

   * What changes:

     * state space becomes network load, connectivity, and flow variables,
     * non crash libraries and metastable sets are defined on network configurations.

3. **Q100 (Pandemic risk under environmental shocks)**

   * Reused components:

     * tail risk framing of rare environmental triggers,
     * methods for connecting environmental extremes to downstream risk models.

   * Why it transfers:

     * large eruptions are part of the exogenous shock space that can affect disease emergence and spread.

   * What changes:

     * tail risk indices are defined on epidemiological and environmental variables,
     * volcanic variables appear as exogenous drivers in a coupled system rather than as the primary configuration.

---

## 9. TU roadmap and verification levels

This block explains the role of Q097 in the TU program and the next measurable steps.

### 9.1 Current levels

* **E_level: E1**

  * A coherent effective encoding element `e*` for large eruption triggering has been specified.
  * At least two experiment types have been defined with explicit falsification conditions and clear domain restrictions.

* **N_level: N1**

  * A stable narrative of "large eruptions as tail risk tension in configuration space" has been articulated.
  * Counterfactual worlds (World T and World F) have been framed in observable and tension terms.

### 9.2 Next measurable step toward E2

To progress from E1 to E2, Q097 should achieve at least one of the following under the encoding element `e*`:

1. **Prototype analysis on real data**

   * Implement a working prototype that:

     * ingests case studies of real eruptions and matched non eruptive intervals,
     * encodes them into `M_volc_reg` using `e*`,
     * computes `DeltaS_volc` and envelope vectors `E_volc_env`,
     * publishes tension profiles and hindcast statistics as open data.

2. **Synthetic model families and benchmarks**

   * Construct synthetic model families where:

     * eruptive and non eruptive trajectories are generated,
     * tail risk encodings based on `e*` are applied,
     * classification performance is systematically benchmarked and documented.

In both cases, the implementation must:

* use `e* in A_enc(Q097)` selected by `Encoding_key`,
* keep all libraries and parameters fixed before analyzing test data,
* publish enough detail for independent reproduction.

### 9.3 Long term role in the TU program

In the longer term, Q097 is expected to:

* serve as a reference node for physical tail risk problems in Earth systems,
* inform how to encode rare extreme events in other domains such as finance, infrastructure, and pandemics,
* provide a grounded example for AI alignment work on forecasting and decision making under low frequency, high impact hazards.

Q097 does not seek to replace domain specific volcanology. Instead, it proposes a way to:

* frame triggering of large eruptions as a structured tail risk tension problem,
* clarify where forecasting attempts are limited by information, encoding choices, or intrinsic unpredictability,
* create a stable interface between physical models, global risk narratives, and AI systems.

---

## 10. Elementary but precise explanation

This block gives an accessible explanation aligned with the effective layer encoding, without appealing to deep TU structure.

Large volcanic eruptions are among the most dramatic events on Earth. They can affect climate, ecosystems, and human societies. Scientists know a lot about how magma forms, how gases drive explosions, and how ash spreads. They still cannot reliably say when a very large eruption will happen at a specific volcano.

In this problem, we describe the situation in terms of a configuration space.

* Each state `m` describes the condition of a volcano and the surrounding crust, including:

  * how stressed the rocks are,
  * how much molten rock is present,
  * how much gas is dissolved or free,
  * how easy it is for magma or gas to move toward the surface,
  * what external forcing is acting on the system.

We then define two kinds of numbers:

* one that measures how similar the current state is to past quiet periods that did not erupt soon,
* one that measures how far the current state is from clearly metastable, safely parked configurations.

From these we build a tail risk tension score `DeltaS_volc`:

* low `DeltaS_volc` means the system looks similar to many past non eruptive states and lies inside a metastable region,
* high `DeltaS_volc` means the system looks unlike those safe states and more like states that might be close to failure.

There are two broad possibilities.

* In a world where triggering is partly predictable, this tail risk tension:

  * tends to rise before large eruptions,
  * stays moderate in most quiet times,
  * behaves in a similar way across different volcanoes and synthetic models.

* In a world where triggering is effectively opaque in the chosen configuration space:

  * tail risk tension does not reliably separate pre eruption periods from normal variability,
  * small admissible changes in how we encode the state completely change the pattern,
  * forecast performance based on `DeltaS_volc` is no better than naive baselines.

Q097 does not claim to solve eruption prediction. It does not tell us exactly when a given volcano will erupt. Instead, it offers:

* a way to ask whether useful tail risk structure exists in a chosen configuration space,
* explicit experiments that can falsify or support specific encodings,
* reusable tools for other problems where rare, extreme events arise in complex systems.

In the Tension Universe picture, Q097 is a prototype for how to treat extreme physical hazards as questions about tail risk tension, while staying strictly at the effective layer.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S problem collection and should be interpreted strictly at the effective layer.

### Scope of claims

* The goal of this document is to specify an **effective layer encoding element** `e* in A_enc(Q097)` for the problem of triggering large volcanic eruptions.

* It introduces:

  * an effective state space `M_volc` and its regular subset `M_volc_reg`,
  * an encoding class `A_enc(Q097)` and a selected element `e*` identified by `Encoding_key`,
  * observable fields, tail risk indices, a tail risk tension scalar `DeltaS_volc`,
  * counterfactual worlds, experiment templates, and engineering interfaces.

* It does **not** claim to:

  * prove or disprove any existing conjecture in volcanology or probability theory,
  * solve the canonical triggering problem in Section 1,
  * introduce any new theorem beyond what is already established in the cited literature.

* It should not be cited as evidence that the corresponding open problem in Earth sciences has been solved.

### Effective layer boundary

* All objects used here, including `M_volc`, `M_volc_reg`, `A_enc(Q097)`, `e*`, `TailRiskIndex`, `MetastabilityMargin`, `DeltaS_volc`, `E_volc_env`, `I_tail_contrast`, and the experiment templates, live entirely at the effective layer of TU.

* This page does **not** specify:

  * any TU core axiom system,
  * any hidden generative rules for semantic tension fields,
  * any mapping from raw physical data to TU core objects.

* Any reference to "worlds" or "configuration space" refers to effective layer models, not to fundamental ontological commitments.

### Encoding and falsification

* The header `Encoding_key` selects a single encoding element `e*`. All experiments and engineering uses in this page are about testing and using this specific element.

* Falsifying `e*` under the experiments in Section 6 means that this particular effective layer encoding is incompatible with the tested data and criteria. It does **not** prove that large eruption triggering is fundamentally unpredictable, nor that TU as a whole is invalid.

* If all elements in `A_enc(Q097)` are falsified under transparent criteria, Q097 remains as a canonical problem, and a revised encoding class must be constructed.

### Relation to other TU components

* This page relies on conventions and constraints defined in the TU charters for:

  * effective layer objects and boundaries,
  * encoding elements and fairness,
  * tension scales and thresholds.

* Any interpretation of `DeltaS_volc`, thresholds `epsilon_VOLC(e*)`, `delta_VOLC(e*)`, and experiment criteria must be consistent with those charters.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

---

**Index:**  
[`← Back to Event Horizon`](../EventHorizon/README.md)  
[`← Back to WFGY Home`](https://github.com/onestardao/WFGY)

**Consistency note:**  
This entry has passed the internal formal-consistency and symbol-audit checks under the current WFGY 3.0 specification.  
The structural layer is already self-consistent; any remaining issues are limited to notation or presentation refinement.  
If you find a place where clarity can improve, feel free to open a PR or ping the community.  
WFGY evolves through disciplined iteration, not ad-hoc patching.
