# Q041 · Nature of dark matter

**BH Code**: `BH_COSMO_DARKMATTER_L1_041`
**Domain**: Cosmology
**Family**: Dark sector
**Rank**: S
**Projection**: L1 (physical), with I / M / C projections noted
**Status**: Open problem (modern form since 1930s)
**First stated by**: Fritz Zwicky (1933), later reinforced by Vera Rubin era rotation curves

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer.

* We only specify observables, constraints, tension indices, functionals, extremality patterns, and falsifiable tests.
* We do not specify any underlying axioms, generators, or constructive rules.
* No explicit mapping from raw observational data to internal TU fields is given.
* We do not claim a unique microphysical identity for dark matter.

This is a semantic tension description, not a proof and not a microscopic theory.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Across multiple independent observations, the gravitational field inferred from dynamics and lensing is not fully explained by visible baryonic matter and radiation.

The canonical problem is to explain the persistent discrepancy using one of the following, or a combination:

* an additional non luminous component (dark matter)
* an effective modification to gravitational dynamics at certain regimes

The target is a single coherent explanation that matches, simultaneously, at least these classes of evidence:

* galaxy rotation curves
* gravitational lensing (galaxy and cluster scale)
* cluster dynamics and mass profiles
* large scale structure formation statistics
* cosmic microwave background constraints on matter content

### 1.2 Status notes

* A single global framework (LambdaCDM with cold dark matter) fits many cosmological observables well.
* There remain active debates about small scale behavior and the space of viable dark sector or modified gravity models.
* No single microphysical model is universally confirmed as the nature of dark matter.

This file encodes the problem as a TU tension extremality structure only.

---

## 2. Position in the BlackHole graph

### 2.1 Closest coupled problems

* Q042 (dark energy): late time expansion and stress energy budget
* Q043 (inflation): early universe initial conditions and primordial spectra
* Q045 (large scale structure): growth and clustering statistics
* Q046 (CMB anomalies): potential imprints of non standard early dynamics
* Q048 (H0 tension): multi probe inconsistency in late universe inference
* Q049 (missing baryons): inventory mismatch in visible sector census

### 2.2 Cross domain edges

* information theory: model compression cost for multi survey consistency
* AI engineering: global field consistency under heterogeneous evidence

---

## 3. Operator and model semantics declaration

**Chosen semantics**: continuous manifold semantics (effective cosmology)

* Let `S` be spacetime.
* Let `Sigma(t)` be a spatial slice at cosmic time `t`.
* All spatial fields below live on `Sigma(t)` unless stated otherwise.
* `grad`, `div`, and `Lap` are Riemannian operators on `Sigma(t)` (effective usage only).

**Time derivative rule**

Unless explicitly stated as smooth, every time evolution is interpreted as finite difference:

* `DeltaF/DeltaT = (F(t2) - F(t1)) / (t2 - t1)` with `t2 > t1`

**Domain restriction rule**

Whenever a ratio appears, its denominator is assumed strictly positive on the working domain.
Any points where this fails are assigned to the exceptional set `S_sing` (defined later).

---

## 4. Observables and data level objects

### 4.1 Core observable families

Define a set of observational channels `O_k`:

* `O_rot`: rotation curve family `v_rot(r)` for galaxies
* `O_lens`: lensing convergence or shear maps, summarized as `kappa(theta)` or equivalent reduced observables
* `O_clu`: cluster dynamical observables, velocity dispersions, hydrostatic mass proxies
* `O_lss`: large scale structure summaries (power spectrum, correlation functions, halo mass function)
* `O_cmb`: CMB derived constraints on matter content and growth history

### 4.2 Effective reconstructed fields

Assume there exists an effective reconstruction procedure (not specified here) that yields:

* `rho_vis(x, t)`: visible sector mass density (baryons plus luminous tracers)
* `rho_dyn(x, t)`: dynamical mass density inferred from gravity sensitive observables

Define the effective discrepancy field:

* `rho_gap(x, t) = rho_dyn(x, t) - rho_vis(x, t)`

Interpretation at the effective layer:

* `rho_gap > 0` indicates a missing mass like effect in that region
* `rho_gap < 0` can occur due to systematics or modeling mismatch and is handled by the tension index definition below

---

## 5. TU encoding at the effective layer

### 5.1 Semantic space objects

* `M` is a semantic state space.
* `X` is a high level semantic state in `M` encoding:

  * the chosen data set collection
  * modeling assumptions and nuisance parameters
  * reconstruction choices that are treated as part of the semantic context

The dimension of `M` is not fixed. Implementations may use `R^n` embeddings.

### 5.2 Metric and stress

* `g_ij` is a metric on `M` supporting distance and energy geometry roles.
* `DeltaS_DM(X1, X2, t) >= 0` is a nonnegative gap measure between semantic states.

The canonical Beta form must exist in this entry as a reducible form:

```txt
[Eq 1] T_ij = S_i * C_j * DeltaS_DM * lambda * kappa
```

`S_i` and `C_j` are effective factors whose detailed construction is not specified at the effective layer.

### 5.3 Effective TU statement for Q041

Assume there exists a family of TU compatible models such that for each semantic state `X`:

* the observable families `O_k(X)` are jointly representable by an effective field system on `Sigma(t)`
* there exists an effective dark sector representation `DM_field(X)` that reduces the inconsistency between channels when evaluated by a shared tension functional

This statement is about existence of consistent encodings, not about identifying a particle.

---

## 6. Tension indices and functionals

### 6.1 Local tension index

Define a local gravitational mismatch index on the working domain:

* `DeltaS_grav(x, t) >= 0`

A minimal effective choice that respects nonnegativity:

```txt
[Eq 2] DeltaS_grav(x, t) = w0(x, t) * abs(rho_gap(x, t)) / (rho_scale(x, t) + eps0)
```

Where:

* `w0(x, t) >= 0` is a reliability weight (downweights uncertain regions)
* `rho_scale(x, t) > 0` is a local scale for normalization (example: `rho_vis + rho_floor`)
* `eps0 > 0` prevents division by zero

This definition is an effective template. Any alternative must keep `DeltaS_grav >= 0` and declare its domain restrictions.

### 6.2 Global tension functional

Define a global tension functional over a system or survey region `Omega`:

```txt
[Eq 3] T_DM[Omega, t] = Integral_Omega ( DeltaS_grav(x, t) ) dV
```

Implementation note:

* In practice this integral is evaluated numerically as a weighted sum over pixels, grid cells, or samples.
* The exact discretization is not specified here, but must be declared by any implementation.

### 6.3 Extremality principle

The effective extremality claim is:

* among admissible encodings `E` that map semantic states `X` to effective fields and reconstructions, the observed universe is compatible with encodings that keep `T_DM` inside a controlled band across multiple channels and multiple scales.

Equivalently, the acceptable class of encodings is constrained by:

```txt
[Eq 4] T_DM[Omega_i, t_i] <= B_i  for a declared set of systems (Omega_i, t_i)
```

Where each bound `B_i` is declared with uncertainty assumptions.

This is not a claim that the true world is a strict minimizer. It is a claim that TU compatible encodings must avoid uncontrolled blow up of `T_DM` across well measured systems.

---

## 7. Counterfactual tension worlds

### 7.1 World T (coherent low tension dark sector)

World T is the world where there exists a single coherent class of dark sector encodings that keeps multi channel tension controlled.

Operationally, there exists an encoding family `E_T` with a small shared parameter set `theta` such that for many systems:

```txt
[Eq 5] T_DM[Omega_i, t_i | E_T(theta)] stays in a narrow band across i
```

Expected signatures at the effective layer:

* rotation and lensing reconstructions agree on `rho_dyn` profiles up to declared uncertainties
* cross scale consistency: galaxy, group, and cluster reconstructions can be explained without adding system specific rules
* information compression: fewer degrees of freedom are needed to summarize the data without large residuals

### 7.2 World F (no coherent low tension dark sector)

World F is the world where no unified encoding family exists that keeps the same tension band across robust data sets.

Operationally, for any candidate encoding family `E` with small shared parameterization, there exist many systems where:

```txt
[Eq 6] T_DM[Omega_i, t_i | E] >> B_i
```

Expected effective layer consequences:

* patchwork effects: different classes of objects require mutually incompatible adjustments
* high parameter cost: compression of multi survey consistency requires a growing list of exceptions
* projection incoherence: improvements in one channel come with large degradation in another

This is a counterfactual tension pattern statement only. It does not decide the world.

---

## 8. Singularity and exceptional set

Define the exceptional set `S_sing` as the subset of points where the required reconstructions are not regular enough to define `DeltaS_grav` reliably, for example due to:

* missing coverage in lensing or rotation data
* strong baryonic feedback uncertainties beyond declared tolerance
* numerical instability in reconstruction

We choose contract option (a):

* restrict the working domain to `Omega = Domain \ S_sing`

All tests and functionals in this file are evaluated on `Omega` with explicit reporting of how `Omega` was chosen.

---

## 9. Falsifiability and discriminating experiments

This section targets falsifying the TU encoding structure, not solving dark matter.

### 9.1 Discriminating test DM TU 1 (scale coherent tension band)

Goal:

* test whether a chosen TU encoding yields scale coherent control of `T_DM` across object classes.

Protocol:

1. Select a multi scale set of systems:

   * galaxies with high quality `v_rot(r)`
   * lensing systems with stable `kappa` maps
   * clusters with multiple mass proxies

2. For each system `i`, declare:

   * working domain `Omega_i`
   * reliability weights `w0_i`
   * normalization scale `rho_scale_i`
   * a bound `B_i` derived from declared noise and systematics

3. Compute:

   * `T_DM[Omega_i, t_i]`

4. Evaluate cross scale stability:

   * check whether `T_DM` stays within the declared bands for the majority of systems without system specific parameter injections.

Falsification criterion:

```txt
[Eq 7] If for a fixed encoding family E(theta) with small shared theta,
       there exists a persistent, class-dependent failure:
       T_DM[Omega_i, t_i | E(theta)] > B_i across many systems,
       then that TU encoding is falsified at the effective layer.
```

Important statement:

* falsifying a TU encoding is not the same as proving any microphysical dark matter model wrong
* it only rejects the specific tension functional plus extremality assumptions used here

### 9.2 Discriminating test DM TU 2 (projection coherence stress test)

Goal:

* verify that lowering tension in P does not explode tension in I or M proxies.

Define an information proxy `C_info(E)` and a model complexity proxy `C_model(E)` for an encoding `E` (definitions are implementation dependent but must be explicit).

Test requirement:

```txt
[Eq 8] An encoding E is unacceptable if it reduces T_DM
       only by causing uncontrolled growth in C_info or C_model
       beyond a declared coherence budget.
```

This explicitly enforces projection coherence as a falsifiable constraint.

---

## 10. AI and WFGY engineering spec

### 10.1 Training signals

Define model predicted dynamical density `rho_dyn_hat(x, t)` and observed reconstructed `rho_dyn_obs(x, t)`.

Define a tension based training loss:

```txt
[Eq 9] L_DM = Sum_over_samples ( w0 * abs(rho_dyn_hat - rho_dyn_obs) / (rho_scale + eps0) )
```

This is a directly computable effective layer loss. No TU Deep structure is required.

### 10.2 Architectural patterns

Recommended patterns for an AI system that aims to be TU compatible on Q041:

* field memory modules: store and update spatial fields with uncertainty tags
* global consistency checkers: enforce cross channel agreement constraints
* multi scale gating: a mechanism that tests whether a single shared encoding can cover galaxy and cluster scales without special cases

### 10.3 Evaluation harness

Benchmark harness template:

* Inputs:

  * visible sector tracers
  * gravitational observables from multiple channels
* Outputs:

  * reconstructed `rho_dyn_hat`
  * `DeltaS_grav` maps
  * global `T_DM` per system
* Evaluation:

  * accuracy of reconstructions under perturbations
  * stability of `T_DM` across object classes
  * projection coherence budget checks using `C_info` and `C_model`

---

## 11. Cross problem transfer template

Reusable components contributed by Q041:

* `DeltaS_grav(x, t)` as a generic multi channel mismatch index
* `T_DM[Omega, t]` as a global functional from local mismatch
* a falsifiable notion of cross scale tension band stability
* projection coherence budget as a hard constraint

Direct reuse targets:

* Q042 (dark energy): define analogous tension over expansion history vs structure growth
* Q045 (large scale structure): define mismatch tension between clustering statistics and inferred mass distribution
* Q048 (H0 tension): define parameter space tension across measurement channels
* Q049 (missing baryons): define mismatch tension over baryon census vs observable proxies

---

## 12. TU roadmap and verification levels

### 12.1 TU penetration level

Assigned level for this entry:

* `E1` well defined observables and tension functionals, with explicit falsifiability tests

Upgrade targets:

* `E2` attach concrete datasets and compute tension distributions with declared uncertainty models
* `E3` implement a working field evolution or agent model that uses the tension objectives and demonstrates empirical advantage
* `E4` cross problem verification where the same tension structure improves Q041 plus at least two coupled problems with third party reproduction

### 12.2 Internal maturity level

Assigned maturity:

* `N1` skeleton complete, tests defined, no public implementation attached yet

---

## 13. Elementary but precise explanation

* We observe how galaxies move and how light bends. Visible matter does not fully explain these effects.
* We define a mismatch score `DeltaS_grav` that measures how large the gap is between gravity inferred mass and visible mass, in a way that is always nonnegative.
* We add up this mismatch over space to get `T_DM`. A good explanation is one that keeps `T_DM` controlled across many objects and many measurement channels without special case rules.
* We describe two worlds. In World T, one coherent explanation keeps `T_DM` stable across scales. In World F, no such coherent explanation exists and the mismatch behaves like a patchwork.
* We give a concrete falsifiable test: if a proposed encoding cannot keep `T_DM` within declared bounds across many systems, then that encoding is rejected, even though the ultimate nature of dark matter might still be unknown.
* For AI, this problem becomes a stress test for building field like representations that stay globally consistent across heterogeneous evidence.

---
