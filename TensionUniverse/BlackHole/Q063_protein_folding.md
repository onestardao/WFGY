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
Last_updated: 2026-01-25
````

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The classical protein folding problem can be stated as follows:

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

This problem lies at the intersection of chemistry, physics, and biology, and is central to understanding how sequence level information translates into functional three dimensional structures in living systems.

### 1.2 Status and difficulty

Important partial resolutions include:

* The energy landscape and folding funnel picture, which explains how rapid and reproducible folding can emerge from high dimensional rugged energy landscapes.
* Detailed experimental and computational studies for specific small proteins, where folding pathways, intermediates, and rates are known at high resolution.
* Physics based and machine learning based structure predictors (for example methods that can reliably predict many protein structures from sequence alone) that address the structure prediction aspect for many cases.

However:

* There is no single, compact, physically grounded theory that:

  * predicts folding pathways, rates, and misfolding behavior for arbitrary sequences and environments, and
  * is widely accepted as complete in the sense defined above.

* Many proteins are marginally stable, exhibit complex multi state folding, or are coupled to chaperones and cellular machinery, which complicates any attempt at a universal theory.

* Strongly correlated effects, solvent interactions, and collective motions make it difficult to derive simple rules directly from microscopic physics.

The problem is therefore considered extremely difficult. Current approaches provide powerful tools and partial solutions, but not a complete, unified, finite principle theory in the sense required here.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q063 plays several roles:

1. It is the flagship thermodynamic_tension problem for biophysical chemistry, where:

   * high dimensional microscopic interactions,
   * low dimensional effective descriptors,
   * and biological constraints

   must be reconciled.

2. It provides a concrete setting to test whether:

   * rugged energy landscapes,
   * folding funnels,
   * and misfolding phenomena

   can be described by a small number of effective invariants and libraries, or whether irreducible residual tension remains.

3. It anchors cross domain connections between:

   * chemistry and soft matter physics (rugged landscapes and glass like behavior),
   * biology (sequence to function mapping and evolution),
   * and AI (energy landscape metaphors for representation and optimization).

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
  Reason: Origin of life scenarios depend on foldable polymers, and require the existence of low tension folding landscapes as building blocks.

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
  Reason: Both involve many body interactions on rugged landscapes, though Q077 focuses on ecosystem level fitness landscapes.

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

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden generative rules or any mapping from raw data to internal TU fields.

### 3.1 State space

We assume an effective state space:

```txt
M
```

with the following interpretation:

* Each element `m` in `M` represents a coherent "folding configuration" for:

  * a fixed amino acid sequence `seq`,
  * a fixed environment `env` (for example temperature, solvent, ionic strength),

  including only coarse grained summaries, not microscopic details.

For each `m` in `M`, the encoding contains:

* A set of conformational basins (for example native basin and misfold basins) with associated free energies.
* Effective transition rates or barriers between the main basins.
* Occupation probabilities or weights for each basin at the chosen environmental conditions.

We do not specify how `m` is constructed from atomistic simulations or experiments. We only assume:

* For any realistic sequence and environment, there exist states `m` that summarize folding relevant information at some resolution.
* There is a regular subset `M_reg` of `M` where all observables defined below are well defined and finite.

### 3.2 Effective fields and observables

On `M`, we introduce the following effective observables.

1. Native basin free energy

```txt
E_native(m)
```

* A real valued observable giving the effective free energy of the native basin for the sequence and environment encoded in `m`.

2. Competing basin free energy

```txt
E_competing(m)
```

* A real valued observable summarizing the free energy of the most relevant competing misfolded basins (for example the lowest misfold free energy, or an effective average over several).

3. Native occupancy

```txt
P_native(m)
```

* A number in the interval `[0, 1]` giving the probability weight of the native basin in the ensemble represented by `m` under the chosen conditions.

4. Misfold occupancy

```txt
P_misfold(m)
```

* A number in the interval `[0, 1]` giving the total probability weight assigned to misfolded basins in `m`.

5. Landscape roughness index

```txt
R_rough(m)
```

* A nonnegative scalar summarizing the roughness of the energy landscape, for example based on the distribution of barrier heights and basin depths.

6. Folding timescale

```txt
tau_fold(m)
```

* A positive scalar summarizing the effective timescale for folding from an unfolded ensemble to the native basin under the conditions encoded in `m`.

7. Misfold escape timescale

```txt
tau_misfold(m)
```

* A positive scalar summarizing the effective timescale for escape from typical misfolded basins into the native basin or other basins.

All of these observables take values in suitable subsets of real space, consistent with the parameter space Par used in the general TU core.

### 3.3 Invariants and effective constraints

From the observables above, we define several effective invariants.

1. Native energy gap

```txt
Gap_native(m) = E_competing(m) - E_native(m)
```

* A real valued quantity representing the energy separating the native basin from its main competitors.

2. Funnel sharpness index

```txt
Funnel_sharpness(m)
```

* A dimensionless, nonnegative scalar that captures how strongly the landscape is biased toward the native basin as a function of some reaction coordinate.
* Higher values correspond to a clearer funnel into the native state; lower values correspond to more frustrated or flat landscapes.

3. Misfold fraction

```txt
Misfold_fraction(m) = P_misfold(m)
```

* A scalar in `[0, 1]` measuring how much of the ensemble weight resides in misfolded basins.

4. Kinetic separation ratio

```txt
K_sep(m) = tau_misfold(m) / tau_fold(m)
```

* A dimensionless ratio comparing the timescale for escaping misfolds to the timescale for folding, when both are defined.

These invariants are required to be stable under moderate changes in coarse graining of the landscape for states in `M_reg`.

### 3.4 Singular set and domain restrictions

Some observables may be undefined or not finite, for example:

* when the effective description has not converged,
* when basin identification is ambiguous,
* or when folding behavior cannot be summarized by a small number of basins.

We define the singular set:

```txt
S_sing = { m in M :
           E_native(m), E_competing(m),
           P_native(m), P_misfold(m),
           R_rough(m), tau_fold(m), tau_misfold(m)
           are not all well defined and finite }
```

Domain restriction:

* All folding tension analysis is restricted to

  ```txt
  M_reg = M \ S_sing
  ```

* For `m` in `S_sing`, invariants such as `Gap_native`, `Funnel_sharpness`, `Misfold_fraction`, and `K_sep` are treated as "out of domain" rather than as extreme values.

* Experiments and protocols in this document are required to specify that they operate only on states in `M_reg`.

This choice emphasizes domain restriction as the primary treatment of singular behavior. When needed, additional regularization procedures may be used in practical implementations, but these are not part of the TU effective layer definition.

---

## 4. Tension principle for this problem

This block states how Q063 is characterized as a tension problem within the Tension Universe at the effective layer.

### 4.1 Core tension functional

We first define two mismatch measures.

1. Funnel mismatch

```txt
DeltaS_funnel(m)
```

* A nonnegative scalar measuring how far the landscape encoded in `m` deviates from a reference "ideal funnel" profile for the same sequence length and environment class.
* `DeltaS_funnel(m) = 0` if the encoded landscape perfectly matches the chosen reference funnel profile.
* `DeltaS_funnel(m)` increases when the energy gap is small, the funnel is flat, or roughness is high relative to the ideal profile.

2. Sequence structure mismatch

```txt
DeltaS_seq_struct(m)
```

* A nonnegative scalar measuring how far the encoded structure ensemble in `m` deviates from a target set of structures determined by sequence and environment.
* `DeltaS_seq_struct(m) = 0` if the native ensemble matches the target set according to the chosen structural similarity metric and tolerance.

We then define a folding tension functional:

```txt
Tension_fold(m) = a1 * DeltaS_funnel(m) + a2 * DeltaS_seq_struct(m)
```

where:

* `a1 > 0` and `a2 > 0` are fixed coefficients chosen once for the encoding class and not adjusted per sequence.
* `Tension_fold(m) >= 0` for all `m` in `M_reg`.

Fairness constraints:

* The reference funnel profiles and structural targets used to define `DeltaS_funnel` and `DeltaS_seq_struct` must be specified in a way that does not depend on the detailed data of the particular state `m` being evaluated.
* Given a sequence length range and environment class, the reference profiles are fixed before any evaluation and cannot be tuned post hoc to reduce tension for specific cases.

These constraints prevent trivial tension minimization by adjusting reference profiles or weights after seeing the data.

### 4.2 Folding as a low tension principle

At the effective layer, the existence of a "full physical solution" for protein folding can be reframed as:

> For biologically relevant sequences and environments, there exist regular states in `M_reg` whose folding tension `Tension_fold` can be kept within a narrow low band across scales and resolutions, using a finite library of effective rules.

More concretely, for any admissible encoding of:

* the landscape in terms of basins and transitions,
* the structural targets for native ensembles,
* the environment class,

there should exist world representing states `m_true` such that:

```txt
Tension_fold(m_true) <= epsilon_fold
```

where:

* `epsilon_fold` is a small threshold depending on measurement precision and modeling granularity,
* `epsilon_fold` does not grow without bound as the resolution of the encoding and the quality of data improve.

In such a world, the apparent complexity of folding landscapes can be compressed into a small set of effective invariants and rules, and the residual thermodynamic_tension between microscopic physics, sequence information, and folding outcomes is low.

### 4.3 Failure as persistent high tension

If no such finite principle description exists, then for any admissible encoding satisfying the constraints above, world representing states would eventually exhibit persistent high tension:

```txt
Tension_fold(m_false) >= delta_fold
```

for some strictly positive `delta_fold` that:

* cannot be driven arbitrarily close to zero by refining encodings or improving data,
* persists across large classes of sequences and environments, not just pathological cases.

In this case, folding would remain fundamentally resistant to compression into a finite library of effective rules, and thermodynamic_tension between microscopic physics, sequence, and structure would remain irreducible.

In summary, Q063, at the effective layer, asks whether the universe of biologically relevant protein folding lies in a low tension regime governed by a finite set of rules, or in a regime where significant residual tension remains even after careful modeling.

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

   * Despite microscopic richness, the diversity of landscapes across proteins can be described using a modest number of landscape archetypes, each associated with specific parameter ranges of the invariants.

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
   * Attempts to classify landscapes into a finite set of types for predictive purposes fail or require frequent ad hoc exceptions.

3. Misfolding unpredictability

   * `Misfold_fraction(m_F)` and `K_sep(m_F)` exhibit patterns that cannot be reliably predicted from sequence and environment by any finite library of rules.
   * Even within narrow families of sequences, folding and misfolding behaviors remain idiosyncratic.

4. No stable low tension band

   * There is no robust low tension band common to most natural proteins; instead, tension levels are spread broadly and sensitive to small changes in sequence or conditions.

In such a world, the thermodynamic_tension between microscopic complexity and macroscopic folding behavior remains intrinsically high.

### 5.3 Interpretive note

These counterfactual worlds do not construct TU internal fields from raw data. They only assert that:

* if there exist states `m` that faithfully represent either a compact theory world or a non compact world,
* then the observable patterns of folding invariants and the behavior of `Tension_fold` would differ qualitatively as described above.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q063 encoding,
* distinguish between different folding tension models,
* and provide evidence for or against particular parameter choices.

These experiments do not solve the protein folding problem. They can only falsify specific TU encodings related to Q063.

### Experiment 1: Folding benchmark tension profiling

*Goal:*

Evaluate whether the proposed `Tension_fold` functional aligns with known differences between well behaved fast folders and frustrated or marginal sequences.

*Setup:*

* Select a benchmark set of proteins with well characterized folding behavior, for example:

  * small two state fast folders,
  * multi state folders with intermediates,
  * proteins prone to misfolding or aggregation.

* For each protein and a chosen environment:

  * collect existing experimental and simulation summaries (for example folding rates, stability, misfolding propensity, landscape analyses),
  * construct effective states `m_data` in `M_reg` that encode these summaries at comparable resolution.

* Fix once and for all, for this experiment:

  * the reference funnel profiles used to define `DeltaS_funnel`,
  * the structural targets used to define `DeltaS_seq_struct`,
  * the coefficients `a1` and `a2` used in `Tension_fold`.

*Protocol:*

1. For each protein in the benchmark set, map its data into a state `m_data` in `M_reg` using any consistent external procedure.

2. For each `m_data`, compute:

   * `Gap_native(m_data)`,
   * `Funnel_sharpness(m_data)`,
   * `Misfold_fraction(m_data)`,
   * `Tension_fold(m_data)`.

3. Group the proteins into categories (for example fast two state, multi state, aggregation prone) based on independent biological knowledge.

4. Compare the distributions of `Tension_fold(m_data)` across these categories.

*Metrics:*

* Within group distribution of `Tension_fold`.
* Separation between group means or medians.
* Rank correlation between `Tension_fold` and external indicators such as:

  * folding rate,
  * stability margin,
  * misfolding propensity.

*Falsification conditions:*

* If, under fixed reference profiles and coefficients:

  * proteins independently identified as fast, robust two state folders consistently exhibit higher `Tension_fold` than proteins known to be frustrated or prone to misfolding,
    then the encoding is considered misaligned and rejected at the effective layer.

* If minor changes in the encoding parameters (within a predefined admissible range) cause arbitrary reversals in the ranking of `Tension_fold` across protein categories, the encoding is considered unstable and rejected.

*Semantics implementation note:*

This experiment uses encodings where conformational spaces are treated as continuous energy landscapes, while sequence and environment labels are discrete. The effective states `m_data` respect this combination and are consistent with the hybrid treatment recorded in the metadata.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. This experiment can reject specific tension encodings for folding, but it does not provide a full physical solution of protein folding.

---

### Experiment 2: Designed perturbations of folding tension

*Goal:*

Test whether changes to sequences predicted to modify `Tension_fold` correspond to measurable changes in folding robustness and misfolding behavior.

*Setup:*

* Choose a small, fast folding single domain protein with well known structure and kinetics.

* Design a set of sequence variants grouped into:

  * variants predicted to decrease `Tension_fold` (for example by increasing `Gap_native` and `Funnel_sharpness`),
  * variants predicted to increase `Tension_fold` (for example by introducing frustration or new misfold basins).

* For each variant, use external methods to estimate:

  * stability (for example unfolding free energy),
  * folding and unfolding rates,
  * misfolding and aggregation tendencies.

*Protocol:*

1. For each sequence variant and environment, construct a state `m_var` in `M_reg` encoding the estimated landscape characteristics.

2. Compute `Tension_fold(m_var)` using the same reference profiles and coefficients as in Experiment 1.

3. Measure empirical changes in:

   * folding rates,
   * stability margins,
   * misfolding or aggregation rates.

4. Compare the direction and rough magnitude of changes in `Tension_fold(m_var)` with the empirical changes.

*Metrics:*

* Sign agreement between predicted changes in `Tension_fold` and observed changes in folding robustness (for example faster folding, higher stability, lower misfolding).
* Correlation between relative changes in `Tension_fold` and relative changes in misfolding propensity across variants.

*Falsification conditions:*

* If variants designed to reduce `Tension_fold` systematically show worse folding behavior (for example slower folding, lower stability, higher misfolding) than the wild type and variants designed to increase `Tension_fold`, then the encoding is considered reversed and rejected.
* If no consistent relationship can be established between `Tension_fold` changes and empirical folding changes across a sufficiently rich set of variants, the encoding is considered ineffective for Q063.

*Semantics implementation note:*

The designed variants and their properties are encoded using the same type of effective states and observables as in Experiment 1. No additional semantic layers are introduced.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. Success or failure in this experiment only tests the quality of the tension encoding, not the existence of a full physical solution of protein folding.

---

## 7. AI and WFGY engineering spec

This block describes how Q063 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

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

### 7.2 Architectural patterns

We outline module patterns that can reuse Q063 structures without revealing any deep TU generative rules.

1. `FoldingTensionHead`

   * Role: a module that, given an internal representation of a protein related context (sequence, environment, structural constraints), produces estimates of:

     * `Gap_native`,
     * `Funnel_sharpness`,
     * `Misfold_fraction`,
     * `Tension_fold`.

   * Interface:

     * Inputs: embeddings representing `seq`, `env`, and any contextual task information.
     * Outputs: a small vector of predicted invariants and a scalar tension estimate.

2. `SequenceToStructureConsistencyFilter`

   * Role: a module that evaluates whether the model's proposed structures or structure related statements for a given sequence are consistent with low folding tension expectations when such expectations are explicitly assumed.
   * Interface:

     * Inputs: sequence representation, proposed structure representation, and optional environment descriptor.
     * Outputs: a consistency score or mask indicating how compatible the proposal is with low `Tension_fold`.

3. `EnergyLandscapeObserver`

   * Role: a generalized observer that compresses high dimensional internal representations into a small set of landscape descriptors similar to `FoldingEnergyLandscapeDescriptor`.
   * Interface:

     * Inputs: internal activations from an AI model when reasoning about folding or related thermodynamic systems.
     * Outputs: features corresponding to energy gap, funnelness, roughness, and misfold degeneracy.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models augmented with the Q063 modules.

1. Task selection

   * Choose a benchmark including:

     * questions about protein stability and folding under mutations,
     * tasks that require reasoning about misfolding and aggregation,
     * explanations of how sequence changes affect folding routes.

2. Conditions

   * Baseline condition:

     * The model operates without explicit FoldingTensionHead, SequenceToStructureConsistencyFilter, or EnergyLandscapeObserver modules.
     * Only general language or structural knowledge is used.

   * TU condition:

     * The same model, or a closely related one, uses these modules and their signals as auxiliary guidance during training or inference when the task explicitly involves folding behavior.

3. Metrics

   * Accuracy on folding related prediction tasks (for example which mutation stabilizes or destabilizes a protein).
   * Internal consistency across related questions (for example predicted structures, stability, and misfolding must be mutually compatible).
   * Robustness of reasoning under rephrasings or perturbations of prompts.

### 7.4 60 second reproduction protocol

A minimal protocol to let external users experience the impact of the Q063 encoding in an AI system.

*Baseline setup*

* Prompt: ask the AI to explain how protein sequence, energy landscape, and folding kinetics are related, and to comment on why some proteins misfold and aggregate.
* Observation: record whether the explanation is diffuse, whether the landscape notion is vague, and whether misfolding is treated as an add on rather than as part of a structured landscape.

*TU encoded setup*

* Prompt: ask the same question, but add instructions for the AI to:

  * describe folding in terms of energy gap, funnel sharpness, misfold fraction, and folding tension,
  * treat these as explicit invariants when structuring the explanation.

* Observation: record whether the explanation:

  * uses the invariants coherently,
  * clearly distinguishes robust folding from marginal or frustrated cases,
  * connects sequence features to changes in the invariants.

*Comparison metric*

* Use a simple rubric to rate:

  * structural clarity of the explanation,
  * explicitness of the links between sequence, landscape, and function,
  * internal consistency in handling misfolding.

*What to log*

* The prompts and responses for both setups.
* Any auxiliary outputs from FoldingTensionHead, SequenceToStructureConsistencyFilter, or EnergyLandscapeObserver modules.
* This allows later inspection of how folding tension concepts were used, without exposing any internal TU generative mechanisms.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q063 and how they transfer to other problems.

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

     * Input states must be in `M_reg`.
     * Basins and transitions must be identified at a resolution sufficient to estimate the listed features.

2. ComponentName: `MisfoldDegeneracyIndex`

   * Type: `observable`

   * Minimal interface:

     * Inputs: a decomposition of `P_misfold` into contributions from individual misfold basins.
     * Output: a scalar index summarizing how many misfold basins contribute substantially to the total misfold occupancy, for example through an entropy based or threshold based count.

   * Preconditions:

     * Misfold basins must be separately identifiable in the encoding.
     * The decomposition must be stable under modest changes in coarse graining.

3. ComponentName: `CounterfactualFoldingWorld_Template`

   * Type: `experiment_pattern`

   * Minimal interface:

     * Inputs: a model class for folding landscapes (for example a family of coarse grained models or a class of AI generated landscapes) and a set of sequences.
     * Output: a pair of experiment definitions representing:

       * a World T like regime (compact folding theory, low tension),
       * a World F like regime (no compact theory, persistent high tension),

       with associated procedures for evaluating `Tension_fold`.

   * Preconditions:

     * The model class must support generation or estimation of the observables required for Q063 invariants.
     * The sequences must be such that experimental or high quality simulation data can be obtained or approximated.

### 8.2 Direct reuse targets

1. Q064 (BH_CHEM_GLASS_TRANS_L3_064)

   * Reused component: `FoldingEnergyLandscapeDescriptor`.
   * Why it transfers: both folding and glass transition involve rugged energy landscapes with many basins and barriers; the descriptor generalizes to non biopolymer systems by interpreting basins and transitions in terms of configurational states of the glass.
   * What changes: conformational basins and native states are replaced by local minima and macroscopic glassy states; `Gap_native` and `Misfold_fraction` are reinterpreted accordingly.

2. Q070 (BH_CHEM_SOFTMATTER_L3_070)

   * Reused component: `CounterfactualFoldingWorld_Template`.
   * Why it transfers: self assembly in soft matter exhibits funnel versus frustration behavior similar to folding; world T and world F scenarios can be used to test whether a compact effective theory exists for particular soft matter systems.
   * What changes: sequences are replaced by building block types or interaction patterns; native states are replaced by desired assembled structures.

3. Q071 (BH_BIO_ORIGIN_LIFE_L3_071)

   * Reused component: `MisfoldDegeneracyIndex`.
   * Why it transfers: early life scenarios require enough sequences with low misfold degeneracy to support stable functional structures; the index provides a quantitative measure of this requirement.
   * What changes: the distribution of sequences and environments is shifted to prebiotic regimes; the threshold for acceptable misfold degeneracy may differ from modern biology.

4. Q123 (BH_AI_INTERP_L3_123)

   * Reused component: `EnergyLandscapeObserver` derived from Q063.
   * Why it transfers: AI representation spaces often behave like energy landscapes; an observer that extracts gap, funnelness, roughness, and degeneracy features is useful for interpretability.
   * What changes: basins and transitions are interpreted in terms of representation patterns and optimization trajectories rather than physical conformations and dynamics.

---

## 9. TU roadmap and verification levels

This block explains how Q063 is positioned along the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of protein folding has been specified in terms of:

    * state space `M`,
    * observables and invariants,
    * a folding tension functional `Tension_fold`,
    * and a singular set with domain restriction.

  * Discriminating experiments have been outlined with clear falsification conditions for specific encodings.

* N_level: N1

  * The narrative linking sequence, energy landscape, folding behavior, and tension is explicit and internally coherent at the effective layer.
  * Counterfactual worlds have been defined in terms of observable patterns and tension regimes.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented in practice:

1. A working prototype that, for a curated set of proteins, constructs states `m_data` in `M_reg` from published data and computes:

   * `Gap_native`,
   * `Funnel_sharpness`,
   * `Misfold_fraction`,
   * `K_sep`,
   * `Tension_fold`,

   and publishes the resulting tension profiles alongside the source data.

2. A set of designed mutation experiments or high resolution simulations where predicted changes in `Tension_fold` are compared systematically with observed changes in folding robustness and misfolding propensity, following Experiment 2.

Both steps operate entirely on observables and do not require exposing any deep TU generative rule.

### 9.3 Path toward higher narrative levels

To progress from N1 to N2 and beyond, the following will be needed:

* A refined set of folding landscape archetypes, grounded in data, that can be described using a small number of invariants and used consistently across multiple proteins.
* Demonstrations that Q063 components (for example `FoldingEnergyLandscapeDescriptor`, `MisfoldDegeneracyIndex`) can transfer to other BlackHole problems such as Q064, Q070, and Q071 without major redesign.

In the long run, Q063 is expected to serve as:

* the reference node for thermodynamic_tension problems in biophysical chemistry,
* a testbed for how far TU style encodings can go in structuring reasoning about complex many body systems,
* and a bridge between microscopic physics, biological function, and AI representations through the shared language of rugged landscapes and tension.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non experts, while still aligned with the effective layer description.

Proteins are chains of amino acids that fold up into specific three dimensional shapes. Those shapes matter, because they determine what the protein can do in a cell.

The classical protein folding problem asks:

* If you know the sequence of amino acids and the environment,
* can you predict what shape the protein will take,
* how fast it will fold,
* and how likely it is to misfold or form harmful clumps

using a small set of physical principles that work for many different proteins?

In the Tension Universe view, we do not try to write down all the atomic details. Instead, we imagine a space of states. Each state summarizes, for one sequence and one environment:

* the important valleys (basins) in the energy landscape,
* how deep they are,
* how easy it is to move between them,
* and how likely the protein is to sit in each basin.

From each state, we extract a few key numbers:

* how much lower the native basin is than its main competitors (the energy gap),
* how strongly the landscape guides the chain toward the native basin (the funnel sharpness),
* how much probability sits in misfolded basins,
* how the timescale to fold compares with the timescale to escape misfolds.

We then combine some of these into a single quantity called folding tension. Roughly:

* low folding tension means the landscape looks like a clean funnel into the native state, with a good gap and limited misfolding,
* high folding tension means the landscape is messy, with many competing basins and unclear guidance toward the native state.

We consider two kinds of worlds:

* In a "compact theory" world, most natural proteins live in states where folding tension can be kept low, and a small set of rules explains how sequence and environment shape the landscape.
* In a "no compact theory" world, many proteins live in states with high folding tension, and no small set of rules can explain the variety of landscapes and behaviors.

This does not solve protein folding. It does not claim we already have the rules. Instead, it gives:

* a precise way to talk about how hard the folding problem is,
* a set of observable quantities to focus on,
* and experiments to test whether a particular way of encoding folding is reasonable.

Q063 is therefore the node in the Tension Universe that says:

* "If there is a simple, deep explanation of protein folding, this is how its effects would look at the level of energy gaps, funnels, misfolding, and tension."
* "If there is not, this is how that failure would show up in the same language."

That makes Q063 a central test of whether biological complexity in proteins can be reduced to a finite set of physically grounded principles, or whether significant residual tension remains even after careful modeling.
