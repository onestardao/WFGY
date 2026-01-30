<!-- QUESTION_ID: TU-Q041 -->
# Q041 · Nature of dark matter

## 0. Header metadata

```txt
ID: Q041
Code: BH_COSMO_DARKMATTER_L3_041
Domain: Cosmology
Family: Dark matter and cosmic structure
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework:

* The goal is to specify state spaces, observables, mismatch quantities, tension functionals, and experiments that encode the dark matter problem as a consistency_tension task.
* This document does not modify the canonical dark matter problem as stated in standard cosmology, and does not identify or endorse any specific microphysical dark matter candidate.
* This document does not prove or disprove the canonical problem, does not introduce new physical theorems, and must not be cited as evidence that the dark matter problem has been solved.
* No deep generative rule, axiom system, or constructive procedure for TU internal fields is described. All such structures remain outside the scope of this file.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem asks:

```txt
What is the nature of dark matter, and how can one reconcile all major astrophysical
and cosmological observations with a single, coherent description of the unseen mass
component that dominates the matter content of the universe?
```

In standard cosmology, several lines of evidence indicate the presence of non luminous, predominantly non baryonic matter that interacts primarily through gravity. These include:

* galaxy rotation curves that remain approximately flat at large radii instead of declining,
* velocity dispersions and dynamics of galaxy clusters,
* gravitational lensing by galaxies and clusters,
* anisotropies in the cosmic microwave background (CMB),
* large scale structure and the matter power spectrum inferred from galaxy surveys and CMB data.

The dark matter problem, in its canonical form, is not simply to add an extra free mass component to fits. The task is to identify a description that:

1. explains the full set of observations across scales from galaxies to the largest structures,
2. is compatible with known constraints on baryons, radiation, and neutrinos,
3. remains stable as measurements and modelling precision improve.

At the effective level, two broad classes of approaches are considered:

* genuine dark matter sectors, often modelled as cold or warm collisionless particles, self interacting species, axions or related fields, or compact objects such as primordial black holes,
* modifications to gravity or inertia, sometimes combined with reduced dark matter sectors.

Q041 treats this situation as a question about whether a low tension description of the unseen mass sector exists inside a constrained encoding class, rather than as a claim that one specific microphysical model is correct.

### 1.2 Status and difficulty

Empirically, the cold dark matter plus cosmological constant model provides a good first order description of many observables. However:

* small scale structure shows tensions with simple cold collisionless dark matter descriptions, such as core versus cusp issues in galaxy centres and the abundance of small satellites,
* the detailed properties of dark matter, including its mass, internal degrees of freedom, and interactions, remain unknown,
* alternative frameworks, including modified gravity or hybrid scenarios, can fit some subsets of data but frequently struggle to match the full multi channel evidence simultaneously under realistic constraints.

No single candidate or framework has been confirmed. Direct detection experiments, collider searches, and astrophysical probes have so far yielded null or ambiguous results. The problem remains open and central to cosmology and particle astrophysics.

Within the BlackHole project, the difficulty is amplified by the need to unify:

* high precision cosmological measurements,
* complex astrophysical environments with baryonic feedback,
* and an unseen sector that must be inferred indirectly through multi channel consistency.

This document does not identify any specific microphysical dark matter candidate and does not claim to resolve the dark matter problem. It only specifies an effective layer encoding and a programme of falsifiable experiments.

### 1.3 Role in the BlackHole graph

Within the BlackHole S problem collection, Q041 acts as:

1. the central node for all problems that involve unseen mass and its role in structure formation,
2. a prototype for consistency_tension problems where multiple observational channels must agree about a hidden sector,
3. a source of reusable components for:

   * dark energy and cosmic acceleration questions,
   * early universe structure and the Hubble constant tension,
   * hidden mechanism reasoning in other domains.

All edges in the BlackHole graph describe reuse of effective layer components or patterns. They do not express logical implication that any connected problem is solved.

### References

1. Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters”, Astronomy and Astrophysics, 641, A6 (2020).
   Includes a detailed discussion of matter density parameters, dark matter abundance, and the role of dark matter in the standard cosmological model.

2. G. Bertone and D. Hooper, “History of dark matter”, Reviews of Modern Physics, 90, 045002 (2018).
   A broad review of the evidence for dark matter and the main classes of particle and astrophysical candidates.

3. J. L. Feng, “Dark Matter Candidates from Particle Physics and Methods of Detection”, Annual Review of Astronomy and Astrophysics, 48, 495–545 (2010).
   Surveys particle physics candidates and experimental strategies for dark matter.

4. A current institutional cosmology overview on dark matter (for example NASA or ESA).
   Provides a high level summary of the evidence for dark matter, typical parameter values, and current experimental searches.

---

## 2. Position in the BlackHole graph

This block records the planned position of Q041 in the Q001–Q125 graph, in terms of upstream, downstream, parallel, and cross domain edges. Each edge has a one line reason that refers to concrete components or tension types at the effective layer.

### 2.1 Upstream problems

These problems supply conceptual and technical scaffolding for Q041.

* Q021 (BH_PHYS_QG_L3_021)
  Reason: provides gravitational sector background and constraints on allowed large scale gravitational behaviour. Q041 uses these constraints when defining admissible encodings for cosmic fields.

* Q025 (BH_PHYS_BARYON_ASYM_L3_025)
  Reason: fixes the allowed baryon budget and asymmetry, which Q041 reuses when defining baryon fraction mismatch and baryon related tension.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: supplies thermodynamic style invariants and energy budget constraints that Q041 reuses for matter and radiation consistency_tension.

* Q043 (BH_COSMO_INFLATION_L3_043)
  Reason: provides primordial perturbation spectra and refine(k) style multi scale power spectrum handling that Q041 uses in spectral mismatch observables.

### 2.2 Downstream problems

These problems reuse Q041 components or treat Q041 as a prerequisite at the effective layer.

* Q042 (BH_COSMO_DARKENERGY_L3_042)
  Reason: reuses Q041 MultiChannel_Cosmo_Descriptor and energy budget consistency patterns to define tension between dark matter, dark energy, and geometry.

* Q047 (BH_COSMO_EARLYBH_L3_047)
  Reason: uses Q041 small scale clustering tension components to constrain early black hole formation scenarios.

* Q048 (BH_COSMO_H0_TENSION_L3_048)
  Reason: reuses DM_Consistency_Tension to relate dark matter assumptions to the Hubble constant tension between early and late universe probes.

* Q049 (BH_COSMO_BARYON_DISTR_L3_049)
  Reason: uses Q041 baryon fraction mismatch and S_sing_DM to frame the missing baryons problem relative to total matter.

### 2.3 Parallel problems

These nodes share similar tension structures without direct component reuse.

* Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)
  Reason: both deal with hidden microscopic sectors that are inferred from macroscopic evidence under a consistency_tension pattern.

* Q039 (BH_PHYS_QTURBULENCE_L3_039)
  Reason: both involve multiscale fields where global statistics emerge from complex dynamics and require multi scale tension invariants.

* Q050 (BH_COSMO_MULTIUNI_L3_050)
  Reason: both consider competing cosmological scenarios constrained by indirect observations of unseen sectors.

### 2.4 Cross domain edges

These edges connect Q041 to problems in other domains that reuse its effective layer patterns.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: reuses Q041 treatment of energy and information budgets to structure information thermodynamics in computational settings.

* Q091 (BH_EARTH_CLIMATE_SENS_L3_091)
  Reason: adopts Q041 parameter sensitivity and multi channel evidence templates for climate sensitivity and feedback analysis.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: mirrors Q041 pattern of constraining a hidden mechanism with multiple observational channels when reasoning about aligned agents.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: reuses the idea of inferring latent structure from many coarse projections, with Q041 as a cosmological prototype.

---

## 3. Tension Universe encoding (effective layer)

All content in this block stays at the TU effective layer. We only specify:

* state spaces,
* effective fields and observables,
* mismatch quantities and tension functionals,
* singular sets and domain restrictions.

We do not describe any deep generative rule, any mapping from raw data to TU lower level fields, or any constructive procedure for internal cosmological fields.

### 3.1 State space

We introduce a state space:

```txt
M_DM
```

Interpretation at the effective layer:

* Each element `m` in `M_DM` represents a coherent dark matter cosmology configuration for a finite spacetime region. It encodes:

  * coarse grained total matter density over comoving coordinates,
  * effective baryonic and dark matter densities,
  * summaries of observables from multiple channels,
  * meta information about resolution and uncertainties.

We require only that:

* for any chosen observation programme and scale range, it is possible to construct states in `M_DM` that encode internally consistent summaries of the relevant data,
* these states respect basic physical constraints such as positivity of densities and consistent matter content at the effective layer.

We do not specify how observational data, simulations, or theoretical models are turned into elements of `M_DM`.

### 3.2 Effective fields and observables

On `M_DM` we define the following effective observables.

1. Total matter density field

```txt
rho_tot(m; x) >= 0
```

* `x` denotes a comoving position in a bounded region of space.
* `rho_tot` summarises the total matter density at that location in state `m`.

2. Baryonic matter density field

```txt
rho_baryon(m; x) >= 0
```

* represents the effective baryonic matter distribution in state `m`, including stars, gas, and other visible or normal components.

3. Dark matter density field

```txt
rho_DM(m; x) >= 0
```

* represents the effective dark matter distribution.
* at the effective layer this is defined as the part of `rho_tot` not accounted for by known baryons and radiation after a chosen encoding step.

4. Matter power spectrum summary

```txt
P_matter(m; k_bin)
```

* for each discrete wave number bin `k_bin` in a finite set, `P_matter` summarises the matter power spectrum amplitude inferred in state `m`.

5. Observation channel summaries

We assume a finite index set of channels `i` for independent lines of evidence. For each channel:

```txt
obs_channel_i(m)
```

summarises the relevant data and modelling outputs. Examples include:

* galaxy rotation curve summaries,
* gravitational lensing maps compressed into a small set of parameters,
* cluster velocity dispersion statistics,
* CMB anisotropy summaries related to matter content,
* large scale structure statistics derived from surveys.

We do not specify the internal structure of `obs_channel_i(m)`; we only require that they are finite dimensional and consistent with basic physical constraints at the effective layer.

6. Reference profiles

We introduce reference objects that represent benchmark expectations for certain scenarios.

* a standard cold dark matter like matter power spectrum:

  ```txt
  ref_P_CDM(k_bin)
  ```

  defined over the same set of `k_bin`.

* a reference baryon fraction profile:

  ```txt
  ref_f_baryon
  ```

  which can be taken as a constant or a mild function of scale inside an allowed range based on nucleosynthesis and CMB constraints.

These reference profiles are chosen within an admissible class described later and are fixed before any particular experiment on a given data set.

### 3.3 Mismatch observables

We define non negative mismatch quantities.

1. Spectral mismatch

```txt
DeltaS_spectrum(m) =
  norm_spectrum( P_matter(m; k_bin) - ref_P_CDM(k_bin) )
```

where:

* `norm_spectrum` is a fixed norm or seminorm on the finite vector of power spectrum differences,
* `DeltaS_spectrum(m) >= 0`,
* `DeltaS_spectrum(m) = 0` when the encoded power spectrum exactly matches the chosen reference profile at the tested resolution.

2. Channel consistency mismatch

```txt
DeltaS_channels(m) =
  aggregate_channels( inconsistency_i(m) over all channels i )
```

Here:

* `inconsistency_i(m)` measures how far channel `i` is from being explainable by a single dark matter density field and baryon fraction within the encoding class,
* `aggregate_channels` combines the channel wise inconsistencies into a single non negative scalar,
* `DeltaS_channels(m) >= 0`,
* `DeltaS_channels(m) = 0` if all channels are mutually consistent with a single dark matter and baryon configuration in the encoding class.

3. Baryon fraction mismatch

For each state `m` we define an effective baryon fraction summary, for example:

```txt
f_baryon(m) =
  average over x in region of
  rho_baryon(m; x) / max( rho_tot(m; x), epsilon_small )
```

where `epsilon_small` is a fixed small constant to avoid division by zero. We then set:

```txt
DeltaS_baryon(m) =
  abs( f_baryon(m) - ref_f_baryon )
```

with the requirement that:

* `DeltaS_baryon(m) >= 0`,
* `DeltaS_baryon(m) = 0` when the effective baryon fraction matches the reference.

### 3.4 Combined dark matter tension functional

We define a combined dark matter tension functional:

```txt
Tension_DM(m) =
  w_spec   * DeltaS_spectrum(m) +
  w_chan   * DeltaS_channels(m) +
  w_baryon * DeltaS_baryon(m)
```

with weights that satisfy the fairness constraints:

```txt
w_spec   > 0
w_chan   > 0
w_baryon > 0
w_spec + w_chan + w_baryon = 1
```

The weights are part of the encoding choice and must be fixed in advance for a given analysis programme.

Properties:

* `Tension_DM(m) >= 0` for all states in the regular domain.
* `Tension_DM(m)` is small when the matter power spectrum, multi channel observables, and baryon fraction all lie close to their reference expectations inside the encoding class.
* `Tension_DM(m)` grows when spectral, channel, or baryon fraction mismatches become large.

### 3.5 Admissible encoding class and fairness constraints

We restrict attention to an admissible encoding class that fixes:

1. A finite library of dark matter model families which generate reference profiles for `ref_P_CDM` and `ref_f_baryon`. Examples include:

   * cold collisionless dark matter models with specified parameter ranges,
   * warm dark matter models with characteristic free streaming scales,
   * self interacting dark matter models inside bounded cross section ranges,
   * limited hybrid scenarios where a dark matter component coexists with modified dynamics, under explicit and pre declared rules.

2. A rule for choosing `ref_P_CDM` and `ref_f_baryon` from this library that does not depend on the specific data set that will be tested. For example:

   * choose a small set of canonical parameter points that are representative of the library,
   * define reference profiles as averages or envelopes over this finite set.

3. A fixed weight triple `(w_spec, w_chan, w_baryon)` for each analysis programme, decided before evaluating `Tension_DM(m)` on any particular data realisation.

In any concrete use, the encoding selects a finite set of canonical parameter points inside each model family and uses only the corresponding finitely many reference profiles. It does not sweep a continuous parameter space while fitting an individual data set.

Fairness constraints:

* reference profiles and weights cannot be tuned after examining the tension results for the same data set,
* model family choices inside the admissible library cannot be changed retrospectively with the sole purpose of driving `Tension_DM` toward zero for a fixed set of observations,
* the admissible class must be constrained enough that different allowed choices cannot make `Tension_DM(m)` arbitrarily small for every possible configuration, otherwise the encoding is judged too flexible.

These constraints are intended to prevent the dark matter tension functional from being reduced by retrospective or over flexible parameter tuning.

### 3.6 Effective tension tensor components

In line with the TU core, we introduce an effective tension tensor:

```txt
T_ij(m) = S_i(m) * C_j(m) * Tension_DM(m) * lambda(m) * kappa_DM
```

where:

* `S_i(m)` summarises the strength of the i th source like component, for example the sensitivity of a given region or channel to dark matter structure,
* `C_j(m)` represents the receptivity of the j th cognitive, observational, or engineering component to dark matter related inconsistencies,
* `Tension_DM(m)` is the combined scalar tension functional defined above,
* `lambda(m)` indicates the local convergence state of reasoning or modelling, inside a fixed bounded range,
* `kappa_DM` is a constant that sets the overall scale at which dark matter tension couples into broader TU dynamics.

The exact index sets for `i` and `j` are not needed at the effective layer. It is sufficient that `T_ij(m)` is well defined and finite for regular states.

### 3.7 Singular set and domain restrictions

We define a singular set:

```txt
S_sing_DM = {
  m in M_DM :
    any of rho_tot, rho_baryon, rho_DM, P_matter, obs_channel_i
    is undefined or not finite on the required domain,
    or basic consistency
      rho_tot(m; x) >= rho_baryon(m; x)
    fails on a set of non negligible measure,
    or the admissible encoding rules cannot be applied
      for example because essential meta information is missing
}
```

We restrict attention to the regular domain:

```txt
M_DM_reg = M_DM \ S_sing_DM
```

Rules:

* all definitions of `DeltaS_spectrum`, `DeltaS_channels`, `DeltaS_baryon`, `Tension_DM`, and `T_ij` are considered meaningful only on `M_DM_reg`,
* if an experiment or modelling pipeline would lead to a state in `S_sing_DM`, the outcome is recorded as out of domain rather than as evidence about the viability of any particular dark matter scenario.

---

## 4. Tension principle for this problem

This block states how Q041 is expressed as a tension principle inside TU at the effective layer.

### 4.1 Core dark matter tension principle

At the effective layer, Q041 is encoded as the following principle:

```txt
There exists a dark matter encoding in the admissible class such that
the combined tension Tension_DM(m) remains in a low, stable band across
all major observational channels and scales, when states represent the
actual universe.
```

Equivalently:

* in a low tension world, one can find regular states `m` in `M_DM_reg` that represent the real universe and satisfy

  ```txt
  Tension_DM(m) <= epsilon_DM
  ```

  for a small threshold `epsilon_DM` that does not diverge when refine(k) increases resolution or data quality,

* in a high tension world, for all regular states and admissible encodings that remain faithful to the data, one eventually finds

  ```txt
  Tension_DM(m) >= delta_DM
  ```

  with `delta_DM > 0` that cannot be removed by further refinement.

Here `refine(k)` refers to moving along a predetermined scale and data quality sequence indexed by an integer `k`, for example by increasing the range of `k_bin` in the power spectrum and adding more precise channel summaries.

This is a classification principle inside the TU effective layer. It does not assert which world class our universe actually realises. The decision about the real universe remains an empirical and theoretical question outside this file.

### 4.2 Low tension world condition

We define a low tension band `Band_low` as an interval:

```txt
Band_low = [0, epsilon_DM]
```

for some small `epsilon_DM` that can depend on:

* known systematic uncertainties,
* noise levels in observational programmes,
* limitations of the encoding library.

The low tension world condition is:

```txt
For each refine step k large enough, there exist regular states m_k in M_DM_reg
that represent the universe at resolution k and satisfy
Tension_DM(m_k) in Band_low,
with no trend toward increasing tension as k increases.
```

This is an effective way to express that the admissible dark matter sector can keep all observables mutually consistent as information quality and coverage improve.

### 4.3 Persistent high tension and failure modes

If no genuine dark matter sector inside the admissible class can explain observations, or if modified gravity or radical alternatives fail to reproduce all channels under the same encoding, we expect at least one of the following persistent high tension patterns.

1. Spectral failure

   * Even after parameter exploration inside the admissible library, `DeltaS_spectrum(m_k)` stays above a positive lower bound that cannot be justified by known uncertainties.

2. Channel conflict

   * Different channels require mutually inconsistent `rho_DM(m; x)` and `rho_baryon(m; x)` for any choice in the admissible class, so `DeltaS_channels(m_k)` remains large along the refine(k) sequence.

3. Baryon fraction inconsistency

   * Effective baryon fractions wander outside the allowed ranges from nucleosynthesis and CMB constraints, so `DeltaS_baryon(m_k)` remains significantly non zero or shows divergent behaviour with refine(k).

In these cases we have:

```txt
Tension_DM(m_k) >= delta_DM
```

for some `delta_DM > 0` that does not shrink as `k` grows. Q041 uses these patterns to classify scenarios at the effective layer. It does not attempt to decide which microphysical explanation is correct.

---

## 5. Counterfactual tension worlds

We now describe counterfactual worlds at the effective layer. These worlds are patterns in observables and tension functionals, not deep level constructions or proofs.

All such worlds are descriptions of how effective summaries and tension profiles would behave if a particular high level scenario is realised. They do not constitute microphysical theories and are not direct claims about the actual universe.

### 5.1 World T_DM: genuine dark matter sector, low tension

In World T_DM:

1. There exists a dark matter sector inside the admissible library such that for states `m_T,k` along a refine(k) sequence

   ```txt
   Tension_DM(m_T,k) stays within Band_low
   ```

   even when the resolution and data quality improve.

2. Spectral consistency

   * `DeltaS_spectrum(m_T,k)` decreases or stabilises as more scales are included, in a way that remains compatible with a cold or closely related dark matter profile and known constraints on baryons and radiation.

3. Channel consistency

   * Channel summaries from rotation curves, lensing, clusters, and CMB all fit within a single dark matter plus baryon configuration inside the encoding class, so `DeltaS_channels(m_T,k)` remains small.

4. Baryon fraction stability

   * Effective baryon fractions inferred from different probes agree with each other and with the reference band, so `DeltaS_baryon(m_T,k)` remains in a small neighbourhood of zero.

World T_DM does not specify the microscopic nature of dark matter. It only states that a coherent dark sector mechanism exists whose effective behaviour keeps tension low.

### 5.2 World F_MOD: purely modified gravity or radical alternative, high tension

In World F_MOD:

1. The true universe has no separate dark matter sector. Instead, modifications to gravity or inertia are used to account for observations.

2. When these alternatives are encoded within the same admissible framework, attempts to interpret data through such models lead to at least one of the following:

   * `DeltaS_spectrum(m_F,k)` stays high because matter clustering does not match the reference band in a way that is compatible with baryon and radiation content,
   * `DeltaS_channels(m_F,k)` remains high since a single set of modified dynamics cannot fit all channels simultaneously under the encoding constraints,
   * `DeltaS_baryon(m_F,k)` becomes large or unstable because baryon fractions required to fit some channels conflict with nucleosynthesis or CMB constraints.

In this world, for all regular states representing the universe at sufficiently large `k`:

```txt
Tension_DM(m_F,k) >= delta_DM
```

for some strictly positive `delta_DM`.

### 5.3 World MIX: hybrid dark matter plus modified dynamics

In World MIX:

1. A combination of dark matter and modified dynamics is allowed, possibly with additional fields or coupling rules, but still restricted to an explicit admissible class.

2. If the hybrid approach genuinely reduces tension without fine tuning, we expect a pattern that is intermediate between World T_DM and World F_MOD:

   * some components of `Tension_DM` decrease because the hybrid explanation has more capacity to fit multi channel data,
   * other components may increase if additional complexity introduces new inconsistencies or conflicts with global constraints.

3. Q041 treats World MIX as a test case. The encoding evaluates whether added complexity provides genuine tension reduction or mainly redistributes inconsistencies across channels and scales.

In all three worlds, the encoding compares tension profiles without taking a position on which scenario is realised in our universe.

---

## 6. Falsifiability and discriminating experiments

This block describes experiments and protocols that can falsify or support specific Q041 encodings at the effective layer. They do not prove or disprove the existence of dark matter in an absolute sense. They test whether a given encoding class and tension functional are adequate and non trivial.

### Experiment 1: Joint cosmological and astrophysical tension survey

Goal:

* evaluate whether a single dark matter encoding from the admissible library can keep `Tension_DM` inside a controlled band across major observational channels.

Setup:

* Inputs:

  * summary data for:

    * galaxy rotation curves,
    * strong and weak lensing maps,
    * cluster dynamics,
    * CMB anisotropies that constrain matter content,
    * large scale structure power spectrum estimates,

  * a finite library of dark matter model families consistent with the admissible encoding class,

  * fixed reference profiles `ref_P_CDM` and `ref_f_baryon`,

  * fixed weights `(w_spec, w_chan, w_baryon)` with each strictly positive and summing to one.

* For each data set and model, construct an effective state `m_model,data` in `M_DM_reg` that encodes the relevant summaries.

Protocol:

1. For each model in the admissible library and each data combination, compute

   * `DeltaS_spectrum(m_model,data)`,
   * `DeltaS_channels(m_model,data)`,
   * `DeltaS_baryon(m_model,data)`,

   using the definitions from Section 3.

2. Compute `Tension_DM(m_model,data)`.

3. For each data combination, record

   * the minimal `Tension_DM` achieved inside the library,
   * the distribution of tension values across models.

4. Repeat the procedure for increasing refine(k) steps. This can be done by

   * extending the scale range of the power spectrum,
   * adding more precise channel summaries,
   * including new observational programmes.

Metrics:

* minimal `Tension_DM` per refine(k) step,
* distribution of tension values across models and channels,
* stability of minimal tension as `k` increases.

Falsification conditions:

* if for all models in the admissible library and for sufficiently large `k`, the minimal `Tension_DM` exceeds a conservative upper bound `epsilon_max` in at least one major channel combination, then the current encoding class is considered falsified as a low tension description,
* if small adjustments inside the admissible library and fixed weight constraints produce arbitrarily different tension profiles without clear physical explanation, the encoding is judged too flexible and rejected.

Semantics implementation note:

* all fields and mismatch quantities in this experiment are treated in a hybrid representation that combines continuous matter fields and discrete scale bins,
* no additional semantic type is introduced, and no dependence on token level representations occurs.

Boundary note:

* falsifying a TU encoding does not solve the canonical dark matter problem,
* this experiment can rule out a specific dark matter tension encoding and its admissible class; it cannot prove or disprove the existence of dark matter itself.

---

### Experiment 2: Mock universe comparison for dark matter and alternatives

Goal:

* assess whether the Q041 encoding can systematically distinguish between simulated universes with genuine dark matter sectors and universes with only modified gravity or related alternatives.

Setup:

* construct two groups of simulations:

  * Group T:

    * simulations that include a dark matter sector drawn from the admissible library and standard gravity,

  * Group F:

    * simulations that use alternative gravity or modified inertia to mimic some dark matter effects, without a genuine dark matter sector.

* for each simulation

  * generate synthetic summaries analogous to real observations,
  * produce states `m_T_sim` and `m_F_sim` in `M_DM_reg` through a common summarisation pipeline.

Protocol:

1. For each simulation state, compute

   * `DeltaS_spectrum`,
   * `DeltaS_channels`,
   * `DeltaS_baryon`,
   * `Tension_DM`.

2. For Group T and Group F, compile the distributions of `Tension_DM`.

3. Study the separation between the tension distributions as refine(k) increases. For example, introduce more realistic small scale physics or improved synthetic observation noise models.

Metrics:

* mean and variance of `Tension_DM` in Group T and Group F,

* a simple separation statistic such as

  ```txt
  Delta_mean = abs( mean_T - mean_F )
  ```

  where `mean_T` and `mean_F` are mean tension values in each group,

* misclassification rate if a threshold on `Tension_DM` is used to distinguish T type and F type simulations.

Falsification conditions:

* if the encoding fails to achieve statistically meaningful separation of Group T and Group F across a reasonable range of simulations and refine(k) steps, then the current encoding is considered non discriminating and rejected,
* if the encoding consistently assigns lower `Tension_DM` to clearly contrived F type simulations than to coherent T type simulations, it is judged misaligned with its intended semantics and rejected.

Semantics implementation note:

* simulated universes and their summaries are treated using the same hybrid representation as in the real data case,
* the experiment does not introduce any additional encoding type beyond the one fixed in Section 0.

Boundary note:

* falsifying a TU encoding does not solve the canonical dark matter problem,
* success or failure on mock universes tests the usefulness of the encoding, not the truth of any particular cosmological scenario.

---

## 7. AI and WFGY engineering spec

This block describes how Q041 can be used as an engineering module for AI systems inside WFGY, still at the effective layer.

None of the signals or modules in this section decides whether dark matter exists. They only structure how models reason about current evidence and constraints.

### 7.1 Training signals

We define training signals derived from Q041 observables.

1. `signal_DM_consistency`

   Definition:

   ```txt
   signal_DM_consistency(m) = Tension_DM(m)
   ```

   Use:

   * a penalty that encourages internal states with low dark matter tension in contexts where a standard dark matter interpretation is assumed.

2. `signal_channel_conflict`

   Definition:

   ```txt
   signal_channel_conflict(m) = DeltaS_channels(m)
   ```

   Use:

   * penalises internal states where explanations for different observational channels imply inconsistent matter configurations.

3. `signal_baryon_budget`

   Definition:

   ```txt
   signal_baryon_budget(m) = DeltaS_baryon(m)
   ```

   Use:

   * enforces awareness that baryons cannot account for all inferred mass while still respecting nucleosynthesis and CMB constraints.

4. `signal_world_switch_stability_DM`

   Definition:

   * a signal derived by comparing model outputs when prompted under the following two types of assumptions:

     * assume a standard dark matter sector,
     * assume no dark matter and attempt to fit data through other means.

   * it measures how cleanly the model separates these regimes and how consistently it applies each assumption without mixing them in a single reasoning chain.

### 7.2 Architectural patterns

We outline architectural patterns that reuse Q041 structures at the effective layer.

1. `CosmoTensionHead_DM`

   Role:

   * a head that reads internal representations of cosmological questions and outputs an estimate of

     * `Tension_DM`,
     * optionally a small vector summary of `DeltaS_spectrum`, `DeltaS_channels`, and `DeltaS_baryon`.

   Interface:

   ```txt
   Input:
     internal embedding representing a cosmology context
   Output:
     scalar tension estimate and a small vector of mismatch scores
   ```

2. `EvidenceChannelAggregator_DM`

   Role:

   * a module that aggregates text and data descriptions of multiple observational channels into a compact descriptor for tension evaluation.

   Interface:

   ```txt
   Input:
     sequence of channel specific embeddings
   Output:
     MultiChannel_Cosmo_Descriptor style feature vector
   ```

3. `TU_CosmoObserver_DM`

   Role:

   * a general observer module that translates internal latent representations into coarse summaries compatible with `rho_tot`, `rho_baryon`, `rho_DM`, and `P_matter`.

   Interface:

   ```txt
   Input:
     internal representation of a cosmological scenario
   Output:
     structured summary suitable for feeding into CosmoTensionHead_DM
   ```

### 7.3 Evaluation harness

We suggest the following evaluation harness for AI systems augmented with Q041 modules.

1. Task selection

   * build a set of cosmology questions that involve

     * evidence for dark matter,
     * comparisons between dark matter and modified gravity scenarios,
     * interpretations of multi channel observational data.

2. Baseline condition

   * the base model answers these questions without explicit Q041 related heads or signals.

3. TU condition

   * the same model, or a close variant, is equipped with

     * CosmoTensionHead_DM,
     * EvidenceChannelAggregator_DM,
     * TU_CosmoObserver_DM,
     * training signals as defined above.

4. Metrics

   * structural quality of explanations, for example

     * clarity in separating evidence channels,
     * explicit acknowledgement of hidden sector assumptions,
     * consistent handling of baryon budgets,

   * consistency between answers across prompts that change assumptions about the presence of dark matter.

### 7.4 Sixty second reproduction protocol

This section gives a minimal protocol that allows external users to experience the effect of Q041 style encoding in an AI system.

Baseline setup:

* Prompt:

  * ask the model to explain why astronomers believe dark matter exists and how multiple types of observations support this idea, with no mention of tension or TU concepts.

* Observation:

  * record whether the explanation

    * mixes channels without clear structure,
    * ignores baryon budget constraints,
    * fails to connect spectrum level and galaxy level evidence.

TU encoded setup:

* Prompt:

  * ask the same question, but instruct the model to organise the answer around

    * a hidden matter component,
    * tension between observations and models without such a component,
    * the idea that a single dark sector must explain all channels in a consistent way.

* Observation:

  * record whether the answer

    * lists distinct observational channels,
    * refers to a coherent dark matter sector that resolves their joint tension,
    * clearly notes what would go wrong in a world with no dark matter sector.

Comparison metric:

* use a simple rubric with criteria such as

  * number of channels correctly identified,
  * explicitness of the hidden sector description,
  * clarity about constraints from baryon budgets and cosmic structure.

What to log:

* prompts, full answers, and any auxiliary tension scores emitted by CosmoTensionHead_DM, so that effective layer behaviour can be audited later without exposing deeper TU structures.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q041 and their direct reuse targets. All components in this block transfer as effective layer templates only. They do not transfer any claim about the truth of specific cosmological scenarios.

### 8.1 Reusable components produced by this problem

1. ComponentName: `DM_Consistency_Tension`

   Type:

   * functional

   Minimal interface:

   ```txt
   Inputs:
     spectrum_summary: vector of matter power spectrum amplitudes
     channel_summaries: collection of obs_channel_i style descriptors
     baryon_fraction_summary: scalar or short vector for baryon content

   Output:
     tension_value: nonnegative scalar representing Tension_DM
   ```

   Preconditions:

   * inputs must be consistent with a single cosmological scenario at the effective layer,
   * reference profiles and weights are fixed in advance.

2. ComponentName: `MultiChannel_Cosmo_Descriptor`

   Type:

   * field

   Minimal interface:

   ```txt
   Inputs:
     list of channel_summaries

   Output:
     combined_feature_vector encoding the joint state of all channels
   ```

   Preconditions:

   * each channel summary is finite dimensional and well defined,
   * channels are tagged so that the aggregator can distinguish their roles.

3. ComponentName: `DM_World_Switch_Template`

   Type:

   * experiment_pattern

   Minimal interface:

   ```txt
   Inputs:
     model_class describing a family of cosmological models
     encoding_rules describing how to construct states in M_DM

   Output:
     specification of World T_DM and World F_MOD style experiments
     including how Tension_DM is computed and compared
   ```

   Preconditions:

   * the model class supports both scenarios with and without a dark matter sector at the effective layer.

### 8.2 Direct reuse targets

1. Q042 (Nature of dark energy)

   Reused components:

   * `MultiChannel_Cosmo_Descriptor`,
   * the pattern of `DM_Consistency_Tension` for budget and channel consistency.

   Why it transfers:

   * dark energy constraints also involve multiple channels and hidden sector components; the same descriptor and tension approach works for energy partition and expansion history.

   What changes:

   * the functional focuses more on geometry and expansion observables, while retaining a similar interface.

2. Q048 (Hubble constant tension)

   Reused components:

   * `DM_Consistency_Tension`,
   * `DM_World_Switch_Template`.

   Why it transfers:

   * the Hubble constant tension compares early and late universe measurements that depend on dark matter assumptions; Q041 components provide a way to quantify consistency_tension across those probes.

   What changes:

   * inputs are tailored to distance ladder, CMB, and baryon acoustic oscillation data.

3. Q050 (Testability of multiverse scenarios)

   Reused components:

   * `DM_World_Switch_Template`.

   Why it transfers:

   * comparing universes with different dark sector properties fits naturally into a world switch pattern.

   What changes:

   * the `model_class` parameter in the template spans broader sets of cosmological models than it does for dark matter alone.

4. Q121 (AI alignment problem)

   Reused component:

   * structural idea behind `MultiChannel_Cosmo_Descriptor` and `DM_Consistency_Tension`.

   Why it transfers:

   * alignment can be framed as hidden mechanism consistency across multiple observable channels, and Q041 offers a concrete pattern for building and testing such tension functionals.

   What changes:

   * observables are behavioural or decision channels instead of astrophysical data.

---

## 9. TU roadmap and verification levels

This block records the current verification levels for Q041 and the next measurable steps at the effective layer.

### 9.1 Current levels

* E_level: E1

  * the effective layer encoding has been specified:

    * state space `M_DM`,
    * observables and summaries,
    * mismatch quantities,
    * tension functional `Tension_DM`,
    * admissible encoding constraints,
    * singular set `S_sing_DM` and regular domain `M_DM_reg`,

  * at least two experiments with explicit falsification conditions have been outlined.

* N_level: N1

  * the narrative that connects dark matter evidence, hidden sector assumptions, and tension functionals is explicit and internally coherent at the effective layer,
  * graph placement is defined in terms of upstream, downstream, parallel, and cross domain edges.

### 9.2 Next measurable step toward E2

To move Q041 from E1 to E2, at least one of the following should be implemented in a reproducible way.

1. A concrete numerical pipeline that

   * constructs `M_DM` style states from real data,
   * computes `DeltaS_spectrum`, `DeltaS_channels`, `DeltaS_baryon`, and `Tension_DM`,
   * publishes tension profiles for a small admissible library of dark matter models, together with code and documentation for external audit.

2. A suite of mock universe experiments where

   * simulations with and without dark matter sectors are generated,
   * Q041 encoding is used to classify them,
   * results and code are made reproducible and available for independent groups.

Both steps operate only on effective observables and do not expose any deep TU generative rule.

### 9.3 Long term role in the TU programme

In the long term, Q041 is expected to serve as:

* the main cosmological example of a hidden sector constrained by multi channel consistency_tension,
* a template for constructing similar encodings in other domains that involve unseen components and indirect evidence,
* a benchmark for testing whether TU style tension functionals can remain informative and non trivial for highly contested open problems.

---

## 10. Elementary but precise explanation

This block provides an explanation for non specialists while staying aligned with the effective layer description.

Astronomers see many signs that there is more matter in the universe than the stars, gas, and dust they can directly observe. Galaxies rotate too fast at their outer edges. Clusters of galaxies stay bound more tightly than visible matter alone would allow. Light bends around galaxies and clusters more than expected. The pattern of tiny temperature variations in the cosmic microwave background also points to extra matter that does not shine.

This unseen mass is called dark matter. The central difficulty is not simply to add some invisible mass into equations. The real difficulty is to find a single description of this dark matter that works for all the different kinds of observations at once and remains stable as data improve.

In the Tension Universe view, Q041 does not try to decide which specific particle or theory is right. Instead, it asks a different type of question.

* Take all the main observations that suggest dark matter.
* Build a way to measure how tense they are with each other if you assume a certain kind of dark matter or an alternative.
* Ask whether you can keep this tension small and stable as data become better and cover more scales.

To do this, Q041 introduces:

* a space of states that summarise how matter is distributed and what different experiments see,

* several numbers that measure how far those states are from a standard dark matter picture:

  * one number for how the matter clumps on different scales,
  * one number for how consistently different observations agree with one another,
  * one number for whether the amount of normal matter stays inside the allowed range,

* a combined tension score that is small when everything fits together and large when something is wrong.

Then Q041 compares different possible worlds.

* In a world where dark matter is real and well described by some model in the library, there should be a way to keep the combined tension score low across all observations, even as they improve.
* In a world with no dark matter, or only modified gravity, the combined tension score should eventually become large and difficult to reduce without special tuning.

This does not prove what dark matter is and does not assume that any particular theory is correct. It does something more modest and precise:

* it turns the vague idea that all the evidence fits into a measurable statement about tension between channels,
* it proposes experiments that can show whether a given way of encoding dark matter is too flexible or too rigid,
* it provides reusable tools that can be applied to other hidden sector problems in physics and in other domains.

Q041 is therefore the central dark matter node in the Tension Universe framework, and a model for how to handle large open questions that depend on unseen parts of the universe, without stepping outside the effective layer.

---

## Tension Universe effective layer footer

This page is part of the WFGY / Tension Universe S problem collection.

### Scope of claims

* The purpose of this document is to specify an effective layer encoding of the named problem, including observables, tension functionals, and experiments.
* It does not prove or disprove the canonical statement in Section 1 and does not claim that any underlying open problem in mathematics or physics has been solved.
* It does not introduce new theorems beyond what is already established in the cited literature.
* It should not be cited as evidence that any specific dark matter or gravity theory is correct.

### Effective layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores, and counterfactual worlds, live inside the effective layer of the TU framework.
* No explicit axiom system, deep generative rule, or construction of TU internal fields from raw data is given in this document.
* Any mapping from real world data, simulations, or proofs into the effective layer is treated as an external implementation detail and remains outside the scope of this file.

### Encoding fairness and non mutation

* The admissible encoding class and all weight constraints are specified so that they cannot be tuned after seeing the outputs on a fixed data set.
* Reference profiles, parameter libraries, and world templates must be chosen in advance for a given analysis programme and then kept fixed for that programme.
* It is not permitted to use the flexibility of the encoding class to drive tension values to zero for arbitrary inputs by retrospective parameter changes.

### Falsifiability and audit

* Each experiment described here is intended to be falsifiable at the effective layer. It can rule out a specific encoding or admissible class if its predictions about tension patterns are not borne out.
* Falsifying an encoding does not falsify the canonical scientific problem; it only shows that a particular TU style description is inadequate.
* Implementations are encouraged to publish code, data, and tension profiles so that external groups can audit effective layer behaviour independently.

### Related TU charters

For global rules that apply to all S problem entries and their encodings, see:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
