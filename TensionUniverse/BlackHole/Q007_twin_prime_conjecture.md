# Q007 · Twin prime conjecture (run 2 · effective-layer spec)

## 0. Header metadata

```txt
ID: Q007
Code: BH_MATH_TWINPRIME_L3_007
Domain: Mathematics
Family: Number theory (analytic and combinatorial)
Rank: S
Projection_dominance: I
Field_type: counting_field
Tension_type: counting_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Encoding_class: encoding_class_TP_E2_proto
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* We only specify observable state spaces, summaries, invariants, mismatch functionals, tension scores and counterfactual worlds.
* We do not specify any underlying TU axiom system, generative rule, or deep structural equation.
* We do not provide a constructive mapping from raw arithmetic or simulation data into internal TU fields. We only assume that such mappings exist and that they can produce states inside the regular domain defined later in this file.
* No object in this file should be read as a direct exposure of any TU “core” or “base” layer. All such structures remain outside the scope of this document.

This page does not claim to prove or disprove the canonical mathematical statement of the twin prime conjecture. It only describes one effective-layer encoding and tension framing for that problem under fixed TU charters.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself.

A twin prime pair is a pair of primes `(p, p + 2)`.

The twin prime conjecture (TPC) states:

> There exist infinitely many primes `p` such that `p` and `p + 2` are both prime.

Equivalently:

> The set of twin prime pairs `(p, p + 2)` is infinite.

### 1.2 Status and difficulty

Classical facts:

* It is known that there are infinitely many primes, but it is not known whether infinitely many twin prime pairs exist.
* Sieve methods and analytic number theory give upper bounds and conditional asymptotic formulas for twin prime counts, but no unconditional proof of infinitude.
* The Hardy–Littlewood prime pair conjecture predicts a precise asymptotic for the number of twin primes up to `x`, involving the twin prime constant `C_2`.

Modern progress:

* Results on bounded gaps between primes (Zhang, Maynard, Tao, Polymath and others) show there are infinitely many prime pairs with bounded gap, currently much larger than `2`.
* These results are compatible with TPC but do not imply it.

TPC is widely regarded as a very difficult open problem. It is simple to state, strongly constrained by analytic number theory, and deeply tied to the fine-scale structure of primes.

### 1.3 Role in the BlackHole / TU program

Within the BlackHole S-problem collection and Tension Universe (TU), Q007 plays several roles:

1. It is the canonical **prime-pair and small-gap counting_tension** problem. We compare actual twin prime counts with fixed analytic expectations and sieve-compatible bands.
2. It anchors a cluster of problems about prime gaps and additive structure of primes, including Goldbach-type questions and bounded gap phenomena.
3. It provides a clean E1 and E2 proto testbed for TU encoding principles:

   * freeze the interval family once,
   * freeze the reference library once,
   * define one reproducible way to aggregate mismatches into a tension functional.

This document does not attempt to prove or disprove TPC. It only specifies an **effective-layer encoding** of how twin prime behavior is turned into a scalar tension signal under strict fairness constraints.

### 1.4 References

1. Standard encyclopedia entry on the twin prime conjecture, including historical background and known results.
2. G. H. Hardy, E. M. Wright, *An Introduction to the Theory of Numbers*, chapters on primes and prime gaps.
3. H. Halberstam, H. E. Richert, *Sieve Methods*, sections on prime pairs and small gaps.
4. Expository surveys on bounded gaps between primes and connections to twin primes by contemporary experts.

---

## 2. Position in the BlackHole graph

This block records how Q007 sits in the BlackHole graph among Q001–Q125. Each edge is justified by a concrete component or tension type at the effective layer.

### 2.1 Upstream problems

Upstream nodes provide prerequisites or tools Q007 relies on.

* **Q001 · Riemann Hypothesis**
  Code: `BH_MATH_NUM_L3_001`
  Reason: supplies spectral tools and zero statistics templates that motivate the reference heuristics encoded in the frozen twin-prime library, though Q007 itself is a counting_field problem at E1.

* **Q005 · abc conjecture**
  Code: `BH_MATH_ABC_L3_005`
  Reason: provides global constraints on prime factors and densities that shape admissible long-range prime patterns, including possible twin prime densities.

* **Q006 · Goldbach conjecture**
  Code: `BH_MATH_GOLDBACH_L3_006`
  Reason: shares additive structure on primes and motivates a common framework for prime pair and small-gap encodings.

* **Q019 · distribution of rational points**
  Code: `BH_MATH_DIOPH_DENSITY_L3_019`
  Reason: encodes general density and distribution methods that are reused for twin prime density analysis.

### 2.2 Downstream problems

Downstream nodes reuse Q007 components or depend on its tension structure.

* **Q018 · pair correlation of zeros of zeta functions**
  Code: `BH_MATH_RANDOM_MATRIX_ZEROS_L3_018`
  Reason: reuses `TwinPrimeGap_TensionFunctional` as a template for linking zero pair statistics to prime pair statistics.

* **Q051 · P versus NP**
  Code: `BH_CS_PVNP_L3_051`
  Reason: uses structured prime-pair counting as a toy model for hard counting problems and approximate counting tension.

* **Q105 · prediction of systemic crashes**
  Code: `BH_COMPLEX_CRASHES_L3_105`
  Reason: reuses prime gap clustering and twin pair scale profiles as toy models for clustering near critical thresholds in complex systems.

### 2.3 Parallel problems

Parallel nodes share similar tension types or narrative roles.

* **Q006 · Goldbach conjecture**
  Code: `BH_MATH_GOLDBACH_L3_006`
  Reason: both study patterns in primes with simple additive relations, using similar counting_tension encodings.

* **Q008 · Collatz conjecture**
  Code: `BH_MATH_COLLATZ_L3_008`
  Reason: both are simple discrete statements with unresolved long-range behavior, producing high combinatorial tension.

* **Q009 · odd perfect numbers**
  Code: `BH_MATH_ODDPERF_L3_009`
  Reason: shares the property of a simple number-theoretic statement with deep unresolved structure in prime factors.

### 2.4 Cross-domain edges

Cross-domain edges connect Q007 to problems in other domains that reuse its components.

* **Q032 · quantum foundations of thermodynamics**
  Code: `BH_PHYS_QTHERMO_L3_032`
  Reason: reuses `PrimePair_ScaleProfile` as a toy model for gap statistics in energy spectra and microstates.

* **Q059 · thermodynamic cost of information processing**
  Code: `BH_CS_INFO_THERMODYN_L3_059`
  Reason: uses twin prime gap patterns as examples of structured, non-trivial sequences in studies of compression and energy cost.

* **Q123 · scalable interpretability**
  Code: `BH_AI_INTERP_L3_123`
  Reason: uses `TwinPrimeGap_TensionFunctional` as a structured field to test whether AI representations capture deep arithmetic patterns.

---

## 3. Tension Universe encoding (effective layer, run 2)

All content in this block is at the effective layer. We only describe:

* state space,
* observables and fields,
* fixed interval family and reference library,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden TU generative rules or any constructive mapping from raw data to internal TU fields.

### 3.1 Canonical interval family

To eliminate degrees of freedom in the choice of regions, we fix a single deterministic interval family for Q007.

We define, for each integer `k >= 10`:

```txt
I_k = [2^k, 2^(k+1)]
```

Given a maximum data bound `X_max >= 2^11`, we define:

```txt
k_min = 10
k_max(X_max) = max { k in Z : k_min <= k and 2^(k+1) <= X_max }
K_all(X_max) = { k in Z : k_min <= k <= k_max(X_max) }
```

For any experiment that uses actual prime or twin prime data up to `X_max`, the only allowed index set of scales is:

```txt
K_finite = K_all(X_max)
```

No experiment is allowed to:

* drop individual `k` inside `K_all(X_max)`,
* reorder intervals,
* inject additional intervals not of the form `I_k`.

This removes interval-selection tuning as a degree of freedom for Q007.

### 3.2 State space

We define a semantic state space:

```txt
M_TP
```

with the following effective interpretation.

Each state `m` in `M_TP` represents a coherent prime gap and twin prime world for a specific finite bound `X_max(m)`, including:

* the list of indices `K_finite(m) = K_all(X_max(m))`,
* summaries of primes and twin prime pairs in each interval `I_k` with `k in K_finite(m)`,
* meta information about data quality and completeness.

We do not specify how raw lists of primes are turned into states. We only assume:

* for each admissible `X_max` and associated `K_all(X_max)`, there exist states `m` whose summaries match actual or synthetic data for all `I_k`,
* these summaries are coherent on a regular subset of `M_TP`.

### 3.3 Effective observables

On `M_TP` we define the following observables, all tied to the frozen interval family.

1. Prime count observable

```txt
pi_1(m; k) >= 0
```

* Input: state `m`, scale index `k` with `k in K_finite(m)`.
* Output: integer equal to the number of primes `p` with `p in I_k`.

2. Twin prime count observable

```txt
pi_2(m; k) >= 0
```

* Input: state `m`, scale index `k`.
* Output: integer equal to the number of twin prime pairs `(p, p + 2)` with `p in I_k`.

3. Data-bound observable

```txt
X_max(m) >= 0
```

* Input: state `m`.
* Output: finite real or integer satisfying `2^(k_max(m)+1) <= X_max(m)` and `K_finite(m) = K_all(X_max(m))` as defined above.

We require that, for any `m` in the regular domain, `pi_1`, `pi_2`, and `X_max` are all well defined and finite.

### 3.4 Frozen reference library RefLib_TP

To remove ambiguity in standard heuristics, we fix a single reference model for twin prime counts, based on the Hardy–Littlewood twin prime heuristic.

Let `C_2` be the twin prime constant, defined by the convergent Euler product:

```txt
C_2 = product over primes p > 2 of [ p (p - 2) / (p - 1)^2 ]
```

For each integer `n >= 3`, define a weight:

```txt
w_HL(n) = 1 / (log n)^2
```

For each interval `I_k = [2^k, 2^(k+1)]`, define the reference twin prime count:

```txt
pi_2_ref(k) =
  round( C_2 * sum over integers n in I_k with n >= 3 of w_HL(n) )
```

Here `round(x)` denotes rounding `x` to the nearest integer, with ties rounded to the nearest even integer. This rounding rule is fixed for this encoding and may not be changed by individual implementations.

The reference library for Q007 is the singleton set:

```txt
RefLib_TP = { HL_fixed }
```

where `HL_fixed` denotes the above rule. There is no freedom to choose alternative reference functions inside this problem file.

For any state `m` and scale `k in K_finite(m)` we define:

```txt
pi_2_ref(m; k) = pi_2_ref(k)
```

Note:

* `pi_2_ref(m; k)` only depends on `k` and the fixed analytic formula, not on `pi_2(m; k)` or any other data in `m`.
* Updating or replacing `RefLib_TP` would define a new encoding class at the charter level, not a silent change of this file.

### 3.5 Sieve-based bounds and DeltaS_sieve

We now define a concrete sieve-based mismatch observable.

For each interval `I_k` we define lower and upper expected bands:

```txt
L_k = max( 0, c_L * pi_2_ref(k) )
U_k = c_U * pi_2_ref(k)
```

with fixed constants:

```txt
c_L = 0.25
c_U = 4.0
```

These constants are chosen once at the TU charter level for Q007 and are not tuned on the basis of data for any particular state.

Given a state `m` and index `k in K_finite(m)` we define the per-interval sieve violation:

```txt
v_sieve(m; k) =
  max( max(0, pi_2(m; k) - U_k),
       max(0, L_k - pi_2(m; k)) )
```

This quantity is:

* zero if the encoded twin prime count lies inside `[L_k, U_k]`,
* positive otherwise, increasing linearly with the distance from the band.

We then define the aggregate sieve mismatch:

```txt
DeltaS_sieve(m) =
  (1 / |K_finite(m)|) * sum over k in K_finite(m) of v_sieve(m; k)
```

This is a nonnegative scalar that:

* is small when twin prime counts stay within the band for most scales,
* grows when counts systematically fall outside the band.

### 3.6 Pair-count mismatch DeltaS_pair and aggregation

Per-interval twin prime mismatch is defined by:

```txt
DeltaS_pair(m; k) =
  | pi_2(m; k) - pi_2_ref(k) |
```

We aggregate these mismatches across all allowed scales for state `m`:

```txt
DeltaS_pair_aggregate(m) =
  (1 / |K_finite(m)|) *
  sum over k in K_finite(m) of DeltaS_pair(m; k)
```

By construction:

```txt
DeltaS_pair_aggregate(m) >= 0
```

This scalar is small when encoded twin prime counts track the HL fixed reference across scales and large when there is persistent deviation.

### 3.7 Fixed weights and combined mismatch DeltaS_TP

To avoid functional degrees of freedom, we fix the weights:

```txt
alpha_pair = 1/2
beta_sieve = 1/2
```

for all uses of Q007 in this file.

The combined twin prime mismatch is defined as:

```txt
DeltaS_TP(m) =
  alpha_pair * DeltaS_pair_aggregate(m)
  + beta_sieve * DeltaS_sieve(m)
```

This is the only combined mismatch scalar used by Q007 at the effective layer.

No other weighting schemes or nonlinear combinations are allowed inside this file. Any alternative combination belongs to a distinct encoding class defined at the charter level.

### 3.8 Core tension functional Tension_TP

The core twin prime tension functional is identified with the combined mismatch:

```txt
Tension_TP(m) = DeltaS_TP(m)
```

That is:

```txt
Tension_TP(m) =
  (1/2) * DeltaS_pair_aggregate(m)
  + (1/2) * DeltaS_sieve(m)
```

This choice removes the earlier freedom to pick an arbitrary monotone continuous function of the mismatch components.

The interpretation is:

* low `Tension_TP(m)` means twin prime counts match the frozen HL reference and stay within the sieve band across all allowed scales,
* high `Tension_TP(m)` means systematic deviation from both the reference and the sieve band.

All mismatch terms and tension values in this file are understood relative to a global dimensionless tension scale fixed by the TU Tension Scale Charter.

### 3.9 Singular set and regular domain

Some states may encode incomplete or inconsistent information. We collect these in a singular set:

```txt
S_sing_TP =
  { m in M_TP :
      X_max(m) undefined
      or K_finite(m) != K_all(X_max(m))
      or there exists k in K_finite(m) with
         pi_1(m; k) undefined
         or pi_2(m; k) undefined
      or DeltaS_TP(m) not finite }
```

We define the regular domain:

```txt
M_reg_TP = M_TP \ S_sing_TP
```

All Q007 tension analysis is restricted to `M_reg_TP`. Any attempt to evaluate `Tension_TP(m)` for `m in S_sing_TP` must be recorded as out of domain for that protocol and not as evidence for or against the twin prime conjecture.

---

## 4. Tension principle for this problem (run 2)

This block states how Q007 is characterized as a tension problem within TU at the effective layer, using the frozen interval family, reference library, and functional defined above.

### 4.1 Twin prime conjecture as low counting_tension

At the effective layer, the twin prime conjecture is recast as the existence of world-representing states `m_T` in `M_reg_TP` such that:

* twin primes continue to appear at all tested scales inside the frozen interval family,
* the combined tension `Tension_TP(m_T)` stays within a low band that does not blow up as data quality and `X_max` increase, when interpreted in the fixed TU tension scale.

More concretely, in a world where TPC holds and where prime data is faithfully encoded, we expect:

* for each admissible `X_max`, there exists at least one state `m_T(X_max) in M_reg_TP` such that:

  ```txt
  Tension_TP(m_T(X_max)) <= epsilon_TP
  ```

  for some finite `epsilon_TP` that:

  * depends on the encoding class and sieve constants,
  * may depend mildly on computational approximation quality,
  * does not grow without bound as `X_max` increases,
  * is interpreted relative to the TU Tension Scale Charter and is not tuned to force any specific dataset to look good or bad.

In this view, TPC becomes the assertion that the actual universe admits low counting_tension representations at all large scales under the frozen Q007 encoding.

### 4.2 Twin prime failure as persistent high counting_tension

If the twin prime conjecture were false, then for any encoding in `encoding_class_TP_E2_proto` that remains faithful to the actual prime sequence, we would expect:

* for some sufficiently large scales `k`, `pi_2(m; k)` becomes extremely small or zero, while `pi_2_ref(k)` remains positive,
* the sieve band `[L_k, U_k]` becomes increasingly strained or violated.

In such a world, there would exist world-representing states `m_F` in `M_reg_TP` and a positive constant `delta_TP` such that, for all sufficiently large `X_max`:

```txt
Tension_TP(m_F(X_max)) >= delta_TP
```

Here `delta_TP` is interpreted on the same global tension scale as in Section 3.8. It cannot be made arbitrarily small by:

* changing `K_finite`,
* changing the reference function inside `RefLib_TP`,
* changing the weights inside this file,

because all of those are frozen by construction.

### 4.3 Interpretive summary

Q007, in run 2, is explicitly a counting_tension harness:

* the only free aspect of the world is the actual prime sequence up to `X_max`,
* the interval family, reference library, sieve bands, and combination function are fully frozen,
* the resulting scalar `Tension_TP(m)` is a reproducible gauge of how twin-prime-like the encoded data is, under a fixed analytic and sieve template.

This formulation does not claim that:

* low tension proves TPC, or
* high tension disproves TPC.

It only states what patterns of mismatch we should see in hypothetical worlds where TPC is true or false, given the Q007 encoding.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer:

* World T: twin primes are infinite and follow patterns compatible with the frozen reference and sieve band.
* World F: twin primes are finite, or so sparse that they cannot be reconciled with the frozen reference and sieve band in any faithful encoding.

The description is entirely in terms of observable counts and tension patterns.

### 5.1 World T (twin primes infinite, low tension)

In World T:

1. For each admissible `X_max`, there exists a state `m_T(X_max) in M_reg_TP` with:

   * `K_finite(m_T) = K_all(X_max)`,
   * nonzero `pi_2(m_T; k)` for all sufficiently large `k` in `K_all(X_max)`.

2. For each such `m_T(X_max)`:

   * per-interval mismatches `DeltaS_pair(m_T; k)` fluctuate within a bounded range compatible with the fixed heuristic `pi_2_ref(k)`,
   * sieve violations `v_sieve(m_T; k)` are zero or small for most `k`.

3. The aggregate mismatch and tension satisfy:

   ```txt
   DeltaS_pair_aggregate(m_T(X_max)) stays within a moderate band
   DeltaS_sieve(m_T(X_max)) stays within a moderate band
   Tension_TP(m_T(X_max)) <= epsilon_TP
   ```

   where `epsilon_TP` does not explode with `X_max` and is interpreted on the fixed TU tension scale.

Twin primes may show irregularities and local clustering, but not persistent, scale-wide suppression relative to the frozen model.

### 5.2 World F (twin primes finite, high tension)

In World F:

1. There exists some scale `k_0` such that, above that scale, twin primes are absent or extremely rare:

   * for all sufficiently large `k >= k_0`, `pi_2(m_F; k)` is zero or much smaller than `pi_2_ref(k)`.

2. For large enough `X_max`, any faithful state `m_F(X_max)` must satisfy:

   * `DeltaS_pair(m_F; k)` large for many `k` in `K_all(X_max)`,
   * `v_sieve(m_F; k)` nonzero for many `k` as `L_k` is violated.

3. Consequently,

   ```txt
   DeltaS_pair_aggregate(m_F(X_max)) >= c_pair > 0
   DeltaS_sieve(m_F(X_max)) >= c_sieve > 0
   Tension_TP(m_F(X_max)) >= delta_TP
   ```

   for some positive constants `c_pair`, `c_sieve`, `delta_TP` that cannot be driven arbitrarily small by re-encoding inside the same class. These constants live on the global TU tension scale and are not tuned to fit any particular dataset.

### 5.3 Interpretive note

These counterfactuals do not claim to construct primes, and they do not exist at the level of internal TU fields. They are:

* templates for how an observable counting_tension functional behaves,
* given that we accept the frozen Q007 encoding and suppose that TPC is either true or false.

They guarantee that if different teams implement Q007 correctly, using the same `I_k`, `RefLib_TP` and sieve bands, their `Tension_TP` profiles are comparable.

---

## 6. Falsifiability and discriminating experiments (run 2)

This block specifies experiments that:

* test the coherence and robustness of the Q007 encoding,
* expose unfair or unstable choices, which now should only come from outside this file,
* do not prove or disprove the twin prime conjecture.

### Experiment 1: Numerical twin prime tension profiles with fixed encoding

**Goal**
Evaluate `Tension_TP` on actual prime data up to `X_max` for the frozen encoding and examine stability under extension of `X_max`.

**Setup**

* Input: published tables or computed lists of primes and twin prime pairs up to some `X_max`.
* Interval family: always `I_k = [2^k, 2^(k+1)]` with `K_finite = K_all(X_max)`.
* Reference: `RefLib_TP = {HL_fixed}`, as defined in Section 3.4.
* Weights: fixed `(alpha_pair, beta_sieve) = (1/2, 1/2)` and uniform averaging over `K_finite`.
* All tension values are recorded on the TU tension scale defined in the TU Tension Scale Charter.

**Protocol**

1. For a sequence of increasing bounds `X_max^(1) < X_max^(2) < ...`, construct states `m_data^(r)` in `M_reg_TP` by:

   * encoding `K_finite(m_data^(r)) = K_all(X_max^(r))`,
   * computing `pi_1(m_data^(r); k)` and `pi_2(m_data^(r); k)` for all `k in K_finite(m_data^(r))`.

2. For each `m_data^(r)`:

   * compute `DeltaS_pair(m_data^(r); k)` and `DeltaS_pair_aggregate(m_data^(r))`,
   * compute `v_sieve(m_data^(r); k)` and `DeltaS_sieve(m_data^(r))`,
   * compute `Tension_TP(m_data^(r))`.

3. Record the trajectory:

   ```txt
   Tension_TP(m_data^(1)), Tension_TP(m_data^(2)), ...
   ```

   together with the decomposed components.

**Metrics**

* Behavior of `Tension_TP(m_data^(r))` as `X_max^(r)` increases.
* Relative contributions of `DeltaS_pair_aggregate` and `DeltaS_sieve`.
* Sensitivity to small implementation differences, such as different but equivalent ways of computing `C_2`, which should be minimal.

**Falsification conditions (encoding level)**

* If implementations that follow the spec produce wildly different `Tension_TP` values on the same prime data, the encoding is considered underspecified and must be tightened.
* If small, justified numerical approximations to `C_2` or to the HL sum cause tension to swing from very low to very high, the encoding is considered too fragile and must be revised at the charter level.
* If, while keeping RefLib, interval family and weights fixed, the tension profile shows unexplainable discontinuities tied to technical encoding choices rather than to actual prime data, that is evidence against the robustness of the current Q007 encoding.

**Boundary note**
Even if the tension trajectory looks low and stable or high and unstable, this experiment does not settle TPC. It only evaluates the behavior of the run 2 encoding.

---

### Experiment 2: Synthetic twin-prime-like and twin-prime-suppressed worlds

**Goal**
Verify that `Tension_TP` reliably distinguishes between synthetic sequences that imitate HL-like twin prime behavior and sequences where twin prime pairs are systematically suppressed beyond some scale.

**Setup**

* Fix the same interval family, reference model, sieve bands, weights, and tension scale as in Experiment 1.
* Construct two families of synthetic sequences of integers:

  * Family `T_model`: sequences with abundant gap-2 pairs, tuned to mimic HL densities in each `I_k`.
  * Family `F_model`: sequences where gap-2 pairs are removed or heavily suppressed for all `k` beyond some fixed `k_0`.

**Protocol**

1. For each synthetic sequence `S` in `T_model` and bound `X_max`, construct a state `m_T_model(S, X_max)`:

   * define `K_finite` via `X_max`,
   * compute `pi_1` and `pi_2` counts from the synthetic sequence.

2. For each synthetic sequence `S` in `F_model` and the same `X_max`, construct `m_F_model(S, X_max)` similarly.

3. For all such states, compute:

   * `DeltaS_pair_aggregate`,
   * `DeltaS_sieve`,
   * `Tension_TP`.

4. Compare the empirical distributions of `Tension_TP` for family `T_model` and `F_model`.

**Metrics**

* Mean and variance of `Tension_TP` for `T_model` and `F_model`.

* Separation statistics, such as:

  ```txt
  P( Tension_TP(T_model) < Tension_TP(F_model) )
  ```

* Robustness under different synthetic constructions, as long as they respect the same frozen encoding.

**Falsification conditions (encoding level)**

* If `Tension_TP` does not tend to be systematically lower for `T_model` than for `F_model` across a range of synthetic designs, the current encoding fails as a twin-prime tension discriminator.
* If some `F_model` variants consistently get lower tension than plausible HL-like `T_model` variants, in ways that contradict the intended semantics, the run 2 encoding must be reconsidered.

**Boundary note**
Success or failure on synthetic families constrains the usefulness of the encoding. It does not provide evidence for or against TPC itself.

---

## 7. AI and WFGY engineering spec (run 2)

This block describes how Q007 can be used as an engineering module for AI systems within WFGY, strictly at the effective layer.

### 7.1 Training signals

We define several training signals derived from Q007 observables.

1. `signal_twin_pair_mismatch`

   * Definition: a normalized version of `DeltaS_pair_aggregate(m)` for the current context.
   * Use: discourages internal states that imply twin prime statistics wildly inconsistent with the frozen HL reference when the context assumes standard twin prime heuristics.

2. `signal_sieve_band_violation`

   * Definition: a normalized version of `DeltaS_sieve(m)`.
   * Use: penalizes states where implied twin prime counts systematically lie outside the fixed sieve band.

3. `signal_twinprime_tension_total`

   * Definition: scaled `Tension_TP(m)` for the current state, mapped into a fixed range by a bounded monotone transform consistent with the TU Tension Scale Charter.
   * Use: provides an overall scalar that downstream modules can attempt to minimize in contexts where twin-prime-consistent behavior is desired, or to keep track of when exploring counterfactual worlds.

4. `signal_counterfactual_split_T_vs_F`

   * Definition: a measure of how distinctly the model separates internal states when prompted under World T versus World F assumptions, based on differences in `Tension_TP` and its components.
   * Use: encourages the model to maintain clear internal bookkeeping about which world assumption is active.

### 7.2 Architectural patterns

We outline module patterns that reuse Q007 structures.

1. `PrimeGapField_Observer`

   * Role: map internal embeddings from number-theoretic contexts into a structured summary of prime and twin prime statistics over the frozen intervals.
   * Inputs: an internal embedding representing numbers up to `X_max`.
   * Outputs: a vector of approximate counts or densities for `pi_1` and `pi_2` over each `I_k`.

2. `TwinPrimeTensionHead`

   * Role: approximate `DeltaS_pair_aggregate`, `DeltaS_sieve` and `Tension_TP` from the outputs of `PrimeGapField_Observer`.
   * Inputs: the summary vector per context.
   * Outputs: scalars approximating the Q007 defined quantities, plus optional decomposed components.

3. `TU_PrimePair_Filter`

   * Role: check candidate statements about twin primes and prime gaps against the tension signals.
   * Inputs: candidate explanations or claims, for example that twin primes behave HL-like at certain scales.
   * Outputs: confidence scores or masks based on `signal_twin_pair_mismatch` and `signal_sieve_band_violation`.

### 7.3 Evaluation harness

To evaluate the effect of Q007 based modules on an AI model:

1. **Task selection**

   * Questions and explanations involving:

     * definitions of TPC and twin primes,
     * known partial results and bounded gaps,
     * heuristic arguments based on HL and sieve methods.

2. **Conditions**

   * Baseline: model without Q007 modules or signals.
   * TU enhanced: same backbone with `PrimeGapField_Observer`, `TwinPrimeTensionHead` and the training signals from Section 7.1.

3. **Metrics**

   * Correctness and faithfulness in separating:

     * proven results,
     * conjectures,
     * heuristic expectations.

   * Consistency across prompts that explicitly switch between assuming TPC is true and assuming TPC is false.

   * Stability of explanations when asked to reference scale wise behavior in `I_k` intervals instead of only informal talk.

### 7.4 Sixty second reproduction protocol

A minimal protocol for external users:

* Baseline prompt:

  > Explain the twin prime conjecture, summarize what is known about bounded gaps between primes, and how sieve methods inform our expectations about twin primes. Clearly distinguish between theorems and conjectures.

* TU prompt:

  > Using a fixed family of intervals `[2^k, 2^(k+1)]` and a Hardy–Littlewood style reference for twin primes, explain the twin prime conjecture as a tension between observed twin prime counts and this frozen model. Describe what a low-tension world and a high-tension world would look like.

The user compares:

* structural clarity,
* explicit mention of scale wise behavior,
* explicit distinction between observed data, heuristic expectations and open status.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by Q007 run 2

1. `TwinPrimeGap_TensionFunctional`

   * Type: functional.

   * Interface:

     * Inputs:

       * `prime_gap_summary` and `twin_pair_summary` over the fixed intervals `I_k`,
       * implicit reference to the frozen HL model and sieve bands.
     * Output: `twin_gap_tension_value = Tension_TP(m)` in `[0, infinity)`.

   * Preconditions:

     * summaries correspond to a coherent state in `M_reg_TP`,
     * intervals are exactly `I_k` as defined in Section 3.1.

2. `PrimePair_ScaleProfile`

   * Type: field.
   * Interface:

     * Inputs: `k` with `k >= 10` and `X_max` such that `2^(k+1) <= X_max`.
     * Output: a descriptor of twin prime density and gap statistics within `I_k`, for example normalized counts and simple histograms.

3. `TwinPrime_CounterfactualWorld_Template`

   * Type: experiment pattern.
   * Interface:

     * Inputs:

       * data source, actual primes or synthetic sequence,
       * bound `X_max`.
     * Output:

       * a pair of experiment definitions corresponding to World T and World F scenarios using `Tension_TP`.

### 8.2 Direct reuse targets

1. **Q006 · Goldbach conjecture**

   * Reuse: `PrimePair_ScaleProfile`.
   * Reason: Goldbach statements depend on prime pairs around even integers. The same scale profiles can be adapted to study how often near by prime pairs appear for such sums.

2. **Q018 · pair correlation of zeros of zeta functions**

   * Reuse: `TwinPrimeGap_TensionFunctional`.
   * Reason: the analogy between zero pair statistics and prime pair statistics allows similar tension functionals to be used for zeros and primes.

3. **Q059 · thermodynamic cost of information processing**

   * Reuse: `PrimePair_ScaleProfile`.
   * Reason: structured but irregular sequences like twin primes are good examples of compressible yet non trivial signals, useful for encoding cost studies.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* **E_level: E1**

  * The run 2 effective encoding for Q007 specifies:

    * a frozen interval family `I_k`,
    * a frozen reference library `RefLib_TP = {HL_fixed}`,
    * explicit sieve based bands and a concrete definition of `DeltaS_sieve`,
    * fixed weights `(alpha_pair, beta_sieve)` and a fixed linear `Tension_TP`,
    * a singular set and regular domain.

  * The encoding already has the structure of an `encoding_class_TP_E2_proto`. E_level remains set to E1 until a public reference implementation and benchmark report are published as described in Section 9.2.

* **N_level: N1**

  * The narrative:

    * explains TPC as a counting_tension problem under fixed analytic and sieve templates,
    * defines World T and World F,
    * clarifies that rejecting encodings is not the same as proving or disproving TPC.

  * N_level remains N1 for consistency with other entries, even though this file already includes minimal counterfactual templates.

### 9.2 Next measurable step toward E2

To reach E2 for Q007, the following should be implemented and published:

1. A reference implementation that:

   * takes as input prime and twin prime tables up to `X_max`,
   * constructs `m_data(X_max)`,
   * computes `DeltaS_pair_aggregate(m_data)`, `DeltaS_sieve(m_data)` and `Tension_TP(m_data)` on the TU tension scale,
   * outputs tension profiles for a sequence of `X_max`.

2. A small benchmark report that:

   * documents the implementation choices,
   * publishes the tension trajectory and component decompositions,
   * allows other teams to rerun the same pipeline and compare results.

This reference implementation is expected to cover at least Experiment 1 and Experiment 2 from Section 6, with all parameters and interval families frozen according to this file.

These steps remain entirely at the effective layer and must respect the frozen encoding of this file and the shared TU charters.

### 9.3 Long term role in TU

In the longer term Q007 is intended to be:

* the canonical example of a prime-pair counting_tension problem,
* a calibration point for how TU handles simple statements with deep unresolved structure,
* a reusable test field for AI based reasoning modules that need to respect:

  * the difference between proofs and heuristics,
  * the constraints of fixed encodings and non mutation policies.

---

## 10. Elementary but precise explanation (aligned with run 2)

The twin prime conjecture asks:

> Are there infinitely many pairs of primes of the form `(p, p + 2)`?

We know there are infinitely many primes, and we can find many twin pairs such as `(3, 5)`, `(5, 7)`, `(11, 13)`, `(17, 19)`. What nobody has proved is whether such pairs keep appearing forever or eventually run out.

In the Tension Universe view, instead of trying to prove the conjecture directly, we do three things.

1. We fix once and for all a way to look at the data.

   * We use intervals of the form `[2^k, 2^(k+1)]` for `k >= 10`.
   * For each interval we count how many primes there are and how many twin prime pairs there are.

2. We fix once and for all a reference model.

   * We use a standard Hardy–Littlewood formula that predicts how many twin primes we should see in each interval.
   * We use simple sieve based bands that say how far above or below that prediction we consider acceptable.

3. We turn the comparison into a single number called `Tension_TP`.

   * If actual twin prime counts track the reference model and stay inside the band, `Tension_TP` is small.
   * If they systematically fall outside, `Tension_TP` is large.

Then we ask two questions.

* In a world where twin primes really do go on forever with a roughly HL like distribution, can we keep `Tension_TP` small and reasonably stable as we look at larger and larger powers of two?
* In a world where twin primes eventually disappear or become extremely rare, are we forced to see `Tension_TP` stay large, no matter how we encode the data, as long as we respect the fixed rules?

This framework does not answer the conjecture. It does:

* give a precise and reproducible way to talk about how twin prime behavior matches or fails to match a fixed analytic and sieve picture,
* make it possible to compare different experiments and implementations, because the interval family and reference are frozen,
* provide a reusable tension field for AI systems and other TU problems that need a structured, non trivial number theoretic benchmark.

Q007 in run 2 is therefore the counting_tension laboratory for twin primes. The statement is simple, the encoding is strictly specified, and the framing is deliberately neutral about whether twin primes are infinite, while forcing all knobs that could hide the answer to be fixed in advance.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

### Scope of claims

* The goal of this document is to specify an effective-layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores and counterfactual worlds, live at the effective layer.
* No step in this file gives a constructive mapping from raw experimental or simulation data into internal TU fields.
* No step exposes any deep TU generative rule or any first-principle axiom system.

### Encoding and fairness

* Admissible encoding classes, reference profiles and weight families used in this page are constrained by the TU charters listed above.
* For every encoding class referenced here:

  * its definition, parameter ranges and reference families are fixed at the charter level before any problem-specific tuning;
  * these choices may depend on general physical or mathematical considerations and on public benchmark selections, but not on the unknown truth value of this specific problem;
  * no encoding is allowed to hide the canonical answer as an uninterpreted field, label or parameter.

### Tension scale and thresholds

* All mismatch terms `DeltaS_*` and tension functionals in this file are treated as dimensionless or normalized quantities, defined up to a fixed monotone rescaling specified in the TU Tension Scale Charter.
* Thresholds such as `epsilon_*`, `delta_*` and experiment cutoffs are always interpreted relative to that fixed scale.
* Changing the tension scale requires an explicit update of the TU Tension Scale Charter, not an edit of individual problem files.

### Falsifiability and experiments

* Experiments described in this document are tests of TU encodings, not tests of the underlying canonical problem itself.
* The rule that falsifying a TU encoding is not the same as solving the canonical statement is understood to apply globally, even where it is not restated.
* When required observables cannot be reliably estimated in practice, the outcome of the corresponding experiment is recorded as inconclusive, not as confirmation.

### Interaction with established results

* All encodings and counterfactual worlds described here are required to respect known theorems and hard constraints in the relevant field.
* If a later analysis finds a concrete conflict with established results, the correct procedure is to update or retire the encoding under the TU charters, not to reinterpret those results.

### Versioning and non-mutation policy

* This file is a versioned specification within the WFGY / Tension Universe research program.
* Definitions and symbols in this file are frozen for this version.
* Revisions, if needed, must be published as a new versioned file or accompanied by an explicit changelog entry and must not silently alter prior definitions.
* All changes to encoding classes, reference libraries, weight ranges or tolerance models that affect multiple problems should be made at the charter level, not by local edits to this file.

### Program note

* This page is an experimental specification within the ongoing WFGY / Tension Universe program.
* All structures and parameter choices are provisional and may be revised in future versions, subject to the constraints above.
