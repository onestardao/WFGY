<!-- QUESTION_ID: TU-Q046 -->
# Q046 · Cosmic microwave background anomalies

## 0. Header metadata

```txt
ID: Q046
Code: BH_COSMO_CMB_ANOMALY_L3_046
Domain: Cosmology
Family: Cosmic microwave background (CMB)
Rank: S
Projection_dominance: P
Field_type: stochastic_field
Tension_type: spectral_tension
Status: Partial
Semantics: continuous
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* We only specify state spaces, observables, mismatch scores, refinement schedules, and falsifiable experiment patterns.
* We do not specify any underlying TU axiom system, deep generating rules, or constructive derivations of TU itself.
* We do not provide any explicit mapping from raw CMB data, pipelines, or instrument models into internal TU fields. We only assume that TU compatible models exist that reproduce the listed observables.
* Falsification statements in this page always target particular combinations of baseline cosmological model and encoding instances `E` in the admissible encoding class `C_CMB` at the effective layer. They are not claims that the physical universe or the Lambda-CDM paradigm are disproved as fundamental theories.
* This node does not claim to solve or refute the canonical CMB anomalies problem. It only provides an effective layer encoding that can be tested, reused, and refined inside the TU program.

---

## 1. Canonical problem and status

### 1.1 Canonical description

The cosmic microwave background (CMB) is the relic radiation from the hot early universe, observed today as a nearly uniform blackbody field with small temperature and polarization anisotropies across the sky.

Under the standard Lambda-CDM cosmological model, the CMB temperature anisotropy field is modeled as a statistically isotropic Gaussian random field on the sphere, fully characterized at first order by its angular power spectrum `C_l` as a function of multipole index `l`.

The CMB anomalies problem asks:

* To what extent do the largest-scale CMB features observed in real data, for example from WMAP and Planck, deviate from the statistical expectations of the standard isotropic Gaussian Lambda-CDM model once a consistent analysis pipeline, foreground treatment, and look-elsewhere accounting have been fixed?

Key anomaly types include, but are not limited to:

* Low amplitude of the quadrupole `l = 2` and related low multipoles.
* Apparent alignments of low multipoles, for example quadrupole octopole alignment.
* Hemispherical power asymmetry at large angular scales.
* The presence of a cold spot with unusual size and depth, compared to Gaussian expectations.

The core question is whether these features are:

1. Atypical but acceptable realizations under Lambda-CDM plus known systematics, or
2. Evidence of new physics, nontrivial cosmic topology, large unmodeled systematics, or deeper mis specification of the cosmological model.

### 1.2 Status and difficulty

Empirically:

* The standard Lambda-CDM model with a small set of parameters fits the CMB power spectrum over a very wide range of multipoles with remarkable precision.
* Several large scale features in the real sky appear unusual when compared to naive isotropic Gaussian expectations with simple analysis choices.

Assessing the significance of these anomalies is difficult because:

* A posteriori selection effects and the look elsewhere effect can greatly inflate the apparent significance if not handled carefully.
* Foregrounds, scanning strategy, noise correlations, and masking can imprint patterns that resemble or distort anomalies.
* There is no unique, universally accepted method to define a single scalar anomaly significance without committing to particular choices of statistics and priors.

As a result:

* Some authors argue that the anomalies are likely statistical flukes or artifacts of analysis choices.
* Others argue that the combined pattern is unlikely under Lambda-CDM and may hint at new physics or nontrivial global structure.

The consensus in mainstream cosmology is that the anomalies are intriguing and worth careful study, but not yet a decisive falsification of Lambda-CDM.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q046 plays several roles.

1. It is the flagship example of a spectral_tension problem in observational cosmology, where a high precision stochastic field baseline Lambda-CDM confronts a single observed realization, our sky.

2. It serves as a bridge between problems about initial conditions, inflation, and large scale structure, by focusing on the largest observable angular scales.

3. It provides a testbed for Tension Universe encodings that must handle:

   * finite ensembles of mock skies versus a unique real sky,
   * rare event statistics and look elsewhere penalties,
   * the distinction between model mis specification and statistical fluke.

4. It feeds downstream into other cosmological tension nodes, for example Hubble constant tension and multiverse or anthropic arguments, by constraining which combinations of model and data treatments are viable.

### References

1. Planck Collaboration, “Planck 2013 results. XXIII. Isotropy and statistics of the CMB”, Astronomy and Astrophysics, 571, A23, 2014, arXiv:1303.5083.
2. Planck Collaboration, “Planck 2015 results. XVI. Isotropy and statistics of the CMB”, Astronomy and Astrophysics, 594, A16, 2016, arXiv:1506.07135.
3. C. L. Bennett et al., “Nine Year Wilkinson Microwave Anisotropy Probe WMAP Observations: Final Maps and Results”, Astrophysical Journal Supplement Series, 208, 20, 2013, arXiv:1212.5225.
4. D. J. Schwarz et al., “CMB Anomalies after Planck”, Classical and Quantum Gravity, 33, 184001, 2016, arXiv:1510.07929.

---

## 2. Position in the BlackHole graph

This block records the position of Q046 in the BlackHole graph, using Q001 to Q125 as nodes. Each edge is labeled with a one line reason that points to specific components or tension structures rather than vague similarity.

### 2.1 Upstream problems

These nodes provide prerequisites, tools, or background structures for Q046.

* Q044 `BH_COSMO_IC_L3_044`
  Reason: Supplies the initial condition frameworks and primordial curvature fields that define the baseline angular power spectrum and correlation structure used in the CMB_LowL_TensionVector.

* Q043 `BH_COSMO_INFLATION_L3_043`
  Reason: Defines the inflationary model space whose predictions for large angle modes and possible anisotropies feed into the reference profiles underlying DeltaS_spec and DeltaS_feat.

* Q041 `BH_COSMO_DARKMATTER_L3_041`
  Reason: Dark matter clustering and potential evolution contribute to integrated Sachs Wolfe effects that enter the large angle spectral components used in the tension functional.

* Q045 `BH_COSMO_LSS_L3_045`
  Reason: Connects large scale galaxy and matter distribution to potential cross correlations with CMB anomalies, constraining interpretations of anomaly features.

### 2.2 Downstream problems

These nodes reuse Q046 components or depend directly on its tension structure.

* Q048 `BH_COSMO_H0_TENSION_L3_048`
  Reason: Reuses the CMB_LowL_TensionVector and related experiment patterns to audit how proposed resolutions of Hubble constant tension interact with large angle CMB anomalies.

* Q049 `BH_COSMO_BARYON_DISTR_L3_049`
  Reason: Uses anomaly related observables as constraints on large scale baryon distribution models and their imprint on the CMB.

* Q050 `BH_COSMO_MULTIUNI_L3_050`
  Reason: Treats Q046 anomaly tension as a selection statistic when embedding our observed sky into ensembles of universes in multiverse scenarios.

### 2.3 Parallel problems

Parallel nodes share similar tension types or structural patterns without direct component dependence.

* Q045 `BH_COSMO_LSS_L3_045`
  Reason: Both Q045 and Q046 compare high precision stochastic field predictions with large scale observed patterns in cosmology. Q045 is labeled consistency_tension and Q046 spectral_tension in the metadata, but they share similar observable and field structures.

* Q048 `BH_COSMO_H0_TENSION_L3_048`
  Reason: Both are precision cosmology tension problems where the significance of the mismatch depends sensitively on priors, analysis choices, and the structure of the underlying model space.

* Q032 `BH_PHYS_QTHERMO_L3_032`
  Reason: Both use fluctuation statistics and rare events to test the consistency between microscopic or field level descriptions and macroscopic observables.

### 2.4 Cross domain edges

Cross domain edges connect Q046 to structurally related problems in other domains.

* Q059 `BH_CS_INFO_THERMODYN_L3_059`
  Reason: Reuses the idea of treating the CMB sky as a finite information snapshot, with Q046 anomaly tension functional becoming a special case of information theoretic rare fluctuation tension.

* Q123 `BH_AI_INTERP_L3_123`
  Reason: CMB anomaly detection structurally matches rare structured pattern in a high dimensional field problems in AI, so Q046 tension tools transfer to out of distribution detection and saliency analyses.

* Q036 `BH_PHYS_HIGH_TC_MECH_L3_036`
  Reason: Both deal with a widely successful baseline theory plus stubborn anomalies, and both use spectral_tension between theoretical spectra and observed features to guide model revisions.

---

## 3. Tension Universe encoding effective layer

All content in this block stays strictly at the effective layer. We specify:

* state space,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any deep generative rules or how internal TU fields are constructed from raw pixel data or instrument modeling.

### 3.1 State space

We assume a state space

```txt
M
```

interpreted as follows.

* Each state `m` in `M` encodes a coherent, finite resolution summary of:

  * large angle CMB temperature anisotropy information,
  * optionally polarization information at similar angular scales,
  * a finite set of anomaly statistics derived from the sky.

We treat:

* real sky states, denoted `m_real`, as those representing the observed CMB sky after some fixed cleaning and masking pipeline,
* mock sky states, denoted `m_mock(k_mock)`, as those representing simulated skies drawn from a specified stochastic model with a fixed parameter set and pipeline.

We do not specify how `m_real` or `m_mock(k_mock)` are built from pixel maps or time ordered data. We only require that for each such state the observables defined below are well defined and finite, except on explicitly declared singular sets.

### 3.2 Effective observables and fields

We define a finite library of observables on `M`. For Q046 we fix a finite set of low multipoles and anomaly descriptors.

Let

```txt
L_low = {2, 3, ..., L_max_low}
```

for some fixed maximum multipole `L_max_low`, for example 30. The exact choice of `L_max_low` is part of the encoding and is fixed before any tension calculation.

Whenever we need to refer to a particular refinement level in the schedule defined in Section 3.4 we write `C_l(m; k)` and `DeltaS_* (m; k)` for quantities evaluated at that level. When the refinement level is clear from context we may omit `k` from the notation.

1. Low multipole power spectrum observables

   For each `m` in `M`, each refinement level `k`, and each `l` in `L_low` we define

   ```txt
   C_l(m; k)
   ```

   as the effective estimate of the angular power at multipole `l` encoded in `m` at refinement level `k`.

   For the Lambda-CDM baseline we have a reference set

   ```txt
   C_l_ref
   ```

   obtained from a fixed parameter set and theory pipeline, chosen from the source pack and frozen before anomaly analysis.

2. Anomaly feature vector

   For each `m` we define an anomaly feature vector

   ```txt
   F_anom(m; k)
   ```

   consisting of a small number of scalar descriptors, for example:

   * `f_align(m; k)` for quadrupole octopole alignment,
   * `f_hemi(m; k)` for hemispherical power asymmetry,
   * `f_cold(m; k)` for cold spot strength and scale.

   The exact contents of `F_anom(m; k)` and any thresholds are defined once for an encoding instance and then held fixed. They do not depend on whether `m` is real or mock.

3. Low multipole spectral mismatch

   For each `m` and refinement level `k` we define

   ```txt
   DeltaS_spec(m; k) = sum over l in L_low of
                       w_l * |C_l(m; k) - C_l_ref| / max(C_l_ref, epsilon_C)
   ```

   where

   * `w_l >= 0` are fixed weights with `sum over l in L_low of w_l = 1`,
   * `epsilon_C > 0` is a fixed small constant to prevent division by zero.

   The weights `{w_l}` and `epsilon_C` are chosen based on the source pack and frozen before any evaluation on real or mock skies.

4. Anomaly feature mismatch

   We define, for each `m` and refinement level `k`,

   ```txt
   DeltaS_feat(m; k) = sum over j of
                       v_j * |f_j(m; k) - f_j_ref| / max(sigma_j_ref, epsilon_F)
   ```

   where

   * `f_j(m; k)` are components of `F_anom(m; k)`,
   * `f_j_ref` and `sigma_j_ref` are reference means and scales derived from the Lambda-CDM mock ensemble or analytic approximations,
   * `v_j >= 0` are fixed weights with `sum over j of v_j = 1`,
   * `epsilon_F > 0` is a fixed small constant.

   The quantities `f_j_ref`, `sigma_j_ref`, `v_j`, and `epsilon_F` are chosen using only the baseline model and mock skies, not by tuning to the observed anomalies.

5. Combined CMB anomaly mismatch

   We define the combined mismatch

   ```txt
   DeltaS_CMB(m; k) = w_spec * DeltaS_spec(m; k) + w_feat * DeltaS_feat(m; k)
   ```

   with fixed nonnegative weights satisfying

   ```txt
   w_spec + w_feat = 1
   0 < w_spec <= 1
   0 < w_feat <= 1
   ```

   The pair `(w_spec, w_feat)` is chosen once for Q046 under a fixed encoding instance and is not tuned after examining the real sky.

### 3.3 Tension tensor components

We adopt the TU core template for an effective tension tensor on `M`.

For each regular state `m` and refinement level `k` we define

```txt
Tension_CMB(m; k) := DeltaS_CMB(m; k)
```

and use it inside a tensorial structure

```txt
T_ij(m; k) = S_i(m; k) * C_j(m; k) * Tension_CMB(m; k) * lambda(m; k) * kappa_CMB
```

where

* `S_i(m; k)` represents source like factors, for example the relative influence of primordial physics, late time integrated effects, or systematics as encoded in the configuration.
* `C_j(m; k)` represents receptivity like factors, specifying how sensitive different reasoning or decision channels are to anomaly related mismatch.
* `Tension_CMB(m; k)` is the combined mismatch defined above.
* `lambda(m; k)` is a bounded scalar describing the local convergence state of the associated reasoning process, consistent with the TU core.
* `kappa_CMB` is a fixed scaling constant specific to the CMB anomalies node, chosen for convenience and not tuned to mute or amplify any particular data set.

The exact index sets for `i` and `j` are not needed at the effective layer. It is sufficient that for all relevant `i`, `j`, `k`, and `m` in the regular domain, `T_ij(m; k)` is well defined and finite.

### 3.4 Invariants, refinement schedule, and admissible encoding class

To compare real and mock skies in a way that respects finite resolution and ensemble size we introduce a discrete refinement index

```txt
k = 1, 2, 3, ...
```

Each `k` labels a refinement level, defined by a fixed set of choices such as:

* number of mock skies `N_mock(k)`,
* technical analysis parameters such as mask choice and smoothing scale,
* possibly tighter control over known systematics.

For each `k` we define a refinement specific invariant

```txt
I_CMB(m; k) = DeltaS_CMB(m; k) = Tension_CMB(m; k)
```

computed using only observables available at the `k`th refinement level.

We now introduce the admissible encoding class for Q046.

```txt
C_CMB
```

is the set of encoding instances for CMB anomalies that satisfy all of the following.

* The feature set `F_anom`, weight sets `{w_l}`, `{v_j}`, and the pair `(w_spec, w_feat)` are fixed once for the encoding instance and do not depend on whether the input state is real or mock.
* The reference quantities `C_l_ref`, `f_j_ref`, `sigma_j_ref`, and the small constants `epsilon_C`, `epsilon_F` are chosen using only the Lambda-CDM baseline and mock skies and are frozen before evaluating the real sky.
* The refinement schedule can increase ensemble size `N_mock(k)` and adjust technical analysis parameters in a prespecified finite family but it does not introduce new anomaly features or retune weights based on the real sky.
* For every `E` in `C_CMB` and every refinement level `k`, the quantities `DeltaS_spec(m; k)`, `DeltaS_feat(m; k)`, and `Tension_CMB(m; k)` are well defined and finite on the regular domain `M_reg`.

This admissible class is meant to prevent rare event significance from being artificially inflated by adding statistics until one appears extreme. All discussion of low tension and high tension worlds in later sections is understood to be relative to encoding instances `E` in `C_CMB`.

### 3.5 Singular set and domain restrictions

We define the singular set

```txt
S_sing = { m in M :
           any C_l(m; k) or f_j(m; k) is undefined for some k,
           or any DeltaS_spec(m; k) or DeltaS_feat(m; k) is not finite for some k }
```

and the regular domain

```txt
M_reg = M \ S_sing
```

Operationally:

* States with missing or corrupted large angle data, or with uncorrected foreground contamination beyond the specification of the encoding, are treated as elements of `S_sing`.
* All definitions of `DeltaS_spec(m; k)`, `DeltaS_feat(m; k)`, `DeltaS_CMB(m; k)`, `Tension_CMB(m; k)`, and `T_ij(m; k)` are taken to be out of domain on `S_sing`, not as evidence for or against any cosmological model.

---

## 4. Tension principle for this problem

This block states how Q046 is framed as a tension problem within TU at the effective layer.

### 4.1 Core tension functional

Given the definition in Section 3.3 we treat

```txt
Tension_CMB(m; k) = DeltaS_CMB(m; k)
```

as the core anomaly tension functional for Q046. For all `m` in `M_reg` and all `k` in the refinement schedule we have

```txt
Tension_CMB(m; k) >= 0
```

and `Tension_CMB(m; k) = 0` only if both spectral and feature mismatches vanish at that refinement level.

### 4.2 Low tension world principle

At the effective layer a low tension world for Q046, relative to an encoding instance `E` in `C_CMB` and a fixed Lambda-CDM baseline, satisfies the following principle.

> For admissible encodings of CMB observables and a fixed Lambda-CDM baseline with specified priors and analysis choices, the real sky state `m_real` yields `Tension_CMB(m_real; k)` that remains within a narrow, stable low tension band across refinement levels.

More concretely there exists a small threshold `epsilon_CMB > 0` and a finite refinement index `k_0` such that

```txt
Tension_CMB(m_real; k) <= epsilon_CMB
```

for all `k >= k_0` given the chosen encoding instance `E` in `C_CMB` and baseline model.

The value of `epsilon_CMB` and the definition of narrow band depend on the size of the mock ensemble and the adopted significance criteria but within a fixed experimental program they are treated as constants, not tuning knobs.

### 4.3 High tension world principle

A high tension world for Q046, relative to the same `C_CMB` and baseline family, satisfies the following principle.

> For any encoding instance `E` in `C_CMB` and any reasonable Lambda-CDM baseline compatible with the wider cosmological data set, the real sky state `m_real` eventually exhibits persistent anomaly tension beyond agreed bounds.

Formally there exists a `delta_CMB > 0` such that for all encoding instances `E` in `C_CMB` and for all sufficiently fine refinements `k` we have

```txt
Tension_CMB(m_real; k) >= delta_CMB
```

and `delta_CMB` cannot be driven arbitrarily close to zero by refining `k` without leaving the encoding class `C_CMB` or contradicting independent cosmological constraints.

Q046, as an effective layer problem, does not assert which principle is realized in our universe. It encodes the structure needed to define tension in a controlled way, test specific encodings and baseline assumptions, and track how evidence accumulates across refinement levels.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds for Q046, entirely at the effective layer and always relative to encoding instances `E` in `C_CMB`.

* World T: anomalies are statistically typical or acceptable given a carefully specified Lambda-CDM baseline and analysis pipeline.
* World F: anomalies remain strongly atypical under any reasonable baseline and encoding instance `E` in `C_CMB`, which suggests new physics or severe model mis specification.

### 5.1 World T Lambda-CDM typical sky, low anomaly tension

In World T and for some encoding instance `E` in `C_CMB`:

1. Low multipole spectra

   For the real sky state `m_real_T` the low multipole spectrum satisfies

   ```txt
   DeltaS_spec(m_real_T; k) is small and stable as k increases
   ```

   once the baseline `C_l_ref` and mask choices inside `E` are fixed.

2. Anomaly features

   The anomaly feature mismatch satisfies

   ```txt
   DeltaS_feat(m_real_T; k) stays within bands
   derived from mock sky ensembles
   ```

   where the bands incorporate look elsewhere corrections agreed in advance.

3. Cross experiment consistency

   When the same encoding instance `E` is applied to independent experiments, for example WMAP and Planck, the corresponding states `m_real_T_WMAP` and `m_real_T_Planck` yield similar tension values up to known noise and calibration differences.

4. Global tension behavior

   The combined tension obeys

   ```txt
   Tension_CMB(m_real_T; k) <= epsilon_CMB
   ```

   for `k >= k_0`, with `epsilon_CMB` as in Section 4.2. Variance across experiments remains compatible with baseline model expectations.

### 5.2 World F genuine anomaly physics or mis specification, high anomaly tension

In World F and for all encoding instances `E` in `C_CMB`:

1. Persistent low multipole discrepancies

   For the real sky state `m_real_F` there exists a refinement index `k_1` such that

   ```txt
   DeltaS_spec(m_real_F; k) >= delta_spec
   ```

   for all `k >= k_1`, with `delta_spec > 0` that cannot be removed without changing the baseline model or leaving `C_CMB`.

2. Robust anomaly features

   The anomaly feature mismatch satisfies

   ```txt
   DeltaS_feat(m_real_F; k) >= delta_feat
   ```

   for some `delta_feat > 0` and all sufficiently large `k`, even after conservative handling of selection effects and systematics.

3. Cross experiment persistence

   Independent experiments, when encoded by the same encoding instance `E`, yield tension values that cluster in a high tension band for the real sky while mock sky ensembles rarely occupy this band.

4. Global high tension

   The combined tension obeys

   ```txt
   Tension_CMB(m_real_F; k) >= delta_CMB
   ```

   with `delta_CMB > 0` that remains robust under refinements and analysis variations that stay inside `C_CMB`.

### 5.3 Interpretive note

These worlds are not deep generative models. They do not specify fundamental physics or simulation pipelines. They only describe how effective observables behave across refinements, how tension bands differ in low versus high tension regimes, and how consistency across experiments is interpreted.

Q046 does not assert that our universe is in World T or World F. It sets up a framework where that question can be investigated for specific encoding instances `E` in `C_CMB` in a controlled, falsifiable way.

---

## 6. Falsifiability and discriminating experiments

This block defines experiments and protocols that can test the coherence of the Q046 encoding, distinguish between different anomaly interpretations, and falsify specific choices of baseline model or encoding parameters.

These experiments do not by themselves prove or disprove Lambda-CDM. They test Q046 effective layer encodings and related assumptions.

Throughout this section we work with encoding instances `E` in `C_CMB`.

### Experiment 1: Mock sky ensemble versus real sky tension distribution

Goal:

* Evaluate whether the Q046 tension encoding places the real sky state `m_real` in a position within the mock sky tension distribution that is consistent with the declared anomaly significance level.

Setup:

* Fix a Lambda-CDM parameter set and isotropic Gaussian field model, taken from the source pack, for example `SRC_LCDM_BASE`.
* Fix a finite set of pre approved foreground masks

  ```txt
  M_masks = {mask_1, ..., mask_r}
  ```

  and a smoothing scale and map making pipeline common to real and mock skies.
* Fix an encoding instance `E` in `C_CMB` that specifies `L_low`, the feature set `F_anom`, and all weights and reference quantities.
* Select a refinement level `k` with specified `N_mock(k)` and associated technical analysis parameters that are compatible with `E`.

Protocol:

1. Generate `N_mock(k)` mock skies from the baseline model and process them through the fixed pipeline to obtain states `m_mock(1), ..., m_mock(N_mock(k))` in `M_reg`.
2. For each `m_mock(i)` compute `DeltaS_spec(m_mock(i); k)`, `DeltaS_feat(m_mock(i); k)`, and `Tension_CMB(m_mock(i); k)`.
3. Process the real sky through the same pipeline, with each mask in `M_masks`, to obtain `m_real` variants and compute `Tension_CMB(m_real; k)` for each variant.
4. Construct the empirical distribution of `Tension_CMB` over the mock ensemble and locate the quantile of `Tension_CMB(m_real; k)` within this distribution for each mask.
5. Repeat for several increasing values of `k` using the same encoding instance `E` and baseline model.

Metrics:

* The empirical cumulative distribution function of `Tension_CMB` for mock skies at each `k`.
* The quantile positions `q_real(k, mask_j)` of `Tension_CMB(m_real; k)` within each mock distribution.
* The stability of `q_real(k, mask_j)` across refinement levels and masks.

Falsification conditions:

* Before looking at the real sky fix an acceptable tail probability `p_star`, for example `p_star = 0.01`, after accounting for a fixed set of look elsewhere corrections encoded in `E`.

* If for a fixed encoding instance `E` in `C_CMB`, a fixed baseline model, and all masks in `M_masks` the quantiles satisfy

  ```txt
  q_real(k, mask_j) <= p_star
  ```

  for all sufficiently large `k`, and this behavior is robust under reasonable changes of technical analysis parameters allowed by the refinement schedule, then the combination of

  * baseline model,
  * reference statistics,
  * and encoding instance `E` in `C_CMB`

  is flagged as high tension and considered falsified as a coherent low tension world description at the TU effective layer.

* If small ad hoc changes in encoding parameters that would move the encoding outside `C_CMB`, for example reweighting `w_l`, `v_j` after seeing the data, can move `q_real(k, mask_j)` from a deep tail to a typical region without clear physical justification, the encoding instance in its original form is considered unstable and rejected.

Semantics implementation note:

* All quantities are treated as continuous field summaries, for example averaged over pixelized skies but interpreted in a continuum limit sense, consistent with the continuous `Field_type` in the metadata. No discrete only or hybrid semantics are introduced in this experiment.

Boundary note:

* Falsifying one encoding instance `E` in `C_CMB` paired with a chosen baseline model is not the same as solving the canonical CMB anomalies question. This experiment can reject specific combinations of baseline model and encoding instance at the TU effective layer but it does not by itself prove or disprove Lambda-CDM as a fundamental theory.

---

### Experiment 2: Cross experiment anomaly tension consistency

Goal:

* Test whether the Q046 encoding yields consistent anomaly tension assessments across independent CMB experiments when applied with the same encoding instance `E` in `C_CMB` and baseline assumptions.

Setup:

* Choose two or more CMB data sets, for example WMAP and Planck, that observe the same sky with different instruments.
* Fix a single Lambda-CDM baseline parameter set and theory pipeline.
* Fix a single encoding instance `E` in `C_CMB` that is compatible with all experiments.
* Use the same finite set of masks `M_masks` as in Experiment 1.

Protocol:

1. Process each experiment data set through its standard cleaning and calibration pipeline, then map to a common representation compatible with `E`, producing states `m_real_WMAP`, `m_real_Planck`, and so on in `M_reg`.
2. For each state and each refinement level `k`, compute `Tension_CMB(m_real_exp; k)` using the same encoding instance `E` and masks in `M_masks`.
3. Optionally generate mock ensembles specific to each experiment, with noise and beam properties included, and compute mock tension distributions for each.
4. Compare

   * the values and decomposition of `Tension_CMB` across experiments for the real sky,
   * the relative positions of these values within the corresponding mock distributions.

Metrics:

* Differences

  ```txt
  |Tension_CMB(m_real_WMAP; k) - Tension_CMB(m_real_Planck; k)|
  ```

  as functions of `k`.
* For each experiment the quantile positions of real sky tension within its own mock tension distribution.
* Coherence between experiments in terms of whether they classify the real sky as low tension, moderate tension, or high tension for the same encoding instance `E`.

Falsification conditions:

* If for a fixed baseline model and encoding instance `E` in `C_CMB` one experiment consistently assigns the real sky to a low tension band while another assigns it to a high tension band, and this discrepancy cannot be explained by known differences in noise, resolution, or sky coverage, then the encoding instance `E` is considered incoherent as a cross experiment anomaly encoding and rejected or revised.
* If plausible tweaks to experiment specific systematics can flip the tension classification without materially changing the underlying sky features, the Q046 encoding instance is flagged as too sensitive to instrument level details and must be revised or replaced by another instance in `C_CMB`.

Semantics implementation note:

* All experiment states are encoded using the same continuous field representation and observables. Differences in beams, noise, and masks are handled in the preprocessing stage and are not treated as changes in the underlying `Field_type`.

Boundary note:

* Falsifying or revising an encoding instance `E` in `C_CMB` based on cross experiment inconsistency tests the internal coherence of that encoding. Agreement or disagreement across experiments under `E` tests encoding and model assumptions but does not by itself settle the global CMB anomalies question.

---

## 7. AI and WFGY engineering spec

This block describes how Q046 can be used as an engineering module for AI systems in the WFGY framework at the effective layer.

### 7.1 Training signals

We define several training signals that leverage Q046 observables and tension functionals.

1. `signal_cmb_lowL_consistency`

   * Definition: a scalar signal proportional to `DeltaS_spec(m; k)` when the model is asked to reason about large angle CMB spectra under a specified Lambda-CDM baseline.
   * Purpose: encourage internal representations and outputs that remain consistent with the declared baseline when the context assumes it.

2. `signal_cmb_anomaly_feature_clarity`

   * Definition: a decomposed signal based on the components of `DeltaS_feat(m; k)`, highlighting contributions from alignment, hemispherical asymmetry, and cold spot statistics.
   * Purpose: train the model to separate different anomaly channels rather than conflating them into a single vague notion of strange sky.

3. `signal_cross_world_separation`

   * Definition: a signal that measures how distinctly the model maintains separate reasoning tracks when prompted under low tension World T versus high tension World F assumptions, as reflected in predicted `Tension_CMB`.
   * Purpose: discourage mixing or averaging mutually incompatible world assumptions.

4. `signal_dataset_consistency`

   * Definition: a signal reflecting differences in Q046 derived tension across descriptions of different experiments, penalizing unjustified large discrepancies.
   * Purpose: align the model explanations with the cross experiment consistency constraints of Experiment 2.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q046 structures.

1. `CMBAnomalyTensionHead`

   * Role: given an internal representation of a CMB related context, for example a summary of data, model, and claims, outputs

     * a scalar estimate of `Tension_CMB(m; k)`,
     * a short vector decomposition into spectral and feature components.

   * Interface:

     * Inputs: condensed embeddings of the current context plus explicit tags specifying baseline model, experiment, and refinement level.
     * Outputs: `(tension_scalar, tension_components_vector)`.

2. `IsotropyConsistencyFilter`

   * Role: a filter that checks whether proposed explanations maintain or break statistical isotropy in ways compatible with Q046 admissible encoding class `C_CMB`.
   * Interface:

     * Inputs: candidate explanations or scenario summaries.
     * Outputs: a score or mask indicating consistency with isotropic Gaussian expectations, given the encoded anomalies.

3. `MockVsRealSkyComparator`

   * Role: a module that compares internal representations of mock skies and the real sky in tension space rather than raw data space.
   * Interface:

     * Inputs: two state like embeddings, mock and real, plus encoding parameters.
     * Outputs: relative tension position and a classification such as typical, borderline, or anomalous.

### 7.3 Evaluation harness

We propose an evaluation harness for AI systems that incorporate Q046 modules.

1. Task family

   * Explain and assess CMB anomalies under different stated assumptions.

     * Pure Lambda-CDM with no new physics.
     * Lambda-CDM plus flexible foreground and systematic models.
     * Extended models, for example nontrivial topology or anisotropic inflation.

2. Conditions

   * Baseline condition:

     * The model has no explicit Q046 modules or tension signals.

   * TU condition:

     * The model uses `CMBAnomalyTensionHead` and `IsotropyConsistencyFilter` to structure reasoning and generate auxiliary tension outputs.

3. Metrics

   * Consistency of answers across logically related prompts, for example whether the model keeps its characterization of anomalies stable when assumptions are stated explicitly versus implicitly.

   * Correct separation of

     * what is data, observed sky,
     * what is baseline model,
     * what is systematic uncertainty,
     * what is new physics speculation.

   * Alignment between the model qualitative narrative and quantitative Q046 tension assessments.

### 7.4 Sixty second reproduction protocol

A minimal protocol for external users to experience Q046 effect in an AI system.

Baseline setup:

* Prompt the model:

  * Explain the large scale anomalies in the cosmic microwave background and whether they seriously challenge the standard cosmological model.

* Record the answer from the baseline system with no explicit Q046 modules.

* Observe whether anomalies are clearly enumerated, connected to statistical significance, and distinguished from pure speculation.

TU encoded setup:

* Prompt the model:

  * Using an explicit notion of anomaly tension based on low multipoles and feature statistics, explain the large scale anomalies in the cosmic microwave background and whether they challenge the standard model. Separate what is data, what is model, and what is unresolved.

* Record the answer from the TU augmented system and any reported Q046 tension summaries.

Comparison metric:

* Rate both answers on:

  * clarity of anomaly list,
  * explicitness about baselines and priors,
  * treatment of statistical flukes versus genuine model stress.

* Optionally have independent evaluators judge which answer better represents the current scientific state.

What to log:

* Prompts, responses, and any Q046 tension outputs.
* Simple structured metadata, for example which anomalies were mentioned and how significance was described.

This record allows later inspection of whether the system used Q046 in a way compatible with the effective layer encoding.

---

## 8. Cross problem transfer template

This block lists reusable components from Q046 and identifies direct reuse targets.

### 8.1 Reusable components produced by this problem

1. ComponentName: `CMB_LowL_TensionVector`

   * Type: observable bundle or functional.

   * Minimal interface:

     * Inputs: low multipole power estimates `C_l(m; k)` for `l` in `L_low`, anomaly feature vector `F_anom(m; k)`, and a reference set from the source pack.
     * Output: a finite dimensional vector of normalized mismatch scores, together with a scalar `Tension_CMB(m; k)`.

   * Preconditions:

     * Inputs must come from states in `M_reg` with clearly specified baseline model, encoding instance `E` in `C_CMB`, and refinement level.

2. ComponentName: `CMB_AnomalyExperiment_Template`

   * Type: experiment pattern.

   * Minimal interface:

     * Inputs: baseline cosmological model specification, ensemble of mock sky states, real sky state, encoding instance `E` in `C_CMB`, and refinement schedule.
     * Output: a standardized plan for computing mock and real tension distributions and for applying falsification conditions.

   * Preconditions:

     * All inputs must use the same encoding instance `E` and refinement definitions.

3. ComponentName: `CMB_AnomalyWorlds_Spec`

   * Type: field or scenario descriptor.

   * Minimal interface:

     * Inputs: encoding parameters specified by `E` in `C_CMB` and mock ensemble statistics.
     * Output: effective definitions of low tension and high tension worlds in terms of `Tension_CMB(m; k)` bands and refinement behavior.

   * Preconditions:

     * Baseline and encoding choices must be fixed before classifying the real sky.

### 8.2 Direct reuse targets

1. Q048 Hubble constant tension

   * Reused components: `CMB_LowL_TensionVector`, `CMB_AnomalyExperiment_Template`.

   * Why it transfers:

     * Proposed changes to the early universe model that relieve Hubble constant tension often modify the CMB power spectrum and large scale structure, so the same tension vector can be used to check whether these changes exacerbate or reduce anomalies.

   * What changes:

     * Additional observables, for example acoustic peak structure, are added to the observable bundle but the low multipole anomaly part and its tension mapping remain the same.

2. Q050 Multiverse and anthropic selection

   * Reused components: `CMB_AnomalyExperiment_Template`, `CMB_AnomalyWorlds_Spec`.

   * Why it transfers:

     * Multiverse scenarios often treat our observed sky as one realization from a large ensemble, and the anomaly tension acts as a selection criterion or weighting factor.

   * What changes:

     * The baseline mock ensemble now corresponds to draws from a multiverse prior rather than a single Lambda-CDM model, but the tension computation and world classification remain structurally identical.

3. Q043 Inflation origin

   * Reused components: `CMB_LowL_TensionVector`.

   * Why it transfers:

     * Specific inflation models predict characteristic modifications to low multipole power and anomaly statistics, so the tension vector provides a compact way to compare model classes.

   * What changes:

     * Reference profiles and feature expectations are updated for each inflationary model class while the form of the tension vector stays fixed.

---

## 9. TU roadmap and verification levels

This block explains the current verification levels for Q046 and the next measurable steps.

### 9.1 Current levels

* E_level: E1

  * The effective encoding of CMB anomalies as a spectral_tension problem is specified in terms of

    * state space `M`,
    * observables `C_l(m; k)` and `F_anom(m; k)`,
    * mismatch measures `DeltaS_spec`, `DeltaS_feat`, and `Tension_CMB`,
    * a discrete refinement schedule and an admissible encoding class `C_CMB`.

  * Concrete experiment patterns and falsification conditions are defined in principle but not yet pinned down to a specific fully implemented pipeline.

* N_level: N1

  * The narrative linking

    * Lambda-CDM baseline,
    * large angle anomalies,
    * tension functionals,
    * counterfactual worlds

    is explicit and self consistent at the effective layer.

  * Clear roles are assigned to upstream and downstream problems but the full cross episode storyline across cosmology is not yet constructed.

### 9.2 Next measurable step toward E2

To move Q046 from E1 to E2 the following concrete achievements are required.

1. Implemented pipeline

   * A publicly documented code and data pipeline that

     * takes in CMB maps and baseline model parameters,
     * computes `C_l(m; k)`, `F_anom(m; k)`, and `Tension_CMB(m; k)` for specified `k`,
     * processes both real and mock skies using the same encoding instance `E` in `C_CMB`.

   * The pipeline must be tied to a finite, versioned source pack for observables and baseline parameters.

2. Published tension summary

   * A released data set of

     * mock tension distributions,
     * real sky tension values,
     * quantile positions,
     * and their dependence on a small set of clearly declared analysis choices.

   * This summary must be sufficient for independent groups to replicate or challenge the encoding instance `E`.

Once these steps are completed the Q046 node can be labeled E2 while still respecting the effective layer boundaries.

### 9.3 Long term role in the TU program

Longer term Q046 is expected to serve as:

* The canonical example of how TU handles problems where there is a single observed field realization, a well defined stochastic baseline, and subtle issues of rare event statistics and model selection.
* A gateway node connecting cosmological tensions, for example Hubble constant tension and sigma_8 tension, with other spectral_tension problems in physics and information theory.
* A template for AI systems that must reason about high precision data versus model mismatches without collapsing into overconfident claims or vague hand waving.

---

## 10. Elementary but precise explanation

This block explains Q046 for non specialists while staying aligned with the effective layer structure.

The cosmic microwave background is the afterglow of the early universe, spread across the whole sky. It is almost perfectly uniform but not exactly. There are tiny temperature variations that form a kind of speckle pattern on the sky.

The standard cosmological model, called Lambda-CDM, predicts that this speckle pattern should look like a random pattern with very specific statistical properties.

* On average it should have the same strength of fluctuations in every direction, isotropy.
* The pattern should be well described by a simple list of numbers, one for each angular scale, called the power spectrum.

When we look at the data from satellites like WMAP and Planck we find that:

* Over most angular scales the pattern matches Lambda-CDM very well.
* On the very largest scales there are some odd features.

  * Certain large scale waves are weaker than expected.
  * Some patterns look unusually aligned.
  * One region seems unusually cold.

The CMB anomalies problem asks whether these oddities are just a rare but acceptable roll of the cosmic dice or a sign that the model is missing something important.

In the Tension Universe view we do not jump directly to declaring victory or failure. Instead we:

1. Summarize the CMB data into a small set of numbers that capture:

   * low scale power,
   * alignments,
   * asymmetries,
   * special spots.

2. Compare these numbers to what Lambda-CDM says is typical using many simulated skies.

3. Combine the differences into a single tension score `Tension_CMB(m; k)`.

If the real sky tension score looks similar to most simulated skies we say the anomalies are low tension under that model and encoding instance. If the real sky score sits far out in the tail and stays there even when we refine the analysis in reasonable ways that stay inside `C_CMB` we say the anomalies create high tension for that combination of model and assumptions.

Q046 does not decide which is the final truth. It builds a careful framework to define what we mean by anomaly and tension, test specific choices of model and analysis, and reuse the same ideas in other cosmology and AI problems where rare patterns might or might not signal something deep.

In this way Q046 becomes a precise reusable module in the broader Tension Universe program rather than a loose collection of surprising plots.

---

## Tension Universe effective layer footer

This page is part of the WFGY and Tension Universe S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the CMB anomalies problem.
* It does not claim to prove or disprove the canonical scientific statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores, and counterfactual worlds, live at the TU effective layer.
* All falsifiability statements apply to combinations of baseline models and encoding instances `E` in `C_CMB`.
* None of the constructions in this page fix or assume any particular choice of TU axioms or deep generating rules.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
