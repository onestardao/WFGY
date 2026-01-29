# Q024 · Origin of neutrino masses and mixing

## 0. Header metadata

```txt
ID: Q024
Code: BH_PHYS_NEUTRINO_MASS_L3_024
Domain: Physics
Family: Particle physics (neutrino and flavor)
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: spectral_tension
Status: Open
Semantics: continuous
E_level: E1
N_level: N1
Encoding_class: A_enc_nu
EncodingKey_Q024: TU_NEUTRINO_MASS_Encoding_v1
LibraryKey_ref_Q024: TU_NEUTRINO_MASS_PriorLib_v1
WeightKey_Q024: TU_NEUTRINO_MASS_Weights_v1
Last_updated: 2026-01-29
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* We only specify:

  * state spaces,
  * observables and effective fields,
  * mismatch measures and tension functionals,
  * counterfactual tension worlds,
  * AI and WFGY engineering hooks.
* We **do not** specify:

  * any underlying TU axiom system,
  * any microscopic TU generative rules,
  * any explicit mapping from raw experimental data or UV Lagrangians to TU internal fields.

More concretely, this page:

* Does not claim to prove or disprove any microscopic theory of neutrino masses and mixing.
* Does not decide whether neutrinos are Dirac or Majorana.
* Does not select a unique seesaw or high scale mechanism.
* Does not introduce any new theorem beyond what is already established in the cited literature.

We assume that for each physically reasonable configuration of neutrino sector parameters, there exist one or more **encoding choices** in an admissible class `A_enc_nu` that map those parameters to states `m` in an effective state space `M_nu`. All observables and tension functionals defined below are evaluated only on the **regular domain** of such encodings and are meant as **bookkeeping tools** for tension, not as microscopic claims.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

In the minimal Standard Model of particle physics, neutrinos are massless.
Experiments have shown that this description is incomplete.

Neutrino oscillation experiments demonstrate that:

* Neutrinos change flavor as they propagate.
* This behavior requires nonzero neutrino masses and mixing among flavor and mass eigenstates.

A convenient effective description uses:

* Three light neutrino mass eigenvalues, usually encoded through mass squared differences:

  ```txt
  Delta_m21_sq = m2_sq - m1_sq
  Delta_m31_sq = m3_sq - m1_sq
  ```

* A unitary mixing matrix (often called PMNS), described by three mixing angles and one or more CP violating phases.

The canonical open problem is:

* What is the fundamental origin of neutrino masses and mixing.
* Are neutrinos Dirac or Majorana particles.
* What sets the size, ordering, and structure of the neutrino mass spectrum and mixing pattern.

Equivalently:

> Find a physically coherent and reasonably simple mechanism that explains:
>
> * Why neutrino masses are nonzero but much smaller than charged lepton and quark masses.
> * Why the observed mixing angles and phases take their measured values, and what correlations among them should exist.
> * Whether neutrinos are their own antiparticles, and if so, how that arises in a more complete theory.

This statement does not assume any specific ultraviolet completion.
It isolates the neutrino sector as an effective layer problem about spectra and mixing.

### 1.2 Status and difficulty

Current experimental information includes:

* Compelling evidence for flavor oscillations in solar, atmospheric, reactor, and accelerator neutrino data.
* Precise measurements of two independent mass squared differences and three mixing angles.
* Hints of CP violation in the lepton sector, although the CP phase is not yet precisely determined.
* Constraints on absolute neutrino mass scale from beta decay, cosmology, and neutrinoless double beta decay searches.

However, the following key questions remain open:

* The absolute neutrino mass scale and exact mass ordering (normal or inverted) are not conclusively determined.
* The Dirac versus Majorana nature of neutrinos is unknown.
* The fundamental mechanism generating neutrino masses is unknown. Proposals include:

  * various seesaw mechanisms,
  * radiative mass generation,
  * effects of extra dimensions or other new sectors.
* There is no universally accepted explanation of why neutrino parameters look as they do, and how they connect to other sectors such as quarks, charged leptons, or high scale physics.

The problem is regarded as extremely difficult, because it likely involves physics at energy scales far beyond direct experimental reach, and it must be compatible with many precise constraints from oscillations, laboratories, and cosmology.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q024 has three main roles.

1. It is the primary **spectral_tension** node for the neutrino sector.
   It encodes how tiny masses and large mixings generate tension with naive expectations from the Standard Model.

2. It acts as a structural bridge between high scale physics and low energy observables.
   Many scenarios for baryogenesis and unification depend on details of neutrino masses and mixing.

3. It provides a reusable pattern for:

   * how to describe small parameters that might arise from hidden high scale structures,
   * how to quantify tension between simple mechanisms and measured spectra,
   * how to keep this description strictly at the effective layer while remaining testable.

### References

1. Particle Data Group, “Neutrino Masses, Mixing, and Oscillations”, in the Review of Particle Physics, latest edition.
2. S. M. Bilenky, “Introduction to the Physics of Massive and Mixed Neutrinos”, Springer, 2010.
3. R. N. Mohapatra and A. Y. Smirnov, “Neutrino Mass and New Physics”, Annual Review of Nuclear and Particle Science 56 (2006) 569.
4. K. Nakamura and S. T. Petcov, “Neutrino Mass, Mixing, and Oscillations”, in earlier editions of the Particle Data Group Review.

---

## 2. Position in the BlackHole graph

This block records the position of Q024 inside the BlackHole graph on nodes Q001 to Q125.
Edges are listed with one line reasons that point to concrete components or tension types.

### 2.1 Upstream problems

These problems provide prerequisites or general frameworks that Q024 relies on at the effective layer.

* Q022 (BH_PHYS_HIERARCHY_L3_022)
  Reason: supplies the general framework for why some masses in the Standard Model are hierarchically small compared to the electroweak scale, which directly includes neutrino masses.

* Q021 (BH_PHYS_QG_L3_021)
  Reason: provides the high scale context for seesaw and other neutrino mass mechanisms that may operate near grand unification or quantum gravity scales.

### 2.2 Downstream problems

These problems reuse Q024 components or depend on its tension structure.

* Q025 (BH_PHYS_BARYON_ASYM_L3_025)
  Reason: reuses neutrino mass and mixing tension components when assessing whether leptogenesis from heavy neutrinos can explain the baryon asymmetry.

* Q041 (BH_COSMO_DARKMATTER_L3_041)
  Reason: uses the neutrino mass spectrum as input when evaluating neutrino contributions to dark matter and sterile neutrino scenarios.

* Q048 (BH_COSMO_H0_TENSION_L3_048)
  Reason: depends on the effective number of neutrino species and their mass spectrum in cosmological fits that may affect the H0 tension.

### 2.3 Parallel problems

Parallel nodes share a similar tension type but no direct component dependence.

* Q023 (BH_PHYS_STRONG_CP_L3_023)
  Reason: both Q023 and Q024 concern small parameters that appear unnatural, and both require explaining why a dimensionless measure of tension is so small.

* Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)
  Reason: both Q024 and Q036 are spectral structure problems where hidden microscopic dynamics must explain observed energy scales and patterns.

### 2.4 Cross domain edges

Cross domain edges connect Q024 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: reuses the pattern “hidden high scale sector induces small effective parameters” as an analogy for the ultimate thermodynamic cost of information processing.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: uses the idea of small but crucial parameters controlled by hidden structure to model misaligned latent directions in AI systems.

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: can import neutrino sector parameters as part of long range cosmological and astrophysical background when constructing Anthropocene scale scenarios.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is strictly at the effective layer.
We describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions,
* admissible encodings and fairness conditions.

We do not describe any deep TU generative rules or any mapping from raw experimental data to internal TU fields.

Unless stated otherwise, all observables in this block are treated as **continuous valued fields**, consistent with `Semantics: continuous` in the header.

### 3.1 State space

We assume the existence of a state space

```txt
M_nu
```

with the following interpretation at the effective layer.

* Each state `m` in `M_nu` represents a coherent “neutrino sector configuration” that encodes:

  * an effective light neutrino mass spectrum, described for example by:

    ```txt
    m_spectrum(m) = (m1, m2, m3, m4, ..., mk)
    ```

    where the first three entries correspond to the three known light neutrinos, and further entries may represent possible sterile states when needed,

  * a mixing descriptor that summarizes the mixing angles and phases in a PMNS like matrix,

  * coarse meta information about whether the configuration lies close to simple texture classes or typical anarchy statistics.

We do not specify how such states are constructed from raw data.
We only require:

* For any set of experimentally allowed neutrino parameters, there exist states `m_data` in `M_nu` that encode them.
* For any model in a simple class of high scale explanations, there exist states `m_model` that summarize its induced low energy neutrino sector.

For the purposes of defining suprema or averages in later observables, we assume that:

* there exists a reasonable collection of subsets of `M_nu` that can serve as admissible region families whenever needed,
* all observables below are well defined and finite on the regular part of the state space.

### 3.2 Effective fields and observables

We define several effective observables on `M_nu`.

1. Neutrino mass spectrum observable

   ```txt
   m_spec(m) = (m1, m2, m3, ..., mk)
   ```

   * Input: state `m` in `M_nu`.
   * Output: a finite vector of nonnegative real numbers representing neutrino masses, or effective mass parameters sufficient for the encoding.

2. Mixing descriptor observable

   ```txt
   U_mix(m)
   ```

   * Input: state `m`.
   * Output: a descriptor that encodes the mixing pattern, for example a tuple of three mixing angles and phases that parametrize a unitary matrix within tolerances.

3. Spectral mismatch observable

   We introduce a class of admissible reference spectra:

   ```txt
   Ref_spec_nu
   ```

   This is a set of simple mass patterns that could arise from low dimensional texture or seesaw models, defined without using detailed real world data.
   Examples include:

   * normal ordering with simple hierarchical ratios,
   * inverted ordering with similar simple ratios,
   * minimal seesaw inspired patterns.

   Given a choice of reference `ref_spec` in `Ref_spec_nu`, we define:

   ```txt
   DeltaS_spec_nu(m; ref_spec) >= 0
   ```

   as a scalar that measures the deviation between `m_spec(m)` and `ref_spec` in a simple norm like way.
   We require:

   * `DeltaS_spec_nu(m; ref_spec) = 0` if the spectrum in `m` matches `ref_spec` exactly,
   * `DeltaS_spec_nu(m; ref_spec)` increases as the spectrum moves further away from the reference pattern.

4. Mixing mismatch observable

   Similarly, we introduce a class of admissible reference mixing patterns:

   ```txt
   Ref_mix_nu
   ```

   This set contains mixing descriptors corresponding to simple textures, such as:

   * approximate tribimaximal patterns,
   * simple one parameter deformations,
   * statistically simple anarchy like distributions.

   Given a reference `ref_mix` in `Ref_mix_nu`, we define:

   ```txt
   DeltaS_mix_nu(m; ref_mix) >= 0
   ```

   as a scalar that measures how far the mixing descriptor `U_mix(m)` deviates from `ref_mix`, again via a simple norm like expression.
   We require:

   * `DeltaS_mix_nu(m; ref_mix) = 0` when the mixing pattern matches the reference exactly,
   * it grows as the mixing pattern departs from that reference.

5. Fairness constraints for reference choices

   The admissible reference classes `Ref_spec_nu` and `Ref_mix_nu` are defined independently of the detailed measured values.
   Once a particular pair `(ref_spec_star, ref_mix_star)` is chosen from these classes for a given encoding, that pair is fixed **before** looking at the full world data set and is then used for all states in the analysis.

   This avoids choosing references after the fact in a way that would artificially reduce tension.

### 3.3 Combined neutrino mismatch

We introduce a finite library of admissible weight pairs:

```txt
L_w_nu
```

Each element of `L_w_nu` is a pair `(w_spec, w_mix)` with:

* `w_spec > 0`, `w_mix > 0`,
* `w_spec + w_mix = 1`.

For any encoding that has fixed a particular pair `(w_spec_star, w_mix_star)` from `L_w_nu` and references `(ref_spec_star, ref_mix_star)` from `Ref_spec_nu` and `Ref_mix_nu`, we define the combined neutrino mismatch observable:

```txt
DeltaS_nu(m) = w_spec_star * DeltaS_spec_nu(m; ref_spec_star)
             + w_mix_star  * DeltaS_mix_nu(m; ref_mix_star)
```

with the following constraints.

* The pair `(w_spec_star, w_mix_star)` is fixed once for a given encoding and is not adjusted after seeing particular world data.
* The library `L_w_nu` is specified at the encoding definition stage and tracked through `WeightKey_Q024`.
* We only consider encodings where all observables needed are finite on the regular domain.

### 3.4 Effective tension tensor components

We assume an effective tension tensor consistent with the TU core decisions:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_nu(m) * lambda(m) * kappa_nu
```

where:

* `S_i(m)` is a source like factor for the ith semantic component that depends on the role of neutrino physics in that component.
* `C_j(m)` is a receptivity like factor that describes how sensitive the jth cognitive or modeling component is to neutrino sector deviations.
* `DeltaS_nu(m)` is the combined neutrino mismatch defined above.
* `lambda(m)` is a convergence state factor, bounded within a fixed range, that encodes whether local reasoning is convergent, recursive, or unstable.
* `kappa_nu` is a sector specific coupling that sets the overall scale of neutrino related tension.

We do not need the explicit index sets for `i` and `j` at this level.
It is sufficient that for each regular state `m`, all tensor components are finite and well defined.

By construction, `T_ij(m)` is a **spectral_tension tensor** for the neutrino sector: it depends only on the observable spectrum and mixing pattern of the neutrino fields and their deviation from simple references, not on any underlying microscopic TU degrees of freedom.

### 3.5 Singular set and domain restriction

Some configurations are physically or logically inconsistent.
We collect them in a singular set:

```txt
S_sing = { m in M_nu :
           m_spec(m) has negative or undefined entries
           or U_mix(m) is not approximately unitary
           or DeltaS_nu(m) is undefined or not finite }
```

We then restrict all tension related analysis to the regular domain:

```txt
M_reg = M_nu \ S_sing
```

Whenever an experiment or protocol would require evaluating `DeltaS_nu(m)` or `Tension_nu(m)` for a state in `S_sing`, the result is treated as **out of domain** and not as evidence about the physical origin of neutrino masses.

### 3.6 Admissible encoding class and fairness constraints

We define the admissible encoding class for Q024 as:

```txt
A_enc_nu
```

An element of `A_enc_nu` is an encoding choice that specifies, at a given resolution:

* a mapping from high level descriptions (for example global fit summaries or simple model outputs) to states in `M_nu`,
* a finite reference library `Ref_spec_nu` of spectral patterns,
* a finite reference library `Ref_mix_nu` of mixing patterns,
* a finite weight library `L_w_nu` of admissible pairs `(w_spec, w_mix)`,
* a selected triple `(ref_spec_star, ref_mix_star, (w_spec_star, w_mix_star))` from these libraries,
* convergence and coupling conventions for `lambda(m)` and `kappa_nu`,
* an explicit rule that all tension evaluations are restricted to `M_reg`.

Fairness and versioning constraints:

* The libraries `Ref_spec_nu`, `Ref_mix_nu`, and `L_w_nu` are defined **without** using detailed world specific data and are tracked by `LibraryKey_ref_Q024` and `WeightKey_Q024`.
* For a given encoding in `A_enc_nu`, the selected references and weights are fixed before any numerical evaluation of world describing states and remain fixed for that encoding.
* Any modification of reference libraries, weight libraries, or mapping details that affect `DeltaS_nu` or `Tension_nu` must be treated as a **new encoding version**, with an updated `EncodingKey_Q024` and a recorded changelog.
* It is not permitted to change reference patterns or weight pairs in response to observed tension values for specific states, if the encoding is to remain within `A_enc_nu`.

These constraints ensure that tension scores are not artificially lowered by post hoc tuning of priors, references, or weights.

---

## 4. Tension principle for this problem

This block states how Q024 is characterized as a tension problem within TU, at the effective layer.

### 4.1 Core tension functional

We define the core neutrino tension functional as:

```txt
Tension_nu(m) = F(DeltaS_spec_nu(m; ref_spec_star),
                  DeltaS_mix_nu(m; ref_mix_star))
```

A simple choice consistent with the constraints above is:

```txt
Tension_nu(m) = DeltaS_nu(m)
```

or equivalently:

```txt
Tension_nu(m) = w_spec_star * DeltaS_spec_nu(m; ref_spec_star)
              + w_mix_star  * DeltaS_mix_nu(m; ref_mix_star)
```

This functional satisfies:

* `Tension_nu(m) >= 0` for all `m` in `M_reg`.
* `Tension_nu(m) = 0` only if the mass spectrum and mixing pattern match the chosen reference pair exactly. This is an idealized limit; realistic world states are expected to have small but nonzero tension.
* `Tension_nu(m)` grows when either spectral or mixing mismatch grows.

In this sense, `Tension_nu` is the **spectral_tension functional** for the neutrino sector: it measures how far an effective neutrino configuration lies from simple reference patterns that stand in for candidate low dimensional mechanisms.

### 4.2 Low tension origin principle

At the effective layer, a low tension origin principle for the neutrino sector can be stated as:

> There exist physically relevant world describing states `m_T` in `M_reg` for which `Tension_nu(m_T)` lies in a modest low tension band, and this band remains bounded as data improve and encodings are refined.

Concretely, for a chosen admissible encoding in `A_enc_nu`:

```txt
exists m_T in M_reg such that
   Tension_nu(m_T) <= epsilon_nu
```

where:

* `epsilon_nu` is a small positive threshold determined and **announced at the encoding definition stage**, before inspecting detailed world tension values,
* refinements of the encoding and additions of realistic data do not force `epsilon_nu` to grow without bound.

In words, there are world like configurations in which simple reference spectra and mixing patterns remain reasonably close to the measured neutrino sector and remain so under reasonable updates.

### 4.3 High tension origin principle

If the origin of neutrino masses requires fine tuning or structurally extreme choices across all reasonable encodings, then the neutrino sector exhibits persistent high tension.

In that case, for any encoding in `A_enc_nu` that satisfies the fairness constraints on references and weights, one expects that for all world describing states `m_F` in `M_reg`:

```txt
Tension_nu(m_F) >= delta_nu
```

for some strictly positive `delta_nu` that is fixed at the encoding level and cannot be pushed arbitrarily close to zero without making the encoding unfaithful to observed or computed neutrino data.

Thus, at the effective layer, Q024 can be viewed as the question:

> Does the universe admit a low tension neutrino sector, or does the structure of neutrino masses and mixing inevitably live in a high tension regime when measured against simple mechanisms within `A_enc_nu`.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds for the neutrino sector, described only in terms of observable patterns and tension functionals.

* World T: neutrino masses and mixing arise from a simple, natural mechanism.
* World F: neutrino masses and mixing arise from structurally complex, fine tuned, or effectively random mechanisms.

Both worlds are defined at the effective layer, in terms of how states in `M_reg` cluster relative to reference patterns and the tension functional `Tension_nu`.

### 5.1 World T (low tension neutrino sector)

In World T:

1. Spectrum structure

   * The mass spectrum in typical world describing states `m_T` is close to a member of `Ref_spec_nu`, for example a simple seesaw inspired hierarchical pattern.
   * The spectral mismatch `DeltaS_spec_nu(m_T; ref_spec_star)` remains modest across refinements of the data and encoding.

2. Mixing structure

   * The mixing descriptor `U_mix(m_T)` lies near a simple reference in `Ref_mix_nu`, such as an approximate tribimaximal pattern corrected by small perturbations.
   * The mixing mismatch `DeltaS_mix_nu(m_T; ref_mix_star)` is stable and comparatively small.

3. Correlation patterns

   * There exist correlations between masses and mixing angles that can be encoded as low dimensional relations in the observable space.
   * These relations allow a compact parametrization of the allowed region for `m_spec` and `U_mix`.

4. Global tension

   * There exist world states `m_T` in `M_reg` for which:

     ```txt
     Tension_nu(m_T) <= epsilon_nu
     ```

     with `epsilon_nu` small and not forced to increase under reasonable data improvements or encoding refinements.

### 5.2 World F (high tension neutrino sector)

In World F:

1. Spectrum structure

   * The mass spectrum in world describing states `m_F` does not lie near any simple reference in `Ref_spec_nu`.
   * The spectral mismatch `DeltaS_spec_nu(m_F; ref_spec)` remains large for all admissible references.

2. Mixing structure

   * The mixing descriptor `U_mix(m_F)` behaves in a way that is difficult to approximate by any simple pattern in `Ref_mix_nu`.
   * The mixing mismatch `DeltaS_mix_nu(m_F; ref_mix)` does not admit a small and stable bound across refinements.

3. Loss of simple correlations

   * Any correlations between masses and mixing angles appear accidental or highly sensitive to small parameter changes.
   * Effective low dimensional parametrizations of the allowed region fail or require many parameters.

4. Global tension

   * For world describing states `m_F` in `M_reg`, there exists a scale `delta_nu > 0` such that:

     ```txt
     Tension_nu(m_F) >= delta_nu
     ```

     and attempts to reduce tension by changing references or weights while staying inside `A_enc_nu` do not remove this lower bound.

### 5.3 Interpretive note

These counterfactual worlds do not describe any deep TU generative rules or specific high scale Lagrangians.
They only describe how observable neutrino sector configurations cluster around or avoid simple reference patterns, and how this behavior is captured by the tension functional `Tension_nu`.

Q024 does not claim to know which type of world we inhabit.
Its role is to make these patterns explicit, measurable, and reusable for other problems.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

* test whether a given TU encoding of the neutrino sector is coherent,
* discriminate between encoding choices,
* provide evidence for or against specific simple mechanism interpretations.

These experiments do not prove or disprove any particular microscopic model.
They can falsify or support effective layer encodings of Q024.

We assume throughout that all constructed states used in these experiments lie in `M_reg`. Any state that falls in `S_sing` is treated as out of domain and excluded from numerical tension evaluations.

### Experiment 1: Global fit tension profiling

**Goal**
Test whether a given `Tension_nu` encoding yields stable and interpretable tension profiles when applied to global fits of neutrino data.

**Setup**

* Input: global fit summaries of neutrino oscillation parameters, including:

  * best fit values and uncertainties for two mass squared differences and three mixing angles,
  * allowed ranges for CP violating phase parameters,
  * normal and inverted ordering scenarios.
* For each scenario (normal or inverted ordering), construct world describing states:

  ```txt
  m_data_NO
  m_data_IO
  ```

  in `M_reg` that encode these summaries.
* Choose and record once:

  * a fixed admissible pair `(ref_spec_star, ref_mix_star)` from `Ref_spec_nu` and `Ref_mix_nu`,
  * a fixed weight pair `(w_spec_star, w_mix_star)` from `L_w_nu`,
  * a low tension threshold `epsilon_nu` and a high tension threshold `T_threshold_nu`, set at the encoding level.

These choices are tied to `EncodingKey_Q024`, `LibraryKey_ref_Q024`, and `WeightKey_Q024` and are not adjusted after seeing tension values.

**Protocol**

1. For each scenario, compute:

   ```txt
   DeltaS_spec_nu(m_data; ref_spec_star)
   DeltaS_mix_nu(m_data; ref_mix_star)
   Tension_nu(m_data)
   ```

   using the definitions from Block 3.

2. Explore the effect of realistic parameter uncertainties by sampling states around the best fit point and evaluating the distribution of `Tension_nu`.

3. Compare the tension distributions between normal and inverted ordering and across different global fit analyses, when available.

**Metrics**

* Typical values and spread of `Tension_nu` for each ordering scenario.
* Sensitivity of `Tension_nu` to realistic changes in oscillation parameters.
* Degree of stability of the tension distribution when using updated global fits.

**Falsification conditions**

The encoding under the current `EncodingKey_Q024` is considered falsified or unstable at the effective layer if any of the following holds:

1. For all admissible `(ref_spec_star, ref_mix_star)` and `(w_spec_star, w_mix_star)` in the pre announced libraries, every world describing state `m_data_*` that matches current fits satisfies:

   ```txt
   Tension_nu(m_data_*) > T_threshold_nu
   ```

   even though the encoding was intended to represent a simple low tension origin.

2. Incorporating updated global fits requires ad hoc changes to `Ref_spec_nu`, `Ref_mix_nu`, or `L_w_nu`, or changes to `epsilon_nu` or `T_threshold_nu` that are driven by the observed tension values, in order to keep `Tension_nu` below `T_threshold_nu`. In that case, the encoding violates fairness and is rejected as a Q024 encoding.

3. Small changes in the input data produce unreasonably large, unstructured jumps in `Tension_nu` for world describing states, indicating that the encoding is numerically unstable or under specified.

**Semantics implementation note**

All quantities are treated as continuous valued observables with finite resolution.
No discrete or hybrid semantics are introduced in this experiment. All tension values are evaluated on states in `M_reg`.

**Boundary note**

Falsifying a TU encoding of the neutrino sector does not solve the canonical origin problem.
This experiment can reject specific tension encodings but does not by itself determine the true microscopic mechanism.

---

### Experiment 2: Future experiment sensitivity template

**Goal**
Assess how projected future experiments constrain the allowed `M_reg` region and the possible `Tension_nu` range, and whether simple low tension encodings remain viable.

**Setup**

* Consider projected sensitivities from long baseline experiments, reactor experiments, and neutrinoless double beta decay searches.
* For each experiment class, define a projected constraint region in the space of mass and mixing parameters, consistent with `M_reg`.

**Protocol**

1. For each projected constraint region, define a family of hypothetical states:

   ```txt
   { m_proj_i }
   ```

   in `M_reg` that are compatible with those constraints.

2. For each state in this family, compute `Tension_nu(m_proj_i)` using the fixed encoding parameters `(ref_spec_star, ref_mix_star, w_spec_star, w_mix_star)`.

3. Track how the envelope of achievable tension values changes as one goes from current constraints to projected constraints.

**Metrics**

* The minimal possible tension in the projected allowed region.
* The fraction of states in the projected region with tension below `epsilon_nu`.
* Sensitivity of low tension regions to specific future measurement outcomes, for example a confirmed normal ordering or a measured CP phase.

**Falsification conditions**

The encoding under the current `EncodingKey_Q024` is considered disfavored or inadequate if:

1. It predicts that for some realistic class of future experimental outcomes, all states in `M_reg` compatible with those outcomes satisfy:

   ```txt
   Tension_nu(m_proj_i) >= T_threshold_nu
   ```

   yet when such outcomes are realized, independent analyses show that low tension configurations remain available in other well specified encodings.

2. The encoding cannot represent the effect of new constraints as meaningful changes in `DeltaS_spec_nu` or `DeltaS_mix_nu`, for example if it lacks enough resolution to distinguish qualitatively different future scenarios. In that case the encoding is underspecified for Q024 and should be revised as a new version.

3. Maintaining a low tension band after future data requires retroactive changes to the reference libraries or weight library that were not planned at the encoding stage.

**Semantics implementation note**

The experiment treats mass and mixing parameters as continuous observables and uses standard uncertainty bands in that representation. All calculations are restricted to `M_reg`.

**Boundary note**

Falsifying a TU encoding with respect to future experiment sensitivity does not establish which microscopic scenario is true.
It only evaluates how useful and stable a given tension encoding is for organizing expectations and interpreting results.

---

## 7. AI and WFGY engineering spec

This block describes how Q024 can be used as an engineering module for AI systems within WFGY, strictly at the effective layer.

The components defined here are **internal diagnostic and steering tools** for AI models. They are not physical mechanisms and must not be interpreted as experimentally confirmed descriptions of the neutrino sector.

### 7.1 Training signals

We define several training signals that leverage the Q024 encoding.

1. `signal_nu_spectrum_coherence`

   * Definition: a penalty signal proportional to `DeltaS_spec_nu(m; ref_spec_star)` when the current context discusses neutrino mass spectra.
   * Purpose: encourage internal representations that treat obviously incoherent or unphysical mass patterns as high tension and disfavored.

2. `signal_nu_mixing_structure`

   * Definition: a signal proportional to `DeltaS_mix_nu(m; ref_mix_star)` when mixing angles and phases appear in the context.
   * Purpose: nudge the model to favor mixing configurations that lie near simple and coherent patterns when such patterns are explicitly assumed in the prompt or configuration.

3. `signal_nu_tension_score`

   * Definition: equal to `Tension_nu(m)` for states extracted from model internal representations.
   * Purpose: provide a scalar summary of how compatible the model’s internal neutrino story is with the chosen low tension encoding. This can be used as an auxiliary loss or monitoring metric.

4. `signal_nu_counterfactual_consistency`

   * Definition: measures the stability and separation of model outputs when prompts explicitly assume a simple low tension world (World T) versus a high tension world (World F).
   * Purpose: encourage the model to separate “assume simple mechanism” and “assume complicated mechanism” modes rather than mixing them in a single answer.

### 7.2 Architectural patterns

We outline module patterns that reuse Q024 structures.

1. `NuSpectrumObserver`

   * Role: extract an effective `m_spec(m)` descriptor from internal embeddings when the model processes neutrino related text.
   * Interface:

     * Input: a context embedding or token level representation.
     * Output: a compact vector approximating neutrino mass parameters that can be treated as `m_spec(m)` for tension calculations.

2. `NuFlavorTensionHead`

   * Role: evaluate `DeltaS_spec_nu`, `DeltaS_mix_nu`, and `Tension_nu` as auxiliary outputs.
   * Interface:

     * Input: a joint descriptor of spectrum and mixing such as `(m_spec(m), U_mix(m))`.
     * Output: a small set of scalar tension scores, for example `(DeltaS_spec_nu, DeltaS_mix_nu, Tension_nu)`.

3. `TU_NuField_Observer`

   * Role: provide a generic link between the model’s internal representations and effective neutrino sector observables used in the tension encoding.
   * Interface:

     * Input: high dimensional internal embeddings.
     * Output: low dimensional observables suitable for Q024, such as spectra, mixing descriptors, and flags for whether the current context is in domain.

These modules do not fix any underlying physics. They only help the AI keep its neutrino related reasoning consistent with a given effective layer encoding.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models with Q024 style modules.

1. Task design

   * Collect a set of problems where neutrino oscillations, mass ordering, and mixing are relevant, including thought experiments and real data summaries.

2. Baseline condition

   * The model operates without explicit Q024 modules or signals.
   * Evaluate consistency and correctness of its answers.

3. TU enhanced condition

   * The model uses Q024 inspired observers and tension heads as auxiliary guidance.
   * Measure changes in reasoning quality and internal consistency, especially in multi step explanations or scenario comparisons.

4. Metrics

   * Accuracy on neutrino related questions with known answers.
   * Frequency of internal contradictions about mass ordering or mixing patterns across related prompts.
   * Stability when prompts switch between different hypothetical scenarios (for example assume normal ordering vs assume inverted ordering).

### 7.4 60 second reproduction protocol

A minimal user facing protocol:

* Baseline setup

  * Prompt: ask the AI to explain how neutrino oscillations imply nonzero masses and mixing, and why these masses are much smaller than those of other fermions.
  * Observation: record whether the explanation is fragmented, glosses over hierarchy issues, or mixes up different experimental constraints.

* TU encoded setup

  * Prompt: ask the same question but instruct the AI to organize the explanation around a “neutrino tension score” that measures how strange the observed masses and mixing are compared to simple mechanisms.
  * Observation: record whether the explanation becomes more structured and explicit about the role of small parameters and high scale physics, and whether it cleanly distinguishes assumptions.

* Comparison metric

  * Use a simple rubric for structure, explicit linkages, and consistency.
  * Optionally ask external evaluators to choose which answer better expresses the core issues of the neutrino sector.

* What to log

  * All prompts, responses, and any auxiliary tension scores such as `Tension_nu`.
  * This allows later inspection of reasoning patterns without exposing any internal TU generative rules.

**Boundary note**

Even when Q024 style modules are used, AI answers remain explanatory narratives at the effective layer.
They do not constitute experimental evidence for any particular neutrino mass mechanism.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q024 and how they transfer to other problems.

Any reuse must respect the encoding and fairness constraints of the target problem and must explicitly declare its own reference and weight choices instead of silently inheriting those of Q024.

### 8.1 Reusable components produced by this problem

1. ComponentName: `NuMassMixingField_Descriptor`

   * Type: field

   * Minimal interface:

     * Inputs: internal or external descriptions of neutrino sector parameters.
     * Output: a compact descriptor containing mass spectrum and mixing parameters.

   * Preconditions:

     * Inputs must represent physically meaningful parameter sets within approximate current constraints and lie in the regular domain of the target encoding.

2. ComponentName: `NuTensionFunctional`

   * Type: functional

   * Minimal interface:

     * Inputs: a `NuMassMixingField_Descriptor` and the fixed encoding parameters `(ref_spec_star, ref_mix_star, w_spec_star, w_mix_star)` for the target problem.
     * Output: a scalar `Tension_nu_value`.

   * Preconditions:

     * The descriptor must correspond to a state in the regular domain of the target problem, analogous to `M_reg` for Q024.

3. ComponentName: `NuCounterfactualWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a model class specifying how neutrino parameters emerge from a higher level theory.
     * Output: a pair of experiment designs representing a low tension scenario and a high tension scenario, each with a specified method for computing `Tension_nu`.

   * Preconditions:

     * The model class must allow extraction of effective neutrino sector parameters at the level of the encoding, and must provide only regular states for tension evaluation.

### 8.2 Direct reuse targets

1. Q025 (BH_PHYS_BARYON_ASYM_L3_025)

   * Reused components: `NuMassMixingField_Descriptor`, `NuTensionFunctional`.
   * Why it transfers: leptogenesis scenarios depend sensitively on neutrino masses and mixings, so baryon asymmetry tension patterns can be expressed partly in terms of a neutrino tension contribution.
   * What changes: additional observables and functionals are added for baryon number violating processes and CP violation beyond the neutrino sector. Priors, reference sets, weights, and thresholds must be declared and versioned in Q025 and cannot silently reuse Q024 choices.

2. Q041 (BH_COSMO_DARKMATTER_L3_041)

   * Reused components: `NuMassMixingField_Descriptor`.
   * Why it transfers: the neutrino mass spectrum contributes to hot dark matter and influences sterile neutrino dark matter scenarios.
   * What changes: the descriptor is combined with cosmological observables to build a dark matter tension functional. Any neutrino related tension indices in Q041 must have their own encoding keys and thresholds.

3. Q048 (BH_COSMO_H0_TENSION_L3_048)

   * Reused components: `NuMassMixingField_Descriptor`, possibly `NuTensionFunctional`.
   * Why it transfers: effective neutrino sector parameters, such as the sum of masses and effective number of species, play a role in cosmological fits that affect the H0 tension.
   * What changes: `Tension_nu` feeds into a larger cosmological tension functional that combines neutrino, dark matter, and expansion history contributions. All priors and weights must be defined under Q048’s own encoding class.

**Cross problem reuse rule**

Whenever Q024 components are reused:

* The target problem must define its own encoding class, reference libraries, weight libraries, and thresholds.
* The target problem must track its own encoding keys and not implicitly rely on `EncodingKey_Q024`.
* Any reuse must respect the TU charters about effective layer scope, encoding fairness, and tension scales.

---

## 9. TU roadmap and verification levels

This block explains how Q024 sits on the TU verification ladder and what the next measurable steps are.

The labels `E_level` and `N_level` are interpreted according to the internal TU verification guidelines for effective encodings and narratives, as referenced by the TU charters.

### 9.1 Current levels

* E_level: E1

  * The encoding specifies a clear state space (`M_nu`), observables, and a basic spectral tension functional (`Tension_nu`).
  * At least two experiments with explicit falsification conditions are defined.
  * Fairness constraints for references and weights are in place and tied to explicit keys.

* N_level: N1

  * The narrative explains how small neutrino masses and large mixing can be framed as a tension problem.
  * Counterfactual worlds are sketched in terms of tension patterns, but no exhaustive enumeration of model classes is attempted.

### 9.2 Next measurable step toward E2

To move Q024 from E1 to E2, one or more of the following concrete actions should be taken, under a new `EncodingKey_Q024` version:

1. Implement a small open source tool that:

   * accepts neutrino parameter sets as input,
   * constructs `NuMassMixingField_Descriptor` objects,
   * computes `Tension_nu` values using fixed encoding parameters tied to `LibraryKey_ref_Q024` and `WeightKey_Q024`,
   * publishes example tension profiles for current global fits and makes both code and data publicly available.

2. Construct a small library of toy model families for neutrino mass generation, and for each family:

   * generate sample parameter sets,
   * evaluate their `Tension_nu` distribution,
   * publish comparative results that show which mechanisms naturally land in low tension regions and which do not, under the same encoding.

These steps remain completely within the effective layer, because they operate only on observable parameter sets and do not expose any underlying TU generative rules.

### 9.3 Long term role in the TU program

In the long term, Q024 is expected to serve as:

* The central neutrino sector node for all problems that depend on neutrino masses and mixing.
* A template for how to encode small parameter puzzles as spectral tension problems without claiming microscopic solutions.
* A bridge between high scale theoretical ideas and low energy experiments, allowing both to be discussed in a common tension language.

Further upgrades beyond E2 and N1 would involve:

* richer libraries of reference patterns and toy models,
* more elaborate experimental templates,
* and integration with broader TU wide tension dashboards, always under updated encoding keys.

---

## 10. Elementary but precise explanation

Neutrinos are extremely light particles that come in three known flavors.
Experiments show that these flavors mix with each other and that the mixing depends on distance and energy in a way that can only happen if neutrinos have nonzero masses.

The puzzle is that:

* Neutrinos are not massless, so the minimal Standard Model is incomplete.
* Their masses are much smaller than those of other particles such as electrons or quarks.
* Their mixing pattern is very different from the mixing pattern of quarks.

The central question is:

> What mechanism gave neutrinos their masses and mixing, and why do the numbers look the way they do.

The Tension Universe view does not attempt to build a detailed high scale theory.
Instead, it asks a more modest but sharp question.

* Define a way to summarize neutrino masses and mixing in a compact descriptor.
* Choose simple reference patterns that might come from clean mechanisms, such as a basic seesaw model or simple texture.
* Measure how far the real world descriptor lies from these reference patterns and call this the neutrino tension.

If there exists a world description in which this tension stays small and stable as data improve, then the neutrino sector can be thought of as low tension within that encoding.
If every faithful description of the neutrino sector looks far from any simple reference pattern, no matter how one encodes it within reasonable rules, then the origin of neutrino masses is high tension.

This approach:

* does not claim to solve the origin problem,
* does provide a precise way to talk about how strange the neutrino sector looks,
* creates reusable tools that help describe related problems in cosmology, baryogenesis, and AI modeling.

Q024 is therefore the node that turns “why are neutrinos so light and so mixed” into a structured spectral tension question that can be tested, falsified, and reused across the Tension Universe framework.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an **effective layer encoding** of the neutrino mass and mixing problem within the TU framework.
* It does not claim to prove or disprove the canonical statement in Section 1 about the microscopic origin of neutrino masses.
* It does not decide whether neutrinos are Dirac or Majorana, nor does it select a unique seesaw or high scale mechanism.
* It does not introduce any new theorem beyond what is already established in the cited literature and standard neutrino phenomenology.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective layer boundary

* All objects used here, including:

  * state spaces `M_nu`, regular domains `M_reg`, and singular sets `S_sing`,
  * observables such as `m_spec(m)` and `U_mix(m)`,
  * mismatch measures `DeltaS_spec_nu`, `DeltaS_mix_nu`, `DeltaS_nu`,
  * the spectral tension functional `Tension_nu(m)`,
  * counterfactual worlds (World T and World F),
    live purely at the TU effective layer.
* No claim is made about how these objects arise from any deeper TU axiom system or from microscopic field theories.
* Any mappings from experimental data or high scale models to these effective objects are part of the encoding class and are not TU axioms.

### Encodings, fairness, and versioning

* The admissible encoding class for this problem is `A_enc_nu`.

* The current encoding version is labeled by:

  ```txt
  EncodingKey_Q024: TU_NEUTRINO_MASS_Encoding_v1
  LibraryKey_ref_Q024: TU_NEUTRINO_MASS_PriorLib_v1
  WeightKey_Q024: TU_NEUTRINO_MASS_Weights_v1
  ```

* Reference libraries for spectra and mixing patterns (`Ref_spec_nu`, `Ref_mix_nu`) and weight libraries (`L_w_nu`) are defined independently of detailed world data and are fixed for a given encoding version.

* All tension evaluations are restricted to the regular domain `M_reg`. States in `S_sing` are treated as out of domain and are not used to support or refute physical claims.

* Priors, reference patterns, weight pairs, and thresholds (`epsilon_nu`, `delta_nu`, `T_threshold_nu`) must be specified before numerical tension evaluation and must not be retuned in response to observed tension values for specific states.

* Any change to these elements that affects `Tension_nu` must be recorded as a new encoding version, with an updated `EncodingKey_Q024` and an explicit changelog.

### Cross problem reuse

* Components exported by Q024 (such as `NuMassMixingField_Descriptor`, `NuTensionFunctional`, and `NuCounterfactualWorld_Template`) may be reused by other problems only if:

  * the target problem defines its own encoding class and regular domain,
  * the target problem declares and versions its own reference libraries, weights, and thresholds,
  * the reuse respects the TU charters on effective layer scope, encoding fairness, and tension scales.
* Cross problem reuse does not transfer any microscopic claim about neutrino physics. It only transfers effective layer bookkeeping patterns.

### TU charters

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
