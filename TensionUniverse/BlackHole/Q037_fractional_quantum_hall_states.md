<!-- QUESTION_ID: TU-Q037 -->
# Q037 · Full classification of fractional quantum Hall states

## 0. Header metadata

```txt
ID: Q037
Code: BH_PHYS_QHALL_FRACTIONAL_L3_037
Domain: Physics
Family: Condensed matter (quantum Hall)
Rank: S
Projection_dominance: P
Field_type: analytic_field
Tension_type: topological_tension
Status: Encoded_E1_Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-31
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe framework.

* This page specifies an effective layer encoding of the fractional quantum Hall (FQH) classification problem.
* It only describes state spaces, descriptor libraries, invariants, tension scores, counterfactual worlds, and experiments that operate on those objects.
* It does not specify any TU core axiom system, any generative rule for TU fields, or any construction that maps microscopic Hamiltonians and wavefunctions to TU core objects.
* It does not claim to provide a complete or final classification of all FQH phases under realistic physical assumptions.
* It does not introduce any new theorem beyond what is already established or standard in the cited literature.
* It should not be cited as evidence that the FQH classification problem has been solved.

All falsifiability and experiment statements in this document concern finite encodings and admissible libraries at the effective layer. They do not assert facts about the unique true structure of microscopic many body quantum theory.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Fractional quantum Hall (FQH) states are strongly correlated phases of two dimensional electrons, or related quasiparticles, in a strong magnetic field, exhibiting:

* quantized Hall conductance at rational filling fractions `nu = p/q`,
* topologically protected edge modes,
* quasiparticle excitations with anyonic statistics,
* robust gap protection against local perturbations.

The canonical classification problem can be stated as:

> Given physically reasonable assumptions on locality, gauge structure, symmetries, and energy gaps, produce a complete and non redundant classification of all possible fractional quantum Hall phases in two dimensions, together with a matching low energy field theory description and anyon content, such that:
>
> 1. Every physically realizable gapped FQH phase fits into exactly one equivalence class in the classification.
> 2. Each equivalence class is represented by a well defined set of topological data, for example a Chern Simons theory, modular tensor category, or equivalent structure.
> 3. No spurious classes are included that cannot correspond to any physically allowed phase under the stated assumptions.

This includes both Abelian and non Abelian FQH states, and must handle issues such as:

* Landau level mixing within a controlled regime,
* disorder and realistic interactions within stated bounds,
* symmetry enriched variants and constraints,
* relation to lattice based fractional Chern insulators where appropriate.

### 1.2 Status and difficulty

Major partial structures are known.

* For many Abelian FQH states, K matrix Chern Simons theories give an effective classification up to equivalence under integer transformations.
* Composite fermion theory organizes large families of observed fractions through effective integer quantum Hall physics in transformed variables.
* Several non Abelian candidate states, for example Moore Read type and related series, have well studied topological field theory descriptions.
* Topological order and modular tensor category frameworks give abstract classification tools for unitary two plus one dimensional topological quantum field theories.

However, a complete classification that satisfies the canonical statement is still out of reach.

* Known schemes may overcount phases by giving different descriptions for the same physical phase, or undercount them by missing allowed topological orders.
* The relation between abstract topological orders and microscopically realizable FQH states is only partially understood.
* Symmetry, disorder, and lattice effects complicate the mapping between field theory data and experimental phases.
* There is no widely accepted finite and verifiable list of all FQH phases satisfying realistic physical constraints.

The problem is therefore treated as an open S level challenge that links condensed matter physics, topology, and quantum information.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q037:

1. Serves as the primary condensed matter example of `topological_tension`, where misalignment between classification labels, consistency axioms, and realized phases produces tension.
2. Links the general classification of quantum phases of matter (Q030) with concrete strongly correlated systems and emergent anyons.
3. Supplies a template for how TU encodes finite library classification problems with refinement ladders and fairness constraints on libraries and coupling rules.
4. Acts as a bridge between physical topological order problems (Q038, Q039) and information theoretic or AI oriented problems that involve discrete invariants coupled to continuous fields.

### References

1. X. G. Wen, Quantum Field Theory of Many Body Systems, Oxford University Press, 2004.
2. J. K. Jain, Composite Fermions, Cambridge University Press, 2007.
3. A. Stern, Anyons and the quantum Hall effect, Annals of Physics 323, 204–249 (2008).
4. C. Nayak, S. H. Simon, A. Stern, M. Freedman, S. D. Sarma, Non Abelian anyons and topological quantum computation, Reviews of Modern Physics 80, 1083–1159 (2008).

---

## 2. Position in the BlackHole graph

This block describes how Q037 sits in the BlackHole graph among Q001 to Q125.

### 2.1 Upstream problems

These provide foundations, tools, or conceptual scaffolding that Q037 relies on.

* Q030 (BH_PHYS_QPHASE_MATTER_L3_030)
  Reason: Supplies the general framework for classifying quantum phases of matter, including topological order and equivalence relations between phases.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Provides concepts of entanglement, information flow, and thermodynamic like constraints that apply to gapped topological phases.

* Q035 (BH_PHYS_QCRITICALITY_L3_035)
  Reason: Encodes criticality and phase transition structures that bound the domain where FQH phases are robustly gapped and classifiable.

### 2.2 Downstream problems

These reuse Q037 components or depend on its tension structure.

* Q038 (BH_PHYS_QCOLD_ATOMS_L3_038)
  Reason: Reuses FQH classification tension to organize strongly correlated cold atom phases that simulate FQH like topological orders.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Uses Q037 finite library and invariant based tension schema as a template for classifying information theoretic resource states with topological structure.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Reuses discrete invariant and continuous field coupling patterns from Q037 as an analogy for classifying internal AI representations.

### 2.3 Parallel problems

Parallel nodes share similar tension types but do not depend directly on Q037 components.

* Q036 (BH_PHYS_QSUPCOND_MEC_L3_036)
  Reason: Both Q036 and Q037 concern emergent topological like structures in strongly correlated systems described by effective field theories.

* Q039 (BH_PHYS_QTURBULENCE_L3_039)
  Reason: Both involve complex many body fields where global invariants constrain possible patterns and give rise to topological_tension.

### 2.4 Cross domain edges

Cross domain edges connect Q037 to nodes in other domains that can reuse its components.

* Q001 (BH_MATH_NUM_L3_001)
  Reason: Reuses Q037 finite library and refinement ladder patterns for spectral tension functionals in number theory.

* Q010 (BH_CS_QINFO_TOPO_L3_010)
  Reason: Can reuse the notion of discrete topological invariants coupled to continuous control parameters for classifying quantum codes and topological information carriers.

* Q040 (BH_PHYS_QBLACKHOLE_INFO_L3_040)
  Reason: Uses classification tension ideas to organize possible black hole microstate and horizon topological order scenarios.

---

## 3. Tension Universe encoding (effective layer)

All content in this block stays strictly at the effective layer. We only describe:

* state spaces,
* observables and effective fields,
* invariants and tension scores,
* singular sets and domain restrictions,
* finite libraries and refinement ladders.

We do not describe any hidden generative rules or procedures that map raw microscopic data to these objects, and we do not expose any TU core axiom machinery.

**Hybrid semantics note.**
The metadata flag `Semantics: hybrid` indicates that Q037 uses a mix of discrete and continuous objects at the effective layer.

* Discrete parts include topological descriptors, anyon labels, fusion and braiding data, and invariant tuples.
* Continuous parts include filling fractions, gap estimates, coupling ranges, and other coarse physical parameters.
* All of these are represented in finite dimensional summaries. We do not work with full infinite dimensional Hilbert spaces or exact microscopic Hamiltonians in this encoding.

### 3.1 State space

We assume a semantic state space

`M`

with the following effective interpretation.

Each `m` in `M` is a coarse grained FQH classification configuration that includes:

* a candidate low energy topological description, for example a Chern Simons theory or equivalent topological order object,
* a set of discrete labels summarizing anyon types, fusion rules, and braiding data,
* a set of continuous parameters, for example filling fraction ranges, coupling ranges, or gap estimates,
* a record of which microscopic FQH states are claimed to be covered by this configuration.

We do not specify how these objects are extracted from wavefunctions or Hamiltonians. We only assume that for any finite set of known or conjectured FQH phases and any reasonable resolution scale there exist states in `M` that encode a proposed classification of those phases.

### 3.2 Finite libraries, refinement ladder, and encoding class

To avoid unconstrained adjustment of encodings, we introduce the following objects at each refinement level `k`.

1. A finite library of topological descriptors at level `k`:

   ```txt
   L_topo(k) = { D_1(k), D_2(k), ..., D_N(k) }
   ```

   where each `D_i(k)` is a possible low energy topological description constrained by:

   * bounded matrix size or equivalent structural complexity,
   * bounded levels or coupling integers,
   * fixed symmetry assumptions that are declared in advance.

2. A finite library of classification invariants at level `k`:

   ```txt
   L_inv(k) = { I_1(k), I_2(k), ..., I_M(k) }
   ```

   where each `I_j(k)` is a rule for mapping a descriptor in `L_topo(k)` to a finite tuple of discrete and continuous invariants.

3. A refinement map:

   ```txt
   refine(k) -> k + 1
   ```

   with the following properties.

   * `L_topo(k+1)` strictly contains `L_topo(k)` and extends it by adding more complex descriptors according to a fixed structural rule, for example allowing larger matrices or additional symmetry types.
   * `L_inv(k+1)` refines `L_inv(k)` by adding new invariants, but does not change the definition of existing invariants at lower levels.
   * The rules that define `L_topo(k)` and `L_inv(k)` for all `k` are fixed at the level of the encoding and do not depend on the actual realized FQH phases or on observed data.

An effective FQH encoding is a tuple

```txt
E = (L_topo(·), L_inv(·), refine(·), w_axiom, w_equiv, w_real)
```

The admissible encoding class

```txt
E_FQH
```

is the set of all such `E` that satisfy:

* finiteness of `L_topo(k)` and `L_inv(k)` for every finite `k`,
* refinement rules that are declared once and reused without data dependent changes,
* weights `w_axiom`, `w_equiv`, `w_real` that satisfy the constraints in Section 3.4 and are fixed once for all levels and all datasets,
* additional fairness and stability constraints stated in Sections 3.4, 4, and 6.

All later definitions of mismatch observables, tension functionals, and experiments are understood to be parameterized by some admissible `E` in `E_FQH`.

### 3.3 Effective observables and mismatch measures

We introduce the following observables on `M` for a given refinement level `k` and admissible encoding `E` in `E_FQH`.

1. A consistency mismatch observable:

   ```txt
   DeltaS_axiom(m; E, k)
   ```

   * Input: state `m`, encoding `E`, and refinement level `k`.

   * Output: nonnegative scalar measuring violations of basic topological and physical consistency constraints for descriptors taken from `L_topo(k)` under encoding `E`.

   * Examples of constraints encoded at the effective level include:

     * modularity and non degeneracy of the topological S and T data,
     * compatibility with charge conservation and locality,
     * existence of a stable energy gap under allowed perturbations.

   * Properties:

     ```txt
     DeltaS_axiom(m; E, k) >= 0
     DeltaS_axiom(m; E, k) = 0 only if all encoded descriptors at level k satisfy the declared consistency constraints
     ```

2. An equivalence mismatch observable:

   ```txt
   DeltaS_equiv(m; E, k)
   ```

   * Input: state `m`, encoding `E`, and level `k`.
   * Output: nonnegative scalar measuring mismatch between equivalence classes of phases and the invariant tuples from `L_inv(k)` under encoding `E`.
   * It penalizes both under separation and over separation.

     * different phases that are assigned the same invariant tuple,
     * identical phases that are assigned distinct invariant tuples.

3. A realization mismatch observable:

   ```txt
   DeltaS_real(m; E, k)
   ```

   * Input: state `m`, encoding `E`, and level `k`.

   * Output: nonnegative scalar measuring mismatch between:

     * phases predicted by descriptors in `L_topo(k)` under `E`, and
     * phases actually realized or strongly supported in experiments or microscopic models.

   * It penalizes:

     * descriptors with no plausible realization within stated physical constraints,
     * observed FQH phases that cannot be mapped to any descriptor in `L_topo(k)` at that level.

All three mismatch observables are defined at the effective layer, and their detailed implementation is part of the encoding `E`. Their functional forms are fixed as part of `E` and do not change when datasets change.

### 3.4 Classification tension functional

At refinement level `k` and for encoding `E` in `E_FQH` we define the FQH classification tension

```txt
Tension_FQH(m; E, k) =
    w_axiom * DeltaS_axiom(m; E, k) +
    w_equiv * DeltaS_equiv(m; E, k) +
    w_real  * DeltaS_real(m; E, k)
```

where `w_axiom`, `w_equiv`, and `w_real` are nonnegative weights satisfying

```txt
w_axiom + w_equiv + w_real = 1
w_axiom, w_equiv, w_real in [w_min, w_max]
```

for some constants `0 < w_min <= w_max < 1` that are chosen once for the encoding `E` and reused for all levels and all datasets.

Fairness constraints for weights and functionals.

* The weights are determined by structural considerations, for example the relative importance of consistency, non redundancy, and realizability, and are fixed before any evaluation against world data.
* The definitions of `DeltaS_axiom`, `DeltaS_equiv`, and `DeltaS_real` are fixed once for all `k`, except for the explicit dependence on which descriptors and invariants are present at that level.
* Refinement by increasing `k` may add descriptors and invariants according to the predetermined `refine` rule but cannot change the functional forms or the weights in response to data outcomes.
* Any search for low tension states `m` must operate within a fixed encoding `E in E_FQH` and is not allowed to retune weights or rewrite mismatch functionals.

Under these constraints, `Tension_FQH` is the concrete realization of the `topological_tension` type declared in the header metadata for Q037.

### 3.5 Tension tensor and singular set

We couple the classification tension into an effective tension tensor on `M` at level `k` and encoding `E`.

```txt
T_ij(m; E, k) = S_i(m; E, k) * C_j(m; E, k) * Tension_FQH(m; E, k) * lambda(m; E, k) * kappa_FQH
```

where:

* `S_i(m; E, k)` encodes source like factors such as how strongly the ith component of the classification is engaged, for example how many phases it claims to cover.
* `C_j(m; E, k)` encodes receptivity like factors such as how sensitive the jth downstream object is to classification errors.
* `Tension_FQH(m; E, k)` is the scalar classification tension defined above.
* `lambda(m; E, k)` is a bounded convergence state indicator imported abstractly from the general TU core but not constructed or exposed in this page.
* `kappa_FQH` is a fixed coupling constant that sets the overall scale of topological_tension for Q037.

Some states may lead to undefined or unbounded mismatch measures. We collect such states into a singular set

```txt
S_sing(E, k) = {
  m in M :
  DeltaS_axiom(m; E, k), DeltaS_equiv(m; E, k), or DeltaS_real(m; E, k)
  is undefined or not finite
}
```

Domain restriction.

* All quantitative analyses of Q037 at the effective layer are restricted to `M_reg(E, k) = M \ S_sing(E, k)`.
* Whenever an experiment or protocol would evaluate `Tension_FQH(m; E, k)` for `m` in `S_sing(E, k)`, the result is treated as out of domain rather than as evidence for or against any classification claim about the physical world.

---

## 4. Tension principle for this problem

This block states how Q037 is framed as a tension problem inside TU.

### 4.1 Core classification tension principle

The central principle is:

> A good FQH classification is one that, for some admissible encoding `E` in `E_FQH` and finite refinement level `k`, can keep the classification tension `Tension_FQH(m; E, k)` low and stable across:
>
> * all known and realistically accessible FQH phases,
> * reasonable extensions of the library that respect the predetermined refinement rules,
> * changes of microscopic realization within the same topological phase.

Concretely, for an encoding `E` in `E_FQH` and its refinement ladder, Q037 asks whether there exist states `m_star` and some finite `k_star` such that

```txt
Tension_FQH(m_star; E, k_star) <= epsilon_FQH
```

with `epsilon_FQH` small, and such that modest increases of `k` and modest extensions of the world data do not force `Tension_FQH(m_star; E, k)` to grow beyond a controlled band.

### 4.2 World where classification succeeds

In a classification success world there exists:

* a finite level `k_star`, and
* a configuration `m_T` in `M_reg(E, k_star)` for some `E` in `E_FQH`,

such that

```txt
Tension_FQH(m_T; E, k_star) <= epsilon_FQH
Tension_FQH(m_T; E, k) remains within a narrow band for all k >= k_star
```

under the predetermined refinement rules. In this world:

* consistency violations are either absent or confined to controlled corner cases,
* equivalence mismatches are corrected by the invariant scheme,
* realization mismatches are small compared to known uncertainties in experiments and modeling.

### 4.3 World where classification fails

In a classification failure world, for every admissible encoding `E` in `E_FQH` and for every level `k` in its refinement ladder

```txt
inf over m in M_reg(E, k) of Tension_FQH(m; E, k) >= delta_FQH(k)
```

with `delta_FQH(k)` bounded below by a strictly positive constant or growing as `k` increases. This means that:

* either consistency constraints cannot be satisfied by any finite library constrained by the refinement rules,
* or equivalence and realization mismatches cannot be simultaneously minimized,
* or both.

Q037 then asks whether our universe behaves more like a success world or a failure world, under the constraints of admissible encodings.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer. Both are parameterized by admissible encodings `E` in `E_FQH`.

### 5.1 World T (classification succeeds with low tension)

In World T there exist an admissible encoding `E_T` and a finite level `k_star` such that:

1. Finite level sufficiency

   * There exists `m_T` in `M_reg(E_T, k_star)` with

     ```txt
     Tension_FQH(m_T; E_T, k_star) <= epsilon_FQH
     ```

     and refining to higher levels only produces small and controllable changes in tension.

2. Stable invariant mapping

   * For all known FQH phases and for typical future discoveries within the stated physical constraints, the invariant tuples derived from `L_inv(k_star)` under `E_T` map phases into equivalence classes that are stable under microscopically different realizations.

3. Realization coverage

   * The fraction of experimentally or numerically observed FQH phases that cannot be mapped into some descriptor in `L_topo(k_star)` under `E_T` is small and does not grow with further experimental exploration in the same physical regime.

4. Redundancy suppression

   * Distinct descriptors in `L_topo(k_star)` that describe the same physical phase are recognized and merged by the equivalence rules used to compute `DeltaS_equiv`, keeping redundancy penalties small.

### 5.2 World F (classification fails with persistent tension)

In World F, for every admissible encoding `E` in `E_FQH`:

1. No finite level suffices

   * For every level `k`, even the best states `m_F(k)` satisfy

     ```txt
     Tension_FQH(m_F(k); E, k) >= delta_FQH
     ```

     for some strictly positive `delta_FQH` independent of `k`.

2. Unstable invariant mapping

   * New FQH phases and improved numerical or experimental data repeatedly show that the existing invariant scheme misidentifies equivalence classes or fails to separate distinct phases.

3. Realization gaps

   * Many experimentally robust FQH phases cannot be matched by any descriptor in `L_topo(k)` for any reasonably bounded `k`, unless one violates the predetermined structural constraints on the library.

4. Endless proliferation

   * Each refinement step designed according to the predetermined rules introduces many new descriptors that have no clear relation to realizable phases, and tension from `DeltaS_real` and `DeltaS_equiv` does not converge toward a small band.

### 5.3 Interpretive note

These worlds do not specify how the microscopic Hamiltonians or wavefunctions are constructed. They only assert that, if there exist effective models that faithfully represent FQH phases, then the patterns of classification tension would behave in qualitatively different ways in World T and World F for admissible encodings in `E_FQH`.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can falsify specific Q037 encodings at the effective layer, without claiming to solve the underlying physical classification problem.

All experiments and protocols in this block operate entirely at the effective layer. They manipulate:

* admissible encodings `E` in `E_FQH`,
* descriptor libraries `L_topo(k)`, invariant libraries `L_inv(k)`,
* finite pools of FQH phases with assigned descriptors and invariants,
* tension scores derived from `DeltaS_axiom`, `DeltaS_equiv`, and `DeltaS_real`.

They do not construct or expose any TU core axiom system or generative field. All claims of falsification are about encodings and refinement ladders, not about the unique microscopic truth of nature.

### Experiment 1: Finite library consistency stress test

Goal.
Test whether a given finite library `L_topo(k)` and invariant set `L_inv(k)` under an encoding `E` can simultaneously keep consistency and equivalence mismatch small for a representative set of known FQH phases.

Setup.

* Choose a level `k` and construct `L_topo(k)` and `L_inv(k)` according to the predetermined refinement rules of some encoding `E` in `E_FQH`.
* Collect a dataset of representative FQH phases, including:

  * classic Laughlin type states,
  * Jain composite fermion sequences,
  * known non Abelian candidate states identified in theory and numerics.
* Construct states `m_data` in `M_reg(E, k)` that encode:

  * an assignment of each phase in the dataset to a descriptor in `L_topo(k)`,
  * invariant tuples computed via `L_inv(k)`.

Fairness constraints for the experiment.

* The encoding `E`, including the refinement rules and weights `w_axiom`, `w_equiv`, `w_real`, is fixed before looking at the dataset and is not tuned during the experiment.
* The library `L_topo(k)` and invariant scheme `L_inv(k)` are built only from structural rules in `E`, not from data driven backfitting.
* The only degrees of freedom during the experiment are:

  * assignments of phases to existing descriptors in `L_topo(k)`,
  * possible choices of representatives inside equivalence classes already defined by `E`.

Protocol.

1. For each `m_data`, evaluate `DeltaS_axiom(m_data; E, k)` and check that the encoded descriptors satisfy the declared topological and physical consistency constraints.
2. Compute `DeltaS_equiv(m_data; E, k)` by checking:

   * whether different physical phases are incorrectly merged into the same invariant tuple,
   * whether identical phases are split into distinct invariant tuples.
3. Compute `Tension_FQH(m_data; E, k)` using the fixed weights.
4. Aggregate the tension values over the dataset and compute summary statistics.

Metrics.

* Average and maximum values of `DeltaS_axiom` and `DeltaS_equiv` across the dataset.
* Distribution of `Tension_FQH(m_data; E, k)` values.
* Sensitivity of the results to modest, pre specified changes in `k`, for example going from `k` to `k+1` under the same refinement rules inside `E`.

Falsification conditions.

* If for the selected dataset and level `k` there is no assignment of descriptors and invariants that yields `Tension_FQH(m_data; E, k)` below a pre agreed threshold `tau_consistent` for most phases, the encoding at level `k` inside `E` is considered falsified as a candidate for a low tension classification.
* If small, pre specified changes to `k`, for example going from `k` to `k+1`, produce assignments that require large jumps in `DeltaS_axiom` or `DeltaS_equiv` that cannot be controlled by the invariant scheme, the encoding is considered unstable and rejected.

Semantics implementation note.
All observables and mismatch measures in this experiment are evaluated using continuous descriptions for field like quantities, such as gap estimates and filling fractions, and discrete indices for topological labels, consistent with the hybrid semantics in the metadata.

Boundary note.
Falsifying a TU encoding for Q037 does not solve the canonical classification problem. This experiment can reject specific libraries and invariant schemes at the effective layer, but it does not provide a full classification or prove that no satisfactory scheme exists.

---

### Experiment 2: Refinement ladder convergence test

Goal.
Determine whether the refinement ladder defined by `L_topo(k)` and `L_inv(k)` in an encoding `E` can converge toward a low tension regime as `k` increases, using a fixed pool of FQH phases.

Setup.

* Fix an admissible encoding `E` in `E_FQH`.
* Fix a pool of FQH phases that is large enough to be representative but finite.
* For several successive levels `k = k_0, k_0+1, ..., k_0+r`, construct the corresponding `L_topo(k)` and `L_inv(k)` according to the predetermined refinement rules of `E`.
* For each `k`, construct candidate states `m_best(k)` in `M_reg(E, k)` that attempt to minimize `Tension_FQH(m; E, k)` for the fixed pool of phases.

Fairness constraints for the experiment.

* The refinement rules that generate `L_topo(k)` and `L_inv(k)` from `k` are fixed as part of `E` and cannot be changed based on observed tensions.
* Weights `w_axiom`, `w_equiv`, `w_real` remain fixed across all levels.
* The phase pool is fixed in advance and is not pruned or reshaped based on tension outcomes.
* Search for `m_best(k)` may adjust only:

  * phase to descriptor assignments inside `L_topo(k)`,
  * choices of which descriptors are treated as representing the same physical phase under the existing invariants.

Protocol.

1. For each `k`, carry out a structured search over assignments of phases to descriptors in `L_topo(k)` and invariant tuples in `L_inv(k)` to find near optimal `m_best(k)` with low `Tension_FQH(m; E, k)`.

2. For each `m_best(k)`, compute

   ```txt
   Tension_FQH(m_best(k); E, k)
   ```

3. Record the sequence

   ```txt
   T_seq(k) = Tension_FQH(m_best(k); E, k)
   ```

4. Analyze whether `T_seq(k)` approaches a stable band or remains large and erratic as `k` increases.

Metrics.

* The sequence `T_seq(k)` over the tested range of `k`.
* Differences `T_seq(k+1) - T_seq(k)` to gauge whether refinement improves or destabilizes tension.
* Measures of redundancy and coverage derived from `DeltaS_equiv` and `DeltaS_real` at each level.

Falsification conditions.

* If `T_seq(k)` fails to enter a low and stable band across the tested range of `k` and instead oscillates or grows beyond controlled uncertainty estimates, then the combination of refinement rules and mismatch functionals in `E` is considered falsified as an encoding of Q037.
* If `T_seq(k)` appears low only because descriptors proliferate without clear relation to realizable phases, while realization mismatch remains large, then the encoding is considered invalid even if the scalar tension value is small.

Semantics implementation note.
The refinement ladder treats discrete and continuous parts of the descriptors in a consistent hybrid fashion. The rules for adding new descriptors or invariants are fixed structurally and are not tuned in response to the observed FQH pool.

Boundary note.
Falsifying a particular refinement ladder does not prove that no successful ladder exists. It only rejects that specific design inside `E_FQH`.

---

## 7. AI and WFGY engineering spec

This block describes how Q037 can be used to design AI modules and evaluation schemes within the WFGY framework at the effective layer.

All training signals, architectural patterns, and evaluation procedures in this block are defined in terms of effective layer quantities:

* descriptor indices, invariant tuples, phase pools,
* mismatch observables `DeltaS_axiom`, `DeltaS_equiv`, `DeltaS_real`,
* scalar tensions `Tension_FQH(m; E, k)` and derived statistics.

They do not assume access to TU core fields or axiom states.

### 7.1 Training signals

1. `signal_topo_consistency_FQH`

   * Definition. Penalty proportional to `DeltaS_axiom(m; E, k)` for states representing proposed FQH classifications.
   * Purpose. Encourage the AI to favor descriptors and invariants that satisfy known consistency constraints of topological order and effective field theory.

2. `signal_equiv_minimality_FQH`

   * Definition. Penalty proportional to `DeltaS_equiv(m; E, k)` when the model proposes classification schemes that over merge or over split FQH phases.
   * Purpose. Drive the AI toward invariant choices that give a near one to one match between classes and physical phases.

3. `signal_realization_coverage_FQH`

   * Definition. Penalty proportional to `DeltaS_real(m; E, k)` when model generated classifications fail to cover known FQH phases or contain descriptors without plausible realizations.
   * Purpose. Keep the model aligned with both theoretical constructions and experimental evidence.

4. `signal_refinement_stability_FQH`

   * Definition. Secondary penalty when `Tension_FQH(m; E, k+1)` is significantly larger than `Tension_FQH(m; E, k)` for nearby states under the same refinement rules.
   * Purpose. Encourage proposals whose tension behaves stably under refinement.

### 7.2 Architectural patterns

1. `TopologicalOrderClassifier_FQH`

   * Role. A head that, given an internal representation of a physical or theoretical FQH context, outputs a candidate descriptor index in `L_topo(k)` and an invariant tuple in `L_inv(k)` for some level `k`.
   * Interface.

     * Input. Internal embeddings representing the problem context, for example text about a particular filling fraction and experimental signatures.
     * Output. Indices into descriptor and invariant libraries, together with confidence scores and local tension estimates derived from `DeltaS_axiom`, `DeltaS_equiv`, and `DeltaS_real`.

2. `ClassificationTensionEvaluator_FQH`

   * Role. A module that computes approximate `DeltaS_axiom`, `DeltaS_equiv`, `DeltaS_real`, and `Tension_FQH` from the outputs of `TopologicalOrderClassifier_FQH` and a reference phase pool.
   * Interface.

     * Input. Descriptor indices, invariant tuples, references to known FQH phases.
     * Output. Scalar tension value and component wise mismatch indicators.

3. `RefinementNavigator_FQH`

   * Role. A control module that proposes moves in `k` and suggests how to allocate attention across descriptors when exploring the refinement ladder.
   * Interface.

     * Input. A history of tensions and assignments over several levels for a fixed encoding `E`.
     * Output. Suggested next level and guidance on which parts of `L_topo(k)` and `L_inv(k)` to focus on.

All three patterns operate only on effective layer objects and do not inspect or require any deeper TU core state.

### 7.3 Evaluation harness

1. Task selection

   * Prepare a benchmark of questions and tasks about FQH phases, including:

     * matching filling fractions to candidate topological orders,
     * reasoning about whether two descriptions represent the same phase,
     * extrapolating possible new FQH phases under physical constraints.

2. Conditions

   * Baseline condition.

     * Use an AI model without explicit Q037 modules, only its general knowledge of FQH physics.
   * TU augmented condition.

     * Use the same model with `TopologicalOrderClassifier_FQH`, `ClassificationTensionEvaluator_FQH`, and possibly `RefinementNavigator_FQH` providing auxiliary signals or intermediate structure.

3. Metrics

   * Accuracy on classification style questions.
   * Internal consistency. Degree to which the model gives compatible answers across related prompts, for example comparing equivalence class judgments across rephrasings.
   * Stability under refinement. Sensitivity of answers when prompts simulate moving up or down the refinement ladder, for example by requesting more or less detailed invariants.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to observe the impact of Q037 style encoding on model explanations.

Baseline setup.

* Prompt.
  Ask the model:
  `Explain how physicists currently classify fractional quantum Hall states, and what is still unknown about this classification.`
* Observation.
  Note whether the answer mixes Abelian and non Abelian cases without clear structure and whether it acknowledges incompleteness in a precise way.

TU encoded setup.

* Prompt.
  Ask the model the same question, with an additional instruction:
  `Organize your explanation around a finite library of effective theories, invariants that label phases, and the tension between consistency, non redundancy, and realizability.`
* Observation.
  Check if the model now introduces a clearer separation between descriptors, invariants, and realized phases, and whether it talks explicitly about holes and redundancies in the classification.

Comparison metric.

* Use a rubric for:

  * structure and clarity of the library plus invariant picture,
  * explicit mention of consistency, non redundancy, and coverage constraints,
  * how clearly the answer separates what is encoded in the classification from what is still unknown.

Logging constraints.

* For both setups, log prompts, responses, and any effective layer tension estimates from `ClassificationTensionEvaluator_FQH`.
* Logs should not record any internal TU core fields or axiom states. They are limited to visible text and effective layer tension objects.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: `FQH_Classification_Tension_Functional`

   * Type. functional.
   * Minimal interface.

     * Inputs. `descriptor_set`, `invariant_scheme`, `realization_pool`, refinement level `k`.
     * Output. `tension_value` and `component_mismatches`, for example `DeltaS_axiom`, `DeltaS_equiv`, `DeltaS_real`.
   * Preconditions.

     * `descriptor_set` is a finite library defined structurally at level `k`.
     * `invariant_scheme` maps each descriptor to a finite tuple.
     * `realization_pool` is a finite set of phases with assigned descriptors and invariants.

2. ComponentName: `Finite_Topological_Library_Schema`

   * Type. field.
   * Minimal interface.

     * Inputs. `k`, plus structural parameters such as maximum matrix size and allowed symmetry classes.
     * Output. `L_topo(k)` and `L_inv(k)` consistent with the refinement rules in an encoding `E`.
   * Preconditions.

     * Structural parameters and refinement rules are fixed before any evaluation against world data.

3. ComponentName: `Refinement_Ladder_Protocol`

   * Type. experiment_pattern.
   * Minimal interface.

     * Inputs. `initial_level k_0`, `max_level k_max`, `phase_pool`.
     * Output. A sequence of recommended evaluations of `Tension_FQH` and associated summary statistics as `k` increases.
   * Preconditions.

     * `phase_pool` is fixed across all levels and contains enough variety to stress test the encoding.

### 8.2 Direct reuse targets

1. Q030 (Classification of quantum phases of matter)

   * Reused component. `FQH_Classification_Tension_Functional` and `Finite_Topological_Library_Schema`.
   * Why it transfers. Q030 generalizes the classification problem beyond FQH. The same notion of finite libraries, invariants, and realization mismatch applies.
   * What changes. Descriptors now include more general topological and symmetry protected phases. Invariants and constraints are broadened accordingly.

2. Q038 (Strongly correlated cold atom phases)

   * Reused component. `Refinement_Ladder_Protocol`.
   * Why it transfers. Cold atom systems can simulate FQH like phases and other topological orders, so the same refinement ladder idea can be used to test classification schemes.
   * What changes. Descriptors are adapted to lattice or continuum cold atom models, and realization pools come from cold atom experiments and numerics.

3. Q059 (Information and thermodynamic resource classification)

   * Reused component. `Finite_Topological_Library_Schema`.
   * Why it transfers. Classification of resource states in quantum information can be organized via discrete invariants and finite libraries that resemble FQH topological orders.
   * What changes. Descriptors represent resource states or channels, and invariants capture relevant monotones and conversion rules instead of Hall conductance and anyon content.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * A coherent effective layer encoding of FQH classification tension has been specified through `E_FQH`.
  * Finite libraries, refinement ladders, and mismatch functionals are defined with fairness constraints and domain restrictions.

* N_level: N1

  * The narrative linking descriptors, invariants, and realizations is explicit.
  * Counterfactual worlds and discriminating experiments are outlined, but not yet implemented or quantified in detail.

### 9.2 Next measurable step toward E2

To reach E2, at least one of the following should be carried out.

1. Implement a prototype of `FQH_Classification_Tension_Functional` acting on a curated collection of FQH phases and a concrete `L_topo(k)` in some encoding `E`, producing public tension profiles and mismatch statistics.
2. Run the refinement ladder experiment for a small but nontrivial pool of phases, documenting how `Tension_FQH(m_best(k); E, k)` behaves across `k` and publishing the results.

Both actions remain at the effective layer and do not require exposing any deep TU generative rules.

### 9.3 Long term role in the TU program

Longer term, Q037 is expected to:

* provide a reference pattern for classification problems where discrete invariants and continuous effective fields must align,
* support cross links between condensed matter, quantum information, and AI representation spaces by exporting its finite library and refinement ladder structures,
* serve as a test bed for evaluating how well TU style encodings can organize extremely complex many body phenomena without over claiming physical results.

---

## 10. Elementary but precise explanation

Fractional quantum Hall states are very special phases of matter. They appear when electrons move in two dimensions in a strong magnetic field. Instead of behaving like an ordinary conductor or insulator, the system develops:

* precisely quantized Hall conductance at rational fractions,
* edge currents that are very hard to disturb,
* quasiparticles that behave like anyons with exotic statistics.

Physicists have many tools to describe these phases, such as effective field theories and topological invariants. But there is still no single, agreed upon list of all possible FQH phases that could exist under realistic conditions. That is the classification problem.

In the Tension Universe view we do not try to solve the physics directly. Instead, we ask:

* what does a good classification look like at a high level,
* how can we tell when a classification scheme is incomplete, redundant, or inconsistent.

We imagine:

* a finite library of candidate effective theories,
* a set of labels that are supposed to distinguish phases,
* a set of known or strongly supported FQH phases from experiments and models.

For each proposed classification we measure three kinds of mismatch.

1. Does each candidate theory satisfy basic consistency rules.
2. Do the labels separate distinct phases and merge identical ones.
3. Do the theories cover the phases we actually see, without inventing many phases that never appear.

We combine these into a single number called the classification tension. If this number can be made small and stable using a finite library and fixed rules, we say the classification is working well. If the number stubbornly stays large, or jumps around every time we refine our rules, the classification is under tension.

This approach does not tell us which classification is ultimately correct. It does not replace detailed calculations or experiments. Instead, it provides:

* a clear way to express what we want from a classification,
* concrete tests that can falsify particular schemes at the effective layer,
* reusable tools for other problems where discrete labels and continuous fields must be woven into a consistent picture.

Q037 is the flagship example of how Tension Universe treats such classification problems, using the rich and still mysterious world of fractional quantum Hall states as its test case.

---

## Tension Universe effective layer footer

This page is part of the WFGY / Tension Universe S problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the fractional quantum Hall classification problem and its associated `topological_tension` structures.
* It does not claim to provide a complete or final classification of all fractional quantum Hall phases.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the fractional quantum Hall classification problem has been solved.

### Effective layer boundary

* All objects used here, including state spaces `M`, descriptor libraries, invariant schemes, tension scores, and counterfactual worlds, live at the effective layer.
* No TU core axiom system, generative rule, or deep field is exposed or constructed in this page.
* All falsifiability statements concern encodings and finite libraries inside the admissible classes `E_FQH`, not the underlying microscopic quantum many body theory itself.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

---

**Index:**  
[`← Back to Event Horizon`](../EventHorizon/README.md)  
[`← Back to WFGY Home`](https://github.com/onestardao/WFGY)

**Consistency note:**  
This entry has passed the internal formal-consistency and symbol-audit checks under the current WFGY 3.0 specification.  
The structural layer is already self-consistent; any remaining issues are limited to notation or presentation refinement.  
If you find a place where clarity can improve, feel free to open a PR or ping the community.  
WFGY evolves through disciplined iteration, not ad-hoc patching.
