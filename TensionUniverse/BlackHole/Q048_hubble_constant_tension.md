# Q048 · Hubble constant tension

## 0. Header metadata

```txt
ID: Q048
Code: BH_COSMO_H0_TENSION_L3_048
Domain: Cosmology
Family: Cosmic expansion and background
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: continuous
E_level: E1
N_level: N2
Last_updated: 2026-01-24
````

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The Hubble constant tension is the apparent inconsistency between different high precision
measurements of the present day expansion rate of the universe, usually denoted as H0.

In the current standard cosmological model, a single parameter H0 should describe the late time
expansion rate, and inferences of H0 based on different observables and epochs should be
mutually consistent once all known systematics are controlled and a shared model class is used.

However, in practice:

* Early universe probes such as the cosmic microwave background (CMB), interpreted within a
  standard flat LCDM model, yield one preferred range of H0.
* Late universe probes such as distance ladder measurements using Cepheids and type Ia supernovae
  yield a higher preferred range of H0.
* Other probes, such as strong lensing time delays or standard sirens, add additional, sometimes
  intermediate, constraints.

The canonical problem can be phrased as:

> Given all current high precision cosmological data sets and an agreed baseline model class,
> do all admissible encodings of these data into an effective expansion parameter H0 converge
> to a mutually consistent value, or is there a persistent, statistically significant tension
> that cannot be removed without introducing qualitatively new ingredients?

This does not assume that any particular data set is correct or that the standard model is final.
It only records that there is a nontrivial, unresolved consistency problem.

### 1.2 Status and difficulty

At the time of writing:

* CMB based analyses (for example Planck 2018) under flat LCDM typically infer H0 in the high
  60s (in units km s^-1 Mpc^-1), with small quoted uncertainties.
* Local distance ladder analyses (for example SH0ES type programs) typically infer H0 in the
  low to mid 70s, also with small quoted uncertainties.
* Alternative calibrations (for example those using the tip of the red giant branch) and other
  probes sometimes yield values closer to the CMB value, but with different systematics.

When these results are compared under shared model assumptions, the disagreement is often quoted
at the few sigma level. The precise significance depends on:

* which data sets are included,
* how systematics are treated,
* what exact model extensions are allowed.

No consensus has been reached on whether:

* the tension is mainly due to unaccounted systematics or hidden correlations,
* modest extensions to the standard cosmological model can resolve it,
* more radical new physics is required,
* or some combination of the above.

There is also no agreed single scalar summary of "the" H0 tension. Different groups define
different tension measures, which is part of why the problem is subtle.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q048 plays the following roles:

1. It is a central example of **consistency_tension** in a high precision physical science:
   several sophisticated inference pipelines, all aimed at the same parameter, fail to agree
   within their stated uncertainties.

2. It links several cosmology nodes:

   * dark matter and dark energy content,
   * large scale structure,
   * early universe initial conditions,
   * modelling of astrophysical distance indicators.

3. It provides a test bed for Tension Universe encodings of:

   * cross probe consistency functionals,
   * multi experiment state spaces and invariants,
   * families of refined encodings indexed by an explicit resolution parameter.

### References

1. Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters",
   Astronomy and Astrophysics, 2018.

2. A. G. Riess et al., "Large Magellanic Cloud Cepheid standards provide a 1 percent foundation
   for the determination of the Hubble constant", Astrophysical Journal, 2019.

3. W. L. Freedman et al., "The Carnegie-Chicago Hubble Program. An independent determination of
   the Hubble constant", Astrophysical Journal, 2019 (and later updates).

4. E. Di Valentino, A. Melchiorri, J. Silk, "Planck evidence for a closed Universe and a possible
   crisis for cosmology", Nature Astronomy, 2020, and subsequent "H0 tension" review papers.

5. Standard encyclopedia style entries on "Hubble constant" and "Hubble tension" in major
   reference works.

---

## 2. Position in the BlackHole graph

This block records how Q048 sits inside the BlackHole graph as nodes and edges among Q001–Q125.
Each edge is listed with a one line reason that points to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools or foundations that Q048 relies on.

* Q041 (BH_COSMO_DARKMATTER_L3_041)
  Reason: Supplies dark matter content and clustering assumptions that enter both early and
  late universe H0 inferences.

* Q042 (BH_COSMO_DARKENERGY_L3_042)
  Reason: Provides the late time acceleration model needed to relate distance indicators and
  redshift to an effective H0.

* Q043 (BH_COSMO_INFLATION_L3_043)
  Reason: Sets initial conditions affecting the CMB anisotropies used in early universe H0
  determinations.

* Q044 (BH_COSMO_IC_L3_044)
  Reason: Encodes assumptions about initial smoothness and low entropy that support the
  background cosmological model used here.

### 2.2 Downstream problems

These problems reuse Q048 components or depend on its tension structure.

* Q045 (BH_COSMO_LSS_L3_045)
  Reason: Reuses the multi probe cross consistency functional defined here to test large scale
  structure probes against CMB and local H0.

* Q050 (BH_COSMO_MULTIUNI_L3_050)
  Reason: Uses the H0_TensionFunctional as a prototype for multi world comparisons of
  cosmological parameter consistency.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Adopts the information view of cross experiment tension first formalised in Q048.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q040 (BH_PHYS_QBLACKHOLE_INFO_L3_040)
  Reason: Both require consistency_tension between different encodings of the same physical
  quantity (information content vs H0).

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: Both study cross probe tensions between historical and current measurements of a
  global state of a system.

### 2.4 Cross domain edges

Cross domain edges connect Q048 to problems in other domains that can reuse its components.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Can reuse the multi reservoir consistency idea, interpreting different thermodynamic
  probes of the same quantity as analogues of early and late universe H0 probes.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Uses Q048 as an example of a high stakes inference mismatch that an aligned AI should
  detect, quantify and communicate instead of averaging away.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden generative rules or construction of internal TU fields from
raw observational data.

### 3.1 State space

We assume the existence of a state space

`M`

of "cosmology inference states for H0". Each element `m` in `M` represents a coherent effective
encoding of:

* summaries of early universe probes relevant for H0,
* summaries of late universe probes relevant for H0,
* the model class and nuisance parameter treatment used in those inferences.

We assume a family of resolution levels indexed by integers `k >= 0`. For each world model,
there is a sequence of states

```txt
m(k) in M,  k = 0, 1, 2, ...
```

where higher `k` correspond to refinements:

* more precise data,
* more detailed modelling of systematics,
* more complete inclusion of probes.

We do not specify how any `m(k)` is constructed from raw data. We only assume that:

* for any fixed modelling protocol and set of probes, there exists at least one `m(k)` encoding
  the resulting effective summaries;
* the refinement order `k` is monotone in the practical sense: larger `k` reflect strictly
  richer or more precise encodings.

We also assume an admissible encoding class `E_adm` which is a set of rules mapping given probe
combinations and model classes to states in `M`. This class is fixed in advance at the level of
the encoding design and is not allowed to depend on the specific numerical outcomes of the
probes for the world under study.

### 3.2 Effective fields and observables

We introduce the following observables on `M`.

1. Early universe H0 summary

```txt
H0_early(m) in R
```

* A real valued scalar summarising the inferred H0 from early universe probes (for example CMB,
  BAO) in state `m`.

2. Late universe H0 summary

```txt
H0_late(m) in R
```

* A real valued scalar summarising the inferred H0 from late universe probes (for example
  distance ladder, strong lensing, standard sirens) in state `m`.

3. Early and late uncertainty scales

```txt
Sigma_early(m) > 0
Sigma_late(m) > 0
```

* Positive real numbers capturing effective one sigma scales for the early and late H0
  determinations encoded in `m`. They combine statistical and systematic components at the
  effective layer.

4. Baseline mismatch observables

We fix in advance a baseline cosmological model and pipeline class `B_base`, independent of any
particular world, and define:

```txt
DeltaS_early(m) >= 0
DeltaS_late(m)  >= 0
```

* `DeltaS_early(m)` measures how strongly the early universe summaries in `m` deviate from what
  `B_base` would predict when fit to those data.
* `DeltaS_late(m)` measures the analogous deviation for late universe summaries.

These observables are required to satisfy:

```txt
DeltaS_early(m) = 0  only if  early summaries match B_base within design tolerance
DeltaS_late(m)  = 0  only if  late summaries match B_base within design tolerance
```

The definition of "design tolerance" is part of the encoding design and must be fixed before
looking at the actual data of the world being analysed.

5. Cross probe H0 mismatch observable

We define a cross probe mismatch:

```txt
DeltaS_cross(m) = G(H0_early(m), H0_late(m), Sigma_early(m), Sigma_late(m))
```

where `G` is a fixed nonnegative function chosen at encoding design time with the following
properties:

* It depends on the H0 summaries only through dimensionless combinations such as:

  ```txt
  d_H0(m) = |H0_early(m) - H0_late(m)| /
            sqrt( Sigma_early(m)^2 + Sigma_late(m)^2 )
  ```

* It is monotone nondecreasing in `d_H0(m)`.

* It satisfies `DeltaS_cross(m) = 0` if and only if `H0_early(m)` and `H0_late(m)` are equal
  within a small multiple of the combined uncertainty.

The function `G` is fixed for the entire admissible encoding class `E_adm` and is not allowed to
be changed after seeing the numerical values for a specific world.

### 3.3 Effective tension tensor components

We define an aggregate mismatch:

```txt
DeltaS_total(m) = w_early * DeltaS_early(m)
                  + w_late * DeltaS_late(m)
                  + w_cross * DeltaS_cross(m)
```

where the weights satisfy:

```txt
w_early  > 0
w_late   > 0
w_cross  > 0
w_early + w_late + w_cross = 1
```

These weights are fixed at the level of encoding design, are common across all states, and are
not tuned per state or per world. This fairness constraint prevents trivial "tension removal"
by state dependent reweighting.

The effective tension tensor is then defined as:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_total(m) * lambda(m) * kappa
```

where:

* `S_i(m)` is a source like factor for the ith component, reflecting how strongly that component
  participates in cosmology inference in state `m`.
* `C_j(m)` is a receptivity like factor for the jth component, reflecting how sensitive it is to
  H0 related mismatch.
* `lambda(m)` is a convergence state factor taking values in a fixed bounded interval, encoding
  whether local reasoning is convergent, recursive, divergent or chaotic.
* `kappa` is a global coupling constant for the H0 consistency_tension encoding.

The indexing sets for `i` and `j` are not specified at this level; it is sufficient that for
each `m` in `M_reg` the tensor is finite.

### 3.4 Invariants and effective constraints

We introduce two scalar invariants that will be used in Block 4 and Block 5.

1. Cross probe H0 invariant

```txt
I_H0(m) = d_H0(m)
        = |H0_early(m) - H0_late(m)| /
          sqrt( Sigma_early(m)^2 + Sigma_late(m)^2 )
```

This invariant measures how many combined standard deviations separate the early and late H0
inferences encoded in `m`. It is dimensionless and nonnegative.

2. Multi scale consistency invariant

We consider the refinement sequence `m(k)` for a given world and define:

```txt
I_scale(m(k)) = DeltaS_total(m(k))
```

The qualitative behaviour of `I_scale(m(k))` as `k` increases encodes whether refinements of
data and modelling:

* drive the total mismatch towards a low band,
* leave it roughly constant,
* or keep it bounded away from zero.

### 3.5 Singular set and domain restrictions

Some observables may become undefined or unbounded, for example if:

* uncertainty scales vanish or become ill conditioned,
* the effective H0 summaries are not finite,
* the baseline mismatch evaluation fails.

We define the singular set:

```txt
S_sing = {
  m in M :
  Sigma_early(m) <= 0  or
  Sigma_late(m)  <= 0  or
  H0_early(m)    not in R  or
  H0_late(m)     not in R  or
  DeltaS_early(m) undefined or infinite  or
  DeltaS_late(m)  undefined or infinite  or
  DeltaS_cross(m) undefined or infinite
}
```

We restrict all H0 tension analysis to the regular set:

```txt
M_reg = M \ S_sing
```

If an experiment or protocol would require evaluating `DeltaS_total(m)` for `m` in `S_sing`,
the result is treated as "out of domain" and not as evidence about the underlying physics.

---

## 4. Tension principle for this problem

This block states how Q048 is characterised as a tension problem within TU at the effective
layer.

### 4.1 Core H0 tension functional

We define the H0 tension functional as:

```txt
Tension_H0(m) = DeltaS_total(m)
```

for all `m` in `M_reg`. This choice satisfies:

* `Tension_H0(m) >= 0`,
* `Tension_H0(m) = 0` only when early, late and cross probe mismatches all vanish,
* `Tension_H0(m)` increases whenever any of the component mismatches grows while others are
  fixed.

Alternative monotone combinations of the component mismatches are allowed within the same
encoding class, but must be fixed before examining world specific data, and must preserve these
properties.

### 4.2 H0 tension as a low tension principle

At the effective layer, the statement that the universe is well described by a single coherent
expansion history compatible with standard modelling can be phrased as:

> There exists at least one admissible encoding sequence `m(k)` in `E_adm` for the actual world
> such that `Tension_H0(m(k))` stays within a low band that does not grow with refinement.

More concretely, there exists a small threshold `epsilon_H0 > 0` and a refinement level
`k0 >= 0` such that for all `k >= k0`:

```txt
Tension_H0(m(k)) <= epsilon_H0
```

for at least one `m(k)` sequence in `E_adm` that faithfully encodes the world. The pair
`(epsilon_H0, k0)` is part of the encoding design and is chosen based on expected achievable
precision, not on the particular numerical value of H0 in the world being studied.

### 4.3 Persistent H0 tension as high tension principle

Conversely, if in all admissible encoding sequences `m(k)` that remain faithful to the actual
world the H0 tension functional stays above a strictly positive threshold independent of
refinement, we are in a high tension regime.

Formally, there exists:

* a positive threshold `delta_H0 > 0`,
* and a minimum refinement level `k0 >= 0`,

such that for all `k >= k0` and all encoding sequences `m(k)` in `E_adm` that accurately encode
the world:

```txt
Tension_H0(m(k)) >= delta_H0
```

In this regime it is not possible to attribute the H0 tension to purely transient modelling
issues that vanish with refinement inside the given model class. Any resolution would require
at least one of:

* moving to a different baseline model class outside `B_base`,
* revising the set of probes considered trustworthy at high precision,
* discovering previously unknown correlations or systematics that fundamentally change the
  effective summaries.

Q048, as a BlackHole node, does not attempt to decide which regime is realised in our universe.
It only sets up a precise distinction between low tension and high tension regimes for an
explicitly constrained family of encodings.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds described strictly at the effective layer:

* World T: H0 tension resolves within modest extensions and refined systematics.
* World F: H0 tension persists and indicates deeper inconsistency.

These worlds are given in terms of observable patterns, not hidden generative rules.

### 5.1 World T (tension resolves under refinement)

In World T:

1. Early and late H0 convergence

   * As `k` increases, there exist encoding sequences `m_T(k)` such that:

     ```txt
     I_H0(m_T(k))  tends to a value of order 1 or less
     ```

     compatible with a shared H0, given the reported uncertainties.

2. Baseline mismatch control

   * `DeltaS_early(m_T(k))` and `DeltaS_late(m_T(k))` remain bounded and can be made small by
     reasonable modifications within the chosen model class (for example improved nuisance
     parameter treatment, calibration updates).

3. Total tension band

   * There exists `epsilon_H0` such that for sufficiently large `k`:

     ```txt
     Tension_H0(m_T(k)) <= epsilon_H0
     ```

     for the world, with `epsilon_H0` comparable to design expectations.

4. Interpretation

   * The remaining differences between different H0 analyses are attributed to finite data,
     manageable systematics, and modest model extensions, not to a deep inconsistency.

### 5.2 World F (tension persists and indicates deeper inconsistency)

In World F:

1. Persistent cross probe mismatch

   * For any admissible encoding sequence `m_F(k)` for the world, there exists `delta_H0 > 0`
     and `k0` such that for all `k >= k0`:

     ```txt
     I_H0(m_F(k)) >= delta_H0
     ```

     with `delta_H0` significantly larger than unity.

2. Baseline mismatch asymmetry

   * Attempts to adjust modelling within `B_base` cannot simultaneously keep both
     `DeltaS_early(m_F(k))` and `DeltaS_late(m_F(k))` small. Reducing one inevitably increases
     the other beyond acceptable design ranges.

3. Total tension floor

   * For all `k >= k0`:

     ```txt
     Tension_H0(m_F(k)) >= delta_H0'
     ```

     for some strictly positive `delta_H0'` that cannot be removed by refinements inside the
     admissible encoding class.

4. Interpretation

   * The tension is interpreted as a sign that at least one of the following is true:

     * some widely used data sets are fundamentally mis calibrated,
     * the baseline model class is qualitatively inadequate,
     * or the joint use of these probes is logically inconsistent in the assumed framework.

### 5.3 Interpretive note

These counterfactual worlds do not construct or modify raw cosmological data. They only assert
that if certain patterns of effective observables hold under admissible encodings, then the
world is in either a low tension or high tension regime as defined by the functional
`Tension_H0`. No claim is made here about which regime is actually realised.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q048 encoding,
* distinguish between different H0 tension models,
* provide evidence for or against particular parameter choices in `E_adm`.

These experiments do not resolve the H0 tension by themselves. They can only falsify or support
specific TU encodings related to Q048.

### Experiment 1: Multi probe tension mapping

*Goal:*

Test whether the `Tension_H0` functional produces stable and interpretable tension estimates
when applied to real combinations of early and late universe probes.

*Setup:*

* Input data: published likelihoods or summary statistics for:

  * early probes such as CMB and BAO,
  * late probes such as distance ladder, strong lensing time delays, standard sirens.
* Fix in advance:

  * the baseline model class `B_base`,
  * the admissible encoding class `E_adm`,
  * the weight triple `(w_early, w_late, w_cross)` and the function `G`.

*Protocol:*

1. For each chosen combination of probes (for example CMB only, CMB+BAO, late only, all probes),
   construct an effective state `m_data` in `M_reg` via an encoding in `E_adm`.
2. For each `m_data`, evaluate:

   * `H0_early(m_data)` and `H0_late(m_data)` where defined,
   * `Sigma_early(m_data)` and `Sigma_late(m_data)`,
   * `DeltaS_early(m_data)`, `DeltaS_late(m_data)` and `DeltaS_cross(m_data)`,
   * `Tension_H0(m_data)`.
3. Build a table or map of `Tension_H0(m_data)` values indexed by probe combinations.
4. Repeat the above for several reasonable modelling choices within `B_base` to check
   robustness.

*Metrics:*

* Distribution of `Tension_H0(m_data)` across probe combinations.
* Maximum and median `Tension_H0` values.
* Sensitivity of `Tension_H0` to changes in:

  * inclusion or exclusion of specific probes,
  * reasonable choices of nuisance parameter treatments.

*Falsification conditions:*

* If small, justified changes in modelling choices within `B_base` and `E_adm` (that leave the
  underlying data and main assumptions unchanged) lead to arbitrarily large swings in
  `Tension_H0(m_data)` or even change its qualitative pattern, then the current encoding is
  considered unstable and rejected.
* If `Tension_H0(m_data)` systematically classifies probe combinations known to be internally
  consistent as high tension, while classifying obviously contradictory synthetic combinations
  as low tension, the encoding is considered mis aligned and rejected.

*Semantics implementation note:*

All quantities in this experiment are treated as continuous real valued summaries in line with
the declared field type. No discrete or hybrid interpretation is introduced here.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. This experiment can reject specific
encodings of H0 tension, but it does not determine whether the H0 tension is ultimately due to
systematics, new physics or other causes.

---

### Experiment 2: Synthetic universes with controlled H0 consistency

*Goal:*

Check whether the Q048 encoding can reliably distinguish between synthetic universes with
consistent H0 across probes and synthetic universes with built in H0 inconsistency.

*Setup:*

* Build two families of simulated data sets:

  * Family C (consistent):

    * All probes are generated from a single "true" background cosmology with a fixed H0.
  * Family I (inconsistent):

    * Early probes are generated from one cosmology and late probes from another, or late probes
      are artificially mis calibrated so that their effective H0 differs by several sigma.

* For each simulated data set, construct an effective state in `M_reg` via an encoding in
  `E_adm`, using the same baseline model class `B_base` and the same encoding parameters as
  in Experiment 1.

*Protocol:*

1. For each simulated universe in Family C and Family I, build a state `m_C` or `m_I` in `M_reg`
   capturing early and late H0 summaries and uncertainties.
2. Evaluate `DeltaS_early`, `DeltaS_late`, `DeltaS_cross` and `Tension_H0` for each state.
3. Compute summary statistics:

   * the distribution of `Tension_H0(m_C)` over Family C,
   * the distribution of `Tension_H0(m_I)` over Family I.
4. Optionally vary some encoding settings within `E_adm` (without using information about which
   family a universe belongs to) to check robustness of the separation.

*Metrics:*

* Mean and variance of `Tension_H0` in Family C and Family I.
* A simple separation measure, for example the fraction of cases where
  `Tension_H0(m_I) > Tension_H0(m_C)` for randomly paired universes.
* Stability of this separation under modest changes in encoding details.

*Falsification conditions:*

* If, under reasonable encoding choices within `E_adm`, the distribution of `Tension_H0(m_C)`
  substantially overlaps or exceeds that of `Tension_H0(m_I)` in most simulations, the encoding
  is considered ineffective and rejected.
* If the separation between Family C and Family I exists only for finely tuned encodings that
  depend on knowing which family each universe belongs to, the encoding is considered to violate
  the fairness constraint and is rejected.

*Semantics implementation note:*

The simulated observables are treated as continuous real valued summaries, using the same
interpretation and field type as in the real data experiment. No additional structure is added.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. Success or failure on synthetic universes
only tests the quality of the encoding, not the true origin of the H0 tension in our universe.

---

## 7. AI and WFGY engineering spec

This block describes how Q048 can be used as an engineering module for AI systems within
WFGY style architectures, at the effective layer.

### 7.1 Training signals

We define several training signals that can be used in AI models to encourage tension aware
cosmology reasoning.

1. `signal_H0_consistency`

   * Definition: a penalty proportional to `I_H0(m)` when the model's internal representation
     implies different H0 values for early and late probes in a single scenario where a shared
     H0 is assumed.
   * Purpose: discourage internal reasoning that implicitly treats early and late probes as
     referring to incompatible expansion histories when the context assumes a single H0.

2. `signal_multi_probe_stability`

   * Definition: a signal that penalises large changes in `Tension_H0(m)` across small changes
     in probe sets or nuisance parameter treatments in a controlled test.
   * Purpose: encourage the model to develop representations where conclusions about H0
     consistency are robust to minor, justified changes in modelling.

3. `signal_tension_explanation_quality`

   * Definition: a composite signal derived from whether the model:

     * correctly identifies which probes are in tension,
     * separates "systematics" narratives from "new physics" narratives,
     * avoids collapsing everything into a single averaged H0 without discussion.
   * Purpose: push the model to articulate structured explanations of H0 tension.

4. `signal_counterfactual_H0_worlds`

   * Definition: a signal based on the difference between answers given under explicit World T
     and World F assumptions in prompts, measured by consistency with their respective
     definitions in Block 5.
   * Purpose: encourage the model to keep distinct world assumptions separate rather than
     mixing them.

### 7.2 Architectural patterns

We outline module patterns that reuse Q048 structures without revealing any deep generative
rules of TU.

1. `H0ConsistencyHead`

   * Role: given an internal representation of a cosmology related context, outputs:

     * an estimate of `Tension_H0(m)`,
     * a small vector of components mirroring `DeltaS_early`, `DeltaS_late` and `DeltaS_cross`.
   * Interface:

     * Input: internal embedding of a conversation or document about cosmology.
     * Output: scalar tension estimate plus component wise contributions.
   * Use: serves as an auxiliary head to guide both training and introspection.

2. `MultiProbeAggregator`

   * Role: aggregates partial evidence about H0 from different probes into a unified internal
     state that is suitable for tension evaluation.
   * Interface:

     * Input: probe specific embeddings (for example "CMB analysis", "distance ladder result").
     * Output: unified representation that can be fed to `H0ConsistencyHead`.
   * Use: encourages the model to keep track of which inference came from which probe.

3. `TU_CosmoObserver_H0`

   * Role: specialised observer module that extracts:

     * implied H0 values,
     * uncertainty scales,
     * qualitative statements about tension,
       from internal representations when prompted.
   * Interface:

     * Input: internal state plus an instruction to "observe H0 related quantities".
     * Output: a structured record containing effective H0 summaries and tension estimates.

### 7.3 Evaluation harness

We suggest an evaluation harness for models augmented with Q048 modules.

1. Task design

   * Build a small test suite of questions and prompts that:

     * describe different H0 measurements and their uncertainties,
     * ask whether these are consistent,
     * request explanations of possible resolutions.

2. Conditions

   * Baseline condition:

     * model without explicit Q048 modules.
   * TU condition:

     * same base model but with `H0ConsistencyHead`, `MultiProbeAggregator` and the training
       signals from 7.1 active.

3. Metrics

   * Accuracy on factual questions about the existence and qualitative size of H0 tension.
   * Consistency of implied H0 values across prompts that refer to the same data.
   * Quality of explanations ranked by independent evaluators, with a rubric that values:

     * clear separation of probes,
     * explicit mention of uncertainties,
     * recognition that tension may or may not point to new physics.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience the impact of the Q048 encoding.

* Baseline setup:

  * Prompt the model: "Explain how different measurements of the Hubble constant compare, and
    whether there is any problem or tension."
  * Observe whether the answer:

    * conflates probes,
    * merely reports a range of values,
    * or incorrectly states that there is no known issue.

* TU encoded setup:

  * Prompt the model: "Using the idea of cross probe tension for H0, explain how early universe
    measurements and late universe measurements compare, and describe what it would mean for
    the tension to resolve or to persist."
  * Observe whether the answer:

    * explicitly distinguishes probes,
    * introduces a consistent notion of "tension",
    * frames possible resolutions in a structured way.

* Comparison metric:

  * Use a simple three point scale on:

    * clarity of which probes disagree,
    * explicitness of the tension concept,
    * balance between systematics and new physics narratives.
  * Compare baseline and TU encoded answers according to this scale.

* What to log:

  * Prompts, full responses, and any auxiliary tension estimates from Q048 modules.
  * This allows later auditing of how the model handles high profile consistency problems.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q048 and how they transfer to other
problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `H0_TensionFunctional`

   * Type: functional
   * Minimal interface:

     * Inputs:

       * `H0_early_summary`,
       * `H0_late_summary`,
       * `Sigma_early_summary`,
       * `Sigma_late_summary`,
       * baseline mismatch indicators for early and late probes.
     * Output:

       * `tension_value` in `R_plus`.
   * Preconditions:

     * Inputs must refer to a single world and a single baseline model class.
     * Uncertainties must be strictly positive.

2. ComponentName: `MultiProbeCosmoState`

   * Type: field
   * Minimal interface:

     * Inputs:

       * a list of probe summaries (early and late),
       * a description of the shared model class and nuisance parameter treatment.
     * Output:

       * an internal representation sufficient for evaluating `H0_TensionFunctional`.
   * Preconditions:

     * At least one early probe and one late probe are present.
     * Summaries are mutually compatible in the sense that they can be modelled within one
       coherent cosmology.

3. ComponentName: `CosmoTensionExperimentPattern_H0`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs:

       * a choice of real or synthetic data sets,
       * encoding parameters within `E_adm`.
     * Output:

       * a set of experiment descriptions following the template in Block 6.
   * Preconditions:

     * Data sets must be labelled by probe type and accompanied by uncertainty information.

### 8.2 Direct reuse targets

1. Q041 (dark matter content and clustering)

   * Reused component: `MultiProbeCosmoState`.
   * Why it transfers:

     * Dark matter constraints often mix probes that also constrain H0. The same state structure
       can hold combined information about matter density and expansion rate.
   * What changes:

     * Additional fields are added to the state representing dark matter related observables,
       and the tension functional is extended to include them.

2. Q042 (dark energy equation of state)

   * Reused component: `H0_TensionFunctional`.
   * Why it transfers:

     * Dark energy studies often examine whether changing the equation of state can reconcile
       early and late H0 measurements. The H0 tension functional provides a scalar objective
       to track while scanning model extensions.
   * What changes:

     * Inputs include extra parameters describing the equation of state, and the interpretation
       of baseline mismatch shifts from pure LCDM to an extended model.

3. Q050 (multiverse and landscape cosmology)

   * Reused component: `CosmoTensionExperimentPattern_H0`.
   * Why it transfers:

     * In multiverse scenarios, one can imagine ensembles of universes with different H0 values
       and probe mixes. The experiment pattern gives a template for asking how likely a given
       universe with a certain H0 tension level would be.
   * What changes:

     * Data sets and prior distributions are taken over multiple hypothetical universes instead
       of one realised universe.

4. Q121 (AI alignment in scientific contexts)

   * Reused component: `H0_TensionFunctional` as an example of "inference tension" functional.
   * Why it transfers:

     * Aligned AI systems must detect when different sources of evidence about the same
       quantity disagree at a high level. The H0 case serves as a concrete calibration example.
   * What changes:

     * The quantity of interest is generalised from H0 to arbitrary scalar scientific parameters.

---

## 9. TU roadmap and verification levels

This block explains how Q048 is positioned along the TU verification ladder and what the next
measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of H0 tension has been specified:

    * state space and observables,
    * aggregate tension functional,
    * singular set and domain restrictions,
    * at least two explicit experiments with falsification conditions.

* N_level: N2

  * The narrative linking early and late probes, tension functionals and counterfactual worlds is
    explicit and internally coherent.
  * Reuse paths to other cosmology and AI problems are identified.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented:

1. A practical tool that:

   * takes as input published H0 related probe summaries,
   * constructs states in `M_reg` under a specified encoding in `E_adm`,
   * computes `Tension_H0` and publishes the resulting tension maps as open data.

2. A synthetic benchmark where:

   * families of consistent and inconsistent universes as in Experiment 2 are constructed,
   * the separation performance of different encoding choices is systematically evaluated,
   * results are documented to allow independent reproduction.

Both steps can be carried out using only observable summaries and choices of encoding parameters,
without revealing any deep TU generative rules.

### 9.3 Long term role in the TU program

In the long run, Q048 is expected to serve as:

* A canonical example of cross experiment tension in a mature physical science.
* A calibration case for more general consistency_tension nodes in the BlackHole graph.
* A link between cosmology, information theory and AI alignment, showing how careful handling
  of inferential tension can prevent premature averaging or oversimplified conclusions.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non specialists, while still aligned with the
effective layer description.

The Hubble constant, often written as H0, describes how fast the universe is expanding today.
There are different ways to measure it:

* By looking at the afterglow of the Big Bang (the CMB) and fitting a model of the early
  universe.
* By building a distance ladder in the nearby universe, using objects like Cepheid stars and
  supernovae.
* By using other methods such as gravitational lensing and gravitational wave "standard sirens".

Ideally, all these methods should agree on the same value for H0, within their quoted
uncertainties, if our basic picture of the universe is correct and all known systematics are
under control. Right now they do not fully agree. This is the H0 tension.

In the Tension Universe view, we do not assume any specific method is right or wrong. Instead,
we ask questions like:

* Can we define a number that tells us how badly the different methods disagree?
* Does this number get smaller when we improve our data and modelling, or does it stay stubbornly
  large?

To do this, we imagine states that summarise, in a single place:

* what the early universe measurements say about H0,
* what the late universe measurements say about H0,
* how uncertain each of these is.

Then we define a "tension score" which:

* is small when early and late H0 agree within their uncertainties and both fit a baseline model,
* is large when they do not.

We also imagine two kinds of worlds:

* In one kind (World T), as we improve our measurements and models, the tension score settles
  down to a small value. The tension is then seen as a temporary issue caused by imperfect data
  and modelling.
* In the other kind (World F), no matter how we refine things, the tension score stays large.
  This would suggest that something more fundamental is wrong with our assumptions or that new
  physics is needed.

This way of looking at the problem does not solve the H0 tension. It does not tell us which
data sets to trust or which physical explanation is correct. What it does provide is:

* a clear, quantitative way to talk about how serious the tension is,
* a framework for testing whether particular ways of encoding the data make sense,
* a set of reusable tools that can be applied to other scientific situations where different
  lines of evidence about the same quantity do not agree.

Q048 is the node in the Tension Universe framework that collects all of this structure for the
Hubble constant tension, and connects it to both other cosmology questions and to the design of
AI systems that reason about scientific evidence.
