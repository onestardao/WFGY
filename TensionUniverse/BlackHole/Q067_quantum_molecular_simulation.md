<!-- QUESTION_ID: TU-Q067 -->
# Q067 · Exact quantum simulation of complex molecules

## 0. Header metadata

```txt
ID: Q067
Code: BH_CHEM_QUANTUM_MOL_SIM_L3_067
Domain: Chemistry
Family: quantum_chemistry
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: computational_tension
Status: Open
Semantics: hybrid
E_level: E2
N_level: N2
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

We do not propose, prove, or disprove any new theorem about quantum chemistry, quantum complexity, or quantum computing. The canonical open problem is taken from existing literature. This page only specifies an **effective-layer encoding** of that problem inside TU.

### 0.1 Fixed encoding for Q067

Throughout this page we fix a single encoding

```txt
E = E_QSIM(
  EncodingKey   = Q067_QSIM_CORE_V1,
  LibraryKey    = Q067_QSIM_LIB_V1,
  WeightKey     = Q067_QSIM_WEIGHTS_V1,
  RefinementKey = Q067_QSIM_REFINE_V1
)
```

relative to the admissible encoding class `E_QSIM` defined in Section 4.

All of the following objects are defined **relative to this fixed encoding `E`**:

* state spaces and domains: `M(E)`, `M_reg(E)`, `S_sing(E)`
* observables: `E_error(m; E)`, `C_cost(m; E)`, `R_res(m; E)`, `F_corr(m; E)`, `S_spec(m; E)`
* tension components: `DeltaS_accuracy(m; E)`, `DeltaS_cost(m; E)`, `DeltaS_complexity(m; E)`
* combined tension: `Tension_QSIM(m; E)`, the tensor `T_ij(m; E)`
* encoding class: `E_QSIM` and its constants `epsilon_chem(E)`, `C_budget(E)`, `f_corr_ref(·; E)`, and weights `(alpha(E), beta(E), gamma(E))`
* reusable components in Section 8, including `QSIM_TensionFunctional`, `MolecularComplexityDescriptor`, and `ActiveSpaceRefinementPattern`
* all experiment templates and evaluation harnesses in Sections 6 and 7.

For readability we often suppress the explicit `E` and write `M`, `M_reg`, `S_sing`, `E_error(m)`, `Tension_QSIM(m)` and similar expressions. Unless explicitly stated otherwise, every such object should be read as shorthand for its encoding dependent form.

Changing any of the four keys in the definition of `E` produces a **different encoding**. Claims about experiments, tension values, or roadmap levels in this page apply only to the specific encoding `E` named above.

### 0.2 Scope of claims

* We **do not** claim that Q067 has been solved in the mathematical or algorithmic sense.
* We **do not** introduce any new axioms for quantum mechanics, computation, or chemistry.
* We **do not** provide any constructive proof that scalable, chemically accurate simulation is possible or impossible.

What we do instead is:

* specify a family of effective observables and tension functionals that an encoding `E` can use to organize known facts and future experiments,
* define what it would mean, at the effective layer, for chemistry to be **simulation low tension** or **simulation high tension** for relevant families of molecules,
* describe falsifiable constraints on how these observables and functionals must behave if they are to count as a valid TU encoding of Q067.

### 0.3 Fairness and non retrospection

All thresholds, weights, and reference maps that belong to `E` are fixed at the level of the encoding:

* `epsilon_chem(E)` sets the scale of chemical accuracy
* `C_budget(E)` sets the normalized cost budget
* `f_corr_ref(·; E)` maps correlation and resolution descriptors to expected cost scales
* `(alpha(E), beta(E), gamma(E))` mix the three tension components into `Tension_QSIM`.

They are **not allowed** to:

* depend on individual molecules, simulation strategies, or benchmark instances,
* be adjusted after seeing tension results for particular cases,
* be tuned differently for classical and quantum methods inside a single encoding.

Experiment templates in Section 6 require that molecule families, refinement ladders, and all parameters that belong to `E` be fixed **before** any tension values are examined. Retrospective tuning for a specific benchmark invalidates the experiment as evidence about Q067.

### 0.4 Boundary with deeper TU layers

The constructions in this page do not expose or rely on any deep TU generative rules, hidden fields, or axiom systems. They are compatible with many different possible deep-layer realizations of TU. Everything here can be read and used as a self-contained effective-layer specification even by readers who have no access to deeper TU machinery.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q067 can be stated as follows.

Given:

* realistic molecular systems with many electrons and nuclei, including strongly correlated and chemically complex cases,
* target observables such as ground state energies, excitation energies, and reaction barriers,
* a practical notion of chemical accuracy, for example energy errors on the order of one kilocalorie per mole,

ask whether there exist computational strategies that

1. achieve chemical accuracy for these observables,
2. do so with resource requirements that scale acceptably with system size and complexity,
3. remain compatible with known physical limits on information processing, noise, and thermodynamics.

Here “computational strategies” include:

* classical approximate methods such as Hartree Fock, coupled cluster, density functional theory, tensor network methods,
* fully quantum algorithms such as phase estimation, variational quantum eigensolvers, quantum imaginary time evolution,
* hybrid classical and quantum pipelines.

The problem for Q067 is **not** to construct a specific algorithm in this document. Instead, it is to capture, at the effective layer, the tension between

* the physical many body structure of molecules,
* the algorithmic difficulty of representing and evolving their quantum states,
* the practical limits of classical and quantum hardware.

The canonical statement itself is imported from the external scientific literature on quantum chemistry and quantum computing. TU does not modify that statement here.

### 1.2 Status and difficulty

Several facts are relevant.

1. In classical quantum chemistry there is a hierarchy of methods.

   * mean field approaches such as Hartree Fock,
   * low order perturbation and coupled cluster methods,
   * multi reference and strongly correlated techniques.

   These methods can often achieve chemical accuracy for small and moderately correlated systems. Their cost, however, typically grows steeply with system size, basis size, and correlation strength.

2. Quantum algorithms promise asymptotic advantages for simulating quantum systems. There are algorithmic families that, in principle, can approximate molecular eigenvalues with polynomial resources in some parameters. In practice

   * known gate counts and error correction overheads for chemically relevant systems remain extremely large,
   * near term noisy hardware severely constrains what can be done.

3. From the viewpoint of computational complexity, closely related problems such as ground state estimation of local Hamiltonians are QMA hard in general. This suggests that fully general, uniformly efficient algorithms for arbitrary quantum systems are unlikely.

4. Real molecules occupy a structured subset of all possible Hamiltonians. It remains an open problem to characterize which families of chemically relevant systems admit scalable, chemically accurate simulation on realistic hardware and which do not.

The canonical problem behind Q067 is therefore open. It sits at the intersection of quantum chemistry, computational complexity theory, and quantum information, and is widely regarded as central to turning quantum simulation into a practical tool for chemistry and materials science.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q067 has three main roles.

1. It is the flagship example of a **computational_tension** problem in chemistry, where physical fidelity, algorithmic cost, and correlation complexity must be balanced in a structured way.

2. It acts as a bridge node between

   * microscopic chemical structure (Q061, Q065, Q066),
   * fundamental quantum information limits (Q031, Q052),
   * thermodynamic resource constraints (Q059).

3. It supplies reusable components for

   * describing molecular complexity at the effective layer,
   * defining tension functionals that mix accuracy, cost, and correlation complexity,
   * constructing counterfactual worlds where chemistry is simulable versus worlds where it is intractable.

Nothing in this section depends on the specific encoding `E`. It provides the external target that the encoding in the following sections must respect.

---

## 2. Position in the BlackHole graph

This block records Q067’s position in the BlackHole graph. Each edge comes with a one line reason that points to a concrete component or tension type at the effective layer.

### 2.1 Upstream problems

Upstream nodes provide prerequisites, tools, or general foundations that Q067 relies on.

* Q031 (BH_PHYS_QINFO_L3_031)
  Reason: supplies general limits and structures of quantum information processing that bound possible simulation algorithms and error correction strategies.

* Q035 (BH_PHYS_QMETROLOGY_LIMIT_L3_035)
  Reason: provides physical limits on precision and noise that constrain what counts as achievable chemical accuracy in practice.

* Q052 (BH_CS_PVSBPP_L3_052)
  Reason: encodes the comparative power of quantum and classical computation, which shapes expectations for quantum simulation advantages.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: introduces thermodynamic cost frameworks for information processing, which Q067 uses to define realistic cost observables.

### 2.2 Downstream problems

Downstream nodes directly reuse Q067 components or treat Q067 as a prerequisite.

* Q063 (BH_CHEM_PROTEIN_FOLDING_L3_063)
  Reason: reuses molecular complexity descriptors and tension functionals to assess feasibility of quantum assisted protein folding simulations.

* Q061 (BH_CHEM_BOND_NATURE_L3_061)
  Reason: depends on Q067 style many body simulation components to probe strongly correlated chemical bonds at high fidelity.

* Q065 (BH_CHEM_ROOMTC_SUPER_L3_065)
  Reason: relies on Q067 style simulation tension analysis for candidate superconducting materials with complex electronic structure.

* Q066 (BH_CHEM_ELECTROCHEM_L3_066)
  Reason: reuses simulation cost and accuracy descriptors for electrochemical interfaces and redox processes.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: both Q032 and Q067 involve many body quantum systems where resource limits and accuracy tradeoffs are central.

* Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)
  Reason: both analyze strongly correlated quantum systems whose emergent behavior depends on subtle spectral and correlation structure.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: shares the difficulty of navigating large configuration spaces and complex energy landscapes, in a different physical regime.

### 2.4 Cross domain edges

Cross domain edges connect Q067 to other domains that reuse its components.

* Q081 (BH_NEURO_CONSCIOUS_HARD_L3_081)
  Reason: uses Q067’s simulation tension ideas as a conceptual contrast for the feasibility of quantum level brain models.

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: reuses molecular complexity descriptors and cost observables for climate relevant chemical processes such as atmospheric chemistry.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: treats Q067 style tension as an example of high stakes simulation where misalignment about feasibility and accuracy can have downstream risks.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer and depends on the fixed encoding `E` described in Section 0. We only describe

* state spaces,
* observables and fields,
* tension components and combined scores,
* singular sets and domain restrictions.

We do not specify any hidden TU generative rules or how internal fields are constructed from raw data.

### 3.1 State space

For the fixed encoding `E` we posit a semantic state space

```txt
M(E)
```

where each state

```txt
m in M(E)
```

represents a coherent simulation world configuration for a particular molecular system at a chosen resolution. At the effective layer, a state `m` includes:

* a **system descriptor**: nuclear charges, approximate geometry, qualitative correlation classification,
* a **representation descriptor**: basis set choice, active space specification, truncation scheme,
* an **algorithm descriptor**: classical method family, quantum algorithm class, or hybrid pipeline type,
* a **resource descriptor**: abstract resource budget such as logical gate counts, time to solution, memory footprint, possibly aggregated into a single cost scale,
* a **target descriptor**: which observables are to be computed and what error tolerances are required.

The encoding `E` specifies how these descriptors are constructed from user facing descriptions and from literature data. We only require that for each physically meaningful molecular instance and reasonable simulation setup there exist states in `M(E)` that encode them in a coherent way.

### 3.2 Observables and fields

The encoding `E` introduces the following effective observables

```txt
E_error(·; E), C_cost(·; E), R_res(·; E), F_corr(·; E), S_spec(·; E)
```

on `M(E)`.

1. Energy error observable

```txt
E_error: M(E) -> R_plus
```

For each `m` in `M(E)`, `E_error(m; E)` is a nonnegative scalar that summarizes the deviation between the simulated energy, or set of energies, and a trusted reference or ideal target for the configuration represented by `m`.

2. Computational cost observable

```txt
C_cost: M(E) -> R_plus
```

`C_cost(m; E)` represents an effective total cost, normalized to a consistent unit such as logical gate count, wall clock time, or a composite cost combining several resources on a fixed scale defined by `E`.

3. Resolution observable

```txt
R_res: M(E) -> R_plus
```

`R_res(m; E)` summarizes the resolution or expressiveness of the chosen representation, for example basis set size, active space dimension, or number of orbitals.

4. Correlation complexity observable

```txt
F_corr: M(E) -> R_plus
```

`F_corr(m; E)` measures the effective strength and complexity of electronic correlations captured in the configuration. It is an abstract indicator. Larger values correspond to stronger and more intricate correlations.

5. Spectral complexity observable

```txt
S_spec: M(E) -> R_plus
```

`S_spec(m; E)` captures features of the low energy spectrum such as density of low lying excitations or indicators tied to entanglement structure.

For all states in the regular domain `M_reg(E)` defined below, these observables take finite, well defined, real values.

Whenever we write `E_error(m)`, `C_cost(m)`, and so on, this should be read as shorthand for the corresponding encoding dependent observables.

### 3.3 Tension components

The encoding `E` fixes two global positive constants

```txt
epsilon_chem(E) > 0
C_budget(E)     > 0
```

and a reference cost scale map

```txt
f_corr_ref(·; E): R_plus × R_plus × R_plus -> R_plus
```

that together set the normalization for the three primary tension components.

1. Accuracy tension

```txt
DeltaS_accuracy(m; E) = max(0, E_error(m; E) / epsilon_chem(E) - 1)
```

* If `E_error(m; E)` is below the chemical accuracy threshold `epsilon_chem(E)` the accuracy tension vanishes.
* If `E_error(m; E)` exceeds the threshold, `DeltaS_accuracy(m; E)` grows linearly in the factor by which the error exceeds the threshold.

2. Cost tension

```txt
DeltaS_cost(m; E) = max(0, C_cost(m; E) / C_budget(E) - 1)
```

* If `C_cost(m; E)` is within the normalized cost budget, cost tension is zero.
* If `C_cost(m; E)` exceeds the budget, `DeltaS_cost(m; E)` measures the relative overshoot.

3. Complexity tension

First the encoding defines a reference cost scale

```txt
C_ref(m; E) = f_corr_ref(F_corr(m; E), R_res(m; E), S_spec(m; E); E)
```

where `C_ref(m; E)` is strictly positive and finite on `M_reg(E)`. Intuitively, `C_ref` represents the cost scale that would be expected from a reasonably well matched algorithm for this level of correlation and resolution.

The complexity tension is then

```txt
DeltaS_complexity(m; E) = max(0, C_cost(m; E) / C_ref(m; E) - 1)
```

This quantity is large when the actual cost for a configuration is significantly higher than what `E` deems appropriate for its correlation and resolution descriptors. It is zero when cost is at or below the reference scale.

The function `f_corr_ref(·; E)` and its dependence on correlation and resolution descriptors are part of `E` and therefore fixed by the encoding keys. Small continuous refinements of `f_corr_ref` fall under `RefinementKey`. Any change that qualitatively alters its behaviour beyond this requires a new `EncodingKey` or `LibraryKey`.

### 3.4 Combined tension functional and tensor

For the fixed encoding `E` we choose positive weights

```txt
alpha(E), beta(E), gamma(E) > 0
alpha(E) + beta(E) + gamma(E) = 1
```

encoded in the `WeightKey`. These are global for Q067 and cannot be tuned per molecule or per algorithm.

The combined Q067 simulation tension functional is

```txt
Tension_QSIM(m; E) =
  alpha(E) * DeltaS_accuracy(m; E)
+ beta(E)  * DeltaS_cost(m; E)
+ gamma(E) * DeltaS_complexity(m; E)
```

This functional satisfies:

* `Tension_QSIM(m; E) >= 0` for all `m` in `M_reg(E)`,
* `Tension_QSIM(m; E) = 0` only when all three tension components vanish,
* monotonicity in each component when the others are fixed.

Consistent with TU core conventions, the encoding also packages this into an effective tension tensor

```txt
T_ij(m; E) = S_i(m; E) * C_j(m; E) * Tension_QSIM(m; E) * lambda(m; E) * kappa(E)
```

where

* `S_i(m; E)` is a source like factor describing how strongly the ith source component depends on this simulation,
* `C_j(m; E)` is a receptivity factor describing how sensitive the jth downstream component is to errors or costs in this simulation,
* `lambda(m; E)` is a convergence state factor, indicating whether local reasoning is convergent, recursive, divergent, or chaotic,
* `kappa(E)` is a fixed coupling constant set by the encoding.

The index sets for `i` and `j` and the detailed form of `S_i`, `C_j`, and `lambda` are part of the encoding and are not needed at this effective level. It is enough that `T_ij(m; E)` is finite on the regular domain.

### 3.5 Singular set and domain restriction

Some configurations are ill formed or push the encoding outside its domain of validity. The encoding collects such cases in a singular set

```txt
S_sing(E) = {
  m in M(E) :
  any of E_error(m; E), C_cost(m; E), R_res(m; E),
  F_corr(m; E), S_spec(m; E)
  is undefined or not finite
}
```

and defines the regular domain

```txt
M_reg(E) = M(E) \ S_sing(E)
```

All Q067 tension analysis is restricted to `M_reg(E)`.

States in `S_sing(E)` do not provide evidence for or against the simulability of chemistry. They only signal that the particular encoding `E` has failed to provide coherent observables for those configurations. A different encoding might classify the same physical situation differently.

---

## 4. Tension principle for this problem

This block states how Q067 is characterized as a tension problem within TU for the fixed encoding `E`.

### 4.1 Admissible encoding class and fairness

We consider an admissible class of encodings

```txt
E_QSIM
```

where each encoding `E` in `E_QSIM` specifies

* how states in `M(E)` are constructed from high level descriptions of molecules, algorithms, and hardware assumptions,
* how the observables `E_error(·; E)`, `C_cost(·; E)`, `R_res(·; E)`, `F_corr(·; E)`, and `S_spec(·; E)` are computed,
* global constants `epsilon_chem(E)`, `C_budget(E)`, and the reference map `f_corr_ref(·; E)`,
* global weights `(alpha(E), beta(E), gamma(E))` with `alpha(E) + beta(E) + gamma(E) = 1`,
* the coupling structure for the tensor `T_ij(·; E)`.

Members of `E_QSIM` may differ in their modeling choices, cost normalizations, and representation of correlation complexity, provided they respect known physical and complexity constraints. They must not differ in ways that trivially eliminate tension for specific families by redefining thresholds after the fact.

The encoding keys play the following roles.

* `EncodingKey` tracks structural changes in the definition of the state space, observables, and singular set.
* `LibraryKey` tracks calibrated numerical tables, reference data mappings, and detailed settings of `f_corr_ref`.
* `WeightKey` tracks the choice of `(alpha, beta, gamma)`.
* `RefinementKey` tracks minor refinements, data updates, and calibration improvements that preserve the qualitative structure of the encoding.

Any change that moves beyond the scope of `RefinementKey` requires a new `EncodingKey` or `LibraryKey` or `WeightKey` and is treated as a different encoding.

Families of molecules or simulation tasks that are used to test Q067 must be specified **before** computing any tension values and **cannot** be reselected based on the outcomes in order to favour a particular encoding.

The verification level `E_level: E2` in the header refers to the fact that we are working with the encoding class `E_QSIM` and one concrete encoding `E` that satisfies these fairness conditions. A different encoding key would require renewed verification.

### 4.2 Q067 as a low tension principle

At the effective layer, Q067 can be framed as a **low tension principle**.

Fix

* the encoding class `E_QSIM` and a particular encoding `E` in this class,
* a family of chemically relevant molecules indexed by a size or complexity parameter `n`. The family definition must be independent of the eventual tension results.

Q067’s optimistic scenario asserts that there exist states

```txt
m_n in M_reg(E)
```

representing feasible simulation strategies for these molecules such that

```txt
Tension_QSIM(m_n; E) <= epsilon_QSIM(E)
```

for all `n` in the considered range, where `epsilon_QSIM(E)` is a modest encoding level constant that does not grow with `n` inside that family.

The low tension principle does not specify how large the range of `n` must be. It only says that within the region of chemistry of interest the simulation tension can be kept in a bounded low band through suitable choices of algorithms, representations, and hardware that remain within the constraints of `E`.

### 4.3 Q067 failure as persistent high tension

The contrasting scenario is that for some families of chemically natural molecules and realistic assumptions about hardware and noise, **any** admissible encoding and **any** coherent simulation strategy will incur high tension beyond acceptable bounds.

Formally, for a given family and any encoding `E` in `E_QSIM`, every sequence of states

```txt
m_n in M_reg(E)
```

representing feasible simulation attempts eventually satisfies

```txt
Tension_QSIM(m_n; E) >= delta_QSIM(E, n)
```

where

* `delta_QSIM(E, n)` is strictly positive for large enough `n`,
* for some thresholds this lower bound exceeds any acceptable tension band once `n` is large enough,
* the growth cannot be removed by changing algorithms, representations, or reasonable hardware assumptions within the constraints of `E`.

In this scenario high accuracy, reasonable cost, and realistic handling of correlation complexity are jointly incompatible beyond moderate sizes. Q067 at the effective layer then says that for those families the world forces us into high simulation tension.

The role of this block is not to decide which scenario is true. It defines what it would mean, within TU and for a specific encoding, for chemistry to be simulation low tension or simulation high tension.

---

## 5. Counterfactual tension worlds

We now sketch two counterfactual worlds at the effective layer for the fixed encoding `E`.

* World T: TU simulable chemistry, where simulation tension remains controllable for many relevant families.
* World F: intractable chemistry at scale, where simulation tension grows beyond acceptable bounds.

These worlds are expressed only in terms of observable patterns and tension scores. They do not expose any deep TU generative rules.

### 5.1 World T: TU simulable chemistry

In World T:

1. Bounded tension across families

   * For many chemically important families, such as organic molecules with bounded correlation complexity, moderate transition metal complexes, and key biomolecular fragments, there exist sequences of states `m_T(n)` in `M_reg(E)` such that

     ```txt
     Tension_QSIM(m_T(n); E) <= epsilon_QSIM(E)
     ```

     with `epsilon_QSIM(E)` modest and almost independent of `n` across the considered regime.

2. Balanced accuracy and cost

   * For these `m_T(n)` the individual tension components satisfy

     ```txt
     DeltaS_accuracy(m_T(n); E) <= epsilon_acc(E)
     DeltaS_cost(m_T(n); E)     <= epsilon_cost(E)
     ```

     for small encoding level constants `epsilon_acc(E)` and `epsilon_cost(E)` that do not grow with `n` across the relevant range.

3. Correlation aware strategies

   * As `F_corr(m_T(n); E)` and `S_spec(m_T(n); E)` increase for more correlated systems, encodings in `E_QSIM` can adjust representations and algorithms so that `DeltaS_complexity(m_T(n); E)` remains in a reasonable band.
   * New algorithmic ideas or hardware improvements might be needed, but the overall pattern remains one of bounded, manageable tension rather than runaway cost.

### 5.2 World F: intractable chemistry at scale

In World F:

1. Unavoidable high tension for some families

   * There exist families of chemically natural molecules and realistic hardware assumptions such that for any encoding `E` in `E_QSIM` and any sequence `m_F(n)` in `M_reg(E)` representing simulation attempts, one eventually has

     ```txt
     Tension_QSIM(m_F(n); E) >= delta_QSIM(E)
     ```

     where `delta_QSIM(E)` is a strictly positive constant that marks a high tension band.

2. Tradeoff breakdown

   * Attempts to suppress accuracy tension, pushing `DeltaS_accuracy(m_F(n); E)` below a small constant, lead to rapid growth in `DeltaS_cost(m_F(n); E)`.
   * Attempts to keep cost tension small, maintaining `DeltaS_cost(m_F(n); E)` near zero, force `E_error(m_F(n); E)` so high that accuracy tension remains large.

3. Correlation barrier

   * For strongly correlated systems increases in `F_corr(m_F(n); E)` and `S_spec(m_F(n); E)` lead to complexity tension that cannot be relieved without violating known complexity bounds or physical hardware limits encoded in `E`.
   * This manifests as `DeltaS_complexity(m_F(n); E)` that remains large despite reasonable changes in representations and algorithms.

In World F the persistence of high simulation tension is not an artifact of poor methods. It is a structural feature of the interplay between chemical structure, computational complexity, and the constraints captured in `E`.

### 5.3 Interpretive note

These counterfactual worlds do not assert which world we inhabit. They only state that if world models compatible with either scenario exist, then Q067’s observables and tension functionals can register the differences in a clean effective layer language.

Any concrete claim that our world behaves more like World T or World F for a specific family of molecules requires

* a fully specified encoding `E` in `E_QSIM`,
* empirical or literature data mapped into `M_reg(E)`,
* experiments of the kind described in Section 6.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can

* test the coherence and usefulness of the Q067 encoding for `E`,
* discriminate between different encodings in `E_QSIM`,
* reject encodings that fail to reflect known facts about quantum simulation in chemistry.

These experiments do not prove or disprove the canonical problem. They evaluate whether a particular effective layer encoding is acceptable.

### Experiment 1: Classical and quantum scaling in tension space

**Goal**

Assess whether a given encoding `E` for Q067 can represent and distinguish realistic tension patterns for classical and quantum simulation strategies across a benchmark ladder of molecules.

**Setup**

* Choose a family of benchmark molecules with increasing size and correlation complexity, for example

  * small organic molecules,
  * medium sized organic and inorganic molecules,
  * strongly correlated transition metal complexes.

* The definition of this family must be fixed and documented **before** any tension values are computed.

* For each molecule and each simulation strategy, collect from the literature or controlled studies

  * best known classical methods and their estimated costs and errors,
  * proposed quantum algorithms where available and their estimated logical costs and errors under reasonable hardware assumptions.

* Fix a single encoding `E` in `E_QSIM`. In particular

  * record `EncodingKey`, `LibraryKey`, `WeightKey`, `RefinementKey` for this experiment,
  * fix `epsilon_chem(E)`, `C_budget(E)`, `(alpha(E), beta(E), gamma(E))`,
  * fix the mapping from algorithm descriptions and hardware assumptions to `C_cost(m; E)`.

All of these choices must be made **before** computing any `Tension_QSIM` values. They must not be altered in response to preliminary results for particular molecules or methods.

**Protocol**

1. For each molecule and each simulation strategy construct a state `m_data` in `M_reg(E)` that encodes

   * the system class and correlation characteristics,
   * representation choices,
   * algorithm type and hardware assumptions,
   * estimated `E_error(m_data; E)` and `C_cost(m_data; E)`,
   * indicators `F_corr(m_data; E)` and `S_spec(m_data; E)`.

2. Compute `DeltaS_accuracy(m_data; E)`, `DeltaS_cost(m_data; E)`, `DeltaS_complexity(m_data; E)` using the formulas in Section 3.

3. Compute `Tension_QSIM(m_data; E)` for all strategies and system sizes.

4. Plot or tabulate `Tension_QSIM(m_data; E)` as a function of problem size or correlation complexity for classical and quantum strategies.

**Metrics**

* For each size or complexity level

  * minimum, maximum, and average `Tension_QSIM` across strategies,
  * relative ranking of classical versus quantum methods.

* Scaling behaviour

  * how `Tension_QSIM` changes with size for each class of methods,
  * whether any class shows systematically lower tension in plausible regimes.

**Falsification conditions**

The encoding `E` is considered misaligned with known facts if, for example

* in regimes where classical simulation is already clearly feasible and quantum proposals are immature, `E` assigns significantly lower `Tension_QSIM` to speculative quantum methods than to mature classical methods without support from the cost and error data,
* in regimes where there is strong consensus that quantum methods offer no practical benefit, `E` cannot produce tension patterns where classical methods are at least competitive.

If small variations that remain within the scope of `RefinementKey` produce arbitrarily different qualitative tension rankings for the same data, the encoding class is considered too unstable and must be revised.

**Semantics note**

All quantities are treated within the hybrid semantics of `E`, with continuous fields for costs and errors and discrete descriptors for algorithm types and basis choices.

**Boundary note**

Falsifying an encoding for Q067 in this experiment does not solve the canonical problem. It only rejects that encoding as a faithful effective layer representation of known simulation behaviour.

---

### Experiment 2: Active space refinement tension ladder

**Goal**

Test whether Q067’s tension components behave plausibly under systematic refinement of representations for strongly correlated molecules.

**Setup**

* Select a small set of strongly correlated molecular systems, for example

  * transition metal dimers,
  * small clusters with open shell character,
  * molecules known to be challenging for single reference methods.

* For each system, construct a **refinement ladder** of simulation setups consisting of discrete rungs with

  * increasing active space size,
  * improved basis sets,
  * more sophisticated correlation treatments.

The refinement ladder must be defined and documented before any tension computations. Its steps cannot be altered retrospectively in response to observed tension trends.

* Use a single encoding `E` in `E_QSIM` with fixed thresholds, weights, and reference maps. Record all four keys as in Experiment 1.

**Protocol**

1. For each rung `k` of the refinement ladder construct a state `m_ref(k)` in `M_reg(E)` encoding

   * the chosen active space and basis,
   * the correlation method class,
   * estimated or measured `E_error(m_ref(k); E)` and `C_cost(m_ref(k); E)`,
   * updated correlation and spectral indicators.

2. Compute `DeltaS_accuracy(m_ref(k); E)`, `DeltaS_cost(m_ref(k); E)`, `DeltaS_complexity(m_ref(k); E)`, and `Tension_QSIM(m_ref(k); E)`.

3. Trace how each tension component and the combined tension change as `k` increases.

**Metrics**

For each system:

* the sequence of accuracy, cost, and complexity tensions along the ladder,
* locations where improvements in accuracy flatten out or where cost and complexity start to dominate.

Qualitative patterns:

* whether there is an initial regime where tension decreases or stabilizes,
* whether beyond some rung tension inevitably grows, indicating diminishing returns.

**Falsification conditions**

The encoding `E` is considered incoherent if, for example

* in a refinement ladder where `E_error(m_ref(k); E)` steadily decreases and both `C_cost(m_ref(k); E)` and correlation indicators grow in ways consistent with known algorithmic scaling, `Tension_QSIM(m_ref(k); E)` shows unmotivated oscillations or non monotonic jumps without clear tradeoff explanations,
* in regimes where practitioners widely agree that further refinement is practically hopeless, the encoding keeps `Tension_QSIM(m_ref(k); E)` artificially in a low band across many rungs.

**Semantics note**

Refinement is modeled as a discrete sequence inside the hybrid semantics of `E`. No infinite resolution limits are taken. We work with finite, realistic ladders.

**Boundary note**

As before, falsifying or supporting an encoding through this experiment does not settle the canonical Q067 problem. It only tests whether the tension functional tracks realistic refinement behaviour.

---

## 7. AI and WFGY engineering spec

This block describes how Q067 can be used as an engineering module for AI systems within WFGY at the effective layer, for the fixed encoding `E`.

All signals and modules described here are **effective layer tools**. They must not be interpreted as evidence that the canonical Q067 problem has been solved. They only organize reasoning about feasibility and tradeoffs.

### 7.1 Training signals

The encoding `E` yields several training signals derived from Q067 observables and tension components.

1. `signal_chem_accuracy_tension`

   * Definition

     ```txt
     signal_chem_accuracy_tension(m; E) = DeltaS_accuracy(m; E)
     ```

   * Purpose

     Penalize internal states or outputs that imply chemically relevant quantities can be computed with errors far above the target accuracy scale while pretending they are acceptable.

2. `signal_cost_realism`

   * Definition

     ```txt
     signal_cost_realism(m; E) = DeltaS_cost(m; E)
     ```

   * Purpose

     Discourage reasoning patterns where the model proposes simulation schemes whose cost is far beyond any realistic budget without surfacing this fact.

3. `signal_corr_awareness`

   * Definition

     ```txt
     signal_corr_awareness(m; E) = DeltaS_complexity(m; E)
     ```

   * Purpose

     Encourage the model to adjust its claims when dealing with strongly correlated molecules, instead of extrapolating intuition from weakly correlated cases.

4. `signal_qsim_tension_total`

   * Definition

     ```txt
     signal_qsim_tension_total(m; E) = Tension_QSIM(m; E)
     ```

   * Purpose

     Provide a single scalar summary of overall simulation tension for use as an auxiliary loss or diagnostic output.

All these signals depend on the encoding `E`. If a different encoding is used, signals must be recalibrated.

### 7.2 Architectural patterns

We outline module patterns for AI systems that reuse Q067 structures.

1. `QSIM_TensionHead`

   * Role

     Given an internal representation of a quantum chemistry or materials simulation query, predict the components of simulation tension and the combined score.

   * Interface

     ```txt
     inputs: internal_embeddings_for_query
     outputs: tension_total, (DeltaS_accuracy, DeltaS_cost, DeltaS_complexity)
     ```

     All outputs are interpreted as estimates of the encoding dependent quantities for some implicit state `m` in `M_reg(E)`.

2. `ActiveSpacePlanner`

   * Role

     Suggest refinement steps in basis and active space choices that trade accuracy against cost while monitoring tension components.

   * Interface

     ```txt
     inputs: current_state_descriptor, target_accuracy_band
     outputs: candidate_next_descriptor, expected_tension_change
     ```

3. `ComplexityGuard`

   * Role

     Check whether proposed simulation strategies implicitly violate known complexity or hardware limits, using correlation and cost indicators.

   * Interface

     ```txt
     inputs: simulation_plan_descriptor
     outputs: guard_score  (low means safe, high means likely unrealistic)
     ```

Each of these modules must carry along the encoding keys so users can see which version of `E` generated its diagnostics.

### 7.3 Evaluation harness

We propose an evaluation harness for AI models augmented with Q067 modules.

1. Task set

   A curated benchmark of questions and design tasks such as

   * “Is this simulation of a large correlated molecule realistic on near term hardware”
   * “Which approximations are acceptable to reach chemical accuracy here”
   * “Compare two simulation strategies in terms of feasibility and reliability”.

2. Conditions

   * Baseline condition

     The model answers without explicit Q067 modules or tension based signals.

   * TU augmented condition

     The model uses `QSIM_TensionHead`, `ActiveSpacePlanner`, and `ComplexityGuard` as auxiliary tools.

3. Metrics

   * rate at which the model proposes obviously unrealistic simulation claims,
   * internal consistency of cost and accuracy statements across multiple steps,
   * agreement with expert assessments on which regimes are feasible and which are likely intractable.

Differences between baseline and TU augmented conditions provide evidence about the usefulness of Q067 for shaping AI behaviour, but they do not change the canonical status of Q067.

### 7.4 Sixty second reproduction protocol

A minimal protocol for external users.

* **Baseline setup**

  * Prompt

    Ask the AI “Can we exactly simulate this complex correlated molecule to chemical accuracy on current hardware” and provide a short description of the molecule. Do not mention tension or TU.

  * Observation

    Record whether the answer is vague, over optimistic, or ignores cost and correlation issues.

* **TU encoded setup**

  * Prompt

    Ask the same question but add instructions such as “explicitly reason about simulation tension, including accuracy, cost, and correlation complexity, using Q067 style observables for the current encoding E”.

  * Observation

    Check whether the answer now discusses correlation difficulty, cost versus accuracy tradeoffs, and realistic hardware constraints.

* **Comparison metric**

  * Use a rubric that scores explanations on

    * explicit mention of tradeoffs,
    * realism of cost assumptions,
    * clarity about what is currently possible.

* **What to log**

  * Prompt text, model responses, any internal estimates of `Tension_QSIM` and its components produced by `QSIM_TensionHead`.
  * The encoding keys must be logged along with the results.

Again, improvements in this protocol show that Q067 provides useful structure for AI behaviour. They do not count as evidence that the canonical open problem has been resolved.

---

## 8. Cross problem transfer template

This block lists reusable components produced by Q067 for the fixed encoding `E` and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `QSIM_TensionFunctional`

   * Type

     functional

   * Minimal interface

     ```txt
     inputs:
       E_error_value,
       C_cost_value,
       F_corr_value,
       S_spec_value,
       resolution_descriptor,
       encoding_keys
     output:
       tension_value
     ```

   * Preconditions

     * Inputs must represent coherent summaries for a single simulation configuration in `M_reg(E)`.
     * The thresholds and weights are those defined by `encoding_keys`, which specify `E`.
     * Users must record which encoding keys were used when tension values are reported.

2. ComponentName: `MolecularComplexityDescriptor`

   * Type

     field

   * Minimal interface

     ```txt
     inputs:
       system_descriptor,
       encoding_keys
     outputs:
       (size_parameter, correlation_indicator, spectral_complexity_indicator)
     ```

   * Preconditions

     * The system descriptor provides enough information to classify molecules along size and correlation dimensions.
     * The mapping from descriptors to indicators is defined by `E` and its keys, and should not be altered per molecule.

3. ComponentName: `ActiveSpaceRefinementPattern`

   * Type

     experiment_pattern

   * Minimal interface

     ```txt
     inputs:
       initial_simulation_descriptor,
       refinement_steps,
       encoding_keys
     outputs:
       ladder_of_descriptors_with_expected_tension_trends
     ```

   * Preconditions

     * The refinement steps are realistic and consistent with quantum chemistry practice.
     * The ladder is fixed before tension trends are computed.
     * Reports of tension trends must include the encoding keys.

### 8.2 Direct reuse targets

1. Q063 (BH_CHEM_PROTEIN_FOLDING_L3_063)

   * Reused components

     `MolecularComplexityDescriptor`, `ActiveSpaceRefinementPattern`.

   * Why it transfers

     Protein folding simulations involve complex energy landscapes and interaction patterns. These components help describe where enhanced classical or quantum simulations might be feasible and how refinement ladders behave.

   * What changes

     System descriptors now refer to biomolecular fragments and coarse grained models rather than small molecules. The basic structure of refinement ladders and tension trends remains the same.

2. Q061 (BH_CHEM_BOND_NATURE_L3_061)

   * Reused components

     `QSIM_TensionFunctional`, `MolecularComplexityDescriptor`.

   * Why it transfers

     Understanding chemical bonds in strongly correlated systems requires careful control over accuracy and cost in local many body simulations.

   * What changes

     The focus shifts toward bond centered observables and local descriptors, but the underlying tension between correlation complexity and simulation resources is the same.

3. Q065 (BH_CHEM_ROOMTC_SUPER_L3_065)

   * Reused components

     all three listed above.

   * Why it transfers

     Candidate high temperature superconductors often involve large, strongly correlated unit cells with complex electronic structures that are difficult to simulate.

   * What changes

     The notion of chemical accuracy is adapted to observables such as pairing gaps, critical temperatures, or phase boundaries. Cost and correlation descriptors follow the Q067 style, and encoding keys ensure that differences in targets are tracked.

---

## 9. TU roadmap and verification levels

This block explains Q067’s place on the TU verification ladder for the fixed encoding `E` and identifies next steps.

### 9.1 Current levels

* **E_level: E2**

  * Effective layer observables, tension components, a combined tension functional, and a singular set have been specified for encoding `E`.
  * Concrete experiment templates with falsification conditions are given for encodings in `E_QSIM`.

* **N_level: N2**

  * Narrative links between physical chemistry, computational cost, and TU tension are explicit and coherent.
  * World T and World F counterfactuals are defined in terms of observable tension patterns.

These levels apply to the specific encoding `E` named in Section 0. Changing encoding keys in a way that alters observables or tension definitions would require re evaluation of these levels.

### 9.2 Next measurable steps toward E3 and N3

To advance toward **E3** for Q067 and encoding `E` at the effective layer:

1. Implement at least one concrete encoding instance of `E` by

   * mapping actual literature data for a benchmark set of molecules and simulation methods into `M_reg(E)`,
   * computing `Tension_QSIM` values and publishing them as open data tagged with encoding keys.

2. Run Experiment 1 and Experiment 2 with real or realistically simulated numbers and document

   * whether tension patterns align with expert expectations,
   * which parts of the encoding need adjustment within the scope of `RefinementKey`.

To advance toward **N3**:

1. Build a cross domain narrative that connects Q067’s simulation tension concepts to

   * Q061 and Q065 in chemistry,
   * Q031 and Q052 in quantum information and complexity,
   * Q121 in AI alignment.

2. Demonstrate that this narrative can be communicated to specialists in each domain without requiring any knowledge of deeper TU layers.

All these steps remain at the effective layer. They do not rely on revealing any generative TU rules.

### 9.3 Long term role in the TU program

In the long term Q067 is intended to serve as

* the reference node for computational tension problems involving quantum many body systems in chemistry,
* a calibration point where claims about quantum advantage and practical feasibility can be grounded in a structured tension formalism,
* a bridge between theoretical complexity results and engineering level decisions about simulation pipelines.

Q067 is also a natural test bed for evaluating TU augmented AI systems that reason about scientific feasibility and resource constraints.

---

## 10. Elementary but precise explanation

This block gives a non technical explanation that remains faithful to the effective layer description for Q067 and encoding `E`.

Chemists want to predict what molecules will do. For simple molecules current methods already work very well. For large or strongly correlated molecules the problem becomes much harder.

People hope that quantum computers will one day let us simulate complicated molecules exactly, or at least well enough to design new drugs and materials. At the same time there are reasons to think that some of these problems might always demand huge resources.

Q067 does not try to answer the full question for all molecules. Instead it builds a careful language for talking about the **tension** in these simulations.

In this language every simulation attempt is described by three main ingredients.

* How accurate it is, measured by an error scale compared to a chemical accuracy target.
* How much computational effort it needs, measured in some consistent cost unit.
* How complicated the molecule’s quantum behaviour is, summarized by indicators of correlation and spectral complexity.

From these pieces Q067 defines three partial tensions, one for accuracy, one for cost, and one for complexity, then combines them into a single simulation tension number. Low tension means “good enough accuracy at reasonable cost for this level of complexity”. High tension means “something important is not matching the targets”.

Q067 then asks us to imagine two types of worlds.

* In a simulable chemistry world, for the molecules we care most about, we can keep simulation tension low by choosing smart methods and using realistic hardware.
* In an intractable chemistry world, for some families of molecules, simulation tension stays high no matter what we try, unless we accept huge costs or poor accuracy.

This way of thinking does not decide which world we live in. It does three more modest but concrete things.

1. It gives precise rules for how to measure simulation tension in a way that cannot be easily cheated by changing thresholds after the results are known.
2. It sets up experiments and data analyses that can tell us whether a particular encoding of tension matches what chemists and physicists already know.
3. It provides reusable tools that other hard problems, such as protein folding or superconductivity, can borrow when they need to talk about the limits of simulation.

In this sense Q067 turns a vague question about “whether quantum computers will solve chemistry” into a structured, testable story about how accuracy, cost, and complexity pull against each other in the space of possible worlds.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S problem collection. It specifies an effective layer encoding of Q067 for a single fixed encoding `E` in the class `E_QSIM`.

### Scope of claims

* The goal of this document is to describe how the canonical Q067 problem is encoded at the effective layer in terms of state spaces, observables, and tension functionals.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new axiom system or deep TU generative rule.
* It should not be cited as evidence that exact quantum simulation of complex molecules is possible or impossible.

### Effective-layer boundary

The following objects are effective layer constructs relative to the encoding `E`:

* state spaces and domains: `M(E)`, `M_reg(E)`, `S_sing(E)`
* observables and fields: `E_error(·; E)`, `C_cost(·; E)`, `R_res(·; E)`, `F_corr(·; E)`, `S_spec(·; E)`
* tension components: `DeltaS_accuracy(·; E)`, `DeltaS_cost(·; E)`, `DeltaS_complexity(·; E)`
* combined tension and tensor: `Tension_QSIM(·; E)`, `T_ij(·; E)`
* encoding class and constants: `E_QSIM`, `epsilon_chem(E)`, `C_budget(E)`, `f_corr_ref(·; E)`, `(alpha(E), beta(E), gamma(E))`
* reusable components and patterns in Section 8, including `QSIM_TensionFunctional`, `MolecularComplexityDescriptor`, and `ActiveSpaceRefinementPattern`
* experiment and evaluation templates in Sections 6 and 7.

All of these are subject to the encoding keys specified for `E`. States in `S_sing(E)` mark the boundary where this effective description fails. They do not constrain what any deeper TU model might do.

### Encoding and fairness constraints

* Thresholds, weights, and reference maps are fixed at the encoding level and must not be tuned per molecule or per algorithm.
* Benchmark families, refinement ladders, and cost mappings used in experiments must be defined before tension values are examined.
* Any change that goes beyond small continuous refinements requires new encoding keys and counts as a different encoding.

When experimental results or AI behaviour are reported using this encoding, the four keys

```txt
EncodingKey, LibraryKey, WeightKey, RefinementKey
```

must be recorded so that others can reproduce and audit the mapping between data and tension values.

### Relation to TU charters

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

Those charters define the global rules that any effective layer encoding, including this one, must satisfy.
