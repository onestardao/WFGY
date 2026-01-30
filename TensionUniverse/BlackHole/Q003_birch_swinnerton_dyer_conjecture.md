# Q003 · Birch and Swinnerton-Dyer Conjecture

## 0. Header metadata

```txt
ID: Q003
Code: BH_MATH_BSD_L3_003
Domain: Mathematics
Family: Number theory (elliptic curves, L-functions)
Rank: S
Projection_dominance: I
Field_type: analytic_field
Tension_type: spectral_tension
Status: Open
Semantics: hybrid
E_level: E2
N_level: N2
Last_updated: 2026-01-30
```

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* We only describe state spaces, observables, mismatch measures, tension functionals, singular sets, falsifiable experiments, and cross-node consistency conditions.
* We do not specify any TU axioms, deep generative rules, or constructive derivations.
* We do not give any explicit mapping from raw numerical or algebraic data to internal TU fields.
* We treat all effective quantities as already encoded inside admissible TU states, without explaining how those states are constructed.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Let `E` be an elliptic curve over the rational field `Q`.

The analytic side uses the Hasse–Weil L-function `L(E, s)`, defined initially by an Euler product and a Dirichlet series in a right half plane, then extended to a meromorphic function on the complex plane.

Define the analytic rank

```txt
rank_an(E) = order of vanishing of L(E, s) at s = 1
```

The algebraic side uses the Mordell–Weil group `E(Q)` of rational points on `E`.

Define the algebraic rank

```txt
rank_alg(E) = rank of the abelian group E(Q)
```

The Birch and Swinnerton-Dyer Conjecture (BSD) has two closely related parts.

1. Rank equality

   ```txt
   rank_an(E) = rank_alg(E)
   ```

   for every elliptic curve `E` over `Q`.

2. Leading term formula

   Let `r = rank_alg(E) = rank_an(E)`. Consider the leading term of `L(E, s)` at `s = 1`:

   ```txt
   L_star(E) = lim_{s -> 1} (L(E, s) / (s - 1)^r)
   ```

   BSD predicts that

   ```txt
   L_star(E)  =  (Reg(E) * |Sha(E)| * prod_{p} c_p(E)) /
                 (|E(Q)_tors|^2 * Omega(E))
   ```

   where:

   * `Reg(E)` is the regulator of `E(Q)`,
   * `Sha(E)` is the Tate–Shafarevich group of `E`,
   * `c_p(E)` are the local Tamagawa factors at primes `p`,
   * `E(Q)_tors` is the torsion subgroup of `E(Q)`,
   * `Omega(E)` is a real period factor.

All of these objects are defined in standard arithmetic geometry. In this TU document they are treated as external mathematical entities that feed into effective observables.

### 1.2 Status and difficulty

BSD is a central open problem in number theory and arithmetic geometry.

* The rank equality part is known in many special cases. For example, for elliptic curves of analytic rank zero or one over `Q` there are deep results that prove the equality under additional hypotheses.
* The full conjecture for all elliptic curves over `Q` remains open.
* The leading term formula is known in many cases under modularity and other hypotheses, with significant partial progress for special families of curves.
* BSD is strongly connected to the theory of modular forms, Galois representations, Iwasawa theory, and the structure of `Sha(E)`.

BSD appears in standard lists of fundamental unsolved problems and is widely considered a benchmark S-level problem in modern mathematics.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q003 plays several roles.

1. It is the flagship example of a problem that couples

   * a spectral side (families of elliptic curve L-functions and their behaviour at `s = 1`), and
   * an arithmetic side (ranks, regulators, Tate–Shafarevich groups, and related invariants).

2. It extends the spectral_tension ideas from Q001 (Riemann Hypothesis) and Q002 (Generalized Riemann Hypothesis) into a mixed discrete and continuous setting.

3. It provides a test bed for TU encodings where

   * families of objects `E_BSD(k)` are selected by explicit external criteria,
   * mismatch measures between analytic and algebraic data are averaged over these families,
   * fairness rules and fixed weights prevent hidden parameter tuning or data selection by tension.

BSD is therefore the canonical S-level example of a spectral_tension problem where arithmetic geometry enters explicitly.

### References

1. Clay Mathematics Institute, “The Birch and Swinnerton-Dyer Conjecture”, official problem description, Millennium Prize Problems, 2000.
2. J. W. S. Cassels and A. Fröhlich (editors), “Algebraic Number Theory”, Academic Press, 1967, especially the chapter on elliptic curves and L-functions.
3. J. H. Silverman, “The Arithmetic of Elliptic Curves”, Graduate Texts in Mathematics 106, Springer, 1986 (second edition 2009).
4. B. Mazur, “Modular curves and the Eisenstein ideal”, Publications Mathématiques de l’IHÉS 47 (1977), 33–186.

---

## 2. Position in the BlackHole graph

This block records Q003 as a node in the BlackHole graph and describes its edges to other S-level problems.

### 2.1 Upstream problems

These nodes provide prerequisites or effective tools for Q003.

* Q001 (BH_MATH_NUM_L3_001, Riemann Hypothesis)
  Reason: Supplies the prototype spectral_tension encoding for a single L-function and its zeros, which is reused conceptually for `L(E, s)`.

* Q002 (BH_MATH_GRH_L3_002, Generalized Riemann Hypothesis)
  Reason: Provides the family-level spectral_tension framework for L-functions that underlies analytic parts of BSD.

* Q016 (BH_MATH_ZFC_CH_L3_016, set theory and continuum structure)
  Reason: Ensures a coherent background for real valued invariants, measure-theoretic bounds, and family indexing needed in the BSD encoding.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019, distribution of rational points)
  Reason: Encodes general tension patterns between Diophantine sets and density statements, which BSD refines in the elliptic curve case.

### 2.2 Downstream problems

These nodes directly reuse Q003 components or depend on its tension structure.

* Q015 (BH_MATH_RANK_BOUNDS_L3_015, uniform rank bounds)
  Reason: Uses the BSD family mismatch functional to constrain possible distributions of ranks across elliptic curve families.

* Q020 (BH_MATH_RATIONAL_POINT_DISTRIB_L3_020, rational point distribution on curves)
  Reason: Extends the BSD style coupling of analytic data and arithmetic data to higher genus curves and more general Diophantine sets.

* Q123 (BH_AI_INTERP_L3_123, AI interpretability and spectral structure)
  Reason: Reuses the idea of a coupled discrete rank and continuous spectral descriptor as an analogy for internal AI representations.

### 2.3 Parallel problems

Parallel nodes share closely related tension types, but there is no direct component dependence.

* Q001 (BH_MATH_NUM_L3_001, Riemann Hypothesis)
  Reason: Both Q001 and Q003 involve spectral patterns that must align with number theoretic observables, formulated as spectral_tension.

* Q002 (BH_MATH_GRH_L3_002, Generalized Riemann Hypothesis)
  Reason: Q002 and Q003 both study families of L-functions, with Q003 adding arithmetic geometry invariants to the tension picture.

* Q018 (BH_MATH_RANDOM_MATRIX_ZEROS_L3_018, zero statistics and random matrices)
  Reason: Shares the emphasis on fine spectral statistics and their comparison with model distributions.

### 2.4 Cross-domain edges

Cross-domain edges connect Q003 to non-mathematical problems that can reuse its patterns.

* Q059 (BH_CS_INFO_THERMODYN_L3_059, information and thermodynamic cost)
  Reason: Reuses the pattern of coupling a discrete structural invariant and a continuous energy-like quantity through a tension functional.

* Q080 (BH_SOC_FINANCIAL_NETWORK_L3_080, systemic risk in financial networks)
  Reason: Mirrors the idea that local structural invariants and global flows must obey a joint consistency relation similar to BSD.

* Q123 (BH_AI_INTERP_L3_123, AI interpretability and spectral structure)
  Reason: Uses BSD as a template where internal spectra and symbolic invariants must match in a constrained way.

---

## 3. Tension Universe encoding (effective layer)

This block describes the effective TU encoding of Q003. It defines state spaces, fields, mismatch measures, weights, aggregators, and singular sets, but not any deep generative rule.

All mismatch terms and tension functionals are treated as dimensionless or normalized quantities, up to a fixed monotone rescaling specified in the TU Tension Scale Charter.

### 3.1 State space and admissible families (family fairness and freeze lock)

We assume a BSD state space

```txt
M_BSD
```

Each state `m` in `M_BSD` represents a finite library of elliptic curves and their effective invariant summaries.

We introduce a family selector

```txt
E_BSD(k)
```

for integers `k >= 1`, with the following properties.

1. Each `E_BSD(k)` is a finite set of elliptic curves over `Q`.

2. Membership in `E_BSD(k)` is determined only by externally auditable conditions, such as:

   * a bound on the conductor, for example `N(E) <= N_max(k)` for a fixed increasing function `N_max(k)`,
   * the requirement that specified external data sources provide a fixed white list of fields for `E` (for example analytic rank, algebraic rank, and a minimum set of invariants),
   * simple structural conditions such as minimality and field of definition over `Q`.

3. None of the following may be used as membership criteria:

   * current or expected values of any mismatch terms,
   * current or expected values of any tension functional,
   * any function of those values.

4. Family freeze lock:

   * For each `k`, once `E_BSD(k)` is defined for a given TU encoding version, it is treated as frozen for that version.

   * For all `k`, there is a monotone extension property:

     ```txt
     E_BSD(k) subset of E_BSD(k+1)
     ```

     up to curves that enter only because `N_max(k+1)` is larger and the data white list is satisfied.

   * Curves are never removed from `E_BSD(k)` solely because they contribute large mismatch or tension.

We do not explain how curves or their invariants are computed. We only assume that for each admissible `k` there exist states `m` that encode coherent summaries for all `E` in `E_BSD(k)`.

### 3.2 Per curve observables

For each elliptic curve `E` in `E_BSD(k)` and each state `m` in `M_BSD`, we assume the existence of effective observables:

```txt
rank_an(E; m)        in {0, 1, 2, ...} union {unknown}
rank_alg(E; m)       in {0, 1, 2, ...} union {unknown}
L_star(E; m)         in R_plus union {undefined}
Reg(E; m)            in R_plus union {undefined}
Sha_size_est(E; m)   in R_plus union {unknown}
Tors_size(E; m)      in {1, 2, 3, ...} union {unknown}
C_tamagawa(E; m)     in R_plus union {unknown}
Omega(E; m)          in R_plus union {undefined}
data_quality_flags(E; m)   in a finite set of quality labels
```

Interpretation at the effective layer:

* `rank_an(E; m)` is the order of vanishing of `L(E, s)` at `s = 1`, as encoded in `m`.
* `rank_alg(E; m)` is the encoded rank of the Mordell–Weil group `E(Q)`.
* `L_star(E; m)` is the encoded leading term of `L(E, s)` at `s = 1`.
* `Reg(E; m)`, `Sha_size_est(E; m)`, `Tors_size(E; m)`, `C_tamagawa(E; m)`, and `Omega(E; m)` are the encoded versions of the corresponding arithmetic invariants.
* `data_quality_flags(E; m)` indicates which parts of the encoded data pass predefined quality checklists.

We do not specify how these quantities are obtained.

### 3.3 Data quality checklists and gating (quality lock)

To avoid using data quality as a hidden tuning knob, we require that `data_quality_flags(E; m)` be derived from explicit checklists.

At minimum, for each curve `E` in each state `m`, the following boolean fields must be defined:

```txt
q_rank_an_reliable(E; m)      in {true, false}
q_rank_alg_reliable(E; m)     in {true, false}
q_L_star_reliable(E; m)       in {true, false}
q_regulator_reliable(E; m)    in {true, false}
q_shae_est_type(E; m)         in {unknown, lower_bound, upper_bound, point_estimate}
q_torsion_reliable(E; m)      in {true, false}
q_tamagawa_reliable(E; m)     in {true, false}
q_period_reliable(E; m)       in {true, false}
q_local_data_reliable(E; m)   in {true, false}
```

Each of these is determined by a fixed checklist specified at the charter level. For example:

* numerical procedures used and their certified error bounds,
* completeness of searches for rational points,
* availability of local factor data for primes up to a fixed bound.

The following constraints hold.

* None of the `q_*` flags may depend on any mismatch term (`Delta_*`) or tension functional.
* For any `E` and `m`, if `q_X_reliable(E; m)` is `false`, then the corresponding observable is allowed to be present but is not used in mismatch computations that claim to be at E2 level.
* `data_quality_flags(E; m)` may bundle these booleans into composite quality labels, but must preserve a mapping back to the individual `q_*` flags so that exclusion from a good set can be audited.

### 3.4 Per curve mismatch measures (error model lock and local factor metric lock)

We define three primary mismatch indicators per curve.

#### 3.4.1 Rank mismatch

```txt
Delta_rank(E; m) =
  |rank_an(E; m) - rank_alg(E; m)|
```

when both `rank_an(E; m)` and `rank_alg(E; m)` are known nonnegative integers and

```txt
q_rank_an_reliable(E; m)  = true
q_rank_alg_reliable(E; m) = true
```

If either rank is marked `unknown` or the corresponding `q_*` flag is `false`, then `Delta_rank(E; m)` is treated as undefined and the curve is excluded from rank mismatch statistics.

#### 3.4.2 Leading term mismatch with capped log model

We introduce an error model constant

```txt
x_min_BSD > 0
```

fixed at the charter level and shared across all Q003 encodings.

We define an effective right hand side quantity:

```txt
BSD_rhs(E; m) =
  (Reg(E; m) * Sha_size_eff(E; m) * C_tamagawa(E; m)) /
  (Tors_size(E; m)^2 * Omega(E; m))
```

where `Sha_size_eff(E; m)` is an effective scalar derived from `Sha_size_est(E; m)` and `q_shae_est_type(E; m)` as follows.

* If `q_shae_est_type(E; m) = point_estimate`, then `Sha_size_eff(E; m)` is that estimate.
* If `q_shae_est_type(E; m)` is `lower_bound` or `upper_bound`, then `Sha_size_eff(E; m)` is defined by a fixed rule (for example mid point in log scale) specified in the charters.
* If `q_shae_est_type(E; m) = unknown`, then `Sha_size_eff(E; m)` is treated as undefined and `E` does not contribute to leading term mismatch statistics.

We require that `Reg(E; m)`, `Tors_size(E; m)`, `C_tamagawa(E; m)`, and `Omega(E; m)` be positive and have their corresponding `q_*` flags set to `true` when `BSD_rhs(E; m)` is used.

We then define a capped logarithmic mismatch

```txt
Delta_value(E; m) =
  |log(max(L_star(E; m),  x_min_BSD)) -
   log(max(BSD_rhs(E; m), x_min_BSD))|
```

when

* `L_star(E; m)` is defined and `q_L_star_reliable(E; m) = true`,
* `BSD_rhs(E; m)` is defined and all relevant `q_*` flags are `true`.

If any required quantity is undefined or its reliability flag is `false`, then `Delta_value(E; m)` is treated as undefined.

This capped log model prevents arbitrarily large mismatch values that arise purely from extremely small or noisy estimates, while keeping the error model fixed and auditable.

#### 3.4.3 Local data mismatch with fixed prime window

We define for each family index `k` a prime window upper bound

```txt
P_max(k)
```

with the following properties.

* `P_max(k)` is a fixed increasing function of `k`, specified at the charter level.
* For each `k`, one has `P_max(k) >= N_max(k)` so that all primes dividing the conductor of any curve in `E_BSD(k)` lie within the window.

For each curve `E` in `E_BSD(k)` we define a deterministic prime set

```txt
P(E, k)
```

consisting of primes `p` with `p <= P_max(k)`, selected by a fixed rule that does not depend on any mismatch or tension values. For example:

* all primes `p` with `p <= P_max(k)`, possibly filtered by simple congruence conditions specified in advance.

We assume the existence of encoded local analytic and arithmetic factors for these primes, and define a per prime discrepancy

```txt
Delta_p(E; m) >= 0
```

for each `p` in `P(E, k)` whenever

```txt
q_local_data_reliable(E; m) = true
```

A minimal example is

```txt
Delta_p(E; m) =
  |log(c_p^analytic(E; m)) - log(c_p^arith(E; m))|
```

where `c_p^analytic` and `c_p^arith` are the analytic and arithmetic local factors or suitable proxies.

We then define the local mismatch

```txt
Delta_local(E; m) =
  mean over p in P(E, k) of Delta_p(E; m)
```

whenever all `Delta_p(E; m)` are defined on `P(E, k)`.

If `q_local_data_reliable(E; m) = false` or if the window `P(E, k)` contains primes without usable data, `Delta_local(E; m)` is treated as undefined.

### 3.5 Family level index sets and aggregators (robust aggregator lock)

For each `k` and each state `m` in `M_BSD`, we define the following index sets.

* `good_rank(k; m)` is the subset of `E_BSD(k)` where `Delta_rank(E; m)` is defined and all required rank reliability flags are `true`.
* `good_value(k; m)` is the subset where `Delta_value(E; m)` is defined and the required reliability flags are `true`.
* `good_local(k; m)` is the subset where `Delta_local(E; m)` is defined and `q_local_data_reliable(E; m) = true`.

Membership in these sets depends only on the observable values and the `q_*` flags, not on any function of mismatch or tension values beyond the well definedness of each `Delta_*`.

We then define per family mean and tail statistics.

For any mismatch quantity `Delta_X(E; m)` and its corresponding good index set `good_X(k; m)` we set

```txt
mean_Delta_X(m; k) =
  average over E in good_X(k; m) of Delta_X(E; m)

q90_Delta_X(m; k)  =
  90th percentile of { Delta_X(E; m) : E in good_X(k; m) }
```

when `good_X(k; m)` is non empty. If `good_X(k; m)` is empty, both quantities are treated as undefined.

We introduce a fixed tail mixing parameter

```txt
eta_tail_BSD in [0, 1)
```

specified at the charter level and shared across all Q003 encodings.

We then define combined family level mismatches

```txt
Delta_BSD_rank(m; k) =
  (1 - eta_tail_BSD) * mean_Delta_rank(m; k) +
  eta_tail_BSD       * q90_Delta_rank(m; k)

Delta_BSD_value(m; k) =
  (1 - eta_tail_BSD) * mean_Delta_value(m; k) +
  eta_tail_BSD       * q90_Delta_value(m; k)

Delta_BSD_local(m; k) =
  (1 - eta_tail_BSD) * mean_Delta_local(m; k) +
  eta_tail_BSD       * q90_Delta_local(m; k)
```

whenever the corresponding means and percentiles are defined and finite.

This mixed aggregator ensures that a small fraction of high mismatch curves cannot be completely washed out by averaging.

### 3.6 Fixed weights and combined mismatch

We fix positive weights

```txt
w_rank   > 0
w_value  > 0
w_local  > 0
w_rank + w_value + w_local = 1
```

These weights are part of the Q003 encoding and do not depend on the state `m`, the family index `k`, or any data driven tuning. They are set at the charter level for this problem and may only be changed through a documented encoding update.

We define the combined BSD mismatch

```txt
Delta_BSD(m; k) =
  w_rank  * Delta_BSD_rank(m; k)  +
  w_value * Delta_BSD_value(m; k) +
  w_local * Delta_BSD_local(m; k)
```

whenever all three terms are defined and finite.

### 3.7 Effective tension tensor and coupling constant

We assume an effective BSD tension tensor over `M_BSD`:

```txt
T_ij_BSD(m; k) =
  S_i(m; k) * C_j(m; k) * Delta_BSD(m; k) * lambda(m; k) * kappa_BSD
```

where:

* `S_i(m; k)` is a source factor describing how strongly the ith semantic or reasoning component relies on BSD couplings for the family `E_BSD(k)`.
* `C_j(m; k)` is a sensitivity factor describing how sensitive the jth downstream component is to discrepancies in BSD couplings.
* `Delta_BSD(m; k)` is the combined mismatch defined above.
* `lambda(m; k)` is a convergence state factor from the TU core, taking values in a fixed range that encodes the local reasoning regime.
* `kappa_BSD` is a fixed scaling constant for BSD related spectral_tension.

The index sets for `i` and `j` are not specified in this effective description.

### 3.8 Singular set and domain restriction

We define the BSD singular set

```txt
S_sing_BSD =
  { m in M_BSD :
      for some admissible k, at least one of
      Delta_BSD_rank(m; k),
      Delta_BSD_value(m; k),
      Delta_BSD_local(m; k),
      Delta_BSD(m; k)
      is undefined or not finite when it is required for tension evaluation }
```

The regular domain is

```txt
M_BSD_reg = M_BSD \ S_sing_BSD
```

All BSD tension analysis in this document is restricted to `M_BSD_reg`.

If an experiment or protocol would require `Delta_BSD(m; k)` but `m` lies in `S_sing_BSD`, the result is treated as “out of domain” and not as evidence for or against the canonical BSD statement.

---

## 4. Tension principle for this problem

This block expresses BSD as a tension principle at the effective layer.

### 4.1 Family level tension functional

For each `k` and for each `m` in `M_BSD_reg` where `Delta_BSD_rank(m; k)`, `Delta_BSD_value(m; k)`, and `Delta_BSD_local(m; k)` are defined, we define the BSD family tension functional

```txt
Tension_BSD(m; k) =
  alpha_BSD * Delta_BSD_rank(m; k)  +
  beta_BSD  * Delta_BSD_value(m; k) +
  gamma_BSD * Delta_BSD_local(m; k)
```

with fixed constants

```txt
alpha_BSD > 0
beta_BSD  > 0
gamma_BSD > 0
```

These constants are part of the Q003 encoding. They do not depend on `m` or `k` and are set together with `w_rank`, `w_value`, `w_local`, and `eta_tail_BSD` at the charter level.

The functional satisfies:

* `Tension_BSD(m; k) >= 0` whenever it is defined.
* `Tension_BSD(m; k)` is small when all three combined mismatches are small.
* `Tension_BSD(m; k)` grows when any of the combined mismatches grows.

### 4.2 BSD as a low tension principle

At the effective layer, BSD is encoded as the claim that the actual universe belongs to a low tension regime for BSD consistent families, as seen through this encoding.

Formally, there exists:

* a family selector `E_BSD(k)` satisfying the fairness conditions in Section 3.1,
* a sequence of states `m_true(k)` in `M_BSD_reg` that represent the actual world at resolution level `k`,
* a sequence of thresholds `epsilon_BSD(k)`,

such that

```txt
Tension_BSD(m_true(k); k) <= epsilon_BSD(k)
```

for all sufficiently large `k`, with `epsilon_BSD(k)` not growing without bound as the resolution increases.

The sequence `epsilon_BSD(k)` may depend on computational and data limitations but is not allowed to be tuned after observing tension values. Any tuning of `epsilon_BSD(k)` must be done at the encoding level before experiments, not based on post hoc inspection, and it is always interpreted as a property of the encoding, not as a law about the external universe.

### 4.3 BSD failure as persistent high tension

If BSD is false in a strong family sense, then the universe belongs to a persistent high tension regime, as seen through encodings that respect the TU charters.

More precisely, for any encoding that is

* faithful to the true analytic behaviour of `L(E, s)` at `s = 1`,
* faithful to the actual arithmetic invariants of `E`, whenever they are well defined,
* compliant with the family fairness rules, quality gating, and fixed weights described in Section 3,

there exists a positive constant `delta_BSD` and an index `k_0` such that for all `k >= k_0`:

```txt
Tension_BSD(m_false(k); k) >= delta_BSD
```

for any state `m_false(k)` in `M_BSD_reg` that accurately encodes the relevant data for `E_BSD(k)`.

### 4.4 Compatibility with GRH based encodings (cross-node consistency lock)

Q002 provides a family level spectral_tension encoding for L-functions under generalized Riemann type assumptions.

A BSD encoding as in this block is considered acceptable only if, for elliptic curve L-functions,

* whenever the Q002 encoding is in a stable low tension regime on the trivial character specialisations corresponding to `L(E, s)` for curves in `E_BSD(k)`,
* the Q003 encoding does not force unavoidable persistent high tension on the same family purely because of internal inconsistencies of the Q003 encoding.

If such a conflict appears, it is treated as evidence that the TU encodings for Q002 and Q003 are misaligned, not as evidence for or against the canonical mathematics.

At the charter level, a cross-node consistency threshold `eta_consistency_BSD` is specified. If on overlapping families one observes

```txt
Tension_BSD(m; k) - Tension_Q002(m; k) > eta_consistency_BSD
```

persistently for states that are otherwise well aligned, the Q003 encoding is flagged for revision or retirement.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds, keeping everything at the effective layer.

* World T_BSD: BSD holds in the expected family sense.
* World F_BSD: BSD fails for a significant family of elliptic curves.

These worlds are described by patterns of observables and tension, not by any deep TU construction.

### 5.1 World T_BSD (BSD true, low family tension)

In World T_BSD:

1. Rank alignment

   * For large `k`, in states `m_T(k)` representing the actual world, most curves in `E_BSD(k)` that meet quality standards satisfy

     ```txt
     Delta_rank(E; m_T(k)) = 0
     ```

   * The family combined rank mismatch `Delta_BSD_rank(m_T(k); k)` stays small and does not grow with `k`.

2. Leading term alignment

   * For curves where both sides of the leading term comparison are defined, the values of `Delta_value(E; m_T(k))` remain within a controlled band.
   * The family combined leading term mismatch `Delta_BSD_value(m_T(k); k)` remains bounded by thresholds compatible with BSD based expectations.

3. Local data alignment

   * Local factor mismatches measured by `Delta_local(E; m_T(k))` are small for most curves in the family, with occasional outliers handled by the tail component in `Delta_BSD_local`.
   * The family combined local mismatch `Delta_BSD_local(m_T(k); k)` remains stable as `k` grows.

4. Global family tension

   * As `k` increases, the combined tension satisfies

     ```txt
     Tension_BSD(m_T(k); k) <= epsilon_BSD(k)
     ```

     with `epsilon_BSD(k)` controlled as described in Section 4.2.

### 5.2 World F_BSD (BSD false, persistent family tension)

In World F_BSD:

1. Rank misalignment

   * There exists a large subfamily of curves where analytic and algebraic ranks systematically disagree in the encoded data.
   * For sufficiently large `k`, the combined rank mismatch `Delta_BSD_rank(m_F(k); k)` remains bounded away from zero.

2. Leading term misalignment

   * For a significant number of curves in `E_BSD(k)`, the difference between `log(L_star(E; m_F(k)))` and `log(BSD_rhs(E; m_F(k)))` remains large even with the capped error model.
   * The combined leading term mismatch `Delta_BSD_value(m_F(k); k)` does not drop into a low band as `k` grows.

3. Local pattern misalignment

   * Local factor discrepancies fail to reconcile with any plausible BSD style coupling, and `Delta_local(E; m_F(k))` is often large on the fixed prime window.
   * The combined local mismatch `Delta_BSD_local(m_F(k); k)` remains at a high level over the family.

4. Global family tension

   * For some fixed `delta_BSD > 0` and all sufficiently large `k`, one has

     ```txt
     Tension_BSD(m_F(k); k) >= delta_BSD
     ```

   * This high tension cannot be removed by refining data or improving numerical precision without changing the underlying world.

### 5.3 Interpretive note

These counterfactual worlds do not attempt to prove or disprove BSD. They live entirely inside the TU effective layer and are not ontological claims about reality.

They specify how a TU encoding would observe different family level patterns of rank, leading term, and local behaviour in scenarios where BSD is true or false, while staying strictly at the level of effective observables and tension.

---

## 6. Falsifiability and discriminating experiments

This block describes experiments and protocols that can falsify specific Q003 encodings. They do not solve BSD. They only test whether given choices of families, weights, and mismatch definitions behave coherently under the TU charters.

### Experiment 1: Tension profile on public elliptic curve data

Goal:
Test whether the chosen BSD mismatch measures and weights give a stable, low tension profile on standard elliptic curve data sets that are widely used in arithmetic geometry.

Setup:

* Use a public database of elliptic curves, such as curves over `Q` with conductor up to a chosen bound `N_max(k)`, for which both analytic and algebraic data are available.
* Fix an admissible `E_BSD(k)` defined by conductor bounds and data availability, without looking at tension values.
* Fix weights `w_rank`, `w_value`, `w_local`, constants `alpha_BSD`, `beta_BSD`, `gamma_BSD`, the tail parameter `eta_tail_BSD`, and the error model constant `x_min_BSD` before any statistics are computed.

Protocol:

1. Construct a state `m_data(k)` in `M_BSD_reg` that encodes the necessary observables and quality flags for all curves in `E_BSD(k)` at the given resolution, without specifying how this encoding is implemented.
2. For each curve `E` in `E_BSD(k)`, determine whether it belongs to `good_rank(k; m_data(k))`, `good_value(k; m_data(k))`, and `good_local(k; m_data(k))`.
3. Compute `mean_Delta_rank(m_data(k); k)`, `q90_Delta_rank(m_data(k); k)`, and the analogous quantities for value and local mismatches.
4. Compute `Delta_BSD_rank(m_data(k); k)`, `Delta_BSD_value(m_data(k); k)`, `Delta_BSD_local(m_data(k); k)`, and `Delta_BSD(m_data(k); k)`.
5. Compute `Tension_BSD(m_data(k); k)` using the fixed constants.
6. Repeat the procedure for several increasing values of `k` with larger conductor bounds.

Metrics:

* For each `k`, record

  * `Delta_BSD_rank(m_data(k); k)`, `Delta_BSD_value(m_data(k); k)`, `Delta_BSD_local(m_data(k); k)`, and `Tension_BSD(m_data(k); k)`,
  * the sizes of `good_rank(k; m_data(k))`, `good_value(k; m_data(k))`, and `good_local(k; m_data(k))`.

* Study the behaviour of these quantities as functions of `k`.

Falsification conditions:

* If, for all reasonable choices of fixed constants consistent with known analytic number theory bounds, the quantity `Tension_BSD(m_data(k); k)` grows rapidly with `k` and exceeds any plausible `epsilon_BSD(k)` band motivated by BSD based heuristics, then the current Q003 encoding is considered falsified at the effective layer.
* If small changes in the definitions of `Delta_rank`, `Delta_value`, or `Delta_local` result in violent, uncontrolled swings in `Tension_BSD(m_data(k); k)` without clear mathematical reasons, the encoding is considered unstable and rejected.

Semantics implementation note:
All quantities in this experiment are treated in a mixed discrete and real valued framework consistent with the hybrid setting in the metadata. The details of representation are external to TU.

Boundary note:
Falsifying a TU encoding is not the same as solving the canonical statement. This experiment can reject specific Q003 encodings, not the underlying Birch and Swinnerton-Dyer Conjecture itself.

---

### Experiment 2: Synthetic BSD consistent and BSD breaking model families

Goal:
Check whether the Q003 tension encoding can reliably distinguish between artificially constructed families that satisfy BSD type relations and families that explicitly violate them.

Setup:

* Design a model family `Family_T` of synthetic elliptic curve like objects with data tuples that satisfy exact or approximate BSD type relations at the effective level.
* Design another model family `Family_F` where the encoded ranks and leading terms are deliberately mismatched so that BSD type relations fail in a controlled way.
* For both families, construct states that play the role of `M_BSD_reg` elements, with all relevant observables and quality flags defined.

Protocol:

1. For each object in `Family_T`, construct a state `m_T_model` that encodes its rank, leading term, and arithmetic invariants with flags approximating the high quality regime.
2. For each object in `Family_F`, construct a state `m_F_model` with the mismatched data and corresponding quality flags.
3. Place the objects into synthetic families `E_BSD_T(k)` and `E_BSD_F(k)` at various scales, and compute `Delta_BSD_rank`, `Delta_BSD_value`, `Delta_BSD_local`, and `Tension_BSD` as in Section 4.
4. Compare the distribution of `Tension_BSD` for `Family_T` and `Family_F` across several choices of `k`.

Metrics:

* Mean and variance of `Tension_BSD` on `Family_T` and on `Family_F`.
* Separation between the two distributions according to a simple distance measure in the tension axis.
* Stability of this separation under moderate changes in family size and parameter ranges.

Falsification conditions:

* If the encoding cannot produce a consistent separation between `Family_T` and `Family_F` in terms of typical `Tension_BSD` values under the fixed parameter choices, then the encoding is considered ineffective for BSD style problems.
* If the encoding often assigns lower tension to obviously BSD breaking model data than to BSD consistent data, it is considered misaligned with the intended BSD principle.

Semantics implementation note:
The synthetic families are treated using the same effective observables, quality flags, and mismatch formulas as real elliptic curves, but their construction is external to TU.

Boundary note:
Falsifying a TU encoding is not the same as solving the canonical statement. This experiment only evaluates whether Q003 encodings respect the intended BSD tension patterns.

---

## 7. AI and WFGY engineering spec

This block explains how Q003 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

### 7.1 Training signals

We define training signals that can be used as auxiliary objectives in AI models.

1. `signal_BSD_rank_consistency`

   * Definition: a penalty proportional to `Delta_rank(E; m)` aggregated over curves that appear in the current context and satisfy the reliability flags.
   * Purpose: encourage internal states that do not implicitly claim rank disagreements when the context assumes BSD rank equality.

2. `signal_BSD_value_consistency`

   * Definition: a penalty based on `Delta_value(E; m)` for curves where enough data are encoded to form a leading term comparison.
   * Purpose: align internal representations with the idea that analytic and arithmetic invariants belong to a single coherent relation.

3. `signal_BSD_local_consistency`

   * Definition: a penalty derived from `Delta_local(E; m)` on the fixed prime window for curves with reliable local data.
   * Purpose: encourage internal states in which local analytic and arithmetic patterns fit together under BSD style couplings.

4. `signal_BSD_family_tension`

   * Definition: a scalar derived from `Tension_BSD(m; k)` in contexts where a whole family of elliptic curves is under discussion.
   * Purpose: guide the model to keep its global picture of BSD related families in a low tension regime when such assumptions are declared.

5. `signal_BSD_world_switch_clarity`

   * Definition: measures the change in answers when the prompt explicitly assumes a BSD true world versus a BSD false world, at the effective layer.
   * Purpose: encourage the model to keep these counterfactual regimes separate, rather than blending them into ambiguous statements.

### 7.2 Architectural patterns

We list module patterns that can reuse Q003 structures.

1. `BSD_TensionHead`

   * Role: given an internal representation of an arithmetic geometry context, outputs estimates of `Delta_BSD_rank`, `Delta_BSD_value`, `Delta_BSD_local`, and `Tension_BSD`.
   * Interface: consumes contextual embeddings and curve identifiers, returns a small vector of tension related scalars.

2. `EllipticArithmeticFilter`

   * Role: checks whether statements involving elliptic curve ranks and L-values are compatible with BSD assumptions in the current context.
   * Interface: takes candidate statements or intermediate representations, returns scores indicating suspected mismatch levels.

3. `BSD_WorldFlag_Controller`

   * Role: maintains an explicit flag indicating whether the current reasoning chain is operating under BSD assumed, BSD agnostic, or BSD denied conditions.
   * Interface: exposes this flag to other modules, which can then use it to condition their behaviour.

### 7.3 Evaluation harness

A simple evaluation harness for AI models augmented with Q003 modules:

1. Choose a benchmark of questions in arithmetic geometry involving elliptic curves where BSD plays a known conceptual role, for example:

   * explaining the relationship between ranks and L-values,
   * discussing implications of partial BSD results,
   * reasoning about hypothetical counterexamples.

2. Run the model in two conditions:

   * baseline condition, without explicit Q003 modules or signals,
   * TU condition, with Q003 related signals and heads active.

3. Compare:

   * correctness and coherence of answers,
   * consistency between answers when the prompt explicitly assumes BSD and when it explicitly denies BSD,
   * the stability of explanations about how analytic and arithmetic invariants are supposed to fit together.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience the effect of Q003 informed reasoning.

Baseline setup:

* Prompt: ask an AI system to explain what BSD says and why it connects analytic ranks and algebraic ranks, without mentioning WFGY or tension.
* Observation: note how clearly the explanation separates analytic and arithmetic sides, and whether the role of families is stated.

TU encoded setup:

* Prompt: ask the same questions, but additionally instruct the AI to structure the explanation around

  * per curve mismatches `Delta_rank`, `Delta_value`, `Delta_local`, and
  * family level tension `Tension_BSD(m; k)` in a mixed discrete and continuous setting.

* Observation: check whether the explanation becomes more systematic, explicitly connecting family behaviour, per curve invariants, and counterfactual worlds.

Comparison metric:

* Use a rubric that scores internal consistency, clarity of the analytic versus arithmetic split, and faithfulness to standard BSD formulations.
* Compare scores between the baseline and TU encoded outputs.

What to log:

* Prompts, full responses, and any Q003 related tension scores.
* Logs can be used later to verify that differences in behaviour came from the Q003 encoding and not from hidden tuning.

---

## 8. Cross problem transfer template

This block identifies reusable components produced by Q003 and records where they transfer.

### 8.1 Reusable components produced by this problem

1. ComponentName: `BSD_FamilyTension_Functional`

   * Type: functional

   * Minimal interface:

     * Inputs: a finite family of objects with per element observables analogous to `rank_an`, `rank_alg`, `L_star`, and arithmetic invariants, plus quality flags.
     * Output: a scalar `family_tension_value` derived from mixed mean and tail averages of per element mismatches.

   * Preconditions: the inputs must encode a coherent finite family and supply enough data to form defined mismatch measures and quality flags.

2. ComponentName: `EllipticCurve_ArithmeticDescriptor`

   * Type: field

   * Minimal interface:

     * Inputs: an identifier for an elliptic curve in a selected family.
     * Output: a descriptor vector containing encoded values for `rank_an`, `rank_alg`, `L_star`, regulator, torsion size, Tate–Shafarevich size estimate, Tamagawa product, period factor, and quality flags.

   * Preconditions: external mathematical data must provide these invariants or reliable approximations.

3. ComponentName: `BSD_CounterfactualWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a model class that produces elliptic curve like objects or genuine elliptic curves with both analytic and arithmetic summaries.
     * Output: two experiment scenarios, one BSD consistent and one BSD breaking, along with procedures for computing the corresponding tension functionals.

   * Preconditions: the model class must support constructing both consistent and deliberately inconsistent pairs of analytic and arithmetic invariants.

### 8.2 Direct reuse targets

1. Q015 (uniform rank bounds)

   * Reuses: `BSD_FamilyTension_Functional` and `EllipticCurve_ArithmeticDescriptor`.
   * Why: uniform rank bounds rely on understanding how ranks can vary across families, and the BSD family tension provides a natural way to detect anomalies.
   * What changes: the focus shifts from the correctness of BSD itself to the distribution of rank patterns compatible with assumed low tension.

2. Q019 (Diophantine density problems)

   * Reuses: `BSD_CounterfactualWorld_Template`.
   * Why: the same pattern of coupling analytic data and Diophantine sets can model tensions in broader density conjectures.
   * What changes: the underlying objects are more general curves or varieties, and the observables differ, but the world T versus world F structure remains similar.

3. Q123 (AI interpretability and spectral structure)

   * Reuses: `EllipticCurve_ArithmeticDescriptor` as a prototype for descriptors that combine discrete structural invariants and continuous spectral summaries.
   * Why: interpretability problems often need to relate internal model spectra and symbolic invariants.
   * What changes: the underlying objects are AI models or subnetworks instead of elliptic curves, and the semantics of “rank” and “leading term” are adapted.

---

## 9. TU roadmap and verification levels

This block records the current verification level and suggests next steps.

### 9.1 Current levels

* E_level: E2

  * A coherent effective encoding of BSD as a family level tension principle has been specified.
  * Mismatch measures, error models, quality gates, robust aggregators, and singular sets are defined together with family fairness rules and cross-node consistency conditions.

* N_level: N2

  * The narrative linking analytic and algebraic sides through tension is explicit.
  * Counterfactual worlds and cross problem transfers are described at the effective layer.

### 9.2 Next measurable step toward E3

To move from E2 to E3:

* Implement an external tool that

  * consumes public elliptic curve data sets,
  * constructs effective states `m_data(k)`,
  * computes `Delta_BSD_rank`, `Delta_BSD_value`, `Delta_BSD_local`, `Delta_BSD`, and `Tension_BSD`,
  * publishes family tension profiles together with enough metadata to allow independent replication.

* Coordinate an independent replication where a separate group applies the same encoding rules and reproduces the main tension profiles on different data sets.

* Verify cross node consistency with Q002 encodings in the overlapping part of the L-function space, using the explicit consistency threshold.

These steps rely only on observable summaries and encodings at the effective layer, not on any deep TU generative rule.

### 9.3 Long term role in the TU program

In the broader TU program, Q003 is expected to serve as

* the main S-level template for problems where discrete rank like invariants and continuous spectral data must fit into a single relation,
* a benchmark for testing whether TU style encodings can support reasoning about world class open conjectures without claiming proofs,
* a source of reusable components for Diophantine, physical, and AI spectral problems that share a similar coupling pattern.

---

## 10. Elementary but precise explanation

This block explains Q003 for non specialists while staying faithful to the effective layer description.

Classically, the Birch and Swinnerton-Dyer Conjecture says that for an elliptic curve there are two very different ways to measure how many rational solutions it has.

* One way counts how many independent rational points there are on the curve. This gives an integer called the algebraic rank.
* The other way looks at a complex analytic function `L(E, s)`, built from data about the curve, and measures how fast it vanishes at a special point `s = 1`. This gives another integer called the analytic rank.

BSD says these two integers should always agree. It also says that the size of the leading term of `L(E, s)` at `s = 1` should match a complicated expression built from other invariants of the curve.

In the Tension Universe view we do not try to prove this statement. Instead we ask what it would mean to measure how well the analytic side and the arithmetic side fit together, curve by curve and family by family.

We imagine

* a family of elliptic curves chosen by clear, tension independent rules,
* for each curve an encoded pair of numbers that represent its analytic rank and algebraic rank,
* for each curve an encoded comparison of the leading term of `L(E, s)` at `s = 1` with the expected arithmetic expression,
* for each curve an encoded summary of how local factors compare.

From these we build mismatch quantities:

* `Delta_rank` measures how far the two ranks disagree,
* `Delta_value` measures how far the leading term is from the expected arithmetic side, in a capped log scale,
* `Delta_local` measures how far local data disagree with their analytic counterparts on a fixed prime window.

We then average these mismatches across a finite family, with an extra weight on the high mismatch tail, forming a combined tension `Tension_BSD`.

Two scenarios appear.

* In a BSD true world, as we look at larger and larger families with better data, these combined mismatches and the overall tension stay small and stable.
* In a BSD false world, no matter how far we go, some of these combined mismatches stay large and the overall tension never drops into a genuinely low band.

This does not tell us which world we live in. It does not give a proof. It gives instead

* a precise way to talk about BSD as a low tension principle,
* a set of observables and experiments that can falsify specific ways of encoding that principle,
* a pattern that can be reused in other problems where discrete structure and continuous spectra must obey a shared relation.

Q003 is therefore the family level counterpart of Q001 and Q002, and it anchors the spectral_tension view of elliptic curves inside the Tension Universe framework without revealing any deep TU generative rule.

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
* Any quantitative examples or engineering suggestions here are to be read as encoding proposals, not as performance guarantees.

### Effective-layer boundary

* All objects used here (state spaces `M`, observables, invariants, tension scores, counterfactual worlds) live at the effective layer.
* No step in this file gives a constructive mapping from raw experimental, numerical, or simulation data into internal TU fields.
* No step exposes any deep TU generative rule or any first-principle axiom system.
* If an implementation appears to require such rules, this document should be read as an abstract specification, not as a disclosure of those rules.

### Encoding and fairness

* Admissible encoding classes, reference profiles, and weight families used in this page are constrained by the shared Tension Universe charters listed above.
* For every encoding class referenced here:

  * its definition, parameter ranges, quality gates, and reference families are fixed at the charter level before any problem-specific tuning;
  * these choices may depend on general physical or mathematical considerations and on public benchmark selections, but not on the unknown truth value of this specific problem;
  * no encoding is allowed to hide the canonical answer as an uninterpreted field, label, or parameter;
  * membership rules for families and good sets must be auditable without access to mismatch or tension outputs.

### Tension scale and thresholds

* All mismatch terms `DeltaS_*`, `Delta_*`, and tension functionals in this file are treated as dimensionless or normalized quantities, defined up to a fixed monotone rescaling specified in the TU Tension Scale Charter.
* Thresholds such as `epsilon_*`, `delta_*`, and experiment cutoffs are always interpreted relative to that fixed scale.
* Changing the tension scale requires an explicit update of the TU Tension Scale Charter, not an edit of individual problem files.
* When example values for thresholds are mentioned, they are illustrations within that scale, not hidden claims about the underlying mathematics.

### Falsifiability and experiments

* Experiments described in this document are tests of TU encodings, not tests of the underlying canonical problem itself.
* The rule “falsifying a TU encoding is not the same as solving the canonical statement” applies globally, even where it is not restated.
* When required observables cannot be reliably estimated in practice, the outcome of the corresponding experiment is recorded as “inconclusive”, not as confirmation.
* Negative results on a specific encoding should trigger revisions of the encoding under the charters, rather than claims about the truth or falsity of the underlying conjecture.

### Interaction with established results

* All encodings and counterfactual worlds described here are required to respect known theorems and hard constraints in the relevant field.
* If a later analysis finds a concrete conflict with established results, the correct procedure is to update or retire the encoding under the TU charters, not to reinterpret those results.
* When known conditional results exist (for example results assuming GRH), encodings should record these dependencies explicitly where they are used.

### Program note

* This page is an experimental specification within the ongoing WFGY / Tension Universe research program.
* All structures and parameter choices are provisional and may be revised in future versions, subject to the constraints above.
* Earlier simplified TU per-problem footers are considered subsumed by this footer together with the TU charters; any additional constraints from those versions should be interpreted through the same effective-layer and fairness principles stated here.
