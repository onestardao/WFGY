# Q049 · Missing baryons problem

## 0. Header metadata

```txt
ID: Q049
Code: BH_COSMO_BARYON_DISTR_L3_049
Domain: Cosmology
Family: Baryon distribution
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Open
Semantics: continuous
E_level: E1
N_level: N1
Last_updated: 2026-01-24
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The standard cosmological model provides a precise estimate of the cosmic baryon density, often written in terms of a density parameter

```txt
Omega_b_true
```

inferred from early-universe probes such as big bang nucleosynthesis (BBN) and cosmic microwave background (CMB) anisotropies.

At low redshift, independent observations count baryons in different phases, for example:

* stars in galaxies
* cold and warm gas in galaxies
* hot gas in clusters and groups
* diffuse intergalactic and circumgalactic media

The **missing baryons problem** is the tension between:

* the theoretically and observationally well-constrained total baryon density `Omega_b_true`, and
* the sum of all observed baryon components at low redshift, which historically falls short of `Omega_b_true` by a significant fraction.

In other words:

> Where are the baryons that should exist according to early-universe cosmology, but that are not clearly accounted for in the census of visible and diffuse matter at later times?

### 1.2 Status and difficulty

Key facts about the status:

* CMB measurements provide high-precision values of `Omega_b_true` that are widely accepted within the standard cosmological model.
* Low-redshift surveys historically recovered only a fraction of this baryon density when summing known components (stars, cold gas, hot cluster gas).
* Subsequent observations have revealed additional baryon reservoirs, especially in warm-hot intergalactic medium (WHIM) and circumgalactic medium (CGM), but uncertainties remain large.
* Hydrodynamical cosmological simulations predict that a large fraction of baryons may reside in diffuse, low-density phases that are observationally challenging to detect.

The difficulty arises from:

* the need to combine multiple observational techniques (X-ray, UV absorption, radio, optical) across a wide range of environments and redshifts,
* uncertain feedback processes (for example galactic winds, AGN feedback) that redistribute baryons across phases and length scales,
* systematic uncertainties in converting observables into baryon mass estimates.

The problem is not whether baryons exist in some absolute sense, but whether we can:

* identify and quantify all major baryon reservoirs,
* reconcile the early-universe baryon budget with late-time phase-resolved baryon distributions,
* understand the dynamical processes that move baryons between phases.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q049 plays three roles:

1. It is a prototype of a **thermodynamic_tension** problem where a conserved quantity (baryon number) is distributed across multiple phases and environments.
2. It provides a concrete arena for studying **hidden reservoirs** and **incomplete observational coverage** in a high-precision cosmological setting.
3. It serves as a bridge node linking:

   * early-universe parameter inference (via Q044 and CMB-related nodes),
   * large-scale structure and feedback physics (via Q045 and related nodes),
   * cross-domain hidden-reservoir problems (for example climate and epidemiology nodes).

### References

1. Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters”, Astronomy and Astrophysics, 641, A6 (2020).
2. J. M. Shull, B. D. Smith, C. W. Danforth, “The baryon census in a multiphase intergalactic medium: 30 percent of the baryons may still be missing”, Astrophysical Journal, 759, 23 (2012).
3. F. Nicastro et al., “Observations of the missing baryons in the warm-hot intergalactic medium”, Nature, 558, 406–409 (2018).
4. N. Nelson et al., “The IllustrisTNG simulations: the distribution of baryons in the low-redshift Universe”, Monthly Notices of the Royal Astronomical Society, 475, 624–647 (2018).

---

## 2. Position in the BlackHole graph

This block records how Q049 sits inside the BlackHole graph as nodes and edges among Q001–Q125. Each edge is listed with a one-line reason that points to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q049 relies on at the effective layer.

* Q044 (BH_COSMO_INIT_COND_L3_044)
  Reason: Provides the primordial baryon density and initial conditions that define the global baryon budget observable Omega_b_true used in Q049.

* Q045 (BH_COSMO_LSS_FORM_L3_045)
  Reason: Encodes large-scale structure formation that determines where baryons can cluster, be shock-heated, or remain diffuse in the cosmic web.

* Q041 (BH_COSMO_DARKMATTER_L3_041)
  Reason: Specifies the gravitational potential wells and halo population that control baryon trapping and ejection across environments.

* Q043 (BH_COSMO_INFLATION_SPECTRUM_L3_043)
  Reason: Sets the primordial fluctuation spectrum that influences the later distribution of baryons among halos, filaments, and voids.

### 2.2 Downstream problems

These problems are direct reuse targets of Q049 components or depend on Q049’s tension structure.

* Q047 (BH_COSMO_EARLYBH_L3_047)
  Reason: Reuses baryon reservoir and phase-partition observables to constrain early supermassive black hole fueling histories.

* Q048 (BH_COSMO_H0_TENSION_L3_048)
  Reason: Uses the CosmicBudgetTensionScore_MB component to test consistency between baryon acoustic observables and expansion-rate inferences.

* Q050 (BH_COSMO_MULTIVERSE_TEST_L3_050)
  Reason: Compares phase-resolved baryon distributions across different candidate cosmological models using Q049 tension functionals.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q042 (BH_COSMO_DARKENERGY_L3_042)
  Reason: Both Q049 and Q042 encode thermodynamic_tension on cosmic inventory consistency, but for different components (baryons versus dark energy).

* Q048 (BH_COSMO_H0_TENSION_L3_048)
  Reason: Both are consistency_tension problems comparing early-universe parameter inferences with late-universe observables.

* Q091 (BH_CLIMATE_ECS_L3_091)
  Reason: Both study how hidden reservoirs and phase partitions (heat and carbon versus baryons) control global observables and feedbacks.

### 2.4 Cross-domain edges

Cross-domain edges connect Q049 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses thermodynamic_tension functionals on phase partitions to study energy-entropy budgets in information processing systems.

* Q091 (BH_CLIMATE_ECS_L3_091)
  Reason: Uses the MissingReservoirWorldTemplate component as an analogy for hidden heat and carbon reservoirs in the climate system.

* Q100 (BH_PANDEMICS_RESERVOIR_L3_100)
  Reason: Applies hidden-reservoir reasoning and coverage observables to pathogen reservoirs and surveillance gaps.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces
* observables and fields
* invariants and tension scores
* singular sets and domain restrictions

We do not describe any hidden generative rules or construction of internal TU fields from raw survey data or simulations.

### 3.1 State space

We assume the existence of a semantic state space

```txt
M
```

with the following interpretation at the effective layer:

* Each element `m` in `M` represents a coherent “baryon-budget world configuration” over a chosen redshift bin `z` and environment partition (for example clusters, groups, filaments, field galaxies, voids).
* A state `m` encodes, at a coarse-grained level:

  * estimates of baryon mass in different phases (for example stars, cold gas, warm gas, hot gas, diffuse WHIM, CGM) for the redshift bin,
  * indicators of observational completeness for each phase,
  * basic information about the large-scale structure environment fractions.

We do not specify how `m` is constructed from catalogs, maps, or simulation outputs. We only assume that:

* For any redshift bin and environment partition of interest, there exist states in `M` that summarize the phase-resolved baryon distribution and its uncertainties.

### 3.2 Observables and fields

We introduce the following effective observables on `M` for a given redshift bin `z`.

1. Global baryon density observables

```txt
Omega_b_true
Omega_b_obs(m, z)
```

* `Omega_b_true` is a scalar representing the true cosmic baryon density inferred from early-universe probes (for example BBN and CMB) under a fixed cosmological model.
* `Omega_b_obs(m, z)` is a scalar representing the total baryon density recovered from all explicitly tracked phases in state `m` at redshift `z`.

2. Phase-resolved baryon fractions

```txt
f_phase(m, phase, z)
```

* Input: state `m`, phase label, and redshift `z`.
* Output: a scalar fraction between 0 and 1 representing the fraction of the total baryon budget assigned to that phase in `m` at `z`.
* By construction:

  ```txt
  0 <= f_phase(m, phase, z) <= 1
  sum over phases of f_phase(m, phase, z) <= 1
  ```

3. Observational completeness indicators

```txt
C_obs(m, phase, z)
```

* Input: state `m`, phase, redshift `z`.
* Output: a scalar between 0 and 1 measuring how well that phase is constrained by observations at `z`.
* Interpretation:

  * `C_obs = 0` means essentially unconstrained or only upper limits,
  * `C_obs` near 1 means well-constrained with multiple independent probes.

4. Baryon budget mismatch observable

```txt
DeltaS_baryon(m, z) >= 0
```

* Measures the deviation between `Omega_b_true` and `Omega_b_obs(m, z)` in a normalized way.

* For example, a simple functional form is:

  ```txt
  DeltaS_baryon(m, z) =
      |Omega_b_true - Omega_b_obs(m, z)| / Omega_b_true
  ```

* Properties:

  ```txt
  DeltaS_baryon(m, z) >= 0
  DeltaS_baryon(m, z) = 0 if Omega_b_obs(m, z) = Omega_b_true
  ```

5. Phase-distribution mismatch observable

We choose a reference phase partition at redshift `z`, denoted by `f_ref(phase, z)`, taken from a fixed, admissible reference source (for example a specific simulation suite or review-level consensus).

We then define:

```txt
DeltaS_phase(m, z) >= 0
```

as a nonnegative scalar measuring the deviation between `f_phase(m, phase, z)` and `f_ref(phase, z)` across phases, for example:

```txt
DeltaS_phase(m, z) =
    sum over phases of w_phase(phase, z) *
    |f_phase(m, phase, z) - f_ref(phase, z)|
```

where:

* `w_phase(phase, z)` are fixed nonnegative weights that sum to 1 across phases at each `z`,
* both `f_phase` and `f_ref` are interpreted as fractions of `Omega_b_true`.

Properties:

```txt
DeltaS_phase(m, z) >= 0
DeltaS_phase(m, z) = 0 if f_phase(m, phase, z) = f_ref(phase, z) for all phases
```

### 3.3 Admissible encoding class and fairness constraints

To avoid hidden tuning, we restrict attention to an admissible class of encodings with the following properties:

1. The reference baryon density `Omega_b_true` is fixed by early-universe probes under a specified cosmological model and is not adjusted based on late-time baryon census results.

2. The reference phase partition `f_ref(phase, z)` is chosen from a fixed, documented reference (for example a particular simulation suite or a published review) before computing `DeltaS_phase` on any states `m`.

3. The weights `w_phase(phase, z)` and the combination weights used later for tension functionals are fixed ahead of time and do not depend on the specific data realized in `m`.

4. Within this class, transformations of the encoding that preserve the above properties are allowed, but any mapping that chooses `f_ref` or weights in response to the observed `f_phase(m, phase, z)` is considered outside the admissible class.

These constraints ensure that tension measures cannot be driven to zero by retroactively fitting reference partitions or weights to match the data.

### 3.4 Effective tension tensor components

We define an effective combined mismatch:

```txt
DeltaS_total(m, z) =
    alpha * DeltaS_baryon(m, z) + beta * DeltaS_phase(m, z)
```

where:

* `alpha > 0` and `beta > 0` are fixed constants chosen within the admissible encoding class,
* `DeltaS_total(m, z) >= 0` for all `m` and `z`.

Following the TU core decision, we define an effective tension tensor:

```txt
T_ij(m, z) = S_i(m, z) * C_j(m, z) * DeltaS_total(m, z) * lambda(m, z) * kappa
```

where:

* `S_i(m, z)` represents the strength of the i-th semantic or physical source component (for example how strongly a particular environment or phase enters the analysis).
* `C_j(m, z)` represents the sensitivity of the j-th cognitive or downstream component to baryon distribution mismatches (for example predictive models or AI agents that rely on baryon budgets).
* `lambda(m, z)` is a convergence-state factor indicating whether local reasoning or modeling is convergent, recursive, divergent, or chaotic.
* `kappa` is a coupling constant setting the overall scale of baryon-distribution thermodynamic_tension in this encoding.

The indexing sets for `i` and `j` are not specified at the effective layer. It is sufficient that for each `m` and `z`, `T_ij(m, z)` is well defined and finite for all relevant indices.

### 3.5 Singular set and domain restrictions

Some observables may become undefined or unreliable if the data coverage is too poor or if the encoding is inconsistent. We define the singular set:

```txt
S_sing = {
  m in M :
  Omega_b_obs(m, z) is undefined or not finite
  or DeltaS_baryon(m, z) is undefined
  or DeltaS_phase(m, z) is undefined
}
```

for the redshift bin under consideration.

We then restrict attention to the regular subset:

```txt
M_reg = M \ S_sing
```

Rules:

* All tension analysis for Q049 is performed only on states `m` in `M_reg`.
* If an attempted evaluation of `DeltaS_baryon` or `DeltaS_phase` encounters a state in `S_sing`, the result is recorded as “out of domain” and is not interpreted as evidence for or against any cosmological model.

---

## 4. Tension principle for this problem

This block states how Q049 is characterized as a tension problem within TU at the effective layer.

### 4.1 Core tension functional

We define a baryon-budget tension functional:

```txt
Tension_MB(m, z) =
    alpha * DeltaS_baryon(m, z) + beta * DeltaS_phase(m, z)
```

with the same `alpha`, `beta` as in Block 3.4. This functional satisfies:

```txt
Tension_MB(m, z) >= 0 for all m in M_reg
Tension_MB(m, z) = 0 only if
  Omega_b_obs(m, z) = Omega_b_true and
  f_phase(m, phase, z) = f_ref(phase, z) for all phases
```

The exact numerical values of `alpha` and `beta` are part of the encoding design but are fixed ahead of any particular experiment, within the admissible encoding class described in Block 3.3.

### 4.2 Missing baryons as a low-tension principle

At the effective layer, a “resolved missing baryons” world is one in which:

* For relevant redshift bins and environments, there exist world-representing states `m` in `M_reg` such that

  ```txt
  Tension_MB(m, z) <= epsilon_MB(z)
  ```

  where `epsilon_MB(z)` is a small threshold that reflects observational uncertainties and modeling limitations.

* As data quality and coverage improve, `epsilon_MB(z)` can be refined but does not grow without bound purely due to adding more reliable information.

* The phase partitions and global baryon budgets remain jointly compatible with early-universe constraints within these low-tension bands.

In this view, resolving the missing baryons problem means showing that the universe admits low-tension configurations across the relevant redshift range for some admissible encoding.

### 4.3 Persistent missing baryons as high tension

Conversely, a “persistent missing baryons” world is one in which:

* For any admissible encoding and reasonable refinement of observational data, there are redshift bins or environments where world-representing states `m` in `M_reg` satisfy

  ```txt
  Tension_MB(m, z) >= delta_MB(z)
  ```

  for some strictly positive `delta_MB(z)` that cannot be reduced below a chosen small threshold without introducing inconsistency with the early-universe constraints or with the observed data.

* The high-tension behavior is not localized to isolated data artifacts but persists under:

  * improved measurements within the same observational strategy,
  * independent observational methods targeting the same reservoirs,
  * different choices of reference phase partitions drawn from the admissible class.

At the effective layer, Q049 asks whether the universe belongs to a low-tension baryon-budget world or to a world where a nontrivial fraction of baryons remains permanently hidden in ways that resist reconciliation.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds, described strictly through observable patterns and tension behaviors:

* World T: missing baryons effectively resolved.
* World F: missing baryons real and persistent.

### 5.1 World T (resolved baryons, low tension)

In World T:

1. Global budget closure

   * For each redshift bin within a chosen range (for example z between 0 and 2), there exist states `m_T(z)` in `M_reg` such that

     ```txt
     DeltaS_baryon(m_T, z) is small and stable
     ```

     when data are refined and combined across independent surveys.

2. Phase-partition compatibility

   * The phase mismatch `DeltaS_phase(m_T, z)` remains within narrow bands compatible with one or more fixed reference partitions taken from the admissible class.

3. Multi-scale stability

   * When the environment partition is refined (for example by splitting halos into mass bins or filaments into density bins), the aggregated `Tension_MB(m_T, z)` remains in a low band, up to expected fluctuations from sampling and systematics.

4. No unexplained high-tension pockets

   * Any local high tension in `Tension_MB` can be traced to identifiable systematics, inadequate modeling, or clearly incomplete surveys, and it decreases as those issues are resolved.

### 5.2 World F (persistent missing baryons, high tension)

In World F:

1. Budget gap

   * There exist redshift bins and environments such that, for all admissible encodings and realistic data refinements, any world-representing state `m_F(z)` in `M_reg` satisfies

     ```txt
     DeltaS_baryon(m_F, z) >= delta_b > 0
     ```

     where `delta_b` is a strictly positive threshold representing a significant fraction of the total baryon budget.

2. Systematic phase mismatch

   * For certain phases or environments, `DeltaS_phase(m_F, z)` does not converge toward reference partitions even when observational completeness `C_obs` increases.

3. Robust high-tension regions

   * The tension functional `Tension_MB(m_F, z)` retains a high baseline for specific redshift and environment ranges, and this high-tension pattern remains under multi-instrument and multi-method observational campaigns.

4. Hidden-reservoir inference pressure

   * Any attempt to reduce `Tension_MB(m_F, z)` within the admissible encoding class forces the introduction of new, poorly constrained phases or mechanisms that themselves remain tension-heavy in other parts of the data space.

### 5.3 Interpretive note

These counterfactual worlds do not assume or construct any internal TU generative rules. They describe how observable baryon budgets and phase partitions would behave, and how the resulting tension measures would respond, if the missing baryons problem were effectively resolved or if it remained fundamentally unresolved.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q049 encoding,
* distinguish between different baryon-budget tension models,
* falsify specific encoding choices for `DeltaS_baryon`, `DeltaS_phase`, and `Tension_MB`.

These experiments do not decide the ultimate truth of cosmological models but can reject particular TU encodings for Q049.

### Experiment 1: Low-redshift baryon census tension scan

*Goal:*
Test whether a specific choice of `Tension_MB` encoding produces stable and interpretable tension profiles when applied to existing low-redshift baryon census data.

*Setup:*

* Input data:

  * Published estimates of baryon content in different phases (stars, cold gas, hot intracluster medium, WHIM, CGM, other diffuse components) for redshift bins in the range z between 0 and 1.
  * Corresponding estimates of observational completeness for each phase.

* Choose:

  * A fixed value of `Omega_b_true` from a standard CMB analysis under a specified cosmological model.
  * A fixed reference phase partition `f_ref(phase, z)` from a selected simulation suite or review.
  * Fixed weights `alpha`, `beta`, and `w_phase(phase, z)` within the admissible encoding class.

*Protocol:*

1. For each redshift bin `z` with available data, construct an effective state `m_data(z)` in `M_reg` encoding:

   * `Omega_b_obs(m_data, z)`
   * `f_phase(m_data, phase, z)`
   * `C_obs(m_data, phase, z)`

2. Compute:

   * `DeltaS_baryon(m_data, z)`
   * `DeltaS_phase(m_data, z)`
   * `Tension_MB(m_data, z)`

3. Record the set of tension values across all `z`, along with the associated completeness indicators.

4. Optionally repeat the procedure with alternative but still admissible choices of `f_ref` to test robustness.

*Metrics:*

* Distribution of `Tension_MB(m_data, z)` over redshift.
* Correlation of `Tension_MB` with `C_obs` (for example whether high tension is always associated with very low completeness).
* Stability of `Tension_MB` under admissible changes in reference phase partitions.

*Falsification conditions:*

* If, for all admissible choices of reference partition and weights, the encoding yields tension profiles that are:

  * extremely sensitive to small arbitrary changes in `f_ref` or `w_phase`, or
  * dominated by numerical artifacts rather than by physically interpretable patterns,

  then the current definition of `DeltaS_baryon`, `DeltaS_phase`, or `Tension_MB` is considered falsified for Q049.

* If `Tension_MB(m_data, z)` is either nearly zero or extremely large in ways that cannot be traced to data completeness or known systematics, the encoding is flagged as misaligned and subject to revision.

*Semantics implementation note:*
This experiment treats all quantities as continuous-field summaries consistent with the metadata declaration and does not introduce discrete or hybrid reinterpretations within this block.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can reject specific tension encodings for Q049, but it does not by itself determine whether the cosmological missing baryons problem is fully resolved.

---

### Experiment 2: Simulation versus observation cross-tension

*Goal:*
Assess whether the Q049 encoding can distinguish, in a stable and interpretable way, between baryon distributions predicted by simulations and those inferred from observations, without being overwhelmed by trivial systematics.

*Setup:*

* Input data:

  * A set of hydrodynamical cosmological simulation snapshots providing phase-resolved baryon distributions at selected redshifts.
  * A matching set of observational baryon census data for similar redshift ranges and environments.

* Use the same `Omega_b_true`, reference phase partition `f_ref`, and weights `alpha`, `beta`, `w_phase` as in Experiment 1, within the admissible encoding class.

*Protocol:*

1. For each chosen redshift `z`, construct:

   * `m_sim(z)` states representing simulation-based phase partitions and total baryon budgets.
   * `m_obs(z)` states representing observation-based phase partitions and total baryon budgets.

2. Compute `DeltaS_baryon`, `DeltaS_phase`, and `Tension_MB` for both `m_sim(z)` and `m_obs(z)`.

3. Compare the distributions of `Tension_MB` across redshifts and environments for simulation and observation.

4. Optionally vary aspects of the simulation physics (for example feedback strength) to see how tension profiles shift.

*Metrics:*

* Differences between `Tension_MB(m_sim, z)` and `Tension_MB(m_obs, z)` across redshifts.
* Sensitivity of tension differences to changes in simulation parameters.
* Robustness of tension differences under admissible changes of `f_ref` within the same simulation family.

*Falsification conditions:*

* If the encoding consistently fails to produce meaningful tension differences between simulations and observations, even when known discrepancies exist in the underlying data, then the encoding is considered too insensitive and rejected for Q049.

* If small, physically unmotivated adjustments to encoding parameters or reference partitions can arbitrarily flip which side (simulation or observation) appears more tension-heavy, then the encoding is considered unstable and rejected.

*Semantics implementation note:*
Both simulations and observations are reduced to the same type of continuous-field summaries before computing tension, preserving consistency with the declared field_type and semantics.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment probes the suitability of the tension functional, not the correctness of the simulations or observations themselves.

---

## 7. AI and WFGY engineering spec

This block describes how Q049 can be used as an engineering module for AI systems within the WFGY framework at the effective layer.

### 7.1 Training signals

We define several training signals that can be used as auxiliary objectives or diagnostics.

1. `signal_baryon_budget_consistency`

   * Definition:

     ```txt
     signal_baryon_budget_consistency(m, z) =
         DeltaS_baryon(m, z)
     ```

   * Purpose: penalize internal states or outputs that imply baryon budgets strongly inconsistent with `Omega_b_true` when the context assumes a standard cosmological model.

2. `signal_phase_partition_stability`

   * Definition:

     ```txt
     signal_phase_partition_stability(m, z) =
         DeltaS_phase(m, z)
     ```

   * Purpose: encourage internal representations that yield phase partitions compatible with the chosen reference patterns when such compatibility is part of the assumed background.

3. `signal_missing_reservoir_flag`

   * Definition:

     ```txt
     signal_missing_reservoir_flag(m, z) =
         1 if Tension_MB(m, z) >= tau_MB
         0 otherwise
     ```

     where `tau_MB` is a threshold chosen to represent a significant baryon-budget tension.

   * Purpose: flag contexts where the model should explicitly acknowledge missing reservoirs or limited observational coverage instead of inventing unsupported reservoirs.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q049 structures without exposing any TU deep generative rules.

1. `CosmicBudgetTensionHead`

   * Role: given an internal embedding of a cosmology-related context, produce estimates of `DeltaS_baryon`, `DeltaS_phase`, and `Tension_MB` as auxiliary outputs.
   * Interface:

     * Inputs: internal embeddings representing the current cosmological scenario or explanation.
     * Outputs: scalar estimates `DeltaS_baryon_hat`, `DeltaS_phase_hat`, `Tension_MB_hat` and optional uncertainty ranges.

2. `PhasePartitionObserver`

   * Role: extract coarse phase-partition features (for example approximate fractions in stars, gas, WHIM, CGM) from text or data representations.
   * Interface:

     * Inputs: context embeddings, optional structured inputs describing environments.
     * Outputs: a vector of phase fraction estimates that can be fed into tension heads or consistency filters.

3. `MissingReservoirDetector`

   * Role: monitor tension outputs and decide when answers should include explicit statements about observational incompleteness or unresolved reservoirs.
   * Interface:

     * Inputs: `Tension_MB_hat`, data completeness indicators if present.
     * Outputs: a control signal that modulates answer templates (for example adding phrases like “current observations are incomplete” or “a significant fraction of baryons may reside in difficult-to-detect phases”).

### 7.3 Evaluation harness

We suggest an evaluation harness to test AI systems augmented with Q049-aware modules.

1. Task selection

   * Construct a set of questions and multi-step prompts about:

     * cosmic baryon census,
     * WHIM and CGM roles,
     * comparison between early-universe baryon density and low-redshift observations.

2. Conditions

   * Baseline condition: the model answers questions without any explicit CosmicBudgetTensionHead or MissingReservoirDetector.
   * TU condition: the model uses these modules and their signals as auxiliary guidance.

3. Metrics

   * Scientific coherence: consistency of baryon budget numbers and phase descriptions across multiple questions and follow-up prompts.
   * Acknowledgment of uncertainty: frequency with which the model correctly indicates incomplete observational coverage instead of overstating precision.
   * Cross-question stability: whether the model maintains a consistent narrative about where baryons reside and how certain that knowledge is.

### 7.4 60-second reproduction protocol

A minimal protocol to let external users experience the practical impact of Q049 encoding.

* Baseline setup

  * Prompt: ask the AI to explain the missing baryons problem, list main baryon components at low redshift, and comment on their relative importance.
  * Observation: record whether the explanation is vague about phases (for example ignores WHIM and CGM), inconsistent about the baryon budget, or overconfident about having completely solved the problem.

* TU encoded setup

  * Prompt: same question, but with an additional instruction to the AI to:

    * use a “baryon budget tension” score as an internal check,
    * explicitly identify any phases or environments where tension remains high or data are incomplete.

  * Observation: record whether the explanation becomes more structured, with clear mention of known reservoirs, data gaps, and unresolved issues.

* Comparison metric

  * Use a rubric for:

    * completeness of phase listing,
    * correctness of qualitative statements about each reservoir,
    * explicit handling of uncertainty and missing data.

* What to log

  * Prompts, responses, and any associated auxiliary tension estimates.
  * This allows independent reviewers to check whether the model’s behavior changes in ways consistent with the Q049 tension framing.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q049 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `CosmicBudgetTensionScore_MB`

   * Type: functional

   * Minimal interface:

     ```txt
     Inputs:
       Omega_b_true
       Omega_b_obs
       {f_phase(phase)}
       {w_phase(phase)}
     Output:
       tension_value = Tension_MB
     ```

   * Preconditions:

     * Inputs describe a consistent baryon census for a given redshift bin.
     * Phase fractions and weights sum appropriately and are taken from the admissible encoding class.

2. ComponentName: `PhasePartitionFieldDescriptor`

   * Type: field

   * Minimal interface:

     ```txt
     Inputs:
       environment_descriptor
       redshift z
     Output:
       phase_fraction_vector
     ```

   * Preconditions:

     * Environments are described at a coarse-grained level (for example halo mass bins, filament versus void, cluster versus field).
     * Phase fractions form a valid vector (entries between 0 and 1, sum less than or equal to 1).

3. ComponentName: `MissingReservoirWorldTemplate`

   * Type: experiment_pattern

   * Minimal interface:

     ```txt
     Inputs:
       model_class
     Outputs:
       World_T_pattern
       World_F_pattern
       tension_evaluation_protocol
     ```

   * Preconditions:

     * Model class admits a partition of a conserved quantity (for example baryons, energy, carbon, pathogen population) into observable and potentially hidden reservoirs.
     * A notion of global budget and phase partitions is available at the effective layer.

### 8.2 Direct reuse targets

1. Q047 (Origin of supermassive black holes)

   * Reused component: `PhasePartitionFieldDescriptor`.
   * Why it transfers: SMBH growth requires knowledge of gas and baryon availability in halos and filaments, which can be summarized by the phase partition descriptor.
   * What changes: environments include specific halo mass and redshift ranges relevant to BH seeding and early accretion.

2. Q048 (Hubble constant tension)

   * Reused component: `CosmicBudgetTensionScore_MB`.
   * Why it transfers: distance ladder and BAO-based H0 inferences depend on baryon acoustic signatures and baryon distribution, which can be cross-checked using the same tension score.
   * What changes: focus shifts to how baryon distribution affects calibration of observables entering the H0 analysis.

3. Q091 (Equilibrium climate sensitivity)

   * Reused component: `MissingReservoirWorldTemplate`.
   * Why it transfers: climate problems also involve potentially hidden reservoirs (for example deep ocean heat, soil carbon) and incomplete coverage; the template can be reused with different observables.
   * What changes: conserved quantity becomes heat or carbon rather than baryon number, and the phase labels are climate-relevant.

4. Q100 (Environmental drivers of pandemic risk)

   * Reused component: `MissingReservoirWorldTemplate`.
   * Why it transfers: pathogen reservoirs and surveillance gaps can be encoded as hidden versus observed compartments, analogous to missing baryon reservoirs.
   * What changes: model class and phases are epidemiological rather than cosmological, but the idea of persistent tension in the budget carries over.

---

## 9. TU roadmap and verification levels

This block explains how Q049 is positioned along the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective-layer encoding of the missing baryons problem has been specified.
  * Observables, mismatch measures, and a tension functional are defined, with an admissible encoding class and singular set.

* N_level: N1

  * The narrative linking early-universe baryon budgets, low-redshift phase partitions, and hidden reservoirs is explicit but still at an outline level.
  * Counterfactual worlds and experiments are specified but not yet tied to concrete numerical implementations.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented:

1. A concrete implementation of `Tension_MB` that operates on published baryon census compilations, providing open tension profiles as a function of redshift and environment.

2. A comparative study where several candidate phase partitions and reference models are tested within the admissible encoding class, with results documented in a way that independent groups can reproduce.

3. An AI evaluation harness, as described in Block 7.3, deployed on a benchmark set of cosmology questions, with before-versus-after analysis of how baryon-budget reasoning changes.

All of these steps respect the effective-layer boundary because they operate on observable summaries and documented reference models only.

### 9.3 Long-term role in the TU program

In the long term, Q049 is expected to serve as:

* The canonical hidden-reservoir node for cosmology, illustrating how thermodynamic_tension on conserved quantities is used when observations are incomplete.
* A template for constructing and testing similar encodings in other domains that face missing-reservoir problems (for example climate, ecology, epidemiology).
* A calibration point for AI systems that must reason about global budgets, reservoirs, and observational gaps without overstating certainty or inventing unsupported components.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non-experts, while still aligned with the effective-layer description.

Cosmology tells us, from early-universe physics, how many baryons the universe should contain. That total amount is encoded in a number called `Omega_b_true`. It comes from careful analysis of the cosmic microwave background and nuclear reactions in the first minutes after the big bang.

Later in cosmic history, we can look around and try to count where those baryons actually are:

* in stars,
* in gas inside galaxies,
* in very hot gas inside clusters of galaxies,
* in more diffuse material between galaxies and around galaxies.

When astronomers add up all those pieces, they do not always get back the total that early-universe physics says should be there. The “missing baryons problem” is simply the question:

> In which phases and environments do the “missing” baryons hide, and how sure are we about our current census?

In the Tension Universe view, we do not try to build a new cosmological model or solve the detailed astrophysics. Instead, we:

1. Represent each possible “world configuration” as a state that summarizes:

   * how many baryons are counted in each phase,
   * how complete the observations are for each phase.

2. Compare two things in each such state:

   * the total baryon density we infer from observations at late times, and
   * the total baryon density predicted by early-universe physics.

3. Measure how much tension there is between:

   * the global budget from early-universe probes, and
   * the phase-resolved census at later times.

This tension is encoded in a number we call `Tension_MB`. It is:

* small when observations and models agree on where the baryons are,
* large when there is a significant shortfall or a very unusual phase distribution.

We then imagine two types of worlds:

* In a “resolved” world, as we gather better data and combine different observations, the tension stays small and stable. The missing baryons problem becomes an accounting exercise that we can close.

* In a “persistent” world, even with improved data, tension remains high in specific redshift ranges or environments. We are forced to conclude that there are reservoirs we have not yet understood, or that our models of how baryons move between phases are incomplete.

Q049, in this framework, does not claim to answer where every baryon is. It provides:

* a precise way to talk about how well we are doing with the baryon census,
* a set of observables and experiments for testing different encodings of “missing baryons” tension,
* components that can be reused in other problems where a conserved quantity seems to be missing from the obvious places.

This keeps the analysis at an effective layer: we work with what can be observed, summarized, and compared, without exposing or relying on any hidden generative rules of the Tension Universe itself.
