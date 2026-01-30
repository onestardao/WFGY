# Q006 · Goldbach conjecture

## 0. Header metadata

```txt
ID: Q006
Code: BH_MATH_GOLDBACH_L3_006
Domain: Mathematics
Family: Additive number theory
Rank: S
Projection_dominance: I
Field_type: combinatorial_field
Tension_type: consistency_tension
Status: Open
Semantics: discrete
E_level: E2
N_level: N2
Last_updated: 2026-01-30
```

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* We only describe discrete state spaces, observables, finite encoding libraries, mismatch measures, tension functionals, singular sets, and falsifiable experiments.
* We do not specify any TU axioms, deep generative rules, or constructive derivations.
* We do not give any explicit mapping from raw prime tables, proofs, or simulations into internal TU fields.
* We treat all effective quantities as already encoded inside admissible TU states, without explaining how those states are constructed.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Goldbach’s conjecture (binary or “strong” Goldbach) is the statement:

> Every even integer `N >= 4` can be written as the sum of two prime numbers.

Equivalently:

For each even integer `N >= 4`, there exist primes `p_1`, `p_2` such that

```txt
N = p_1 + p_2 .
```

Often one defines, for each even `N`, the number of Goldbach representations

```txt
r_2(N) = count of ordered pairs (p_1, p_2) of primes with p_1 + p_2 = N .
```

The conjecture then says that `r_2(N) >= 1` for all even `N >= 4`.

There is also a “weak” or “ternary” Goldbach conjecture stating that every odd integer greater than or equal to `7` can be written as the sum of three primes. That weaker form has been proved. The binary form remains open.

In this Q006 entry we focus on the binary conjecture.

### 1.2 Status and difficulty

Goldbach’s conjecture has been open since the eighteenth century and is one of the central problems of additive number theory. Key partial results include:

* Almost all even integers can be written as the sum of two primes in the sense of asymptotic density, under suitable analytic number theory hypotheses.
* Chen’s theorem: every sufficiently large even integer `N` can be represented as

  ```txt
  N = p + P_2
  ```

  where `p` is a prime and `P_2` is an “almost prime” (an integer with at most two prime factors, counted with multiplicity).
* Various results using the circle method show that every sufficiently large odd integer is the sum of a bounded number of primes, with successively improved bounds over time.
* Extensive numerical verification has checked Goldbach’s conjecture for all even `N` up to large computational limits, pushing any potential first counterexample very far out.

No general proof or disproof is known. The problem is deeply connected with the distribution of prime numbers and techniques from analytic number theory such as exponential sums and the circle method.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q006 plays several roles:

1. It is the canonical example of an additive number theory problem where **coverage of a discrete line** (even integers) by a structured set (prime pairs) is the central observable.

2. It provides a prototype for **discrete consistency_tension**: tension between observed coverage and representation multiplicities and the expected behavior predicted by density models derived from prime distributions.

3. It links spectral and density information (Q001, Q019) to concrete combinatorial events: whether each even `N` in a window has at least one admissible representation.

4. It acts as a discrete counterpart to spectral problems, useful to test how TU encodings behave when everything lives on the integers rather than on continuous fields.

### References

1. R. K. Guy, *Unsolved Problems in Number Theory*, 3rd edition, Springer, 2004, Part A, section on Goldbach’s conjecture.
2. T. Tao, “Every odd number greater than 1 is the sum of at most five primes”, *Annals of Mathematics*, 2014, based on arXiv:1201.6656.
3. T. Estermann, “On Goldbach’s problem: Proof that almost all even positive integers are sums of two primes”, *Proceedings of the London Mathematical Society*, 1938.
4. A. Ivić, *The Riemann Zeta-Function: Theory and Applications*, Dover Publications, reprint edition, chapters on additive prime problems.

---

## 2. Position in the BlackHole graph

This block records how Q006 sits inside the BlackHole graph. Every edge has a one-line reason pointing to a concrete component or tension object.

### 2.1 Upstream problems

These problems provide prerequisites or reusable structures that Q006 relies on at the effective layer.

* Q001 (BH_MATH_NUM_L3_001 · Riemann Hypothesis)
  Reason: supplies spectral and density constraints for primes that underlie the expected number of Goldbach representations and the Goldbach mismatch profiles.

* Q005 (BH_MATH_ABC_L3_005 · abc conjecture)
  Reason: provides global constraints on sums of integers and prime factors that can be reused to bound “pathological” additive decompositions interacting with Goldbach coverage.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019 · Diophantine density frameworks)
  Reason: offers general density and counting frameworks on the integers that are reused to formalize coverage of even integers by prime pairs.

### 2.2 Downstream problems

These problems directly reuse Q006 components or depend on Q006’s tension structures.

* Q007 (BH_MATH_TWINPRIME_L3_007 · Twin prime conjecture)
  Reason: reuses the EvenIntegerWindow and PrimePairWindow structures to define and compare small gap prime pair tension versus Goldbach coverage tension.

* Q008 (BH_MATH_COLLATZ_L3_008 · Collatz conjecture)
  Reason: reuses the discrete coverage and windowing formalism to compare coverage of positive integers by Collatz orbits with coverage of the even line by prime pairs.

* Q009 (BH_MATH_NONLINEAR_PRIMEPATTERN_L3_009 · Nonlinear prime patterns)
  Reason: reuses Q006’s discrete combinatorial tension library as a baseline for more complicated additive and multiplicative prime patterns.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q001 (BH_MATH_NUM_L3_001 · Riemann Hypothesis)
  Reason: both encode consistency between prime distributions and deeper structures (spectral versus additive), using related mismatch and tension functionals.

* Q007 (BH_MATH_TWINPRIME_L3_007)
  Reason: both focus on primes in pairs; Q006 on sums, Q007 on gaps, with similar counting and window based invariants.

* Q009 (BH_MATH_NONLINEAR_PRIMEPATTERN_L3_009)
  Reason: all three describe discrete fields on integers populated by primes and analyze pattern frequencies under consistency_tension.

### 2.4 Cross domain edges

Cross domain edges connect Q006 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059 · Information and thermodynamics)
  Reason: reuses discrete coverage sequences as examples of structured, sparse occupancy patterns for information density and redundancy models.

* Q123 (BH_AI_INTERP_L3_123 · AI representation interpretability)
  Reason: uses Goldbach style coverage and multiplicity patterns as benchmark structures for testing whether AI internal representations understand arithmetic relations.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* discrete state spaces and window libraries,
* observables and fields,
* invariants and mismatch scores,
* singular sets and domain restrictions,
* a finite encoding library and refinement behaviour.

We do not describe any rule mapping raw prime tables or proofs into internal TU fields.

### 3.1 Window library and density models

We fix once and for all a finite library of windows and density models for Q006.

1. **Window scales**

   We choose a finite index set

   ```txt
   K_stage1 = { k_0, k_0 + 1, ..., k_1 }
   ```

   with associated even integer windows

   ```txt
   W_k = { N : 2^k <= N <= 2^(k+1), N even }  for each k in K_stage1 .
   ```

   The integers `k_0`, `k_1` are fixed as part of this encoding. They are not tuned after observing any tension values.

2. **Density model library**

   We fix a finite library of admissible density models for Goldbach type questions,

   ```txt
   D_j,  j in J_stage1 .
   ```

   In the baseline encoding for Q006 we use a single Hardy–Littlewood type model for binary Goldbach:

   ```txt
   J_stage1 = { 0 }
   D_0 = HL_Goldbach_Model
   ```

   where `HL_Goldbach_Model` denotes a specification that:

   * uses standard prime number theory and singular series heuristics,
   * produces, for each even `N`, an expected number of representations `E[r_2(N)]`,
   * does not use any calibration to empirically observed Goldbach data.

   Any future alternative density model or calibration procedure would define a different encoding version of Q006, not a modification of this baseline.

3. **Coupling rule**

   The coupling between windows and density models is fixed as

   ```txt
   Couple(k) = j(k) = 0  for all k in K_stage1 .
   ```

   That is, all windows share the same theoretical `HL_Goldbach_Model`. There is no data driven choice of `j(k)` inside this encoding.

4. **Refinement order**

   The refinement order on windows is

   ```txt
   refine(k) = k + 1
   ```

   whenever `k + 1` is still in `K_stage1`. Refinement means moving from window `W_k` to `W_(k+1)` and updating the associated expected quantities using the same fixed `D_0`.

### 3.2 State space

We assume a state space

```txt
M
```

with the following effective interpretation.

* Each state `m` in `M` carries the data for exactly one window index `k(m)` in `K_stage1`.

* The associated Goldbach window is

  ```txt
  W(m) = W_{k(m)} = { N : 2^{k(m)} <= N <= 2^{k(m)+1}, N even } .
  ```

* For each even `N` in `W(m)`, the state `m` encodes a summary of prime pairs `(p_1, p_2)` with

  ```txt
  p_1 + p_2 = N ,
  ```

  in a way that is sufficient to evaluate the observables defined below.

The construction of `m` from raw data is not specified. We only assume that:

* For any finite window and prime pair data that could arise in practice, there exist states in `M` that encode it.

### 3.3 Effective observables

We define observables and fields on `M` at the level needed for tension evaluation.

#### 3.3.1 Goldbach coverage observable

```txt
GoldbachCoverage(m) in [0, 1]
```

* Input: a state `m` with window `W(m)`.
* Output: the fraction of even integers in `W(m)` that admit at least one representation as a sum of two primes.

Formally, if

```txt
E(m)     = set of even integers in W(m),
E_cov(m) = { N in E(m) : r_2(N; m) >= 1 } ,
```

then

```txt
GoldbachCoverage(m) = |E_cov(m)| / |E(m)| .
```

Here `r_2(N; m)` is defined below.

#### 3.3.2 Goldbach multiplicity per integer

For each even `N` in `W(m)` we define

```txt
GoldbachMultiplicity(m; N) = r_2(N; m) >= 0
```

where:

* `r_2(N; m)` is the number of ordered prime pairs `(p_1, p_2)` encoded in `m` such that `p_1 + p_2 = N`.

If a particular representation convention is used (for example restricting to `p_1 <= p_2`), that choice is fixed once and applied consistently. In this baseline we use ordered pairs to align with standard analytic number theory conventions.

#### 3.3.3 Multiplicity profile summary

We define, for each state `m`, a fixed 7 dimensional multiplicity summary:

```txt
MultProfile(m) in R^7
```

constructed as follows.

Let

```txt
X_N(m) = log(1 + r_2(N; m))  for each even N in W(m) .
```

Define:

```txt
mu(m)     = mean_N X_N(m)
sigma2(m) = variance_N X_N(m)
q10(m)    = 10th percentile of X_N(m)
q50(m)    = 50th percentile (median) of X_N(m)
q90(m)    = 90th percentile of X_N(m)
f0(m)     = fraction of N in W(m) with r_2(N; m) = 0
f1(m)     = fraction of N in W(m) with r_2(N; m) = 1
```

All averages, variances, and quantiles are taken over the finite set of even integers in `W(m)`.

Then

```txt
MultProfile(m) = [
  mu(m),
  sigma2(m),
  q10(m),
  q50(m),
  q90(m),
  f0(m),
  f1(m)
] .
```

This summary specification is fixed for Q006 and is not adjusted per experiment or dataset.

### 3.4 Expected coverage and multiplicity from the density model

Using the fixed Hardy–Littlewood type density model `D_0 = HL_Goldbach_Model`, we define, for each window index `k` in `K_stage1`:

1. **Per integer expectations**

   For each even `N` in `W_k` the model provides

   ```txt
   E[r_2(N)] >= 0
   ```

   as the expected number of ordered prime pairs with sum `N`, according to the theoretical density model.

2. **Expected coverage ratio**

   We define

   ```txt
   GoldbachCoverageExp(k) in [0, 1]
   ```

   as a function of `E[r_2(N)]` over `N` in `W_k`. For example, one may take

   ```txt
   GoldbachCoverageExp(k) =
     fraction of N in W_k with E[r_2(N)] above a fixed small threshold tau_cov > 0
   ```

   where `tau_cov` is a constant fixed for Q006 and chosen on theoretical grounds. The exact formula is part of the encoding and is not fitted to actual coverage data.

3. **Expected multiplicity profile**

   We define an expected multiplicity profile

   ```txt
   GoldbachMultExp(k) in R^7
   ```

   by applying the same summary construction as in `MultProfile(m)`, but replacing the empirical `r_2(N; m)` by model expectations or a fixed analytic surrogate. Concretely:

   * Define model based values `X_N^model(k) = log(1 + E[r_2(N)])`.
   * Compute the same statistics `mu_model(k), sigma2_model(k), q10_model(k), q50_model(k), q90_model(k)` and fractions
     `f0_model(k), f1_model(k)` using the distribution of `X_N^model(k)` and model based estimates of `P(r_2(N) = 0)` and `P(r_2(N) = 1)`.

   Then

   ```txt
   GoldbachMultExp(k) = [
     mu_model(k),
     sigma2_model(k),
     q10_model(k),
     q50_model(k),
     q90_model(k),
     f0_model(k),
     f1_model(k)
   ] .
   ```

The entire procedure for obtaining `GoldbachCoverageExp(k)` and `GoldbachMultExp(k)` from `D_0` is frozen at the encoding level. It may depend on general analytic number theory considerations but never on measured `r_2(N; m)` from a specific state.

For a state `m` with window index `k(m)`, we use

```txt
GoldbachCoverageExp(m) = GoldbachCoverageExp(k(m))
GoldbachMultExp(m)     = GoldbachMultExp(k(m)) .
```

### 3.5 Additive coverage mismatch with local structure

We now define a coverage mismatch that combines global coverage deviation and local structure deviation.

1. **Global coverage mismatch**

   ```txt
   DeltaS_add_global(m) =
     | GoldbachCoverage(m) - GoldbachCoverageExp(m) | .
   ```

2. **Local coverage structure**

   For each window `W_k` we fix a deterministic partition into a finite number of contiguous even integer subwindows:

   ```txt
   W_k = union over b = 1..B of W_{k,b}
   ```

   where each `W_{k,b}` is a block of consecutive even integers. The integer `B` and the partition rule (for example, equal length on the logarithmic scale) are fixed at the encoding level and do not depend on data.

   For a state `m` with `k = k(m)`, the same partition defines subwindows

   ```txt
   W_b(m) = W_{k(m), b}  for b = 1,...,B .
   ```

   For each block `b` we define local empirical fractions:

   ```txt
   h0(m; b) = fraction of N in W_b(m) with r_2(N; m) = 0
   h1(m; b) = fraction of N in W_b(m) with r_2(N; m) = 1
   ```

   Using the model `D_0`, we also define expected local fractions:

   ```txt
   h0_exp(m; b) = model based fraction of N in W_b(m) with r_2(N) = 0
   h1_exp(m; b) = model based fraction of N in W_b(m) with r_2(N) = 1
   ```

   from the same Hardy–Littlewood style heuristics used to construct `GoldbachMultExp`.

   We collect these into vectors:

   ```txt
   H_local(m)      = [ h0(m;1), h1(m;1), ..., h0(m;B), h1(m;B) ] in R^{2B}
   H_local_exp(m)  = [ h0_exp(m;1), h1_exp(m;1), ..., h0_exp(m;B), h1_exp(m;B) ] in R^{2B} .
   ```

3. **Local coverage mismatch**

   We define

   ```txt
   DeltaS_add_local(m) =
     distance_local( H_local(m), H_local_exp(m) ) >= 0
   ```

   where `distance_local` is a fixed nonnegative function, for example an `L2` distance between the two vectors. The choice of `distance_local` is frozen at the encoding level and not tuned based on data.

4. **Combined additive mismatch**

   We choose fixed weights

   ```txt
   c_cov > 0,  c_loc > 0,  c_cov + c_loc = 1
   ```

   and define the additive mismatch

   ```txt
   DeltaS_add(m) =
       c_cov * DeltaS_add_global(m)
     + c_loc * DeltaS_add_local(m) .
   ```

All quantities above are treated as dimensionless or normalized according to the TU tension scale conventions.

### 3.6 Multiplicity mismatch

We define the multiplicity mismatch using the 7 dimensional profile.

Let

```txt
M_emp(m)   = MultProfile(m)          in R^7
M_model(m) = GoldbachMultExp(m)      in R^7 .
```

We fix a norm on `R^7`, for example the Euclidean norm, and define

```txt
DeltaS_mult(m) =
  distance_mult( M_emp(m), M_model(m) ) >= 0
```

where `distance_mult` is a fixed nonnegative function (for example the `L2` norm). This function is chosen once for Q006 and not adjusted by data.

### 3.7 Combined Goldbach mismatch

We choose fixed weights

```txt
a_add  > 0
a_mult > 0
a_add + a_mult = 1
```

and define the combined Goldbach mismatch

```txt
DeltaS_GC(m) =
    a_add  * DeltaS_add(m)
  + a_mult * DeltaS_mult(m) .
```

This quantity is nonnegative and is treated as a dimensionless or normalized score.

### 3.8 Effective tension tensor component

In line with the TU core decision, we define an effective tension tensor component over `M`:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_GC(m) * lambda(m) * kappa_GC
```

where:

* `S_i(m)` is a source factor describing how strongly component `i` is driven by Goldbach related claims in the configuration `m` (for example, how strongly the context insists on full coverage of even integers).
* `C_j(m)` is a receptivity factor describing how sensitive component `j` is to deviations from Goldbach like behaviour (for example, how much a given reasoning path depends on additive prime structure).
* `DeltaS_GC(m)` is the combined Goldbach mismatch defined above.
* `lambda(m)` is the convergence state factor from the TU core, taking values in a fixed range that encodes whether local reasoning is convergent, recursive, divergent, or chaotic.
* `kappa_GC` is a fixed coupling constant setting the overall scale of Goldbach related consistency_tension.

Here `lambda(m)` and `kappa_GC` are treated as opaque TU core parameters; their construction and evolution are not specified in this file.

The indexing sets for `i` and `j` are not specified. It is sufficient that, for each `m` in the regular domain, `T_ij(m)` is finite and well defined.

### 3.9 Singular set and regular domain

Some states may encode incomplete or inconsistent data, or values outside the domain of the observables above. We collect these into a singular set:

```txt
S_sing = { m in M :
           GoldbachCoverage(m) is undefined
           or MultProfile(m) is undefined
           or DeltaS_GC(m) is not finite }
```

We restrict all Goldbach tension analysis to the regular domain

```txt
M_reg = M \ S_sing .
```

When an experiment or protocol would require evaluating `DeltaS_GC(m)` for `m` in `S_sing`, the result is treated as “out of domain” and does not count as evidence for or against Goldbach’s conjecture.

---

## 4. Tension principle for this problem

This block states how Q006 is treated as a tension problem within TU at the effective layer.

### 4.1 Core tension functional with alarm behaviour

We define an explicit Goldbach tension functional:

```txt
Tension_GC(m) =
    b_add  * DeltaS_add(m)
  + b_mult * DeltaS_mult(m)
  + b_hole * HoleIndicator(m)
```

with fixed weights

```txt
b_add  > 0
b_mult > 0
b_hole > 0
b_add + b_mult + b_hole = 1 .
```

The alarm first semantics for Goldbach are:

* `b_hole` is chosen to dominate the scale of `Tension_GC(m)` whenever a coverage hole is present. In practice this means that any state with `HoleIndicator(m) = 1` is treated as high tension, independently of how small `DeltaS_add(m)` and `DeltaS_mult(m)` might otherwise be.

The `HoleIndicator` is defined as:

```txt
HoleIndicator(m) = 0
    if every even N in W(m) has r_2(N; m) >= 1

HoleIndicator(m) = 1
    otherwise .
```

Then:

* `Tension_GC(m) >= 0` for all `m` in `M_reg`.
* `Tension_GC(m)` is small when both coverage and multiplicity mismatch are small and there are no uncovered even integers.
* `Tension_GC(m)` is large when coverage gaps or extreme multiplicity anomalies occur, and in particular any uncovered even integer forces a high tension state by design.

### 4.2 Goldbach as a low tension principle

At the effective layer, Goldbach’s conjecture is encoded as the claim that, for sufficiently refined windows in the fixed library, the real universe admits low tension, hole free representations.

More concretely:

* For each `k` in `K_stage1` above some threshold `k_crit`, there should exist states

  ```txt
  m_T(k) in M_reg
  ```

  that encode the actual universe on `W_k` such that:

  ```txt
  HoleIndicator(m_T(k)) = 0
  Tension_GC(m_T(k))    <= epsilon_GC(k)
  ```

  for a family of thresholds `epsilon_GC(k)` with the following properties:

  * Each `epsilon_GC(k)` is chosen in advance based on theoretical expectations and uncertainties for that scale, not tuned to fit observed mismatches.
  * All `epsilon_GC(k)` are interpreted relative to the global TU tension scale and do not change if the scale is reparametrized.
  * The sequence `epsilon_GC(k)` does not grow without bound along the refinement order; for example it may stay bounded or slowly decrease.

### 4.3 Goldbach failure as persistent high tension

If Goldbach’s conjecture is false, then for any encoding in the admissible class described above, world representing states inevitably exhibit persistent high tension along an infinite subsequence of windows.

Formally, there would exist a lower bound `delta_GC > 0` and an infinite subsequence of indices `k` in `K_stage1` such that, for all states

```txt
m_F(k) in M_reg
```

that accurately encode the real world on `W_k`, one has:

```txt
HoleIndicator(m_F(k)) = 1
Tension_GC(m_F(k))    >= delta_GC .
```

In this case, the low tension band defined by the thresholds `epsilon_GC(k)` would never be consistently reached for all large windows.

Thus, at the effective layer, Q006 is the claim that our universe belongs to the low tension branch rather than the persistent high tension branch, relative to the fixed finite encoding library and tension definition.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds, both at the effective layer and both expressed only in terms of observables and tension functionals.

* World T: Goldbach true, globally low discrete tension.
* World F: Goldbach false, persistent high discrete tension.

These worlds are templates for tension patterns and do not assert any deep ontological claim about the universe.

### 5.1 World T (Goldbach true, low discrete tension)

In World T:

1. **Complete coverage**

   For every window index `k` above some `k_crit`, the world representing state `m_T(k)` satisfies

   ```txt
   GoldbachCoverage(m_T(k)) = 1
   HoleIndicator(m_T(k))    = 0 .
   ```

2. **Stable multiplicity statistics**

   For all such windows, the multiplicity mismatch remains small:

   ```txt
   DeltaS_mult(m_T(k)) <= epsilon_mult(k)
   ```

   where `epsilon_mult(k)` is a pre chosen tolerance that does not blow up along the refinement order.

3. **Bounded total tension**

   The overall Goldbach tension satisfies

   ```txt
   Tension_GC(m_T(k)) <= epsilon_GC(k)
   ```

   for all sufficiently large `k` in `K_stage1`, with `epsilon_GC(k)` defined as in Block 4.

4. **Refinement stability**

   As windows refine via `refine(k) = k + 1`, the tension values `Tension_GC(m_T(k))` remain in a low band and do not display unmotivated spikes caused by the encoding itself.

### 5.2 World F (Goldbach false, persistent high tension)

In World F:

1. **Structural coverage gaps**

   There exists an infinite subsequence of window indices `k` and corresponding states `m_F(k)` representing the real world on `W_k` such that

   ```txt
   GoldbachCoverage(m_F(k)) < 1
   HoleIndicator(m_F(k))    = 1 .
   ```

   These gaps are not localized early anomalies but appear at arbitrarily large scales.

2. **Unremovable mismatch**

   Even within the fixed density model and finite library, windows with coverage gaps cannot be reinterpreted as low tension states. For all admissible modelling choices attached to such windows, the combined mismatch remains bounded away from zero.

3. **Persistent high tension**

   There is a fixed `delta_GC > 0` such that

   ```txt
   Tension_GC(m_F(k)) >= delta_GC
   ```

   for all large `k` in the subsequence.

4. **Refinement behaviour**

   Refining windows does not wash out the tension. As `k` increases along the subsequence, high tension persists instead of relaxing into the low band defined in World T.

### 5.3 Interpretive note

These worlds do not claim any method to construct internal TU fields from raw data. They only assert that, if there exist effective models of our universe that respect the encoding constraints, then the pattern of Goldbach tension across window scales must qualitatively match one of these two scenarios.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments at the effective layer that can:

* falsify specific choices of the Q006 tension encoding,
* test robustness of the encoding against synthetic and real data,
* distinguish between tension patterns expected in World T and World F models.

They do not prove or disprove Goldbach’s conjecture itself.

### Experiment 1: Finite window numerical tension profile

**Goal**

Test whether the chosen `Tension_GC` functional produces stable, nontrivial tension profiles on real Goldbach data and can distinguish windows with and without coverage holes.

**Setup**

* Choose an upper bound `N_max` up to which Goldbach representations `r_2(N)` have been computed or can be computed.
* Select indices `k` in `K_stage1` such that `W_k` is contained in `[4, N_max]`.
* For each such `k`, construct a state `m_real(k)` encoding:

  * the actual coverage of even integers in `W_k`,
  * the multiplicity `r_2(N)` for all even `N` in `W_k`.
* Construct synthetic “holey” windows by removing all representations for a small set of even integers in selected windows, producing states `m_hole(k)` with artificially induced gaps.

**Protocol**

For each admissible `k`:

1. For the real world state `m_real(k)` evaluate

   ```txt
   GoldbachCoverage(m_real(k))
   DeltaS_add(m_real(k))
   DeltaS_mult(m_real(k))
   Tension_GC(m_real(k))
   HoleIndicator(m_real(k))
   ```

2. For each synthetic state `m_hole(k)` evaluate the same observables and tension.

3. Compare the distributions of `Tension_GC` values for real and synthetic states across all tested windows.

**Metrics**

* For each `k`, the values:

  ```txt
  GoldbachCoverage(m_real(k)),
  DeltaS_add(m_real(k)),
  DeltaS_mult(m_real(k)),
  Tension_GC(m_real(k)),
  HoleIndicator(m_real(k)) .
  ```

* For each `k`, the values:

  ```txt
  GoldbachCoverage(m_hole(k)),
  DeltaS_add(m_hole(k)),
  DeltaS_mult(m_hole(k)),
  Tension_GC(m_hole(k)),
  HoleIndicator(m_hole(k)) .
  ```

* Separation of `Tension_GC` values between real and synthetic windows. For example:

  ```txt
  min_k ( Tension_GC(m_hole(k)) - Tension_GC(m_real(k)) ) .
  ```

* Stability of `Tension_GC(m_real(k))` as `k` varies within the tested range.

**Falsification conditions**

* If for many windows `Tension_GC(m_hole(k))` lies in the same numeric band as `Tension_GC(m_real(k))`, so that windows with large artificial gaps cannot be distinguished from real windows, the encoding is considered inadequate and rejected.
* If small changes to the pre chosen weights `b_add`, `b_mult`, `b_hole` or to the density model internals cause arbitrary flips in which windows appear low tension or high tension, without clear mathematical reasons, then the encoding is considered unstable and must be revised.

**Encoding implementation note**

This experiment only assumes that the state `m` can be evaluated through the observables in Block 3. It does not depend on any particular method of constructing `m` from raw prime tables and does not expose any deeper TU generative mechanism.

**Boundary note**

Falsifying a TU encoding is not the same as solving the canonical Goldbach conjecture.

---

### Experiment 2: Model world comparison for Goldbach like sequences

**Goal**

Assess whether the Q006 tension encoding can consistently distinguish between synthetic sequences that satisfy Goldbach like coverage and sequences with structured coverage gaps.

**Setup**

* Construct or select two families of synthetic model worlds over the same window scales:

  * Family T models: for each even integer `N` in the window, at least one admissible representation is provided, possibly generated by a random mechanism that mimics known Goldbach heuristics.
  * Family F models: for each window, a small but structured set of even integers is assigned zero representations, while other integers behave similarly to Family T.
* For each model world and window index `k`, construct a state `m_T_model(k)` or `m_F_model(k)` in `M_reg` that encodes:

  * coverage of the window,
  * multiplicity summaries, following the same observable definitions as in Block 3.

**Protocol**

For each model world state, compute:

```txt
GoldbachCoverage(m_T_model(k)) or GoldbachCoverage(m_F_model(k))
DeltaS_add(m_T_model(k))      or DeltaS_add(m_F_model(k))
DeltaS_mult(m_T_model(k))     or DeltaS_mult(m_F_model(k))
Tension_GC(m_T_model(k))      or Tension_GC(m_F_model(k))
HoleIndicator(m_T_model(k))   or HoleIndicator(m_F_model(k))
```

Aggregate tension values over all `k` and over all models in each family.

**Metrics**

* Mean and variance of `Tension_GC` over Family T and Family F.
* A separation measure, for example the difference between mean values of `Tension_GC` in the two families.
* Sensitivity of this separation to the particular choice of `b_add`, `b_mult`, `b_hole` when those choices remain within the admissible encoding class.

**Falsification conditions**

* If, under admissible choices of the encoding parameters, the distributions of `Tension_GC` for Family T and Family F cannot be separated in a consistent way, then the encoding is considered non discriminating and rejected.
* If some members of Family F (with explicit coverage gaps) systematically receive lower tension than typical members of Family T, the encoding is considered misaligned with the intended consistency_tension semantics and must be revised.

**Encoding implementation note**

The construction of synthetic model worlds is external to TU. At the TU level, only the aggregate observables and tension values are used, and no assumptions are made about the internal mechanism that generated the synthetic data.

**Boundary note**

Falsifying a TU encoding is not the same as solving the canonical Goldbach conjecture.

---

## 7. AI and WFGY engineering spec

This block describes how Q006 can be used as a module in AI and WFGY systems at the effective layer.

### 7.1 Training signals

We list several training signals that use Q006 observables and tension.

1. `signal_goldbach_coverage_band`

   * Definition: a penalty signal proportional to

     ```txt
     | GoldbachCoverage(m) - GoldbachCoverageExp(m) |
     ```

     whenever the context assumes Goldbach like behaviour on window `W(m)`.

   * Purpose: push internal representations toward windows where observed coverage ratios match the expected ones whenever that is part of the task assumptions.

2. `signal_goldbach_multiplicity_shape`

   * Definition: a signal based on `DeltaS_mult(m)`, possibly rescaled, applied in contexts where the model is asked to reason about the typical number of representations of even integers.

   * Purpose: encourage the model to learn multiplicity patterns that are compatible with standard analytic number theory heuristics.

3. `signal_goldbach_tension_scalar`

   * Definition: directly equal to `Tension_GC(m)` when the model encodes a state `m` for a given window.

   * Purpose: act as a single scalar regularizer that discourages high tension states when solving problems that assume Goldbach like behaviour.

4. `signal_world_T_vs_world_F_consistency`

   * Definition: a pair of signals comparing the model’s outputs under world T style prompts (assuming Goldbach) and world F style prompts (negating or questioning Goldbach), together with the corresponding tensions.

   * Purpose: ensure that the model cleanly separates the two assumptions and maintains internal consistency in each world, instead of mixing them.

### 7.2 Architectural patterns

We describe module patterns that can reuse Q006 structures without revealing any deeper TU construction.

1. `EvenWindowField`

   * Role: a module that maps internal task representations into discrete windows `W_k` over the even integers, together with an index `k` and the associated density model handle.

   * Interface:

     * Input: internal embeddings of a number theory context and a scale hint.
     * Output: a discrete window index `k`, a representation of `W_k`, and a handle for the associated density model `D_0`.

2. `PrimePairScanner`

   * Role: a module that produces or retrieves candidate prime pairs `(p_1, p_2)` for a given even `N` in a window.

   * Interface:

     * Input: internal representations plus an even integer `N`.
     * Output: a list or summary of candidate prime pairs used to compute `GoldbachMultiplicity(m; N)`.

3. `TU_DiscreteTensionHead_GC`

   * Role: a tension head that, given window level summaries, outputs `Tension_GC(m)` and its components.

   * Interface:

     * Input: coverage ratio, multiplicity summary vector, expected coverage, expected multiplicity summary.
     * Output: `DeltaS_add(m)`, `DeltaS_mult(m)`, `Tension_GC(m)`.

### 7.3 Evaluation harness

We outline an evaluation harness to compare baseline AI systems and TU augmented systems on Goldbach related reasoning tasks.

1. **Task design**

   Construct a benchmark of tasks that include:

   * explaining Goldbach’s conjecture and known partial results,
   * reasoning about hypothetical coverage gaps,
   * extrapolating multiplicity patterns,
   * comparing windows with known coverage versus synthetic windows with removed representations.

2. **Conditions**

   * Baseline condition: the model answers tasks without any explicit tension based modules.
   * TU condition: the model uses `EvenWindowField`, `PrimePairScanner`, and `TU_DiscreteTensionHead_GC` to maintain and report Goldbach tension during reasoning.

3. **Metrics**

   * Task accuracy on factual questions about Goldbach and related results.
   * Internal consistency when prompted with world T and world F assumptions.
   * Correlation between reported `Tension_GC` and the presence or absence of coverage gaps in synthetic tasks.

### 7.4 60 second reproduction protocol

A simple protocol for external users:

* **Baseline setup**

  * Prompt: ask an AI system to explain Goldbach’s conjecture, its status, and why “almost all even integers” results are not yet a full proof.
  * Observation: identify whether the explanation correctly distinguishes between full coverage and almost all results.

* **TU encoded setup**

  * Prompt: same as above, but add a request:
    “Structure your explanation in terms of coverage of even windows by prime pairs, multiplicity patterns, and a Goldbach tension index that is low when coverage is complete and expected multiplicities match.”
  * Observation: compare the structure and clarity of this answer with the baseline; in particular, whether the model explicitly talks about coverage ratios, multiplicity patterns, local versus global behaviour, and what it would mean for tension to stay high.

* **Comparison metric**

  * Simple rubric scoring on structure, explicit mention of coverage and tension, and clarity of what is still unknown.

* **What to log**

  * Prompts, outputs, and any `Tension_GC(m)` values or components that the system chooses to expose.

---

## 8. Cross problem transfer template

This block lists reusable components from Q006 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `GoldbachCoverage_Field`

   * Type: field

   * Minimal interface:

     ```txt
     Inputs:  even_window W, prime_pair_summary
     Output:  coverage_ratio in [0, 1]
     ```

   * Preconditions:

     * `W` is a finite set of even integers.
     * `prime_pair_summary` is sufficient to determine whether each `N` in `W` has at least one prime pair representation.

2. ComponentName: `GoldbachMultiplicity_Profile`

   * Type: observable

   * Minimal interface:

     ```txt
     Inputs:  even_window W, prime_pair_summary
     Output: multiplicity_summary_vector in R^7
     ```

   * Preconditions:

     * For each `N` in `W`, the number of representations is well defined and finite.
     * The summary vector is constructed using the fixed 7 dimensional rule from Section 3.3.3.

3. ComponentName: `Tension_GC_Functional`

   * Type: functional

   * Minimal interface:

     ```txt
     Inputs:  coverage_ratio,
              multiplicity_summary_vector,
              expected_coverage,
              expected_multiplicity_summary
     Output: tension_scalar >= 0
     ```

   * Preconditions:

     * Expected values come from a model in the admissible density library.
     * Weights `b_add`, `b_mult`, `b_hole` are those fixed for Q006.

### 8.2 Direct reuse targets

1. Q007 (BH_MATH_TWINPRIME_L3_007 · Twin prime conjecture)

   * Reused component: `GoldbachCoverage_Field`, `GoldbachMultiplicity_Profile`.
   * Why it transfers: twin prime problems also consider pairs of primes in a discrete window. The same field and multiplicity machinery can be reused by changing the definition of admissible pairs from “sum equals N” to “difference equals 2”.
   * What changes: the window and pair definition change, but the way coverage and multiplicity are summarized remains the same.

2. Q009 (BH_MATH_NONLINEAR_PRIMEPATTERN_L3_009 · Nonlinear prime patterns)

   * Reused component: `Tension_GC_Functional` as a template.
   * Why it transfers: Q009 studies more complex prime patterns, but still needs to compare observed coverage and multiplicity with expectations from model distributions.
   * What changes: observables now report patterns for polynomial or other nonlinear relations, while the functional form of coverage and multiplicity based tension is adapted but conceptually inherited from Q006.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* **E_level: E2**

  * An explicit discrete encoding of Goldbach in terms of coverage, local structure, multiplicity, and a finite encoding library has been specified.
  * Tension functionals and singular sets are clearly defined at the effective layer, with alarm first semantics for coverage holes.

* **N_level: N2**

  * World T and World F scenarios are clearly described in terms of tension patterns.
  * Cross problem links and reuse targets are identified.

### 9.2 Next measurable step toward E3: Goldbach window tension harness

To move from E2 to E3, Q006 needs a concrete, reproducible tension harness that can be implemented and independently re run. A minimal E3 oriented roadmap is:

1. **Spec and freeze phase**

   * Publish a machine readable specification that fixes:

     * the index set `K_stage1` and the concrete windows `W_k`,
     * the subwindow partition rule and block count `B`,
     * the exact Hardy–Littlewood style model used as `D_0`,
     * the precise formulas for `GoldbachCoverageExp(k)` and `GoldbachMultExp(k)`,
     * the definitions of `MultProfile(m)`, `DeltaS_add_global`, `DeltaS_add_local`, `DeltaS_mult`, `DeltaS_GC`,
     * the numeric choices of weights `a_add`, `a_mult`, `b_add`, `b_mult`, `b_hole`, `c_cov`, `c_loc`,
     * the chosen norms `distance_local` and `distance_mult`.
   * This spec is treated as the frozen encoding for Q006, with a version tag and a hash. Any later change is recorded as a new encoding version, not a silent update.

2. **Implementation and publication phase**

   * Provide an open source implementation that, given prime tables and `r_2(N)` values up to `N_max`, constructs for multiple window scales `k`:

     ```txt
     GoldbachCoverage(m_real(k))
     MultProfile(m_real(k))
     DeltaS_add(m_real(k))
     DeltaS_mult(m_real(k))
     Tension_GC(m_real(k))
     HoleIndicator(m_real(k))
     ```

   * Publish:

     * the code,
     * the input prime data range,
     * the resulting tension profiles over `K_stage1`,
     * any synthetic model world results used for Experiment 2.

3. **Independent reproduction phase**

   * A separate group re implements the harness using the published spec and independent prime data.
   * They reproduce:

     * the main tension sequences `Tension_GC(m_real(k))`,
     * the qualitative separation between real and synthetic “holey” windows.
   * Cross check that all numbers and behaviours fall within the stated tolerances, or else identify concrete discrepancies.

Achieving these three phases, without loosening any of the effective layer constraints, would justify raising Q006 to `E3` while keeping `N2` or higher.

### 9.3 Long term role in the TU program

In the broader Tension Universe program, Q006 is expected to serve as:

* the canonical discrete testbed for consistency_tension on the integer line,
* a bridge between purely spectral problems (like Q001) and more directly combinatorial problems (like Q007 and Q009),
* a calibration point for how discrete tension encodings behave when pushed to extremely hard open problems, and for how AI systems can use such encodings to reason about additive number theory without claiming proofs.

---

## 10. Elementary but precise explanation

This block gives an explanation aimed at non specialists, while remaining faithful to the effective layer description.

The classical Goldbach conjecture says:

> Every even number `N >= 4` can be written as the sum of two prime numbers.

For example:

```txt
4  = 2 + 2
6  = 3 + 3
8  = 3 + 5
10 = 5 + 5 or 3 + 7
```

There are two natural questions one can ask.

1. For a given even number `N`, is there at least one way to write it as a sum of two primes?
2. If we look at many even numbers in a row, how many such representations do we usually see, and how are they distributed?

In the Tension Universe view, we do not try to prove or disprove Goldbach directly. Instead we proceed in several steps.

* First, we choose a **window** of even numbers, for example all even `N` between `2^k` and `2^(k+1)`.
* For each even `N` in that window we look at how many ordered pairs of primes `(p_1, p_2)` satisfy `p_1 + p_2 = N`. This number is called `r_2(N)` in this file.
* From this we build:

  * a **coverage ratio** between `0` and `1`, telling us what fraction of even numbers in the window actually have at least one representation,
  * a **multiplicity profile** that summarizes how many representations a typical even number has, using averages, percentiles, and the fraction with `0` or `1` representation.

Next, using standard prime number theory heuristics, we build a **theoretical model** that predicts:

* what the coverage ratio should look like in that window,
* what the multiplicity profile should look like in that window.

We then compare:

* the actual coverage ratio with the expected coverage ratio,
* the actual multiplicity profile with the expected multiplicity profile,
* whether there are any even numbers in the window that have no representations at all.

From these comparisons we build a **Goldbach tension number**:

* It is small when coverage is complete and the multiplicity statistics look as expected.
* It is large when coverage gaps appear or when the multiplicity pattern looks very different from what the model suggests.
* By design, if there is even a single even number in the window with no representation, the tension immediately jumps into a high band.

Finally we imagine two kinds of worlds.

* In a **Goldbach true world**, every sufficiently large even number can be written as a sum of two primes. As we slide our windows to larger and larger numbers, the coverage is always complete and the Goldbach tension stays in a low band.
* In a **Goldbach false world**, there are infinitely many windows where at least one even number has no representation. In those windows the Goldbach tension is forced to be high and never relaxes into the low band.

This framework does not tell us which world we live in and does not provide a proof. What it does provide is:

* a clear way to describe what we can observe about Goldbach behaviour in finite ranges,
* a precise notion of what low tension and high tension mean in this context,
* a reusable template that can be applied to other discrete prime pattern problems.

Q006 is thus the canonical example of how Tension Universe encodes a famous unsolved problem on the integers using coverage, local structure, multiplicity, and a controlled notion of discrete tension, while staying strictly at the effective layer.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective layer boundary

* All objects used here (state spaces `M`, observables, invariants, mismatch scores, tension functionals, counterfactual “worlds”) live at the effective layer.
* No step in this file gives a constructive mapping from raw experimental, numerical, or simulation data into internal TU fields.
* No step exposes any deep TU generative rule or any first principle axiom system.
* Counterfactual World T and World F descriptions are narrative devices for tension patterns, not ontological claims about the universe.

### Encoding and fairness

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

For every encoding class referenced here:

* its definition, parameter ranges, and reference families are fixed at the charter level before any problem specific tuning;
* these choices may depend on general physical or mathematical considerations and on public benchmark selections, but not on the unknown truth value of this specific problem;
* no encoding is allowed to hide the canonical answer as an uninterpreted field, label, or parameter.

### Tension scale and thresholds

* All mismatch terms `DeltaS_*` and tension functionals in this file are treated as dimensionless or normalized quantities, defined up to a fixed monotone rescaling specified in the TU Tension Scale Charter.
* Thresholds such as `epsilon_*`, `delta_*` and experiment cutoffs are always interpreted relative to that fixed scale.
* Changing the tension scale requires an explicit update of the TU Tension Scale Charter, not an edit of individual problem files.

### Falsifiability and experiments

* Experiments described in this document are tests of TU encodings, not tests of the underlying canonical problem itself.
* The rule “falsifying a TU encoding is not the same as solving the canonical statement” is understood to apply globally, even where it is not restated.
* When required observables cannot be reliably estimated in practice, the outcome of the corresponding experiment is recorded as “inconclusive”, not as confirmation.

### Interaction with established results

* All encodings and counterfactual worlds described here are required to respect known theorems and hard constraints in the relevant field.
* If a later analysis finds a concrete conflict with established results, the correct procedure is to update or retire the encoding under the TU charters, not to reinterpret those results.
* Canonical mathematical statements in Section 1 always take precedence over any narrative or heuristic commentary in later sections.

### Versioning and program note

* This page is an experimental specification within the ongoing **WFGY / Tension Universe** research program.
* All structures and parameter choices are provisional and may be revised in future versions, subject to the constraints above.
* Substantial changes to windows, models, or weights should be recorded as new encoding versions with explicit version tags and hashes, to preserve reproducibility and cross problem consistency.
