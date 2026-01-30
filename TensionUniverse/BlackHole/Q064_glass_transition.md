# Q064 · Glass transition in supercooled liquids and amorphous solids

## 0. Header metadata

```txt
ID: Q064
Code: BH_CHEM_GLASS_TRANS_L3_064
Domain: Chemistry
Family: Physical chemistry / soft matter
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
EncodingKey:   Q064_GLASS_CORE_V1
LibraryKey:    Q064_GLASS_LIB_V1
WeightKey:     Q064_GLASS_WEIGHTS_V1
RefinementKey: Q064_GLASS_REFINE_V1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

The goal of this page is narrow and explicit.

* It specifies an effective layer encoding of the glass transition problem.
* It defines state spaces, observables, invariants, tension scores, and counterfactual experiment patterns.
* It provides a way to log and test encodings by keys

  ```txt
  EncodingKey   = Q064_GLASS_CORE_V1
  LibraryKey    = Q064_GLASS_LIB_V1
  WeightKey     = Q064_GLASS_WEIGHTS_V1
  RefinementKey = Q064_GLASS_REFINE_V1
  ```

Within this page:

* We do not claim to prove or disprove the canonical scientific statement in Section 1.
* We do not claim any new theorem in thermodynamics, statistical mechanics, or glass theory.
* We do not introduce or expose any TU level axiom system or deep generative rules.
* We do not specify any direct mapping from microscopic coordinates or trajectories to TU internal fields.

All TU objects in this entry live at the effective layer.

* State spaces `M`, `M_reg`, and the singular set `S_sing`.
* Observables such as `tau_alpha`, `eta`, `S_conf`, `xi_dyn`, `R_rough`, `f_cage`.
* Invariants such as `Fragility_index`, `DynamicArrestIndex`, `LandscapeComplexityIndex`.
* Tension functionals such as `Tension_glass`.
* Counterfactual worlds and experiment templates.

They are abstract devices that organize known and possible patterns of observations.
They are not claims about the unique microscopic reality of any particular material.

The encoding in use here is identified by the four keys written above.
Any material change to functional forms, constants, admissible ranges, or numerical tolerances that define this encoding must be recorded as a new key combination. It is then treated as a different encoding, not as a repaired version of the same one.

The field

```txt
Status: Open
```

in the header refers only to the canonical scientific problem described in Section 1.
It does not encode any claim that TU has solved, approximated, or partly resolved that canonical problem.

This page should be read as one S level node in a larger TU effective layer graph. It does not reveal, change, or depend on any unspoken TU bottom layer structure.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The classical glass transition problem can be stated as follows.

Consider liquids that can be cooled below their melting temperature without crystallizing. These supercooled liquids exhibit a dramatic increase in viscosity and relaxation times over a modest change in control parameters, for example temperature or density. Eventually they form amorphous solids called glasses.

The core question is:

> Is there a compact, physically grounded, and quantitatively predictive theory that explains how microscopic interactions and configurations in supercooled liquids give rise to
>
> * the enormous slowdown of dynamics
> * the emergence of rigidity without long range crystalline order
> * and the associated thermodynamic and dynamic anomalies
>
> across families of materials and control protocols, using a finite set of effective invariants and rules?

This includes questions such as:

* Is there an underlying thermodynamic phase transition, or only a dynamic crossover.
* Can a small set of structural or landscape descriptors fully account for the slowing down.
* How do dynamic heterogeneity and cooperative motion arise and scale.

This canonical question is independent of TU. It is the problem as seen in the standard physics and chemistry literature.

### 1.2 Status and difficulty

Observed facts that motivate the difficulty include the following points.

* The viscosity `eta(T)` and main structural relaxation time `tau_alpha(T)` can increase by ten or more orders of magnitude over a moderate temperature range as the system approaches a glassy state.
* Dynamic heterogeneity emerges. Different regions relax at very different rates, and cooperative rearrangements involving many molecules become important.
* The structure factor and pair correlations change only modestly, even while dynamics slow dramatically.
* Many theoretical frameworks have been proposed, including for example

  * mode coupling type formalisms
  * energy landscape and inherent structure pictures
  * random first order transition type scenarios
  * dynamic facilitation and kinetically constrained models.

Despite major progress there is no universally accepted compact theory that yields a small set of invariants and rules which

* describe the onset of dynamic arrest
* unify different classes of glass formers such as molecular, polymer, colloidal
* and predict key observables across protocols without extensive case by case fitting.

In the BlackHole collection we record this situation as

```txt
Status: Open
Rank:   S
```

This is purely about the canonical problem.
It does not say anything about the strength or weakness of any TU encoding.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem set, Q064 plays three main roles at the effective layer.

1. It is a flagship example of a thermodynamic tension problem in soft condensed matter, where thermodynamic quantities, dynamic observables, and emergent rigidity must be held together inside a single coherent description.

2. It is a test bed for the idea that a rugged high dimensional energy landscape can be summarized by a finite set of landscape complexity and fragility invariants, combined with a small number of dynamic arrest indicators.

3. It acts as a bridge node between other S problems, for example

   * microscopic chemistry and bonding (Q061)
   * general non equilibrium thermodynamics (Q032)
   * biological or AI systems that may exhibit glass like dynamic arrest (for example Q071, Q121, Q123).

All of this is stated strictly at the level of effective layer nodes and edges.
No claim is made that these roles correspond to a unique or complete microscopic understanding of glass formation.

---

## 2. Position in the BlackHole graph

This block records how Q064 sits inside the BlackHole graph.
Each edge is an effective layer relation, with a one line reason that points to a concrete component, invariant, or tension type.

### 2.1 Upstream problems

These nodes provide prerequisites or general tools for Q064 at the effective layer.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Supplies the general thermodynamic tension framework for non equilibrium relaxation and slow dynamics that Q064 uses to interpret glassy behavior.

* Q061 (BH_CHEM_BOND_NATURE_L3_061)
  Reason: Provides an effective description of bonding and strong correlations. Q064 relies on this to justify coarse grained interaction models for glass forming liquids and solids.

* Q067 (BH_CHEM_QUANTUM_MOL_SIM_L3_067)
  Reason: Constrains what can in practice be computed from microscopic simulations. This bounds how directly landscape and dynamics can be resolved in Q064 encodings.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: Gives general soft matter organization principles. Q064 specializes these to the amorphous, dynamically arrested regime.

### 2.2 Downstream problems

These nodes reuse Q064 effective layer components or depend on its tension structure.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: Reuses the `GlassEnergyLandscapeDescriptor` component from Section 8 to classify soft matter phases and transitions between fluid, gel, and glassy states.

* Q071 (BH_BIO_ORIGIN_LIFE_L3_071)
  Reason: Uses the `DynamicHeterogeneityIndex` observable to bound prebiotic environments where reaction and diffusion rates are controlled by amorphous matrices.

* Q080 (BH_BIO_BIOSPHERE_LIMITS_L3_080)
  Reason: Reuses glassy arrest indicators, including the `DynamicArrestIndex` invariant, to discuss how dynamic slowdowns in cells and tissues can constrain biosphere level adaptability.

### 2.3 Parallel problems

Parallel nodes share similar tension structures but do not depend on Q064 components by construction.

* Q063 (BH_CHEM_PROTEIN_FOLDING_L3_063)
  Reason: Both Q063 and Q064 deal with rugged landscapes and strong sensitivity of dynamics to shallow thermodynamic changes, though in different physical systems.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: Both problems focus on soft matter systems where emergent rigidity and slow dynamics arise from many body interactions, with different geometric constraints and observables.

* Q077 (BH_BIO_MICROBIOME_L3_077)
  Reason: Both Q064 and Q077 involve many interacting units on a high dimensional landscape where metastability and slow relaxation are central themes.

### 2.4 Cross domain edges

Cross domain edges capture effective layer reuse outside chemistry.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Reuses glassy relaxation invariants as concrete examples of extreme non equilibrium thermodynamic behavior.

* Q095 (BH_EARTH_BIODIVERSITY_L3_095)
  Reason: Uses amorphous state and dynamic arrest ideas as microscopic mechanisms that affect ecological timescales and niche persistence.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Uses the `DynamicArrestIndex` invariant as an analogy for pathological trapping in AI objective landscapes and policy spaces.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Reuses the `GlassEnergyLandscapeDescriptor` as a template for describing slow modes and metastable regions in AI representation spaces.

All edges here describe reuse or analogy at the effective layer only.
They do not assert that the underlying microscopic physics or algorithms are identical across the linked problems.

---

## 3. Tension Universe encoding (effective layer)

This block defines the Q064 encoding strictly at the effective layer, for a single fixed encoding identified by

```txt
EncodingKey   = Q064_GLASS_CORE_V1
LibraryKey    = Q064_GLASS_LIB_V1
WeightKey     = Q064_GLASS_WEIGHTS_V1
RefinementKey = Q064_GLASS_REFINE_V1
```

We specify:

* state space
* observables and fields
* invariants and tension scores
* singular sets and domain restrictions
* fairness constraints tied to these keys.

We do not describe any deep TU generative rule, and we do not specify how raw data are mapped to TU fields.

### 3.1 State space

We assume a state space

```txt
M
```

with the following interpretation.

* Each element `m` in `M` represents a coherent glass forming configuration at the effective layer. It is specified by

  * material type, for example molecular liquid, polymer melt, colloidal suspension
  * interaction class, for example strong directional bonding versus nearly isotropic
  * control parameters such as temperature, pressure, density, composition, cooling rate
  * regime label such as equilibrium liquid, deeply supercooled, near glass transition, glassy solid.

* For each `m` we assume the existence of finite, well defined summaries of

  * structural information at some chosen coarse graining scale
  * potential energy landscape statistics at that scale
  * dynamic relaxation time distributions under the chosen protocol.

We do not specify how these summaries are constructed from microscopic coordinates or trajectories. We only assume that for each regime and protocol of interest there exist states `m` with consistent summaries.

We define the regular subset

```txt
M_reg subset of M
```

as the set of states for which all observables and invariants defined below are finite and well defined.
The singular set `S_sing` is defined in Section 3.5 and is key dependent.

### 3.2 Observables and effective fields

On `M_reg` we introduce the following effective layer observables.

1. Structural relaxation time

```txt
tau_alpha(m) > 0
```

Main structural relaxation time or a closely related timescale, measured under the protocol encoded in `m`.

2. Viscosity or effective viscosity like quantity

```txt
eta(m) > 0
```

Effective viscosity or equivalent measure of resistance to flow for the state `m`.

3. Configurational entropy proxy

```txt
S_conf(m)
```

A scalar summarizing the effective number of distinct amorphous basins that are relevant at the control parameters of `m`.
We only assume that `S_conf(m)` is finite and monotone with respect to effective landscape complexity in the regime considered.

4. Dynamic heterogeneity length scale

```txt
xi_dyn(m) >= 0
```

A characteristic length associated with spatial correlations in relaxation dynamics.

5. Landscape roughness index

```txt
R_rough(m) >= 0
```

A scalar that summarizes the spread and height of energy barriers between relevant amorphous basins at the chosen coarse graining.

6. Caged fraction

```txt
f_cage(m) in [0, 1]
```

Fraction of regions or particles that are effectively trapped on the timescale `tau_alpha(m)`.

7. Protocol label field

```txt
Prot(m)
```

A discrete label for the preparation or measurement protocol, for example slow cooling, fast quench, isothermal aging.
This label is used only to group states and is not a continuous observable.

Each observable above is an effective map from `M_reg` to real numbers or a small discrete set.
The hybrid field type of Q064 arises from the combination of continuous valued observables with discrete protocol labels.

### 3.3 Invariants and effective constraints

From the observables we define effective layer invariants. Their detailed functional forms and constants are part of the library and weight specifications tied to the four keys in the header.

1. Fragility index

```txt
Fragility_index(m)
```

An index that summarizes how sharply `tau_alpha(m)` grows as the control parameter approaches the glassy regime.
In a concrete implementation, the fragility index can be derived from fits of the form

```txt
tau_alpha(T) ~ exp( A / ( T - T0 ) )
```

or similar relations. The choice of fit family and parameter interpretation is fixed at the encoding class level, as part of `LibraryKey` and `WeightKey`, not per material.

2. Dynamic arrest index

```txt
DynamicArrestIndex(m)
```

A scalar that combines relaxation time, viscosity, and caging into a single measure of arrest. One possible family of constructions is

```txt
DynamicArrestIndex(m) =
  c1 * log10( tau_alpha(m) / tau_ref )
  + c2 * log10( eta(m) / eta_ref )
  + c3 * f_cage(m)
```

where constants `c1`, `c2`, `c3`, `tau_ref`, `eta_ref` are fixed once for the encoding with keys

```txt
LibraryKey    = Q064_GLASS_LIB_V1
WeightKey     = Q064_GLASS_WEIGHTS_V1
RefinementKey = Q064_GLASS_REFINE_V1
```

They are not tuned per material.

3. Landscape complexity index

```txt
LandscapeComplexityIndex(m)
```

A scalar that summarizes how crowded and rough the relevant part of the landscape is. For example

```txt
LandscapeComplexityIndex(m) =
  d1 * S_conf(m) + d2 * R_rough(m)
```

where constants `d1` and `d2` are again fixed globally by the same keys.

In all cases, these invariants are required to be stable under modest changes in coarse graining and data quality, within explicit tolerance bands defined in the library and refinement specifications for the chosen key combination.

### 3.4 Encoding class and fairness constraints

To prevent post hoc tuning and to make tension measures falsifiable, we restrict attention to an admissible encoding class `E_glass`.

Each encoding `E` in `E_glass` specifies the following items.

* The functional forms used to extract `Fragility_index`, `DynamicArrestIndex`, and `LandscapeComplexityIndex` from raw observable summaries.
* The global constants and reference values such as `c1`, `c2`, `c3`, `d1`, `d2`, `tau_ref`, `eta_ref`, `Fragility_ref(Class)`, `LCI_ref(Class)`.
* The allowed tolerances for coarse graining and numerical errors.
* The specific ranges of control parameters in which the encoding is declared valid.

In this page we fix a single encoding

```txt
E = E_glass(Q064_GLASS_CORE_V1,
            Q064_GLASS_LIB_V1,
            Q064_GLASS_WEIGHTS_V1,
            Q064_GLASS_REFINE_V1)
```

and all constructions are to be read as relative to this encoding.
Any material change to the items listed above must be recorded as a new key combination and treated as a different encoding, not as a repaired version of `E`.

Under a fixed encoding `E` we impose fairness constraints.

* All functional forms, constants, and reference maps must be chosen before looking in detail at the specific material data sets that will later be used for evaluation.
* The same encoding `E` must be applied to all materials and protocols in any given study.
* If the encoding is modified after inspecting specific data in order to improve apparent agreement, the modified version is counted as a new element in `E_glass` and must be re tested on the full suite of systems.

These rules are enforced at the level of the four keys in the header.
They give falsifiable content to any statement that uses Q064 invariants or tension scores.

### 3.5 Singular set and domain restriction

For the fixed encoding `E` described above we define a singular set

```txt
S_sing(E) = { m in M :
              tau_alpha(m), eta(m), S_conf(m), xi_dyn(m),
              R_rough(m), or f_cage(m)
              are undefined, inconsistent, or non finite
              in this encoding }
```

and the regular domain

```txt
M_reg(E) = M \ S_sing(E)
```

All glass tension functionals introduced later are defined only on `M_reg(E)`.

If experiments or models produce states that map into `S_sing(E)`, the result is treated as an out of domain event for this encoding.
It is not treated as evidence for extreme but finite tension values.

Different key combinations in `E_glass` can induce different singular sets.
This means that domain coverage is an empirical property of each encoding, and can be compared across encodings at the effective layer.

---

## 4. Tension principle for this problem

This block defines how Q064 is framed as a tension problem at the effective layer, again for the fixed encoding identified by the keys in the header.

### 4.1 Core tension functional

For the encoding `E` we define a glass tension functional on `M_reg(E)`.

```txt
Tension_glass(m) =
  b1 * DeltaS_relax(m) +
  b2 * DeltaS_structure(m)
```

where:

* `b1 > 0` and `b2 > 0` are global constants fixed once for the encoding, recorded under `WeightKey`.
* `DeltaS_relax(m)` measures mismatch between observed relaxation scaling and a chosen reference scaling law for the class of materials.
* `DeltaS_structure(m)` measures mismatch between structural or landscape observables and a reference pattern expected for a compact glass theory.

One simple family of constructions that is compatible with this view is as follows.

```txt
DeltaS_relax(m) =
  | Fragility_index(m) - Fragility_ref(Class(m)) |

DeltaS_structure(m) =
  | LandscapeComplexityIndex(m) - LCI_ref(Class(m)) |
```

where:

* `Fragility_ref(Class(m))` is a reference fragility value for the material class of `m`.
* `LCI_ref(Class(m))` is a reference landscape complexity value for that class.

The maps `Fragility_ref` and `LCI_ref` are part of the library specification for the encoding and are fixed once per key combination.
They cannot be chosen separately for each material.

By construction one has

```txt
Tension_glass(m) >= 0
```

for all `m` in `M_reg(E)`.
Small tension corresponds to systems where both dynamic and structural invariants lie near the reference values for their class under the chosen encoding.

The function `Tension_glass` is therefore a key dependent effective layer tool.
Changing the encoding keys in the header changes the function itself, not only its numerical values.

### 4.2 Low tension principle for compact glass theory

At the effective layer a compact theory of the glass transition corresponds to the following principle.

> For a wide range of glass forming systems and protocols there exists an encoding `E` in `E_glass` and states `m` in `M_reg(E)` representing those systems such that
>
> * `Tension_glass(m)` lies in a low tension band
> * the band does not blow up as data quality improves or as more systems are added
>
> when everything is evaluated with the fixed encoding keys of `E`.

Formally there exists an encoding `E` and constants `epsilon_glass > 0` and `K >= 1` such that for all systems within the declared scope of `E`,

```txt
Tension_glass(m_data) <= epsilon_glass
```

up to a factor `K` that accounts for controlled experimental and numerical uncertainties.

If such an encoding exists and is stable across many systems, one can say that the glass transition behaves in a compact way at the effective layer under that encoding.
The statement is conditional on the encoding keys and remains purely at the level of observables and invariants.

### 4.3 High tension failure for non compact scenarios

If no compact theory exists within the constraints of `E_glass` under the key based fairness rules, then we expect a different pattern.

> For every encoding `E` in `E_glass` and for any candidate bound `epsilon_glass`, there exist glass forming systems within the declared scope of `E` whose faithful states `m` in `M_reg(E)` satisfy
>
> * `Tension_glass(m)` is bounded below by a strictly positive value that does not go away under refinement
>
> when evaluated with the keys that define `E`.

Concretely, for each encoding `E` in `E_glass` there would exist a positive number `delta_glass(E)` such that for some systems

```txt
Tension_glass(m_data) >= delta_glass(E)
```

and this inequality persists when

* more accurate data are used
* reasonable coarse graining changes are applied
* protocol labels remain within the declared scope for `E`.

These statements speak only about patterns of effective layer invariants and how they behave under a fixed encoding.
They do not assert or deny any particular microscopic mechanism for glass formation.

---

## 5. Counterfactual tension worlds

We now consider two counterfactual worlds described purely at the level of observables, invariants, and tension scores, for the fixed encoding `E`.

* World T: a compact glass theory world with low thermodynamic tension.
* World F: a non compact world where glass behavior resists compression and exhibits persistent high tension.

These worlds are devices for thinking about patterns.
They do not invoke or reveal any TU axioms or deep generative rules.

### 5.1 World T (compact glass theory, low tension)

In World T, for the encoding `E` fixed by our keys:

1. Coherent scaling of relaxation and viscosity

   The relation between `tau_alpha(m)`, `eta(m)`, and control parameters can be expressed by a small family of scaling forms whose parameters are tied to `Fragility_index(m)`.
   For most materials in the scope of `E` the observed data lie close to these forms, so `DeltaS_relax(m)` remains small.

2. Controlled landscape complexity

   The pair `S_conf(m)` and `R_rough(m)` combines into `LandscapeComplexityIndex(m)` values that cluster around class dependent reference values `LCI_ref(Class(m))`.
   The scaling of `LandscapeComplexityIndex(m)` as control parameters change remains predictable within the declared tolerance bands.

3. Dynamic heterogeneity aligned with invariants

   The fields `xi_dyn(m)` and `f_cage(m)` correlate with `DynamicArrestIndex(m)` in a way that can be captured by a small set of relations.
   No large population of systems shows strong violations of these relations within the declared scope.

4. Overall low glass tension

   For most relevant states `m_T` that represent real systems one has

   ```txt
   Tension_glass(m_T) <= epsilon_glass
   ```

   with `epsilon_glass` stable as more systems are added and as measurements improve.

### 5.2 World F (non compact glass behavior, high tension)

In World F, for every encoding `E` in `E_glass` that respects the key based fairness constraints:

1. Wide variation in relaxation patterns

   Different glass formers exhibit scaling of `tau_alpha(T)` and `eta(T)` that cannot be captured by any small family of forms with parameters tied to `Fragility_index`.
   Clusters of materials that look similar structurally display very different dynamic slowdowns.

2. Uncompressible landscape diversity

   The pair `S_conf(m)` and `R_rough(m)` produces `LandscapeComplexityIndex(m)` values that are broadly scattered.
   Attempts to define `LCI_ref(Class(m))` with small residuals fail. Large systematic deviations appear regardless of the details of the encoding.

3. Irregular dynamic heterogeneity

   The fields `xi_dyn(m)` and `f_cage(m)` do not correlate in a clean way with `DynamicArrestIndex(m)` across systems.
   Systems with similar `DynamicArrestIndex` display very different heterogeneity patterns.

4. Persistent high glass tension

   For some states `m_F` that represent real systems in the declared scope of `E` one has

   ```txt
   Tension_glass(m_F) >= delta_glass(E)
   ```

   with `delta_glass(E) > 0`, and this lower bound does not vanish as the encoding is refined within its allowed bands.

### 5.3 Interpretive note

These counterfactual worlds do not claim any specific microscopic mechanism.
They only describe how patterns of observables and invariants differ, depending on whether a compact effective theory exists under the encoding constraints.

They also do not modify, assume, or reveal any TU level axiom system.
They are tools for thinking about what different data patterns would mean for a key based encoding.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can falsify or support particular encodings `E` in `E_glass` for Q064, without proving or disproving any microscopic theory.

In this page the default encoding is the one identified by

```txt
EncodingKey   = Q064_GLASS_CORE_V1
LibraryKey    = Q064_GLASS_LIB_V1
WeightKey     = Q064_GLASS_WEIGHTS_V1
RefinementKey = Q064_GLASS_REFINE_V1
```

Any post hoc change of functional forms, constants, reference maps, or tolerances that define `E` must be recorded as a new key combination and treated as a different encoding.

### Experiment 1: Multi material glass tension profiling

*Goal*

Test whether there exists an encoding `E` in `E_glass` such that a diverse set of glass formers exhibit low and clustered values of `Tension_glass(m)` under fixed parameters and fixed keys.

*Setup*

* Select a representative set of materials

  * molecular glass formers
  * polymer glasses
  * colloidal glasses.
* For each material, collect published data or simulations that provide

  * `tau_alpha(T)` or equivalent relaxation times
  * `eta(T)` or viscosities
  * estimates or proxies for `S_conf(T)`
  * measures of dynamic heterogeneity such as four point correlations or related indicators.

*Encoding choice*

* Fix a single encoding `E` with keys

  ```txt
  EncodingKey   = Q064_GLASS_CORE_V1
  LibraryKey    = Q064_GLASS_LIB_V1
  WeightKey     = Q064_GLASS_WEIGHTS_V1
  RefinementKey = Q064_GLASS_REFINE_V1
  ```

  before inspecting the detailed data of the test materials.

*Protocol*

1. Using only prior knowledge that is allowed by the constitution, specify the functional forms, constants, and reference maps in `E`. Record them under the chosen keys.

2. For each material and control parameter range construct an effective state `m_data` in `M_reg(E)` that summarizes the observables.

3. Compute invariants and the tension

   ```txt
   Fragility_index(m_data)
   DynamicArrestIndex(m_data)
   LandscapeComplexityIndex(m_data)
   Tension_glass(m_data)
   ```

4. Analyze the distribution of `Tension_glass(m_data)` values across all materials and conditions.

*Metrics*

* Histogram or distribution summary of `Tension_glass(m_data)` across the material set.
* Spread of `Tension_glass` values within each material class and across classes.
* Correlation between `Tension_glass` and intuitive indicators of glassy behavior strength.

*Falsification conditions*

* If for the chosen encoding `E` there is no finite `epsilon_glass` such that a large majority of systems fall into `Tension_glass(m_data) <= epsilon_glass` with modest spread, the encoding `E` is considered falsified as a candidate compact description.

* If small changes of the encoding parameters within their declared tolerance bands lead to arbitrarily different tension distributions, the encoding is considered unstable and rejected.

Any change of functional forms, constants, or reference maps beyond the declared bands defines a new encoding and requires a fresh evaluation under new keys.

*Semantics implementation note*

Hybrid field type is used. Continuous observables (`tau_alpha`, `eta`, `S_conf`, `xi_dyn`, `R_rough`, `f_cage`) are treated as real valued functions on `M_reg(E)`, while material and protocol types are discrete labels. All computations are performed in this mixed but well defined framework.

*Boundary note*

Falsifying a TU encoding under fixed keys is not the same as solving the canonical problem.
This experiment can rule out specific glass tension encodings, but it does not by itself prove or disprove the existence of a compact microscopic theory.

---

### Experiment 2: Protocol and composition perturbation tests

*Goal*

Check whether `Tension_glass(m)` changes in a way that is consistent with observed changes in dynamic arrest when protocols or compositions are varied, under a fixed encoding with fixed keys.

*Setup*

* Select one or more glass forming systems for which systematic data exist under

  * different cooling rates
  * different pressures or densities
  * small compositional changes, for example binary mixtures with varied composition.
* For each condition obtain

  * `tau_alpha`
  * `eta`
  * estimates of `S_conf` and `xi_dyn`
  * caged fraction `f_cage`.

*Encoding choice*

* Use the same encoding `E` with keys

  ```txt
  EncodingKey   = Q064_GLASS_CORE_V1
  LibraryKey    = Q064_GLASS_LIB_V1
  WeightKey     = Q064_GLASS_WEIGHTS_V1
  RefinementKey = Q064_GLASS_REFINE_V1
  ```

  as in Experiment 1. Do not modify these keys after inspecting the perturbation data.

*Protocol*

1. For each condition, construct states `m_cond` in `M_reg(E)`.

2. Compute invariants

   ```txt
   Fragility_index(m_cond)
   DynamicArrestIndex(m_cond)
   LandscapeComplexityIndex(m_cond)
   Tension_glass(m_cond)
   ```

3. Compare changes in `Tension_glass(m_cond)` between conditions with changes in

   * `tau_alpha(m_cond)`
   * `eta(m_cond)`
   * `xi_dyn(m_cond)`
   * `f_cage(m_cond)`.

*Metrics*

* Direction and magnitude of changes in `Tension_glass` when

  * cooling rate is decreased or increased
  * pressure is increased at fixed temperature
  * composition is varied.

* Consistency between increased dynamic arrest and increased `Tension_glass`.

*Falsification conditions*

* If across multiple systems and perturbations the encoding predicts decreasing `Tension_glass` when dynamic arrest is clearly increasing, or no consistent trend while observables show clear systematic changes, then the encoding is considered misaligned and rejected.

*Semantics implementation note*

The hybrid field type is again used. Protocol changes are represented by changes in discrete labels and continuous control parameters, while observables are continuous. No deeper mapping from microscopic dynamics to TU fields is specified.

*Boundary note*

Falsifying or supporting a TU encoding in this sense does not address the canonical question of whether there is a unique microscopic mechanism for the glass transition.
It only evaluates how well one fixed effective layer encoding tracks observed patterns under perturbations.

---

## 7. AI and WFGY engineering spec

This block describes how Q064 can be used as an engineering module for AI systems in WFGY, strictly at the effective layer.

All modules in this section read and write only effective layer observables, invariants, and tension scores derived from the Q064 encoding with the keys in the header. They do not access, assume, or reveal any TU deep generative rule.

### 7.1 Training signals

We define several training signals derived from the glass encoding.

1. `signal_glass_relaxation_scaling`

   * Definition: a loss term proportional to `DeltaS_relax(m)` for internal states that represent glass forming systems.
   * Use: penalizes internal representations that imply relaxation patterns incompatible with the chosen compact scaling forms under the assumed conditions and keys.

2. `signal_dynamic_heterogeneity`

   * Definition: a loss term based on the difference between inferred dynamic heterogeneity indicators from internal representations and target patterns mapped to `xi_dyn` and `f_cage`.
   * Use: encourages the model to keep track of which regions are fast or slow in a way that matches known glassy behavior.

3. `signal_glass_tension_score`

   * Definition: a scalar auxiliary prediction target equal to `Tension_glass(m)` as computed from encoded invariants.
   * Use: gives the model a continuous knob that measures how close a scenario is to dynamic arrest under the given encoding.

4. `signal_counterfactual_glass_consistency`

   * Definition: a consistency signal that compares the model’s answers when prompted under

     * a World T assumption
     * a World F assumption

     and penalizes mixing of these assumptions in a single reasoning chain.
   * Use: helps the model keep different high level hypotheses about the glass transition separate at the effective layer.

### 7.2 Architectural patterns

We outline module patterns that reuse Q064 components.

1. `GlassTensionHead`

   * Role: given an internal representation of a glass related context, predict

     * `Fragility_index`
     * `DynamicArrestIndex`
     * `LandscapeComplexityIndex`
     * `Tension_glass`.

   * Interface:

     * Input: an embedding that summarizes the problem context, including material, protocol, and observables.
     * Output: a small vector of invariant estimates plus a scalar tension.

2. `ConfigEntropyObserver`

   * Role: map internal representations to an effective `S_conf` and to coarse measures of landscape roughness.

   * Interface:

     * Input: internal states that capture structural descriptions.
     * Output: a pair `(S_conf_hat, R_rough_hat)` that can be fed into invariant computations.

3. `HeterogeneityFilter`

   * Role: interpret internal descriptions of glassy systems in space and time and extract a `DynamicHeterogeneityIndex` compatible with `xi_dyn` and `f_cage`.

   * Interface:

     * Input: sequences or grids of local state embeddings.
     * Output: a scalar or short vector that characterizes heterogeneity patterns.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models that are augmented with Q064 modules.

1. Task suite

   * Questions and design tasks about

     * explaining glass transition phenomena
     * predicting qualitative effects of protocol changes
     * comparing different glass formers
     * suggesting experimental or simulation probes.

2. Conditions

   * Baseline

     * A model without explicit Q064 modules.

   * TU augmented

     * The same base model with

       * `GlassTensionHead`
       * `ConfigEntropyObserver`
       * `HeterogeneityFilter`
       * training signals defined above.

3. Metrics

   * Accuracy on factual and explanatory questions about glassy dynamics.

   * Internal consistency

     * how often predictions about relaxation and heterogeneity agree across prompts that describe the same physical situation.

   * Stability of reasoning

     * whether answers remain consistent when the prompt is rephrased but the encoded invariants should be unchanged.

### 7.4 60 second reproduction protocol

This is a minimal user facing protocol to test whether the encoding improves structured reasoning at the effective layer.

*Baseline setup*

* Prompt the model with
  `Explain what the glass transition is and why dynamics slow down in supercooled liquids.`

* Observe

  * whether the answer is fragmented
  * whether it mixes incompatible pictures in an uncontrolled way
  * whether it ignores dynamic heterogeneity or treats it only as noise.

*TU encoded setup*

* Prompt the same model with
  `Explain what the glass transition is and why dynamics slow down in supercooled liquids. Organize your explanation using configurational entropy, relaxation time scaling, dynamic heterogeneity, and an effective glass tension that measures mismatch between dynamics and structure.`

* Observe

  * whether the explanation becomes more structured
  * whether it links observables to a clear notion of dynamic arrest
  * whether it acknowledges unresolved aspects without confusion.

*Comparison metric*

* A rubric that scores

  * clarity of structure
  * explicit linking of structure and dynamics
  * internal consistency about how arrest emerges.

*What to log*

* Prompts, responses, and any auxiliary tension scores from `GlassTensionHead`.
* Keys used for the encoding during the test.

This protocol does not produce or test any microscopic theory. It only checks whether the Q064 encoding, under explicit keys, improves the organization of reasoning at the effective layer.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q064 and their direct reuse targets, all at the effective layer.

### 8.1 Reusable components produced by this problem

1. ComponentName: `GlassEnergyLandscapeDescriptor`

   * Type: field

   * Minimal interface:

     * Inputs:

       * summaries of basin depths and barrier heights
       * control parameters such as temperature and density.

     * Output:

       * a feature vector that contains at least

         * `Fragility_index`
         * `LandscapeComplexityIndex`
         * additional optional landscape features defined in the library for Q064.

   * Preconditions:

     * The system is in a regime where an effective landscape description is meaningful and observables are well defined, that is `m` lies in `M_reg(E)`.

2. ComponentName: `DynamicHeterogeneityIndex`

   * Type: observable

   * Minimal interface:

     * Inputs:

       * local relaxation patterns or equivalent internal representations.

     * Output:

       * a scalar or short vector that summarizes the strength and length scale of dynamic heterogeneity, consistent with `xi_dyn` and `f_cage`.

   * Preconditions:

     * The underlying data allow extraction of local relaxation statistics or correlators.

3. ComponentName: `DynamicArrestInvariantFamily`

   * Type: invariant family

   * Minimal interface:

     * Inputs:

       * `tau_alpha`, `eta`, `f_cage` or their surrogates.

     * Output:

       * a value of `DynamicArrestIndex(m)` plus optional derived indices that separate time scale and viscosity contributions.

   * Preconditions:

     * The encoding keys are fixed and valid for the domain of interest.

4. ComponentName: `CounterfactualGlassWorld_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs:

       * specification of a class of glass forming systems and protocols
       * an encoding `E` in `E_glass` with explicit keys.

     * Output:

       * two experiment designs

         * a World T style evaluation that assumes compact behavior
         * a World F style evaluation that assumes non compact behavior

       each with a procedure to compute distributions of `Tension_glass`.

   * Preconditions:

     * Sufficient data or model access to estimate invariants and tension in both scenarios.

### 8.2 Direct reuse targets

1. Q070 (BH_CHEM_SOFTMATTER_L3_070)

   * Reused component:

     * `GlassEnergyLandscapeDescriptor`.

   * Why it transfers:

     * soft matter self assembly problems can be framed with similar landscape descriptors even when the final states are gels or ordered structures rather than glasses.

   * What changes:

     * the interpretation of invariants shifts from dynamic arrest to pathway selection and phase competition.

2. Q071 (BH_BIO_ORIGIN_LIFE_L3_071)

   * Reused component:

     * `DynamicHeterogeneityIndex`.

   * Why it transfers:

     * prebiotic chemistry in crowded or amorphous environments experiences glass like dynamic constraints, which can be summarized by the same heterogeneity indices.

   * What changes:

     * observables relate to reaction networks and diffusion limits rather than purely physical relaxation.

3. Q123 (BH_AI_INTERP_L3_123)

   * Reused components:

     * `GlassEnergyLandscapeDescriptor`
     * `DynamicArrestInvariantFamily`
     * `CounterfactualGlassWorld_Template`.

   * Why it transfers:

     * representation spaces in AI models can exhibit rugged landscapes and slow modes that are analogous, at the effective layer, to glassy systems.

   * What changes:

     * physical control parameters are replaced by training and architecture parameters, and tension measures relate to learning dynamics and generalization rather than viscosity.

All transfers described here operate purely at the effective layer, and do not assert any microscopic equivalence between the systems involved.

---

## 9. TU roadmap and verification levels

This block explains Q064’s position in the TU verification ladder and the next measurable steps, consistent with the labels

```txt
E_level = E1
N_level = N1
```

in the header metadata.

These levels are internal to the TU program.
They do not correspond to any claim about having solved or nearly solved the canonical glass transition problem.

### 9.1 Current levels

* E_level: E1

  * A coherent effective layer encoding for glassy systems has been specified for the key combination in the header.

    * state space
    * observables
    * invariants
    * singular set
    * tension functional.

  * Discriminating experiments are defined at the level of observables and encodings, not microscopic theories.

* N_level: N1

  * The narrative that links rugged landscapes, dynamic arrest, and thermodynamic tension is explicit at the effective layer.
  * Counterfactual worlds and cross domain connections are stated, but not yet systematically instantiated in shared datasets.

### 9.2 Next measurable step toward E2

To reach E2 at this node, at least one of the following should be implemented and documented for the encoding identified by

```txt
EncodingKey   = Q064_GLASS_CORE_V1
LibraryKey    = Q064_GLASS_LIB_V1
WeightKey     = Q064_GLASS_WEIGHTS_V1
RefinementKey = Q064_GLASS_REFINE_V1
```

1. Data based prototype

   * Build a prototype tool that

     * ingests published data on `tau_alpha`, `eta`, `S_conf`, `xi_dyn`, and `f_cage` for several glass formers
     * constructs states `m_data` for the fixed encoding `E`
     * computes `Fragility_index`, `DynamicArrestIndex`, `LandscapeComplexityIndex`, and `Tension_glass`
     * publishes the resulting tension profiles and distributions as an open data set tied to the same keys.

2. Model world study

   * Construct model glass forming systems, for example Lennard Jones mixtures, under different protocols and

     * apply the encoding `E` to simulation outputs
     * compare experiment like and simulation based tension profiles
     * test stability of results under coarse graining changes.

Both steps operate entirely at the effective layer.
Success or failure of particular encodings is recorded without any claim about microscopic uniqueness.

### 9.3 Long term role in the TU program

Long term, Q064 is expected to serve as

* the reference S level node for thermodynamic tension problems in soft condensed matter
* a template for how to encode rugged landscape and dynamic arrest phenomena without revealing deep TU generative rules
* a bridge from physical glassiness to

  * biological crowding and aging
  * AI training and representation pathologies
  * other non equilibrium systems where dynamic arrest appears.

---

## 10. Elementary but precise explanation

This block provides a non technical explanation aligned with the effective layer description.

In everyday terms, the glass transition is about how a liquid can become so sluggish that it behaves like a solid, even though its atoms or molecules never line up into a crystal.

As such a liquid is cooled or compressed, its viscosity and relaxation times can increase by many orders of magnitude. Motion slows down enormously. Yet if you look only at simple structural measures, the system still looks like a disordered liquid, not like a crystal.

In the Tension Universe view we do not try to explain every microscopic detail. Instead we ask two main questions.

* Can we describe glass forming systems using a small number of effective quantities that capture

  * how fast they relax
  * how crowded their energy landscape is
  * how uneven their local dynamics are.

* Can we combine these into a single number, a glass tension, that

  * is small when structure and dynamics fit together in a simple way
  * becomes large when they do not.

We imagine assigning to each material and protocol a state that stores

* its typical relaxation time and viscosity
* a measure of how many distinct disordered configurations matter
* a measure of how rough the energy landscape is
* a measure of how patchy and unequal the local motion is.

From these we build invariants such as

* a fragility index
* a dynamic arrest index
* a landscape complexity index.

Then we define a glass tension that grows when

* relaxation behavior does not match the expected patterns for a given class
* or when landscape and heterogeneity indicators are out of line with those patterns.

In a world where a compact glass theory exists, we should be able to choose one reasonable encoding, with explicit keys, so that many different glass formers end up with similar low glass tension.
In a world where no such theory exists, any fixed encoding will see some systems with stubbornly high glass tension, and this pattern will not vanish as data improve.

Q064 does not claim to solve the glass transition.
It organizes what is known and unknown into an effective layer language of observables, invariants, and tension, and provides ways to test and compare encodings under clear keys and fairness rules. This is its role as a BlackHole S level problem in the Tension Universe framework.

---

## Tension Universe effective-layer footer

This page is part of the WFGY / Tension Universe S problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the named problem and to define key based experiments on that encoding.
* It does not claim to prove or disprove the canonical scientific statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem in mathematics, physics, chemistry, biology, AI, or any other field has been solved.

### Effective-layer boundary

* All objects in this page are effective layer constructs. This includes

  * state spaces `M`, `M_reg`, and singular sets `S_sing`
  * observables, invariants, and tension scores
  * counterfactual worlds and experiment templates
  * engineering modules and training signals.

* No raw data to TU field mapping is specified or assumed here.
  Any such mapping, if it exists, is external to this page.

### Encoding keys and fairness

* Every concrete Q064 encoding is identified by a key combination

  ```txt
  EncodingKey
  LibraryKey
  WeightKey
  RefinementKey
  ```

* All invariants and tension scores in this page are to be read as functions of these keys as well as of the state `m`.

* Any material change to functional forms, constants, admissible ranges, or numerical tolerances that define the encoding requires a new key combination. The result is treated as a different encoding and must be re evaluated from scratch.

### Relation to the TU program

* Q064 is an S rank node in the TU effective layer graph. It serves as a reference problem for thermodynamic tension in soft condensed matter and for cross domain analogies to dynamic arrest.
* E_level and N_level labels are internal to the TU program and do not express any claim about the canonical problem being solved or nearly solved.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
