# Q015 · Uniform boundedness of ranks of elliptic curves

## 0. Header metadata

```txt
ID: Q015
Code: BH_MATH_RANK_BOUNDS_L3_015
Domain: Mathematics
Family: Number theory (arithmetic geometry)
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: risk_tail_tension
Status: Open
Semantics: discrete
E_level: E1
N_level: N1
Last_updated: 2026-01-24
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Fix a number field `K` of finite degree over `Q`.

Let `E(K)` denote the Mordell–Weil group of `K` rational points on an elliptic curve `E` defined over `K`.

The group `E(K)` is finitely generated. There is a decomposition

```txt
E(K) ~= E(K)_torsion + Z^r
```

where `E(K)_torsion` is the finite torsion subgroup and `r` is a nonnegative integer called the rank of `E(K)`.

The uniform boundedness of ranks problem asks:

> For a fixed number field `K`, does there exist a finite constant `R(K)` such that for every elliptic curve `E` over `K`, the rank `r(E(K))` satisfies
>
> `r(E(K)) <= R(K)`?

Equivalently, is the set of ranks of elliptic curves over `K` bounded from above by a field dependent constant.

Special case:

* For `K = Q`, this asks whether there exists a universal constant `R(Q)` such that every elliptic curve over `Q` has rank at most `R(Q)`.

There are related questions about uniform boundedness in families over varying fields, but this entry focuses on the fixed field case.

### 1.2 Status and difficulty

Facts that frame the status:

* It is known that elliptic curves over `Q` can have rank at least `28` and over some number fields even higher ranks are known.

* There is no known proof that ranks are unbounded over `Q`, and no known proof that they are bounded. Both directions remain open.

* Deep conjectures in arithmetic statistics suggest that:

  * "Typical" elliptic curves should have rank `0` or `1`.
  * Higher ranks should be increasingly rare in a quantitative sense.

* The Birch and Swinnerton–Dyer conjecture links the rank to the order of vanishing of the associated L function at `s = 1`. This gives a pathway from analytic data to rank, but the conjecture is open in general.

No proof or disproof of uniform boundedness is known for `K = Q` or for general number fields. The problem is considered extremely difficult and sits near the center of modern arithmetic geometry.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q015 serves as:

1. A prototype for **risk_tail_tension** problems in arithmetic geometry.

   * The "risk" is the possibility of extremely high ranks.
   * The "tail" is the part of the rank distribution at large rank.

2. A bridge between analytic information and arithmetic complexity.

   * It links Q003 (BSD), Q001 and Q002 (spectral control of L functions), and Q019 (distribution of rational points).

3. A test case for Tension Universe encodings that must handle:

   * finite libraries of objects indexed by a size parameter,
   * tail behavior of an arithmetic invariant,
   * refinement in a discrete scale variable `k` without after the fact parameter tuning.

### References

1. J. H. Silverman, "The Arithmetic of Elliptic Curves", Springer Graduate Texts in Mathematics, first edition 1986, second edition 2009.
2. G. Faltings, "Endlichkeitssätze für abelsche Varietäten über Zahlkörpern", Inventiones Mathematicae 73 (1983), 349–366.
3. H. Darmon, F. Diamond, R. Taylor (editors), "Fermat’s Last Theorem and the Birch and Swinnerton–Dyer Conjecture", papers and surveys on ranks and L functions.
4. M. Bhargava, A. Shankar, "The average rank of elliptic curves over `Q`", various papers in Annals of Mathematics and related journals, around 2015, giving statistical information about ranks.

---

## 2. Position in the BlackHole graph

This block records how Q015 is connected to other Q nodes and which components are expected to be reused. Reasons are given at the effective layer and point to concrete components defined later.

### 2.1 Upstream problems

These problems supply tools or conceptual frameworks that Q015 relies on.

* Q003 (BH_MATH_BSD_L3_003)
  Reason: Provides the analytic to arithmetic bridge between L function behavior and ranks, used conceptually when defining rank related tension and counterfactual worlds.

* Q014 (BH_MATH_BOMB_LANG_L3_014)
  Reason: Supplies global expectations about rational points on higher dimensional varieties, which influence how rank boundedness connects to more general finiteness principles.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019)
  Reason: Encodes methods for describing growth of rational points in bounded height regions, directly related to how rank affects point counts.

* Q001 (BH_MATH_RIEMANN_L3_001)
  Reason: Offers a template for spectral tension encodings that can be adapted when L functions and their zeros enter the discussion of rank statistics.

* Q002 (BH_MATH_GRH_L3_002)
  Reason: Supplies stronger analytic assumptions that may tighten the expected reference profiles used for rank and height distributions.

### 2.2 Downstream problems

These problems reuse Q015 components or take Q015 as a direct dependency.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019)
  Reason: Reuses the finite library encoding and tail tension functionals when relating ranks to counts of rational points in families.

* Q020 (BH_MATH_HEIGHT_DISTRIB_L3_020)
  Reason: Reuses the RankHeightCoupling observable to study how other arithmetic invariants scale with height or conductor.

* Q101 (BH_ECON_EQUITY_PREM_L3_101)
  Reason: Adapts the rank tail tension pattern to risk tail tension in financial return distributions as an abstract template.

### 2.3 Parallel problems

Parallel nodes share similar tension patterns but do not require direct component reuse.

* Q003 (BH_MATH_BSD_L3_003)
  Reason: Both handle connections between arithmetic invariants and analytic objects, but Q003 focuses on exact equalities while Q015 focuses on uniform bounds and tails.

* Q014 (BH_MATH_BOMB_LANG_L3_014)
  Reason: Both express global boundedness or finiteness principles across large families, framed as tension between complexity and structural constraints.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019)
  Reason: Both involve describing how arithmetic complexity behaves as height bounds grow.

### 2.4 Cross domain edges

Cross domain edges connect abstract tension templates from Q015 to other fields.

* Q101 (BH_ECON_EQUITY_PREM_L3_101)
  Reason: Reuses the idea of finite libraries indexed by a scale parameter and a tail tension score to model heavy tail financial risks.

* Q105 (BH_COMPLEX_CRASHES_L3_105)
  Reason: Reuses the "finite library with rare extreme states" picture as an abstract structure for systemic failures or crashes in complex systems.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We describe only:

* state spaces,
* observables and fields,
* mismatch and tension functionals,
* singular sets and domain restrictions.

We do not describe any hidden TU generative mechanisms or how data are constructed from first principles.

Throughout this file the base field `K` is fixed.

### 3.1 State space

We introduce a semantic state space

```txt
M
```

with the following effective interpretation.

Each state `m` in `M` represents a finite library of elliptic curves over `K` together with coarse statistics about ranks and size parameters.

More concretely, for each integer scale parameter `k` in a chosen index set, `m` encodes:

* a finite library `L_k` of elliptic curves over `K` selected by a fixed rule that depends only on a size parameter such as conductor or height,
* for each `E` in `L_k`, a rank estimate and associated size parameter,
* aggregated statistics over `L_k`.

We do not specify how the library is generated from raw data. We only require:

1. The library rule is fixed in advance and depends only on a size parameter, not on observed ranks.
2. For each `k`, the encoded library `L_k` is finite.
3. The encoded rank and size statistics are well defined for all curves in `L_k`.

### 3.2 Observables and fields

We define the following effective observables for a state `m` in `M` and index `k` in the library index set.

1. Library size

```txt
library_size(m; k) >= 0
```

* Number of elliptic curves in `L_k` encoded inside `m`.

2. Maximal rank in the library

```txt
rank_max(m; k) >= 0
```

* Maximum of the ranks `r(E(K))` for curves in `L_k`, according to the encoded rank data.

3. Rank distribution descriptor

```txt
rank_distribution(m; k)
```

* A tuple or vector that summarizes how many curves in `L_k` have ranks in various bins.
* For example it might record counts for rank `0`, `1`, `2`, and one or more tail bins `>= 3`, `>= 4`, and so on.
* The precise encoding is not important, only that it is a finite dimensional summary that can be compared with reference profiles.

4. Size parameter profile

```txt
size_profile(m; k)
```

* A tuple or vector summarizing size parameters such as conductors or heights for curves in `L_k`.
* For example it might record average logarithmic height, median conductor, and a dispersion measure.

The observables are treated as deterministic functions of `m` and `k` in the effective description.

### 3.3 Mismatch observables

We now define mismatch observables that compare the data in `m` with reference behaviors compatible with a uniform rank bound hypothesis.

1. Rank tail mismatch

```txt
DeltaS_rank_tail(m; k) >= 0
```

* Measures how far the encoded `rank_distribution(m; k)` deviates from a reference "bounded rank" profile at the tail.
* The reference class is fixed in advance and consists of distributions where ranks are bounded by some ceiling and tails decay in a specified way as `k` grows.

2. Rank height coupling mismatch

```txt
DeltaS_height_rank_coupling(m; k) >= 0
```

* Measures inconsistency between how `rank_max(m; k)` grows with the scale parameter and how the size profile behaves.
* For example, if `size_profile(m; k)` grows roughly like a known function of `k`, but `rank_max(m; k)` grows in a way that cannot be reconciled with any bounded rank hypothesis, this mismatch becomes large.

3. Combined rank bound mismatch

We define a combined mismatch:

```txt
DeltaS_rank_bound(m; k) =
  w_tail * DeltaS_rank_tail(m; k)
  + w_cpl  * DeltaS_height_rank_coupling(m; k)
```

where:

* `w_tail` and `w_cpl` are fixed positive weights chosen before any data analysis,
* `w_tail + w_cpl = 1` for normalization.

The weights are part of the encoding design and are not adjusted after observing library data.

### 3.4 Singular set and domain restriction

Some states may encode incomplete or inconsistent information. This can make mismatch observables undefined or infinite.

We define the singular set:

```txt
S_sing = {
  m in M :
  there exists k in the index set
  such that DeltaS_rank_tail(m; k)
  or DeltaS_height_rank_coupling(m; k)
  is undefined or not finite
}
```

We then define the regular domain:

```txt
M_reg = M \ S_sing
```

All rank bound tension analysis in this file is restricted to states `m` in `M_reg`. If an experimental protocol attempts to evaluate `DeltaS_rank_bound(m; k)` for a state in `S_sing`, the result is treated as "out of domain" rather than as meaningful evidence about the conjecture.

---

## 4. Tension principle for this problem

This block explains how Q015 is encoded as a tension principle at the effective layer.

### 4.1 Core tension functional

We define an effective rank bound tension functional for each state `m` in `M_reg` and index `k`:

```txt
Tension_rank_bound(m; k) =
  alpha * DeltaS_rank_tail(m; k)
  + beta  * DeltaS_height_rank_coupling(m; k)
```

where:

* `alpha > 0` and `beta > 0` are fixed constants chosen in advance,
* `alpha + beta = 1`,
* `Tension_rank_bound(m; k) >= 0` for all `m` in `M_reg`.

We may also consider an aggregated tension over a range of indices:

```txt
Tension_rank_bound_agg(m; K_range) =
  sup over k in K_range of Tension_rank_bound(m; k)
```

for a finite or countable set `K_range` of indices.

### 4.2 Finite libraries and refinement order

We choose a refinement order on libraries through a sequence of index values:

```txt
k_1 < k_2 < k_3 < ...
```

Each `k_j` corresponds to a library rule based on a size cutoff `H(k_j)` that is fixed in advance. For example, `L_k` might be:

* all curves over `K` with conductor at most `H(k)`, or
* all curves over `K` with canonical height at most `H(k)`,

where `H(k)` is a strictly increasing function of `k` chosen once and used for all states.

Refinement rule:

* Increasing `k` corresponds to enlarging the library by raising the size cutoff.
* Neither the library rule nor the refinement rule depends on observed ranks.

This gives a discrete refinement structure:

```txt
k_1 < k_2 < ...  means  L_{k_1} subset or contained in L_{k_2} in a controlled way.
```

### 4.3 Fairness constraints

To avoid after the fact tuning, we impose fairness constraints on the encoding:

1. Library construction is independent of rank outcomes.

   * For each `k`, `L_k` is determined only by the size cutoff `H(k)` and a fixed enumeration scheme, not by rank data.

2. Reference profiles are fixed in advance.

   * The class of reference rank distributions and reference height growth curves is specified before any comparison with actual libraries.
   * Reference objects may be based on neutral statistical models, but they are not adapted to the particular extreme ranks observed later.

3. Weights and coefficients are locked.

   * The weights `w_tail`, `w_cpl`, and the combination coefficients `alpha`, `beta` are chosen once and kept constant across all libraries and experiments.

These constraints ensure that tension scores are not tuned to match or hide observed extremes.

### 4.4 Rank bound as a low tension principle

At the effective layer, the uniform rank bound conjecture for `K` can be phrased as a low tension principle:

> There exists a field dependent ceiling `R(K)` and a choice of fair encoding such that for libraries `L_k` built by the fixed refinement rule, world representing states `m` in `M_reg` satisfy
>
> `Tension_rank_bound(m; k)` in a controlled low band for all sufficiently large `k`.

More precisely, in a world where a uniform bound exists and the encoding is fair, we expect:

```txt
There exists epsilon_U > 0 and k_0
such that for all k >= k_0
and for some world states m_U(k) in M_reg
representing the actual arithmetic,
Tension_rank_bound(m_U(k); k) <= epsilon_U.
```

The threshold `epsilon_U` may depend on modeling choices and numerical precision, but it should not grow without control as `k` increases.

### 4.5 Unbounded ranks as persistent high tension

If ranks are unbounded over `K`, and encodings remain fair and faithful to the data, we expect that any world representing sequence `m_N(k)` will eventually exhibit persistent high tension.

This can be expressed as:

```txt
There exists delta_N > 0 and a sequence k_j
with k_j -> infinity as j increases,
such that for world states m_N(k_j) in M_reg
Tension_rank_bound(m_N(k_j); k_j) >= delta_N
for infinitely many j.
```

The positive constant `delta_N` captures a lower bound on how much the observed rank tails and rank height coupling deviate from the reference bounded rank world.

In this way, Q015 becomes the question of whether the actual universe sits in a low tension rank world or a persistent high tension rank world relative to a fair encoding.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds, both framed entirely at the effective layer.

* World U: a world where uniform boundedness of ranks holds over `K`.
* World N: a world where ranks over `K` are unbounded.

These descriptions do not construct curves or ranks from first principles. They only describe patterns in libraries and tension scores.

### 5.1 World U (uniform bound world)

In World U:

1. Library behavior

   * For each sufficiently large index `k`, there exists a state `m_U(k)` in `M_reg` representing a library `L_k` in which the maximal rank `rank_max(m_U(k); k)` stays below a ceiling `R(K)` that does not depend on `k`.

2. Rank distribution tail

   * The rank distribution summaries `rank_distribution(m_U(k); k)` converge, in an appropriate sense, toward a reference bounded rank profile as `k` increases.
   * The rank tail mismatch `DeltaS_rank_tail(m_U(k); k)` stays small and eventually stabilizes within a narrow band.

3. Rank height coupling

   * The growth of `rank_max(m_U(k); k)` as a function of `k` remains compatible with the way size profiles grow.
   * The mismatch `DeltaS_height_rank_coupling(m_U(k); k)` remains small and does not show systematic drift upward.

4. Tension profile

   * The rank bound tension satisfies:

     ```txt
     Tension_rank_bound(m_U(k); k) <= epsilon_U
     ```

     for all `k` beyond some index `k_0`, with `epsilon_U` as in Block 4.

### 5.2 World N (unbounded ranks world)

In World N:

1. Library behavior

   * For any candidate ceiling `R`, there exist indices `k` and world representing states `m_N(k)` in `M_reg` where `rank_max(m_N(k); k) > R`.

2. Rank distribution tail

   * For an infinite sequence of indices `k_j`, the rank distribution summaries `rank_distribution(m_N(k_j); k_j)` show heavier tails than any reference bounded rank profile in the class fixed by the encoding.
   * The rank tail mismatch `DeltaS_rank_tail(m_N(k_j); k_j)` is bounded below by some positive constant on infinitely many `j`.

3. Rank height coupling

   * The growth of `rank_max(m_N(k_j); k_j)` relative to `size_profile(m_N(k_j); k_j)` violates any bounded rank compatible coupling model in the reference class.
   * The mismatch `DeltaS_height_rank_coupling(m_N(k_j); k_j)` remains bounded away from zero for infinitely many `j`.

4. Tension profile

   * There exists `delta_N > 0` such that

     ```txt
     Tension_rank_bound(m_N(k_j); k_j) >= delta_N
     ```

     for infinitely many `j`.

### 5.3 Interpretive note

The descriptions of World U and World N are conditional:

* They assume the existence of fair and faithful encodings as defined in Block 4.
* They do not assert that either world is the actual universe.
* They do not provide a proof of uniform boundedness or its failure.

Instead, they give a way to talk about what patterns of rank and height data would look like in each scenario when summarized through finite libraries and tension scores.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments that can test the coherence and usefulness of the Q015 encoding. They do not prove or disprove uniform boundedness. They can falsify particular choices of encoding and parameter settings at the effective layer.

### Experiment 1: Tension profile in enumerated libraries over Q

*Goal:*
Evaluate whether the chosen `Tension_rank_bound` encoding produces stable and interpretable tension profiles when applied to enumerated elliptic curves over `Q` ordered by a size parameter.

*Setup:*

* Fix `K = Q`.
* Choose a standard enumeration of elliptic curves over `Q` by conductor or height, for example via minimal Weierstrass equations and an ordering by conductor.
* For a sequence of cutoff values `H(k)` that increase with `k`, define libraries `L_k` as all curves in the enumeration with conductor at most `H(k)`.
* For each `L_k`, construct a state `m_k` in `M_reg` that encodes:

  * approximate ranks (based on known results, numerical experiments, or collected databases),
  * size parameters,
  * library size and rank distribution summaries.

*Protocol:*

1. For each `k` in a chosen finite set, compute:

   * `library_size(m_k; k)`,
   * `rank_max(m_k; k)`,
   * `rank_distribution(m_k; k)`,
   * `size_profile(m_k; k)`.

2. Compute mismatch observables:

   * `DeltaS_rank_tail(m_k; k)` by comparing the observed tail of `rank_distribution(m_k; k)` with a fixed reference bounded rank profile.
   * `DeltaS_height_rank_coupling(m_k; k)` by comparing the relationship between `rank_max(m_k; k)` and `size_profile(m_k; k)` with the reference coupling model.

3. Combine them into tension values:

   ```txt
   Tension_rank_bound(m_k; k) =
     alpha * DeltaS_rank_tail(m_k; k)
     + beta  * DeltaS_height_rank_coupling(m_k; k)
   ```

4. Record the sequence `Tension_rank_bound(m_k; k)` as `k` increases.

*Metrics:*

* Shape of the tension sequence as a function of `k`.
* Sensitivity of the tension sequence to small changes in reference profile within the fixed class.
* Stability of tension values under minor variations in how rank bins are chosen in `rank_distribution`.

*Falsification conditions:*

* If for all reasonable choices of weights and reference profiles within the predefined class, the sequence `Tension_rank_bound(m_k; k)` behaves in an erratic way that cannot be attributed to sampling noise or known limitations of the data, then the current encoding is considered unstable and rejected.
* If very small changes in encoding details cause large qualitative changes in whether the tension is classified as low or high for the same library data, the encoding is considered too fragile and rejected.
* If `DeltaS_rank_tail` and `DeltaS_height_rank_coupling` frequently become undefined or non finite for states that should be regular by construction, so that many `m_k` fall into `S_sing`, the encoding is considered improperly posed and rejected.

*Semantics implementation note:*
This experiment treats libraries and distributions in a discrete setting. All summaries and mismatch measures are based on finite histograms and finite dimensional vectors, consistent with the discrete choice in the metadata.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can reject specific ways of encoding rank bound tension, but it cannot prove or disprove uniform boundedness of ranks.

---

### Experiment 2: Synthetic families with forced high rank tails

*Goal:*
Test whether the Q015 encoding can distinguish synthetic models that have artificially heavy rank tails from models that respect a bounded rank pattern.

*Setup:*

* Construct two model families of elliptic curve libraries over `Q` or another fixed number field.

  * Family U model: synthetic libraries generated so that ranks are capped at a fixed ceiling and distributions follow a bounded rank reference profile.
  * Family N model: synthetic libraries where a small fraction of curves are assigned artificially high ranks in a way that violates any bounded rank profile in the reference class.

* Ensure that both families share similar size profiles, so that the main difference is in rank tails.

*Protocol:*

1. For each index `k` in a chosen range, build:

   * a synthetic state `m_U(k)` for the bounded rank model,
   * a synthetic state `m_N(k)` for the high rank tail model.

2. For each state, compute:

   * `DeltaS_rank_tail`,
   * `DeltaS_height_rank_coupling`,
   * `Tension_rank_bound(m_U(k); k)` and `Tension_rank_bound(m_N(k); k)`.

3. Compare the distributions of tension values for the two families across indices.

*Metrics:*

* Mean and variance of `Tension_rank_bound` for the U model and the N model as functions of `k`.
* Separation between the two tension distributions, measured by simple statistics such as difference in means or overlap of empirical histograms.
* Robustness of separation under small changes in encoding parameters within the fixed reference class.

*Falsification conditions:*

* If the encoding assigns consistently lower or comparable tension to N model libraries with forced high rank tails than to U model libraries with bounded ranks, the encoding is considered misaligned with the intended risk_tail_tension type and rejected.
* If the encoding fails to maintain a meaningful separation between the two families under parameter choices that remain within the predefined class, it is considered ineffective for Q015 and must be revised.

*Semantics implementation note:*
All synthetic libraries are constructed and analyzed in the discrete framework. Observables are finite dimensional summaries and all tension scores are computed by algebraic operations on these summaries.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. Success or failure on synthetic families only tests the quality of the Q015 tension encoding, not the truth of the uniform boundedness conjecture for actual elliptic curves.

---

## 7. AI and WFGY engineering spec

This block describes how Q015 can be used as a module inside AI systems that reason about arithmetic geometry, without exposing any deep TU generative rules.

### 7.1 Training signals

We define several training or diagnostic signals derived from Q015.

1. `signal_rank_tail_tension`

   * Definition: a scalar signal proportional to `DeltaS_rank_tail(m; k)` for states where the model is asked to reason about families of elliptic curves.
   * Purpose: penalize internal representations that imply rank tails incompatible with bounded rank assumptions in contexts where such assumptions are part of the background.

2. `signal_rank_height_consistency`

   * Definition: a signal based on `DeltaS_height_rank_coupling(m; k)`, indicating how coherent the relationship between rank growth and size growth is.
   * Purpose: encourage the model to avoid narratives where maximal rank grows far faster than size in ways that contradict established heuristics or conjectured bounds.

3. `signal_library_coherence`

   * Definition: a summary measure that combines rank and height consistency checks across a finite set of indices `k` for a given reasoning episode.
   * Purpose: provide a single scalar diagnostic that flags when the model tells mutually inconsistent stories about rank distributions across different size ranges.

### 7.2 Architectural patterns

We outline module patterns for integrating Q015 style tension into AI systems.

1. `RankTensionHead`

   * Role: given internal embeddings that represent a family of elliptic curves or a discussion about ranks, this module outputs an estimate of `Tension_rank_bound(m; k)` or related components.
   * Interface: takes embeddings and a scale tag `k`, outputs a small vector with estimated tail mismatch, coupling mismatch, and overall tension.

2. `ArithmeticLibraryObserver`

   * Role: extracts approximate `rank_distribution`, `size_profile`, and `rank_max` summaries from an internal representation of a library or a sequence of curves mentioned in context.
   * Interface: maps embeddings and optional textual descriptions to a library summary suitable for feeding into Q015 tension calculations.

3. `TU_RankConstraint_Filter`

   * Role: acts as a soft filter that adjusts or flags model outputs that imply very high ranks or implausible rank distributions without adequate justification.
   * Interface: evaluates candidate answers and returns a corrected answer or a warning score when tension exceeds a threshold.

### 7.3 Evaluation harness

We propose an evaluation harness to test Q015 aware models.

1. Task set

   * A collection of questions on topics such as:

     * typical rank behavior,
     * known high rank examples,
     * conjectured distributions,
     * consequences of assuming bounded vs unbounded rank scenarios.

2. Conditions

   * Baseline condition: model runs without explicit RankTensionHead or library observer modules.
   * TU condition: model runs with Q015 modules active and tension signals used either as losses during training or as auxiliary guidance during inference.

3. Metrics

   * Logical consistency: how often the model maintains consistent statements about rank ceilings and tails across a multi turn dialogue.
   * Stability: how robust the answers are under rephrasing of questions or small changes in context.
   * Awareness of uncertainty: how often the model correctly identifies the status of uniform boundedness as open rather than making unjustified claims.

### 7.4 60 second reproduction protocol

A minimal user facing protocol to see Q015 in action.

* Baseline setup

  * Prompt the AI: ask for an overview of what is known about ranks of elliptic curves over `Q`, including typical ranks, known high rank examples, and whether there is a known upper bound.
  * Record the answer, focusing on:

    * whether it mistakenly states that ranks are known to be bounded,
    * whether it gives a coherent picture of typical versus maximal behavior.

* TU encoded setup

  * Prompt the AI with a similar question, adding an instruction to:

    * use the idea of finite libraries indexed by size,
    * separate typical rank behavior from tail behavior,
    * avoid claiming any proven uniform bound.

  * If possible, instruct the system to expose an internal estimate of `Tension_rank_bound` for the scenario it describes.

* Comparison metric

  * Rate both answers on:

    * correctness regarding open status,
    * clarity in distinguishing typical behavior from extreme tails,
    * internal consistency across different parts of the explanation.

* What to log

  * Prompts, full responses, any tension scores or library summaries produced by Q015 modules.
  * Logs can be used to refine Q015 encodings and improve model training, without exposing any deep TU generative content.

---

## 8. Cross problem transfer template

This block describes reusable components introduced by Q015 and how they transfer to other problems in the BlackHole graph.

### 8.1 Reusable components produced by this problem

1. ComponentName: `RankTailTension_Functional`

   * Type: functional

   * Minimal interface:

     ```txt
     Inputs:
       rank_distribution_summary
       reference_rank_profile
     Output:
       scalar_tail_mismatch >= 0
     ```

   * Preconditions:

     * The rank distribution summary and reference profile share compatible binning.
     * Both inputs are finite dimensional vectors.

2. ComponentName: `FiniteLibraryEncoding_Template`

   * Type: experiment_pattern

   * Minimal interface:

     ```txt
     Inputs:
       object_family_descriptor
       size_cutoff_function H(k)
       enumeration_rule
     Output:
       for each k:
         library L_k
         library_summary(k)
     ```

   * Preconditions:

     * The enumeration rule depends only on the size cutoff and not on the invariant being studied.
     * For each `k`, the resulting library is finite.

3. ComponentName: `RankHeightCoupling_Observable`

   * Type: observable

   * Minimal interface:

     ```txt
     Inputs:
       rank_max_sequence over k
       size_profile_sequence over k
       coupling_model_reference
     Output:
       scalar_coupling_mismatch >= 0
     ```

   * Preconditions:

     * Both sequences are indexed by the same `k` values.
     * The coupling model reference supplies a predicted relationship between rank and size.

### 8.2 Direct reuse targets

1. Q003 (BH_MATH_BSD_L3_003)

   * Reused component: `FiniteLibraryEncoding_Template`.
   * Why it transfers: BSD analyses often consider families of elliptic curves; structuring them as finite libraries indexed by size is natural.
   * What changes: the main invariants of interest include L function values and regulators in addition to ranks.

2. Q019 (BH_MATH_DIOPH_DENSITY_L3_019)

   * Reused component: `RankTailTension_Functional` and `RankHeightCoupling_Observable`.
   * Why it transfers: rational point counts and densities depend on ranks and heights; tail behavior of ranks influences the tails of point distributions.
   * What changes: the functionals are extended to incorporate point count data and additional complexity measures.

3. Q101 (BH_ECON_EQUITY_PREM_L3_101)

   * Reused component: `FiniteLibraryEncoding_Template`.
   * Why it transfers: risk modeling can treat portfolios or assets as libraries indexed by scale, for example by market capitalization or time horizon.
   * What changes: ranks are replaced by financial risk measures, and size profiles are replaced by economic scale measures.

---

## 9. TU roadmap and verification levels

This block explains the current verification status of Q015 within the Tension Universe program and identifies concrete next steps.

### 9.1 Current levels

* E_level: E1

  * A coherent effective layer encoding has been specified.
  * State space, observables, mismatch functionals, singular set, and at least two experiments with explicit falsification conditions have been defined.
  * No claim is made about numerical results or full scale implementations yet.

* N_level: N1

  * The basic narrative about bounded versus unbounded rank worlds has been articulated in terms of finite libraries and tension scores.
  * Counterfactual worlds U and N are clearly distinguished and linked to observable patterns.
  * There is room to refine the narrative further once implementations exist.

### 9.2 Next measurable step toward E2

To promote Q015 from E1 to E2, at least one of the following should be achieved in practice:

1. Implementation of Experiment 1 with real data.

   * Build libraries `L_k` of elliptic curves over `Q` up to explicit conductor or height bounds.
   * Compute empirical rank and size summaries.
   * Evaluate `Tension_rank_bound(m_k; k)` for a documented choice of encoding parameters.
   * Publish the tension sequences and methodology in a way that can be replicated independently.

2. Implementation of Experiment 2 with transparent model families.

   * Construct synthetic bounded rank and high rank tail families with clearly documented rules.
   * Run the Q015 encoding and demonstrate that tension scores separate the two families in a robust way.
   * Provide code and data so that others can re run the tests.

Both steps can be carried out without exposing any deep TU generative rules. They operate entirely on observable summaries and fixed encoding choices.

### 9.3 Long term role in the TU program

Longer term, Q015 is expected to serve as:

* A standard template for risk tail tension problems in number theory and other domains.
* A test of how far one can go in structuring extremely hard conjectures at the effective layer without over claiming.
* A calibration point for AI systems that must talk responsibly about open problems with large but structured uncertainty.

---

## 10. Elementary but precise explanation

This block gives a non technical explanation of Q015 that still conforms to the effective layer description.

An elliptic curve is a type of equation that defines a smooth curve. When the coefficients are rational numbers, you can ask for all points on the curve whose coordinates are rational numbers too.

These rational points form a group. This group can be broken into two parts:

* a finite part, and
* a grid like part that looks like several copies of the integers.

The number of copies of the integers is called the rank of the elliptic curve. It measures how rich the pattern of rational points is.

For each number field `K`, you can look at all elliptic curves over `K` and ask:

* is there a single number `R(K)` that is bigger than or equal to the rank of every curve over `K`?

No one knows the answer. Some curves have quite high rank. Most curves seem to have small rank. It is not clear whether ranks stay under some fixed ceiling or keep growing without limit.

In the Tension Universe view, we do not try to prove anything about this directly. Instead, we:

1. Build finite libraries of elliptic curves ordered by a size parameter.

2. For each library, summarize:

   * how many curves have each rank,
   * how large the curves are according to a size measure.

3. Compare the observed patterns with reference patterns that would make sense if ranks were bounded.

From this comparison we define mismatch numbers and then a single tension score for each library. That score is small if the library behaves like a world where ranks are bounded. The score is large if the library behaves like a world where ranks keep growing.

We then imagine two kinds of worlds:

* In a bounded world, as we look at larger and larger libraries, the tension scores stay small and stable.
* In an unbounded world, as we look further out, the tension scores are forced to stay high again and again.

This does not tell us which world we live in. It does not prove a theorem. It gives us:

* a way to talk precisely about what kind of data would support one picture or the other, and
* a set of tools that can be reused when other problems involve rare extreme behaviors in large families.

In this sense, Q015 is a central example of how the Tension Universe framework handles questions about whether complexity in a mathematical system remains under control or grows without bound.
