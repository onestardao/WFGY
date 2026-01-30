<!-- QUESTION_ID: TU-Q068 -->
# Q068 · Prebiotic chemistry networks

## 0. Header metadata

```txt
ID: Q068
Code: BH_CHEM_PREBIOTIC_NETWORK_L3_068
Domain: Chemistry
Family: Prebiotic chemistry and origins of life
Rank: S
Projection_dominance: M
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-30
EncodingClass: E_PREBIO
EncodingKey:   Q068_PREBIO_CORE_V1
LibraryKey:    Q068_PREBIO_LIB_V1
WeightKey:     Q068_PREBIO_WEIGHTS_V1
RefinementKey: Q068_PREBIO_REFINE_V1
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* We only specify:

  * state spaces,
  * observables and fields,
  * mismatch and tension functionals,
  * singular sets and regular domains,
  * experiment patterns,
  * AI and engineering interfaces.

* We **do not**:

  * propose or modify any underlying axiom system or TU generative rule,
  * claim to prove or disprove the canonical open problem about prebiotic chemistry networks,
  * introduce any new theorem about physics, chemistry, or origins of life.

This page works inside a fixed **admissible encoding class**:

```txt
E_PREBIO = { E : prebiotic-network encodings compatible with TU effective layer rules }
```

and all constructions below are defined with respect to a **single encoding**

```txt
E in E_PREBIO
```

identified in the header by

```txt
EncodingKey   = Q068_PREBIO_CORE_V1
LibraryKey    = Q068_PREBIO_LIB_V1
WeightKey     = Q068_PREBIO_WEIGHTS_V1
RefinementKey = Q068_PREBIO_REFINE_V1
```

For this document:

* every state space, observable, mismatch functional, tension functional, singular set, and tensor is implicitly a function of `E`,
* we write `M(E)`, `DeltaS_struct(m; E)` and similar when precision is needed,
* when there is no risk of confusion we may omit `; E` in the notation, but the dependence on `E` is always present.

**Fairness and non retrospection**

* All global thresholds and weights that appear here, such as

  ```txt
  a_struct(E), a_flux(E), a_robust(E),
  epsilon_pre(E), delta_pre(E)
  ```

  are **encoding level constants**. They are fixed once for the encoding `E` and do not depend on individual states, experiments, or datasets.

* Reference ensembles for networks and environments, as well as robustness criteria, are also fixed at the encoding level and are not tuned case by case.

* Any substantial change to:

  * mismatch definitions,
  * reference ensembles,
  * global thresholds,
  * or weight schemes

  must be recorded as a change in `WeightKey`, `RefinementKey`, or `EncodingKey`, and is treated as a **different encoding** rather than a retroactive adjustment of the same one.

The role of this page is:

* to describe how the canonical problem behind Q068 can be encoded at the effective layer,
* to specify falsifiable properties of particular encodings in `E_PREBIO`,
* to define reusable modules for AI and WFGY systems.

It is **not** evidence that prebiotic chemical networks of any particular sort actually exist in nature. All world level scenarios and counterfactuals that follow are **conditional on the chosen encoding `E`**.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Consider plausible prebiotic environments on early Earth or similar planets that are driven far from equilibrium by energy fluxes such as light, redox gradients, or geothermal heat. Within such environments, complex chemical reaction networks involving small molecules, simple polymers, and mineral surfaces can, in principle, emerge and evolve.

The canonical problem for Q068 is:

> Do there exist physically realistic, non equilibrium prebiotic chemical networks that
>
> 1. are robustly sustained by environmental driving,
> 2. maintain and propagate nontrivial chemical organization over long times,
> 3. can, in a well defined sense, increase their functional complexity,
>    without already presupposing modern biological machinery?

Equivalently, in more operational terms:

> Under realistic early Earth conditions, can we identify classes of reaction networks and environmental protocols that support long lived, self sustaining, and structurally organized prebiotic chemistry, rather than quickly relaxing to chemical equilibrium or trivial steady states?

The problem is not only to propose isolated reaction sequences. The goal is to understand the **structure and existence of entire network regimes** that can act as proto metabolic scaffolds.

### 1.2 Status and difficulty

Progress has been made in several directions:

* Identification of specific prebiotic reaction pathways, such as routes toward nucleotide precursors, simple peptides, and lipid precursors under plausible early Earth conditions.
* Development of systems chemistry models that explore network level behavior beyond single reactions.
* Non equilibrium thermodynamics frameworks that relate entropy production, fluxes, and emergent structures.

However, there is no widely accepted, quantitative theory that simultaneously:

* unifies non equilibrium driving, network topology, and environmental variability,
* clearly distinguishes regimes that support robust prebiotic organization from those that do not,
* connects laboratory scale experiments with planetary scale constraints in a systematic way.

The problem remains extremely hard because it sits at the intersection of:

* complex reaction network dynamics,
* disordered and heterogeneous geochemical environments,
* non equilibrium thermodynamics and information like notions of organization.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q068 serves as:

1. The core S level node for **prebiotic chemistry networks**, linking chemistry to origins of life biology.
2. A template for **thermodynamic_tension** problems where sustained non equilibrium structure and organization must be explained without invoking existing biological machinery.
3. An interface node between:

   * chemical S problems (Q061–Q070),
   * biological and origins of life problems (Q071–Q080),
   * planetary environment and climate problems in other domains.

Q068 is the primary place where non equilibrium chemical networks are explicitly encoded in Tension Universe terms.

### References

1. I. Prigogine and G. Nicolis, *Self Organization in Non Equilibrium Systems*, Wiley, 1977.
2. J. D. Sutherland, “The Origin of Life Out of Equilibrium”, discussed in modern reviews of prebiotic chemistry and non equilibrium driving.
3. E. Smith and H. J. Morowitz, *The Origin and Nature of Life on Earth: The Emergence of the Fourth Geosphere*, Cambridge University Press, 2016.
4. Standard reviews on prebiotic chemistry and systems chemistry in origin of life textbooks and survey articles.

---

## 2. Position in the BlackHole graph

This block records how Q068 sits in the BlackHole graph. Each edge has a one line reason pointing to concrete components or tension types, at the effective layer.

### 2.1 Upstream problems

These provide foundations, tools, or constraints that Q068 reuses at the effective layer.

* **Q061 (BH_CHEM_BOND_NATURE_L3_061)**
  Reason: Supplies effective descriptions of strongly correlated chemical bonding used inside the network state space and flux descriptors.

* **Q062 (BH_CHEM_CATALYST_DESIGN_L3_062)**
  Reason: Provides design level views of catalysis that feed into how catalytic motifs are represented in prebiotic network observables.

* **Q066 (BH_CHEM_ELECTROCHEM_L3_066)**
  Reason: Contributes non equilibrium electrochemical motifs reused as template fields for environmental driving and energy flux observables.

* **Q067 (BH_CHEM_QUANTUM_MOL_SIM_L3_067)**
  Reason: Enables high accuracy effective parameters for key prebiotic reactions, which are then aggregated in the network level encoding.

### 2.2 Downstream problems

These directly reuse Q068 components or depend on its notion of prebiotic network tension.

* **Q069 (BH_CHEM_SELECTIVITY_RULES_L3_069)**
  Reason: Reuses network based selectivity components to frame reaction selectivity as emergent from prebiotic network structures.

* **Q070 (BH_CHEM_SOFTMATTER_L3_070)**
  Reason: Uses the non equilibrium network observables of Q068 as prototypes for soft matter self assembly under continuous driving.

* **Q071 (BH_BIO_ORIGIN_LIFE_L3_071)**
  Reason: Builds on Q068 prebiotic network tension to specify when a network crosses into proto biological organization.

* **Q072 (BH_BIO_GENETIC_CODE_L3_072)**
  Reason: Treats the emergence of coding as a special case of structured channels embedded in driven chemical networks defined at the Q068 level.

### 2.3 Parallel problems

Parallel nodes share similar tension types or structural motifs, but no direct component dependence.

* **Q064 (BH_CHEM_GLASS_TRANS_L3_064)**
  Reason: Both Q064 and Q068 involve rugged energy landscapes and non equilibrium structure formation, expressed via thermodynamic_tension.

* **Q070 (BH_CHEM_SOFTMATTER_L3_070)**
  Reason: Both focus on sustained non equilibrium organization in soft condensed matter, though Q068 is specific to prebiotic chemistry networks.

### 2.4 Cross domain edges

Cross domain edges mark problems that can reuse Q068 components or interpret them in other settings.

* **Q031 (BH_EARTH_PLANET_ENV_L3_031)**
  Reason: Uses Q068 environment flux descriptors to constrain which planetary surface and subsurface conditions support prebiotic networks.

* **Q073 (BH_BIO_METABOLIC_CORE_L3_073)**
  Reason: Reuses prebiotic network motifs as ancestral templates for core metabolic networks.

* **Q098 (BH_CS_AUTOCATALYTIC_ALG_L3_098)**
  Reason: Adopts the network level tension formalism from Q068 to analyze autocatalytic structures in abstract algorithmic networks.

---

## 3. Tension Universe encoding (effective layer)

This block describes the effective layer encoding of prebiotic chemistry networks. It only specifies state spaces, observables, mismatch functionals, tension functionals, and singular sets, with explicit dependence on the encoding `E`.

### 3.0 Encoding class and notation

We work with the admissible encoding class

```txt
E_PREBIO
```

where each `E in E_PREBIO` provides:

* a semantic state space `M(E)`,
* observable fields

  * `C_i(m; E)` for species abundances,
  * `J_e(m; E)` for reaction fluxes,
  * `Phi_env(m; E)` for environmental driving descriptors,
  * `Sigma_net(m; E)` for entropy production rates,
  * `O_struct(m; E)` for structural organization,
* mismatch observables

  * `DeltaS_struct(m; E)`,
  * `DeltaS_flux(m; E)`,
  * `DeltaS_robust(m; E)`,
* a combined mismatch functional `DeltaS_pre(m; E)`,
* a tension tensor `T_ij(m; E)`,
* a singular set `S_sing(E)` and regular domain `M_reg(E)`.

For the rest of this document we fix a single encoding `E` with keys given in the header and view all objects as defined relative to this `E`. When the context is clear we may omit `; E` for readability, but it is always implied.

### 3.1 State space

We postulate an effective state space

```txt
M(E)
```

with the following interpretation:

* Each state `m in M(E)` represents a coarse grained configuration of a prebiotic chemical network in a specified environment, including:

  * a finite set of chemical species and reaction channels,
  * an effective representation of network topology, such as which species participate in which reactions,
  * aggregate information about fluxes, entropy production, and environmental driving.

We do not specify how `m` is constructed from underlying microstates or from any TU deep layer. At the effective layer we only require:

* For any finite laboratory or geochemical setup in a bounded region and time window, there exist states in `M(E)` that encode a consistent coarse grained description of the network under that setup.

### 3.2 Effective fields and observables

We introduce the following observables and fields on `M(E)`.

1. **Species abundance field**

   ```txt
   C_i(m; E) >= 0
   ```

   * For each species index `i` in a finite set associated with `m`, `C_i(m; E)` is an effective abundance, for example a concentration, at a chosen reference time window.

2. **Reaction flux field**

   ```txt
   J_e(m; E)
   ```

   * For each reaction channel index `e` in the network associated with `m`, `J_e(m; E)` is an effective net flux, for example an average reaction rate in a chosen time window.
   * Fluxes can be positive, negative, or zero, depending on direction conventions.

3. **Environmental driving descriptor**

   ```txt
   Phi_env(m; E)
   ```

   * A finite dimensional descriptor of environmental driving, aggregating quantities such as:

     * light intensity bands,
     * redox potential differences,
     * temperature gradients,
     * pH gradients,
     * other relevant energy or matter fluxes at the encoding resolution.

4. **Entropy production rate**

   ```txt
   Sigma_net(m; E) >= 0
   ```

   * An effective scalar observable summarizing the network level entropy production rate associated with the combination of reaction fluxes and environmental driving.
   * For states in the regular domain defined below, `Sigma_net(m; E)` is finite and well defined.

5. **Structural organization score**

   ```txt
   O_struct(m; E)
   ```

   * A scalar observable that summarizes structural organization of the network, such as:

     * presence and strength of cycles,
     * modularity,
     * redundancy of key pathways,
     * separation between fast and slow subnetworks,
     * existence of autocatalytic sets.

The detailed construction of these observables from experimental or simulated data is part of the encoding `E` and lies outside this document. Here we only assume that for states in the regular domain, all are well defined and finite.

### 3.3 Mismatch observables and reference classes

To define tension, we introduce mismatch observables relative to fixed reference classes that are part of `E`.

1. **Reference ensembles**

Each `E in E_PREBIO` specifies:

* a reference ensemble of reaction networks that are:

  * random or near equilibrium, given the same species list and total driving magnitudes,
  * constructed according to a fixed, pre declared protocol recorded by `LibraryKey(E)` and `RefinementKey(E)`,
* a reference ensemble of environmental profiles compatible with the same total energy flux scale.

These ensembles are chosen **once per encoding** and do not depend on the target state `m`. They are not tuned after seeing specific experiments or simulation outputs.

2. **Structural mismatch observable**

   ```txt
   DeltaS_struct(m; E) >= 0
   ```

   * Measures how far the structural organization of the network in `m` deviates from the reference ensemble, in terms of `O_struct(m; E)` and additional structure descriptors fixed by `E`.
   * `DeltaS_struct(m; E)` is zero when the network organization is indistinguishable from typical reference networks, within encoding resolution.
   * It increases as the organization becomes more structured, more fragile, or more finely tuned in ways that matter for prebiotic function.

3. **Flux mismatch observable**

   ```txt
   DeltaS_flux(m; E) >= 0
   ```

   * Measures how far the flux pattern `J_e(m; E)` and associated `Sigma_net(m; E)` deviate from what would be expected for near equilibrium or reference driven networks under similar `Phi_env(m; E)`.
   * `DeltaS_flux(m; E)` is zero when fluxes and entropy production are compatible with a reference regime and positive when they show significant non equilibrium organization signatures.

4. **Robustness mismatch observable**

   ```txt
   DeltaS_robust(m; E) >= 0
   ```

   * Encodes how sensitive the network behavior is to small perturbations in `Phi_env(m; E)` and `C_i(m; E)`.
   * `DeltaS_robust(m; E)` is small when the network maintains its organizational features under moderate environmental fluctuations.
   * It is larger when the network collapses, loses structure, or becomes chaotic under such perturbations.

For a fixed encoding `E`, all three mismatch observables are fixed functions. They are **not** adjusted post hoc in response to particular data points or desired outcomes.

### 3.4 Combined prebiotic network tension

We define a combined mismatch

```txt
DeltaS_pre(m; E) =
  a_struct(E) * DeltaS_struct(m; E)
+ a_flux(E)   * DeltaS_flux(m; E)
+ a_robust(E) * DeltaS_robust(m; E)
```

with nonnegative weights

```txt
a_struct(E) >= 0,
a_flux(E)   >= 0,
a_robust(E) >= 0,
a_struct(E) + a_flux(E) + a_robust(E) = 1.
```

These weights are part of the encoding `E` and are recorded by `WeightKey(E)`.

* They are chosen once, based on general principles about the relative importance of structure, flux, and robustness for prebiotic viability.
* They are **not** tuned per state, per experiment, or per dataset.

Intuitively:

* `DeltaS_struct` measures how organized the network is compared to near equilibrium baselines.
* `DeltaS_flux` measures how non equilibrium the fluxes are compared to reference ensembles.
* `DeltaS_robust` measures how stable the organization is under realistic fluctuations.

### 3.5 Effective tension tensor and regular domain

We assume an effective tension tensor

```txt
T_ij(m; E) = S_i(m; E) * C_j(m; E) * DeltaS_pre(m; E) * lambda(m; E) * kappa(E)
```

where:

* `S_i(m; E)` is a source like factor for semantic or functional dimensions indexed by `i`.
* `C_j(m; E)` is a receptivity like factor for downstream or cognitive dimensions indexed by `j`.
* `DeltaS_pre(m; E)` is the combined mismatch defined above.
* `lambda(m; E)` is a convergence state factor provided by the TU core, taking values in a fixed bounded interval. In this document it is treated as an observable of the effective layer.
* `kappa(E)` is a constant that sets the overall scale of prebiotic network tension for this encoding.

The detailed index sets for `i` and `j` are not needed at the Q068 level. It is enough that

* `T_ij(m; E)` is finite on the regular domain, and
* encodes how prebiotic network tension couples to other TU components when needed.

We define the singular set

```txt
S_sing(E) = {
  m in M(E) :
    Sigma_net(m; E) is undefined or not finite
    or any of DeltaS_struct(m; E),
           DeltaS_flux(m; E),
           DeltaS_robust(m; E)
       is undefined or not finite
}
```

and restrict effective analysis to the regular domain

```txt
M_reg(E) = M(E) \ S_sing(E).
```

Whenever an experiment or evaluation attempts to use states in `S_sing(E)`, the result is treated as **out of domain** rather than as evidence for or against the existence of robust prebiotic networks or the validity of TU itself.

---

## 4. Tension principle for this problem

This block states how Q068 is characterized as a tension problem within TU at the effective layer, relative to the fixed encoding `E`.

### 4.1 Core prebiotic network tension functional

For all `m in M_reg(E)` we define

```txt
Tension_prebiotic(m; E) = DeltaS_pre(m; E) >= 0.
```

Interpretation:

* Low `Tension_prebiotic(m; E)` means:

  * structure and fluxes are in a regime compatible with sustained, organized non equilibrium behavior under the chosen environment, according to encoding `E`.

* High `Tension_prebiotic(m; E)` means:

  * the configuration is fragile, near collapse, or incompatible with the required non equilibrium organization, again according to `E`.

No claim is made that nature must adopt the same notion of tension. This is a **tool** for organizing evidence and reasoning.

### 4.2 Prebiotic viability as a low tension regime

At the effective layer, Q068 can be framed as the statement that there exist physically realistic, environmentally compatible states

```txt
m_viable in M_reg(E)
```

such that

```txt
Tension_prebiotic(m_viable; E) <= epsilon_pre(E)
```

for a small threshold `epsilon_pre(E)` that:

* reflects acceptable deviations from reference ensembles and robustness criteria for this encoding,
* remains bounded as we increase resolution in network description and environmental detail inside the same encoding,
* is determined by encoding choices fixed in advance and recorded in `WeightKey(E)` or related metadata.

Such states represent **viable prebiotic networks** in the sense of this encoding `E`:

* they are not trivial random networks,
* they are not finely tuned equilibria,
* they exhibit organized structures sustained by non equilibrium driving, with robustness against moderate perturbations.

This is an encoding level notion of viability; it is not a claim that such networks exist in the real world.

### 4.3 Failure regimes as persistent high tension

Conversely, for the same encoding `E`, we may find that in all physically realistic settings and data sources, every state `m_real` that faithfully encodes a candidate prebiotic network satisfies

```txt
Tension_prebiotic(m_real; E) >= delta_pre(E)
```

for some strictly positive `delta_pre(E)` such that:

* `delta_pre(E)` cannot be reduced below a meaningful level by making the encoding more detailed while staying within the same encoding class and keys,
* attempts to retune observables or weights would require changing encoding keys and would therefore correspond to a different encoding.

In this situation, relative to `E`:

* prebiotic chemistry appears as a **high tension regime**,
* any networks with nontrivial organization either:

  * are extremely fragile under environmental change, or
  * require unrealistically fine tuning of conditions, or
  * fail to persist over relevant timescales.

Thus, at the effective layer, Q068 distinguishes:

* encodings and worlds in which low tension prebiotic network regimes exist and can be instantiated,
* encodings and worlds in which all realistic prebiotic chemistry falls into high tension regimes.

These are statements about the **joint behavior** of the encoding `E` and world models. They are not proofs about the unique structure of the physical universe.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds at the effective layer, relative to the fixed encoding `E`. They are expressed only in terms of observables and tension scores; no microphysical generative mechanism is specified.

### 5.1 World T (prebiotic networks viable)

World T is a world where non equilibrium prebiotic chemistry readily forms robust networks under plausible environmental conditions.

1. **Network emergence**

   For a broad set of geochemical settings, one can construct states `m_T in M_reg(E)` such that:

   ```txt
   DeltaS_struct(m_T; E) is small,
   DeltaS_flux(m_T; E)   is small,
   DeltaS_robust(m_T; E) is small.
   ```

   These networks exhibit nontrivial organization and remain stable under the driving schemes represented in `Phi_env(m_T; E)`.

2. **Entropy production and structure**

   ```txt
   Sigma_net(m_T; E) > 0
   ```

   and remains in a band where non equilibrium driving is strong enough to support structure but not so extreme as to destroy it. Networks do not require extremely fine tuning of entropy production to remain viable.

3. **Environmental robustness**

   Moderate changes in `Phi_env(m_T; E)` do not push networks into `S_sing(E)`, and

   ```txt
   Tension_prebiotic(m_T; E) <= epsilon_pre(E)
   ```

   over a range of conditions. Low tension prebiotic regimes occupy a non negligible volume in the space of environmental parameters for this encoding.

### 5.2 World F (prebiotic networks fragile or absent)

World F is a world where prebiotic networks are either extremely fragile or do not reach meaningful organization, as measured by the encoding `E`.

1. **Collapse to equilibrium or triviality**

   For most plausible geochemical settings, any state `m_F in M_reg(E)` that shows initial organization quickly evolves toward configurations with:

   ```txt
   O_struct(m_F; E) near reference values,
   DeltaS_struct(m_F; E) and DeltaS_flux(m_F; E)
     large or poorly controlled.
   ```

   Networks either relax toward near equilibrium behavior or fluctuate in ways that do not maintain sustained organization.

2. **Flux and robustness**

   Small perturbations in `Phi_env(m_F; E)` or `C_i(m_F; E)` lead to drastic changes in `J_e(m_F; E)`, pushing states into `S_sing(E)` or into regimes with high `Tension_prebiotic(m_F; E)`.

3. **Absence of low tension regime**

   No matter how the encoding resolution is refined within the same encoding class and keys, it is not possible to identify states that maintain `Tension_prebiotic(·; E)` below a reasonable `epsilon_pre(E)` over long time windows.

### 5.3 Interpretive note

These worlds do not specify how networks or environments are generated from microphysics or from TU deep layers. They only assert that, **for any such generative mechanism compatible with a given world and the encoding `E`**, there either exist or do not exist effective states with the observable properties described above.

Any conclusion of the form “our world looks more like World T than World F” must be understood as:

* conditional on the chosen encoding `E`,
* dependent on how experimental and simulation data are mapped into `M_reg(E)`.

---

## 6. Falsifiability and discriminating experiments

This block lists experiments that can falsify specific Q068 encodings at the effective layer. All experiments are defined relative to the fixed encoding `E` identified in the header.

### Experiment 1: Microreactor network persistence under controlled driving

**Goal**
Test whether the chosen `Tension_prebiotic(·; E)` encoding correctly distinguishes persistent, organized network behavior from transient or trivial chemistry in microreactor experiments.

**Setup**

* Use microfluidic or batch microreactor platforms with simple prebiotic mixtures, for example carbon sources, inorganic ions, and potential catalysts.
* Apply controlled non equilibrium driving, such as periodic temperature cycling, redox gradients, light pulses, or flow gradients.
* Fix a protocol, recorded under `RefinementKey(E)`, that maps experimental conditions to environmental descriptors `Phi_env(m_exp; E)` and extracts effective `C_i(m_exp; E)`, `J_e(m_exp; E)`, `Sigma_net(m_exp; E)`, and `O_struct(m_exp; E)`.

All analysis is carried out with a **single encoding**

```txt
E in E_PREBIO
```

specified by the keys in the header. Any substantial change in extraction rules, reference ensembles, or weighting that would alter `DeltaS_*` in more than a small, smooth way must be recorded as a change in keys and treated as a different encoding.

**Protocol**

1. Prepare multiple experimental conditions with different driving protocols but similar overall chemical compositions.

2. For each condition, record time series of species abundances and reaction rates sufficient to estimate

   ```txt
   C_i(m_exp; E),
   J_e(m_exp; E),
   Sigma_net(m_exp; E),
   O_struct(m_exp; E).
   ```

3. For each experiment, construct a state `m_exp in M_reg(E)` that reflects the coarse grained network at the chosen time window and driving protocol.

4. Compute

   ```txt
   DeltaS_struct(m_exp; E),
   DeltaS_flux(m_exp; E),
   DeltaS_robust(m_exp; E),
   Tension_prebiotic(m_exp; E).
   ```

5. Compare tension values and network lifetimes, structural richness, and robustness across conditions.

**Metrics**

* Distribution of `Tension_prebiotic(m_exp; E)` across all experiments.
* Correlation between:

  * lower tension and observed network persistence or structural richness,
  * higher tension and fragility or trivial behavior.
* Stability of `Tension_prebiotic(m_exp; E)` estimates under small, explicitly documented variations in the extraction protocol that do not change encoding keys.

**Falsification conditions**

The encoding `E` is considered misaligned and rejected if any of the following hold:

1. Experiments that clearly show long lived, structurally rich networks (according to independent criteria) systematically yield **high** `Tension_prebiotic(m_exp; E)` above a pre declared upper band, while trivial or short lived chemistry systematically yields **lower** values, without a coherent explanation in terms of mismatch definitions.

2. Small, well documented changes in the extraction protocol that preserve physical meaning cause large, uncontrolled swings in `Tension_prebiotic(m_exp; E)` without physical justification.

3. To avoid failure under 1 or 2, one must repeatedly adjust mismatch definitions, weights, or reference ensembles in ways that would require changing `EncodingKey`, `LibraryKey`, or `WeightKey`. Such behavior is treated as evidence that the original encoding `E` is not stable and must be abandoned.

**Semantics implementation note**

All observables `C_i`, `J_e`, `Sigma_net`, and `O_struct` are estimated in a hybrid representation consistent with the metadata. The details of that representation, including discretizations and statistical estimators, are part of `E` and are not specified here.

**Boundary note**

Falsifying the TU encoding `E` does **not** solve the canonical problem. This experiment can reject specific Q068 encodings but does not, by itself, establish the existence or absence of viable prebiotic networks in nature.

---

### Experiment 2: Planetary scale constraint via environmental ensembles

**Goal**
Assess whether the Q068 encoding can identify planetary environments that are compatible with low tension prebiotic networks, in a way that matches independent scientific expectations.

**Setup**

* Use geophysical and geochemical models to generate ensembles of early Earth or exoplanet surface and subsurface environments.
* For each environment, define effective environmental descriptors `Phi_env(m_env; E)` and constraints on possible chemical inventories, following a protocol fixed by `RefinementKey(E)`.

All mapping from geophysical model outputs into environmental descriptors is handled outside TU. This document only requires that the resulting observables are well defined for states in `M_reg(E)`.

**Protocol**

1. For each environment in the ensemble, define a family of hypothetical networks consistent with:

   * the allowed chemical inventory,
   * the driving patterns encoded in `Phi_env(m_env; E)`.

2. For each such network, define states `m_model in M_reg(E)` with estimated

   ```txt
   C_i(m_model; E),
   J_e(m_model; E),
   Sigma_net(m_model; E),
   O_struct(m_model; E).
   ```

3. Evaluate `Tension_prebiotic(m_model; E)` for all model states using the fixed encoding.

4. For each environment, identify whether there exist model states with

   ```txt
   Tension_prebiotic(m_model; E) <= epsilon_pre(E).
   ```

**Metrics**

* Fraction of environments in the ensemble that admit at least one low tension network state.
* Distribution of `Tension_prebiotic(m_model; E)` across environments.
* Sensitivity of conclusions to modest changes in environmental parameters within the same ensemble, without changing encoding keys.

**Falsification conditions**

The encoding `E` is considered suspect or rejected if:

1. It labels almost all plausible early Earth environments as high tension regimes with no low tension pockets, while independent origin of life arguments, supported by geochemistry and systems chemistry, strongly suggest the presence of viable prebiotic regimes.

2. It is so permissive that almost any environment is labeled as low tension without discriminating physically meaningful differences between settings that experts regard as promising and settings that experts regard as implausible.

3. Avoiding 1 or 2 requires repeated, ad hoc adjustment of mismatch definitions or weights, in a way that would change `WeightKey(E)` or `EncodingKey`. This indicates that the original encoding was not stable.

**Semantics implementation note**

The mapping from geophysical model outputs to `Phi_env` and to network parameters is handled outside TU. The Q068 description only requires that the resulting observables define coherent states in `M_reg(E)`.

**Boundary note**

Falsifying the TU encoding `E` does not determine whether Q068 has a positive or negative answer in the real universe. Planetary scale constraints can rule out particular encodings or parameter choices but cannot, by themselves, settle the canonical problem.

---

## 7. AI and WFGY engineering spec

This block describes how Q068 can be instantiated as an AI and WFGY module at the effective layer, relative to the encoding `E`.

### 7.1 Training signals

We define several training signals derived from Q068 observables.

1. **`signal_entropy_profile_alignment`**

   * Definition: a signal proportional to `DeltaS_flux(m; E)` and `Sigma_net(m; E)`, penalizing configurations where non equilibrium driving is either too weak or too strong to sustain structure.
   * Purpose: encourage the model to recognize and favor regimes where non equilibrium fluxes are compatible with organized prebiotic networks.

2. **`signal_structural_organization_score`**

   * Definition: a signal derived from `O_struct(m; E)` and `DeltaS_struct(m; E)`, rewarding internal representations that capture network motifs associated with robust prebiotic organization.
   * Purpose: bias the model toward explanations where persistent cycles, modularity, and controlled branching appear in prebiotic scenarios.

3. **`signal_robustness_margin`**

   * Definition: a signal that tracks `DeltaS_robust(m; E)` and measures how much environmental variation can be tolerated before the network collapses or loses structure.
   * Purpose: penalize narratives that rely on extremely fine tuned conditions and reward scenarios with reasonable robustness margins.

4. **`signal_prebiotic_viability_index`**

   * Definition: a scalar defined as

     ```txt
     VI(m; E) = 1 / (1 + Tension_prebiotic(m; E))
     ```

     so that `VI(m; E)` is near 1 for low tension configurations and near 0 for high tension ones.

   * Purpose: provide a compact viability score used as an auxiliary target or classifier for prebiotic scenarios.

### 7.2 Architectural patterns

1. **`PrebioticNetworkEncoder`**

   * Role: maps textual or structured descriptions of prebiotic scenarios into internal representations corresponding to states `m in M_reg(E)`.
   * Interface:

     * inputs: descriptions of species, reactions, and environmental conditions,
     * outputs: latent codes used to estimate `C_i`, `J_e`, `Sigma_net`, `O_struct`, and `Tension_prebiotic`.

2. **`NonEquilibriumTensionHead`**

   * Role: a head network that reads internal embeddings and outputs estimates of `DeltaS_struct(m; E)`, `DeltaS_flux(m; E)`, `DeltaS_robust(m; E)`, and `Tension_prebiotic(m; E)`.
   * Interface:

     * inputs: internal embeddings for the current scenario,
     * outputs: scalar or low dimensional tension components and an overall tension score.

3. **`EnvironmentFluxModule`**

   * Role: encodes environmental descriptions into `Phi_env` like latent variables, consistent with the encoding `E`.
   * Interface:

     * inputs: descriptions of planetary or laboratory environments,
     * outputs: `Phi_env` representations used both by the network encoder and the tension head.

### 7.3 Evaluation harness

1. **Task selection**

   * A curated set of benchmark questions and case studies on prebiotic chemistry, non equilibrium networks, and origins of life scenarios, for example:

     * distinguish trivial one shot reaction mixtures from persistent, network level prebiotic regimes,
     * compare two proposed scenarios in terms of organization, flux, and robustness.

2. **Conditions**

   * Baseline:

     * the model answers tasks without explicit access to Q068 modules or tension based signals.
   * TU condition:

     * the model uses `PrebioticNetworkEncoder` and `NonEquilibriumTensionHead`,
     * training incorporates `signal_prebiotic_viability_index` or related signals as auxiliary objectives.

3. **Metrics**

   * Accuracy on questions where non equilibrium and network aspects are central.
   * Internal consistency across multi step reasoning about prebiotic scenarios, as measured by alignment of narrative claims with estimated `Tension_prebiotic(m; E)`.
   * Diversity and plausibility of proposed network structures and environmental combinations, checked against external expert judgments.

### 7.4 60 second reproduction protocol

A minimal 60 second protocol for external users to probe Q068 style behavior.

* **Baseline setup**

  * Prompt: ask the AI to describe how non equilibrium conditions might support the origin of life, and to contrast “just random chemistry” with structured prebiotic networks.
  * Observation: record whether the explanation:

    * clearly distinguishes trivial chemistry from persistent networks,
    * discusses organization, flux, and robustness.

* **TU encoded setup**

  * Prompt: same theme, but explicitly instruct the AI to reason in terms of:

    * network organization,
    * entropy production and fluxes,
    * robustness under environmental variation,
    * a single viability index similar to `VI(m; E)`.

  * Observation: compare structure, clarity, and use of network level concepts between the two conditions.

* **Comparison metric**

  * Use a rubric rating:

    * explicit mention of network motifs,
    * treatment of non equilibrium driving,
    * discussion of robustness rather than fine tuning,
    * alignment between narrative claims and qualitative tension assessments.

* **What to log**

  * Prompts and full responses for both conditions.
  * If available, internal tension or viability scores estimated by Q068 modules (`Tension_prebiotic`, `VI(m; E)`).
  * These logs support later analysis of how Q068 modules influenced reasoning, without exposing any TU deep layer constructs.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. **ComponentName:** `PrebioticNetwork_TensionScore`

   * Type: functional

   * Minimal interface:

     ```txt
     inputs: network_description, environment_description, EncodingKey
     output: tension_value >= 0
     ```

   * Preconditions:

     * Inputs must be sufficient, under the encoding keyed by `EncodingKey`, to define effective `C_i`, `J_e`, `Sigma_net`, and `O_struct` without leaving `M_reg(E)`.

2. **ComponentName:** `NonEquilibriumFlux_Descriptor`

   * Type: field

   * Minimal interface:

     ```txt
     inputs: environment_description, EncodingKey
     output: Phi_env_like_descriptor
     ```

   * Preconditions:

     * Environment description must include enough information to define non equilibrium driving magnitudes and directionality at the encoding resolution.

3. **ComponentName:** `CounterfactualPrebioticWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     ```txt
     inputs: model_class_of_networks, EncodingKey
     output: (WorldT_experiment, WorldF_experiment)
     ```

   * Preconditions:

     * The model class must support generation of networks under varying environmental driving and allow estimation of `Tension_prebiotic(·; E)`.

### 8.2 Direct reuse targets

1. **Q069 (reaction selectivity rules)**

   * Reused component: `PrebioticNetwork_TensionScore`.
   * Why it transfers:

     * selectivity can be reframed as the emergence of low tension paths in a network, so the same functional helps characterize selective regimes.
   * What changes:

     * the focus shifts from long term persistence to specificity of products under competing pathways; observables are extended to include selectivity metrics.

2. **Q070 (soft matter self assembly)**

   * Reused component: `NonEquilibriumFlux_Descriptor`.
   * Why it transfers:

     * soft matter self assembly also depends on how non equilibrium driving couples to structure.
   * What changes:

     * observables are now structural motifs in soft materials rather than purely chemical reaction networks; tension functionals are adjusted but keep the same flux descriptor patterns.

3. **Q071 (origin of life)**

   * Reused component: `CounterfactualPrebioticWorld_Template`.
   * Why it transfers:

     * Q071 needs explicit World T and World F constructions for different origins of life scenarios built on prebiotic networks.
   * What changes:

     * additional observables covering information storage, replication, and heredity are added on top of the Q068 framework; new mismatch functionals measure informational organization and fidelity.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* **E_level: E1**

  * An effective layer encoding of prebiotic network tension has been specified, including:

    * state space `M(E)`,
    * observables `C_i`, `J_e`, `Phi_env`, `Sigma_net`, `O_struct`,
    * mismatch functionals `DeltaS_struct`, `DeltaS_flux`, `DeltaS_robust`,
    * combined functional `Tension_prebiotic`,
    * singular set `S_sing(E)` and regular domain `M_reg(E)`.
  * Concrete experimental patterns (Experiment 1 and Experiment 2) exist with falsification conditions for encodings in `E_PREBIO`.
  * At E1 level, no particular encoding `E` is yet validated against a broad dataset; this page documents the specification for `EncodingKey = Q068_PREBIO_CORE_V1`.

* **N_level: N1**

  * The narrative connects prebiotic networks, non equilibrium driving, and organization in a coherent way.
  * World T and World F counterfactuals are defined in terms of observable tension patterns, but have not yet been systematically compared with multiple independent origins of life models.

### 9.2 Next measurable steps toward E2

To move from E1 to E2 for Q068, at least one of the following should be implemented and documented for a concrete encoding `E` in `E_PREBIO`:

1. A software prototype that:

   * takes a structured description of a prebiotic experiment or model as input,
   * constructs states `m in M_reg(E)`,
   * computes `Tension_prebiotic(m; E)` and its components for multiple scenarios,
   * publishes results and extraction protocols as open data linked to `EncodingKey`, `LibraryKey`, `WeightKey`, and `RefinementKey`.

2. A published series of microreactor experiments explicitly designed according to the Q068 Experiment 1 template, with:

   * documented tension profiles for different driving protocols,
   * stability analyses under small changes in extraction rules,
   * explicit discussion of how the data constrain or falsify encodings in `E_PREBIO`.

### 9.3 Long term role in the TU program

In the longer term, Q068 is expected to:

* anchor all prebiotic network and non equilibrium chemistry problems in the BlackHole graph,
* provide a standard way to compare different origins of life proposals in terms of **network level thermodynamic_tension**,
* serve as a bridge between:

  * chemical S problems about reaction networks,
  * biological S problems about early metabolism and coding,
  * planetary S problems about environmental conditions and fluxes.

In this role, Q068 is not a final answer to how life began. It is a **shared language and testbed** for tension based reasoning about prebiotic chemistry, designed to be compatible with multiple scientific theories and to remain strictly at the effective layer.

---

## 10. Elementary but precise explanation

Classically, origin of life studies ask questions such as:

* What chemicals were available on early Earth?
* What reactions could happen among them?
* Could those reactions, step by step, lead to life?

Q068 takes a more **network based** view.

Imagine a large web of reactions where molecules turn into other molecules, powered by sunlight, heat, or chemical gradients. Some webs are boring: you mix things, they react once, then everything settles into a quiet mixture. Other webs might be special: they keep cycling, they reinforce certain pathways, and they build structures that last for a while.

Q068 asks, in effect:

* Can such special, self sustaining webs of reactions exist under realistic early Earth conditions?
* If they do exist, what makes them different from the boring ones?

In the Tension Universe view, and for a fixed encoding `E`, we do not try to follow every molecule. Instead, we build a coarse description of the network:

* how many molecules of each type are present on average,
* which reactions carry significant flux,
* how much “push” comes from the environment,
* how organized the reaction graph is,
* how sensitive the behavior is to small changes in conditions.

From these pieces, Q068 defines a single quantity, `Tension_prebiotic(m; E)`, that measures how “strained” or “fragile” the network is in this description.

* If `Tension_prebiotic` is low, the network looks like one that can keep going and stay organized under a range of conditions.
* If it is high, the network looks fragile, trivial, or short lived.

Q068 then invites us to imagine two kinds of worlds, always relative to the encoding `E`:

* In a **good** world, there are many ways for nature to set up low tension networks. Prebiotic chemistry often falls into regimes where organized networks appear and persist.
* In a **bad** world, almost all networks are high tension. Networks either relax to equilibrium quickly or require extreme fine tuning that is unlikely to occur naturally.

Q068 does not decide which kind of world we actually inhabit. Instead, it provides:

1. A precise way to talk about “interesting prebiotic chemistry” versus “just random reactions”, using measurable or at least estimable quantities.
2. A set of experiments and planetary models that can test whether a particular **encoding** of this idea makes sense.
3. Reusable tools that other problems, such as early metabolism or the emergence of coding, can borrow when they need to talk about network level limits and possibilities.

In that sense, Q068 is the main S level problem for turning vague ideas about “chemical soups” into a structured, testable notion of prebiotic networks under non equilibrium conditions, while remaining firmly at the effective layer.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S problem collection. It provides an **effective layer encoding** of the canonical problem “Prebiotic chemistry networks” and does not by itself claim to solve that problem in the mathematical or physical sense.

### Scope of claims

* This document:

  * specifies one encoding level view of prebiotic network tension,
  * defines observables, mismatch functionals, tension functionals, singular sets, and experiment templates,
  * proposes AI and engineering modules that reuse these constructs.

* This document does **not**:

  * prove or disprove the existence of robust prebiotic networks in nature,
  * introduce or modify TU deep layer axioms or generative rules,
  * claim any new theorem in chemistry, physics, or origins of life.

Any empirical conclusion drawn from this page is conditional on:

* the fixed encoding `E` identified by `EncodingKey`, `LibraryKey`, `WeightKey`, and `RefinementKey`,
* the specific procedures used to map data into `M_reg(E)`.

### Effective layer objects in this page

At the effective layer, for the encoding `E`, this page uses the following TU objects:

* State related:

  * `M(E)`: semantic state space of prebiotic network configurations,
  * `S_sing(E)`: singular set where key observables are undefined or not finite,
  * `M_reg(E) = M(E) \ S_sing(E)`: regular domain of analysis.

* Observables and fields:

  * `C_i(m; E)`: species abundance field,
  * `J_e(m; E)`: reaction flux field,
  * `Phi_env(m; E)`: environmental driving descriptor,
  * `Sigma_net(m; E)`: entropy production rate,
  * `O_struct(m; E)`: structural organization score.

* Mismatch and tension functionals:

  * `DeltaS_struct(m; E)`: structural mismatch,
  * `DeltaS_flux(m; E)`: flux mismatch,
  * `DeltaS_robust(m; E)`: robustness mismatch,
  * `DeltaS_pre(m; E)`: combined prebiotic mismatch,
  * `Tension_prebiotic(m; E)`: core prebiotic network tension functional.

* Tensor and coupling:

  * `T_ij(m; E)`: effective tension tensor for prebiotic networks,
  * `S_i(m; E)`, `C_j(m; E)`: source and receptivity factors,
  * `lambda(m; E)`: convergence state factor supplied by the TU core,
  * `kappa(E)`: encoding level coupling constant.

* Reusable components:

  * `PrebioticNetwork_TensionScore`,
  * `NonEquilibriumFlux_Descriptor`,
  * `CounterfactualPrebioticWorld_Template`,
  * AI heads and encoders listed in the engineering spec.

All of these objects are defined at the effective layer and are constrained by the encoding `E`. None of them expose TU deep layer structure.

### Encoding and fairness constraints

* Thresholds and weights:

  * `a_struct(E)`, `a_flux(E)`, `a_robust(E)`,
  * `epsilon_pre(E)`, `delta_pre(E)`,
    are fixed at the encoding level and do not depend on particular datasets or states.

* Reference ensembles for networks and environments are fixed prior to evaluation and are recorded by `LibraryKey(E)` and `RefinementKey(E)`.

* Any substantial change in mismatch definitions, thresholds, or reference ensembles must be tracked by updating keys and is treated as a **new encoding**, not as a retroactive modification of `E`.

* Experiments and evaluations must always log:

  * the encoding keys used,
  * the procedures for mapping data into `M_reg(E)`,
  * the definitions of observables and mismatch functionals.

### Relationship to the canonical problem

* Q068, as encoded here, provides a **language and framework** for discussing prebiotic network tension.

* It can:

  * falsify specific encodings,
  * organize evidence about particular scenarios,
  * support AI and WFGY modules that respect non equilibrium and network constraints.

* It cannot, by itself:

  * prove that prebiotic networks must exist,
  * prove that they cannot exist,
  * establish a unique physical mechanism for the origin of life.

Any stronger claim requires independent scientific evidence and is outside the scope of this effective layer page.

---

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
