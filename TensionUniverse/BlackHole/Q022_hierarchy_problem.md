<!-- QUESTION_ID: TU-Q022 -->
# Q022 · Hierarchy problem

## 0. Header metadata

```txt
ID: Q022
Code: BH_PHYS_HIERARCHY_L3_022
Domain: Physics
Family: High energy theory
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: spectral_tension
Status: Open
Semantics: continuous
E_level: E1
N_level: N2
Last_updated: 2026-01-30

EncodingKey_Q022: TU_HIER_Encoding_v1
LibraryKey_ref_Q022: TU_HIER_RefModels_v1
WeightKey_Q022: TU_HIER_Weights_v1
````

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* We only specify state spaces, observables, invariants, tension scores, counterfactual worlds, and engineering patterns.
* We do **not** specify any deep TU generative rules, axioms, microscopic ontology, or construction procedures that would generate these objects from first principles.
* Any mapping from experimental data or microscopic models into the effective state spaces used here is treated as an **external choice**, not fixed by this document.
* This page does **not** claim to solve the hierarchy problem, does **not** claim that any specific ultraviolet mechanism is realized in nature, and does **not** provide a proof of any new theorem in high energy physics.
* All spectral_tension quantities defined here are **diagnostic functionals** on effective observables. They express how mass and scale spectra compare with a pre committed reference library. They must not be read as evidence that the underlying spectra are uniquely determined by TU.

The role of this page is to define a **transparent effective layer encoding** of the hierarchy problem that external readers can inspect, test, and reuse, while the deep TU level remains hidden.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The hierarchy problem asks why the characteristic electroweak scale is so small compared with a natural ultraviolet reference scale such as the Planck scale or a grand unification scale.

At the level of effective field theory, consider

```txt
m_weak  ~  10^2 GeV
M_UV    ~  10^16 to 10^19 GeV
```

Radiative corrections to the Higgs mass parameter are generically of order `M_UV^2`, so the renormalized value of the Higgs mass squared at low energy receives contributions

```txt
m_H^2(ren)  =  m_H^2(bare)  +  c * M_UV^2  +  loop_terms(masses, couplings)
```

with `c` a dimensionless coefficient that is not forced to vanish by any manifest symmetry in the minimal Standard Model.

Unless there is a protective structure, the observed small value of `m_weak` requires extremely delicate cancellations between the bare parameter and the loop corrections. The hierarchy problem is the question

```txt
Why is m_weak << M_UV in a way that does not look like arbitrary fine tuning?
```

Equivalently, why is the ratio

```txt
r_scale  =  M_UV / m_weak
```

so large, yet realized in a way that might be explained by symmetries, dynamics, or selection effects rather than unexplained parameter adjustment.

### 1.2 Status and difficulty

The hierarchy problem is not a single formal conjecture. It is a cluster of related questions about naturalness, radiative stability, and ultraviolet completion.

* In the minimal Standard Model treated as an effective field theory with a high cutoff, the Higgs mass parameter is unstable under radiative corrections.

* Many proposed frameworks aim to address this instability, including

  * low scale supersymmetry,
  * composite or pseudo Nambu Goldstone Higgs models,
  * extra dimensional models with warped or large geometries,
  * frameworks based on environmental or anthropic selection in a larger landscape.

* Experimental constraints from colliders and precision tests have put strong pressure on some of the simplest realizations, especially those predicting light superpartners or strongly coupled new states near the TeV scale.

There is no consensus solution. The problem is deeply entangled with questions about

* the correct ultraviolet completion of the Standard Model,
* the structure of quantum gravity,
* the role of naturalness as a guiding principle in fundamental physics.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q022 has three main roles.

1. It is the principal node for **scale separation tension** between low energy physics and an ultraviolet completion, expressed as a spectral_tension on mass and coupling spectra.
2. It provides a template for other naturalness problems such as strong CP (Q023) and cosmological constant tension problems (Q027).
3. It tests whether TU encodings can express, at the effective layer

   * the relation between radiative corrections and observed scales,
   * a quantitative notion of fine tuning,
   * counterfactual worlds in which scale separation is realized in more or less natural ways.

This document uses only standard effective field theory language in Section 1 and applies TU structures strictly in later sections.

### References

1. G. F. Giudice, “Naturally Speaking: The Naturalness Criterion and Physics at the LHC”, in *Perspectives on LHC Physics*, World Scientific, 2008.
2. J. Polchinski, *Effective Field Theory and the Fermi Surface*, in *Recent Directions in Particle Theory*, Proceedings of TASI 1992, World Scientific, 1993.
3. M. Dine, *Supersymmetry and String Theory: Beyond the Standard Model*, Cambridge University Press, 2007.
4. Standard encyclopedia entry on “Hierarchy problem (physics)”, including its relation to the Higgs mass, naturalness, and candidate solutions.

---

## 2. Position in the BlackHole graph

This block records how Q022 sits inside the BlackHole graph among Q001 to Q125.

### 2.1 Upstream problems

These problems provide conceptual and technical prerequisites at the effective layer.

* Q021 (BH_PHYS_QG_L3_021)

  Reason: Supplies candidate quantum gravity and ultraviolet completion frameworks that define the high scale `M_UV` and the classes of couplings relevant for radiative corrections.

* Q032 (BH_PHYS_QTHERMO_L3_032)

  Reason: Provides a general framework for viewing quantum fields, vacuum structure, and energy densities as thermodynamic like objects, which is reused when defining effective energy scales and their stability.

### 2.2 Downstream problems

These problems reuse Q022 components or depend on the hierarchy tension structure.

* Q023 (BH_PHYS_STRONG_CP_L3_023)

  Reason: Reuses naturalness style tension functionals to quantify the fine tuning of the QCD theta angle.

* Q024 (BH_PHYS_NEUTRINO_MASS_L3_024)

  Reason: Uses scale separation and naturalness observables to analyze why neutrino masses are tiny compared with charged lepton masses.

* Q027 (BH_PHYS_CC_NATURALNESS_L3_027)

  Reason: Extends the notion of hierarchy tension to vacuum energy and the cosmological constant problem.

### 2.3 Parallel problems

These problems share similar scale separation or naturalness tension types without direct component reuse.

* Q026 (BH_PHYS_MEASUREMENT_L3_026)

  Reason: Both Q022 and Q026 concern apparently unnatural parameter or process selections that are not directly enforced by obvious symmetries.

* Q031 (BH_PHYS_EARLY_UNIVERSE_L3_031)

  Reason: Early universe scenarios often require finely tuned parameters. Q031 and Q022 share similar tension patterns regarding parameter stability.

From the metadata viewpoint, Q021 and Q022 are parallel in using **spectral_tension**. Q022 focuses on mass and scale spectra. Q021 focuses on spectra of regimes in spacetime.

### 2.4 Cross domain edges

Cross domain edges connect Q022 to problems in other domains that reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)

  Reason: Reuses scale separation descriptors to relate computational resources at different hardware scales to physical energy costs.

* Q123 (BH_AI_INTERP_L3_123)

  Reason: Applies hierarchy tension descriptors to internal AI representations, asking whether different layers or modules show unnatural scale separations in their learned quantities.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We describe

* state space,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any rule that constructs internal TU fields from raw experimental or microscopic data.

### 3.1 State space

We assume a semantic state space

```txt
M
```

with the following interpretation.

Each element `m` in `M` represents a coherent effective description of a fundamental physics model that includes

* a low energy electroweak scale,
* at least one ultraviolet reference scale relevant to radiative corrections,
* the structure of relevant couplings and degrees of freedom that feed into the Higgs sector.

For each `m` we assume the following effective quantities are well defined.

1. Electroweak scale observable

```txt
m_weak(m)  >  0
```

An effective scalar summarizing the characteristic scale of electroweak symmetry breaking in the model encoded by `m`.

2. Ultraviolet reference scale observable

```txt
M_UV(m)  >  m_weak(m)
```

An effective scalar summarizing the highest physically relevant scale at which the effective field theory description is trusted before new physics must appear.

3. Scale ratio observable

```txt
r_scale(m)  =  M_UV(m) / m_weak(m)
```

A dimensionless indicator of the separation between the ultraviolet scale and the electroweak scale.

4. Naturalness cost observable

```txt
Delta_nat(m)  >=  0
```

An effective scalar summarizing how sensitively the low energy mass parameter depends on variations of the fundamental parameters at the ultraviolet scale. It can be thought of as a coarse version of derivatives like `partial m_weak^2 / partial p_i` aggregated over relevant microscopic parameters `p_i`. The exact microscopic definition is not needed at the effective layer, only that `Delta_nat(m)` is finite and nonnegative in the regular domain.

From the TU metadata viewpoint, the pair `r_scale(m)` and `Delta_nat(m)` encodes a **spectral_tension** on the mass and coupling spectrum. It records how distorted the effective eigenvalue and parameter pattern is relative to a reference library.

### 3.2 Reference library and admissible encodings

To avoid tuning after the fact, we introduce

1. A finite reference library of models

```txt
L_ref = { l_1, l_2, ..., l_K }
```

Each `l_k` is a model class selected before looking at any detailed data about the actual world. Examples include

* a minimal Standard Model with a fixed cutoff,
* a supersymmetric benchmark with a symmetry protecting the Higgs mass,
* a composite Higgs benchmark,
* a warped extra dimensional benchmark.

For each `l_k` the pair

```txt
(r_scale_ref(k), Delta_nat_ref(k))
```

is defined by the same effective observables as above, evaluated in that benchmark model.

2. An admissible encoding class

```txt
E_hier
```

is the set of encoding maps that assign to each candidate fundamental model a state `m` in `M` together with `m_weak(m)`, `M_UV(m)` and `Delta_nat(m)` such that

* these observables vary continuously with respect to small changes in the model parameters within a given class,
* they respect obvious symmetries of the model, for example gauge symmetries,
* none of their defining parameters are allowed to depend on the measured value of `m_weak` or `M_UV` for the particular world being considered.

In addition, for Q022 we require that

* the admissible encodings in `E_hier` form a **finite or effectively enumerable class**, identified by `EncodingKey_Q022`,
* all choices of thresholds, reference library entries, and weights that enter the definitions below are fixed by the triplet `(EncodingKey_Q022, LibraryKey_ref_Q022, WeightKey_Q022)` **before** evaluating any world data.

This prevents the encoding from being adjusted after seeing the world and makes the fairness constraints explicit.

### 3.3 Effective mismatch observables

Using the observables above and the library, we define two dimensionless mismatch observables.

1. Scale separation mismatch

```txt
H_scale(m)  =  max( 0 , r_scale(m) - r_scale_max ) / r_scale_max
```

where `r_scale_max` is a fixed positive constant chosen before examining the actual world, for example a number that distinguishes modest scale separations from extremely large ones. By construction

```txt
H_scale(m)  >=  0
```

and it becomes large when the scale ratio is far above the chosen reference band.

2. Naturalness mismatch

```txt
H_nat(m)  =  Delta_nat(m) / Delta_nat_ref_max
```

where `Delta_nat_ref_max` is a fixed positive constant defined using the library, for example

```txt
Delta_nat_ref_max  =  max over k of Delta_nat_ref(k)
```

for those reference models considered acceptably natural. Again,

```txt
H_nat(m)  >=  0
```

and it becomes large when the naturalness cost is much worse than in any of the reference models.

Both `r_scale_max` and `Delta_nat_ref_max` are chosen once and for all for this encoding, not adapted to match any particular world.

The pair `(H_scale(m), H_nat(m))` implements the **spectral_tension** mentioned in the header metadata. It quantifies how far the mass and coupling spectrum of a scenario deviates from a pre committed band of reference spectra.

### 3.4 Effective tension tensor components

Consistent with the TU core, we define an effective tension tensor on `M`:

```txt
T_ij(m)  =  S_i(m) * C_j(m) * H_total(m) * lambda(m) * kappa
```

where

* `S_i(m)` is a source factor summarizing how strongly the ith semantic channel depends on the Higgs sector and the ultraviolet scale,
* `C_j(m)` is a receptivity factor summarizing how sensitive the jth cognitive or downstream structure is to hierarchy tension,
* `H_total(m)` is a scalar hierarchy tension score defined below,
* `lambda(m)` is a convergence state factor in a fixed bounded interval,
* `kappa` is a fixed coupling constant that sets the overall scale.

The indices `i` and `j` label a finite collection of semantic channels and downstream uses. The precise identity of those channels is not required at the effective layer.

### 3.5 Invariants, hierarchy score, and singular set

We define a scalar hierarchy tension score

```txt
H_total(m)  =  g_scale * H_scale(m)  +  g_nat * H_nat(m)
```

with `g_scale > 0` and `g_nat > 0` fixed once and for all for the encoding and identified by `WeightKey_Q022`. This score satisfies

```txt
H_total(m)  >=  0
```

and grows when either scale separation or naturalness cost become large relative to their reference bands.

Singular configurations arise when the basic observables cease to be meaningful. We define a singular set

```txt
S_sing  =  {
  m in M :
  m_weak(m) <= 0          or
  M_UV(m)   <= m_weak(m)  or
  m_weak(m) or M_UV(m) not finite  or
  Delta_nat(m) not finite
}
```

The regular domain is

```txt
M_reg  =  M \ S_sing
```

All hierarchy tension analysis is restricted to `M_reg`. When an experiment or protocol would attempt to evaluate `H_total(m)` for `m` in `S_sing`, the result is treated as **out of domain** rather than as evidence about Q022.

---

## 4. Tension principle for this problem

This block states how Q022 is characterized as a tension problem inside TU.

### 4.1 Core hierarchy tension question

At the effective layer, Q022 is framed as the **question** whether the universe realizes electroweak symmetry breaking in a way that admits low hierarchy tension descriptions within the admissible encoding class.

More concretely, for an admissible encoding in `E_hier` with fixed parameters identified by `(EncodingKey_Q022, LibraryKey_ref_Q022, WeightKey_Q022)`, the low tension scenario is that there exist world representing states `m_world` in `M_reg` such that

```txt
H_total(m_world)  <=  epsilon_hier
```

for some small threshold `epsilon_hier` that does not grow without bound as we include more accurate information about the Higgs sector and the ultraviolet completion.

The high tension scenario is that any faithful encoding and world representing state compatible with observations is forced into persistent large `H_total`.

Q022, at the TU effective layer, does not assert which scenario is realized. It only provides the structure needed to pose and investigate this question.

### 4.2 Failure of the hierarchy principle inside a fixed encoding class

If every admissible encoding in `E_hier` that remains faithful to the observed particle spectrum and known constraints has the property that all world representing states satisfy

```txt
H_total(m_world)  >=  delta_hier
```

for some strictly positive `delta_hier` that cannot be removed by reasonable refinements within that encoding class, then the universe realizes electroweak symmetry breaking in a high tension regime relative to that class.

In that case the hierarchy problem is not resolved by symmetry or dynamics **within that encoding class** and must be addressed by changing the class, for example by allowing more radically different ultraviolet structures or selection effects.

The effective statement of Q022 can thus be read as

```txt
Is there an admissible encoding and model class in which world states
compatible with observations lie in a low hierarchy tension band,
or is every faithful encoding forced into persistent high H_total?
```

This is a statement about effective encodings, not a statement about the ultimate theory of nature.

---

## 5. Counterfactual tension worlds

We sketch two counterfactual worlds at the effective layer.

* World T: hierarchy tension is low because some protective mechanism or structural relation holds.
* World F: hierarchy tension is high because no such mechanism is present within the encoding class.

These worlds are specified relative to encodings in `E_hier`. They are not claims about the full space of logically possible theories.

### 5.1 World T (low hierarchy tension)

In World T

1. Protective mechanism

   There exists a structural reason in the model class, such as a symmetry, compositeness, or special geometric pattern, that controls radiative corrections to the Higgs sector. In the effective description this shows up as

   ```txt
   Delta_nat(m_T)  is comparable to or smaller than Delta_nat_ref_max
   ```

2. Controlled scale separation

   The scale ratio `r_scale(m_T)` can still be large, but the mismatch observable `H_scale(m_T)` is not extreme and can remain in a reference band compatible with the library.

3. Combined hierarchy tension

   For world states `m_T` that reflect the actual universe in World T we have

   ```txt
   H_total(m_T)  <=  epsilon_hier
   ```

   for a small `epsilon_hier` that is stable under data refinement and improved modeling.

### 5.2 World F (high hierarchy tension)

In World F

1. No effective protection

   Radiative corrections drive the Higgs parameter toward `M_UV` with no symmetry or dynamical alignment that keeps `m_weak` stable. The effective naturalness cost is large

   ```txt
   Delta_nat(m_F)  >>  Delta_nat_ref_max
   ```

   for every state `m_F` consistent with observed data and constraints.

2. Extreme scale separation

   The scale ratio `r_scale(m_F)` is large enough that `H_scale(m_F)` is significantly above its reference band.

3. Combined hierarchy tension

   The combined score satisfies

   ```txt
   H_total(m_F)  >=  delta_hier
   ```

   with `delta_hier > 0` that cannot be removed by any refinement of the encoding that remains faithful to observational facts.

### 5.3 Interpretive note

These counterfactual worlds are not claims about what the ultimate theory of nature is. They are effective scenarios about how hierarchy tension appears when the world is encoded through admissible maps in `E_hier`. They distinguish worlds where electroweak physics is structurally supported from worlds where it appears fine tuned.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that do not solve the hierarchy problem but can

* test whether a given hierarchy encoding is coherent,
* distinguish low tension and high tension regions of model space,
* falsify specific choices of observables and thresholds.

In all experiments, states that fall into the singular set `S_sing` are treated as **out of domain** and excluded from hierarchy tension statistics.

### Experiment 1: Hierarchy tension scan over model libraries

**Goal**

Test whether the chosen encoding and tension functional can assign clearly different hierarchy tension scores to model classes that are intuitively natural or unnatural.

**Setup**

* Choose a finite set of explicit benchmark models that include

  * low scale supersymmetric models with different mediation schemes,
  * composite or pseudo Nambu Goldstone Higgs models,
  * minimal Standard Model with a fixed high cutoff,
  * extra dimensional models with warped or large volume geometries.

* For each benchmark, identify a representative point in its parameter space that is compatible with current collider and precision constraints.

**Protocol**

1. For each benchmark model and parameter point, construct a state `m` in `M_reg` using an encoding in `E_hier`.
2. Evaluate `m_weak(m)`, `M_UV(m)`, `Delta_nat(m)` and then compute `H_scale(m)`, `H_nat(m)` and `H_total(m)`.
3. Discard any configuration that lies in `S_sing` as out of domain.
4. Record the set of hierarchy tension scores across all benchmarks.
5. Group models into “intuitively natural” and “intuitively unnatural” based on independent qualitative criteria.

**Metrics**

* Distribution of `H_total(m)` for the two groups.
* Separation between the two distributions, for example in terms of mean values or a simple distance between their cumulative distributions.
* Stability of the separation under small changes of `g_scale`, `g_nat`, and library reference values that remain within the declared fixed choices for `WeightKey_Q022` and `LibraryKey_ref_Q022`.

**Falsification conditions**

* If the encoding assigns similar or lower `H_total` to benchmarks that are widely regarded as unnatural than to benchmarks regarded as natural, and this persists under small robust parameter changes, the current choice of observables and weights is considered falsified at the effective layer.
* If `H_total` is dominated by arbitrary parameter choices in the encoding, such that tiny changes in encoding constants qualitatively reorder the tension ranking without clear justification, the encoding is considered unstable and rejected.

**Encoding implementation note**

All quantities are implemented as continuous real valued observables, consistent with the header metadata `Semantics: continuous`. No discrete or hybrid interpretation is introduced in this experiment.

**Boundary note**

Falsifying a TU encoding in this sense does not solve the canonical hierarchy problem. It only rejects specific spectral_tension encodings for Q022.

---

### Experiment 2: Data driven tightening of hierarchy tension bands

**Goal**

Assess how collider and precision measurements shrink the low tension region of model space and whether any admissible low tension models remain after including updated data.

**Setup**

* Start from a broad prior over model classes that include the benchmarks above and additional general parameterized deformations.
* Use publicly available constraints from collider searches, electroweak precision observables, and flavor physics.

**Protocol**

1. Sample model instances from the prior and discard those incompatible with existing experimental constraints.
2. For each surviving instance, encode it as `m` in `M_reg` using an encoding in `E_hier`.
3. Evaluate `H_total(m)` and discard any `m` that lies in `S_sing` as out of domain.
4. Define a low tension band `H_total(m) <= H_cut` with `H_cut` chosen in advance based on library references and not tuned to the data outcome.
5. Compute the fraction `f_low` of surviving models that lie within the low tension band.

**Metrics**

* Fraction `f_low` of models in the low tension band before and after applying new data.
* Sensitivity of `f_low` to reasonable variations in `H_cut` that remain consistent with the original library based definition and the fixed `WeightKey_Q022`.

**Falsification conditions**

* If, after applying updated constraints, `f_low` becomes effectively zero for every encoding in `E_hier` that respects the fairness constraints, the current hierarchy resolution strategy is considered falsified at the effective layer.
* If the only way to keep `f_low` from collapsing to zero is to move `H_cut` or other thresholds in a way that directly depends on the new data, the encoding is judged to have become post hoc and is rejected.

**Encoding implementation note**

The entire procedure treats model parameters and observables as continuous quantities. Sampling and evaluation are carried out in a way that is independent of the specific measured values of `m_weak` and `M_UV` for our world, except through the experimental constraints themselves.

**Boundary note**

Falsifying a particular family of low tension explanations in this way does not prove which ultraviolet mechanism, if any, resolves the hierarchy problem in nature. It only documents that the given encoding and model class no longer provide a viable low tension band.

---

## 7. AI and WFGY engineering spec

This block describes how Q022 can be used as a module in AI systems inside the WFGY framework.

All modules and signals defined here operate at the effective layer. They must **not** be interpreted as solving the hierarchy problem. They only track and report hierarchy spectral_tension on effective observables.

### 7.1 Training signals

1. `signal_scale_ratio_stability`

   * Definition: a penalty proportional to `H_scale(m)` when the model is reasoning about questions that involve relations between electroweak and ultraviolet scales.
   * Purpose: discourage internal states that treat extremely large scale separations as unremarkable when the context calls for awareness of naturalness.

2. `signal_naturalness_cost`

   * Definition: a penalty proportional to `H_nat(m)` when the model proposes or evaluates theoretical scenarios.
   * Purpose: reduce preference for explanations that implicitly require very fine tuned cancellations unless such tuning is explicitly discussed.

3. `signal_hierarchy_tension_score`

   * Definition: an auxiliary scalar equal to `H_total(m)` for states encoding specific physics scenarios.
   * Purpose: give the system an explicit knob representing hierarchy tension that can be minimized, compared, or reported to the user.

4. `signal_counterfactual_hier_separation`

   * Definition: a training signal that encourages the model to maintain distinct internal patterns for World T and World F style reasoning about the hierarchy problem, rather than mixing the two.
   * Purpose: improve clarity when the system is asked to reason under different assumptions about naturalness.

### 7.2 Architectural patterns

1. `HierarchyTensionHead`

   * Role: a module that maps internal representations of physics scenarios to an estimated `H_total(m)` together with `H_scale(m)` and `H_nat(m)`.
   * Interface:

     * Inputs: context embeddings that contain information about scales, couplings, and mechanisms.
     * Outputs: a small vector of tension scores that downstream modules or users can inspect.

2. `NaturalnessConsistencyFilter`

   * Role: filters or re ranks candidate completions according to their implied hierarchy tension.
   * Interface:

     * Inputs: candidate text completions or structured scenario descriptions.
     * Outputs: soft scores indicating whether each candidate is low, moderate, or high tension in the sense of Q022.

3. `ScaleSeparationDescriptor`

   * Role: a general purpose descriptor for scale separation patterns that can be reused in other physics or AI interpretability tasks.
   * Interface:

     * Inputs: internal numerical summaries of scale related quantities.
     * Outputs: a compact representation suitable for comparison and clustering.

These modules should only monitor and structure reasoning. They do not themselves introduce new physics or fix ultraviolet completions.

### 7.3 Evaluation harness

1. Task set

   * Construct a benchmark of questions and tasks where awareness of the hierarchy problem and naturalness considerations is important, for example

     * comparing different beyond Standard Model proposals,
     * explaining trade offs between naturalness and experimental constraints,
     * critiquing scenario descriptions that hide fine tuning.

2. Conditions

   * Baseline condition: the model uses no explicit hierarchy tension modules.
   * TU condition: the model uses `HierarchyTensionHead` and `NaturalnessConsistencyFilter` with signals from Q022.

3. Metrics

   * Accuracy and coherence on tasks that explicitly ask about naturalness or the hierarchy problem.
   * Frequency of unmarked acceptance of highly fine tuned scenarios.
   * Stability of the model reasoning when the user explicitly asks for low tension solutions versus arbitrary solutions.

### 7.4 60 second reproduction protocol

* Baseline setup

  * Prompt: ask the model to explain the hierarchy problem and compare two specific models, for example a minimal Standard Model with high cutoff and a low scale supersymmetric model, without mentioning tension or WFGY.
  * Observation: record whether the explanation clearly identifies issues of fine tuning and scale separation.

* TU encoded setup

  * Prompt: ask the same question but instruct the model to use “hierarchy tension” and “scale separation tension” as organizing ideas, and to report a qualitative `H_total` style judgment for each model.
  * Observation: record whether the explanation becomes more structured and whether the tension scores align with independent expert expectations.

* Comparison metric

  * Use a rubric that scores explanations for clarity, explicit recognition of fine tuning, and consistent treatment of scale ratios, then compare baseline and TU encoded responses.

* What to log

  * Prompts, raw responses, and the hierarchy tension scores produced by Q022 related modules, so that users can audit the behavior without access to any internal generative rules of TU.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: `HierarchyTensionScore`

   * Type: functional

   * Minimal interface:

     * Inputs: `m_weak`, `M_UV`, `Delta_nat` for a given scenario.
     * Output: scalar `H_total` together with `H_scale` and `H_nat`.

   * Preconditions:

     * Inputs must be well defined and finite, with `M_UV > m_weak > 0`.

   From the metadata viewpoint this functional is the **canonical spectral_tension functional** for Q022: it maps effective mass and coupling spectra to a single nonnegative tension score.

2. ComponentName: `ScaleSeparationDescriptor`

   * Type: field

   * Minimal interface:

     * Inputs: a list of relevant physical scales for a scenario.
     * Output: a compact vector summarizing ratios and qualitative separation patterns.

   * Preconditions:

     * The scales provided should be distinct and associated with identifiable physical sectors.

3. ComponentName: `CounterfactualScaleWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a model class with at least one low energy scale and one ultraviolet scale.
     * Output: a pair of experiment descriptions analogous to World T and World F, together with associated tension evaluation procedures.

   * Preconditions:

     * The model class must admit a meaningful definition of naturalness or fine tuning at the effective layer.

### 8.2 Direct reuse targets

1. Q023 (Strong CP and theta naturalness)

   * Reused component: `HierarchyTensionScore` and `CounterfactualScaleWorld_Template`.
   * Why it transfers: the effective tension can be repurposed to measure how natural a small QCD theta angle is relative to high energy dynamics.
   * What changes: the observables become angle parameters and associated nonperturbative effects rather than mass scales, but the structure of low versus high tension worlds is analogous.

2. Q027 (Cosmological constant naturalness)

   * Reused component: `ScaleSeparationDescriptor`.
   * Why it transfers: the cosmological constant problem also involves extreme separation between vacuum energy scales and other physical scales.
   * What changes: the observables involve vacuum energy densities and spacetime curvature rather than the Higgs mass, but the descriptor format is the same.

3. Q059 (Information thermodynamics of computation)

   * Reused component: `ScaleSeparationDescriptor`.
   * Why it transfers: tasks involving mapping logical depth to physical energy scales can reuse the notion of scale separation across physical and computational domains.
   * What changes: scales are now temperature, energy per operation, and device sizes rather than particle physics scales.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * The basic hierarchy tension observables and functional have been defined at the effective layer.
  * Singular sets and admissible encoding constraints have been specified so that external auditors can see where the freedom lies.

* N_level: N2

  * The narrative distinguishes low and high hierarchy tension worlds.
  * Counterfactual patterns and their relation to proposed mechanisms are explicit enough to structure discussions and experiments.

### 9.2 Next measurable step toward E2

To move from E1 to E2, the following concrete steps are proposed.

1. Implement a public code that, given benchmark models and parameter points, computes `H_total`, `H_scale`, and `H_nat` and publishes the resulting scores and choices of encoding parameters associated with `EncodingKey_Q022`.
2. Apply the Experiment 1 and Experiment 2 protocols to existing benchmark sets and document which encodings and models remain viable under the declared fairness constraints.

Both steps operate strictly at the effective layer on observable summaries and do not require revealing any deep TU generative rules.

### 9.3 Long term role in the TU program

In the longer term, Q022 is intended to act as

* the central node for naturalness and scale separation tension problems in physics,
* a template for expressing similar questions in other domains where parameters appear fine tuned,
* a bridge for connecting fundamental theory discussions with AI systems that can track and report hierarchy tension in their own internal reasoning.

---

## 10. Elementary but precise explanation

The hierarchy problem is about something that sounds simple but is very stubborn.

On one side there is the electroweak scale, set by the Higgs field. It tells you roughly where certain particles get their mass. This scale is around one hundred GeV.

On the other side there is a very high scale such as the Planck scale, where gravity becomes strong or where new physics is expected. This is many orders of magnitude higher.

If you write the equations for the Higgs in a standard way, quantum corrections try to drag its mass parameter up toward the high scale. To keep the observed mass small, you have to balance the bare value and the corrections to a very delicate degree. That looks like fine tuning.

The question is

```txt
Is there a good reason why this delicate balance happens,
or is it just an unexplained adjustment of numbers?
```

In the Tension Universe view we do not try to answer this directly. Instead, we

* define a number that measures how extreme the separation of scales is,
* define another number that measures how fine tuned the parameters look,
* combine them into a hierarchy tension score.

We then imagine two kinds of worlds.

In a low tension world, there is some mechanism that keeps the Higgs mass stable. For example a symmetry that forces certain dangerous corrections to cancel, or a composite structure that makes the Higgs behave differently at high energies. In such a world the hierarchy tension score stays modest and does not explode when you look more carefully.

In a high tension world, nothing protects the Higgs. The corrections are huge and the small observed mass only appears because large contributions cancel in an unnatural way. In such a world the hierarchy tension score is large for any realistic description.

This way of talking does not decide which world we live in. It does not prove any specific theory. What it gives is

* a clear set of observables and scores that say how serious the hierarchy problem is in a given scenario,
* a way to test whether different proposed solutions really reduce the tension or only hide it,
* reusable tools that can be carried over to other naturalness and scale separation problems.

Q022 is therefore the reference pattern for expressing hierarchy and naturalness questions in the Tension Universe framework, staying within the effective layer and leaving the deep generative rules hidden.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S problem collection.

### Scope of claims

* The goal of this document is to specify an **effective layer encoding** of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.
* For Q022 in particular, the hierarchy and spectral tension scores defined here are diagnostic tools on effective observables. They are not evidence that any specific ultraviolet solution to the hierarchy problem is realized in nature.

### Effective layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores, and counterfactual worlds, live entirely at the effective layer of the TU framework.
* No statement in this document specifies or relies on any deep TU generating rules, axiom systems, or microscopic ontology.
* Any procedure that maps experimental data or microscopic models into the state spaces mentioned here is external to this document and may be implemented in multiple ways.

### Encoding and fairness

* The encoding keys in the header metadata identify a finite or effectively enumerable class of admissible encodings for this problem.
* All thresholds, weights, and library choices are fixed before evaluating world data and must not be tuned post hoc to improve tension scores.
* Falsifying a specific encoding, library, or weight choice in this sense does not falsify the TU framework as a whole.

### Reuse and versioning

* The reusable components named in Section 8 are defined at the level of interfaces and effective observables only.
* Future documents may refine or extend these components as long as backward compatibility with the stated interfaces is preserved.
* When comparing different TU documents, readers should always check the encoding keys and version tags in the header metadata.

### Charters

This encoding is governed by the following TU charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

