<!-- QUESTION_ID: TU-Q047 -->
# Q047 · Origin of supermassive black holes

## 0. Header metadata

```txt
ID: Q047
Code: BH_COSMO_EARLYBH_L3_047
Domain: Cosmology
Family: early_universe_and_compact_objects
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-31
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* We only describe state spaces, observables, mismatch functionals, tension scores, counterfactual worlds, and experiment patterns.
* We do not specify any underlying TU axiom system, deep generative rules, or constructive derivations of TU itself.
* We do not define any explicit mapping from raw observational catalogs or simulations to TU state spaces. We only assume that there exist TU compatible models that can reproduce the listed observables.
* We do not introduce any new theorem beyond what is already established in the cited literature for early supermassive black holes.
* We do not claim to have solved the canonical astrophysical problem of supermassive black hole origin.

All falsifiability and experiment statements in this entry apply only to concrete combinations of:

* baseline cosmological models,
* encoding choices in the admissible class Enc_047,
* and specified data or model families.

They do not, by themselves, prove or disprove any fundamental cosmological theory.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem is:

How can supermassive black holes (SMBHs) with masses of order `10^8` to `10^10` solar masses appear at very high redshift (for example `z >= 6`, and now even higher with recent surveys), given the limited cosmic time available for seed formation, accretion, and mergers under physical constraints?

In standard cosmology, early structure formation proceeds from small fluctuations in the matter density field, growing into halos that host the first stars, galaxies, and compact objects. The origin of extremely massive black holes at early times is still not fully understood, because straightforward growth from typical stellar mass seeds often appears too slow when constrained by:

* Eddington limited or mildly super Eddington accretion rates,
* feedback from radiation and outflows,
* realistic merger rates and halo assembly histories.

The canonical problem behind Q047 is to reconcile the observed early SMBH population with physically consistent formation channels, or to clearly characterize the residual inconsistency.

### 1.2 Status and difficulty

There is no single accepted formation channel that explains all known early SMBHs. Current ideas include:

* Light seeds:

  * Remnants of Population III stars with initial masses around `10^2` to `10^3` solar masses, growing through accretion and mergers.

* Heavy seeds:

  * Direct collapse black holes (DCBHs) formed from massive gas clouds with suppressed fragmentation, giving initial masses around `10^4` to `10^6` solar masses.

* Dense stellar cluster collapse:

  * Core collapse of very dense clusters leading to massive black hole seeds.

Each channel faces challenges when confronted with:

* the number densities and masses of observed high redshift quasars,
* limits on how often highly super Eddington accretion can persist,
* feedback that may limit fuel supply,
* constraints from reionization history and background radiation.

The problem is classified here as S rank because:

* it is strongly constrained by multiple observational domains,
* it interacts with fundamental cosmological parameters and structure formation,
* it remains open despite extensive numerical and analytical work.

### 1.3 Role in the BlackHole graph

Within the BlackHole S problem collection, Q047 plays three roles:

1. It is the primary example of a cosmological consistency_tension problem, where formation channels and growth budgets must jointly explain an extreme population within finite time.
2. It anchors the family of early universe anomalies that stress standard structure formation together with H0 tension, CMB anomalies, and related nodes.
3. It provides a concrete test bed for Tension Universe encodings that mix continuous cosmic fields with discrete object counts in a single hybrid description.

### References

1. M. Volonteri, 2010, “Formation of supermassive black holes”, Astronomy and Astrophysics Review, 18, 279 to 315.
2. K. Inayoshi, E. Visbal, Z. Haiman, 2020, “The Assembly of the First Massive Black Holes”, Annual Review of Astronomy and Astrophysics, 58, 27 to 97.
3. X. Fan, C. L. Carilli, B. Keating, 2006, “Observational constraints on quasar growth at high redshift”, Annual Review of Astronomy and Astrophysics, 44, 415 to 462.
4. Representative JWST and ground based survey papers on high redshift quasars and early SMBHs, providing updated mass and number density estimates.

---

## 2. Position in the BlackHole graph

This block records how Q047 connects to other S problems. All edges are given as Q IDs with one line reasons that point to concrete components or tension types.

### 2.1 Upstream problems

These nodes provide foundations and tools that Q047 depends on at the effective layer.

* Q041
  Reason: Encodes the dark matter halo framework and small scale structure seeds that host early SMBH formation environments.

* Q043
  Reason: Supplies primordial fluctuation spectra and initial condition models that set the halo mass function relevant for early SMBH seeds.

* Q045
  Reason: Encodes large scale structure formation timelines and halo growth histories used when early SMBH growth budgets are evaluated.

### 2.2 Downstream problems

These nodes reuse Q047 components or depend on its tension structure.

* Q040
  Reason: Reuses early SMBH population fields as boundary conditions for information flow and evaporation histories of realistic black holes.

* Q048
  Reason: Uses early SMBH growth budget consistency as an additional cross check on early expansion history and H0 reconstruction models.

* Q059
  Reason: Reuses energy and entropy budget components from Q047 as a physically grounded case study in information thermodynamics of extreme systems.

### 2.3 Parallel problems

Parallel nodes have similar tension types but no direct component dependence.

* Q046
  Reason: Both Q046 and Q047 analyze early universe anomalies where standard structure formation timelines are stressed by observations.

* Q048
  Reason: Both encode consistency_tension between early and late time cosmological inferences, expressed through multiple independent observables.

### 2.4 Cross domain edges

Cross domain edges connect Q047 to problems in other domains that can reuse its patterns.

* Q036
  Reason: Can reuse multiscale growth and energy channel budget patterns to structure microscopic and macroscopic constraint matching.

* Q121
  Reason: Uses early SMBH origin as a constrained physical test bed for reasoning about extreme tail events and long horizon planning in AI alignment.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden generative rules, any mapping from raw data or simulations into TU fields, or any deep construction of Tension Universe itself.

### 3.1 State space

We posit an effective semantic state space

```txt
M_047
```

Each element `m` in `M_047` represents a coherent early SMBH cosmos configuration, which includes:

* a summary of the cosmic expansion history over a redshift window of interest,
* halo mass and number density summaries over a range of masses and redshifts,
* black hole seed populations, including seed mass functions and number densities by channel,
* SMBH populations at high masses and high redshifts,
* coarse summaries of accretion and merger histories associated with these populations.

We do not specify how such states are constructed from observational catalogs or simulations. We only assume that, for any finite set of redshift and mass bins, there exist states in `M_047` encoding the relevant summaries in a consistent way.

### 3.2 Core observables and fields

At the effective layer, we define the following observables on `M_047`.

1. Halo abundance field

```txt
n_halo(m; z_bin, k_halo) >= 0
```

* Input:

  * a state `m`,
  * a discrete redshift bin label `z_bin`,
  * a discrete halo mass bin label `k_halo`.

* Output:

  * an effective number density of halos in that bin.

2. Seed population field

```txt
n_seed(m; z_bin, k_seed, channel) >= 0
```

* Input:

  * `z_bin`: redshift bin,
  * `k_seed`: seed mass bin,
  * `channel`: a finite label set for formation channels for example PopIII, DCBH, cluster.

* Output:

  * effective number density of seeds in that bin and channel.

3. SMBH population field

```txt
n_SMBH(m; z_bin, k_BH) >= 0
```

* Input:

  * `z_bin`: redshift bin,
  * `k_BH`: SMBH mass bin for example ranges like 10^8 to 10^9 solar masses.

* Output:

  * effective number density of SMBHs in that bin.

4. Growth budget observable

```txt
G_budget(m; z_seed_bin, z_target_bin, k_seed, k_BH)
```

* Input:

  * a pair of redshift bins `(z_seed_bin, z_target_bin)` with `z_seed_bin` earlier than `z_target_bin` in cosmic time ordering,
  * a seed mass bin label `k_seed`,
  * a target SMBH mass bin label `k_BH`.

* Output:

  * an effective scalar summarizing whether it is physically possible for a seed in `k_seed` at `z_seed_bin` to grow into an SMBH in `k_BH` at `z_target_bin` using allowed channels in the encoding.

The value of `G_budget` is interpreted qualitatively:

* values near 1 indicate that the budget is just sufficient,
* values much greater than 1 indicate surplus growth capacity,
* values much less than 1 indicate a shortfall.

We do not specify the detailed formula, only that it is well defined on `M_047`.

5. Channel mix observable

```txt
F_mix(m; z_range, k_BH)
```

* Input:

  * a redshift range label `z_range`,
  * a target SMBH mass bin label `k_BH`.

* Output:

  * a finite dimensional vector whose components give the fraction of total SMBH mass density in that `k_BH` bin contributed by each seed and growth channel.

### 3.3 Mismatch observables

We now define two mismatch observables.

1. Consistency mismatch

```txt
DeltaS_consist(m; z_target_bin, k_BH)
```

* Nonnegative scalar.
* Measures how far the allowed growth budgets from all seeds and channels fall short of explaining the SMBH population in mass bin `k_BH` at `z_target_bin`, given the encoded physics in `m`.

Qualitative properties:

* If there exist seed distributions and growth histories within physical limits that can account for the observed SMBH mass in that bin, `DeltaS_consist` can be small.
* If no combination within physical limits is sufficient, `DeltaS_consist` stays bounded away from zero.

2. Population mismatch

```txt
DeltaS_pop(m; z_target_bin, k_BH)
```

* Nonnegative scalar.
* Measures the mismatch between the predicted SMBH number density in that bin given the encoding in `m` and a reference number density derived from observations for the same bin.

Qualitative properties:

* If predicted and observed number densities agree within uncertainties, `DeltaS_pop` can be small.
* Large discrepancies drive `DeltaS_pop` up.

### 3.4 Combined tension functional template

We define a basic combined mismatch:

```txt
DeltaS_EBH(m; z_target_bin, k_BH) =
    w_consist * DeltaS_consist(m; z_target_bin, k_BH) +
    w_pop     * DeltaS_pop(m; z_target_bin, k_BH)
```

with:

* `w_consist > 0`,
* `w_pop > 0`,
* `w_consist + w_pop = 1`.

The weights are part of the encoding class and will be fixed globally before any experiment. They cannot be tuned per object or per test set.

To obtain a scalar tension per state, we choose a finite index set `K` of pairs `(z_target_bin, k_BH)` that represent:

* the redshift and mass bins where early SMBH tension is most pronounced based on survey design and known selection functions.

We then define:

```txt
Tension_EBH(m) = max over (z_target_bin, k_BH) in K
                 of DeltaS_EBH(m; z_target_bin, k_BH)
```

This is a maximum over a finite index set, not a supremum over a continuous domain. The composition of `K` is part of the admissible encoding class and is fixed before any application of Q047 to a concrete data set.

### 3.5 Singular set and domain restriction

Some states in `M_047` may encode inconsistent or incomplete information. We define the singular set:

```txt
S_sing_047 = { m in M_047 :
               any of n_halo, n_seed, n_SMBH, G_budget,
               DeltaS_consist, DeltaS_pop, or Tension_EBH
               is undefined or not finite on the index set used }
```

We then define the regular domain:

```txt
M_reg_047 = M_047 \ S_sing_047
```

All tension statements for Q047 are restricted to `M_reg_047`. If an experiment would require evaluating a quantity at a state in `S_sing_047`, that evaluation is treated as out of domain rather than as evidence about the physical world.

### 3.6 Admissible encoding class and fairness constraints

To prevent post hoc tuning, we define an admissible encoding class:

```txt
Enc_047
```

An encoding in `Enc_047` specifies:

* the choice of redshift bins and mass bins,
* the construction of halo, seed, and SMBH summaries,
* the ingredients used in `G_budget`,
* the index set `K` used in `Tension_EBH`,
* the global weights `w_consist`, `w_pop`,
* a discrete refinement parameter `k` and the corresponding map `refine(k)`.

Encodings in `Enc_047` must satisfy:

1. Weight constraint:

   ```txt
   0.3 <= w_consist <= 0.7
   0.3 <= w_pop     <= 0.7
   w_consist + w_pop = 1
   ```

2. Reference independence:

   * The choice of bins, weights, physical limits used in `G_budget`, and the index set `K` must not depend on the detailed properties of particular extreme observed SMBHs.
   * They may depend on broad survey characteristics and known global constraints, but they must be chosen and documented before Q047 is applied to any specific catalog that is used for tension evaluation.

3. Refinement behavior:

   * There exists a discrete refinement parameter `k` in the positive integers and a map:

     ```txt
     refine(k)
     ```

     which, for increasing `k`, performs finer binning in redshift and mass and may include more objects in a controlled way.

   * Across a refinement sequence `enc_k`, physical growth limits, accretion prescriptions, and uncertainty models are held fixed. Refinement can add resolution and sample size, but it cannot quietly introduce new physical assumptions.

4. Stability requirement:

   * For any fixed physical universe representation, the sequence `Tension_EBH^(k)(m_k)` for a compatible sequence of states `m_k` under `enc_k` must not oscillate wildly purely due to refinements that keep physical content similar.

   * If such oscillations occur without a clear physical reason such as a qualitative change in the survey window, the encoding is considered unstable and rejected.

5. Family T and Family F independence:

   * When Q047 is used together with model families such as Family T and Family F in Experiment 2, membership in these families must be specified by physical design choices such as seed channel activation and growth constraints, not by the resulting `Tension_EBH` values.

   * In particular, Family T and Family F cannot be defined by thresholding `Tension_EBH`. Otherwise the separation test would become circular.

Only encodings that satisfy these constraints are members of `Enc_047`.

---

## 4. Tension principle for this problem

### 4.1 Core tension functional

The core tension functional for Q047 is:

```txt
Tension_EBH(m) = max over (z_target_bin, k_BH) in K
                 of DeltaS_EBH(m; z_target_bin, k_BH)
```

where `DeltaS_EBH` is defined as in Block 3.4 and the index set `K` is part of `Enc_047`.

Basic properties:

* `Tension_EBH(m) >= 0` on `M_reg_047`.
* Small values correspond to encodings where early SMBH masses and number densities are consistent with physically allowed growth budgets and channels.
* Large values correspond to encodings where some combination of consistency and population mismatch remains stubbornly high.

For a given encoding `enc_k` in `Enc_047` at refinement level `k`, we can write:

```txt
Tension_EBH^(k)(m) = Tension_EBH(m under enc_k)
```

to emphasize the dependence on refinement.

### 4.2 Low tension principle World T pattern

At the effective layer, a low tension early SMBH universe is one for which there exist:

* an encoding sequence `enc_k` in `Enc_047`,
* a corresponding sequence of states `m_k` in `M_reg_047`,

such that:

```txt
Tension_EBH^(k)(m_k) <= epsilon_EBH
```

for all sufficiently large `k`, where:

* `epsilon_EBH > 0` is a small threshold fixed in advance,
* the inequality is understood in a coarse sense compatible with observational uncertainties and modeling errors.

In words:

* as we refine our description of the early universe and include more detailed halo and SMBH information, the tension associated with early SMBH formation remains within a stable low band.

### 4.3 Persistent high tension principle World F pattern

A persistent high tension early SMBH universe is one for which, for every encoding sequence `enc_k` in `Enc_047` that respects physical constraints, and for every compatible sequence of states `m_k` in `M_reg_047` representing that universe, there exists `delta_EBH > 0` such that:

```txt
Tension_EBH^(k)(m_k) >= delta_EBH
```

for all sufficiently large `k`.

In words:

* no matter how we refine our physically reasonable encodings, the tension associated with early SMBH formation stays bounded away from zero.

### 4.4 Q047 as a tension statement

At the effective layer, we do not claim to know which type of universe we inhabit. Instead, Q047 is framed as:

* a program to encode the origin of early SMBHs in terms of `Tension_EBH`,
* a program to test whether realistic cosmological models and formation channels can reduce `Tension_EBH` into a low band,
* a way to compare different cosmological models by their ability to inhabit a low tension regime under the same class `Enc_047`.

The canonical statement of Q047 in TU terms is therefore:

> Does there exist at least one physically realistic encoding in `Enc_047` and a compatible representation of our universe such that the sequence `Tension_EBH^(k)` remains in a low band across refinements, or does every such encoding show persistent high tension?

Q047 does not assert which answer holds in our universe. It only structures the question in a way that is compatible with TU effective layer rules and with explicit falsifiability for specific encoding choices.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer. These are templates for model families and simulations, not claims about reality.

### 5.1 World T: low tension early SMBH formation

In World T:

1. Seed availability:

   * There exists a combination of seed channels and environments such that the encoded `n_seed` fields provide enough seeds with sufficiently high initial masses in relevant halos at high redshift.

2. Growth history:

   * For a significant fraction of early SMBHs, there exist growth paths from seeds to observed `k_BH` bins where `G_budget` is close to or above 1, without exceeding encoded physical limits.

3. Population statistics:

   * The encoded `n_SMBH` fields match observed number densities within uncertainty bands across the index set `K`.

4. Tension profile:

   * For at least one encoding sequence `enc_k` in `Enc_047` and compatible states `m_k`, the sequence `Tension_EBH^(k)(m_k)` remains bounded by `epsilon_EBH`.

World T represents universes where early SMBH formation is challenging but ultimately compatible with physically reasonable models.

### 5.2 World F: persistent high tension early SMBH formation

In World F:

1. Seed limitations:

   * For any physically reasonable seed channel mix encoded in `Enc_047`, the encoded `n_seed` fields underproduce seeds that can plausibly reach observed masses by the required times.

2. Growth bottlenecks:

   * Encoded `G_budget` values remain below 1 for many observed SMBH bins, even when using the most optimistic but still physical accretion and merger scenarios allowed in the encoding.

3. Population mismatch:

   * Encoded `n_SMBH` systematically underpredict observed number densities in some bins in `K`, by amounts that cannot be reconciled by uncertainty alone.

4. Tension profile:

   * For any encoding sequence and compatible `m_k`, there exists `delta_EBH > 0` such that `Tension_EBH^(k)(m_k) >= delta_EBH` for all sufficiently large `k`.

World F represents universes where early SMBHs of the observed type are effectively impossible to produce given the encoded physics.

### 5.3 Interpretive note

These world templates are used to:

* build model families for experiments,
* define what it means for an encoding to separate plausible from implausible universes in terms of tension.

They do not construct internal TU fields from raw data and do not assert which world our universe belongs to.

---

## 6. Falsifiability and discriminating experiments

This block defines experiments at the effective layer that can:

* falsify specific choices in `Enc_047`,
* test whether the Q047 encoding behaves in a stable, interpretable way.

These experiments cannot solve the canonical astrophysical open problem. They only accept or reject particular encodings.

### Experiment 1: Observational tension band test

*Goal:*
Test whether a given encoding in `Enc_047` can keep `Tension_EBH` within a predefined low band when confronted with current and future early SMBH observations.

*Setup:*

* Inputs:

  * A catalog of high redshift SMBHs with estimated masses and redshifts for example from SDSS, HSC, JWST, and other surveys.
  * A set of cosmological parameters and halo mass function constraints consistent with upstream problems.

* Pre fixed parameters:

  * A global choice of bins and weights defining an encoding sequence `enc_k` in `Enc_047`, selected and documented before detailed catalog analysis.
  * A threshold band `[0, tau_max]` for `Tension_EBH`, with `tau_max` chosen before computing tension values for the test catalog.
  * A tolerance fraction `eta` in `(0, 1)` indicating what fraction of catalog objects may exceed the tension band while still being acceptable. The value of `eta` is chosen in advance based on methodological considerations, not tuned to the catalog at hand.

*Protocol:*

1. Choose a refinement level `k` and take the corresponding `enc_k` in `Enc_047` together with compatible states `m_k_data` that encode the halo, seed, and SMBH summaries for the catalog. The construction of `m_k_data` is not described in TU terms.

2. For each object in the catalog that falls into the index set `K`, compute its contribution to `DeltaS_consist` and `DeltaS_pop`, and therefore to `DeltaS_EBH` and `Tension_EBH^(k)(m_k_data)`.

3. Compute the fraction `f_k` of catalog objects for which `Tension_EBH^(k)(m_k_data)` exceeds `tau_max`.

4. Repeat for several higher refinement levels `k`, updating `m_k_data` and recomputing `f_k` while keeping the encoding class and global parameters fixed.

*Metrics:*

* The sequence `(f_k)` across refinements.
* The distribution of `Tension_EBH^(k)(m_k_data)` for each `k`.
* Stability of these distributions under modest variations of encoding choices that remain within `Enc_047`.

*Falsification conditions:*

* If for a given encoding class and fixed `(tau_max, eta)` it holds that for all sufficiently large `k`:

  ```txt
  f_k > eta
  ```

  then that encoding class is considered falsified as a low tension explanation of early SMBHs.

* If small adjustments of non critical encoding details for example slight changes in bin edges produce large swings in `Tension_EBH` distributions without clear physical justification, the encoding is considered unstable and rejected.

*Semantics implementation note:*
All continuous quantities for example cosmic time, redshift, masses are represented through binned fields, and all object counts are treated as discrete observables. This matches the hybrid description given in the metadata.

*Boundary note:*
Falsifying a TU encoding in this sense does not solve the canonical problem of early SMBH origin. Rejecting an encoding does not by itself prove that early SMBHs cannot be explained or that any particular cosmological model is wrong.

---

### Experiment 2: Model world separation test

*Goal:*
Check whether the Q047 encoding can reliably distinguish between model universes where early SMBHs are easy to produce and model universes where they are designed to be difficult or impossible.

*Setup:*

* Construct or import two model families:

  * Family T models:

    * Cosmological simulations or semi analytic models in which early SMBH formation has been intentionally made efficient but still within stated physical assumptions.

  * Family F models:

    * Models in which early SMBH formation channels are suppressed or restricted in physically motivated ways, leading to far fewer or no high mass black holes at the relevant redshifts.

* For each model and refinement level `k`, construct a state `m_k_T` or `m_k_F` in `M_reg_047` under an encoding `enc_k` in `Enc_047`. The definition of Family T and Family F must be fixed by model construction choices before any `Tension_EBH` values are examined.

*Protocol:*

1. For each model in Family T and each refinement level `k`, compute `Tension_EBH^(k)(m_k_T)`.

2. For each model in Family F and each refinement level `k`, compute `Tension_EBH^(k)(m_k_F)`.

3. For each `k`, construct the empirical distributions:

   ```txt
   D_T^(k) = distribution of Tension_EBH^(k) over Family T
   D_F^(k) = distribution of Tension_EBH^(k) over Family F
   ```

4. Compute a simple separation metric for each `k`, for example the difference in means or a chosen distance between `D_T^(k)` and `D_F^(k)`.

*Metrics:*

* Mean and variance of `Tension_EBH^(k)` for each family.
* A separation score `S_sep(k)` measuring how clearly the two distributions are apart.
* Stability of `S_sep(k)` across reasonable encoding variations in `Enc_047`.

*Falsification conditions:*

* Before running the experiment, fix a threshold `S_sep_thres > 0` that quantifies the minimum acceptable separation between the two distributions.

* If for all reasonable parameter choices in `Enc_047` and all sufficiently large `k`, the separation score `S_sep(k)` remains below `S_sep_thres`, the Q047 encoding is considered ineffective and rejected for use as a diagnostic of early SMBH viability.

* If the encoding assigns systematically lower `Tension_EBH` values to Family F for which early SMBHs are designed to be rare than to Family T where they are designed to be common, the encoding is misaligned with its intended interpretation and is rejected.

*Semantics implementation note:*
Both Family T and Family F models are mapped into the same hybrid representation with binned fields for continuous quantities and discrete counts for objects, as specified in the metadata, so that tension comparisons are meaningful.

*Boundary note:*
Falsifying a TU encoding or failing to separate model families only tests the quality of the encoding. It does not by itself settle the actual origin of early SMBHs in our universe.

---

## 7. AI and WFGY engineering spec

This block describes how Q047 can be used as an engineering module for AI systems within WFGY, without exposing any deep TU generative rules.

### 7.1 Training signals

1. `signal_EBH_growth_budget`

   * Definition:

     * A nonnegative signal derived from `DeltaS_consist(m; z_target_bin, k_BH)` aggregated over the index set `K`.

   * Purpose:

     * Penalize internal representations that imply SMBH growth histories incompatible with physically allowed budgets when the context assumes standard physics.

2. `signal_EBH_population_match`

   * Definition:

     * A signal based on `DeltaS_pop(m; z_target_bin, k_BH)` aggregated over `K`.

   * Purpose:

     * Encourage consistency between modeled SMBH population statistics and observationally based reference profiles when such profiles are part of the assumed background.

3. `signal_EBH_tension_scalar`

   * Definition:

     * Directly equal to `Tension_EBH(m)` for the state associated with the current context.

   * Purpose:

     * Provide a scalar consistency indicator that a model can learn to keep low in scenarios where a low tension early SMBH explanation is assumed.

4. `signal_EBH_counterfactual_clarity`

   * Definition:

     * A signal that penalizes answers that fail to distinguish clearly between World T and World F style assumptions when the user explicitly asks for separate scenarios.

   * Purpose:

     * Help models maintain clean separation between worlds where early SMBHs are easy and worlds where they are hard, instead of mixing them.

### 7.2 Architectural patterns

1. `EarlyBHConsistencyHead`

   * Role:

     * A model head that, given an internal representation of a cosmological context, outputs an estimate of `Tension_EBH(m)` and optionally the decomposed components `DeltaS_consist` and `DeltaS_pop`.

   * Interface:

     * Input: internal context embeddings.
     * Output: `tension_scalar`, optional vector of component scores.

2. `CosmicTimelineFilter`

   * Role:

     * A filtering module that examines proposed narratives about early SMBH formation for example from PopIII seeds at high redshift to SMBHs at lower redshift and checks for gross violations of encoded growth budgets.

   * Interface:

     * Input: structured representation of proposed timeline and growth channels.
     * Output: a soft mask or score indicating whether the narrative is low or high tension under Q047 encoding.

3. `EBH_WorldSwitch_Controller`

   * Role:

     * A controller that toggles between World T and World F assumptions in reasoning chains when requested and ensures that downstream conclusions are consistent with the chosen world.

   * Interface:

     * Input: world selection signal and internal state.
     * Output: modified internal state with appropriately adjusted tension expectations.

### 7.3 Evaluation harness

We outline an evaluation harness to test AI models using Q047 components.

1. Task selection:

   * Analytical tasks:

     * Questions about whether particular SMBH growth histories are plausible under standard physics.

   * Explanatory tasks:

     * Requests to explain the challenges of early SMBH formation and to compare different seed channels.

2. Conditions:

   * Baseline:

     * The model answers without explicit use of `EarlyBHConsistencyHead` or other Q047 modules.

   * TU enhanced:

     * The model uses Q047 signals and modules during inference.

3. Metrics:

   * Consistency:

     * Fraction of answers that avoid obvious violations of growth budgets or cosmic time constraints.

   * Clarity:

     * Degree to which answers explicitly identify where tension arises instead of glossing over it.

   * Stability:

     * Whether the model maintains coherent narratives when prompts are rephrased or extended.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience Q047 encoding effects.

* Baseline setup:

  * Prompt:

    * Ask the AI to explain how astronomers think early SMBHs might form and what the main challenges are.

  * Observation:

    * Note whether the answer lists channels but fails to clearly articulate where time and growth constraints become critical.

* TU encoded setup:

  * Prompt:

    * Ask the same question, but add instructions to organize the explanation around growth budgets and a consistency tension between formation channels and observed SMBH masses at high redshift.

  * Observation:

    * Note whether the answer introduces notions similar to `DeltaS_consist`, `DeltaS_pop`, and `Tension_EBH`, even if those names are not shown, and whether tension hot spots are clearly highlighted.

* Comparison metric:

  * Use a simple rubric to rate:

    * explicit mention of growth time limits,
    * distinction between seed channels,
    * clarity about why certain scenarios remain high tension.

* What to log:

  * Prompts and responses for both setups.
  * Any auxiliary tension estimates produced by the Q047 modules if exposed.
  * This allows later inspection of how Q047 encoding affected the reasoning.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: `EBH_GrowthBudget_Functional`

   * Type: functional

   * Minimal interface:

     * Inputs:

       * `halo_summary` for relevant redshift bins,
       * `seed_summary` by channel,
       * `accretion_constraints` and merger time scale summaries.

     * Output:

       * `consistency_score` in the interval `[0, 1]` interpreted as how close the growth budget is to being sufficient.

   * Preconditions:

     * Inputs must be constructed under an encoding in `Enc_047` and represent mutually consistent summaries for the same cosmological model.

2. ComponentName: `EBH_TensionProfile_Field`

   * Type: field

   * Minimal interface:

     * Inputs:

       * `z_target_bin`,
       * `k_BH`.

     * Output:

       * `tension_value` equal to `DeltaS_EBH(m; z_target_bin, k_BH)`.

   * Preconditions:

     * A state `m` in `M_reg_047` must be available for the cosmological model considered.

3. ComponentName: `EBH_WorldTemplate`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs:

       * `model_class` describing a family of cosmological or physical models that can be mapped into `M_047`.

     * Output:

       * two experiment designs:

         * a World T variant where early SMBHs are made easy,
         * a World F variant where early SMBHs are made hard,

         each with an associated procedure for computing `Tension_EBH`.

   * Preconditions:

     * The model class must provide enough information to define halo, seed, and SMBH summaries at the effective layer.

### 8.2 Direct reuse targets

1. Q048

   * Reused components:

     * `EBH_TensionProfile_Field`.

   * Why it transfers:

     * Q048 studies H0 and related cosmological tensions. Early SMBH tension profiles provide an independent constraint on expansion history and structure growth.

   * What changes:

     * The field is interpreted as a function of H0 and other cosmological parameters, not only of halos and black holes.

2. Q040

   * Reused components:

     * `EBH_GrowthBudget_Functional`.

   * Why it transfers:

     * Realistic black hole information histories need formation and growth budgets as boundary conditions. Q047 provides these budgets for early SMBHs.

   * What changes:

     * The focus shifts from feasibility of formation to how these budgets constrain later information flow and evaporation scenarios.

3. Q059

   * Reused components:

     * `EBH_WorldTemplate`.

   * Why it transfers:

     * Information thermodynamics of extreme systems can use early SMBH origin as a case where tail event modeling and growth constraints are tightly coupled.

   * What changes:

     * The emphasis is on entropy and information flow metrics, while the underlying World T and World F constructions remain similar.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of early SMBH origin has been specified.
  * Mismatch observables `DeltaS_consist` and `DeltaS_pop`, and the combined tension `Tension_EBH`, are defined on a regular domain `M_reg_047`.
  * At least two experiment patterns have been described with clear falsification conditions for encodings in `Enc_047`.

* N_level: N1

  * The narrative of Q047 as a consistency_tension problem is explicit.
  * World T and World F templates are defined in terms of observable patterns and tension behaviors, without exposing deep TU generative rules.

### 9.2 Next measurable step toward E2

To move from E1 to E2, the following measurable steps are envisioned:

1. Finite library instantiation:

   * Define explicit finite libraries for:

     * halo mass function approximations,
     * seed channel recipes,
     * accretion and merger constraints.

   * Implement a concrete subset of `Enc_047` where all elements are fully specified.

2. Refinement behavior study:

   * For at least one realistic cosmological model and one family of simulations, compute `Tension_EBH^(k)` for several refinement levels.
   * Publish the behavior of `Tension_EBH^(k)` and check for stability patterns consistent with the constraints on `Enc_047`.

3. Early observational application:

   * Apply a selected encoding in `Enc_047` to an actual high redshift SMBH catalog.
   * Report the observed fraction `f_k` of high tension objects across refinements.

These steps stay at the effective layer because they operate entirely on observable summaries and do not disclose any deep TU generative machinery.

### 9.3 Long term role in the TU program

In the longer term, Q047 is expected to serve as:

* a benchmark for hybrid encodings where continuous fields and discrete object counts interact,
* a reference consistency_tension problem connecting early universe cosmology, astrophysical black hole demographics, and information focused problems downstream,
* a test case for AI systems using WFGY style tension modules to reason about extreme events over long horizons.

As other S problems relating to cosmology and high energy physics are developed, Q047 will help ensure that their encodings and narratives remain mutually consistent in terms of growth budgets, energy flows, and tail behavior.

---

## 10. Elementary but precise explanation

This block explains Q047 in simpler language while staying faithful to the effective layer description.

Astronomers see very bright quasars in the distant universe. These objects are powered by black holes that are hundreds of millions or even billions of times more massive than the Sun. The surprising part is that some of them appear when the universe was still very young.

To make a supermassive black hole, several ingredients are needed:

* a starting seed black hole,
* gas to feed it,
* time for it to grow through accretion and mergers,
* and a surrounding environment that lets this happen without shutting the process down too soon.

If we try to grow these black holes from typical stellar mass seeds and we respect limits on how fast they can swallow matter without breaking basic physics, the available time can be very tight. In many simple calculations, it seems too tight.

In Tension Universe language, we do not try to solve this formation problem outright. Instead we:

1. Describe each possible universe with early black holes as a state that summarizes:

   * how many halos exist,
   * how many seeds there are, and how massive they are,
   * how big and how numerous the supermassive black holes are,
   * and how fast they are allowed to grow.

2. For each state, we measure two kinds of mismatch:

   * one between what the seeds and growth channels can plausibly produce and what is actually needed,
   * one between predicted and observed numbers of supermassive black holes.

3. We combine these mismatches into a single tension number. If this number is small, the early black holes are easy to explain in that encoding. If it is large, they are hard to explain.

Then we consider two kinds of hypothetical worlds:

* In a low tension world, there is at least one reasonable way to set up the seeds and growth so that, as we take more detailed data into account, the tension stays small.
* In a persistent high tension world, no matter how we set things up within the rules, the tension stays large.

Q047 does not claim we know which kind of world we live in. It gives us:

* a language to talk about why early supermassive black holes are a problem,
* clear quantities to compute from simulations and observations,
* a way to test whether a given description of the early universe makes the problem better or worse.

The same tools can then be reused in other questions where something very massive appears surprisingly early and we need to see whether our models can honestly support it without hidden cheating.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective-layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here state spaces, observables, invariants, tension scores, counterfactual worlds, experiment patterns live strictly at the effective layer of the Tension Universe framework.
* None of these objects should be interpreted as a direct statement about fundamental ontology or dynamics.
* Any concrete numerical implementation requires a separate, explicit source pack and code base, which are outside the scope of this document.

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
