# Q099 · Global freshwater dynamics under climate change

## 0. Header metadata

```txt
ID: Q099
Code: BH_EARTH_WATER_BALANCE_L3_099
Domain: Earth system
Family: Hydrology and freshwater resources
Rank: S
Projection_dominance: M
Field_type: dynamical_field
Tension_type: thermodynamic_tension
Status: Reframed_only
Semantics: continuous
E_level: E1
N_level: N1
Encoding_key: TU_BH_Q099_FW_v1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

### 0.1 Scope of objects

This page works only at the **effective layer** of the Tension Universe program.

All objects in the main text, including:

* the state space `M` and its regular subset `M_reg(Q099, E*)`,
* basin level summaries `P_k`, `E_k`, `R_k`, `dS_k`, `W_k`, `E_env_k`,
* derived observables `res_k`, `S_renew_k`, `D_total_k`, `ratio_k`, `T_extreme_k`,
* mismatch functionals `DeltaS_balance`, `DeltaS_demand`, `DeltaS_risk`,
* the freshwater tension functional `Tension_FW`,

are defined as **effective layer encodings** of global freshwater dynamics. They are not claimed to be unique, fundamental, or derived from any deep TU axioms.

No hidden construction of internal TU fields, no core level tensors, and no generative rules for world histories are specified or used in this document.

### 0.2 Encoding class and selected element

Q099 uses an explicit **encoding class**:

```txt
A_enc(Q099) = { E_1, ..., E_Lenc }
```

Each element `E` in `A_enc(Q099)` specifies, in advance:

* a choice of basin tiling `B(E)` and study subset `B_study(E)` from a finite library of basin definitions;
* allowed temporal resolutions `Delta_t(E)` from a finite menu (for example annual, seasonal, decadal);
* a specific function `f_ratio(E)` used to map basin stress ratios into scalar scores;
* a positive constant `epsilon_ref(E)` that regularizes division by small renewable supply;
* a weight triple `(w_balance(E), w_demand(E), w_risk(E))` with nonnegative entries that sum to 1;
* threshold bands
  `epsilon_balance(E)`, `epsilon_demand(E)`, `epsilon_risk(E)`, `epsilon_FW(E)` for low tension;
  `delta_balance(E)`, `delta_demand(E)`, `delta_risk(E)`, `delta_FW(E)` for high tension.

The mapping from external data and model outputs to effective layer states `m` in `M` is performed by **external procedures** that are not specified here. This document only assumes that these procedures can produce coherent summaries that respect the constraints of Section 3.

The metadata field

```txt
Encoding_key: TU_BH_Q099_FW_v1
```

selects a single element

```txt
E* in A_enc(Q099)
```

for this page. All subsequent notations

```txt
DeltaS_balance(m)
DeltaS_demand(m)
DeltaS_risk(m)
Tension_FW(m)
S_sing(Q099, E*)
M_reg(Q099, E*)
```

are shorthand for the corresponding quantities evaluated under `E*`. No component of `E*` may be tuned in response to the experiments described in Section 6.

### 0.3 Semantics regime

The metadata field

```txt
Semantics: continuous
```

is implemented as follows:

* All encoded quantities `P_k`, `E_k`, `R_k`, `dS_k`, `W_k`, `E_env_k` are real valued aggregates over finite basin tiles and finite time windows.
* Derived observables and tension scores are real valued functionals of these aggregates.
* No discrete socio technical labels or hybrid types are introduced in this problem. Human influence enters only through continuous quantities such as withdrawals and environmental flow requirements.

The continuous semantics regime means that all observables and tension functionals live in finite dimensional real vector spaces determined by the choice of `E*`.

### 0.4 Claims and non claims

This document **does**:

* define an effective layer state space and freshwater tension functional for Q099;
* specify mismatch measures for budget closure, supply demand balance, and risk tails;
* define low tension and high tension regimes in terms of inequalities relative to thresholds attached to `E*`;
* propose experiments that can falsify particular encoding choices in `A_enc(Q099)`.

This document **does not**:

* claim to solve any canonical open problem in hydrology or climate science;
* claim to predict actual future freshwater trajectories of the real Earth system;
* introduce any new theorem beyond what is already established in the cited scientific literature;
* expose or rely on any deep TU core construction, internal tensor fields, or generative dynamics.

### 0.5 Relation to canonical problem and BlackHole graph

Q099 is one node in the BlackHole S problem collection. The canonical problem statement in Section 1 is taken from mainstream Earth system and water resources science.

This page only re encodes that problem at the effective layer in TU language, under a specific encoding element `E*`. All references to other `Q` nodes in Section 2 and Section 8 are **graph relations between effective layer encodings**, not statements about deep causal or ontological structure.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q099 can be phrased as:

> Understand and quantify the long term global balance of freshwater availability, variability, and use under anthropogenic climate change, in a way that links physical water cycle dynamics, human withdrawals, ecological needs, and risk of large scale scarcity or flood crises.

Operationally, this involves at least four coupled questions:

1. How do precipitation, evapotranspiration, runoff, and storage components of the water cycle respond to different warming levels and circulation patterns?
2. How do these physical changes translate into renewable freshwater availability at river basin and aquifer scales that matter for societies and ecosystems?
3. How do human withdrawals, infrastructure, and land use changes feed back into these dynamics, altering availability, variability, and extremes?
4. Under what conditions does the global freshwater system cross thresholds into persistent deficit, regional collapse, or cascading crises?

This is not a single theorem but a coupled set of dynamical, statistical, and socio hydrological questions that must be kept conceptually coherent.

### 1.2 Status and difficulty

Key aspects are well studied but far from closed:

* Global water cycle intensification under warming is supported by climate model ensembles and observations, but regional projections remain uncertain, especially for extremes.
* Basin scale water budgets can be estimated from observations and reanalyses, yet closure errors, data gaps, and model structural uncertainties are substantial.
* Groundwater depletion, reservoir operations, and land use changes are known to alter runoff and storage, but large scale feedbacks are still poorly constrained.
* Planetary boundary frameworks for freshwater use exist, but robust quantitative thresholds and attribution of transgressions remain debated.

The difficulty arises from:

* strong coupling between atmosphere, land, oceans, cryosphere, biosphere, and human systems;
* multi scale behavior in space and time, from local catchments to planetary aggregates and from daily extremes to century scale trends;
* deep uncertainty in future socio economic pathways and adaptation responses.

Q099 is therefore treated as a reframed system level problem, not as a classical open conjecture.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q099:

1. acts as the primary node for **global freshwater balance and stress** at the Earth system scale;
2. connects the physical climate cluster (Q091–Q098) to socio economic and risk clusters (Q100–Q110) through a single conserved quantity: usable freshwater;
3. provides a reference template for encoding problems where:

   * a physically conserved quantity (water mass) is redistributed by dynamics,
   * human use changes boundary conditions and internal fluxes,
   * the main concern is long horizon risk of deficit or excess rather than a single event.

### References

1. IPCC, “Climate Change 2021: The Physical Science Basis”, Working Group I contribution to the Sixth Assessment Report, chapters on the global water cycle.
2. IPCC, “Climate Change 2022: Impacts, Adaptation and Vulnerability”, Working Group II contribution, sections on water resources and regional freshwater risks.
3. United Nations World Water Assessment Programme, “The United Nations World Water Development Report”, recurring editions on global water resources and governance.
4. P. H. Gleick et al., review articles and assessments on global freshwater resources, water security, and climate change impacts in the peer reviewed literature.

---

## 2. Position in the BlackHole graph

This block records how Q099 sits inside the BlackHole graph. All edges refer only to Q IDs and give a one line reason tied to concrete components or tension types.

### 2.1 Upstream problems

These problems provide foundations or tools that Q099 relies on at the effective layer.

* Q091
  Reason: Supplies the climate sensitivity and warming pathways that drive changes in global precipitation and evaporation fields used in the freshwater balance.

* Q092
  Reason: Encodes climate tipping points that can abruptly reorganize circulation patterns and thus freshwater distribution across basins.

* Q093
  Reason: Provides carbon cycle feedback scenarios that determine the long term temperature trajectories which Q099 must be conditioned on.

* Q094
  Reason: Describes ice sheet and glacier mass loss that alters sea level, runoff timing, and the partition between solid and liquid freshwater.

* Q096
  Reason: Encodes monsoon stability and regional circulation regimes that control the seasonal timing and intensity of freshwater input in key basins.

### 2.2 Downstream problems

These problems directly reuse Q099 components or depend on its freshwater tension structure.

* Q098
  Reason: Uses Q099 freshwater tension indices as input to the planetary boundary assessment for the hydrological dimension of Earth system safety.

* Q100
  Reason: Reuses Q099 basin level water stress and sanitation related observables as drivers for water borne and hygiene related pandemic risks.

* Q103
  Reason: Incorporates Q099 freshwater constraints and variability as limiting factors in long run global economic growth and capital deployment scenarios.

* Q109
  Reason: Uses Q099 regional freshwater scarcity and flood risk patterns as key drivers of long term migration flows and displacement pressure.

### 2.3 Parallel problems

Parallel nodes share similar tension types or structural features but have no direct component dependence.

* Q095
  Reason: Both Q095 and Q099 track conserved quantities in the hydrosphere, with tension arising from imbalances between fluxes and storage.

* Q097
  Reason: Q097 focuses on extreme precipitation and flood events, while Q099 aggregates over longer timescales; both see risk tail tension in hydrological extremes.

* Q104
  Reason: Q104 studies wealth and income inequality; Q099 studies freshwater distribution inequality; both encode persistent imbalance across spatial units.

### 2.4 Cross domain edges

Cross domain edges link Q099 to problems in other domains that can reuse its components.

* Q104
  Reason: Reuses basin level freshwater availability and stress indices as structural drivers of long run inequality patterns across regions.

* Q105
  Reason: Uses Q099 freshwater drought and flood stress fields as inputs to models of systemic crashes in infrastructure and financial systems.

* Q108
  Reason: Treats Q099 freshwater scarcity maps as background fields that intensify political polarization around resource allocation and environmental policy.

* Q110
  Reason: Depends on Q099 long run freshwater dynamics to evaluate how institutions must evolve to manage shared water resources and transboundary basins.

---

## 3. Tension Universe encoding (effective layer)

All content in this block stays at the effective layer. We describe only:

* state spaces,
* fields and observables,
* invariants and tension scores,
* singular sets and domain restrictions.

No hidden generative rule or mapping from raw data to internal TU fields is specified.

Throughout this section, all definitions are understood to be taken with respect to the encoding element `E*` selected by `Encoding_key`.

### 3.1 State space

We postulate a continuous field state space

```txt
M
```

with the following interpretation:

* Each element `m` in `M` represents a coherent configuration of the global freshwater system over a chosen time window and spatial tiling.

For a fixed temporal resolution `Delta_t` in the finite menu attached to `E*` and a finite set of spatial units

```txt
B(E*) = { B_1, ..., B_K }
```

for example, river basins or grid cells, a state `m` encodes, for each unit `B_k`:

* mean precipitation `P_k(m)`,
* evapotranspiration `E_k(m)`,
* surface and subsurface runoff `R_k(m)`,
* change in water storage `dS_k(m)`,
* human withdrawals `W_k(m)`,
* ancillary indicators such as environmental flow requirements `E_env_k(m)` and, where available, groundwater depletion proxies.

We assume:

* the tiling `B(E*)` comes from a finite library of pre specified basin or grid definitions agreed upon before analysis;
* the time window and `Delta_t` are chosen from a finite set of resolutions attached to `E*`;
* for each `m`, all encoded quantities for the chosen tiling and time window are finite real numbers.

No assumption is made here about how these quantities are estimated from observations or models.

### 3.2 Effective fields and observables

We define the following observables on `M` for the encoding `E*`:

1. Basin level water balance residual

```txt
res_k(m) = P_k(m) - E_k(m) - R_k(m) - dS_k(m)
```

Interpretation: `res_k(m)` measures the degree to which the encoded physical water budget closes in basin `B_k` over the chosen time window, excluding human withdrawals.

2. Renewable freshwater supply

```txt
S_renew_k(m) = max(0, R_k(m) + dS_k(m)_pos)
```

where `dS_k(m)_pos` denotes the positive part of storage change (gain).

Interpretation: `S_renew_k(m)` is an effective measure of the renewable freshwater made available to human and ecosystem use in basin `B_k`.

3. Human and ecological demand

```txt
D_total_k(m) = W_k(m) + E_env_k(m)
```

* `W_k(m)` is encoded human use (agriculture, industry, domestic).
* `E_env_k(m)` is an encoded environmental flow requirement needed to maintain ecosystems.

4. Basin stress ratio

Let `epsilon_ref(E*)` be the small positive reference constant fixed by `E*`. We define

```txt
ratio_k(m) = D_total_k(m) / (S_renew_k(m) + epsilon_ref(E*))
```

Interpretation: `ratio_k(m)` summarizes how strongly demand presses against renewable supply in basin `B_k`.

5. Global freshwater stress index

For the finite study set

```txt
B_study(E*) subset of B(E*)
```

we define

```txt
Index_stress(m) = average over k in B_study(E*) of f_ratio(E*)( ratio_k(m) )
```

where `f_ratio(E*)` is a nondecreasing function fixed by `E*` (for example truncated linear or logistic). The average is either a simple arithmetic mean or a pre declared population weighted mean, chosen once in `E*`.

### 3.3 Mismatch observables and tension components

We construct three mismatch observables that will form components of freshwater tension.

1. Budget mismatch

```txt
DeltaS_balance(m; E*) =
    average over k in B_study(E*) of | res_k(m) |
```

This measures the degree to which the encoded physical budgets fail to close across the study basins.

2. Supply demand mismatch

```txt
DeltaS_demand(m; E*) =
    average over k in B_study(E*) of max( 0, ratio_k(m) - 1 )
```

This captures how often and how strongly basins operate in effective deficit (demand exceeding renewable supply).

3. Risk tail mismatch

For each basin we encode a tail indicator

```txt
T_extreme_k(m)
```

that summarizes the probability or frequency of severe droughts or floods over the time window under the encoded climate scenario. The construction of `T_extreme_k(m)` from external sources is fixed in `E*` and does not depend on `Tension_FW`.

We then define

```txt
DeltaS_risk(m; E*) =
    average over k in B_study(E*) of T_extreme_k(m)
```

where each `T_extreme_k(m)` is already scaled into a nonnegative risk score by agreed upon rules before analysis.

For readability, we write `DeltaS_balance(m)`, `DeltaS_demand(m)`, and `DeltaS_risk(m)` in later sections, with the implicit understanding that they are evaluated under `E*`.

### 3.4 Admissible encoding class and fairness constraints

The encoding class `A_enc(Q099)` is constrained by the TU Encoding and Fairness Charter. For each `E` in `A_enc(Q099)` the following must hold:

1. **Finite design space**

   * The basin tiling `B(E)` and study set `B_study(E)` are selected from finite libraries declared outside this document.
   * The allowed temporal resolutions `Delta_t(E)` form a finite set.

2. **Pre committed functions and constants**

   * The function `f_ratio(E)` is chosen from a small, finite catalogue of monotone mappings (for example, piecewise linear or logistic families with a few discrete parameter choices).
   * The constant `epsilon_ref(E)` is chosen from a finite set of positive reference values.
   * The weight triple `(w_balance(E), w_demand(E), w_risk(E))` is selected from a finite menu of weightings and satisfies
     `w_balance(E) >= 0`, `w_demand(E) >= 0`, `w_risk(E) >= 0`,
     `w_balance(E) + w_demand(E) + w_risk(E) = 1`.

3. **Threshold bands**

   * The thresholds

     ```txt
     epsilon_balance(E), epsilon_demand(E),
     epsilon_risk(E), epsilon_FW(E)
     delta_balance(E),   delta_demand(E),
     delta_risk(E),      delta_FW(E)
     ```

     are defined as part of `E` and are compatible with the TU Tension Scale Charter.
   * Thresholds may depend on resolution and tiling, but once `E` is selected they are fixed and may not be re tuned using the results of Q099 experiments.

4. **External data to state mapping**

   * The mapping from observational data or model outputs to states `m` in `M` is defined externally and is independent of `Tension_FW` values.
   * No step in the data processing pipeline is allowed to use freshwater tension scores or the desire for a particular classification as a tuning signal.

5. **Finiteness and non plasticity**

   * The set `A_enc(Q099)` is finite. Working groups are expected to define and publish the finite set explicitly.
   * Once `Encoding_key` selects `E*`, all experiments and classifications on this page are to be read with respect to `E*`. The element `E*` itself is not modified in response to experimental outcomes.

These constraints ensure that Q099 encodings are auditable and cannot be adjusted ad hoc to make particular futures appear safer or more stressed.

### 3.5 Combined freshwater tension functional

Given `E*`, we define the combined freshwater tension functional

```txt
Tension_FW(m; E*) =
    w_balance(E*) * DeltaS_balance(m; E*)
  + w_demand(E*) * DeltaS_demand(m; E*)
  + w_risk(E*)   * DeltaS_risk(m; E*)
```

where the weights `w_balance(E*)`, `w_demand(E*)`, and `w_risk(E*)` are nonnegative, not all zero, and sum to 1 as part of the encoding element `E*`.

For brevity, we write `Tension_FW(m)` for `Tension_FW(m; E*)` in later sections.

Properties at the effective layer:

1. **Nonnegativity**

   ```txt
   Tension_FW(m) >= 0
   ```

   for all states `m` in the regular domain defined below.

2. **Componentwise sensitivity**

   * If all three components `DeltaS_balance(m)`, `DeltaS_demand(m)`, `DeltaS_risk(m)` are small, then `Tension_FW(m)` lies in a low band determined by `epsilon_FW(E*)`.
   * If any one component becomes large while the others remain bounded, `Tension_FW(m)` increases by at least a fixed fraction determined by the corresponding weight.

3. **Stability under data refinement**

   * Because all functions and weights are fixed by `E*`, refining input data or increasing spatial resolution only affects the arguments of `DeltaS_balance`, `DeltaS_demand`, and `DeltaS_risk`, not the structure of `Tension_FW` itself.

### 3.6 Singular set and domain restrictions

We define the singular set for Q099 and `E*` as

```txt
S_sing(Q099, E*) = {
    m in M :
        any encoded P_k(m), E_k(m), R_k(m), dS_k(m), W_k(m), E_env_k(m)
        is undefined or not finite
        or DeltaS_balance(m; E*), DeltaS_demand(m; E*), DeltaS_risk(m; E*)
           cannot be computed as finite real numbers
}
```

and the regular domain as

```txt
M_reg(Q099, E*) = M \ S_sing(Q099, E*)
```

All freshwater tension evaluations in this document are restricted to `M_reg(Q099, E*)`. Whenever an experimental protocol would require evaluating `Tension_FW(m)` for `m` in `S_sing(Q099, E*)`, the result is treated as *out of domain* and not as evidence about real world freshwater behaviour.

Any encoding element `E` in `A_enc(Q099)` that routinely produces large portions of `M` inside `S_sing(Q099, E)` for data that should be representable at the chosen resolution is considered ill posed for Q099 at the effective layer.

For readability, we write `S_sing` and `M_reg` in later sections, with the implicit dependence on `(Q099, E*)`.

---

## 4. Tension principle for this problem

This block states how Q099 is characterized as a tension problem within TU, without asserting a single theorem.

### 4.1 Core freshwater tension principle

For the encoding element `E*`, the core principle is:

> A globally sustainable freshwater regime corresponds to configurations `m` in `M_reg` where physical budgets are approximately closed, demand rarely and weakly exceeds renewable supply, and risk tails for drought and flood are contained within agreed safety bands.

Formally, there should exist world relevant configurations `m_safe` in `M_reg` such that

```txt
DeltaS_balance(m_safe)  <= epsilon_balance(E*)
DeltaS_demand(m_safe)   <= epsilon_demand(E*)
DeltaS_risk(m_safe)     <= epsilon_risk(E*)
Tension_FW(m_safe)      <= epsilon_FW(E*)
```

where the thresholds `epsilon_balance(E*)`, `epsilon_demand(E*)`, `epsilon_risk(E*)`, `epsilon_FW(E*)` belong to the low tension band for `E*` and do not grow without bound as data quality and resolution improve.

### 4.2 High tension freshwater world

A high tension freshwater regime is one where, for world relevant configurations `m_stress` in `M_reg`, at least one of the following holds persistently across refinements:

```txt
DeltaS_balance(m_stress)  >= delta_balance(E*)
DeltaS_demand(m_stress)   >= delta_demand(E*)
DeltaS_risk(m_stress)     >= delta_risk(E*)
Tension_FW(m_stress)      >= delta_FW(E*)
```

with strictly positive thresholds `delta_balance(E*)`, `delta_demand(E*)`, `delta_risk(E*)`, `delta_FW(E*)` that cannot be made small without contradicting the encoded physical and socio economic information.

### 4.3 Q099 as a classification statement

At the effective layer, Q099 does not claim that the world is provably in either regime. Instead it encodes:

* a structured way to classify world relevant configurations `m` into lower and higher freshwater tension bands;
* a requirement that any long term scenario for climate and society be accompanied by an explicit `Tension_FW` assessment under a disclosed encoding element `E`;
* a demand that any claim about sustainable or unsafe freshwater futures be expressible as inequalities in terms of `DeltaS_balance`, `DeltaS_demand`, `DeltaS_risk`, and `Tension_FW`.

The tension principle is therefore a classification and consistency framework, not a theorem.

---

## 5. Counterfactual tension worlds

We define two counterfactual worlds, described only through observable patterns and tension bands under `E*`.

### 5.1 World T (sustainable freshwater regime)

In World T, there exists an encoding element `E` in `A_enc(Q099)` and a family of world representing configurations `m_T` in `M_reg(Q099, E)` such that:

1. **Physical closure**

   * For realistic resolutions, `DeltaS_balance(m_T)` stays within small bands compatible with known closure errors in hydrological data and models.
   * Budget residuals `res_k(m_T)` fluctuate but do not indicate systematic inconsistency between precipitation, evapotranspiration, runoff, and storage.

2. **Demand versus supply**

   * The basin stress ratios `ratio_k(m_T)` exceed 1 only rarely and modestly, so that `DeltaS_demand(m_T)` remains below `epsilon_demand(E)` across most basins and time windows.

3. **Risk tails**

   * The tail indicators `T_extreme_k(m_T)` reflect droughts and floods, but their aggregated effect `DeltaS_risk(m_T)` stays within `epsilon_risk(E)` for basins representing major population and ecosystem centers.

4. **Global freshwater tension**

   * The combined tension satisfies

     ```txt
     Tension_FW(m_T) <= epsilon_FW(E)
     ```

     in scenarios consistent with deliberate mitigation and adaptation efforts.

For this page, World T is discussed conceptually under `E*`. Any eventual empirical claims about the existence of `m_T` must be tied to a concrete `E`.

### 5.2 World F (runaway freshwater stress regime)

In World F, for every encoding element `E` in `A_enc(Q099)` that faithfully represents external data, there exist world representing configurations `m_F` in `M_reg(Q099, E)` such that:

1. **Persistent budget discrepancy**

   * `DeltaS_balance(m_F)` exceeds `delta_balance(E)` over extended periods, due to structural mismatches between precipitation, evapotranspiration, runoff, and storage under high warming and land use change.

2. **Chronic deficits**

   * For many basins in `B_study(E)`, `ratio_k(m_F)` is significantly greater than 1 over extended time windows, pushing `DeltaS_demand(m_F)` beyond `delta_demand(E)` and indicating chronic overuse.

3. **Amplified risk tails**

   * `T_extreme_k(m_F)` is high for multiple key basins, with `DeltaS_risk(m_F)` exceeding `delta_risk(E)` and indicating frequent and severe droughts and floods beyond historical norms.

4. **High global freshwater tension**

   * For realistic scenario families,

     ```txt
     Tension_FW(m_F) >= delta_FW(E)
     ```

     across most plausible socio economic pathways, signalling a structurally stressed freshwater world.

Again, this world is defined in terms of observables and tension scores under `E`, not in terms of any particular model or simulation engine.

### 5.3 Interpretive note

These counterfactual worlds do not depend on how configurations are generated or simulated. They describe only how observable freshwater quantities and risks would behave if the world were in a sustainable or runaway regime under some encoding element in `A_enc(Q099)`.

They are used to test and interpret encodings, not to assert that the real Earth system will follow any particular path.

---

## 6. Falsifiability and discriminating experiments

This section specifies experiments that can falsify specific Q099 encodings at the effective layer. All experiments are to be read as operating under the encoding element `E*` selected by `Encoding_key`.

Throughout this section:

* `E*` is fixed in advance and not tuned using experimental outcomes;
* the mapping from external data to `m` is fixed before tension scores are computed.

### Experiment 1: Basin level budget closure under climate projections

**Goal**

Test whether the encoding `E*` yields physically consistent basin level budgets under existing climate projections and observations.

**Setup**

* Select a finite set of basins `B_study(E*)` that cover a broad range of climates and socio economic conditions.
* Fix time windows (for example, recent decades and mid century projections) and the temporal resolution `Delta_t` from those allowed in `E*`.
* Use published climate model ensembles and observation based products to construct states `m_hist` and `m_proj` in `M_reg` for each basin, encoding `P_k`, `E_k`, `R_k`, `dS_k`, `W_k`, and `E_env_k` according to externally specified rules.

**Protocol**

1. For each basin and time window, compute:

   * `res_k(m)` and check its magnitude against known closure error ranges;
   * `DeltaS_balance(m)` for the corresponding state.
2. Aggregate results into distributions of `res_k(m_hist)` and `res_k(m_proj)` across basins and time windows.
3. Compute `DeltaS_balance(m_hist)` and `DeltaS_balance(m_proj)` for each scenario and compare them to `epsilon_balance(E*)` and `delta_balance(E*)`.

**Metrics**

* Distribution of `res_k(m)` across basins and time windows.
* Values of `DeltaS_balance(m_hist)` and `DeltaS_balance(m_proj)` under different climate scenarios.
* Sensitivity of these metrics to small perturbations in input climate fields and observational products that are allowed under external data uncertainty.

**Falsification conditions**

The encoding element `E*` is rejected for Q099 if any of the following holds:

* For historical periods where closure errors are well characterized, `DeltaS_balance(m_hist)` systematically exceeds `delta_balance(E*)` across basins, indicating that the encoding fails to represent known physical constraints.
* Small perturbations of input data within documented uncertainty ranges cause `DeltaS_balance(m_hist)` or `DeltaS_balance(m_proj)` to jump across low and high tension bands in ways that are not linked to identifiable structural changes in the data, indicating numerical fragility of `E*` as a classification tool.

Rejection of `E*` under these conditions does not falsify the canonical freshwater problem; it only shows that this particular encoding element is inadequate for Q099.

**Logging requirements**

For each experiment run, the following metadata must be logged alongside results:

* `Encoding_key` and a description of `E*` (including `B(E*)`, `B_study(E*)`, `Delta_t`, `f_ratio(E*)`, `epsilon_ref(E*)`);
* numerical values of `w_balance(E*)`, `w_demand(E*)`, `w_risk(E*)`;
* thresholds `epsilon_balance(E*)`, `delta_balance(E*)`;
* data source names and versions for all climate and hydrological inputs;
* any pre processing steps applied before constructing states `m`.

These logs allow independent groups to reproduce and audit the experiment.

---

### Experiment 2: Coupled human freshwater stress scenarios

**Goal**

Assess whether the encoding `E*` can robustly distinguish low tension and high tension socio hydrological futures under different socio economic and adaptation scenarios.

**Setup**

* Select a set of global scenario families combining climate pathways and socio economic narratives.
* For each scenario family, construct states `m_scenario` in `M_reg` for a target period (for example, late century), encoding `P_k`, `E_k`, `R_k`, `dS_k`, `W_k`, and `E_env_k` for basins in `B_study(E*)`.
* Fix the weight triple `(w_balance(E*), w_demand(E*), w_risk(E*))` and all thresholds in `E*` before any scenario is evaluated.

**Protocol**

1. Partition the scenario ensemble into two sets using external criteria that do not involve Q099 tension scores:

   * low stress candidates (for example strong mitigation and adaptation pathways);
   * high stress candidates (for example high emission, low adaptation pathways).
2. For each scenario and for each target time window:

   * compute `DeltaS_balance(m_scenario)`, `DeltaS_demand(m_scenario)`, `DeltaS_risk(m_scenario)`, and `Tension_FW(m_scenario)`;
   * record tension bands relative to `epsilon_*` and `delta_*` for `E*`.
3. Perform perturbation tests by slightly modifying demand projections or adaptation measures within plausible ranges and recomputing tension metrics.

**Metrics**

* Range and distribution of `Tension_FW(m_scenario)` in each scenario family.
* Share of basins in chronic deficit mode, defined by `ratio_k(m_scenario) > 1` for extended periods.
* Separation between low tension and high tension scenario families, for example by comparing quantiles of `Tension_FW` and component scores.
* Sensitivity of classification outcomes (low vs high tension) to small, justified changes in scenario assumptions.

**Falsification conditions**

The encoding element `E*` is rejected for Q099 if:

* the encoding systematically assigns `Tension_FW(m_scenario)` values below `epsilon_FW(E*)` to scenarios externally classified as high stress while assigning values above `delta_FW(E*)` to scenarios externally classified as low stress, across a wide range of plausible external criteria; or
* modest changes in scenario assumptions within documented uncertainty ranges frequently flip scenario classifications between low tension and high tension without corresponding structural changes in the underlying freshwater quantities.

As in Experiment 1, rejection of `E*` does not falsify the canonical freshwater problem; it only shows that this encoding element does not provide a stable and discriminating freshwater tension measure.

**Logging requirements**

For each scenario comparison, the following metadata must be logged:

* `Encoding_key` and the full specification of `E*`;
* the external criteria used to label scenarios as low stress or high stress;
* numerical values of `epsilon_*` and `delta_*` thresholds used for band classification;
* descriptions and versions of all scenario data sources;
* details of any perturbations applied in sensitivity tests.

These logs permit independent reconstruction of scenario classifications and tension profiles.

---

## 7. AI and WFGY engineering spec

This block describes how Q099 can be used as an engineering module in AI systems under the WFGY framework, without exposing any TU core level mechanisms.

### 7.1 Training signals

For an AI system that can internally represent approximate freshwater states `m`, Q099 suggests the following training signals:

1. `signal_water_budget_closure`

   * Definition: a penalty proportional to `DeltaS_balance(m)` for internally simulated or reasoned freshwater configurations.
   * Purpose: encourage internal states that respect basic physical water budget closure where appropriate.

2. `signal_water_stress_ratio`

   * Definition: a signal derived from the distribution of `ratio_k(m)` across basins in `B_study(E*)`, with higher penalties for widespread or severe `ratio_k(m) > 1`.
   * Purpose: align the model’s reasoning about water availability with stress aware interpretations.

3. `signal_risk_tail_hydrology`

   * Definition: a signal based on `DeltaS_risk(m)` that increases when drought and flood risk tails become concentrated in vulnerable basins.
   * Purpose: push the model to pay attention to extreme event structure, not just mean conditions.

4. `signal_scenario_separation`

   * Definition: a contrastive signal that rewards a clear margin in `Tension_FW(m_scenario)` between externally labelled low stress and high stress scenario families.
   * Purpose: improve the model’s ability to distinguish genuinely safer futures from structurally risky ones.

All of these signals depend only on effective layer quantities and can be computed without reference to any TU core objects.

### 7.2 Architectural patterns

Possible architectural patterns that reuse Q099 components include:

1. `FreshwaterTensionHead`

   * Role: an auxiliary head that maps internal representations of Earth system and socio economic state into an estimate of `Tension_FW(m)` and its components.
   * Interface:

     * input: a compact embedding of scenario or narrative information;
     * outputs: scalar `Tension_FW(m)` and component scores `DeltaS_balance(m)`, `DeltaS_demand(m)`, `DeltaS_risk(m)`.

2. `BasinStressObserver`

   * Role: a module that projects latent spatial information into basin level summaries `ratio_k(m)` and `T_extreme_k(m)`.
   * Interface:

     * input: a spatial latent field representing climate and socio economic patterns;
     * output: vectors of basin level stress and risk metrics indexed by `B_study(E*)`.

3. `ScenarioComparator`

   * Role: a module that takes two scenario embeddings and produces comparative freshwater tension judgments.
   * Interface:

     * inputs: encodings of two scenarios;
     * outputs: a signed difference in `Tension_FW`, component wise comparisons, and optional uncertainty estimates.

### 7.3 Evaluation harness

A minimal evaluation harness for AI systems using Q099 components might include:

1. **Task types**

   * narrative to risk: given a textual description of a climate and development pathway, estimate freshwater stress at basin and global level using Q099 metrics;
   * policy comparison: compare two adaptation or infrastructure strategies in terms of their impact on freshwater tension metrics.

2. **Baselines**

   * baseline model: standard Earth system and policy reasoning with no explicit freshwater tension heads;
   * TU augmented model: same backbone, augmented with Q099 based heads and training signals.

3. **Metrics**

   * agreement with expert qualitative assessments of freshwater risks for well studied scenarios;
   * internal consistency: reduction in contradictions across answers about water availability, stress, and extremes;
   * sensitivity alignment: improved sensitivity of model outputs to scenario changes known to affect freshwater stress (for example irrigation expansion, reservoir construction, aggressive mitigation).

### 7.4 60 second reproduction protocol

A simple protocol for external users to experience Q099 informed reasoning is:

1. **Baseline setup**

   * Prompt: ask the AI to compare two future climate scenarios in terms of water security, without mentioning any formal tension encoding.
   * Observation: note whether the explanation is vague, mixes different notions of risk, or neglects budget closure and chronic deficits.

2. **TU encoded setup**

   * Prompt: ask the same question, but request an answer structured around three components:

     * physical water budget closure,
     * supply versus demand at basin level,
     * extreme event risk tails,
       and a single scalar freshwater tension score summarizing each scenario.
   * Observation: check whether the explanation now explicitly references these components and uses a coherent scalar comparison.

3. **Comparison metric**

   * Use a simple rubric scoring structure, explicitness of trade offs, and clarity of what drives differences in stress between scenarios.

4. **What to log**

   * Prompts, full responses, any exposed `Tension_FW` values and component scores, and the `Encoding_key` used.
   * This allows external reviewers to test whether the model is using Q099 encodings in a disciplined way.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: `FreshwaterTensionScore`

   * Type: functional
   * Minimal interface:

     * inputs: basin level summaries of `P_k`, `E_k`, `R_k`, `dS_k`, `W_k`, `E_env_k` over a time window, plus a declared encoding element `E`;
     * outputs: scalar `Tension_FW(m; E)` and component values `DeltaS_balance(m; E)`, `DeltaS_demand(m; E)`, `DeltaS_risk(m; E)`.
   * Preconditions: input summaries must be defined for a finite set of basins consistent with `B(E)` and the chosen time resolution.

2. ComponentName: `BasinWaterBudgetField`

   * Type: field
   * Minimal interface:

     * inputs: climate and socio economic scenario descriptors plus `E`;
     * outputs: fields `res_k`, `S_renew_k`, `D_total_k`, `ratio_k`, and `T_extreme_k` over `B_study(E)`.
   * Preconditions: scenario descriptors must be rich enough to determine approximate freshwater variables at the resolution of interest.

3. ComponentName: `WaterStressRiskTail_Template`

   * Type: experiment_pattern
   * Minimal interface:

     * inputs: a scenario family, an encoding element `E`, and a mapping from scenario variables to freshwater summaries;
     * outputs: an experiment specification with metrics based on `DeltaS_demand` and `DeltaS_risk`.
   * Preconditions: there must be a documented way to derive freshwater stress indicators from the scenario inputs.

### 8.2 Direct reuse targets

1. Q098

   * Reused component: `FreshwaterTensionScore`.
   * Why it transfers: Q098 needs a scalar indicator of freshwater pressure on the Earth system to help define and monitor a planetary boundary.
   * What changes: the safe band thresholds are reframed in planetary boundary language, but the functional form of `Tension_FW` is preserved.

2. Q103

   * Reused component: `BasinWaterBudgetField`.
   * Why it transfers: Q103 models growth slowdowns and constraints; freshwater availability and variability appear as direct constraints on productive capacity and infrastructure viability.
   * What changes: the outputs feed into economic modules rather than primarily into risk modules.

3. Q100

   * Reused component: `WaterStressRiskTail_Template`.
   * Why it transfers: Q100 studies global pandemic risk; water related sanitation stress and outage patterns are natural drivers in the experiment design.
   * What changes: the evaluation metrics emphasize connections to disease transmission and public health.

4. Q109

   * Reused component: `BasinWaterBudgetField` and `WaterStressRiskTail_Template`.
   * Why it transfers: Q109 studies migration; persistent high freshwater tension becomes a core push factor shaping migration patterns.
   * What changes: the outputs are integrated into mobility and demographic modules.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

Under the TU program, and relative to the encoding element `E*`, Q099 is currently assessed as:

* `E_level: E1`

  * A clear effective layer encoding for global freshwater tension has been specified.
  * Core observables, tension components, and a combined `Tension_FW` functional are defined with explicit domain restrictions and encoding class constraints.
* `N_level: N1`

  * A structured narrative linking physical budgets, supply demand balance, and risk tails has been laid out.
  * Counterfactual worlds and scenario experiments are specified conceptually.

These levels may be revised as implementations and comparative studies accumulate.

### 9.2 Next measurable step toward E2

To progress from `E_level: E1` to `E_level: E2`, at least one of the following should be realized and documented:

1. A prototype implementation that, for a chosen climate model ensemble and socio economic scenarios, computes `Tension_FW(m; E*)` for a curated set of basins and publishes:

   * the explicit definition of `E*`;
   * maps and time series of `Tension_FW` and its components;
   * the associated uncertainty analysis.

2. A structured comparison between several encoding elements in `A_enc(Q099)`, showing:

   * which choices of `E` pass the falsification tests in Section 6;
   * how sensitive tension scores and classifications are to differences in tiling, weights, and thresholds;
   * how these differences relate to the TU Encoding and Fairness Charter.

Both steps operate entirely at the effective layer. They do not require exposing any TU core structures.

### 9.3 Long term role in the TU program

In the long term, Q099 is expected to:

* anchor the freshwater dimension of Earth system tension assessments;
* provide an example of how to integrate physical conservation laws, human use, and extreme event risk into a single effective layer tension framework;
* serve as a reusable module for broader systemic risk analyses involving food, energy, health, migration, and political stability.

---

## 10. Elementary but precise explanation

At a simple level, Q099 asks:

> How much trouble are we in, globally, when it comes to water, once we account for climate change, our own withdrawals, and extreme events like droughts and floods?

The Tension Universe view breaks this into three pieces:

1. **Budget closure**

   * When we add up rain, evaporation, river flow, and changes in stored water in each region, does the book almost balance, or are there big unexplained gaps?

2. **Demand versus renewable supply**

   * In each basin, do people and ecosystems want much more water than nature reliably provides, or is demand usually below renewable supply?

3. **Risk tails**

   * How often do we see very bad events, with too little water or too much water, compared to what societies and ecosystems can cope with?

For each region, we can compute simple numbers that say:

* how large the budget error is;
* how large the gap is between demand and renewable supply when there is a deficit;
* how strong the tail of dangerous events is.

We then average these numbers in a careful way, with weights fixed ahead of time, to get a single freshwater tension score for the world or for a group of regions.

In a **low tension freshwater world**, budgets almost close, demand rarely exceeds supply by much, and extreme droughts and floods are serious but manageable.

In a **high tension freshwater world**, budgets look inconsistent, many regions live in chronic deficit, and extremes become common and damaging.

Q099 does not predict exactly what will happen or claim to know which world we will end up in. Instead, it gives a precise way to:

* turn complex data and scenarios into a few meaningful tension numbers;
* compare different futures in terms of how stressed the global freshwater system would be;
* connect freshwater stress to other big questions about safety, growth, health, migration, and governance.

---

## Tension Universe effective layer footer

This page is part of the **WFGY / Tension Universe** S problem collection.

### Scope of claims

* The goal of this document is to specify an **effective layer encoding** of the named problem and to define associated freshwater tension functionals.
* It does not claim to prove or disprove the canonical problem statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem in Earth system or hydrological science has been solved.

### Effective layer boundary

* All objects used here (state spaces `M`, observables, invariants, tension scores, counterfactual worlds, experiments) live at the effective layer of the TU framework.
* No deep TU core constructs, no generative dynamics for world histories, and no underlying axiom systems are exposed or relied upon in this document.
* The encoding class `A_enc(Q099)` and the selected element `E*` are part of an auditable design space, as required by the TU Encoding and Fairness Charter.

### Encoding and fairness

* All weights, thresholds, tilings, and functions that define `E*` are pre committed and belong to a finite library.
* Experimental outcomes in Section 6 may be used to reject or compare encoding elements, but not to silently adjust `E*` in order to obtain desired classifications.
* Any scientific or policy use of Q099 encodings must disclose the `Encoding_key` and enough metadata to reconstruct `E*`.

### Relation to other TU components

* This page is meant to be read alongside other Q nodes in the Earth system cluster and their encodings, as part of a larger map of S problems.
* AI and engineering uses of Q099 should treat it as one reusable module among many, not as a privileged or fundamental description of freshwater dynamics.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
