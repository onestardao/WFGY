<!-- QUESTION_ID: TU-Q023 -->
# Q023 · Strong CP problem

## 0. Header metadata

```txt
ID: Q023
Code: BH_PHYS_STRONG_CP_L3_023
Domain: Physics
Family: Strong CP and QCD vacuum
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: continuous
E_level: E1
N_level: N1
Last_updated: 2026-01-30
EncodingKey_Q023: TU_STRONG_CP_Encoding_v1
LibraryKey_ref_Q023: TU_STRONG_CP_PriorLib_v1
WeightKey_Q023: TU_STRONG_CP_Weights_v1
```

---

## 0. Effective layer disclaimer

All claims in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* This document specifies an effective layer encoding of the strong CP problem in terms of:

  * state spaces,
  * observables,
  * mismatch functionals,
  * tension scores,
  * counterfactual tension worlds,
  * AI facing engineering interfaces.

* It does not:

  * prove or disprove the canonical strong CP statement,
  * introduce any new theorem about QCD, CP violation, or quantum field theory,
  * claim that any specific Peccei Quinn or ultraviolet mechanism is realized in nature,
  * claim that the strong CP problem has been solved.

* All TU objects used here:

  * state space `M`,
  * observables such as `theta_eff(m)` and `O_EDM(m)`,
  * mismatch functionals such as `DeltaS_theta(m)` and `DeltaS_EDM(m)`,
  * tension indices such as `Tension_CP(m)`,
  * counterfactual worlds `World T_CP` and `World F_CP`,
    live entirely at the effective layer. They are bookkeeping devices over observable summaries, not microscopic fields or fundamental variables.

* No deep TU generative rules, axiom systems, or constructive procedures are specified or assumed in this page. In particular:

  * We do not describe how TU itself is generated from ZFC or any other base theory.
  * We do not define any mapping from raw QCD Lagrangians or ultraviolet completions to the internal TU ontology.
  * We only assume that for any consistent microscopic scenario, there exists at least one effective layer state `m` that encodes its observable consequences.

* This page should not be cited as evidence that strong CP is resolved. At most, it may be cited as:

  * a description of how the strong CP problem can be expressed as an effective layer tension problem inside TU,
  * a specification of certain mismatch functionals and experiments that can be used to audit encodings and AI systems.

For Q023 in particular, the strong CP tension indices defined here are diagnostic tools on effective observables. They are not themselves physical mechanisms and they do not decide which, if any, proposed strong CP resolution is realized in nature.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

In quantum chromodynamics (QCD), the most general renormalizable Lagrangian for the strong interactions allows a term of the form

```txt
L_theta = (theta_QCD / 32 pi^2) * G_a^{mu nu} * G̃_{a,mu nu}
```

where:

* `theta_QCD` is a dimensionless parameter,
* `G_a^{mu nu}` is the gluon field strength,
* `G̃_{a,mu nu}` is its dual,
* the term is odd under CP.

In addition, phases in the quark mass matrix contribute to an effective strong CP angle. The physical, observable angle can be written schematically as

```txt
theta_eff = theta_QCD + arg det(M_q)
```

where `M_q` is the quark mass matrix. The precise expression is not needed here; the key point is that `theta_eff` controls CP violation in the strong interactions.

The strong CP problem is the following canonical question:

> Why is the effective strong CP angle `theta_eff` so extremely small, consistent with experimental bounds that suggest `|theta_eff|` is less than about `10^{-10}`, when a natural expectation would allow `theta_eff` to be of order 1?

Equivalently, among all a priori allowed values of `theta_eff` in the range `(-pi, pi]`, why does nature realize a value that is so close to zero that no strong CP violation has been observed, especially in the neutron electric dipole moment (EDM)?

### 1.2 Status and difficulty

Experimentally:

* Measurements of the neutron EDM `d_n` give extremely strong bounds on CP violation in the strong sector.
* Current limits imply that `|theta_eff|` is smaller than roughly `10^{-10}`, with the exact numerical bound depending on theoretical assumptions in the mapping from `theta_eff` to `d_n`.

Theoretically:

* QCD as a gauge theory does not force `theta_QCD` to vanish.
* Quark masses are generically complex, contributing additional CP phases.
* No symmetry in the minimal Standard Model enforces `theta_eff = 0`.

Several broad classes of proposed resolutions exist:

* Peccei Quinn (PQ) mechanisms and axions introduce a new approximate symmetry that dynamically relaxes `theta_eff` toward zero.
* Massless up quark scenarios attempt to rotate away phases if one quark mass were exactly zero, but these are disfavored by current data.
* Spontaneous CP violation with special alignment attempts to arrange the vacuum such that effective strong CP violation cancels.

Despite decades of work, no universally accepted and experimentally confirmed solution is known. The problem is regarded as one of the central naturalness puzzles in high energy physics.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q023 plays several roles:

1. It is a primary example of a consistency_tension problem in physics, where a dimensionless parameter is allowed to be of order 1 but is observed to be extremely small.

2. It provides a canonical template for encoding naturalness tension between:

   * a prior over parameters (here, a prior over `theta_eff`),
   * and realized observational constraints (neutron EDM bounds and other CP sensitive observables).

3. It acts as a bridge between:

   * QCD vacuum structure and topological sectors,
   * constraints from EDM experiments,
   * and broader questions of parameter tuning that also appear in other S level problems such as the hierarchy problem and cosmological constant problem.

### References

1. Particle Data Group (PDG), strong CP problem and electric dipole moment sections, in the Review of Particle Physics.
2. M. E. Peskin, D. V. Schroeder, “An Introduction to Quantum Field Theory”, Addison Wesley, 1995, chapters on QCD, anomalies, and the theta term.
3. S. Weinberg, “The Quantum Theory of Fields, Volume 2: Modern Applications”, Cambridge University Press, 1996, sections on nonabelian gauge theories and CP violation.
4. J. E. Kim, G. Carosi, “Axions and the Strong CP Problem”, Reviews of Modern Physics 82 (2010).
5. M. Dine, “TASI lectures on the strong CP problem”, in a standard TASI lecture series volume.

---

## 2. Position in the BlackHole graph

This block records the position of Q023 in the BlackHole graph. Edges reference other Q nodes and point to concrete components or tension functionals defined in this file.

### 2.1 Upstream problems

These problems provide prerequisites or general frameworks on which the Q023 encoding depends.

* Q022 (BH_PHYS_HIERARCHY_L3_022)
  Reason: Supplies the general naturalness framework and tuning index tools that are reused by the `ThetaTensionFunctional` and `Tension_CP` defined here.

* Q028 (BH_PHYS_QCD_CONFINEMENT_L3_028)
  Reason: Provides the effective description of QCD vacuum structure and topological sectors that underlies the state space for the `StrongCP_ObservableBundle`.

### 2.2 Downstream problems

These problems directly reuse components from Q023 or treat Q023 as a prerequisite.

* Q025 (BH_PHYS_BARYON_ASYM_L3_025)
  Reason: Reuses `CP_TensionWorld_Template` to structure CP phase budgets in baryogenesis scenarios and uses `Tension_CP` as a constraint on allowed strong sector contributions.

* Q028 (BH_PHYS_QCD_CONFINEMENT_L3_028)
  Reason: Reuses `StrongCP_ObservableBundle` to classify which confinement and vacuum structures remain compatible with small `theta_eff` and EDM bounds.

* Q021 (BH_PHYS_QG_L3_021)
  Reason: Reuses `ThetaTensionFunctional` and `StrongCP_ObservableBundle` when embedding QCD into candidate quantum gravity or grand unification models, and propagates `Tension_CP` up to ultraviolet structures.

### 2.3 Parallel problems

Parallel nodes share similar tension types but do not directly reuse Q023 components.

* Q022 (BH_PHYS_HIERARCHY_L3_022)
  Reason: Both Q022 and Q023 encode small dimensionless parameters as naturalness tension problems using tuning indices analogous to `ThetaTensionFunctional`.

* Q024 (BH_PHYS_NEUTRINO_MASS_L3_024)
  Reason: Also features unusually small parameters and mixing phases; can reuse the conceptual pattern of consistency_tension without directly using `StrongCP_ObservableBundle`.

### 2.4 Cross domain edges

Cross domain edges connect Q023 to non QCD problems that reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses the idea behind `ThetaTensionFunctional` to quantify informational cost of fine tuning in general parameter spaces, viewing small `theta_eff` as a compressed support under a broader prior.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Uses `CP_TensionWorld_Template` as an analogy for interpreting internal AI parameters and phases as tuned versus untuned, with `Tension_CP` acting as a template for interpretability tension indices.

* Q010 (BH_COSM_COSMO_CONST_L3_010)
  Reason: Shares the same naturalness structure of an extremely small dimensionless number, and reuses the tuning index pattern introduced by `ThetaTensionFunctional` in a different physical context.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is strictly at the effective layer. We describe:

* the state space,
* observables and effective fields,
* tension related functionals,
* singular sets and domain restrictions,
* admissible encoding classes and fairness constraints.

We do not specify any deep TU generative rules or explicit mappings from raw microscopic data to internal TU fields.

### 3.1 State space

We assume a semantic state space

```txt
M
```

for Q023 with the following interpretation:

* Each `m` in `M` is a coherent strong CP world slice that includes:

  * an effective strong CP angle `theta_eff(m)` in the range `(-pi, pi]`,
  * a bundle of QCD and hadronic CP observables, including predicted neutron EDM and related EDMs,
  * meta information about the theoretical mapping used between microscopic parameters and those observables.

We do not specify how `m` is constructed from the fundamental QCD Lagrangian or ultraviolet completions. We only assume that for any consistent choice of microscopic parameters and effective theory, there is at least one state `m` that accurately encodes the corresponding effective observables.

### 3.2 Effective fields and observables

We introduce the following effective observables and fields on `M`.

1. Effective strong CP angle

   ```txt
   theta_eff(m) in (-pi, pi]
   ```

   * `theta_eff(m)` is the net physical strong CP angle for state `m`, after including contributions from `theta_QCD` and quark mass phases.
   * It is treated as a well defined real number modulo `2 pi` for all `m` in the regular domain.

2. EDM observable bundle

   ```txt
   O_EDM(m) = { d_n(m), d_p(m), d_nuc(m), d_atom(m), ... }
   ```

   * A finite bundle of predicted electric dipole moments for neutron, proton, selected nuclei, and atoms that are dominantly sensitive to strong CP effects.
   * Each element in the bundle is a real number with consistent units, derived from the effective theory used in `m`.

3. Experimental EDM bounds

   ```txt
   B_EDM = { d_n_bound, d_p_bound, d_nuc_bound, d_atom_bound, ... }
   ```

   * A set of externally fixed positive numbers representing current experimental upper bounds on the magnitudes of the corresponding EDM observables.
   * These bounds are treated as inputs to the encoding, not as derived quantities.

4. Prior model index for theta

   ```txt
   p_theta(m) in L_ref_theta
   ```

   * An index selecting one prior model from a finite or effectively enumerable library `L_ref_theta` of a priori distributions for `theta_eff`.

   * Elements of `L_ref_theta` might include:

     * a uniform distribution over `(-pi, pi]`,
     * distributions symmetric around zero with different widths,
     * other simple analytic families.

   * The library `L_ref_theta` is assumed to be fixed in advance and independent of the actual measured EDM bounds. The choice of `L_ref_theta` for this page is summarized at the effective layer by `LibraryKey_ref_Q023` in the header.

5. Naturalness mismatch for theta

   ```txt
   DeltaS_theta(m) >= 0
   ```

   * Measures how atypical the value `theta_eff(m)` is under the prior model indexed by `p_theta(m)`.

   * A simple example form is:

     ```txt
     DeltaS_theta(m) = - log_prior_theta(theta_eff(m) ; p_theta(m)) + c_theta
     ```

     where `c_theta` is chosen so that typical values under the prior give mismatch of order 1, and the logarithm base is fixed once and for all.

   * In all cases, `DeltaS_theta(m)` is nonnegative and finite for `m` in the regular domain.

6. EDM mismatch

   ```txt
   DeltaS_EDM(m) >= 0
   ```

   * Measures how close the predicted EDMs `O_EDM(m)` are to saturating the experimental bounds `B_EDM`.

   * A simple example is:

     ```txt
     DeltaS_EDM(m) = max over observables o in O_EDM(m) of f_EDM( |o| / bound_o )
     ```

     where `f_EDM` is a nondecreasing function with `f_EDM(1) = 1` and `f_EDM(x)` growing for `x > 1` or near saturation.

   * If all `|o|` are well below their bounds, `DeltaS_EDM(m)` is small; if any observable approaches or exceeds its bound, `DeltaS_EDM(m)` increases.

7. Combined strong CP mismatch

   We define the combined mismatch functional

   ```txt
   DeltaS_CP(m) = w_theta * DeltaS_theta(m) + w_EDM * DeltaS_EDM(m)
   ```

   where:

   * `w_theta` and `w_EDM` are nonnegative weights satisfying

     ```txt
     w_theta + w_EDM = 1
     ```

   * the pair `(w_theta, w_EDM)` is selected from a finite or effectively enumerable library of admissible weight choices `L_w_CP` that is fixed in advance and not tuned using the actual EDM data.

   The specific library used in this page is summarized at the effective layer by `WeightKey_Q023` in the header.

### 3.3 Effective tension tensor components

We adopt a TU consistent form for the effective tension tensor over `M`:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_CP(m) * lambda(m) * kappa_CP
```

where:

* `S_i(m)` is a source factor describing how strongly the ith semantic or physical source component participates in strong CP related reasoning in state `m`.
* `C_j(m)` is a receptivity factor describing how sensitive the jth cognitive or downstream component is to strong CP tension.
* `DeltaS_CP(m)` is the combined strong CP mismatch defined above.
* `lambda(m)` is a convergence state factor shared with other TU encodings, indicating whether local reasoning around `m` is convergent, recursive, divergent, or chaotic.
* `kappa_CP` is a coupling constant that sets the overall scale of strong CP related tension for this problem.

We do not need to specify the full index sets of `i` and `j`. It is sufficient that for all `m` in the regular domain, all relevant components `T_ij(m)` are finite and well defined.

### 3.4 Invariants and effective constraints

We define the following effective invariants to summarize strong CP tension patterns.

1. Theta naturalness index

   ```txt
   I_theta(m) = DeltaS_theta(m)
   ```

   A single nonnegative scalar summarizing how tuned `theta_eff(m)` is under the chosen prior.

2. EDM saturation index

   ```txt
   I_EDM(m) = DeltaS_EDM(m)
   ```

   Captures how close the predicted EDMs are to saturating or exceeding experimental bounds.

3. Global strong CP tension

   ```txt
   Tension_CP(m) = DeltaS_CP(m)
   ```

   Aggregates these two aspects into a single scalar index.

   For typical world like states `m_true` that accurately encode our universe, we expect:

   * `Tension_CP(m_true)` to be small if a structural resolution of the strong CP problem exists within the admissible encoding class.
   * `Tension_CP(m_true)` to be bounded away from zero if the smallness of `theta_eff` is due only to tuning.

We will use `Tension_CP(m)` as the primary tension functional in Block 4.

### 3.5 Singular set and domain restrictions

Some observables or mismatch measures may be undefined or divergent for certain encodings. We define the singular set

```txt
S_sing = {
  m in M :
  theta_eff(m) is undefined or not finite
  or any element of O_EDM(m) is undefined or not finite
  or DeltaS_theta(m) or DeltaS_EDM(m) is undefined or not finite
}
```

We choose the following treatment:

* The domain of strong CP tension analysis is restricted to the regular set

  ```txt
  M_reg = M \ S_sing
  ```

* Whenever an experiment or protocol would require evaluating `Tension_CP(m)` for a state in `S_sing`, the result is treated as out of domain and does not contribute numerical tension values.

* For modeling tasks that approximate integrals over `M`, we interpret integrals as restricted to `M_reg`, and we require any regularization schemes to keep `DeltaS_theta` and `DeltaS_EDM` finite for states counted as regular.

This choice preserves measurability of `Tension_CP` and its invariants at the effective layer, and it separates breakdowns of the encoding itself from genuine physical tension.

### 3.6 Admissible encoding class and fairness constraints

We now collect the admissible encoding class and fairness assumptions in one place.

* Let `A_enc_strongCP` denote the class of admissible strong CP encodings used in this page. Each element of `A_enc_strongCP` consists of:

  * a mapping from microscopic parameters and effective theories to states `m` in `M`,
  * a choice of prior models from `L_ref_theta`,
  * a choice of weight pairs from `L_w_CP`,
  * mapping kernels from microscopic parameters to EDM predictions `O_EDM(m)`.

* All encodings in `A_enc_strongCP` must satisfy:

  * states that are used for tension evaluation lie in `M_reg`,
  * `theta_eff(m)`, `O_EDM(m)`, `DeltaS_theta(m)`, and `DeltaS_EDM(m)` are finite on `M_reg`,
  * priors over `theta_eff` are selected from the fixed library `L_ref_theta` summarized by `LibraryKey_ref_Q023`,
  * weight pairs `(w_theta, w_EDM)` are selected from the fixed library `L_w_CP` summarized by `WeightKey_Q023`.

* Fairness constraints:

  * Libraries `L_ref_theta` and `L_w_CP` are fixed before looking at the EDM data that will later be used to evaluate tension.
  * Thresholds such as `T_threshold` in experiments are pre announced and not adjusted to fit the data.
  * Priors, weights, and mapping kernels are not retuned in a post hoc way that depends on the observed smallness of `theta_eff` or on updated EDM bounds.
  * Any future extensions or refinements of `A_enc_strongCP` must document changes to these libraries and thresholds as versioned updates to the effective layer encoding key `EncodingKey_Q023`.

These constraints ensure that claims about low or high `Tension_CP` are not artifacts of hidden fine tuning in the encoding itself.

---

## 4. Tension principle for this problem

This block states how Q023 is characterized as a tension problem within TU, using the observables and functionals defined in Block 3.

### 4.1 Core tension functional

We treat

```txt
Tension_CP(m) = DeltaS_CP(m)
```

as the core strong CP tension functional, with the following properties:

* `Tension_CP(m) >= 0` for all `m` in `M_reg`.

* `Tension_CP(m)` is small when:

  * `theta_eff(m)` is typical under the chosen prior in `L_ref_theta`,
  * predicted EDMs are comfortably below their bounds.

* `Tension_CP(m)` grows when:

  * `theta_eff(m)` lies in a highly atypical region under the chosen prior,
  * or EDM predictions approach or exceed their experimental bounds.

We restrict to weight pairs `(w_theta, w_EDM)` from `L_w_CP` and to prior models from `L_ref_theta` that are selected before evaluating real world data, preserving fairness.

In this sense, Q023 is a consistency_tension problem because it measures how consistent the realized small `theta_eff` and associated EDM bounds are with simple prior expectations and mapping assumptions.

### 4.2 Strong CP as a low tension principle

At the effective layer, a structural resolution of the strong CP problem can be expressed as the existence of low tension world like states within the admissible encoding class `A_enc_strongCP`:

> There exist states `m_T` in `M_reg` that faithfully represent our universe and belong to an encoding in `A_enc_strongCP` such that `Tension_CP(m_T)` remains within a low band across refinements.

More concretely:

* For any fixed choice of:

  * prior model `p_theta` from `L_ref_theta`,
  * weight pair `(w_theta, w_EDM)` from `L_w_CP`,
  * and other modeling details within `A_enc_strongCP`,

  there should exist world like states `m_T` such that

  ```txt
  Tension_CP(m_T) <= epsilon_CP
  ```

  where `epsilon_CP` is a small, nonnegative threshold that does not grow without bound as:

  * EDM measurements become more precise, or
  * theoretical mappings between `theta_eff` and observables are refined.

* Structural mechanisms, such as effective symmetries or alignment conditions, manifest at the effective layer as additional constraints on `M_reg` and on `A_enc_strongCP` that make small `theta_eff` a generic outcome rather than a tuned exception.

### 4.3 Persistent tuning as high tension

Conversely, if the strong CP problem is not structurally resolved within `A_enc_strongCP`, then world like states will exhibit persistent high tension:

> For all encoding choices in `A_enc_strongCP` that remain faithful to observed data, any state `m_F` representing our universe has `Tension_CP(m_F)` bounded away from zero by a positive constant.

Formally, there exists `delta_CP > 0` such that:

```txt
Tension_CP(m_F) >= delta_CP
```

for all world like states `m_F` in `M_reg` that encode current and future EDM constraints, within the admissible encoding class.

In this case:

* The smallness of `theta_eff` appears as a tuned coincidence with respect to the prior models in `L_ref_theta`.
* Improving EDM bounds or theoretical mappings tends to sharpen the tension rather than relieve it.

The strong CP problem, in TU terms, is therefore the question of whether the universe belongs to a low tension structural world or a high tension tuned world, within `A_enc_strongCP`.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds at the effective layer, using only observables and tension patterns without committing to specific microscopic mechanisms.

### 5.1 World T_CP (structural resolution, low tension)

In World T_CP:

1. Structural explanation

   * The admissible encoding class `A_enc_strongCP` contains additional structural relations, for example effective symmetries or alignment conditions, that generically drive `theta_eff` close to zero.
   * These relations imply that most world like states `m_T` in `M_reg` have small `theta_eff(m_T)` without tuning.

2. Prior compatibility

   * Under typical prior models in `L_ref_theta`, the values of `theta_eff(m_T)` that arise in `M_reg` are not statistically extreme.
   * `DeltaS_theta(m_T)` remains of order 1 or less as refinements of the encoding are introduced.

3. EDM alignment

   * Predicted EDMs derived from `m_T` remain comfortably below the experimental bounds `B_EDM`.
   * `DeltaS_EDM(m_T)` remains small and does not approach large values as bounds improve.

4. Global tension behavior

   * For all world like states `m_T` in `M_reg` consistent with World T_CP, the tension satisfies

     ```txt
     Tension_CP(m_T) <= epsilon_CP
     ```

     for some small `epsilon_CP` that is stable under reasonable refinements in data and modeling assumptions.

### 5.2 World F_CP (no structural resolution, persistent tuning)

In World F_CP:

1. No structural suppression

   * Within `A_enc_strongCP`, there is no structural relation that enforces small `theta_eff`.
   * The prior models in `L_ref_theta` treat values of order 1 and values near zero as comparably allowed before seeing EDM data.

2. Atypical theta

   * The states `m_F` in `M_reg` that faithfully reflect our universe have `theta_eff(m_F)` lying in a highly atypical region under the chosen prior.
   * `DeltaS_theta(m_F)` is large and does not decrease as the encoding is refined.

3. EDM bound pressure

   * Predicted EDMs are near the experimental bounds in a way that appears accidental rather than structurally enforced.
   * As EDM bounds improve, the mismatch `DeltaS_EDM(m_F)` tends to grow.

4. Global tension behavior

   * For world like states `m_F` consistent with World F_CP, there exists `delta_CP > 0` such that

     ```txt
     Tension_CP(m_F) >= delta_CP
     ```

     and this lower bound cannot be removed by any refinement within `A_enc_strongCP` that remains faithful to the data.

### 5.3 Interpretive note

These worlds are not claims about which mechanism is realized in nature. They are effective layer descriptions of two distinct patterns:

* a world where small `theta_eff` is structurally generic and low tension,
* a world where small `theta_eff` is tuned and high tension.

The purpose of Q023 is to make these patterns explicit and measurable in the TU framework, not to decide between them.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can test and constrain the Q023 encoding. They can falsify particular choices of priors, weights, and mapping details in `A_enc_strongCP`, but they do not prove or disprove the canonical strong CP statement.

### Experiment 1: Global strong CP tension fit from EDM data

Goal:

* Test whether a specific Q023 encoding, including chosen `L_ref_theta`, `L_w_CP`, and EDM mismatch mapping, can describe current and future EDM data without unstable retuning and without producing unacceptably large `Tension_CP` for world like states.

Setup:

* Input data:

  * Current experimental upper bounds on neutron EDM and other EDMs sensitive to strong CP.
  * Any future improved bounds that are available.
* Encoding choices:

  * Fix a finite subset of prior models `L_ref_theta_used` from `L_ref_theta`.
  * Fix a finite subset of weight pairs `L_w_CP_used` from `L_w_CP`.
  * Fix a mapping from QCD and CP parameters to EDM predictions, consistent with one or more effective theories, for example chiral effective models, but expressed only at the level of observables.
* State construction:

  * For each combination of prior model, weight pair, and effective theory, construct at least one state `m_data` in `M` that encodes:

    * the chosen prior,
    * the observed EDM bounds,
    * and the mapping from parameters to predicted observables.

Protocol:

1. For each candidate state `m_data`:

   * First check whether `m_data` lies in `S_sing`. If yes, discard it as out of domain.
   * If `m_data` lies in `M_reg`, compute `DeltaS_theta(m_data)` using the chosen prior model and `theta_eff(m_data)` consistent with EDM bounds.
2. For each regular `m_data`, compute `DeltaS_EDM(m_data)` from the predicted EDMs and their bounds.
3. Compute `Tension_CP(m_data)` as defined in Block 3 for each regular state.
4. Record the set of `Tension_CP(m_data)` values over all combinations in `L_ref_theta_used` and `L_w_CP_used`.
5. When new EDM bounds are released, update the bundle `B_EDM`, reconstruct the corresponding `m_data_new` states, discard any that fall in `S_sing`, and recompute `Tension_CP(m_data_new)` without changing the prior models or weight pairs.

Metrics:

* `T_max_current`: maximum `Tension_CP` observed among current regular `m_data`.
* `T_max_future`: maximum `Tension_CP` observed after incorporating future bounds, with the same priors and weights.
* Stability indicators:

  * whether `T_max_current` and `T_max_future` remain in a similar range,
  * whether small changes in the encoding produce large, unexplained shifts in `Tension_CP`.

Falsification conditions:

The Q023 encoding under test is considered falsified at the effective layer if any of the following occurs:

1. For all plausible combinations of priors and weights in `L_ref_theta_used` and `L_w_CP_used`, one finds

   ```txt
   Tension_CP(m_data) > T_threshold
   ```

   for regular `m_data`, where `T_threshold` is a pre announced upper bound for acceptable tension in a structurally resolved strong CP scenario.

2. Incorporating updated experimental bounds requires ad hoc changes to priors or weight libraries in order to keep `Tension_CP` below `T_threshold`. In that case, the encoding is judged unstable and rejected.

These conditions do not rule out the strong CP problem itself; they only rule out particular Q023 encodings as adequate models of a low tension world.

Semantics implementation note:

* All quantities in this experiment are treated as continuous fields, consistent with the metadata semantics.
* We work with real valued observables and mismatch scores over the regular domain `M_reg` and avoid introducing discrete or hybrid semantics in this block.

Boundary note:

* Falsifying a TU encoding in this sense does not solve the canonical strong CP statement.
* This experiment can reject specific choices of priors, weights, and mappings in `A_enc_strongCP`, but it does not solve the strong CP problem or prove that any given mechanism is realized.

---

### Experiment 2: Model world comparison of strong CP resolutions

Goal:

* Assess whether the Q023 tension encoding can distinguish, at the effective layer, between different classes of proposed strong CP resolutions by their predicted tension patterns, without committing to which one is realized.

Setup:

* Define a model class of candidate resolutions, for example:

  * Class S: scenarios with structural suppression of `theta_eff` (symmetry like or alignment like).
  * Class T: scenarios with no structural suppression, where small `theta_eff` arises from tuning.
* For each model in Class S and Class T:

  * Construct a state `m_S` or `m_T` in `M` encoding its predictions for `theta_eff` and EDM observables at a chosen resolution.
  * Ensure that states used in the analysis lie in `M_reg` by excluding any that fall in `S_sing`.
  * Use the same finite libraries `L_ref_theta` and `L_w_CP` as in Experiment 1.

Protocol:

1. For each regular `m_S` and `m_T` in `M_reg`, compute `DeltaS_theta`, `DeltaS_EDM`, and `Tension_CP`.
2. Aggregate the resulting tension values into two distributions:

   * `D_S` for Class S,
   * `D_T` for Class T.
3. Optionally, refine the encoding by improving mappings from microscopic parameters to EDM observables, keeping the fairness constraints intact, then repeat the calculations.

Metrics:

* Mean and variance of `Tension_CP` in `D_S` and `D_T`.
* A simple separation metric, for example:

  * `Delta_mean = mean(D_T) - mean(D_S)`,
  * the fraction of models where `Tension_CP` in Class S is below a low threshold while Class T is above a higher threshold.

Falsification conditions:

The Q023 encoding under test is considered inadequate for discriminating strong CP resolutions if:

1. The distributions `D_S` and `D_T` substantially overlap even when the underlying model classes are constructed to be structurally different in how they suppress or tune `theta_eff`.
2. For all reasonable choices in `L_ref_theta` and `L_w_CP`, it remains impossible to achieve a regime where:

   * Class S models concentrate at low `Tension_CP`,
   * Class T models concentrate at higher `Tension_CP`.

In that case, the encoding may be considered too blunt or misaligned, and it should be refined or replaced.

Semantics implementation note:

* All model world observables and mismatch scores are treated as continuous quantities.
* We stay within the same continuous semantics as specified in the metadata and interpret all tension indices as real valued functions on `M_reg`.

Boundary note:

* Falsifying a TU encoding in this experiment does not solve the canonical strong CP statement.
* This experiment can show that a particular encoding fails to distinguish classes of strong CP resolutions, but it does not decide which, if any, of those resolutions is true in our universe.

A more quantitative separation target or numeric threshold for `D_S` and `D_T` may be specified in future E2 upgrades of this page. In this E1 version, it is enough to demand a robust ordering where typical Class S models occupy lower tension regions than typical Class T models, under stable choices from `L_ref_theta` and `L_w_CP`.

---

## 7. AI and WFGY engineering spec

This block describes how Q023 can be used to build and evaluate AI systems within the WFGY framework at the effective layer.

### 7.1 Training signals

We define several training signals derived from strong CP observables and tension indices.

1. `signal_theta_naturalness`

   * Definition: proportional to `DeltaS_theta(m)` for states associated with reasoning about `theta_eff`.
   * Use: penalize internal reasoning states that treat extremely small `theta_eff` as if it were a generic, untuned value under a simple prior.

2. `signal_EDM_consistency`

   * Definition: proportional to `DeltaS_EDM(m)` for states where neutron EDM and related bounds are in play.
   * Use: encourage the model to respect known EDM limits; penalize answers that imply predictions far above established bounds in contexts that explicitly assume current experimental constraints.

3. `signal_CP_tension_index`

   * Definition: set equal to `Tension_CP(m)` for the current reasoning state.
   * Use: act as a scalar diagnostic or auxiliary loss that monitors how tuned a scenario appears, given the chosen priors and mappings.

4. `signal_world_switch_consistency`

   * Definition: measures the difference between the model’s internal representations and outputs when reasoning under World T_CP assumptions versus World F_CP assumptions.
   * Use: encourage clean separation of assumptions; the model should not mix low tension and high tension worlds in a single answer.

These signals are auxiliary controls on internal representations. They are not physical measurements and they do not by themselves yield any conclusion about which strong CP mechanism is realized in the actual universe.

### 7.2 Architectural patterns

We outline module patterns that reuse Q023 components without exposing any deep TU generative rules.

1. `ThetaTensionHead`

   * Role: given an internal representation of a QCD or CP related context, produce an estimate of `Tension_CP(m)` and its decomposition into `DeltaS_theta` and `DeltaS_EDM`.
   * Interface:

     * Inputs: internal embeddings from the base model corresponding to strong CP related text or tasks.
     * Outputs: scalar tension estimate and a small vector describing components `(DeltaS_theta, DeltaS_EDM)`.

2. `CPConstraintFilter`

   * Role: act as a filter that checks proposed parameter values or qualitative statements about `theta_eff` and EDMs against known bounds and priors.
   * Interface:

     * Inputs: candidate parameter descriptions and associated internal states.
     * Outputs: scores or masks indicating how compatible each candidate is with low `Tension_CP`.

3. `CP_TensionWorld_Interpreter`

   * Role: provide an interface for switching between World T_CP and World F_CP assumptions during reasoning.
   * Interface:

     * Inputs: a world label (T_CP or F_CP) and context embeddings.
     * Outputs: adjusted internal states that reflect the corresponding tension profile while keeping the base content fixed.

All these modules are internal to the AI system. They are diagnostic and steering tools for reasoning patterns, not physical models of QCD or strong CP dynamics.

### 7.3 Evaluation harness

We propose an evaluation harness to test the impact of Q023 modules on AI reasoning.

1. Task set

   * A small benchmark of qualitative and semi quantitative questions about:

     * the definition of the strong CP problem,
     * reasons why `theta_eff` is expected to be small or large under different assumptions,
     * comparisons of proposed resolutions, for example symmetry based versus tuned scenarios.

2. Conditions

   * Baseline condition:

     * The model answers questions using its default reasoning capabilities, without explicit Q023 modules.
   * TU enhanced condition:

     * The model routes relevant contexts through `ThetaTensionHead`, `CPConstraintFilter`, and `CP_TensionWorld_Interpreter`.

3. Metrics

   * Conceptual coherence:

     * Are explanations of the strong CP problem internally consistent?
     * Does the model clearly distinguish between structural explanations and fine tuning?
   * Assumption awareness:

     * When asked to switch between assume a structural resolution exists and assume there is no structural resolution, does the model change its reasoning in a controlled way?
   * Stability:

     * Does the presence of Q023 modules reduce contradictory statements about `theta_eff` and EDM bounds across a set of related questions?

### 7.4 60 second reproduction protocol

A minimal protocol to let users experience how Q023 changes AI explanations.

Baseline setup:

* Prompt the AI:

  ```txt
  Explain what the strong CP problem is, why it is puzzling, and briefly describe one proposed solution.
  ```

* Record the answer and note whether:

  * the definition is accurate,
  * the role of `theta_eff` and EDM bounds is clear,
  * structural versus tuned explanations are distinguished.

TU encoded setup:

* Prompt the AI:

  ```txt
  Explain the strong CP problem using the idea of a prior over theta_eff and a tension measure between allowed CP phases and experimental EDM bounds. Then compare a world where this tension is structurally small and a world where it is large.
  ```

* Ensure that `ThetaTensionHead` and `CPConstraintFilter` are active during this interaction.

* Record the answer and the internal `Tension_CP` estimates.

Comparison metric:

* Evaluate whether the TU encoded answer:

  * is more explicit about why `theta_eff` should generically be order 1 under a simple prior,
  * clearly ties the smallness of `theta_eff` to EDM bounds,
  * cleanly separates structural and tuned worlds.

What to log:

* Prompts and outputs for both baseline and TU runs.
* Internal tension estimates and mismatch components where available.

These logs allow later inspection and comparison of reasoning patterns without exposing any deep TU generative rules and without treating the AI tension indices as physical measurements.

---

## 8. Cross problem transfer template

This block records the reusable components produced by Q023 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `ThetaTensionFunctional`

   * Type: functional

   * Minimal interface:

     * Inputs: `theta_prior_model`, `theta_eff_value`.
     * Output: `tuning_index` (a nonnegative scalar summarizing how tuned `theta_eff_value` is under the prior).

   * Preconditions:

     * `theta_prior_model` must belong to `L_ref_theta`.
     * The prior must be chosen without using the EDM data that will later be used to evaluate tension.

2. ComponentName: `StrongCP_ObservableBundle`

   * Type: field

   * Minimal interface:

     * Inputs: a descriptor of a strong interaction context, for example which QCD effective theory and energy scale are used.
     * Output: a bundle of observables `{theta_eff, O_EDM}` suitable for use in tension calculations.

   * Preconditions:

     * The context descriptor must specify enough information to compute or approximate `theta_eff` and the relevant EDMs.
     * Outputs must be finite for states in `M_reg`.

3. ComponentName: `CP_TensionWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a model class of strong CP scenarios, partitioned into structural resolution type and tuning type.
     * Output: a pair of experiment templates for World T_CP and World F_CP, each specifying:

       * which observables to track,
       * how to evaluate `Tension_CP`,
       * what thresholds define low and high tension regimes.

   * Preconditions:

     * The model class must allow construction of states in `M_reg` with well defined `theta_eff`, EDM observables, and mapping choices.

### 8.2 Direct reuse targets

1. Q022 (BH_PHYS_HIERARCHY_L3_022)

   * Reused component: `ThetaTensionFunctional`.
   * Why it transfers: the same tuning index structure can be applied to other small parameters, for example scalar masses or couplings, by replacing `theta_eff` with the parameter of interest and adjusting the prior library.
   * What changes: prior models become distributions over masses or couplings rather than angles, and observables change accordingly, but the consistency_tension pattern remains.
   * When reusing this component across problems, the prior library and thresholds must be re specified at the effective layer for each problem and must not be silently carried over from Q023.

2. Q025 (BH_PHYS_BARYON_ASYM_L3_025)

   * Reused component: `CP_TensionWorld_Template`.
   * Why it transfers: baryogenesis scenarios require sufficient CP violation while respecting constraints like small strong CP phases; the same template can structure worlds with different CP budgets.
   * What changes: the observables include baryon asymmetry indicators and CP violating rates, and `Tension_CP` becomes part of a broader CP tension index.

3. Q028 (BH_PHYS_QCD_CONFINEMENT_L3_028)

   * Reused component: `StrongCP_ObservableBundle`.
   * Why it transfers: classification of QCD vacuum and confinement scenarios must account for the presence or absence of strong CP violation; the observable bundle provides a standardized way to label them.
   * What changes: additional fields related to confinement order parameters and topological sector structure are added to the bundle.

---

## 9. TU roadmap and verification levels

This block summarizes the current verification levels for Q023 and outlines the next measurable steps.

### 9.1 Current levels

* E_level: E1

  * An effective layer encoding of the strong CP problem has been specified.
  * Observables, mismatch measures, tension functionals, and a singular set with domain restriction have been defined.
  * At least one experiment with explicit falsification conditions has been described.

* N_level: N1

  * The narrative linking priors over `theta_eff`, EDM bounds, and strong CP tension is explicit and coherent at the conceptual level.
  * Counterfactual worlds T_CP and F_CP are described in terms of tension patterns but are not yet tied to a detailed classification of all proposed mechanisms.

### 9.2 Next measurable step toward E2

To raise Q023 to E2, the following measurable steps are proposed:

1. Implement a concrete prototype that:

   * takes as input a set of prior models from `L_ref_theta` and EDM data,
   * constructs explicit states `m_data` in `M_reg`,
   * computes `DeltaS_theta`, `DeltaS_EDM`, and `Tension_CP` for those states,
   * and publishes the resulting tension profiles as open data.

2. Refine the admissible encoding class `A_enc_strongCP` by:

   * specifying a finite library of mapping kernels from microscopic parameters to EDM observables,
   * bounding how these kernels may change as theory improves, to preserve stable tension behavior.

Both steps remain within the effective layer because they operate on observables and mismatch measures without revealing any deep TU generative rules.

### 9.3 Long term role in the TU program

In the long term, Q023 is expected to:

* Serve as the canonical template for parameter naturalness problems in physics where small dimensionless numbers appear.
* Provide reusable components (`ThetaTensionFunctional`, `StrongCP_ObservableBundle`, and `CP_TensionWorld_Template`) that can be adapted to hierarchy, cosmological constant, and other tuning problems.
* Act as a benchmark for how far TU style encodings can structure reasoning around open naturalness puzzles without claiming solutions.

---

## 10. Elementary but precise explanation

The strong CP problem can be summarized as follows.

Quantum chromodynamics, our theory of the strong force, allows a certain kind of term that breaks CP symmetry. This term is controlled by an angle called `theta_eff`. There is no obvious reason in the basic equations why `theta_eff` should be tiny; a natural guess is that it could be anywhere between `-pi` and `pi`.

However, if `theta_eff` were not extremely small, we would expect to see strong CP violation in experiments. In particular, the neutron would have a measurable electric dipole moment. Experiments have looked for this and have not found it, which implies that `theta_eff` must be less than roughly one part in ten billion.

So the puzzle is:

```txt
Why is theta_eff so close to zero, when it did not have to be?
```

In the Tension Universe view, instead of jumping directly to a specific solution, we first make the tension precise.

1. We imagine a prior over `theta_eff`. For example, one simple prior is that all values between `-pi` and `pi` are equally likely.

2. We look at the actual bounds from neutron EDM and related experiments.

3. We define mismatch measures:

   * one that says how unusual our small `theta_eff` is under the prior,
   * one that says how close predicted EDMs are to the experimental limits.

4. We combine these into a single number called `Tension_CP`. This number is small if the situation looks natural, and large if it looks tuned.

Then we consider two types of worlds:

* In a structural resolution world, some deeper reason forces `theta_eff` to be tiny, so most consistent stories about the world have small `Tension_CP`.
* In a no resolution world, there is no deeper reason, and our tiny `theta_eff` is just a lucky accident; in that case, any story that matches experiments ends up with large `Tension_CP`.

Q023 does not claim to know which type of world we live in. Instead, it:

* sets up the observables and mismatch measures needed to talk about strong CP as a tension problem,
* defines experiments that can falsify specific encodings of this tension,
* and provides a template that can be reused for other naturalness puzzles in physics.

This effective layer description keeps the focus on what can be observed, measured, and quantified, while leaving deeper mechanisms open for further work.

---

## Tension Universe effective layer footer

This page is part of the WFGY / Tension Universe S problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the named problem, including observables, mismatch measures, tension indices, counterfactual worlds, and AI facing engineering patterns.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.
* For Q023 in particular, the strong CP tension functionals and AI modules defined here are diagnostic tools on effective summaries of `theta_eff` and EDM data. They are not physical mechanisms and they do not determine which strong CP resolution, if any, is realized in nature.

### Effective layer boundary

* All objects used here, including:

  * state spaces `M`,
  * observables such as `theta_eff(m)` and `O_EDM(m)`,
  * mismatch measures such as `DeltaS_theta(m)` and `DeltaS_EDM(m)`,
  * tension indices such as `Tension_CP(m)`,
  * counterfactual worlds `World T_CP` and `World F_CP`,
    live strictly at the effective layer of the TU framework.
* No axiom system, generative rule set, or microscopic TU ontology is exposed or assumed in this page.
* Mappings from microscopic theories to `M` are treated as black box encodings that must satisfy explicit regularity and fairness constraints; their internal details are outside the scope of this document.

### Encodings and fairness

* The admissible encoding class for this problem is denoted `A_enc_strongCP` and is summarized at the effective layer by:

  * `EncodingKey_Q023` for the encoding family,
  * `LibraryKey_ref_Q023` for prior and reference libraries,
  * `WeightKey_Q023` for admissible weight choices.
* All encodings in `A_enc_strongCP`:

  * restrict attention to the regular domain `M_reg = M \ S_sing`,
  * use prior models from `L_ref_theta` and weight pairs from `L_w_CP` that are fixed in advance,
  * obey fairness constraints that forbid post hoc retuning in response to EDM data,
  * document changes as versioned updates at the effective layer rather than silent internal modifications.
* Experiments in Section 6 are designed to falsify or refine encodings in `A_enc_strongCP` without changing the canonical strong CP statement itself.

### Cross problem reuse and versioning

* Components labeled as reusable, such as `ThetaTensionFunctional`, `StrongCP_ObservableBundle`, and `CP_TensionWorld_Template`, are patterns at the effective layer.
* When these components are reused in other problems, their priors, thresholds, and mapping details must be re specified and versioned for each problem. They must not be silently imported from Q023 in a way that would hide additional tuning.
* Updates to this page that change the behavior of encodings or experiments should:

  * increment the effective layer encoding key `EncodingKey_Q023`,
  * record the change in accompanying changelogs or external repositories where the code and data live.

### TU charters

This page is governed by the following Tension Universe charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
