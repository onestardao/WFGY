<!-- QUESTION_ID: TU-Q088 -->
# Q088 · Development of cortical maps

## 0. Header metadata

```txt
ID: Q088
Code: BH_NEURO_DEV_PATTERN_L3_088
Domain: Neuroscience
Family: Cortical development and plasticity
Rank: S
Projection_dominance: M
Field_type: developmental_neuroscience_field
Tension_type: map_topology_tension
Status: Open problem (no agreed unifying principle)
Semantics: hybrid (continuous sheet, discrete modules)
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

## 0. Effective layer disclaimer

This entry works strictly at the effective layer of the Tension Universe (TU) framework.

* It only defines effective state spaces, encoders, tension functionals and experiment classes for Q088.
* It does not specify or assume any particular bottom-level axiom system, microscopic dynamics or generating rules for TU itself.
* It does not claim to prove or disprove the canonical statement in Section 1 and must not be cited as a solution to the open problem.
* It does not provide an explicit mapping from raw biological variables (molecules, cells, detailed wiring diagrams) to internal TU fields. It only assumes that TU compatible models can reproduce the effective objects defined here.
* All references to state spaces, observables, invariants, tension scores and counterfactual worlds in this file are to be read as effective constructs.
* All uses of the tension terms T_topo, T_mod, T_wire and T_map, and all experiments in Section 6, are understood to be restricted to the regular domain specified in Section 3.5. States inside the singular set S_sing are explicitly out-of-domain for this entry.

Within these boundaries, the goal of this file is to give a precise, falsifiable encoding of Q088 at the effective layer, suitable for scientific testing and engineering use.

---

## 1. Canonical problem and status

**Canonical statement**

The problem asks for a general theory of how topographic and modular maps in cortex arise during development. Examples include:

* Retinotopic maps in visual cortex
* Somatotopic maps in somatosensory cortex
* Tonotopic maps in auditory cortex
* Modular structures such as orientation columns, ocular dominance columns and hypercolumns

Empirically, these maps emerge from initially coarse, noisy projections and gradually refine into structured organizations. Multiple mechanisms are known to contribute, including molecular gradients, axon guidance cues, spontaneous and sensory driven activity, and synaptic plasticity.

What is missing is a principled account that explains, in a single language:

1. Why cortical maps are approximately continuous and locally smooth yet contain modular structure and defects.
2. How the same basic cortex blueprint supports very different maps across modalities and species.
3. How innate constraints (molecular and anatomical) and experience dependent refinement combine into a small set of organizing rules.
4. Why certain map layouts are common or robust, while others are almost never seen.

**Status in the literature**

There are several major families of models.

* Chemoaffinity and axon guidance models, where molecular labels and gradients specify coarse topography that is later refined by activity.
* Self organizing models and neural field models, where local learning and lateral interactions produce maps that minimize some cost or energy functional.
* Hybrid models that include both molecular cues and activity dependent plasticity, often tuned to specific systems such as retinotopy.

These models explain many specific phenomena, but there is no single accepted functional or energy principle that covers all known cortical maps, all relevant developmental time scales and the full diversity of species and modalities. The question therefore remains an open S level problem in neuroscience.

**Role of this BlackHole entry**

This entry does not propose a new molecular mechanism. Instead it provides:

* A precise definition of what counts as a “cortical map” state at the effective layer.
* A tension functional over such states that encodes topographic distortion, modular frustration and wiring cost.
* A finite library of allowed map encoders and refinement procedures.
* A set of falsifiable predictions about developmental trajectories of this tension under biologically plausible dynamics.

If the proposed structure is consistently supported by data, it would count as a strong organizing principle for Q088 at the effective layer, while still leaving many micro level biological details open.

**References (non exhaustive)**

1. Swindale, N. V. “The development of topography in the visual cortex: a review of models.” Network: Computation in Neural Systems, 1996.
2. Cang, J., and Feldheim, D. A. “Developmental mechanisms of topographic map formation and alignment.” Annual Review of Neuroscience, 2013.
3. Goodhill, G. J. “Contributions of theoretical modeling to the understanding of neural map development.” Neuron, 2007.
4. Koulakov, A. A., and Chklovskii, D. B. “Orientation preference patterns in mammalian visual cortex: a wire length minimization approach.” Neuron, 2001.

---

## 2. Position in the BlackHole graph

**Upstream dependencies**

These problems supply constraints or ingredients that any solution to Q088 must respect.

* Q078  `BH_BIO_DEVELOPMENTAL_L3_078`
  “From genotype to phenotype.” Cortical map development is a special case of genotype to phenotype mapping where the phenotype is a spatially organized neural sheet.

* Q085  `BH_NEURO_PLASTICITY_RULES_L3_085`
  “General rules of synaptic plasticity.” Activity dependent refinement of maps must be compatible with whatever turns out to be the unified plasticity rules.

* Q083  `BH_NEURO_CODE_L3_083`
  “Neural coding principles.” The meaning of “topographic preservation” and “feature map” depends on how information is encoded in spike trains and population activity.

**Downstream dependents**

Progress on Q088 would provide structural primitives or constraints for these problems.

* Q089  `BH_NEURO_PREDICTIVE_CODE_L3_089`
  Predictive coding architectures typically assume layered topographic maps. A solution of Q088 at the effective layer would constrain which predictive coding implementations are biologically realistic.

* Q090  `BH_NEURO_SOC_BRAIN_L3_090`
  Social cognition networks are built on specific cortical areas that inherit their internal geometry from developmental maps.

* Q081  `BH_NEURO_CONSCIOUS_HARD_L3_081`
  Any account of the neural basis of conscious experience must use whatever spatial and modular structure cortex actually has. A theory of map formation limits the space of possible “neural correlates of consciousness” architectures.

**Graph role**

Within the BlackHole graph, Q088 acts as a meso scale hub:

* Above cell and synapse level, below global cognitive architecture.
* Bridging biological development (Q071–Q080) and high level cognition and consciousness (Q081–Q090).
* Providing a concrete test bed for Tension Universe encodings of self organization in a real biological system.

---

## 3. Tension Universe encoding (effective layer)

We describe how Q088 is represented in the Tension Universe effective layer. All objects and functionals below are effective constructs. They are not claimed to be fundamental physics.

### 3.1 State space

We fix the following effective objects.

* Sensory manifold S_in
  A low dimensional metric space representing the relevant sensory coordinates.
  Examples: retinal coordinates, skin surface coordinates, sound frequency axis.

* Cortical sheet C
  A two dimensional manifold with boundary, representing a patch of cortical tissue (for example area V1 or S1). Coarse geometry and boundaries are treated as given by anatomy.

* Map m
  A surjective function from S_in to C that associates sensory coordinates with cortical locations. At the effective layer we do not resolve individual axons. We represent m as a discretized map over a grid.

* Feature field phi
  A function from C to a feature space F that attaches feature preferences to cortical locations. F can include orientation, eye dominance, frequency, body part identity and similar labels.

* Wiring summary W
  An effective descriptor of connection patterns, such as local versus long range connectivity statistics.

A complete effective state for this problem is

```txt
state = (m, phi, W; params)
```

where params are hyperparameters that specify species, modality and scale.

### 3.2 Finite encoder library

To avoid hidden freedom and post hoc parameter tuning, we fix once, for this problem, a finite library of map encoders.

We introduce a finite registry of encoder prototypes:

* A finite set of smooth map encoders

  ```txt
  L_smooth = {SmoothEnc_1, ..., SmoothEnc_Ks}
  ```

  Each element of L_smooth is a concrete, pre registered encoder that represents m as a smooth map between grids using a fixed basis (for example a bounded set of radial basis functions with prescribed centers and widths).

* A finite set of modular encoders

  ```txt
  L_modular = {ModEnc_1, ..., ModEnc_Km}
  ```

  Each element of L_modular is a concrete encoder that represents phi as a tiling into modules (for example orientation columns) with fixed shape families, scale ranges and label sets.

* A finite set of fracture encoders

  ```txt
  L_fracture = {FracEnc_1, ..., FracEnc_Kf}
  ```

  Each element of L_fracture is a concrete encoder that captures map discontinuities and topological defects using a fixed catalogue of allowed singular structures (for example pinwheels and borders), with explicitly bounded parameter ranges.

We write

```txt
L_map = L_smooth ∪ L_modular ∪ L_fracture
```

and we fix a finite composition rule that specifies how elements of L_smooth, L_modular and L_fracture can be combined to encode a complete state (m, phi, W) at a given refine(k) level.

For this Q088 entry:

* Every encoder actually used in experiments or simulations must be an element of the finite registry L_map.
* No new encoder families or prototypes may be introduced after inspecting data for Q088. Any proposal that requires new encoders is treated as a new, versioned entry, not as a silent update of this file.
* Refinement operations (Section 3.4) are allowed to change resolution but not the encoder IDs selected from L_map.

The exact contents of the encoder registry (names, parameters) are stored in an external TU registry document referenced by this entry. This file fixes the structure and rules that the registry must obey.

### 3.3 Tension functional

We define a map topology tension functional

```txt
T_map(state) = alpha * T_topo(m)
             + beta  * T_mod(phi, m)
             + gamma * T_wire(W, m)
```

with the following constraints.

* T_topo, T_mod and T_wire are non negative functionals computed from finite encodings in L_map and finite summaries of W.

* The same functional forms for T_topo, T_mod and T_wire must be reused across species, modalities and experiments for this Q088 entry.

* The weights alpha, beta and gamma are non negative and satisfy

  ```txt
  alpha + beta + gamma = 1
  alpha >= eps_global
  beta  >= eps_global
  gamma >= eps_global
  ```

  for a fixed constant eps_global in the open interval (0, 1/3]. The value of eps_global is defined at the Tension Universe level by the TU Encoding and Fairness Charter and cannot be tuned per dataset.

* For this entry, the triple (alpha, beta, gamma) must be chosen once and for all, stored under a named configuration in the TU registry (for example `Q088_Tmap_weights_v1`), and reused unchanged across all datasets, species and experiments that claim to implement this file.

At the BlackHole level we only require that:

* Each term T_topo, T_mod and T_wire is non negative.
* Each term is computed from encoders in the finite library L_map and from finite summaries of W.
* The same weight triple (alpha, beta, gamma) is used across all experiments for this entry and is not retrofitted to individual datasets.

Any implementation that changes the functional forms of T_topo, T_mod or T_wire, or that tunes alpha, beta or gamma after looking at the data, is not an implementation of this Q088 spec.

### 3.4 Refinement procedure

We use a discrete refinement procedure refine(k) that increases resolution while preserving the encoder family.

* refine(0)
  Coarsest grid consistent with known anatomy and map extent.

* refine(k+1)
  Subdivides each cell from refine(k) into a fixed number of smaller cells, then reuses the same encoder family L_map to represent m and phi at the finer scale.

Refinement is allowed only along this hierarchy. No ad hoc mesh changes or encoder switches are permitted when fitting to new data. In particular:

* The encoder IDs selected from L_map must stay within the finite registry.
* Moving from refine(k) to refine(k+1) may only change the resolution parameters allowed by the encoder definitions, not the encoder prototypes themselves.

### 3.5 Singular set and domain restriction

We explicitly identify states where the above encoding is invalid.

* Singular set S_sing

  1. Cases where C is not homeomorphic to a two dimensional sheet at the relevant scale, for example due to large lesions or malformations that disconnect the area.
  2. Cases where S_in does not admit a low dimensional metric representation, for example when the relevant input space is intrinsically combinatorial and not spatial.
  3. In vitro preparations where there is no meaningful sensory manifold (for example isolated organoids without defined input axes).

For states in S_sing, T_map is not defined. This is a domain failure, not a claim about biology.

* Domain restriction

  We restrict Q088 in this entry to:

  * Primary sensory cortices (V1, A1, S1 and analogues).
  * Developmental windows from initial thalamocortical innervation until early adulthood.
  * Species where both sensory manifold and cortical area boundaries are reasonably well characterized.

All statements in this file that mention T_topo, T_mod, T_wire, T_map or their trajectories are to be understood as restricted to regular states with

```txt
state ∉ S_sing
```

Data or systems that fall into S_sing may not be used to tune encoders, refine(k) choices or weight configurations for this entry. They may only be used to mark the limits of the model’s applicability.

Higher order maps, symbolic representations and late life degeneration are addressed in other problems (for example Q087 and Q089).

---

## 4. Tension principle for this problem

The Tension Universe principle for Q088 is:

> During development, cortical maps evolve along trajectories that tend to reduce T_map, subject to biological constraints on growth, connectivity and activity, and they settle into constrained local minima of T_map that depend on species, modality and environment.

Key points.

1. T_map does not need to reach a global minimum. Anatomical constraints, finite developmental time and noise can trap the system in local minima.
2. Different modalities and species correspond to different parameter regimes, not to different energy functionals. The same structural terms T_topo, T_mod and T_wire and the same weight triple (alpha, beta, gamma) are reused for this entry.
3. Known phenomena such as map over expansion after sensory deprivation, reorganization after injury and emergence of modular patterns are interpreted as motion in state space that approximately follows the gradient of negative T_map, possibly with stochastic terms.
4. This principle is effective. It does not specify the exact molecular implementation. It only asserts that whatever the true micro dynamics are, they can be represented as approximately minimizing T_map under the stated encoding and domain restrictions.

This is a strong claim. It is falsifiable by systematically comparing T_map trajectories inferred from data against the predicted qualitative and quantitative patterns, under the fixed encoders and weights described in Section 3.

---

## 5. Counterfactual tension worlds

We now define a small family of counterfactual worlds for structured comparison. All worlds share the same encoder library L_map, weight configuration (alpha, beta, gamma) and T_map functional, but differ in constraint settings.

* World A: strong innate cues
  Molecular gradients and axon guidance cues are dominant. Activity dependent plasticity is weak. Trajectories of T_map are expected to show rapid early decrease dominated by T_topo, with relatively little late change. Maps are stable and similar across individuals.

* World B: strong activity dependence
  Molecular cues provide only coarse targeting. Activity dependent plasticity has large learning rates. T_map decreases more slowly and may temporarily increase when external input statistics change. Individual variability is high.

* World C: wiring cost dominated
  The system primarily minimizes T_wire, subject to weak topographic and modular terms. This favors short range connections even if topography and modularity are partially sacrificed. The result may be overly smooth maps with weak modular structure.

* World D: no coherent tension principle
  Dynamics do not approximate any consistent minimization of T_map with fixed weights. Observed maps are widely variable and fail to show systematic trajectories in T_map across development.

These worlds are coarse grained regimes in parameter space of the same effective model. Data can be used to infer which regime real cortical development occupies and whether a single regime covers multiple species and modalities under the constraints of this entry.

---

## 6. Falsifiability and discriminating experiments

All experiments in this section must use:

* Encoders drawn from the finite registry L_map.
* A pre registered refine(k) level.
* The single, pre registered weight configuration (alpha, beta, gamma) for this entry.

These choices must be fixed before inspecting detailed map patterns and logged for external audit.

### 6.1 Longitudinal map development trajectories

**Goal**

Test whether developmental trajectories of cortical maps in real animals resemble motion that reduces T_map under the fixed encoders and weights, rather than arbitrary drift that only superficially looks like refinement.

**Semantics implementation note**

* S_in is instantiated as an effective sensory coordinate space for the modality of interest (for example visual field coordinates for V1).
* C is instantiated as the cortical sheet for the chosen area, with boundaries defined by standard anatomical criteria.
* Maps and modular patterns are encoded using pre registered prototypes from L_map at a fixed refine(k) level, respecting the hybrid semantics declared in the header (“continuous sheet, discrete modules”).

**Boundary note**

This experiment does not test all possible theories of cortical map development. It tests the particular encoding of Q088 and the T_map principle defined in this file. A failure of this test falsifies the current Q088 effective layer proposal, not the canonical problem statement itself.

**Setup**

* Choose a species and cortical area where longitudinal imaging of map development is possible (for example mouse visual cortex).
* Use established methods to estimate retinotopic maps and orientation preference maps at multiple developmental time points.
* For each time point t, encode (m_t, phi_t, W_t) using a pre registered choice of encoders from L_map and a fixed refine(k) level, chosen before detailed inspection of the maps.

**Prediction**

1. The sequence T_map(state_t) must show a characteristic pattern.

   * Initial high T_topo and T_mod values as projections are coarse and modular structure is weak.
   * Monotonic or near monotonic decrease of T_topo during the main refinement period.
   * Emergence of modular patterns that reduce T_mod while increasing T_wire only within a small budget.

2. Across individuals with similar rearing conditions, the shape of T_map trajectories should be similar up to noise and minor time warping.

**Falsification condition**

The proposed encoding is falsified if, for a pre registered species, area and developmental window, one observes any of the following with high confidence, under the fixed encoders and weights:

* Persistent high T_topo or T_mod despite normal appearing maps by conventional analysis.
* Systematic increase of T_map over development that cannot be attributed to boundary conditions or measurement noise.
* Strong individual variability in T_map trajectories that does not correlate with known environmental or genetic differences.

If these failures persist across multiple reasonable choices of refine(k) within the fixed encoder family (pre registered before data analysis), the current T_map structure is rejected as a unifying principle for Q088 at the effective layer.

### 6.2 Perturbation and reorganization experiments

**Goal**

Test whether disruptions and recoveries of cortical maps correspond to predictable changes in T_map and its components, rather than arbitrary rearrangements that are invisible to the proposed tension functional.

**Semantics implementation note**

* The same definitions of S_in, C, encoders from L_map and refine(k) used in the longitudinal experiments must be reused here.
* Perturbations are represented as changes in boundary conditions, input statistics or lesions while keeping the encoding pipeline fixed.
* Comparisons are always made between regular states (state ∉ S_sing).

**Boundary note**

These experiments probe the robustness and explanatory power of the Q088 encoding under perturbations. A failure of T_map to reflect disruption and recovery falsifies or at least seriously weakens this specific tension principle. It does not, by itself, rule out all tension based approaches to cortical maps.

**Setup**

* Use existing perturbations such as altered sensory input, partial lesions or cross modal rewiring (for example retinal input to auditory cortex).
* Apply the same encoding pipeline as in Section 6.1 to pre and post perturbation maps, using the same encoders, refine(k) level and weight configuration.

**Prediction**

* T_map should increase immediately after a perturbation that disrupts map organization, then decrease again as the system reorganizes, possibly to a new local minimum consistent with changed constraints.
* The direction and magnitude of changes in the individual terms T_topo, T_mod and T_wire should match qualitative expectations. For example, a lesion that removes part of S_in should increase topographic distortion (T_topo) but may reduce wiring cost (T_wire) in some regions.

**Falsification condition**

If perturbations produce stable maps that are not local minima of T_map under any reasonable boundary conditions, or if T_map fails to reflect qualitative notions of “disruption” and “recovery” in a consistent way across individuals and experiments, then either:

* The effective encoding of Section 3 is inadequate, or
* The tension principle of Section 4 does not describe real cortical map development,

and the Q088 effective layer proposal must be revised or rejected.

---

## 7. AI and WFGY engineering spec

This block states how an AI system equipped with WFGY and Tension Universe tools would work with Q088 in practice. It is an engineering spec, not a claim about biological implementation.

### 7.1 Data interface

Inputs:

* Anonymized imaging data or estimated maps over time for a given cortical area and species.
* Metadata specifying S_in definition, cortical boundaries, developmental ages and experimental conditions.

Outputs:

* Encoded states (m_t, phi_t, W_t) at chosen refine(k) levels.
* Time series of T_topo, T_mod, T_wire and T_map.
* Summaries of individual and group trajectories.

All calls that compute these quantities are routed through a WFGY style semantic firewall that logs encoder choice, parameters, data slices used and tension values. This prevents silent changes to encoders, weights or domains.

### 7.2 Algorithmic pipeline

At a high level:

1. Map reconstruction

   * Ingest raw data.
   * Reconstruct m_t and phi_t using a pre registered algorithm for the chosen modality.

2. Encoding selection

   * Choose encoder prototypes from L_map based only on modality, species and experimental design, not on the detailed pattern of the maps.
   * Fix refine(k) resolution and the weight configuration (alpha, beta, gamma) before inspecting the fine structure of the map.

3. Tension computation

   * Compute T_topo, T_mod and T_wire for each state_t using fixed formulas and encoders.
   * Combine them with the fixed weights alpha, beta, gamma to obtain T_map.

4. Trajectory analysis

   * Compare trajectories across individuals, species and experimental conditions.
   * Test the predictions from Section 6 using pre registered statistical criteria.

5. Logging and audit

   * Store all decisions, parameter values and results in a structured log to allow external audit and replication.

### 7.3 Scope and limitations

* The spec only covers primary sensory cortical maps. Higher order maps and subcortical structures require separate entries.
* The spec assumes that adequate data quality and longitudinal coverage are available, which may be a limiting factor in current experiments.
* The spec does not dictate which molecular or cellular mechanisms produce the observed trajectories. It only constrains their effective consequences at the map level.

---

## 8. Cross problem transfer template

Here we specify how the structure defined for Q088 can be reused or imported into other BlackHole problems and how results from other problems feed back into Q088.

### 8.1 From Q078 (genotype to phenotype) to Q088

* Use Q078 encodings of developmental gene expression patterns and morphogen gradients as priors on the allowed coarse forms of m and W.
* Restrict the initial conditions for state_0 in Q088 to those compatible with these priors.

This makes Q088 a special case of genotype to phenotype mapping where the phenotype is a map plus modular structure.

### 8.2 From Q085 (plasticity rules) to Q088

* Use Q085 to constrain which learning rules can drive motion in state space.
* Check whether the plasticity rules that best fit synaptic level data also produce T_map trajectories consistent with Section 6 when embedded in network simulations.

If there is a mismatch, at least one of Q085 and Q088 must be revised.

### 8.3 From Q088 to Q089 (predictive coding implementation)

* Treat the final map states for a given species and modality as the geometry on which predictive coding circuits must be implemented.
* Use T_map to define a cost for predictive wiring that respects or violates topographic constraints.

This constrains which predictive coding implementations are plausible in real cortex and which require unrealistic rewiring.

### 8.4 Generic reuse template

To reuse the Q088 structure for another problem:

1. Identify the relevant sensory or feature manifold S_in and cortical or neural sheet C.
2. Encode the map and modular structure using encoder prototypes from L_map and a pre registered refine(k) level.
3. Compute T_map using the same functional and weight configuration.
4. Interpret changes in T_map across manipulations or conditions as differences in developmental or plasticity regimes.

This template keeps the core definitions fixed and only changes the biological context.

---

## 9. TU roadmap and verification levels

We now state a roadmap for this entry and how it moves through verification levels.

### 9.1 E levels

* E0
  Pure narrative speculation without precise encodings or functionals.

* E1 (current)
  Precise state space, finite encoder library, tension functional structure and falsifiable experiment classes defined as in this file. No full scale implementation or data fitting yet.

* E2
  At least one complete implementation of the encoding and tension computation on real or high quality simulated data, with pre registered analysis and public code. First serious attempts at falsification performed.

* E3
  Cross species and cross modality validation, including both visual and non visual maps. Consistent support for T_map trajectories and counterfactual regimes across multiple labs and datasets.

This entry is at E1. Parts of Sections 6 and 7 are designed so they can be promoted to E2 with minimal extra assumptions.

### 9.2 N levels

Informal narrative levels:

* N1 (current)
  Coherent description focused on experts in neuroscience and theoretical modeling.

* N2
  Extended explanatory material that connects map development to broader questions in cognition and pathology (for example Q087 and Q081) while preserving the precise core definitions.

* N3
  Integration into a more general Tension Universe description of self organization across biological systems, making Q088 a clear special case of a wider pattern.

### 9.3 Internal consistency checkpoints

For any future edits or implementations associated with this entry:

1. Check that all encoders remain within the finite registry L_map and that refine(k) is used only as defined in Section 3.4.
2. Check that S_sing and domain restrictions (Section 3.5) are respected. Data outside the domain must not be used to tune encoders, refine(k) or weights.
3. Check that alpha, beta and gamma match the pre registered configuration for this entry and are not adjusted after looking at the data.
4. Check that every experiment using this entry specifies in advance which falsification conditions will be used and logs all relevant choices so that an external auditor can re run the analysis.

If any of these checkpoints fail, the work should be treated as a different proposal, not as an implementation of this Q088 entry.

---

## 10. Elementary but precise explanation

This block is for readers who are not specialists but still want a precise idea of what is being claimed.

The cortex is a sheet of brain tissue that carries many maps of the body and the world. There is a map of the visual field, a map of the body surface, a map of sound frequencies and more. These maps are not present at birth in final form. They grow and refine over time as the brain develops.

The open question is: what rule makes these maps organize themselves the way they do?

The idea in this entry is to treat map development like a physical system that tries to reduce a kind of tension.

* One part of the tension measures how much the map distorts neighborhood relations. Nearby points in the eye or on the skin should end up nearby in cortex.
* Another part measures how “frustrated” the modular patterns are. Orientation columns and similar modules should fit smoothly into the map instead of breaking it into irregular fragments.
* A third part measures wiring cost. The brain prefers solutions that use shorter and more efficient connections.

We do not know exactly how neurons implement this rule. However we can write down a precise formula that combines these three ingredients into a single number called T_map. Then we can test real data.

If we take images of developing maps in animals and encode them in a fixed way, we can see how T_map changes over time.

* If the idea is right, T_map should start high and then go down as the map refines.
* If we disrupt the system, for example by changing the input or making a small lesion, T_map should go up and then down again as the map reorganizes.

If instead T_map does not behave in these ways, and there is no reasonable way to adjust the fixed definitions without breaking the rules set at the start, then this particular tension principle is wrong for cortical maps.

In that sense Q088, in this Tension Universe version, is not “solved”. It is turned into a clear set of claims that can be confronted with experiments and either supported or falsified.

---

## Tension Universe effective-layer footer

This page is part of the WFGY / Tension Universe S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective-layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.
* All candidate principles stated here are to be read as testable, revisable hypotheses about effective behaviour, not as final statements about biology or physics.

### Effective-layer boundary

* All objects used here (state spaces, observables, invariants, tension scores, counterfactual worlds) live in the effective layer of the Tension Universe framework.
* No claim is made that any of these objects correspond one-to-one to fundamental physical quantities.
* Whenever this entry speaks about “minimizing” or “trajectories” of T_map, it refers to behaviour under the encoders, weights and domains fixed in this file.
* Data or systems that fall into the singular set S_sing are explicitly out-of-domain for this entry: for them, T_map is undefined and must not be retrofitted.

### Encoding and fairness

* Encoders, weights and refinement levels used by this entry must be chosen from finite, pre registered libraries, as defined in Section 3.
* They may not be adjusted post hoc to fit particular datasets. Any such adjustment defines a different proposal.
* Any implementation claiming to instantiate this entry must log encoder IDs, weight configurations, refine(k) choices and domain filters so that an external auditor can check compliance with this spec and with the TU Encoding and Fairness Charter.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
