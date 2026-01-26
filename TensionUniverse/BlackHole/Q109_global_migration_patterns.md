# Q109 · Global migration patterns

## 0. Header metadata

```txt
ID: Q109
Code: BH_SOC_MIGRATION_L3_109
Domain: Social and economic systems
Family: Global migration and mobility
Rank: S
Projection_dominance: I
Field_type: socio_technical_field
Tension_type: incentive_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-26
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q109 is:

> Describe and understand the long run structure, drivers, and feedbacks of global human migration flows, and explain how economic, political, environmental, and demographic forces generate large scale patterns over decades and centuries.

In standard social science language this involves several linked questions:

1. Given a partition of the world into regions or countries, how do people move between them over time, both in terms of gross flows and net flows.
2. How do wage gaps, employment opportunities, demographic pressures, conflict, environmental stress, and policy barriers shape those flows.
3. How do feedback mechanisms, such as diasporas, remittances, and political responses, reinforce or damp migration patterns.
4. How do migration systems evolve, stabilize, or destabilize across long horizons.

There is no single closed form equation or theorem that solves this problem. Instead it is a structural open problem about how to encode and integrate:

* global data on stocks and flows,
* multiple interacting drivers,
* local and global feedback loops,
* and regime shifts such as large scale refugee movements or sudden policy changes.

### 1.2 Status and difficulty

Global migration is one of the best documented large scale social processes. However, even with extensive data and theory, several key aspects remain unresolved:

* Competing theories of international migration explain different slices of reality but do not integrate into a single widely accepted structural model.
* Quantitative gravity models can fit historical flows reasonably well, yet they often struggle with regime shifts, rare shocks, and nonlinear feedbacks.
* Long horizon predictions are notoriously fragile, especially when climate change, conflict, and institutional changes are involved.
* The role of feedback via diasporas, remittances, and political responses is empirically supported but difficult to formalize in a way that scales globally.

For these reasons, Q109 is treated as an open structural problem. It is not unsolved in the sense of a single missing proof, but in the sense that we do not yet have a widely accepted, verifiable, and portable encoding that captures the main regularities and instabilities of global migration systems.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection Q109 plays several roles:

1. It is a flagship example of a socio_technical_field problem governed by incentive_tension and risk_tail_tension on flows over a network.
2. It provides a template for encoding large scale human mobility as flows on a graph with multi-driver inputs and multi-scale feedbacks.
3. It links economic, environmental, and institutional problems by acting as a conduit for their combined effects on human populations.
4. It supplies reusable components such as MigrationFlow_Field and MigrationFeedback_Kernel that appear in multiple other S-problems.

### References

1. Castles, S., de Haas, H., Miller, M. J. (2014). The Age of Migration: International Population Movements in the Modern World. Fifth edition. Guilford Press.
2. Massey, D. S., Arango, J., Hugo, G., Kouaouci, A., Pellegrino, A., Taylor, J. E. (1993). Theories of International Migration: A Review and Appraisal. Population and Development Review, 19(3), 431–466.
3. United Nations Department of Economic and Social Affairs (2020). International Migration 2020: Highlights. UN DESA Population Division.
4. World Bank (2011). Global Bilateral Migration Database. World Bank Development Research Group.
5. de Haas, H. (2011). The Determinants of International Migration: Conceptualizing Policy, Origin and Destination Effects. Working Papers, International Migration Institute, University of Oxford.

---

## 2. Position in the BlackHole graph

This block records how Q109 sits inside the BlackHole graph as nodes and edges among Q001–Q125. Each edge has a one line reason that points to a concrete component or tension type rather than vague similarity.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q109 relies on at the effective layer.

* Q104 (BH_SOC_INEQUALITY_L3_104)
  Reason: Provides WealthInequality_Field and IncentiveGradient components that feed into migration drivers in Driver_Field.

* Q101 (BH_ECON_EQUITY_PREMIUM_L3_101)
  Reason: Supplies structural insight into risk and return that shapes cross border capital and labor flows jointly with MigrationFlow_Field.

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: Encodes large scale socio environmental regime shifts that change EnvironmentalStress inputs within Driver_Field.

* Q099 (BH_EARTH_WATER_STRESS_L3_099)
  Reason: Provides EnvironmentalStress_Field for water and agriculture that can act as push and pull factors for migration corridors.

### 2.2 Downstream problems

These problems are direct reuse targets of Q109 components or depend on Q109 tension structure.

* Q110 (BH_SOC_INSTITUTION_EVOLUTION_L3_110)
  Reason: Reuses MigrationFeedback_Kernel and Tension_MIG_Functional as pressure terms driving institutional adaptation.

* Q100 (BH_HEALTH_PANDEMIC_RISK_L3_100)
  Reason: Uses MigrationFlow_Field and SpatialMobility_Field as conduits for pathogen spread across regions.

* Q125 (BH_AI_MULTI_AGENT_DYNAMICS_L3_125)
  Reason: Treats agents moving in abstract policy or state spaces using a MobilityNetwork component patterned after MigrationFlow_Field.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q105 (BH_FIN_SYSTEMIC_CRASH_L3_105)
  Reason: Both Q105 and Q109 encode flows on networks with strong feedback and risk_tail_tension over rare, large scale shifts.

* Q108 (BH_SOC_POLARIZATION_L3_108)
  Reason: Both encode socio_technical_field dynamics where long run feedback between agents and institutions shapes macro patterns.

### 2.4 Cross domain edges

Cross domain edges connect Q109 to problems in other domains that can reuse its components.

* Q091 (BH_EARTH_CLIMATE_SENSITIVITY_L3_091)
  Reason: ClimateSensitivity_Field interacts with Driver_Field via ClimateStressToMigration_Channel for certain regions.

* Q092 (BH_EARTH_TIPPING_POINTS_L3_092)
  Reason: Uses MigrationShock_Response to describe population redistribution after climate tipping events.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Reuses non equilibrium flow language (flux, steady state, dissipation) to frame flow based invariants in Tension_MIG_Functional.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state space,
* effective fields and observables,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden generative rules or any direct mapping from raw data or micro agents to internal TU fields.

### 3.1 State space and finite libraries

We assume a semantic state space

```txt
M
```

with elements `m` that represent coherent global migration configurations over specified time windows.

Each state `m` encodes:

* A finite region index set `R_set`:

  ```txt
  R_set = {1, 2, ..., N_R}
  ```

  where each index corresponds to a region or country in a chosen partition.

* A finite time window index set `Tau_set`:

  ```txt
  Tau_set = {1, 2, ..., N_T}
  ```

  where each index corresponds to a contiguous time window such as a decade or a five year period.

* Flow summaries between regions for each time window.

* Region level driver summaries for each region and time window.

* Barrier summaries for each origin destination pair and time window.

* Coarse information about feedback responses that link past flows to subsequent drivers and barriers.

We also fix in advance a finite corridor library:

```txt
C_lib = { (i, j) in R_set x R_set : i != j }
```

and we restrict all aggregated tension measures to this library.

We do not specify any rule that constructs `m` from underlying data. We only assume that for any fixed choice of `R_set`, `Tau_set`, and `C_lib` there exist states that encode coherent summaries.

### 3.2 Effective fields and observables

We introduce the following effective fields on `M`.

1. Migration flow field

```txt
F_flow(m; i, j, tau) >= 0
```

* Input: state `m`, origin region index `i`, destination region index `j`, time window index `tau`.
* Output: nonnegative scalar summarizing the average migration flow rate from `i` to `j` over the time window indexed by `tau`.

2. Driver field

```txt
D_driver(m; i, tau)
```

* Input: state `m`, region index `i`, time window index `tau`.
* Output: vector of driver indicators for region `i` and time `tau`. Examples include income per capita, unemployment, conflict level, environmental stress, demographic pressure.

3. Policy barrier field

```txt
B_policy(m; i, j, tau)
```

* Input: state `m`, origin `i`, destination `j`, time window `tau`.
* Output: scalar in a fixed closed interval such as `[0, 1]` indicating institutional and legal barriers to migration along corridor `(i, j)` in that period. Higher values correspond to stronger barriers.

4. Feedback kernel

```txt
K_feedback(m; i, j, tau)
```

* Input: state `m`, corridor `(i, j)`, time window `tau`.
* Output: finite dimensional summary of how past flows along `(i, j)` influence future values of `D_driver` or `B_policy` for the same corridor or related corridors.

5. Structural prediction field

```txt
F_pred(m; i, j, tau)
```

* Input: state `m`, corridor `(i, j)`, time window `tau`.
* Output: predicted flow value from a simple structural relation that uses `D_driver` and `B_policy` as inputs. At the effective layer we only require that:

  * `F_pred(m; i, j, tau) >= 0` for all states in a regular domain.
  * For fixed `R_set`, `Tau_set`, and `C_lib`, the mapping from driver and barrier summaries to `F_pred` is stable and does not depend on the realized flows `F_flow` in that same state.

### 3.3 Mismatch observables and aggregated invariants

We define mismatch observables over the finite libraries.

1. Flow mismatch observable

```txt
DeltaS_flow(m; i, j, tau) =
    | F_flow(m; i, j, tau) - F_pred(m; i, j, tau) |
```

* Defined for all `(i, j)` in `C_lib` and `tau` in `Tau_set` where both `F_flow` and `F_pred` are finite.
* Measures deviation between observed and structurally predicted flows.

2. Feedback mismatch observable

```txt
DeltaS_feedback(m; i, j, tau)
```

* Defined as a nonnegative scalar whenever:

  * The effect of past flows on drivers and barriers along `(i, j)` can be summarized, and
  * A reference pattern with weak or no feedback can be specified.

* It measures how strongly the observed evolution of drivers and barriers deviates from this weak feedback reference.

3. Aggregated flow tension invariant

We aggregate across the finite library:

```txt
I_flow(m) =
    max over (i, j) in C_lib, tau in Tau_set
        DeltaS_flow(m; i, j, tau)
```

This is an invariant of the state `m` given the fixed library, and it is finite whenever all relevant mismatches are finite.

4. Aggregated feedback tension invariant

```txt
I_feedback(m) =
    max over (i, j) in C_lib, tau in Tau_set
        DeltaS_feedback(m; i, j, tau)
```

This captures the strongest feedback discrepancy in the encoded migration system.

5. Structural imbalance summary

We define an additional summary `I_imbalance(m)` that captures net flows from highly stressed regions:

```txt
I_imbalance(m) =
    max over i in R_set, tau in Tau_set
        ImbalanceScore(m; i, tau)
```

where `ImbalanceScore` is a nonnegative scalar function of:

* net inflow or outflow for region `i` in `tau`,
* driver indicators in `D_driver(m; i, tau)`.

The exact functional form is part of the encoding choice, but it must be fixed in advance for a given encoding class and must return finite values on the regular domain.

### 3.4 Encoding class and singular set

To prevent arbitrary tuning, we restrict attention to an admissible encoding class for Q109, denoted `E_MIG`. An element of `E_MIG` consists of:

* A choice of region partition `R_set`, time windows `Tau_set`, and corridor library `C_lib`, all finite and fixed before tension evaluation.
* A structural prediction rule for `F_pred` that uses only `D_driver` and `B_policy`, with parameters chosen without access to realized `F_flow` in the same state.
* Fixed aggregation functions for `I_flow`, `I_feedback`, and `I_imbalance` across the libraries.

Within any encoding in `E_MIG` all parameter choices and functional forms are fixed before tension values are computed for specific states.

We define a singular set:

```txt
S_sing = {
    m in M :
    some F_flow or F_pred or D_driver or B_policy or
    DeltaS_flow or DeltaS_feedback is undefined or not finite
}
```

and a regular domain:

```txt
M_reg = M \ S_sing
```

All migration tension analysis in Q109 is restricted to `M_reg`. When an attempted evaluation falls in `S_sing`, the result is treated as out of domain rather than as evidence for or against any hypothesis.

---

## 4. Tension principle for this problem

This block states how Q109 is characterized as a tension problem within TU, at the effective layer.

### 4.1 Core migration tension functional

Given an admissible encoding in `E_MIG`, we define a migration tension functional:

```txt
Tension_MIG(m) =
    w_flow * I_flow(m) +
    w_feedback * I_feedback(m) +
    w_imbalance * I_imbalance(m)
```

with weights satisfying:

```txt
w_flow > 0
w_feedback > 0
w_imbalance > 0
w_flow + w_feedback + w_imbalance = 1
```

The weights are part of the encoding and must be fixed before evaluating any states that are used in experiments. Once fixed, they are not adjusted to fit particular datasets.

Properties:

* `Tension_MIG(m) >= 0` for all `m` in `M_reg`.
* `Tension_MIG(m)` is small when flows, feedbacks, and imbalances all remain within their reference bands.
* `Tension_MIG(m)` grows when mismatches or imbalances become large along any corridor or region.

### 4.2 Low tension and sustainable migration regimes

At the effective layer, low tension migration regimes are characterized by:

* Flow mismatches that remain bounded and moderate across corridors and time windows.
* Feedback mismatches that indicate either weak feedback or feedback that stabilizes drivers and barriers.
* Structural imbalances that remain within tolerable ranges, without sustained extreme net flows out of already stressed regions.

Formally, for a chosen encoding in `E_MIG` there exists a threshold `epsilon_MIG > 0` such that:

```txt
Tension_MIG(m) <= epsilon_MIG
```

for states `m` that represent sustainable migration configurations under the given partition and time horizon.

`epsilon_MIG` depends on the encoding and on the scale of variation in the drivers, but it is fixed once the encoding is fixed and does not change after inspecting particular states.

### 4.3 High tension and unstable migration regimes

High tension migration regimes are characterized by one or more of the following:

* Persistent large deviations between actual and structurally predicted flows along many corridors.
* Strong and destabilizing feedbacks, where flows trigger rapid changes in drivers or barriers that further amplify flows.
* Sustained structural imbalances, such as long periods where high stress regions experience large net outflows without corresponding improvements in conditions.

For an admissible encoding in `E_MIG` we say that a regime is high tension if there exists a threshold `delta_MIG > 0` such that:

```txt
Tension_MIG(m) >= delta_MIG
```

for states `m` representing that regime, and `delta_MIG` cannot be reduced arbitrarily by refining inputs or re partitioning while remaining within the same encoding class.

In this sense Q109 frames an open structural question:

> For realistic encodings of the global migration system, which historical and hypothetical worlds fall into low tension regimes and which fall into high tension regimes, and how do systems move between them.

This framing does not assert any generative rule for real world migration, but it gives a way to express and test consistency between flows, drivers, and feedbacks.

---

## 5. Counterfactual tension worlds

We now describe two stylized counterfactual worlds at the effective layer. They are not predictions or generative models, but structured patterns of observables.

### 5.1 World S: structured and stable migration system

World S is a low tension regime with the following properties:

1. Flow structure

   * For most corridors in `C_lib` and time windows in `Tau_set`, the flow mismatch `DeltaS_flow(m_S; i, j, tau)` remains small relative to the scale of flows.
   * `I_flow(m_S)` stays below the low tension threshold `epsilon_MIG` for long stretches of time.

2. Feedback behavior

   * The feedback mismatch `DeltaS_feedback(m_S; i, j, tau)` is small for most corridors.
   * Where feedback exists it tends to be stabilizing: increased flows help ease driver pressures in origin regions or are absorbed by institutions in destination regions.

3. Structural balance

   * The imbalance summary `I_imbalance(m_S)` stays moderate. Regions under strong environmental or economic stress do not experience unchecked sustained outflows without observable improvements in conditions or institutional responses.

4. Global tension

   * Overall, `Tension_MIG(m_S)` remains within a stable band with occasional peaks that correspond to isolated shocks rather than sustained structural mismatches.

### 5.2 World U: unstable and feedback dominated migration system

World U is a high tension regime with the following properties:

1. Flow structure

   * Large corridors exist where `DeltaS_flow(m_U; i, j, tau)` is consistently high. Observed flows repeatedly contradict structural predictions based on slowly moving drivers and barriers.
   * `I_flow(m_U)` is often near or above the high tension threshold `delta_MIG`.

2. Feedback behavior

   * Feedback mismatches `DeltaS_feedback(m_U; i, j, tau)` are large on key corridors. Past flows significantly alter drivers and barriers in ways that accelerate further flows or provoke strong political reactions.
   * Feedback loops amplify differences between regions and lead to cascades of movement.

3. Structural imbalance

   * Imbalance scores are high for some regions for extended periods. These regions see large net outflows while driver stress remains high or increases, indicating deep structural mismatches.

4. Global tension

   * `Tension_MIG(m_U)` remains high for long stretches, with sharp spikes aligned with crises such as multi country conflicts, sudden environmental shocks, or rapid institutional breakdowns.

### 5.3 Interpretive note

World S and World U are templates for observable patterns in the state space `M_reg` under different regimes. They do not specify how the states are generated from micro level decisions or policies. Their purpose is to provide:

* a structured vocabulary for distinguishing stable and unstable migration regimes, and
* a test bed for encodings of `Tension_MIG` that should, in principle, separate S type regimes from U type regimes.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can falsify specific Q109 encodings in the class `E_MIG`. They do not solve the canonical problem but they constrain which encodings are acceptable at the effective layer.

### Experiment 1: Multi decade flow versus structural prediction

*Goal:*
Test whether a given encoding of `F_pred`, `DeltaS_flow`, and `Tension_MIG` can account for several decades of bilateral migration data without producing trivial or pathological tension patterns.

*Setup:*

* Data:

  * Use public global bilateral migration stocks or flows for at least two or three decades, such as from UN DESA and World Bank datasets.
  * Use region level drivers such as income per capita, population, conflict indices, and environmental stress proxies.

* Encoding:

  * Choose a fixed region partition `R_set`, time windows `Tau_set`, and corridor library `C_lib` before inspecting tension outputs.
  * Choose a structural prediction rule for `F_pred` and weights `(w_flow, w_feedback, w_imbalance)` before computing mismatches.

*Protocol:*

1. For each time window `tau` in `Tau_set`, construct a state `m_data(tau)` that encodes flows, driver indicators, and barrier summaries for that period, all restricted to the chosen libraries.

2. For each `m_data(tau)` compute:

   * `DeltaS_flow(m_data(tau); i, j, tau)` for all `(i, j)` in `C_lib`,
   * `I_flow(m_data(tau))`,
   * any available `DeltaS_feedback` contributions and `I_imbalance(m_data(tau))`,
   * the overall `Tension_MIG(m_data(tau))`.

3. Record the time series of `Tension_MIG` over all `tau` and its distribution across corridors.

4. Compare observed tension patterns with simple expectations, such as low tension during relatively stable periods and moderate peaks during known large shocks.

*Metrics:*

* Range and variability of `Tension_MIG(m_data(tau))` over time.
* Frequency and magnitude of high tension peaks.
* Corridor level distribution of `DeltaS_flow` and `DeltaS_feedback`.

*Falsification conditions:*

* If, under the fixed encoding, `Tension_MIG(m_data(tau))` is almost always near zero, even during periods known to involve major migration crises, the encoding is considered trivial and rejected.
* If, under the fixed encoding, `Tension_MIG(m_data(tau))` is almost always extremely large and insensitive to meaningful differences between periods, the encoding is considered non informative and rejected.
* If small, justified changes in drivers or barriers produce arbitrarily large changes in `Tension_MIG`, while leaving flows nearly unchanged, the encoding is considered unstable and rejected.

*Semantics implementation note:*
Region and time indices are treated as discrete labels, while flows, drivers, and tension values are real valued quantities. All computations respect this hybrid setting.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can reject or refine Q109 encodings in `E_MIG` but does not provide a definitive structural theory of global migration.

---

### Experiment 2: Weak versus strong feedback model worlds

*Goal:*
Check whether the Q109 encoding can reliably distinguish weak feedback migration models from strong feedback models at the effective layer.

*Setup:*

* Construct or select two families of simulation models:

  * Class W: models where migration flows respond mainly to slowly changing drivers and relatively fixed barriers, with weak feedback effects.
  * Class S: models where migration flows significantly alter future drivers and barriers, with strong feedback loops and possible cascades.

* Generate multiple simulated histories for each class under similar initial driver conditions.

*Protocol:*

1. For each simulated history in Class W and Class S, define a sequence of states `m_W(tau)` and `m_S(tau)` using the same `R_set`, `Tau_set`, and `C_lib` as in Experiment 1.
2. Compute `DeltaS_flow`, `DeltaS_feedback`, `I_flow`, `I_feedback`, and `Tension_MIG` for each state.
3. Build distributions of `Tension_MIG` values for Class W and Class S and compare them.
4. Repeat for several reasonable encodings in `E_MIG` to test robustness.

*Metrics:*

* Mean and variance of `Tension_MIG` in Class W and Class S.
* Separation between the two distributions, for example via simple summary statistics or classification performance of a threshold rule.
* Stability of the separation under small changes in encoding parameters within `E_MIG`.

*Falsification conditions:*

* If the encoding produces nearly identical `Tension_MIG` distributions for Class W and Class S across a range of reasonable parameter settings, then the definition of `DeltaS_feedback` or the aggregation in `Tension_MIG` is considered insufficient and rejected.
* If Class W consistently shows higher `Tension_MIG` than Class S despite being designed as a weak feedback family, the encoding is considered misaligned with the intended notion of feedback tension and must be revised.

*Semantics implementation note:*
The simulation outputs are mapped into the same discrete region and time index sets as in data based experiments, with real valued flows and drivers, so that tension measures are computed in a consistent hybrid setting.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. Success or failure on synthetic models tests the usefulness of Q109 encodings but does not settle the real world structure of migration.

---

## 7. AI and WFGY engineering spec

This block describes how Q109 can be used as an engineering module inside WFGY based AI systems, at the effective layer.

### 7.1 Training signals

We define several training signals derived from Q109 observables.

1. `signal_migration_flow_consistency`

   * Definition: a nonnegative signal proportional to aggregated `DeltaS_flow` across selected corridors and time windows in the current context.
   * Purpose: penalize internal representations that imply migration flows inconsistent with their own stated drivers and barriers when the context expects structural coherence.

2. `signal_migration_feedback_stability`

   * Definition: a signal derived from `I_feedback`, emphasizing periods and corridors where feedback is near or beyond a chosen threshold.
   * Purpose: make models sensitive to feedback dominated regimes and encourage clear separation between weak and strong feedback narratives.

3. `signal_structural_imbalance`

   * Definition: a signal derived from `I_imbalance`, focusing on regions where net flows and drivers indicate persistent imbalance.
   * Purpose: discourage explanations that ignore or downplay severe imbalances when discussing long run migration patterns.

4. `signal_regime_shift_alert`

   * Definition: a binary or graded indicator that triggers when `Tension_MIG` crosses a preset high tension threshold.
   * Purpose: nudge models to treat such contexts as regime shifts requiring special care in reasoning, rather than as minor fluctuations.

### 7.2 Architectural patterns

We outline reusable architectural patterns that draw on Q109 without revealing any deep TU generative rules.

1. `MigrationFlowHead`

   * Role: an auxiliary head that, given a representation of a global or regional context, predicts coarse migration flows between abstract regions.
   * Interface: input is an encoded context embedding; outputs are approximate flow magnitudes for a small set of representative corridors; internal losses are shaped by `signal_migration_flow_consistency`.

2. `MigrationFeedbackMonitor`

   * Role: a module that estimates whether the described situation corresponds to weak or strong feedback in migration dynamics.
   * Interface: input is a sequence of context embeddings; output is a feedback stability score influenced by `signal_migration_feedback_stability`.

3. `SocioTechnicalTensionObserver`

   * Role: a generic observer that extracts tension like summaries from flows, drivers, and feedbacks in socio technical settings, reusing the structure of `Tension_MIG`.
   * Interface: input is a structured representation of a socio technical system; outputs are scalar tension indicators and decomposed components.

### 7.3 Evaluation harness

We propose a simple evaluation harness for AI systems using Q109 components.

1. Task selection

   * Build a benchmark of questions and scenarios about global migration, regional migration crises, and long run demographic shifts.

2. Conditions

   * Baseline condition: the model answers questions without explicit Q109 derived modules.
   * TU condition: the model uses MigrationFlowHead, MigrationFeedbackMonitor, and the associated training signals.

3. Metrics

   * Factual accuracy on questions with known answers.
   * Structural consistency: absence of obvious contradictions between described drivers, barriers, and implied flows.
   * Regime awareness: ability to flag and treat high tension situations differently from low tension ones.

### 7.4 60 second reproduction protocol

A minimal protocol to let external users experience the effect of Q109 style encoding.

* Baseline setup:

  * Prompt: ask an AI system to explain how global migration flows have changed over recent decades and what drives them, without mentioning tension or TU.
  * Observation: record whether the explanation lists drivers but misses feedbacks, regime shifts, or structural imbalances.

* TU encoded setup:

  * Prompt: ask the same question but add an instruction to organize the explanation using flows, drivers, barriers, feedback, and migration tension; request explicit mention of stable versus unstable regimes.
  * Observation: record whether the explanation becomes more structured, with clearer separation between low tension and high tension episodes.

* Comparison metric:

  * Rate both answers on structure, explicit use of flows and drivers, treatment of feedback, and recognition of high tension regimes.
  * Optionally use several independent evaluators.

* What to log:

  * Prompts, full responses, and any auxiliary tension scores produced by Q109 modules.
  * This log enables later analysis of how the encoding changes reasoning behavior.

---

## 8. Cross problem transfer template

This block describes the components that Q109 produces and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `MigrationFlow_Field`

   * Type: field

   * Minimal interface:

     ```txt
     inputs: m, i, j, tau
     output: flow_rate >= 0
     ```

   * Preconditions:

     * `i` and `j` are distinct indices in a fixed region set `R_set`.
     * `tau` is in the fixed time window set `Tau_set`.
     * The state `m` belongs to the regular domain `M_reg` where flows are defined and finite.

2. ComponentName: `MigrationFeedback_Kernel`

   * Type: functional

   * Minimal interface:

     ```txt
     inputs: m, i, j, tau
     output: feedback_summary_vector
     ```

   * Preconditions:

     * The state `m` encodes enough information about past flows and driver changes along `(i, j)` to define a finite summary.
     * The summary is computed in a consistent way across states in a given encoding.

3. ComponentName: `Tension_MIG_Functional`

   * Type: functional

   * Minimal interface:

     ```txt
     inputs: I_flow(m), I_feedback(m), I_imbalance(m)
     output: Tension_MIG(m) >= 0
     ```

   * Preconditions:

     * `I_flow`, `I_feedback`, and `I_imbalance` are defined and finite for `m` in `M_reg`.
     * Weights `(w_flow, w_feedback, w_imbalance)` are fixed for the encoding.

### 8.2 Direct reuse targets

1. Target: Q098 (Anthropocene system dynamics)

   * Reused components: `MigrationFlow_Field`, `MigrationFeedback_Kernel`.
   * Why it transfers: Q098 needs channels that move population and capacity between regions when environmental and economic conditions shift, and migration flows provide such channels.
   * What changes: driver indicators are extended to include more detailed environmental metrics; feedback summaries include links between environmental policy and migration.

2. Target: Q100 (Environmental drivers of pandemic risk)

   * Reused components: `MigrationFlow_Field`, `Tension_MIG_Functional`.
   * Why it transfers: pathogen spread depends critically on human movements; high migration tension regimes often align with rapid changes in exposure networks.
   * What changes: flows are combined with health specific factors, and tension is interpreted as joint stress on health systems and migration systems.

3. Target: Q110 (Evolution of institutions)

   * Reused components: `MigrationFeedback_Kernel`, `Tension_MIG_Functional`.
   * Why it transfers: strong feedback loops between migration and institutions are a key driver of institutional change, which Q110 aims to encode.
   * What changes: the tension output is used as one input into InstitutionalChange_Pressure instead of being a final observable.

4. Target: Q125 (Multi agent AI dynamics)

   * Reused components: `MigrationFlow_Field` as a pattern, `MigrationFeedback_Kernel` as a template.
   * Why it transfers: agent movement between abstract states, roles, or platforms can be modeled analogously to migration between regions.
   * What changes: regions become states in an AI or digital ecosystem, flows are agent transitions, and drivers are incentives inside that ecosystem.

---

## 9. TU roadmap and verification levels

This block explains how Q109 fits into the TU verification ladder and what the next measurable steps are.

### 9.1 Current verification levels

* E_level: E1

  * A coherent effective layer encoding has been specified, including state space, fields, mismatch observables, tension functional, and singular set.
  * The encoding is precise enough to support falsifiable experiments on real and simulated data.

* N_level: N2

  * The narrative linking flows, drivers, barriers, feedbacks, and tension is explicit and non circular.
  * Counterfactual worlds S and U are described in terms of observable patterns, not hidden generative rules.

### 9.2 Next measurable step toward E2

To move from E1 to E2 for Q109, at least one of the following should be implemented and documented:

1. A data based implementation of Experiment 1 on a multi decade global migration dataset, including:

   * code that computes `Tension_MIG` over a chosen period,
   * published tension profiles for that period,
   * and at least one rejected encoding in `E_MIG` whose failures are clearly explained.

2. A simulation based implementation of Experiment 2 with:

   * at least one weak feedback model class and one strong feedback model class,
   * clear separation between tension distributions for the two classes under a chosen encoding,
   * and a public description of which aspects of the encoding were essential for that separation.

### 9.3 Long term role in the TU program

In the long run Q109 is expected to serve as:

* A reference node for flow based socio technical problems, similar to how Q001 frames spectral tension in mathematics.
* A convergence point where climate, conflict, economic inequality, and institutional dynamics connect through human mobility.
* A benchmark for AI systems that claim to reason about global social dynamics, by testing whether they can produce and use structured tension encodings rather than ad hoc narratives.

---

## 10. Elementary but precise explanation

This block gives a non technical explanation that remains aligned with the effective layer description.

People move between countries for many reasons. They look for better jobs, safer environments, and more stable futures. They may be pushed by conflict or environmental stress, or pulled by opportunities and family networks. Governments set rules and barriers that make moving easier or harder. Over time these choices and rules add up to large patterns of movement that shape whole regions.

The classical way to study migration is to collect data on who moves where and why, and to build theories that connect those flows to wages, populations, and policies. This has produced many useful ideas, but it is still difficult to see the global structure and to understand when the system is stable and when it is on the edge of crisis.

In the Tension Universe view we do not try to directly model every individual decision. Instead we ask:

* How can we summarize flows between regions over time.
* How can we summarize the main drivers, barriers, and feedbacks.
* How can we define a tension measure that becomes small when flows and drivers fit together in a stable way, and large when they do not.

We imagine a space of states where each state holds:

* an approximate map of how many people move between regions in a given period,
* a summary of drivers such as income differences, conflict, and climate stress,
* a summary of how policies and social reactions respond to past flows.

For each state we measure:

* how much observed flows differ from what a simple structural model would predict,
* how strongly past flows seem to change future drivers and barriers,
* how unbalanced the system is, for example when stressed regions keep losing people without getting better.

We combine these into a single number called migration tension. Low tension worlds are ones where flows and drivers match reasonably well and feedbacks mostly stabilize the system. High tension worlds are ones where flows keep surprising the structural model, feedbacks amplify problems, and imbalances grow.

This does not tell us exactly what will happen to global migration. It does not simulate every decision. What it does provide is:

* a structured way to talk about stability and instability in migration systems,
* a way to test whether a given encoding of flows and drivers is useful or trivial,
* and a set of components that can be reused in other problems where human movement plays a central role.

Q109 is the node in the Tension Universe that captures this view of global migration patterns. It is not a final answer, but a contract for how to describe, compare, and stress test different stories about how people move across the planet.
