# Q063 · Full physical solution of protein folding

## 0. Header metadata

```txt
ID: Q063
Code: BH_CHEM_PROTEIN_FOLDING_L3_063
Domain: Chemistry
Family: Biophysical chemistry
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Partial
Semantics: hybrid
E_level: E1
N_level: N1
EncodingKey: Q063_FOLDING_CORE_V1
LibraryKey: Q063_FOLDING_LIB_V1
WeightKey: Q063_FOLDING_WEIGHTS_V1
RefinementKey: Q063_FOLDING_REFINE_V1
Last_updated: 2026-01-29
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* The goal of this document is to provide an **effective layer encoding** of the classical protein folding problem, using:

  * abstract state spaces,
  * observables and invariants,
  * tension functionals,
  * and falsifiable experiment patterns.
* This document **does not**:

  * claim to provide a full physical solution of protein folding,
  * introduce any new theorem or physical law,
  * modify the canonical scientific statements listed in Section 1,
  * or expose any TU axioms, deep generative rules, or construction mechanisms.

More precisely:

* The state space `M`, the regular subset `M_reg`, the singular set `S_sing`, and all observables, invariants, and tension functionals are **summary objects** that live only at the effective layer.

* No mapping is specified from raw microscopic data (for example atomistic simulations, experiments) to TU internal fields. Any such mapping, if used in practice, is an external implementation choice outside the scope of this document.

* All falsifiability and experiment statements refer to the **Q063 encoding** identified by:

  ```txt
  EncodingKey:   Q063_FOLDING_CORE_V1
  LibraryKey:    Q063_FOLDING_LIB_V1
  WeightKey:     Q063_FOLDING_WEIGHTS_V1
  RefinementKey: Q063_FOLDING_REFINE_V1
  ```

  and to possible future encodings that would use different keys. They do not claim to falsify or confirm the physical truth of protein folding in nature.

* The metadata field `Status: Partial` refers to the canonical scientific status of the protein folding problem. It reflects that there are powerful partial resolutions but no widely accepted complete theory in the strong sense defined below. It does **not** indicate that TU has partially solved the problem.

This page is meant to be read together with the TU charters listed in the footer, which govern effective layer boundaries, encoding and fairness constraints, and tension scale conventions.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The classical protein folding problem can be stated as follows.

Given:

* an amino acid sequence `seq`,
* a specification of environmental conditions `env` (for example temperature, solvent, ionic strength),

find a predictive and physically grounded theory that:

1. Determines the native structure or ensemble of structures favored by `seq` under `env`.
2. Predicts folding pathways and timescales from unfolded to native states.
3. Quantifies misfolding propensities, metastable states, and aggregation routes.
4. Does so with a finite set of effective principles that apply across a wide range of sequences and conditions.

A "full physical solution" of protein folding, in the sense of this problem, means:

* a finite library of effective rules and invariants that,
* given `seq` and `env`,
* yields accurate predictions of:

  * native structure ensemble,
  * folding kinetics,
  * misfolding and aggregation behavior,

up to specified tolerances, without requiring case by case empirical fitting for each new sequence.

This problem lies at the intersection of chemistry, physics, and biology. It is central to understanding how sequence level information translates into functional three dimensional structures in living systems.

### 1.2 Status and difficulty

Important partial resolutions include:

* The energy landscape and folding funnel picture, which explains how rapid and reproducible folding can emerge from high dimensional rugged energy landscapes.
* Detailed experimental and computational studies for specific small proteins, where folding pathways, intermediates, and rates are known at high resolution.
* Physics based and machine learning based structure predictors that address the structure prediction aspect for many cases, often with high accuracy for static structures.

However:

* There is no single, compact, physically grounded theory that:

  * predicts folding pathways, rates, and misfolding behavior for arbitrary sequences and environments, and
  * is widely accepted as complete in the strong sense defined above.
* Many proteins are marginally stable, exhibit complex multi state folding, or are coupled to chaperones and cellular machinery. These features complicate any attempt at a universal theory.
* Strongly correlated effects, solvent interactions, and collective motions make it difficult to derive simple rules directly from microscopic physics.

The canonical problem is therefore considered extremely difficult. Current approaches provide powerful tools and partial solutions, but not a complete, unified, finite principle theory in the sense used here.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q063 plays several roles.

1. It is the flagship thermodynamic_tension problem for biophysical chemistry, where:

   * high dimensional microscopic interactions,
   * low dimensional effective descriptors,
   * and biological constraints
     must be reconciled at the effective layer.
2. It provides a concrete setting to test whether:

   * rugged energy landscapes,
   * folding funnels,
   * and misfolding phenomena
     can be described by a small number of effective invariants and libraries, or whether irreducible residual tension remains.
3. It anchors cross domain connections between:

   * chemistry and soft matter physics (rugged landscapes and glass like behavior),
   * biology (sequence to function mapping and evolution),
   * and AI (energy landscape metaphors for representation and optimization).

The remaining sections describe how this problem is encoded in the Tension Universe framework without changing its canonical scientific content.

### References

1. K. A. Dill, J. L. MacCallum, "The protein folding problem, 50 years on", Science 338, 1042–1046 (2012).
2. J. N. Onuchic, P. G. Wolynes, Z. Luthey Schulten, N. D. Socci, "Toward an outline of the topography of a realistic protein folding funnel", Proceedings of the National Academy of Sciences 92, 3626–3630 (1995).
3. C. M. Dobson, "Protein folding and misfolding", Nature 426, 884–890 (2003).
4. P. G. Wolynes, J. N. Onuchic, D. Thirumalai, "Navigating the folding routes", Science 267, 1619–1620 (1995).
5. J. L. Klepeis, K. Lindorff Larsen, R. O. Dror, D. E. Shaw, "Long timescale molecular dynamics simulations of protein structure and function", Current Opinion in Structural Biology 19, 120–127 (2009).

---

## 2. Position in the BlackHole graph

This block records how Q063 sits inside the BlackHole graph as nodes and edges among Q001–Q125. Each edge is listed with a one line reason that points to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q063 relies on at the effective layer.

* Q061 (BH_CHEM_BOND_NATURE_L3_061)
  Reason: Provides effective description of chemical bonding in strongly correlated systems, which justifies using coarse grained folding energy models based on local interactions.

* Q067 (BH_CHEM_QUANTUM_MOL_SIM_L3_067)
  Reason: Supplies limits and patterns for quantum and classical simulation of complex molecules, constraining how folding energy landscapes can be approximated.

* Q071 (BH_BIO_ORIGIN_LIFE_L3_071)
  Reason: Origin of life scenarios depend on foldable polymers and require low tension folding landscapes as building blocks.

### 2.2 Downstream problems

These problems are direct reuse targets of Q063 components or depend on Q063 tension structure.

* Q071 (BH_BIO_ORIGIN_LIFE_L3_071)
  Reason: Reuses the FoldingEnergyLandscapeDescriptor component to evaluate which early sequences could support stable folding.

* Q078 (BH_BIO_DEVELOPMENTAL_L3_078)
  Reason: Uses the SequenceToStructureConsistency component from Q063 to connect genotype changes to protein level changes during development.

* Q080 (BH_BIO_BIOSPHERE_LIMITS_L3_080)
  Reason: Depends on the MisfoldDegeneracyIndex from Q063 to discuss how folding robustness constrains biosphere scale adaptability.

### 2.3 Parallel problems

Parallel nodes share similar tension types or structural patterns but no direct component dependence.

* Q064 (BH_CHEM_GLASS_TRANS_L3_064)
  Reason: Both Q063 and Q064 involve rugged energy landscapes and thermodynamic_tension between local minima and macroscopic behavior.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: Both study self assembly in soft matter and depend on funnels, metastable basins, and kinetic trapping.

* Q077 (BH_BIO_MICROBIOME_L3_077)
  Reason: Both involve many body interactions on rugged landscapes, although Q077 focuses on ecosystem level fitness landscapes.

### 2.4 Cross domain edges

Cross domain edges connect Q063 to problems in other domains that can reuse its components.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Reuses folding landscape descriptors as concrete examples of non trivial thermodynamic systems with many metastable states.

* Q095 (BH_EARTH_BIODIVERSITY_L3_095)
  Reason: Uses folding robustness and misfold tension as one microscopic source for macro scale biodiversity patterns.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Reuses the EnergyLandscapeObserver pattern from Q063 as a template for describing energy like landscapes in AI representation spaces.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Uses the MisfoldDegeneracyIndex as an analogy for counting harmful basins in AI objective or policy landscapes.

All edges reference only Q identifiers. No external identifiers are needed to merge Q063 into a global adjacency list.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions,
* and the admissible encoding class associated with the metadata keys.

We do not describe any hidden generative rules or any mapping from raw data to internal TU fields.

### 3.1 State space

We assume an effective state space:

```txt
M
```

with the following interpretation.

* Each element `m` in `M` represents a coherent "folding configuration" for:

  * a fixed amino acid sequence `seq`,
  * a fixed environment `env` (for example temperature, solvent, ionic strength),
    including only coarse grained summaries, not microscopic details.

For each `m` in `M`, the encoding contains:

* a set of conformational basins (for example native basin and misfold basins) with associated free energies,
* effective transition rates or barriers between the main basins,
* occupation probabilities or weights for each basin at the chosen environmental conditions.

We do not specify how `m` is constructed from atomistic simulations or experiments. We only assume:

* for any realistic sequence and environment, there exist states `m` that summarize folding relevant information at some resolution,
* there is a regular subset `M_reg` of `M` where all observables defined below are well defined and finite.

The semantics are **hybrid**:

* conformational landscapes, free energies, and timescales are treated as continuous fields or real valued observables,
* sequence and environment labels, and basin identifiers, are treated as discrete indices that parameterize those fields.

This is the meaning of `Semantics: hybrid` in the header metadata.

### 3.2 Effective fields and observables

On `M`, we introduce the following effective observables.

1. Native basin free energy

   ```txt
   E_native(m)
   ```

   * a real valued observable giving the effective free energy of the native basin for the sequence and environment encoded in `m`.

2. Competing basin free energy

   ```txt
   E_competing(m)
   ```

   * a real valued observable summarizing the free energy of the most relevant competing misfolded basins. This may be the lowest misfold free energy or an effective aggregate.

3. Native occupancy

   ```txt
   P_native(m)
   ```

   * a number in the interval `[0, 1]` giving the probability weight of the native basin in the ensemble represented by `m` under the chosen conditions.

4. Misfold occupancy

   ```txt
   P_misfold(m)
   ```

   * a number in the interval `[0, 1]` giving the total probability weight assigned to misfolded basins in `m`.

5. Landscape roughness index

   ```txt
   R_rough(m)
   ```

   * a nonnegative scalar summarizing the roughness of the energy landscape, for example based on the distribution of barrier heights and basin depths.

6. Folding timescale

   ```txt
   tau_fold(m)
   ```

   * a positive scalar summarizing the effective timescale for folding from an unfolded ensemble to the native basin under the conditions encoded in `m`.

7. Misfold escape timescale

   ```txt
   tau_misfold(m)
   ```

   * a positive scalar summarizing the effective timescale for escape from typical misfolded basins into the native basin or other basins.

All of these observables take values in suitable subsets of real space, consistent with the parameter space used in the general TU core.

### 3.3 Encoding class and admissible constructions

The Q063 encoding identified by the metadata keys

```txt
EncodingKey:   Q063_FOLDING_CORE_V1
LibraryKey:    Q063_FOLDING_LIB_V1
WeightKey:     Q063_FOLDING_WEIGHTS_V1
RefinementKey: Q063_FOLDING_REFINE_V1
```

uses the following **admissible encoding class** at the effective layer.

1. **Funnel profile library**

   * There is an admissible class `F_funnel_adm` of reference funnel profiles.
   * Each profile is a map that assigns an idealized energy landscape shape to:

     * a range of sequence lengths,
     * a coarse environment class.
   * All profiles in `F_funnel_adm` are defined by the library associated with `LibraryKey = Q063_FOLDING_LIB_V1`.

2. **Structural target library**

   * There is an admissible class `S_target_adm` of structural targets and similarity metrics.
   * Each element specifies:

     * a representation of the target native ensemble for a given sequence and environment class,
     * a structural similarity metric and tolerance used to compare an encoded ensemble to the target.
   * The allowed targets and metrics are also determined by `LibraryKey = Q063_FOLDING_LIB_V1`.

3. **Reference selections for this encoding**

   For the specific encoding `Q063_FOLDING_CORE_V1` we fix, once and for all:

   * a reference selection rule `Profile_ref` that picks a unique funnel profile from `F_funnel_adm` for any given sequence length and environment class,
   * a reference selection rule `Structure_ref` that picks a structural target and similarity metric from `S_target_adm` for any given sequence and environment class.

   These selection rules are part of the library and refinement specification and do not depend on the detailed data of individual states `m`.

4. **Mismatch functionals**

   The functionals

   ```txt
   DeltaS_funnel(m)
   DeltaS_seq_struct(m)
   ```

   are defined as follows.

   * For any `m` in `M_reg`, `DeltaS_funnel(m)` is computed by comparing the encoded landscape in `m` to the reference funnel profile `Profile_ref` for the corresponding length and environment class. The comparison uses only constructions from `F_funnel_adm`.
   * For any `m` in `M_reg`, `DeltaS_seq_struct(m)` is computed by comparing the encoded native ensemble in `m` to the structural target chosen by `Structure_ref`, using the associated similarity metric and tolerance.

   Both functionals must satisfy:

   * nonnegativity for all `m` in `M_reg`,
   * `DeltaS_funnel(m) = 0` if and only if the encoded landscape matches the reference profile within the predefined tolerance for that profile,
   * `DeltaS_seq_struct(m) = 0` if and only if the encoded ensemble matches the target within the predefined tolerance for that target,
   * stability under moderate changes in coarse graining that preserve the shape of the landscape and ensemble at the effective layer.

   Any implementation that satisfies these constraints and uses only constructions from the admissible libraries is considered part of the same encoding class.

5. **Weight specification and refinement**

   The folding tension is defined as

   ```txt
   Tension_fold(m) = a1 * DeltaS_funnel(m) + a2 * DeltaS_seq_struct(m)
   ```

   where:

   * `a1 > 0` and `a2 > 0` are fixed real coefficients assigned by `WeightKey = Q063_FOLDING_WEIGHTS_V1`,
   * the pair `(a1, a2)` does not depend on the specific sequence, environment, or dataset,
   * optionally, additional constraints such as `a1 + a2 = 1` may be imposed in the weight specification, but they are part of the same key.

   If any of the following changes are made:

   * funnel profile library or selection rule,
   * structural target library or selection rule,
   * weight coefficients or their constraints,
   * coarse graining or numerical approximation schemes that materially affect tension values,

   then the encoding is considered a **different** effective layer encoding of Q063 and must receive a new combination of:

   ```txt
   EncodingKey, LibraryKey, WeightKey, RefinementKey
   ```

   Experiments and comparisons are required to specify which key combination they use. This rule is part of the encoding and fairness charter.

### 3.4 Invariants and effective constraints

From the observables above, we define several effective invariants.

1. Native energy gap

   ```txt
   Gap_native(m) = E_competing(m) - E_native(m)
   ```

   * a real valued quantity representing the energy separating the native basin from its main competitors.

2. Funnel sharpness index

   ```txt
   Funnel_sharpness(m)
   ```

   * a dimensionless, nonnegative scalar that captures how strongly the landscape is biased toward the native basin as a function of some reaction coordinate,
   * higher values correspond to a clearer funnel into the native state, lower values correspond to more frustrated or flat landscapes.

3. Misfold fraction

   ```txt
   Misfold_fraction(m) = P_misfold(m)
   ```

   * a scalar in `[0, 1]` measuring how much of the ensemble weight resides in misfolded basins.

4. Kinetic separation ratio

   ```txt
   K_sep(m) = tau_misfold(m) / tau_fold(m)
   ```

   * a dimensionless ratio comparing the timescale for escaping misfolds to the timescale for folding, when both are defined.

These invariants are required to be stable under moderate changes in coarse graining of the landscape for states in `M_reg`.

### 3.5 Singular set and domain restrictions

Some observables may be undefined or not finite, for example:

* when the effective description has not converged,
* when basin identification is ambiguous,
* or when folding behavior cannot be summarized by a small number of basins at the chosen resolution.

We define the singular set:

```txt
S_sing = { m in M :
           E_native(m), E_competing(m),
           P_native(m), P_misfold(m),
           R_rough(m), tau_fold(m), tau_misfold(m)
           are not all well defined and finite }
```

Domain restriction:

* All folding tension analysis is restricted to the **regular domain**

  ```txt
  M_reg = M \ S_sing
  ```

* For `m` in `S_sing`, invariants such as `Gap_native`, `Funnel_sharpness`, `Misfold_fraction`, and `K_sep` are treated as **out of domain** rather than as extreme values.

* Experiments and protocols in this document are required to specify that they operate only on states in `M_reg`. If certain proteins or conditions cannot be mapped into `M_reg` under a given encoding, they are recorded as out of domain for that encoding and are not used as evidence for or against the encoding.

This choice emphasizes domain restriction as the primary treatment of singular behavior. When needed, additional regularization procedures may be used in practical implementations, but these are outside the TU effective layer definition and would be covered by `RefinementKey`.

---

## 4. Tension principle for this problem

This block states how Q063 is characterized as a tension problem within the Tension Universe at the effective layer.

### 4.1 Core tension functional

We first recall the mismatch measures.

* Funnel mismatch

  ```txt
  DeltaS_funnel(m)
  ```

  * a nonnegative scalar measuring how far the landscape encoded in `m` deviates from a reference ideal funnel profile for the same sequence length and environment class, chosen from the admissible profile library associated with `LibraryKey`,
  * `DeltaS_funnel(m) = 0` if the encoded landscape matches the chosen reference funnel profile within the predefined tolerance for `EncodingKey = Q063_FOLDING_CORE_V1`,
  * `DeltaS_funnel(m)` increases when the energy gap is small, the funnel is flat, or roughness is high relative to the reference profile.

* Sequence structure mismatch

  ```txt
  DeltaS_seq_struct(m)
  ```

  * a nonnegative scalar measuring how far the encoded structure ensemble in `m` deviates from a target set of structures determined by sequence and environment,
  * the target and similarity metric are chosen from `S_target_adm` by the selection rule encoded in `LibraryKey`,
  * `DeltaS_seq_struct(m) = 0` if the native ensemble matches the target set within the specified structural similarity tolerance.

The folding tension functional is then:

```txt
Tension_fold(m) = a1 * DeltaS_funnel(m) + a2 * DeltaS_seq_struct(m)
```

where:

* `a1 > 0` and `a2 > 0` are fixed coefficients determined by `WeightKey = Q063_FOLDING_WEIGHTS_V1`,
* the same pair `(a1, a2)` is used for all states in `M_reg` under this encoding,
* `Tension_fold(m) >= 0` for all `m` in `M_reg`.

**Fairness and stability constraints**

* The reference funnel profiles, structural targets, similarity metrics, and coefficients `(a1, a2)` used to define `Tension_fold` are specified by the combination of keys:

  ```txt
  EncodingKey, LibraryKey, WeightKey, RefinementKey
  ```

* For a fixed key combination, these objects are chosen **before** evaluating any particular dataset or sequence collection and are not retuned after inspecting the tension values on specific states.

* If any of these choices are changed in response to data for a given benchmark or sequence family, the result is considered a **different encoding** of Q063 and must be labeled with new keys. It cannot be compared directly to the original encoding as if it were the same.

These constraints prevent trivial tension minimization by adjusting reference profiles or weights after seeing the data. They implement the TU encoding and fairness charter at the level of Q063.

### 4.2 Folding as a low tension principle

At the effective layer, the existence of a "full physical solution" for protein folding can be reframed as:

> For biologically relevant sequences and environments, there exist regular states in `M_reg` whose folding tension `Tension_fold` can be kept within a narrow low band across scales and resolutions, using a finite library of effective rules tied to a small number of encoding keys.

More concretely, for any admissible encoding that satisfies the fairness constraints above, there should exist world representing states `m_true` such that:

```txt
Tension_fold(m_true) <= epsilon_fold
```

where:

* `epsilon_fold` is a small threshold depending on measurement precision and modeling granularity,
* `epsilon_fold` does not grow without bound as the resolution of the encoding and the quality of data improve,
* the same encoding keys and admissible classes are used across a broad set of sequences and environments.

In such a world, the apparent complexity of folding landscapes can be compressed into a small set of effective invariants and rules, and the residual thermodynamic_tension between microscopic physics, sequence information, and folding outcomes is low.

### 4.3 Failure as persistent high tension

If no such finite principle description exists, then for any admissible encoding satisfying the constraints above, world representing states would eventually exhibit persistent high tension:

```txt
Tension_fold(m_false) >= delta_fold
```

for some strictly positive `delta_fold` that:

* cannot be driven arbitrarily close to zero by refining encodings or improving data while keeping the key combination fixed,
* persists across large classes of sequences and environments, not just pathological cases.

In this case, folding would remain fundamentally resistant to compression into a finite library of effective rules, and thermodynamic_tension between microscopic complexity, sequence, and structure would remain irreducible.

In summary, Q063, at the effective layer, asks whether the universe of biologically relevant protein folding lies in a low tension regime governed by a finite set of rules, or in a regime where significant residual tension remains even after careful modeling within a fixed encoding.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds, both described strictly at the effective layer. They differ only in the patterns of observables and tension functionals, not in any hidden TU generative rule.

* World T: folding is governed by a compact, effective theory and belongs to a low tension regime.
* World F: no compact effective theory exists, and folding belongs to a persistent high tension regime.

### 5.1 World T (compact folding theory, low tension)

In World T:

1. Stable low tension band for native proteins

   * For most naturally occurring single domain proteins and biologically relevant environments, there exist states `m_T` in `M_reg` such that:

     ```txt
     Tension_fold(m_T) <= epsilon_fold
     ```

     for a small `epsilon_fold` that is nearly constant across protein families.

2. Predictable energy gaps and funnels

   * `Gap_native(m_T)` and `Funnel_sharpness(m_T)` follow simple relationships as functions of sequence features and environment descriptors.
   * These relationships can be expressed with a finite library of effective rules that generalize across many systems.

3. Controlled misfolding

   * `Misfold_fraction(m_T)` and `K_sep(m_T)` remain within predictable ranges for most native proteins in their physiological environments.
   * Deviations, when they occur, can be traced to well understood causes (for example extreme sequences, pathological environments) that are themselves captured by the same effective framework.

4. Compressible landscape diversity

   * Despite microscopic richness, the diversity of landscapes across proteins can be described using a modest number of landscape archetypes, each associated with specific ranges of invariants.

In such a world, once the effective theory is known, sequence and environment determine folding outcomes with relatively small residual tension.

### 5.2 World F (no compact theory, persistent high tension)

In World F:

1. Persistent high tension for many sequences

   * For a large class of biologically relevant sequences and environments, any state `m_F` in `M_reg` that faithfully represents true folding behavior satisfies:

     ```txt
     Tension_fold(m_F) >= delta_fold
     ```

     for some `delta_fold` that remains significantly larger than zero even as encodings and data improve.

2. Uncompressible landscape variability

   * `Gap_native(m_F)`, `Funnel_sharpness(m_F)`, and `R_rough(m_F)` vary in ways that cannot be captured by a finite set of archetypes without large residual errors.
   * Attempts to classify landscapes into a small number of types for predictive purposes fail or require frequent ad hoc exceptions.

3. Misfolding unpredictability

   * `Misfold_fraction(m_F)` and `K_sep(m_F)` exhibit patterns that cannot be reliably predicted from sequence and environment by any finite library of rules.
   * Even within narrow families of sequences, folding and misfolding behaviors remain idiosyncratic.

4. No stable low tension band

   * There is no robust low tension band common to most natural proteins. Instead, tension levels are broadly distributed and sensitive to small changes in sequence or conditions.

In such a world, the thermodynamic_tension between microscopic complexity and macroscopic folding behavior remains intrinsically high.

### 5.3 Interpretive note

These counterfactual worlds do not construct TU internal fields from raw data. They only assert that:

* if there exist states `m` that faithfully represent either a compact theory world or a non compact world,
* then the observable patterns of folding invariants and the behavior of `Tension_fold` would differ qualitatively as described above.

The distinction is made entirely at the effective layer and is tied to specific encoding keys.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q063 encoding,
* distinguish between different folding tension models,
* and provide evidence for or against particular parameter choices.

These experiments do not solve the protein folding problem. They can only falsify specific TU encodings related to Q063, identified by their keys.

### Experiment 1: Folding benchmark tension profiling

**Goal**

Evaluate whether the proposed `Tension_fold` functional aligns with known differences between well behaved fast folders and frustrated or marginal sequences.

**Setup**

* Select a benchmark set of proteins with well characterized folding behavior, for example:

  * small two state fast folders,
  * multi state folders with intermediates,
  * proteins prone to misfolding or aggregation.
* For each protein and a chosen environment:

  * collect existing experimental and simulation summaries (for example folding rates, stability, misfolding propensity, landscape analyses),
  * construct effective states `m_data` in `M_reg` that encode these summaries at comparable resolution using an external procedure.

**Encoding choices**

* Fix once and for all, for this experiment:

  * the encoding key combination

    ```txt
    EncodingKey:   Q063_FOLDING_CORE_V1
    LibraryKey:    Q063_FOLDING_LIB_V1
    WeightKey:     Q063_FOLDING_WEIGHTS_V1
    RefinementKey: Q063_FOLDING_REFINE_V1
    ```

  * the reference funnel profiles used to define `DeltaS_funnel`,

  * the structural targets used to define `DeltaS_seq_struct`,

  * the coefficients `a1` and `a2` used in `Tension_fold`.

* These choices are made **before** inspecting any benchmark results. They remain fixed for all proteins in this experiment. If any of them are changed based on the data, the resulting analysis is considered to use a different encoding and must be labeled with new keys.

**Protocol**

1. For each protein in the benchmark set, map its data into a state `m_data` in `M_reg` using a consistent external mapping. Proteins for which this mapping fails, or results in a state in `S_sing`, are recorded as out of domain and are excluded from tension statistics.
2. For each `m_data`, compute:

   * `Gap_native(m_data)`,
   * `Funnel_sharpness(m_data)`,
   * `Misfold_fraction(m_data)`,
   * `Tension_fold(m_data)`.
3. Group the proteins into categories, for example:

   * fast two state,
   * multi state with intermediates,
   * aggregation prone or misfolding prone.
4. Compare the distributions of `Tension_fold(m_data)` across these categories.

**Metrics**

* Within group distribution of `Tension_fold`.
* Separation between group means or medians.
* Rank correlation between `Tension_fold` and external indicators such as:

  * folding rate,
  * stability margin,
  * misfolding propensity.

**Falsification conditions**

* For the fixed encoding key combination, if proteins independently identified as fast, robust two state folders consistently exhibit higher `Tension_fold` than proteins known to be frustrated or prone to misfolding, then the encoding is considered misaligned and rejected at the effective layer.
* If minor changes in refinement parameters within the same key combination produce arbitrary reversals in the ranking of `Tension_fold` across protein categories, the encoding is considered unstable and rejected.

**Semantics implementation note**

This experiment uses encodings where conformational spaces are treated as continuous energy landscapes, while sequence and environment labels are discrete. The effective states `m_data` respect this combination and are consistent with `Semantics: hybrid` in the metadata.

**Boundary note**

Falsifying a Q063 encoding does not solve the protein folding problem. This experiment can reject specific tension encodings for folding but cannot by itself provide a full physical solution.

---

### Experiment 2: Designed perturbations of folding tension

**Goal**

Test whether changes to sequences predicted to modify `Tension_fold` correspond to measurable changes in folding robustness and misfolding behavior.

**Setup**

* Choose a small, fast folding single domain protein with well known structure and kinetics.
* Design a set of sequence variants grouped into:

  * variants predicted to **decrease** `Tension_fold` (for example by increasing `Gap_native` and `Funnel_sharpness`),
  * variants predicted to **increase** `Tension_fold` (for example by introducing frustration or new misfold basins).
* For each variant, use external methods to estimate:

  * stability (for example unfolding free energy),
  * folding and unfolding rates,
  * misfolding and aggregation tendencies.

**Encoding choices**

* Use the same encoding key combination as in Experiment 1:

  ```txt
  EncodingKey:   Q063_FOLDING_CORE_V1
  LibraryKey:    Q063_FOLDING_LIB_V1
  WeightKey:     Q063_FOLDING_WEIGHTS_V1
  RefinementKey: Q063_FOLDING_REFINE_V1
  ```

* No retuning of funnel profiles, structural targets, or weights is allowed based on the variant results. Any such retuning would produce a different encoding that must be treated separately.

**Protocol**

1. For each sequence variant and environment, construct a state `m_var` in `M_reg` encoding the estimated landscape characteristics. Variants that cannot be mapped into `M_reg` are recorded as out of domain.
2. Compute `Tension_fold(m_var)` using the same profiles, targets, and coefficients as in Experiment 1.
3. Measure empirical changes in:

   * folding rates,
   * stability margins,
   * misfolding or aggregation rates.
4. Compare the direction and rough magnitude of changes in `Tension_fold(m_var)` with the empirical changes.

**Metrics**

* Sign agreement between predicted changes in `Tension_fold` and observed changes in folding robustness, for example:

  * reduced tension associated with faster folding, higher stability, lower misfolding,
  * increased tension associated with the opposite.
* Correlation between relative changes in `Tension_fold` and relative changes in misfolding propensity across variants.

**Falsification conditions**

* If variants designed to reduce `Tension_fold` systematically show worse folding behavior (for example slower folding, lower stability, higher misfolding) than the wild type and variants designed to increase `Tension_fold`, then the encoding is considered reversed and rejected at the effective layer.
* If no consistent relationship can be established between `Tension_fold` changes and empirical folding changes across a sufficiently rich set of variants, the encoding is considered ineffective for Q063.

**Semantics implementation note**

The designed variants and their properties are encoded using the same type of effective states and observables as in Experiment 1. No additional semantic layers are introduced.

**Boundary note**

Falsifying a Q063 encoding does not solve the protein folding problem. Success or failure in this experiment only tests the quality of the tension encoding under a specified key combination, not the existence of a full physical solution.

---

## 7. AI and WFGY engineering spec

This block describes how Q063 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

All modules described here **only read and write effective layer objects** such as observables, invariants, and tension values. They do not access or reveal any TU deep generative rules.

### 7.1 Training signals

We define several training signals that can be used in AI models to encourage folding aware and tension aware reasoning.

1. `signal_folding_energy_gap`

   * Definition: a signal proportional to `Gap_native(m)` for states representing protein sequences in specified environments.
   * Purpose: reward internal representations and outputs that respect plausible energy gaps between native and competing basins when such gaps are supported by external data.

2. `signal_funnelness`

   * Definition: a signal based on `Funnel_sharpness(m)`, penalizing internal states that imply highly frustrated, non funnel like landscapes when the context assumes efficient biological folding.
   * Purpose: guide the model toward explanations and predictions that align with funnel based views where appropriate.

3. `signal_misfold_tension`

   * Definition: a signal derived from `Misfold_fraction(m)` and `K_sep(m)`, penalizing states that imply high misfold occupancy or long escape times when biological evidence points to robust folding.
   * Purpose: steer reasoning away from scenarios that contradict known robustness for specific proteins and conditions.

4. `signal_counterfactual_folding_consistency`

   * Definition: a signal measuring how clearly the model separates reasoning under World T assumptions from reasoning under World F assumptions when prompted to consider each explicitly.
   * Purpose: encourage explicit handling of assumptions about folding theory completeness rather than mixing them.

These signals are defined relative to a specific encoding key combination. If the encoding changes, the mapping from internal states to these signals must be reconsidered.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q063 structures without revealing any deep TU generative rules.

1. `FoldingTensionHead`

   * Role: a module that, given an internal representation of a protein related context (sequence, environment, structural constraints), produces estimates of:

     * `Gap_native`,
     * `Funnel_sharpness`,
     * `Misfold_fraction`,
     * `Tension_fold`.
   * Interface:

     * Inputs: embeddings representing `seq`, `env`, and contextual task information.
     * Outputs: a small vector of predicted invariants and a scalar tension estimate.

2. `SequenceToStructureConsistencyFilter`

   * Role: a module that evaluates whether the model's proposed structures or structure related statements for a given sequence are consistent with low folding tension expectations when such expectations are explicitly assumed.
   * Interface:

     * Inputs: sequence representation, proposed structure representation, and optional environment descriptor.
     * Outputs: a consistency score or mask indicating how compatible the proposal is with low `Tension_fold`.

3. `EnergyLandscapeObserver`

   * Role: a generalized observer that compresses high dimensional internal representations into a small set of landscape descriptors similar to the `FoldingEnergyLandscapeDescriptor`.
   * Interface:

     * Inputs: internal activations from an AI model when reasoning about folding or related thermodynamic systems.
     * Outputs: features corresponding to energy gap, funnelness, roughness, and degeneracy.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models augmented with the Q063 modules.

1. Task selection

   * Choose a benchmark including:

     * questions about protein stability and folding under mutations,
     * tasks that require reasoning about misfolding and aggregation,
     * explanations of how sequence changes affect folding routes.

2. Conditions

   * Baseline condition:

     * the model operates without explicit FoldingTensionHead, SequenceToStructureConsistencyFilter, or EnergyLandscapeObserver modules,
     * only general language or structural knowledge is used.
   * TU condition:

     * the same model, or a closely related one, uses these modules and their signals as auxiliary guidance during training or inference when the task explicitly involves folding behavior.

3. Metrics

   * Accuracy on folding related prediction tasks, such as which mutation stabilizes or destabilizes a protein.
   * Internal consistency across related questions, for example predicted structures, stability, and misfolding must be mutually compatible.
   * Robustness of reasoning under rephrasings or perturbations of prompts.

### 7.4 60 second reproduction protocol

A minimal protocol to let external users experience the impact of the Q063 encoding in an AI system.

**Baseline setup**

* Prompt: ask the AI to explain how protein sequence, energy landscape, and folding kinetics are related, and to comment on why some proteins misfold and aggregate.
* Observation: record whether the explanation is diffuse, whether the landscape notion is vague, and whether misfolding is treated as an add on rather than as part of a structured landscape.

**TU encoded setup**

* Prompt: ask the same question, but add instructions for the AI to:

  * describe folding in terms of energy gap, funnel sharpness, misfold fraction, and folding tension,
  * treat these as explicit invariants when structuring the explanation.
* Observation: record whether the explanation:

  * uses the invariants coherently,
  * clearly distinguishes robust folding from marginal or frustrated cases,
  * connects sequence features to changes in the invariants.

**Comparison metric**

* Use a simple rubric to rate:

  * structural clarity of the explanation,
  * explicitness of the links between sequence, landscape, and function,
  * internal consistency in handling misfolding.

**What to log**

* The prompts and responses for both setups.
* Any auxiliary outputs from FoldingTensionHead, SequenceToStructureConsistencyFilter, or EnergyLandscapeObserver modules.
* This allows later inspection of how folding tension concepts were used, without exposing any internal TU generative mechanisms.

This protocol measures how the Q063 encoding changes the **structure of reasoning** in an AI system. It does not provide direct evidence that the canonical protein folding problem has been solved.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q063 and how they transfer to other problems.

All components are defined relative to a specific encoding key combination. If the encoding changes, the precise numerical values they produce may also change, even if the conceptual roles remain similar.

### 8.1 Reusable components produced by this problem

1. ComponentName: `FoldingEnergyLandscapeDescriptor`

   * Type: `field`
   * Minimal interface:

     * Inputs: effective summaries of conformational basins and transitions for a given sequence and environment.
     * Outputs: a vector of features including:

       * `Gap_native`,
       * `Funnel_sharpness`,
       * `R_rough`,
       * `Misfold_fraction`,
       * `K_sep`.
   * Preconditions:

     * input states must be in `M_reg`,
     * basins and transitions must be identified at a resolution sufficient to estimate the listed features.

2. ComponentName: `MisfoldDegeneracyIndex`

   * Type: `observable`
   * Minimal interface:

     * Inputs: a decomposition of `P_misfold` into contributions from individual misfold basins.
     * Output: a scalar index summarizing how many misfold basins contribute substantially to the total misfold occupancy. For example this can be based on an entropy like expression or a threshold based count.
   * Preconditions:

     * misfold basins must be separately identifiable in the encoding,
     * the decomposition must be stable under modest changes in coarse graining.

3. ComponentName: `CounterfactualFoldingWorld_Template`

   * Type: `experiment_pattern`
   * Minimal interface:

     * Inputs: a model class for folding landscapes, for example a family of coarse grained models or a class of AI generated landscapes, and a set of sequences.
     * Output: a pair of experiment definitions representing:

       * a World T type regime, compact folding theory with low tension,
       * a World F type regime, no compact theory with persistent high tension,
         with associated procedures for evaluating `Tension_fold`.
   * Preconditions:

     * the model class must support generation or estimation of the observables required for Q063 invariants,
     * the sequences must be such that experimental or high quality simulation data can be obtained or approximated.

### 8.2 Direct reuse targets

1. Q064 (BH_CHEM_GLASS_TRANS_L3_064)

   * Reused component: `FoldingEnergyLandscapeDescriptor`.
   * Why it transfers: both folding and glass transition involve rugged energy landscapes with many basins and barriers. The descriptor generalizes to non biopolymer systems by interpreting basins and transitions in terms of configurational states of the glass.
   * What changes: conformational basins and native states are replaced by local minima and macroscopic glassy states. `Gap_native` and `Misfold_fraction` are reinterpreted accordingly.

2. Q070 (BH_CHEM_SOFTMATTER_L3_070)

   * Reused component: `CounterfactualFoldingWorld_Template`.
   * Why it transfers: self assembly in soft matter exhibits funnel versus frustration behavior similar to folding. World T and World F scenarios can be used to test whether a compact effective theory exists for particular soft matter systems.
   * What changes: sequences are replaced by building block types or interaction patterns. Native states are replaced by desired assembled structures.

3. Q071 (BH_BIO_ORIGIN_LIFE_L3_071)

   * Reused component: `MisfoldDegeneracyIndex`.
   * Why it transfers: early life scenarios require enough sequences with low misfold degeneracy to support stable functional structures. The index provides a quantitative measure of this requirement.
   * What changes: the distribution of sequences and environments is shifted to prebiotic regimes. The threshold for acceptable misfold degeneracy may differ from modern biology.

4. Q123 (BH_AI_INTERP_L3_123)

   * Reused component: `EnergyLandscapeObserver` derived from Q063.
   * Why it transfers: AI representation spaces often behave like energy landscapes. An observer that extracts gap, funnelness, roughness, and degeneracy features is useful for interpretability.
   * What changes: basins and transitions are interpreted in terms of representation patterns and optimization trajectories rather than physical conformations and dynamics.

All such transfers remain at the effective layer. They do not imply that the underlying physical or algorithmic mechanisms are identical across domains.

---

## 9. TU roadmap and verification levels

This block explains how Q063 is positioned along the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of protein folding has been specified in terms of:

    * state space `M`,
    * observables and invariants,
    * a folding tension functional `Tension_fold`,
    * an admissible encoding class tied to specific keys,
    * and a singular set with domain restriction.
  * Discriminating experiments have been outlined with clear falsification conditions for specific encodings.

* N_level: N1

  * The narrative linking sequence, energy landscape, folding behavior, and tension is explicit and internally coherent at the effective layer.
  * Counterfactual worlds have been defined in terms of observable patterns and tension regimes.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented in practice for a fixed encoding key combination.

1. A working prototype that, for a curated set of proteins, constructs states `m_data` in `M_reg` from published data and computes:

   * `Gap_native`,
   * `Funnel_sharpness`,
   * `Misfold_fraction`,
   * `K_sep`,
   * `Tension_fold`,
     and publishes the resulting tension profiles alongside the source data and keys used.
2. A set of designed mutation experiments or high resolution simulations where predicted changes in `Tension_fold` are compared systematically with observed changes in folding robustness and misfolding propensity, following Experiment 2.

Both steps operate entirely on observables and do not require exposing any deep TU generative rule.

### 9.3 Path toward higher narrative levels

To progress from N1 to N2 and beyond, the following will be needed.

* A refined set of folding landscape archetypes, grounded in data, that can be described using a small number of invariants and used consistently across multiple proteins.
* Demonstrations that Q063 components such as `FoldingEnergyLandscapeDescriptor` and `MisfoldDegeneracyIndex` can transfer to other BlackHole problems such as Q064, Q070, and Q071 without major redesign.

In the long run, Q063 is expected to serve as:

* the reference node for thermodynamic_tension problems in biophysical chemistry,
* a testbed for how far TU style encodings can go in structuring reasoning about complex many body systems,
* a bridge between microscopic physics, biological function, and AI representations through the shared language of rugged landscapes and tension.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non experts, while still aligned with the effective layer description.

Proteins are chains of amino acids that fold into specific three dimensional shapes. Those shapes matter because they determine what the protein can do in a cell.

The classical protein folding problem asks:

* if you know the sequence of amino acids and the environment,
* can you predict what shape the protein will take,
* how fast it will fold,
* and how likely it is to misfold or form harmful clumps,

using a small set of physical principles that work for many different proteins.

In the Tension Universe view, we do not try to write down all the atomic details. Instead, we imagine a space of states. Each state summarizes, for one sequence and one environment:

* the important valleys, or basins, in the energy landscape,
* how deep they are,
* how easy it is to move between them,
* and how likely the protein is to sit in each basin.

From each state, we extract a few key numbers:

* how much lower the native basin is than its main competitors, the energy gap,
* how strongly the landscape guides the chain toward the native basin, the funnel sharpness,
* how much probability sits in misfolded basins,
* how the timescale to fold compares with the timescale to escape misfolds.

We then combine some of these into a single quantity called folding tension. Roughly:

* low folding tension means the landscape looks like a clean funnel into the native state, with a good gap and limited misfolding,
* high folding tension means the landscape is messy, with many competing basins and unclear guidance toward the native state.

We consider two kinds of effective worlds.

* In a compact theory world, most natural proteins live in states where folding tension can be kept low, and a small set of rules explains how sequence and environment shape the landscape.
* In a no compact theory world, many proteins live in states with high folding tension, and no small set of rules can explain the variety of landscapes and behaviors.

This does not solve protein folding. It does not claim we already have the rules. Instead, it gives:

* a precise way to talk about how hard the folding problem is,
* a set of observable quantities to focus on,
* and experiments to test whether a particular way of encoding folding is reasonable under fixed keys.

Q063 is therefore the node in the Tension Universe that says:

* if there is a simple, deep explanation of protein folding, this is how its effects would look at the level of energy gaps, funnels, misfolding, and tension,
* if there is not, this is how that failure would show up in the same language.

That makes Q063 a central test of whether biological complexity in proteins can be reduced to a finite set of physically grounded principles at the effective layer, or whether significant residual tension remains even after careful modeling.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S problem collection.

### Scope of claims

* The goal of this document is to specify an **effective layer encoding** of the named problem.
* It does not claim to solve the canonical scientific problem described in Section 1.
* It does not introduce any new theorem or physical law beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved, or that a full physical theory of protein folding has been completed.

### Effective-layer boundary

* All objects used here, including the state space `M`, the regular domain `M_reg`, the singular set `S_sing`, and all observables, invariants, and tension functionals, live at the **effective layer** of the Tension Universe.
* No mapping is defined from raw experimental or simulation data to internal TU fields. Any such mapping, if implemented, is an external choice and is not part of this document.
* No TU axioms, deep generative rules, or construction procedures are exposed or assumed.

### Encoding and fairness

* The Q063 encoding described in this page is identified by the metadata keys:

  ```txt
  EncodingKey:   Q063_FOLDING_CORE_V1
  LibraryKey:    Q063_FOLDING_LIB_V1
  WeightKey:     Q063_FOLDING_WEIGHTS_V1
  RefinementKey: Q063_FOLDING_REFINE_V1
  ```

* All definitions of `DeltaS_funnel`, `DeltaS_seq_struct`, `Tension_fold`, and related invariants are tied to these keys and to the associated admissible libraries and weights.

* Fairness constraints require that reference profiles, structural targets, and weights be chosen before evaluating particular datasets and not retuned afterward to hide high tension. Any material change to these choices defines a new encoding that must be labeled with new keys.

* Experiments and falsification statements in this page apply only to specific encodings identified by their keys. They do not claim to falsify the canonical scientific problem itself.

### Relation to the TU program

* Q063 is an S rank node in the BlackHole problem graph, representing the protein folding problem at the effective layer.
* It connects biophysical chemistry to other domains such as glassy physics, origin of life, and AI interpretability through shared language about rugged landscapes and tension.
* Its main purpose in the TU program is to provide a structured, falsifiable, and transferable encoding of folding tension that can be used in empirical studies and AI systems without claiming to resolve the underlying science.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
