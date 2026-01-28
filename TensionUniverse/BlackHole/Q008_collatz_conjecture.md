# Q008 · Collatz conjecture

## 0. Header metadata

```txt
ID: Q008
Code: BH_MATH_COLLATZ_L3_008
Domain: Mathematics
Family: Discrete dynamics and Diophantine trajectories
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: computational_tension
Status: Open
Semantics: discrete
E_level: E1
N_level: N1
Spec_version: 2
Last_updated: 2026-01-28
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Define the map `T` on positive integers as follows:

```txt
T(n) = n / 2        if n is even
T(n) = 3 * n + 1    if n is odd
```

Given a starting integer `n >= 1`, define its Collatz orbit as the sequence

```txt
n_0 = n
n_{k+1} = T(n_k)  for k >= 0
```

The classical form of the Collatz conjecture (the `3 * n + 1` problem) is:

> For every positive integer `n`, the orbit of `n` under `T` eventually reaches the cycle `1 -> 4 -> 2 -> 1`.

Equivalently, every positive integer is conjectured to have a finite total stopping time. The total stopping time of `n` is the smallest `k` such that `n_k = 1`, if such a `k` exists.

### 1.2 Status and difficulty

The Collatz conjecture is an open problem in number theory and discrete dynamics. It is extremely easy to state, yet remains unresolved despite extensive numerical and theoretical work.

Known partial results include:

* The conjecture has been verified by computer for starting values in very large ranges, up to scales such as `n` near `2^68` and beyond in later computations.
* Many structural properties of orbits are known. These include typical growth and decay patterns, parity structure, and the existence of very long but ultimately terminating orbits.
* Terence Tao proved that for almost all starting values (in a natural density sense), the orbit eventually attains values that are bounded by a fixed power of the starting value. This gives strong evidence that non terminating behavior, if it exists at all, must be extremely rare.

No proof is known that every orbit reaches the trivial cycle, and no explicit counterexample has been found. The problem is widely regarded as very difficult and is often used as a model case where a simple local rule generates globally elusive dynamics.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q008 has three main roles.

1. Prototype of a discrete dynamical S problem

   Q008 is the canonical example of a system where a very simple local update rule on integers induces orbit structures that are hard to analyze at global scale.

2. Testbed for computational_tension

   Q008 is used to define a computational_tension functional that compares finite orbit statistics between a Collatz true world and worlds with non terminating behavior or nontrivial cycles.

3. Bridge to complexity and information problems

   The discrete trajectory and stopping time concepts in Q008 transfer directly to problems in computational complexity and information thermodynamics, where long discrete processes must be summarized and compared.

### References

1. Richard K. Guy, *Unsolved Problems in Number Theory*, 3rd edition, Springer, 2004. Chapter on the `3 * n + 1` problem and related iterative maps.
2. Jeffrey C. Lagarias (editor), *The Ultimate Challenge: The 3x+1 Problem*, American Mathematical Society, 2010.
3. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, arXiv:1909.03562, 2019, with subsequent journal publication.
4. Standard encyclopedia entry on “Collatz conjecture” in a widely used mathematics reference.

---

## 2. Position in the BlackHole graph

This block describes how Q008 sits inside the BlackHole graph. Each edge has a one line reason that refers to a concrete component or tension structure.

### 2.1 Upstream problems

Upstream nodes provide prerequisites or general frameworks that Q008 reuses at the effective layer.

* Q016 (BH_MATH_ZFC_CONTINUUM_L3_016)
  Reason: Supplies the foundational view of sets and real valued quantities used for densities of starting values, limiting behaviors, and real valued observables defined in Block 3.

* Q019 (BH_MATH_DIOPH_DENSITY_L3_019)
  Reason: Provides general Diophantine density and distribution tools reused to interpret `Obs_termination_ratio` and related frequency based observables.

### 2.2 Downstream problems

Downstream nodes reuse Q008 components or depend on its discrete trajectory tension structure.

* Q051 (BH_CS_P_VS_NP_L3_051)
  Reason: Reuses `DiscreteTrajectory_Tension_008` as a toy model for the difficulty of predicting or verifying long computation traces.

* Q053 (BH_CS_ONE_WAY_FUNCTIONS_L3_053)
  Reason: Reuses `StoppingTimeField_Descriptor_008` to build intuition for one way like behavior in simple iterative maps.

### 2.3 Parallel problems

Parallel nodes share similar tension types without direct component reuse.

* Q006 (BH_MATH_GOLDBACH_L3_006)
  Reason: Both Q006 and Q008 are elementary number theoretic problems where computational_tension arises from the gap between simple local rules and globally hard patterns.

* Q009 (BH_MATH_ODD_PERFECT_L3_009)
  Reason: Both study extremely constrained integer structures, where tension is driven by the difficulty of reconciling local multiplicative patterns with global classification.

### 2.4 Cross domain edges

Cross domain edges show where Q008 components transfer into other domains.

* Q051 (BH_CS_P_VS_NP_L3_051)
  Reason: Cross domain transfer of `DiscreteTrajectory_Tension_008` into complexity theory, where discrete iterative structure is used to reason about verification costs and resource limits.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses `StoppingTimeField_Descriptor_008` as a discrete model for information flow and dissipation in stepwise processes.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We describe only state spaces, observables, reference profiles, mismatch functionals, tension functionals, and singular sets. No rule is given for how raw Collatz data is mapped into internal TU fields, and no deep TU generative mechanism is exposed.

### 3.1 State space and refinement path

We assume an effective state space

```txt
M_008
```

together with a fixed refinement path encoded by the following data.

1. Refinement indices

   We consider integers `k >= k_min`, where `k_min >= 1` is a fixed baseline index.

2. Starting value sets

   For each refinement level `k` we define

   ```txt
   N_k = 2^k
   S_k = { 1, 2, ..., N_k }.
   ```

   The set `S_k` is the set of starting values whose trajectories are summarized at level `k`. This choice is part of the encoding and does not depend on which counterfactual world is realized.

3. Truncation rules

   For each `k` we fix two deterministic truncation bounds:

   ```txt
   L_max(k)   = C_len * (log_2 N_k)^2
   V_max(k)   = N_k^gamma
   ```

   where `C_len >= 1` and `gamma >= 2` are fixed positive constants chosen at the encoding level and recorded as part of the Q008 specification. They are not adjusted after inspecting data.

   For a starting value `n` in `S_k`:

   * we follow the Collatz map for at most `L_max(k)` steps, unless we reach the trivial cycle earlier,
   * we record whether the orbit ever exceeds `V_max(k)` within the first `L_max(k)` steps.

4. States along the refinement path

   A state `m(k)` in `M_008` lying on the refinement path encodes a coherent finite snapshot of trajectories for all starting values in `S_k`, truncated according to `L_max(k)` and `V_max(k)`, together with summary statistics defined below. We do not specify how `m(k)` is represented internally, only that the observables in Section 3.3 are well defined.

5. Monotonicity of refinement

   Refinement follows the inclusions

   ```txt
   S_k subset S_{k+1}
   L_max(k) <= L_max(k+1)
   V_max(k) <= V_max(k+1)
   ```

   Once a trajectory has been classified at a given level `k` as not reaching the trivial cycle within `L_max(k)` or as exceeding `V_max(k)`, this fact is recorded at level `k` and is never retroactively erased at that level, even if later levels reveal more steps.

A general state `m` in `M_008` may encode data for a single `k` or for several refinement indices. For tension statements in this file we only use states that match this refinement scheme.

### 3.2 Finite encoding library

We introduce a finite encoding library for Q008:

```txt
L_enc_008_finite = {
    Enc_orbit_length,
    Enc_max_excursion,
    Enc_parity_signature
}
```

The internal representation of each encoding is fixed once and for all at the effective layer. Each encoding has a minimal input–output interface.

1. `Enc_orbit_length`

   * Input: truncated Collatz trajectories for starting values in `S_k` with truncation rules `L_max(k)` and `V_max(k)`.
   * Output: a histogram vector

     ```txt
     Hist_len(m; k) = (h_len(m; k; j))_{j=0,...,J_len}
     ```

     where:

     * bins `j = 0,...,J_len-2` represent ranges of stopping times measured in units of Collatz steps, for example logarithmic bins in base 2,
     * bin `j = J_len-1` is the censored bin that collects starting values in `S_k` whose trajectories did not reach the trivial cycle within `L_max(k)` steps, or exceeded `V_max(k)` before termination.

     The binning scheme (cut points, number of bins `J_len`) is fixed and does not depend on any observed data.

2. `Enc_max_excursion`

   * Input: the same truncated trajectories as above.
   * Output: a histogram vector

     ```txt
     Hist_exc(m; k) = (h_exc(m; k; j))_{j=0,...,J_exc}
     ```

     where:

     * bins `j = 0,...,J_exc-2` represent ranges of maximal orbit values below or equal to `V_max(k)`,
     * bin `j = J_exc-1` is an overflow bin that collects starting values whose truncated trajectory exceeded `V_max(k)` at least once before termination or truncation.

     The binning scheme for maximal excursion is also fixed in advance.

3. `Enc_parity_signature`

   * Input: truncated trajectories for starting values in `S_k`.
   * Output: a compact vector of parity or symbolic pattern features (for example frequency of odd steps, simple parity patterns, or short parity word statistics).
   * In this version of Q008, `Enc_parity_signature` is part of the state description but does not directly enter the main tension functional. It is retained for future extensions of computational_tension in discrete dynamics.

For each encoding, the following effective layer rules hold.

* The dimension of each histogram and the interpretation of each bin index are fixed as part of the TU encoding and are not changed after observing data.
* Refinement in `k` increases the amount of data summarized, but does not change the binning schemes or the mapping from trajectories to bins.

### 3.3 Observables and fields

We now define observables on `M_008` that will feed into mismatch and tension functionals. For each state `m` compatible with refinement level `k` we define:

1. Orbit length observable

   ```txt
   Obs_orbit_length(m; k) = Hist_len(m; k)
   ```

   where `Hist_len(m; k)` is the histogram produced by `Enc_orbit_length`. Each component satisfies

   ```txt
   h_len(m; k; j) >= 0
   sum_j h_len(m; k; j) = 1
   ```

   so the histogram is normalized.

2. Maximal excursion observable

   ```txt
   Obs_max_excursion(m; k) = Hist_exc(m; k)
   ```

   where `Hist_exc(m; k)` is the histogram produced by `Enc_max_excursion`. Each component satisfies

   ```txt
   h_exc(m; k; j) >= 0
   sum_j h_exc(m; k; j) = 1.
   ```

3. Termination ratio observable

   We define a scalar observable

   ```txt
   Obs_termination_ratio(m; k) =
       1 - h_len(m; k; J_len-1)
   ```

   that is, one minus the censored bin mass in `Hist_len`. This represents the fraction of starting values in `S_k` whose orbits reached the trivial cycle within `L_max(k)` steps without leaving the allowed value range.

   The termination ratio is therefore not an independent construct. It is a dedicated channel that reads out a specific bin in `Obs_orbit_length`.

All three observables are defined on any state `m` that encodes the necessary histogram data for level `k`.

### 3.4 Reference profiles

Reference profiles are fixed objects that describe hypothetical behavior in a Collatz true world. They are part of the encoding and cannot be altered after data inspection within a given version.

1. Reference orbit length profile

   For each `k` we fix a reference histogram

   ```txt
   Ref_orbit_length(k) = (L_ref(k; j))_{j=0,...,J_len}
   ```

   with the same dimension and bin interpretation as `Obs_orbit_length`. The components satisfy

   ```txt
   L_ref(k; j) >= 0
   sum_j L_ref(k; j) = 1.
   ```

2. Reference maximal excursion profile

   For each `k` we fix a reference histogram

   ```txt
   Ref_max_excursion(k) = (E_ref(k; j))_{j=0,...,J_exc}
   ```

   with the same interpretation as `Obs_max_excursion` and normalized in the same way.

3. Reference termination profile

   For each `k` we fix a scalar

   ```txt
   Ref_term(k) = 1 - eps_term(k)
   ```

   where `eps_term(k)` is a small nonnegative function of `k` chosen at the encoding level. A simple choice is

   ```txt
   eps_term(k) = eps_0
   ```

   for all `k >= k_min`, with `eps_0` a small constant such as `10^-6`. More general choices can allow slow dependence on `k`, but must be specified in advance and written into the encoding.

The triplet

```txt
(Ref_orbit_length, Ref_max_excursion, Ref_term)
```

is treated as an external artifact for Q008. Any update of these profiles defines a new version of the encoding and must be logged as such. Reference profiles never depend on observed data for particular states.

### 3.5 Fixed mismatch metrics

We define three mismatch functionals using fixed metrics. The formulas stated here are not examples. They are the definitions used in this specification.

1. Length mismatch

   For a state `m` and level `k` we define

   ```txt
   DeltaS_length(m; k) =
       (1/2) * sum_{j=0}^{J_len} | h_len(m; k; j) - L_ref(k; j) |
   ```

   This is the total variation distance between `Obs_orbit_length(m; k)` and `Ref_orbit_length(k)`.

2. Excursion mismatch

   For a state `m` and level `k` we define

   ```txt
   DeltaS_excursion(m; k) =
       (1/2) * sum_{j=0}^{J_exc} | h_exc(m; k; j) - E_ref(k; j) |
   ```

   This is again the total variation distance, this time between `Obs_max_excursion(m; k)` and `Ref_max_excursion(k)`.

3. Termination mismatch

   For a state `m` and level `k` we define

   ```txt
   DeltaS_term(m; k) =
       max( 0, Ref_term(k) - Obs_termination_ratio(m; k) )
   ```

   This mismatch is zero if the observed termination ratio is at least as large as the reference value, otherwise it grows linearly with the deficit.

All three mismatch functionals are nonnegative and equal to zero if and only if the corresponding observable exactly matches the reference profile in the sense specified above. No alternative metric is used in this version of Q008.

### 3.6 Combined Collatz tension functional and weight set

We define a combined tension functional at level `k` by:

```txt
Tension_Collatz(m; k) =
    w_len  * DeltaS_length(m; k)
  + w_exc  * DeltaS_excursion(m; k)
  + w_term * DeltaS_term(m; k)
```

where the weights `(w_len, w_exc, w_term)` are chosen from a fixed finite admissible set

```txt
W_008_adm = {
  (1/3, 1/3, 1/3),
  (0.4, 0.4, 0.2),
  (0.25, 0.25, 0.5)
}
```

The following rules apply.

* The admissible set `W_008_adm` is part of the Q008 encoding and does not depend on any data.
* In any single experimental run or analysis, one weight triple from `W_008_adm` is chosen in advance and logged as part of the protocol.
* Once a weight triple is fixed for that run, it is not adjusted based on observed tension values.
* Moving from one triple in `W_008_adm` to another is treated as defining a distinct encoding choice within Q008, not as an in run parameter tweak.

The weights satisfy

```txt
w_len >= 0,  w_exc >= 0,  w_term >= 0
w_len + w_exc + w_term = 1.
```

### 3.7 Effective tension tensor

The Q008 tension functional feeds into the TU tension tensor at the effective layer through the standard pattern

```txt
T_ij(m; k) =
    S_i(m; k) * C_j(m; k)
  * Tension_Collatz(m; k)
  * lambda(m; k) * kappa_008
```

where:

* `S_i(m; k)` encodes the strength of the i-th source component of the Collatz related context at refinement level `k`.
* `C_j(m; k)` encodes the sensitivity of the j-th downstream component to Collatz related tension at this level.
* `lambda(m; k)` is a bounded convergence or divergence factor from the TU core decisions.
* `kappa_008` is a fixed coupling constant specific to Q008.

The index sets for `i` and `j` are finite and model dependent. They are not specified at the effective layer.

### 3.8 Singular set and domain restriction

Some states may encode incomplete or inconsistent information, for example if histograms are not normalized or the termination ratio is undefined. We define the singular set

```txt
S_sing_008 =
  { m in M_008 :
    for some k, any of the following holds:
      Obs_orbit_length(m; k) is not a normalized histogram, or
      Obs_max_excursion(m; k) is not a normalized histogram, or
      Obs_termination_ratio(m; k) is undefined, or
      any mismatch DeltaS_length(m; k), DeltaS_excursion(m; k),
      or DeltaS_term(m; k) is not finite }
```

The regular domain is

```txt
M_008_reg = M_008 \ S_sing_008.
```

All tension statements and experiments in this file are restricted to states in `M_008_reg`. If an experiment would require evaluating `Tension_Collatz(m; k)` for a state in `S_sing_008`, that evaluation is treated as out of domain and not as evidence for or against the Collatz conjecture.

---

## 4. Tension principle for this problem

This block states the effective layer principle that Q008 uses to distinguish low tension and high tension worlds.

### 4.1 Core tension principle

At the effective layer, the Collatz conjecture is encoded as a statement about the existence of low tension refinement paths that respect the fixed encoding.

A refinement path is a sequence of states

```txt
m(k) in M_008_reg,  for k >= k_min,
```

such that each `m(k)` encodes histogram data for starting values in `S_k` with truncation rules `L_max(k)` and `V_max(k)` as specified in Section 3.1.

We consider two types of branches.

* Low tension branch

  There exists at least one admissible choice of weight triple in `W_008_adm`, a threshold `epsilon_Collatz > 0`, and a refinement path `m_T(k)` such that

  ```txt
  Tension_Collatz(m_T(k); k) <= epsilon_Collatz
  ```

  for all sufficiently large `k`. The threshold `epsilon_Collatz` is chosen in advance based on theoretical expectations and is not allowed to grow without bound with `k`.

* High tension branch

  For any admissible choice of weight triple in `W_008_adm` and any encoding that is faithful to actual trajectories in a Collatz false world, there exists a refinement path `m_F(k)` and a strictly positive `delta_Collatz` such that

  ```txt
  Tension_Collatz(m_F(k); k) >= delta_Collatz
  ```

  for infinitely many `k`.

The Collatz conjecture is then rephrased at the effective layer as the statement that the actual universe belongs to a low tension branch with respect to this encoding.

### 4.2 Stability, monotonicity, and fairness

The tension principle is subject to several stability and fairness conditions.

1. Fixed refinement scheme

   The sequences `S_k`, `L_max(k)`, and `V_max(k)` are fixed by formulas in Section 3.1 and do not depend on which counterfactual world we are in. Refinement is monotone in the sense described there.

2. Termination footprint monotonicity

   Because of the censored bin in `Obs_orbit_length` and the overflow bin in `Obs_max_excursion`, non terminating behavior cannot be hidden by truncation. If a starting value fails to reach the trivial cycle by step `L_max(k)` or exceeds `V_max(k)`, then its contribution to the censored or overflow bins is visible in `DeltaS_length`, `DeltaS_excursion`, and `DeltaS_term` at level `k`. These contributions cannot be erased by redefining bins or metrics.

3. Fixed metrics and weights

   The metrics in Section 3.5 and the finite weight set `W_008_adm` in Section 3.6 are fixed parts of the encoding. Within a given version of Q008 there is no freedom to choose different metrics. Changing `W_008_adm` or the metric definitions yields a new version of the encoding that must be clearly labeled.

4. Gauge invariance with respect to narratives

   The classification of refinement paths into low tension and high tension branches depends only on the arrays of mismatch values

   ```txt
   (DeltaS_length(m; k), DeltaS_excursion(m; k), DeltaS_term(m; k))
   ```

   together with the chosen weight triple. Rewriting the narrative explanation at the N layer does not alter the branch classification as long as the underlying histograms and weights remain the same.

5. No post hoc tuning within a run

   In any single experimental run, the following objects are chosen and logged in advance before numerical data or tension values are examined:

   * the refinement levels to be used,
   * the reference profiles,
   * the weight triple from `W_008_adm`,
   * the threshold conventions for low and high tension labels.

   These choices are not adjusted during or after the run to achieve a desired conclusion. A new choice of encoding or weights counts as a new run.

Under these conditions, the tension principle expresses a genuine structural distinction between worlds with robust low tension Collatz behavior and worlds where any faithful encoding must carry persistent high tension.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds in terms of observable patterns and tension behavior, using the fixed encoding.

### 5.1 World T: Collatz true, low discrete trajectory tension

In World T the classical conjecture holds.

1. Termination behavior

   For each refinement level `k` there exists a state `m_T(k)` in `M_008_reg` that encodes trajectories for starting values in `S_k`. The termination ratio satisfies

   ```txt
   Obs_termination_ratio(m_T(k); k) >= Ref_term(k) - small_noise(k)
   ```

   where `small_noise(k)` is a bounded nonnegative modeling term that accounts for truncation effects and reference approximation errors. In particular, the censored bin mass remains very small.

2. Orbit length patterns

   The observable `Obs_orbit_length(m_T(k); k)` stays close to `Ref_orbit_length(k)` in total variation distance. The corresponding mismatch `DeltaS_length(m_T(k); k)` remains bounded by a small constant that does not grow with `k`.

3. Maximal excursion patterns

   The observable `Obs_max_excursion(m_T(k); k)` stays close to `Ref_max_excursion(k)`. The mismatch `DeltaS_excursion(m_T(k); k)` also remains small and stable.

4. Global tension

   For an admissible choice of weights and a suitable small threshold `epsilon_Collatz`, we have

   ```txt
   Tension_Collatz(m_T(k); k) <= epsilon_Collatz
   ```

   for all sufficiently large `k`. Refinement along larger `S_k` and higher truncation limits does not force the tension out of this low band.

### 5.2 World F: Collatz false, high discrete trajectory tension

In World F the classical conjecture fails. There exist starting values whose orbits do not reach the trivial cycle, or there exist nontrivial cycles that break the boundedness picture.

1. Non terminating or anomalous behavior

   Along some refinement path `m_F(k)` in `M_008_reg`, non terminating or anomalous behavior produces visible mass in the censored bin of `Obs_orbit_length` or in the overflow bin of `Obs_max_excursion` for infinitely many indices `k`.

2. Orbit length and excursion anomalies

   There exist positive constants `delta_length` and `delta_exc` such that for infinitely many `k` we have

   ```txt
   DeltaS_length(m_F(k); k) >= delta_length
   DeltaS_excursion(m_F(k); k) >= delta_exc
   ```

   or at least one of these inequalities holds, depending on how the anomalies manifest.

   In addition, if the termination ratio is significantly below `Ref_term(k)` for infinitely many `k`, then `DeltaS_term(m_F(k); k)` remains bounded away from zero.

3. Global tension

   For any admissible choice of weights in `W_008_adm` there exists a strictly positive `delta_Collatz` such that

   ```txt
   Tension_Collatz(m_F(k); k) >= delta_Collatz
   ```

   for infinitely many refinement levels `k`. This lower bound cannot be eliminated by retuning weights inside `W_008_adm` or changing the decomposition of the N layer narrative.

### 5.3 Interpretive note

These worlds are not constructions of raw trajectories inside the TU core. They are patterns of observable summaries and mismatch arrays. The difference between World T and World F is entirely encoded in whether there exists a refinement path with persistently low `Tension_Collatz` or whether any honest refinement path that respects the fixed encoding exhibits persistent high tension.

---

## 6. Falsifiability and discriminating experiments

This block defines experiments that can falsify or validate specific Q008 encodings at the effective layer. These experiments do not prove or disprove the Collatz conjecture, but they can reject poorly designed encodings or parameter choices that violate the TU charters.

### Experiment 1: Numerical discrete trajectory tension profile

*Goal*
Test whether `Tension_Collatz` behaves in a stable and interpretable way when applied to actual computed Collatz trajectories across several refinement levels.

*Setup*

* Input data: published or freshly computed Collatz trajectories for starting values `n` with `1 <= n <= N_K` for some maximal index `K`.
* Encoding: choose in advance

  * refinement indices `k_min,...,K`,
  * truncation rules `L_max(k)` and `V_max(k)` (as in Section 3.1),
  * reference profiles `Ref_orbit_length(k)`, `Ref_max_excursion(k)`, and `Ref_term(k)`,
  * one weight triple `(w_len, w_exc, w_term)` from `W_008_adm`.

*Protocol*

1. For each `k` in `{k_min,...,K}`, construct a state `m_data(k)` in `M_008_reg` that encodes:

   * `Obs_orbit_length(m_data(k); k)` as a normalized histogram with a censored bin,
   * `Obs_max_excursion(m_data(k); k)` as a normalized histogram with an overflow bin,
   * `Obs_termination_ratio(m_data(k); k)` as described in Section 3.3.

2. Compute

   ```txt
   DeltaS_length(m_data(k); k)
   DeltaS_excursion(m_data(k); k)
   DeltaS_term(m_data(k); k)
   Tension_Collatz(m_data(k); k)
   ```

   for each `k`.

3. Record the full arrays of mismatch values and tension values as functions of `k`.

*Metrics*

* The sequence of `Tension_Collatz(m_data(k); k)` as `k` increases.
* The behavior of individual mismatch terms, especially `DeltaS_term`, under refinement.
* Stability of these sequences under small allowed changes in reference profiles that remain within the same version of the encoding.

*Falsification conditions*

* If for all admissible choices in `W_008_adm` the tension sequence is wildly unstable under minor, charter respecting changes of reference profiles, the current encoding is considered inadequate.
* If different admissible encodings with the same raw data lead to contradictory labels of low tension versus high tension that cannot be explained by the finite variation allowed in `W_008_adm`, then the encoding must be revised.
* If the tension functional systematically fails to react to known large deviations in orbit behavior inside the tested range, the mismatch definitions must be reconsidered.

*Boundary note*
Falsifying a TU encoding is not the same as disproving the Collatz conjecture. This experiment only evaluates whether the current Q008 encoding is a good effective layer summary.

---

### Experiment 2: Toy model comparison of terminating and non terminating maps

*Goal*
Check whether the Q008 encoding can distinguish between toy iterative maps that always terminate and maps that exhibit non terminating cycles, under the same histogram based encoding.

*Setup*

* Construct two families of maps on positive integers.

  * Family `Ttoy`: maps that mimic the structural complexity of the Collatz map but are designed so that all orbits eventually reach a trivial cycle.
  * Family `Ftoy`: maps with similar local rule complexity but with known non terminating or nontrivial cycles for some starting values.

* For each map, compute trajectories for starting values in `S_k` for several values of `k`, using the same truncation rules `L_max(k)` and `V_max(k)`.

*Protocol*

1. Fix the encoding, reference profiles, and weight triple in advance.
2. For each map in `Ttoy` and each refinement level `k`, construct a state `m_Ttoy(k)` in `M_008_reg` and compute `Tension_Collatz(m_Ttoy(k); k)`.
3. For each map in `Ftoy` and each `k`, construct a state `m_Ftoy(k)` and compute `Tension_Collatz(m_Ftoy(k); k)`.
4. Compare the distributions of tension values for the two families.

*Metrics*

* The empirical distributions of `Tension_Collatz` for `Ttoy` and `Ftoy` at each `k`.
* The separation between these distributions, for example differences in averages or quantiles.
* Robustness of this separation under allowed encoding changes that stay within the same version of Q008.

*Falsification conditions*

* If for reasonable encoding choices the tension distributions for `Ttoy` and `Ftoy` maps are systematically indistinguishable, the encoding fails to capture basic differences between terminating and non terminating behavior and is rejected.
* If non terminating maps in `Ftoy` repeatedly receive lower tension values than terminating maps in `Ttoy` in ways that contradict their known properties, the encoding is considered misaligned and must be revised.

*Boundary note*
Success or failure on toy maps tests only the Q008 encoding. It does not by itself confirm or disprove the original Collatz conjecture.

---

## 7. AI and WFGY engineering spec

This block describes how Q008 can be used as a module inside AI systems within the WFGY framework, at the effective layer.

### 7.1 Training signals

The following training signals rely on Q008 observables and mismatch fields without exposing any deep TU rules.

1. `signal_discrete_orbit_consistency`

   * Definition: a nonnegative penalty proportional to a weighted sum of `DeltaS_length(m; k)` and `DeltaS_excursion(m; k)` in contexts where Collatz true behavior is assumed.
   * Purpose: discourage internal states or reasoning traces that suggest orbit length or excursion patterns incompatible with low tension Collatz behavior.

2. `signal_termination_ratio_alignment`

   * Definition: a penalty based on `DeltaS_term(m; k)`.
   * Purpose: enforce that, under Collatz true assumptions, internal representations do not imply large fractions of non terminating or censored trajectories.

3. `signal_tension_contrast_T_vs_F`

   * Definition: a signal that promotes clear separation between World T and World F narratives. It rewards large differences between predicted `Tension_Collatz` under explicitly Collatz true prompts and Collatz false prompts.
   * Purpose: train the model to keep counterfactual worlds distinct instead of mixing them.

4. `signal_discrete_dynamics_transfer`

   * Definition: a reward for successful transfer of Q008 style discrete trajectory reasoning to other iterative systems, while preserving low tension behavior in known terminating cases.
   * Purpose: encourage generalization of discrete trajectory intuition beyond the specific Collatz map.

### 7.2 Architectural patterns

1. `DiscreteTrajectoryHead_008`

   * Role: read internal embeddings of a discrete dynamics context and output approximate summaries analogous to `Obs_orbit_length`, `Obs_max_excursion`, and `Obs_termination_ratio`.
   * Interface:

     * Input: a vector or tensor encoding the current discrete dynamics problem.
     * Output: approximate histograms and a scalar termination score, plus an optional approximate `Tension_Collatz`.

2. `TerminationConsistencyFilter_008`

   * Role: act as a soft filter on candidate statements about termination or non termination.
   * Interface:

     * Input: a candidate statement, its internal representation, and a context tag (World T or World F).
     * Output: a score indicating whether the statement is consistent with low or high `Tension_Collatz` for that context.

3. `TU_DiscreteDynamics_Observer_008`

   * Role: map internal states to the minimal information needed to evaluate or approximate mismatch terms and `Tension_Collatz`.
   * Interface:

     * Input: internal embeddings of the current reasoning state.
     * Output: a compact vector that approximates the histogram based observables and termination ratio.

### 7.3 Evaluation harness

An evaluation harness for AI models augmented with Q008 components can proceed as follows.

1. Task design

   * Construct a benchmark of discrete dynamics questions, including Collatz like problems, toy maps with known termination behavior, and mixed contexts with explicit assumptions.

2. Conditions

   * Baseline condition: the model runs without Q008 specific modules or training signals.
   * TU condition: the model uses the Q008 modules and training signals described above.

3. Metrics

   * Accuracy on questions about termination properties.
   * Rate at which the model contradicts itself within a single context, for example asserting both termination and non termination for the same map.
   * Stability of the model’s answers when the prompt switches between World T and World F assumptions.

4. Analysis

   * Compare the baseline and TU conditions to test whether the Q008 encoding improves coherence, consistency, and interpretability in discrete trajectory reasoning.

### 7.4 Sixty second reproduction protocol

A minimal procedure that allows external users to experience the impact of Q008 encoding.

* Baseline setup

  * Prompt: ask the model to explain why the Collatz conjecture is considered hard and to describe typical trajectory behavior, without mentioning WFGY or tension.
  * Observation: record whether the answer separates observed data, heuristic beliefs, and the open status of the problem.

* TU encoded setup

  * Prompt: ask the model to explain the same topic but explicitly request organization around:

    * discrete trajectory statistics,
    * the three mismatch fields `DeltaS_length`, `DeltaS_excursion`, `DeltaS_term`,
    * low tension versus high tension worlds.

  * Observation: record whether the explanation becomes more structured, and whether the role of termination as a distinct signal is clear.

* Comparison metric

  * Rate both responses for clarity about what is known, what is measured, and what remains unproved.
  * Check whether the TU encoded answer avoids informal leaps from large finite experiments to global statements.

---

## 8. Cross problem transfer template

This block lists reusable components produced by Q008 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `DiscreteTrajectory_Tension_008`

   * Type: functional

   * Minimal interface:

     * Inputs: discrete trajectory summary histograms, termination ratios, and refinement indices.
     * Output: a nonnegative scalar tension value summarizing how well observed behavior matches a low tension terminating pattern.

   * Preconditions: histograms must be normalized and compatible with a fixed binning scheme.

2. ComponentName: `StoppingTimeField_Descriptor_008`

   * Type: field
   * Minimal interface:

     * Inputs: a family of starting states and refinement parameters.
     * Output: histograms of stopping times and termination ratios in the style of `Obs_orbit_length` and `Obs_termination_ratio`.

3. ComponentName: `WorldT_WorldF_DiscreteCycle_Template_008`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: a family of discrete maps with known or hypothesized termination behavior.
     * Output: experiment descriptions for a World T scenario and a World F scenario, each with clear rules for constructing mismatch arrays and tension values.

### 8.2 Direct reuse targets

1. Q051 (BH_CS_P_VS_NP_L3_051)

   * Reused components: `DiscreteTrajectory_Tension_008`, `StoppingTimeField_Descriptor_008`.
   * Why it transfers: complexity questions often involve very long discrete computations. Q008 style tension gives a way to discuss how computation length, resource usage, and termination patterns fit into low or high tension regimes.
   * What changes: trajectories become computation traces instead of Collatz orbits. Stopping times become measures of time or resource usage.

2. Q053 (BH_CS_ONE_WAY_FUNCTIONS_L3_053)

   * Reused components: `StoppingTimeField_Descriptor_008`, `WorldT_WorldF_DiscreteCycle_Template_008`.
   * Why it transfers: one way function candidates often involve iterative structure. The Q008 template helps construct low tension worlds where inversion is easy and high tension worlds where inversion seems structurally hard.
   * What changes: histograms summarize inversion difficulty instead of orbit termination.

3. Q059 (BH_CS_INFO_THERMODYN_L3_059)

   * Reused components: `DiscreteTrajectory_Tension_008`.
   * Why it transfers: Q059 views information processing as sequences of discrete updates. Q008 style tension evaluates how far real processes deviate from simple toy models with predictable termination and energy like constraints.

---

## 9. TU roadmap and verification levels

This block positions Q008 on the TU verification ladder and states the next measurable steps.

### 9.1 Current levels

* E_level: E1

  * The effective state space, fixed refinement scheme, observables, mismatch metrics, tension functional, and singular set are clearly specified.
  * Reference profiles and weight sets are fixed at the encoding level, with rules for versioning.
  * Concrete experiment templates with falsification conditions are defined.

* N_level: N1

  * World T and World F are described through discrete trajectory tension patterns, with termination treated as a distinct channel.
  * Cross problem transfer directions have been identified and linked to specific components.

### 9.2 Next measurable step toward E2

To move Q008 from E1 to E2, one or more of the following should be implemented and documented outside this file.

1. A working implementation of the encoding that:

   * constructs `Obs_orbit_length`, `Obs_max_excursion`, and `Obs_termination_ratio` from numerical data along the fixed refinement path,
   * evaluates `DeltaS_length`, `DeltaS_excursion`, `DeltaS_term`, and `Tension_Collatz` for several refinement levels,
   * logs these values in a reusable format.

2. A published tension profile table that, for each tested `k`, records:

   ```txt
   DeltaS_length(m_data(k); k)
   DeltaS_excursion(m_data(k); k)
   DeltaS_term(m_data(k); k)
   Tension_Collatz(m_data(k); k)
   ```

   under a clearly specified encoding and weight triple.

3. A demonstration of the toy map experiment with:

   * explicit definitions of `Ttoy` and `Ftoy` families,
   * tension distributions for each family across refinement levels,
   * analysis of robustness under allowed encoding changes.

These steps remain at the effective layer. They do not expose any TU core rules or claim any progress toward proving or disproving the conjecture.

### 9.3 Long term role in the TU program

In the long term, Q008 is expected to serve as:

* a reference node for discrete dynamical S problems with simple rules and complex global behavior;
* a test case for computational_tension design, including clear treatment of termination signals;
* a bridge between number theoretic dynamics and broader questions in complexity, cryptography, and information thermodynamics.

---

## 10. Elementary but precise explanation

This block gives an accessible explanation that stays faithful to the effective layer description.

The Collatz conjecture is about a very simple game on positive integers. Take any positive number `n`. If `n` is even, divide it by `2`. If `n` is odd, compute `3 * n + 1`. Repeat this rule on each new number that appears.

The conjecture says that no matter where you start, if you keep applying this rule, you will eventually see the loop

```txt
1, 4, 2, 1, 4, 2, 1, ...
```

Computers have checked this rule for many starting numbers and always found that the loop is reached. Still, nobody has a proof that this will happen for every possible starting number, and nobody has found a true counterexample.

In the Tension Universe picture we do not try to prove the conjecture directly. Instead, we look at many starting numbers at once and ask:

* How many steps do their trajectories take before reaching the loop, at least within the part we have computed?
* How high do the trajectories climb along the way?
* What fraction of starting numbers seem to reach the loop within a generous time and value budget?

We group starting numbers into ranges and, for each range, build simple histograms. One histogram counts how many numbers have short stopping times, how many have medium stopping times, and how many seem not to have stopped yet within our cutoffs. Another histogram counts how large the trajectories get before they come back down or before we stop computation. From these histograms we also read off a single number: the termination ratio, the fraction that appears to reach the loop within our budget.

We then compare these observed histograms to reference patterns that express what we would expect to see in a world where the conjecture is true. The differences between observed histograms and reference histograms give three mismatch scores:

* one for stopping times,
* one for maximal size,
* one for termination ratio.

A weighted combination of these mismatch scores is called the Collatz tension at that scale.

Now we imagine two types of worlds.

* In a Collatz true world, for some reasonable way of choosing reference patterns and weights, it should be possible to follow larger and larger ranges of starting numbers so that the Collatz tension stays low and stable. The censored and overflow bins should remain tiny, and the termination ratio should stay very close to one.

* In a Collatz false world, any honest attempt to summarize many starting numbers with our fixed encoding should eventually produce visible and persistent tension. This shows up as large mismatch scores coming from non terminating trajectories or very extreme behavior, and these scores cannot be tuned away by small changes in the encoding.

This approach does not answer the yes or no question about the conjecture. What it does provide is a well defined way to talk about:

* what we can measure from many trajectories at once,
* how to test whether an encoding behaves consistently under refinement,
* how to reject encodings that would allow us to hide non terminating behavior.

Q008 is therefore the discrete trajectory benchmark of the Tension Universe program. It turns the Collatz conjecture into a precise tension statement at the effective layer, with termination treated as a first class signal and with clear rules about what can be tuned and what must stay fixed.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an **effective-layer encoding** of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here (state spaces `M_008`, observables, invariants, tension scores, counterfactual worlds) live at the effective layer.
* No step in this file gives a constructive mapping from raw experimental or simulation data into internal TU fields.
* No step exposes any TU first-principle axiom system or deep generative rule.

### Encoding and fairness

* Admissible encoding classes, reference profiles, and weight families used in this page are constrained by shared Tension Universe charters:

  * [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
  * [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
  * [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)

* For every encoding referenced here:

  * its definition, parameter ranges, and reference families are fixed at the charter level or at the specification level before any problem specific tuning;
  * these choices may depend on general mathematical considerations and on public benchmark selections, but not on the unknown truth value of this specific problem;
  * no encoding is allowed to hide the canonical answer as an uninterpreted field, label, or parameter;
  * within a single experimental run, parameters such as reference profiles, weight triples, and thresholds are **not** changed after inspecting data. Any change to these parameters defines a new run with a new encoding identifier.

### Tension scale and thresholds

* All mismatch terms and tension functionals in this file are treated as **dimensionless or normalized quantities**, defined up to a fixed monotone rescaling specified in the TU Tension Scale Charter.
* Thresholds such as `epsilon_Collatz`, `delta_Collatz`, and experiment cutoffs are always interpreted relative to that fixed scale.
* Changing the tension scale requires an explicit update of the TU Tension Scale Charter, not an edit of individual problem files.

### Falsifiability and experiments

* Experiments described in this document are **tests of TU encodings**, not tests of the underlying canonical problem itself.
* The rule “falsifying a TU encoding is not the same as solving the canonical statement” applies globally, even where it is not restated.
* When required observables cannot be reliably estimated in practice, the outcome of the corresponding experiment is recorded as “inconclusive”, not as confirmation.
* Within any given version of this page, low tension or high tension labels for an experiment are evaluated under a fixed encoding and are not reinterpreted by retroactive parameter changes.

### Interaction with established results

* All encodings and counterfactual worlds described here are required to respect known theorems and hard constraints in the relevant field.
* If later analysis finds a concrete conflict with established results, the correct procedure is to update or retire the encoding under the TU charters, not to reinterpret those results.

### Program note

* This page is an experimental specification within the ongoing **WFGY / Tension Universe** research program.
* All structures and parameter choices are provisional and may be revised in future versions, subject to the constraints above. Any such revision is recorded through explicit versioning of this file and of the corresponding artifacts.
