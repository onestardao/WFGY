<!-- QUESTION_ID: TU-Q030 -->
# Q030 · Classification of quantum phases of matter

## 0. Header metadata

```txt
ID: Q030
Code: BH_PHYS_QPHASE_MATTER_L3_030
Domain: Physics
Family: Condensed matter and quantum many body
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Open
Semantics: hybrid
Encoding_class: TU_effective_QPhase_classification
EncodingKey_Q030: E_PHASE_Q030_V1
LibraryKey_ref_Q030: Lref_PHASE_Q030_V1
WeightKey_Q030: W_PHASE_Q030_V1
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All content in this entry is restricted to the **effective layer** of the Tension Universe (TU) framework.

More precisely:

* This page only specifies:

  * effective state spaces and phase summaries,
  * observables and effective fields,
  * finite invariant libraries and tension functionals,
  * singular sets and domain restrictions,
  * experiments and AI engineering patterns that use these objects.
* It **does not** introduce or modify any TU core axioms, any deep layer generative rules, or any global TU field equations.
* It **does not** specify any explicit mapping from:

  * microscopic Hamiltonians or wavefunctions, or
  * raw experimental data,
    into internal TU fields. It only assumes that some such mappings exist in principle and can produce the effective summaries mentioned here.
* All references to existence of phases, libraries or encodings are statements about **effective encodings** that can be audited at this layer. They are not claims that the canonical open problem Q030 has been mathematically solved.
* Parameters such as:

  * the convergence factor `lambda(m_r)`, and
  * the coupling constant `kappa_phase`,
    are treated here as opaque effective parameters imported from the TU core. This document does not define them, derive them, or allow them to be tuned in response to particular models or data.

Throughout this entry, any experiment or AI module is understood to operate **only** on the effective objects defined here. No argument in this page should be interpreted as evidence that the classification of quantum phases of matter is complete, decidable, or settled at the level of fundamental physics.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The classical problem of classifying quantum phases of matter can be summarised as follows.

Consider quantum many body systems at or near zero temperature, in various spatial dimensions, with specified symmetries and interaction structures. A **quantum phase of matter** is informally an equivalence class of microscopic Hamiltonians such that:

* there is a well defined thermodynamic limit,
* systems in the same class can be connected by a continuous path of Hamiltonians without closing the relevant energy gap or changing long range order in a way that counts as a phase transition,
* and systems in different classes cannot be connected by such a path without encountering a phase transition.

The **classification problem** asks whether there exists, for a given dimension, symmetry class and interaction regime, a family of invariants that:

1. assigns the same invariants to all systems in the same phase, and
2. assigns different invariants to systems in distinct phases.

Modern work has widened the range of recognised phases. Quantum phases now include not only classical symmetry breaking phases but also:

* topological orders,
* symmetry protected topological (SPT) phases,
* long range entangled phases that are not captured by Landau symmetry breaking alone.

The canonical question can be phrased in a compact way.

> Does there exist, in realistic settings, a finite, computable and reasonably complete classification scheme for quantum phases of matter, and if so what is its structure and domain of validity?

### 1.2 Status and difficulty

Partial classification results are known in several restricted regimes.

* In free or non interacting fermion systems, many SPT phases can be classified by K theory like schemes in various dimensions.
* In certain interacting settings, group cohomology and related constructions classify SPT phases with given symmetry groups.
* Tensor network and exactly solvable model constructions provide explicit examples of topological orders in two spatial dimensions and in some higher dimensional cases.

However, in general:

* Classification in higher dimensions with strong interactions is incomplete.
* The distinction between intrinsic topological order and SPT phases is well understood only in restricted frameworks.
* There is no universally agreed finite invariant library that is known to classify all realistic quantum phases across dimensions and symmetries.
* There is ongoing debate about how wild the space of phases can be and whether any complete classification is possible in practice, even at zero temperature.

From the BlackHole viewpoint, Q030 is therefore treated as an open and possibly unbounded classification problem in condensed matter physics and quantum many body theory.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q030 plays the following roles.

1. It is the primary **thermodynamic_tension** node for quantum many body systems. It provides the reference pattern for how microscopic Hamiltonians and macroscopic phase structure pull against each other in the TU encoding.
2. It anchors a cluster of problems about non perturbative phases, including high temperature superconductivity, exotic orders, and quantum turbulence.
3. It serves as the main test case for the idea that a finite library of effective invariants can control extremely complex state spaces without crossing into hidden deep layer rules of Tension Universe.

### References

1. X. G. Wen, “Quantum Field Theory of Many Body Systems: From the Origin of Sound to an Origin of Light and Electrons”, Oxford University Press, 2004.
2. X. G. Wen, “Topological orders in rigid states”, International Journal of Modern Physics B, 4 (1990), and related review articles on quantum phases and topological order.
3. A. P. Schnyder, S. Ryu, A. Furusaki, A. W. W. Ludwig, “Classification of topological insulators and superconductors”, Physical Review B 78 (2008).
4. Review style entry on “phases of matter and quantum phases” in a standard condensed matter physics encyclopedia or survey volume, with explicit discussion of the incompleteness of current classification schemes.

---

## 2. Position in the BlackHole graph

This block describes how Q030 connects to other S problems via explicit graph edges.

### 2.1 Upstream problems

Upstream nodes supply foundations and tools that Q030 relies on at the effective layer.

* Q026 (BH_PHYS_QMEAS_MACRO_L3_026)
  Reason: provides an effective description of how microscopic quantum states yield macroscopic measurement records and stability. Phase distinctions rely on which macroscopic observables can be stably distinguished.

* Q027 (BH_PHYS_QDECOH_SCALE_L3_027)
  Reason: encodes decoherence scales and mechanisms that protect or destroy quantum phase structure, including robustness of order parameters and entanglement patterns.

* Q032 (BH_PHYS_QTHERMO_NONEQ_L3_032)
  Reason: supplies the quantum thermodynamics framework needed to talk about zero temperature limits, thermodynamic limits and non equilibrium steady states that underlie phase definitions.

### 2.2 Downstream problems

Downstream nodes reuse Q030 components or depend on its tension structure.

* Q031 (BH_PHYS_HOLOGRAPHIC_PHASES_L3_031)
  Reason: reuses phase invariant libraries and phase tension functionals as input to the classification of holographic and gravitational phases in emergent geometry.

* Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)
  Reason: needs Q030 phase descriptors to distinguish competing mechanisms and phase diagrams in high temperature superconductivity.

* Q039 (BH_PHYS_QTURBULENCE_L3_039)
  Reason: uses Q030 notions of phases and phase boundaries to define what counts as quantum turbulence inside phases versus across phase transitions.

### 2.3 Parallel problems

Parallel nodes share similar tension patterns but have no direct component reuse.

* Q028 (BH_PHYS_COLOR_CONFINEMENT_L3_028)
  Reason: both Q028 and Q030 involve non perturbative phases where local gauge fields produce emergent global structure that is hard to classify.

* Q029 (BH_PHYS_SUPERSYM_L3_029)
  Reason: both Q029 and Q030 study how microscopic theories with rich internal structure project into low energy spectra and phase patterns, and both use tension functionals to compare finite invariant libraries with increasingly strong experimental or numerical constraints.

* Q040 (BH_PHYS_QBLACKHOLE_INFO_L3_040)
  Reason: quantum black hole microstates can be viewed as exotic phases of quantum gravity, with classification problems closely analogous to condensed matter phases.

### 2.4 Cross domain edges

Cross domain edges show reuse of Q030 components outside condensed matter.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: reuses phase diagrams and thermodynamic_tension ideas for information theoretic and computational phases, for example phases of learning or phases of computation.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: reuses the concept of “phases of representation” where internal states of AI models cluster into qualitatively distinct regimes that behave like phases.

* Q001 (BH_MATH_NUM_L3_001)
  Reason: shares formal patterns where complex spectra and global structure are summarised by finite libraries of invariants, and where tension arises between finite summaries and infinite systems.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is strictly at the effective layer.

We only define:

* state spaces of phase summaries,
* observables and effective fields,
* invariants and tension functionals,
* singular sets and domain restrictions.

We do not describe any deep layer generative rules, any explicit construction of internal TU fields from microscopic Hamiltonians, or any mapping from raw experimental data into TU fields.

**Hybrid semantics note.** In this encoding:

* observables like `OP`, `ES` and `RC` are treated as continuous or field valued effective quantities,
* objects like `TI`, phase labels, and library indices are treated as discrete index valued quantities.

The header field `Semantics: hybrid` records that both types coexist at the effective layer in a single encoding class. No additional hidden semantics is implied.

### 3.1 State space

We introduce a state space

```txt
M_phase
```

with the following interpretation.

* Each state `m` in `M_phase` is a coarse summary of a quantum phase configuration for a specific physical setting.
* A state `m` aggregates, at a chosen resolution:

  * information about an equivalence class of microscopic Hamiltonians believed to realise one quantum phase,
  * symmetry data such as global symmetries and higher form symmetries that are relevant to phase structure,
  * thermodynamic limit information when defined,
  * coarse descriptors of ground state entanglement patterns,
  * selected response coefficients to standard probes.

We do not specify how these summaries are constructed from wavefunctions or Hamiltonians. We only assume:

* for any physically relevant phase and a chosen resolution scale `r`, there exist one or more states in `M_phase` that encode an effective summary of that phase at resolution `r`.

For refinements we assume a resolution parameter

```txt
r in R_plus
```

that indexes how detailed the phase summary is. Larger `r` corresponds to higher resolution summaries. We write `m_r` when we want to emphasise the resolution of a state.

### 3.2 Effective fields and observables

We define several families of effective observables on `M_phase`.

1. Order parameter profile

   ```txt
   OP(m_r; region)
   ```

   * Input: `m_r` in `M_phase`, and a coarse spatial region description.
   * Output: a finite vector summarising symmetry breaking order parameters in that region when applicable.
   * Interpretation: in symmetry broken phases, `OP` reveals which symmetries are broken and the approximate values of order parameters.

2. Entanglement signature

   ```txt
   ES(m_r; region)
   ```

   * Input: `m_r` and a region.
   * Output: a finite descriptor summarising entanglement structure in that region, for example scaling laws of entanglement entropy and presence or absence of topological contributions.
   * Interpretation: distinguishes short range entangled phases, long range entangled phases, and topologically ordered phases at the effective layer.

3. Topological and SPT index tuple

   ```txt
   TI(m_r)
   ```

   * Input: `m_r`.
   * Output: a finite tuple in a discrete index space, for example group cohomology labels, topological field theory data, or other quantised invariants.
   * Interpretation: classifies phases up to the reach of known topological and SPT classification schemes.

4. Response coefficient map

   ```txt
   RC(m_r; probe)
   ```

   * Input: `m_r` and a standard probe description, for example a gauge field, boundary condition or defect.
   * Output: a finite tuple summarising quantised or characteristic responses such as Hall conductance, protected edge modes or anomaly inflow signatures.

We require that for all states considered in the regular analysis domain, these observables are well defined and finite at the chosen resolution.

### 3.3 Invariants, finite libraries and admissible classes

We now define the idea of a finite invariant library and the admissible class for these libraries.

1. Finite invariant library

   A finite invariant library is a tuple

   ```txt
   L_phase = (L_OP, L_ES, L_TI, L_RC)
   ```

   where:

   * `L_OP` is a finite selection rule for extracting or aggregating pieces of `OP`,
   * `L_ES` is a finite selection rule for extracting or aggregating entanglement signatures from `ES`,
   * `L_TI` is a finite projection rule on `TI`, possibly with coarsening,
   * `L_RC` is a finite selection of probes and response components from `RC`.

   Given a state `m_r`, the library `L_phase` produces a finite descriptor

   ```txt
   Inv_L(m_r)
   ```

   in some finite dimensional space.

2. Admissible library class

   We restrict to an admissible class of libraries `A_phase` with the following properties.

   * Each `L` in `A_phase` is specified without reference to any particular phase data beyond general physical settings such as dimension and symmetry class.
   * Once chosen for a given analysis, `L` is fixed and cannot be tuned after observing how specific phases map into `Inv_L`.
   * `L` only depends on known families of invariants in the literature and simple combinations of them, not on hidden TU specific structures.

3. Fairness and non cheating constraint

   For each analysis we must fix `L` in `A_phase` before evaluating phases. We are not allowed to choose `L` separately for each phase in a way that uses the target mapping as input. This forbids cheating configurations where the library is effectively redefined per phase.

### 3.4 Tension primitives

We define two basic tension primitives.

1. Intra phase consistency tension

   ```txt
   DeltaS_intra(m_r; L_phase) >= 0
   ```

   * Measures how consistent the different components of `Inv_L(m_r)` are with the assumption that `m_r` encodes a single well defined phase.
   * Large values indicate that order parameter data, entanglement signatures, topological indices and responses send conflicting messages about phase identity.

2. Inter phase indistinguishability tension

   ```txt
   DeltaS_inter(m_r, n_r; L_phase) >= 0
   ```

   * Measures how well the library `L_phase` distinguishes two states `m_r` and `n_r`.
   * If physical reasoning or external arguments say that `m_r` and `n_r` are different phases, but `Inv_L(m_r)` and `Inv_L(n_r)` coincide or are very close, then `DeltaS_inter` is large.

We do not supply formulas that depend on hidden deep layer objects. We only require that these tensions are computed from the finite descriptors `Inv_L` and external phase relation information that is accessible at the effective layer.

### 3.5 Phase classification tension functional

We define a phase classification tension functional

```txt
Tension_phase(m_r; L_phase) =
    w_intra * DeltaS_intra(m_r; L_phase)
  + w_cover * CoverPenalty(m_r; L_phase)
```

with the following components.

* `w_intra` and `w_cover` are non negative weights with

  ```txt
  w_intra + w_cover = 1
  ```

  fixed before analysis for a given study. They cannot be tuned after looking at data.

* `DeltaS_intra` is as defined above.

* `CoverPenalty(m_r; L_phase)` is a non negative quantity that reflects how many distinct physical phases appear to be mapped into the same `Inv_L` region as `m_r` in the model class under consideration. If the library `L_phase` clusters many distinct phases together, `CoverPenalty` becomes large.

The detailed formulas may vary between studies. Admissible choices must be documented and fixed ahead of data analysis. This functional is meant to capture how well a finite invariant library `L_phase` supports a low tension classification over the phases that appear in practice.

### 3.6 Effective tension tensor and coupling

At the effective layer we introduce a semantic tension tensor component associated with Q030.

```txt
T_ij(m_r) = S_i(m_r) * C_j(m_r) * Tension_phase(m_r; L_phase) * lambda(m_r) * kappa_phase
```

where:

* `S_i(m_r)` are source like factors that encode how strongly different theoretical or experimental contexts rely on correct phase identification.
* `C_j(m_r)` are receptivity like factors that encode how sensitive downstream tasks are to phase misclassification.
* `lambda(m_r)` is the convergence state factor from the TU core that describes whether local reasoning near `m_r` is convergent, recursive, divergent or chaotic.
* `kappa_phase` is a coupling constant for Q030 that sets the overall scale of phase classification tension.

The index sets for `i` and `j` are not needed at this level. It is enough that for each `m_r` in the regular domain, `T_ij(m_r)` is finite.

### 3.7 Singular set and domain restriction

We collect all problematic states into a singular set

```txt
S_sing_phase =
  { m_r in M_phase :
    OP, ES, TI or RC is undefined or divergent at resolution r
    or Inv_L(m_r) cannot be formed
    or Tension_phase(m_r; L_phase) is undefined or not finite }
```

We define the regular domain

```txt
M_phase_reg = M_phase \ S_sing_phase
```

All Q030 analysis in this document is restricted to `M_phase_reg`. When an experiment encounters states in `S_sing_phase`, the output is marked as out of domain rather than as meaningful evidence about phase classification itself.

### 3.8 Edge bulk tension functional

For model families where a bulk edge correspondence is theoretically expected, we define an auxiliary edge bulk tension functional

```txt
Tension_edge_bulk(m_r; L_phase) >= 0
```

with the following interpretation.

* `Tension_edge_bulk(m_r; L_phase)` measures how well bulk invariants and edge responses encoded in `Inv_L(m_r)` and `RC(m_r; probe_edge)` align with known bulk edge correspondence patterns for the model class under study.
* Large values indicate systematic mismatches, for example:

  * bulk topological indices predicting protected edge modes while `RC` shows no such signature, or
  * edge responses signalling protected modes while bulk invariants encode a trivial phase.
* Small values indicate that bulk and edge descriptors are consistent with each other, within declared uncertainties.

The exact formula used to build `Tension_edge_bulk` from `TI`, `ES` and `RC` is considered part of the encoding element and must be documented once for each encoding. It must not depend on particular models in a way that violates the admissible library constraints.

### 3.9 Encoding element for Q030

We package the Q030 encoding into a single encoding element

```txt
E_PHASE_Q030_V1 =
  (Encoding_class,
   EncodingKey_Q030,
   LibraryKey_ref_Q030,
   WeightKey_Q030,
   M_phase_reg,
   A_phase,
   Tension_phase,
   Tension_edge_bulk,
   kappa_phase)
```

with the following commitments.

* `Encoding_class` is fixed as `TU_effective_QPhase_classification` as declared in the header.
* `EncodingKey_Q030`, `LibraryKey_ref_Q030` and `WeightKey_Q030` are the identifiers listed in the header metadata. They must be used consistently in logs and tooling.
* `M_phase_reg` and `A_phase` are the regular domain and admissible library class defined above.
* `Tension_phase` and `Tension_edge_bulk` are the tension functionals defined in Sections 3.5 and 3.8.
* `kappa_phase` is a fixed coupling constant for this encoding element and cannot be tuned per model.

All experiments, AI modules and cross problem transfers in this entry are understood to use `E_PHASE_Q030_V1` by default. Any future change to the invariant library, weight scheme or tension functionals that materially affects results must be registered as a new encoding element with a new `EncodingKey_Q030` and a corresponding update in the header metadata.

---

## 4. Tension principle for this problem

This block states the effective layer tension principle that defines Q030.

### 4.1 Core tension statement

At the effective layer Q030 is about the tension between two tendencies.

1. The desire for a finite, stable and computable library of invariants `L_phase` in `A_phase` that can classify quantum phases of matter in realistic settings.
2. The apparent richness of interacting quantum many body systems that may require arbitrarily complex or infinite information to distinguish all phases.

The phase classification problem is rephrased as follows.

* Low tension principle: there exist admissible libraries `L_phase` and resolution schemes `r` such that for all physically relevant phases represented in `M_phase_reg`, the phase classification tension `Tension_phase(m_r; L_phase)` stays within a controlled low band that does not blow up as `r` increases.

* High tension principle: for every admissible library `L_phase`, there exist physically realizable phases for which `Tension_phase(m_r; L_phase)` stays large or grows as the resolution increases.

Q030 asks which of these patterns better describes our universe for realistic condensed matter and quantum many body systems.

### 4.2 Low tension regime (good classification)

In a low tension regime there exists at least one `L_phase` in `A_phase` such that:

* For states `m_r` that represent a single phase, `DeltaS_intra(m_r; L_phase)` is small and remains small as `r` grows.
* For states `m_r` and `n_r` that correspond to distinct phases, `DeltaS_inter(m_r, n_r; L_phase)` becomes large at some finite resolution, so `L_phase` does not merge them.
* `CoverPenalty(m_r; L_phase)` is small for all `m_r` in the explored model class, which means the library does not accidentally collapse many phases into one cell of `Inv_L`.

In this regime finite invariant libraries are sufficient to organise phase diagrams and predict phase boundaries in a stable way.

### 4.3 High tension regime (classification failure)

In a high tension regime the following patterns appear.

* For any admissible `L_phase` there exist models where:

  * known distinct phases map to nearly identical `Inv_L` values, so `DeltaS_inter` remains small even though phases are different, or
  * systems believed to be in the same phase are mapped to noticeably different invariant values, so `DeltaS_intra` is large.
* The number or complexity of invariants needed to distinguish phases appears to grow without practical bound as one enlarges the space of models, dimensions or symmetry classes.
* `CoverPenalty(m_r; L_phase)` remains large for whole families of models, indicating that finite invariant libraries are intrinsically too coarse.

In this regime attempts to classify phases with finite libraries stay in a high tension band. The effective layer description is that classification is intrinsically wild.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds that differ only in their effective tension patterns. We do not commit to which world we live in.

### 5.1 World T: classification tame enough

In World T the following patterns hold.

1. Existence of effective libraries

   * For each relevant dimension and symmetry class there exists an admissible `L_phase` in `A_phase` and a refinement scheme for `r` such that:

     ```txt
     sup over m_r in explored_phase_family
     Tension_phase(m_r; L_phase) <= epsilon_phase
     ```

     for some small `epsilon_phase` that does not increase without bound as `r` grows.

2. Stability under refinement

   * As `r` increases and phase summaries become more detailed, the invariant values `Inv_L(m_r)` converge or stabilise for each phase. Intra phase tension does not explode with resolution.

3. Predictive coherence

   * The library `L_phase` correctly predicts when parameter changes cross or do not cross phase transitions for large classes of models. Misclassifications are rare and admit clear explanations as limitations of the model class rather than of the library structure.

World T is the low tension scenario where classification is tractable enough to serve as a stable foundation for condensed matter theory.

### 5.2 World F: classification intrinsically wild

In World F we see the opposite pattern.

1. Persistent counterexamples

   * For every `L_phase` in `A_phase` there exist model families where:

     * known distinct phases map to essentially the same `Inv_L` region, or
     * systems believed to share the same phase map to widely separated `Inv_L` values that cannot be reconciled by refinement.

2. Resolution induced instability

   * As `r` grows, new features appear in `OP`, `ES`, `TI` or `RC` that repeatedly invalidate previous invariant libraries. `Tension_phase(m_r; L_phase)` cannot be kept uniformly small.

3. Growing complexity

   * The number of invariants required to separate phases in the explored model class grows with the size or complexity of the systems. Any fixed finite library either merges many phases or splits phases in misleading ways.

World F is a high tension scenario where classification by finite invariant libraries is intrinsically unstable, at least for broad families of models.

### 5.3 Interpretive note

These worlds are described purely in terms of effective observables and tension patterns. They do not assume or describe any deep layer TU rules. They only encode how well finite invariant libraries seem to behave as we expand model classes and refine data.

---

## 6. Falsifiability and discriminating experiments

In this section we **fix once and for all** the encoding element

```txt
E_PHASE_Q030_V1
```

as defined in Section 3.9. All references to `L_phase`, weights, `Tension_phase` and `Tension_edge_bulk` are understood to refer to the choices bundled into `E_PHASE_Q030_V1`.

Experiments in this block cannot prove or disprove that classification is ultimately tame or wild. They can falsify specific choices of invariant libraries and tension functionals for Q030 at the effective layer, that is, they can falsify `E_PHASE_Q030_V1` as a suitable encoding element.

### Experiment 1: Finite invariant stress test on model families

**Goal**

Test whether the fixed finite invariant library and weight scheme inside `E_PHASE_Q030_V1` can maintain low phase classification tension across a broad family of lattice models in a fixed dimension and symmetry class.

**Setup**

* Choose a concrete class of models, for example spin systems on two dimensional lattices with specified on site symmetries and interaction range.
* Use the candidate invariant library `L_phase` that is part of `E_PHASE_Q030_V1`, including its rules for `OP`, `ES`, `TI` and `RC`.
* Select a diverse set of Hamiltonians in this class, including models believed to realise distinct phases and models believed to sit within the same phase.

**Protocol**

1. For each Hamiltonian and a chosen set of parameter values, construct an effective state `m_r` in `M_phase_reg` by summarising ground state and low energy properties at resolution `r`.
2. Compute `Inv_L(m_r)`, `DeltaS_intra(m_r; L_phase)`, and for selected pairs `(m_r, n_r)` compute `DeltaS_inter(m_r, n_r; L_phase)`.
3. Use independent physical reasoning or numerical diagnostics to label which pairs are believed to be in the same phase and which are believed to be in different phases.
4. Record cases where:

   * same phase pairs have large `DeltaS_intra` or large `DeltaS_inter`, or
   * different phase pairs have small `DeltaS_inter`.
5. Aggregate these results into a distribution of `Tension_phase(m_r; L_phase)` across the model family.

**Metrics**

* Maximum and typical values of `Tension_phase(m_r; L_phase)` across all models.
* Number of phase relation contradictions, where invariant comparisons disagree with independent phase identifications.
* Sensitivity of results to moderate changes in resolution `r`, for example from `r` to `r` plus one refinement step.

**Falsification conditions**

* Before running the experiment, fix:

  * a threshold band for acceptable `Tension_phase` values, and
  * a maximum tolerated contradiction rate for phase relations.
* If, for a reasonably large and diverse model family:

  * the number of contradictions remains above the tolerated rate, and
  * `Tension_phase(m_r; L_phase)` stays above the acceptable band for many states,
    then the encoding element `E_PHASE_Q030_V1` is rejected at the effective layer for this domain.
* If small admissible modifications of `L_phase` inside the declared `A_phase` class would be required to patch obvious failures, but these modifications would need to depend on particular models in ways that violate the fairness and non cheating constraints, then the current form of `E_PHASE_Q030_V1` is also considered rejected.

**Semantics implementation note**

All quantities are treated according to the hybrid field interpretation declared in the metadata. Continuous parts describe fields and entanglement profiles. Discrete parts describe index tuples and phase labels. No additional interpretation layers are introduced in this experiment.

**Boundary note**

Falsifying the encoding element `E_PHASE_Q030_V1` for this experiment does not solve the canonical classification problem. It only shows that this particular effective encoding is not adequate for the tested model family.

---

### Experiment 2: Edge bulk anomaly consistency test

**Goal**

Check whether the edge bulk part of `E_PHASE_Q030_V1`, in particular the combination of `ES`, `TI`, `RC` and `Tension_edge_bulk`, can maintain consistent relations between bulk invariants and protected boundary phenomena across families of models.

**Setup**

* Choose models where theory predicts clear correspondence between bulk invariants and boundary behaviour, for example integer quantum Hall systems or two dimensional topological insulators with robust edge modes.
* Use the candidate invariant library `L_phase` and the edge bulk tension functional `Tension_edge_bulk` from `E_PHASE_Q030_V1`.

**Protocol**

1. For each model and appropriate geometries, construct `m_r` in `M_phase_reg` that encodes bulk properties and corresponding boundary properties at resolution `r`.
2. Compute `TI(m_r)` and `RC(m_r; probe_edge)` for probes that test for edge states and anomaly inflow.
3. Use theoretical expectations to label which combinations of `TI` should imply which edge responses.
4. Count mismatches where:

   * bulk `TI` components predict protected edge phenomena but `RC` shows no such signature, or
   * edge responses indicate protected modes while bulk `TI` encodes a trivial phase.
5. For each `m_r`, compute `Tension_edge_bulk(m_r; L_phase)` from these mismatches according to the rule bundled into `E_PHASE_Q030_V1`.

**Metrics**

* Fraction of models in the test set with consistent bulk edge behaviour.
* Distribution of `Tension_edge_bulk(m_r; L_phase)` across the set.
* Robustness of these results under modest changes in `r` or in how `RC` is summarised, within the admissible encoding rules.

**Falsification conditions**

* Before running the experiment, fix:

  * a maximum acceptable value for `Tension_edge_bulk` in models where bulk edge correspondence is well understood, and
  * a maximum tolerated mismatch rate.
* If, for a representative class of models where bulk edge correspondence is well understood, the encoding produces many systematic mismatches or persistently large `Tension_edge_bulk` values, then the edge bulk part of `E_PHASE_Q030_V1` is considered misaligned and the encoding element is rejected.
* If the encoding only produces good correspondence after fine tuning details that effectively customise `L_phase` or the edge bulk functional to each model, it violates the admissible library constraint and is rejected.

**Semantics implementation note**

Bulk and edge properties are treated within the same hybrid interpretation as in Experiment 1. Summary descriptors are restricted to the declared dynamical_field and thermodynamic_tension roles. No additional deep layer mechanism is assumed.

**Boundary note**

Falsifying the encoding element `E_PHASE_Q030_V1` for this experiment does not solve the canonical classification problem. It constrains how well this particular finite invariant library and edge bulk functional express bulk edge correspondence, but it does not prove that a universally good library exists or does not exist.

---

## 7. AI and WFGY engineering spec

This block describes how Q030 is used as an engineering module for AI systems inside WFGY, still at the effective layer and under the fixed encoding element `E_PHASE_Q030_V1`.

### 7.1 Training signals

We define several training signals that can be implemented without exposing any deep TU rules.

1. `signal_phase_equivalence_consistency`

   * Definition: a penalty based on `DeltaS_intra(m_r; L_phase)` for contexts where the model has implicitly committed to a single phase description.
   * Purpose: encourage the model to represent phase consistent stories where order parameters, entanglement, topological indices and responses do not contradict each other.

2. `signal_phase_boundary_detection`

   * Definition: a signal derived from changes in `Inv_L(m_r)` along parameter sweeps. Large changes at points where the model claims that no phase transition occurs are penalised.
   * Purpose: help the model learn coherent phase diagrams and correctly identify phase transitions versus smooth crossovers.

3. `signal_edge_bulk_consistency`

   * Definition: a penalty based on `Tension_edge_bulk(m_r; L_phase)` in examples where bulk edge correspondence is expected to hold.
   * Purpose: push the model to maintain consistency between bulk descriptors and boundary phenomena in its internal representations and outputs.

4. `signal_phase_cluster_separation`

   * Definition: a reward when internal representations of models in different phases form well separated clusters in embedding space, in alignment with `Inv_L` derived phase labels.
   * Purpose: help the model internalise phase distinctions in a geometric way that aligns with Q030.

### 7.2 Architectural patterns

We describe module patterns that reuse Q030 structures.

1. `PhaseClassifierHead`

   * Role: given an internal representation of a many body context, produce a phase label or phase embedding.
   * Interface:

     * Input: internal embeddings for a model plus context about parameters.
     * Output: phase class probabilities or a low dimensional phase embedding that can be compared between models.

2. `PhaseTensionEstimator`

   * Role: estimate `Tension_phase(m_r; L_phase)` from internal representations.
   * Interface:

     * Input: internal embeddings and any extracted `Inv_L` like quantities.
     * Output: scalar phase tension estimates and decomposed contributions, for example from intra phase consistency and cover penalties.

3. `EdgeBulkChecker`

   * Role: evaluate edge bulk consistency at the effective layer using Q030 templates.
   * Interface:

     * Input: embeddings for bulk contexts and boundary contexts.
     * Output: a soft score indicating how well bulk and edge features align with known patterns.

### 7.3 Evaluation harness

We outline an evaluation harness for AI models augmented with Q030 modules.

1. Task collection

   * Include tasks that require reasoning about phase diagrams, quantum critical points and characteristic properties of phases in standard condensed matter models.

2. Conditions

   * Baseline condition:

     * model without `PhaseClassifierHead` or `PhaseTensionEstimator`, trained or prompted in a general way.
   * TU condition:

     * same base model but with Q030 derived modules and training signals integrated in fine tuning or structured prompting.

3. Metrics

   * Accuracy on phase identification questions for benchmark models.
   * Correctness of predicted phase diagrams along known parameter sweeps.
   * Frequency of bulk edge mismatches in explanations or predictions.
   * Stability of answers when prompts are rephrased or details perturbed.

### 7.4 60 second reproduction protocol

This protocol lets external users experience the impact of Q030 style encoding in a short interaction.

* Baseline setup:

  * Prompt the AI with a description of a standard quantum lattice model and ask it to explain the phase diagram and nature of the phases, without any mention of Tension Universe or Q030.
  * Observe whether the explanation mixes unrelated criteria, omits entanglement and topological structure, or contradicts known results.
* TU encoded setup:

  * Use a second prompt for the same model that explicitly instructs the AI to:

    * describe phases in terms of finite invariant libraries,
    * articulate how order parameters, entanglement, topological indices and response coefficients fit together,
    * highlight where classification appears simple and where it appears hard.
* Comparison metric:

  * Rate both answers on:

    * internal consistency,
    * explicit mention of phase invariants,
    * clarity about what is known and unknown in classification.
* What to log:

  * the prompts used,
  * the full responses,
  * any internal estimates of `Tension_phase(m_r; L_phase)` or `Tension_edge_bulk(m_r; L_phase)` if the system exposes them.

These logs support later inspection without revealing any hidden TU generative rule.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q030 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `PhaseTensionFunctional`

   * Type: functional
   * Minimal interface:

     * Inputs: phase summary state `m_r` in `M_phase_reg`, finite invariant library description `L_phase`.
     * Output: scalar value `Tension_phase(m_r; L_phase)`.
   * Preconditions:

     * `Inv_L(m_r)` is defined and finite.
     * `L_phase` belongs to the admissible library class `A_phase` for the domain under study.

2. ComponentName: `PhaseInvariantLibraryDescriptor`

   * Type: field or functional descriptor
   * Minimal interface:

     * Inputs: specification of dimension, symmetry class and interaction regime.
     * Output: a concrete `L_phase` description, including:

       * which invariants are used,
       * how they are aggregated,
       * how resolution parameter `r` is handled.
   * Preconditions:

     * The descriptor must be fixed before analysing particular models.

3. ComponentName: `CounterfactualPhaseWorld_Template`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: model family description and candidate invariant library `L_phase`.
     * Output: experimental setups and analysis rules for World T like and World F like scenarios as in Sections 5 and 6.
   * Preconditions:

     * The model family must admit at least coarse phase identifications by independent means for comparison.

### 8.2 Direct reuse targets

1. Q031 (BH_PHYS_HOLOGRAPHIC_PHASES_L3_031)

   * Reused components: `PhaseTensionFunctional`, `PhaseInvariantLibraryDescriptor`, `CounterfactualPhaseWorld_Template`.
   * Why it transfers: holographic and gravitational phases can be organised by invariant libraries for entanglement and geometry, closely analogous to condensed matter phases.
   * What changes: the nature of invariants and observables moves from local order parameters and transport to geometric and entanglement entropies in gravity.

2. Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)

   * Reused components: `PhaseInvariantLibraryDescriptor`.
   * Why it transfers: high temperature superconductivity is mediated by complex phase diagrams with competing orders. Q030 provides the invariant library structure to organise these phases.
   * What changes: specific invariants emphasise superconducting order parameters, pseudogap behaviour and relevant correlation functions.

3. Q059 (BH_CS_INFO_THERMODYN_L3_059)

   * Reused components: `PhaseTensionFunctional`.
   * Why it transfers: phases of information processing and learning can be viewed through the lens of phase diagrams and finite invariants. Phase tension provides a scalar summary of how well a set of invariants separates regimes.
   * What changes: observables become information theoretic quantities rather than physical order parameters.

4. Q123 (BH_AI_INTERP_L3_123)

   * Reused components: `PhaseTensionFunctional`, `CounterfactualPhaseWorld_Template`.
   * Why it transfers: internal states of AI systems can be grouped into phases of representation with different qualitative behaviours. Q030 templates help define tension between coarse interpretability libraries and rich internal dynamics.
   * What changes: states `m_r` represent model internal activations or attention patterns instead of physical phases.

---

## 9. TU roadmap and verification levels

This block places Q030 on the TU verification ladder and defines next measurable steps, always at the effective layer and under `E_PHASE_Q030_V1`.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of quantum phase classification has been specified, including:

    * state space `M_phase`,
    * finite invariant libraries `L_phase` in an admissible class `A_phase`,
    * tension functionals `Tension_phase` and `Tension_edge_bulk`,
    * singular set `S_sing_phase` and domain restriction `M_phase_reg`.
  * At least two experiments with clear falsification conditions for the encoding element `E_PHASE_Q030_V1` have been described.

* N_level: N1

  * The narrative links microscopic Hamiltonians, phases, finite invariant libraries and classification tension in a clear way.
  * Counterfactual worlds T and F are defined in terms of observable patterns and do not rely on deep layer content.

### 9.2 Next measurable step toward E2

To advance Q030 from E1 to E2 the following measurable steps are proposed.

1. Implement a concrete `PhaseTensionFunctional` and a `PhaseInvariantLibraryDescriptor` for a selected two dimensional model class, for example spin systems with given symmetries.

2. Run a finite invariant stress test similar to Experiment 1 with publicly documented model families, publishing:

   * descriptions of `L_phase`,
   * the set of models and parameter sweeps,
   * computed tension profiles,
   * lists of phase relation contradictions.

3. Optionally implement the edge bulk anomaly consistency test for standard topological phases and publish the distribution of `Tension_edge_bulk(m_r; L_phase)`.

These steps remain at the effective layer and do not expose any deep TU generative rule.

### 9.3 Long term role in TU

In the longer term Q030 is expected to serve as:

* the canonical template for thermodynamic_tension problems in quantum many body physics,
* a bridge between condensed matter classification programs and similar classification questions in quantum gravity and information theory,
* a test bed for how far finite invariant libraries can go in taming extremely complex phase spaces before deep layer structure must be invoked.

---

## 10. Elementary but precise explanation

This block gives a precise but accessible explanation of Q030.

In everyday language a phase of matter is a way that matter can organise itself. Water, ice and steam are different phases. In quantum many body systems there are many more exotic phases. Some have topological order, some have protected edge states, some differ mainly in how their quantum entanglement is arranged.

The classification problem asks a simple sounding question.

> Is there a finite checklist that lets us tell which quantum phase we are in?

For example, could we write down a finite list of numbers and labels such that:

* if two systems have the same list, they are in the same phase,
* if they have different lists, they are in different phases.

In practice we already use ingredients like order parameters, topological indices, entanglement patterns and response coefficients. The question is whether some finite combination of these is enough, even in complicated interacting systems.

In the Tension Universe view we do not try to solve this question by deep theory inside this document. Instead we:

* define an effective space of phase summaries,
* define what it means to pick a finite library of phase invariants,
* define a tension measure that becomes small when the library works well and large when it fails.

We then imagine two kinds of worlds.

* In one world there are invariant libraries that keep this tension small across all realistic phases. Classification is hard but tame.
* In the other world every finite library eventually runs into trouble. The tension never really goes away as we explore more phases and more detailed models.

Q030 does not assert which world is real. It provides a clean way to talk about these possibilities in terms of observable patterns, experiments and AI modules. It gives a template for building tools that measure how well current classification schemes are doing, and for deciding when we need new ideas rather than more detailed tuning.

In this sense Q030 is the main BlackHole node for quantum phases of matter. It encodes how close we are to having a usable map of the phase landscape, and how much tension remains between simple classification schemes and the richness of quantum many body physics.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S problem collection. It encodes Q030, “Classification of quantum phases of matter”, at the effective layer of the TU framework.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the Q030 problem inside the fixed encoding element `E_PHASE_Q030_V1`.
* It does not claim to solve the canonical open problem of classifying all quantum phases of matter.
* It does not introduce any new theorem about condensed matter physics beyond what is already established in the cited literature.
* It should not be cited as evidence that the full classification problem has been settled, nor that any particular phase diagram is complete.

### Effective layer boundary

* All objects used here (state spaces `M_phase`, observables, invariant libraries, tension scores, counterfactual worlds) live at the TU effective layer as defined in the TU Effective Layer Charter.
* This entry does not expose TU core axioms, deep layer generative rules, or any explicit mapping from microscopic Hamiltonians or raw data into TU fields.
* Parameters such as `lambda(m_r)` and `kappa_phase` are treated as opaque imports from the TU core. They are not defined, tuned or justified inside this document.

### Encoding and fairness commitments

* This page fixes a single encoding element `E_PHASE_Q030_V1`, which includes the admissible library class `A_phase`, the reference library identifiers, the weight scheme and the tension functionals used in all experiments and AI modules.
* Any substantial change to these ingredients must be treated as a new encoding element with a new `EncodingKey_Q030` and a corresponding update to the header metadata.
* Experiments in Section 6 are designed to falsify or support `E_PHASE_Q030_V1` as an effective encoding. Rejecting this encoding element does not imply that no good encoding exists. Accepting it does not imply that the canonical problem has been solved.

### Cross problem reuse

* Components defined here, such as `PhaseTensionFunctional`, `PhaseInvariantLibraryDescriptor` and `CounterfactualPhaseWorld_Template`, are intended for reuse by other BlackHole nodes only at the effective layer.
* Any reuse in other problems must respect the same effective layer boundary and fairness constraints. In particular, reusers must not reinterpret these components as evidence about deep layer TU structure.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
