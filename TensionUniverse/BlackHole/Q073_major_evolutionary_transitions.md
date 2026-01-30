<!-- QUESTION_ID: TU-Q073 -->
# Q073 · Mechanisms of major evolutionary transitions

## 0. Header metadata

```txt
ID: Q073
Code: BH_BIO_EVO_L3_073
Domain: Biology
Family: Evolutionary biology (major transitions)
Rank: S
Projection_dominance: I
Field_type: dynamical_field
Tension_type: incentive_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-30
````

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the **effective layer** of the Tension Universe (TU) framework.

* The goal of this document is to specify an effective-layer encoding of the problem of **major evolutionary transitions** and to outline associated tension observables, counterfactual worlds, and experiment patterns.
* It does **not** claim to prove or disprove any canonical statement in Section 1, nor to provide a complete historical reconstruction of actual transitions in natural evolution.
* It does **not** introduce any new theorem beyond what is already established or reasonably extrapolated from the cited literature.
* It does **not** specify any deep-layer TU axiom system, generative rule, or constructive mapping from raw biological data or simulations to internal TU fields.
  We only assume that such mappings can exist within TU-compatible models.
* All objects in this entry (state spaces `M`, observables, invariants, tension scores, counterfactual “worlds”) live at the effective layer and are subject to the TU charters on effective-layer scope, encoding and fairness, and tension scales.

Any concrete use of this entry in empirical or simulated work must:

* choose a specific encoding instance that respects the TU Effective Layer, TU Encoding and Fairness, and TU Tension Scale charters, and
* treat the resulting tension measurements as properties of that encoding, not as direct proofs about historical reality.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical question behind Q073 can be stated as follows:

How can the major evolutionary transitions in the history of life be described and partially explained by general mechanisms that reorganize units of selection, information channels, and cooperation, such that new higher-level individuals or organizations emerge and remain stable over evolutionary timescales?

Classical examples of major transitions include:

* independent replicators to genetic systems with chromosomes,
* prokaryotic cells to eukaryotic cells,
* unicellular organisms to multicellular organisms,
* solitary individuals to eusocial colonies,
* non-symbolic communication to language-using societies.

Across these cases, three structural changes recur:

1. Units that were capable of independent replication become parts of a larger unit.
2. There is a reorganization of information storage, transmission, and control.
3. Conflicts between lower-level and higher-level units are managed or suppressed, at least within certain conditions.

The canonical problem is to identify and characterize the mechanisms that:

* reduce conflicts and align incentives across levels,
* enable robust information integration and division of labor,
* make higher-level individuals or organizations evolutionarily stable and evolvable.

### 1.2 Status and difficulty

The idea of major transitions is well established, and there is a substantial body of work describing:

* which transitions have occurred in the history of life,
* qualitative similarities among them,
* models for particular cases such as evolution of multicellularity and eusociality.

However, there is no single widely accepted, quantitative theory that:

* unifies all major transitions under a small set of general mechanisms,
* provides clear, comparable metrics for multi-level alignment and information integration,
* predicts when major transitions are possible, likely, or blocked in a given evolutionary landscape.

Open difficulties include:

* describing transitions in terms that apply across very different substrates (biochemical, ecological, cultural),
* defining precise notions of individuality and fitness at multiple levels,
* understanding how transitions interact with constraints such as mutation rates, population structures, and ecological feedbacks.

Q073 focuses on mechanisms that can be described at an effective layer, with emphasis on multi-level incentive structures, information integration, and dynamical stability, without committing to a single substrate-specific micro-model.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q073 serves as:

1. A reference node for **incentive_tension** problems in biology, where selection pressures at different levels must be reconciled.
2. A bridge from prebiotic and molecular questions (for example Q071 Origin of life, Q072 Origin of the genetic code, Q078 Genotype–phenotype mapping) to large-scale biosphere and social dynamics (for example Q080, Q098, Q107).
3. A source of reusable concepts and components for:

   * multi-level selection,
   * cooperation and conflict management,
   * emergence and stabilization of new levels of individuality,

   with intended transfer to non-biological domains including complex social systems and multi-agent AI.

### References

1. J. Maynard Smith, E. Szathmary, “The Major Transitions in Evolution”, Oxford University Press, 1995.
2. E. Szathmary, “The origin of replicators and reproducers”, Philosophical Transactions of the Royal Society B, 2006.
3. R. E. Michod, “Darwinian Dynamics: Evolutionary Transitions in Fitness and Individuality”, Princeton University Press, 1999.
4. S. Okasha, “Evolution and the Levels of Selection”, Oxford University Press, 2006.

---

## 2. Position in the BlackHole graph

This block records how Q073 is positioned in the BlackHole graph. All edges reference concrete components or tension patterns defined at the effective layer.

### 2.1 Upstream problems

These nodes provide prerequisites and reusable frameworks.

* Q071 (Origin of life, BH_BIO_ORIGIN_L3_071)
  Reason: Supplies baseline replicator and minimal reproducer models that Q073 extends into multi-level organizational transitions, using the `MultiLevelSelection_TensionFunctional` defined in Section 8.1.

* Q072 (Origin of the genetic code, BH_BIO_GENETIC_CODE_L3_072)
  Reason: Provides information-channel and encoding concepts that feed into `info_integration_L` and higher-level organizing units in Q073.

* Q078 (From genotype to phenotype, BH_BIO_GENOTYPE_PHENOTYPE_L3_078)
  Reason: Defines mapping structures from genotype to phenotype that become more layered and hierarchical in `MultiLevelSelection_TensionFunctional`.

### 2.2 Downstream problems

These nodes reuse Q073 components directly.

* Q080 (Limits of biosphere adaptability, BH_BIO_ADAPT_L3_080)
  Reason: Reuses `OrganizationalLevel_Descriptor` to evaluate how the number and diversity of organizational levels affect long-term adaptability.

* Q098 (Anthropocene system dynamics, BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: Uses `TransitionScenario_Template` to model human-driven transitions in planetary-scale socio-ecological systems.

* Q107 (Mechanisms of large scale collective action, BH_SOC_COLLECTIVE_L3_107)
  Reason: Reuses `MultiLevelSelection_TensionFunctional` to describe incentive alignment between individuals, organizations, and institutions.

* Q125 (Multi agent AI dynamics, BH_AI_MULTIAGENT_L3_125)
  Reason: Reuses `TransitionScenario_Template` to construct World T and World F scenarios for emergent higher-level AI organizations.

### 2.3 Parallel problems

Parallel problems share similar tension types but do not depend directly on Q073 components.

* Q075 (Fundamental mechanisms of aging, BH_BIO_AGING_L3_075)
  Reason: Both Q075 and Q073 involve long-term tradeoffs between individual-level fitness and system-level maintenance under incentive_tension.

* Q104 (Dynamics of wealth and income inequality, BH_SOC_INEQUALITY_L3_104)
  Reason: Both study misalignment and partial alignment of incentives across nested levels of organization.

### 2.4 Cross-domain edges

These edges show transfer of Q073 concepts beyond biology.

* Q105 (Prediction of systemic crashes, BH_SOC_SYSTEMIC_RISK_L3_105)
  Reason: Uses `TransitionScenario_Template` to model breakdowns and reconfigurations of cooperative structures in complex systems.

* Q121 (AI alignment problem, BH_AI_ALIGNMENT_L3_121)
  Reason: Adapts `MultiLevelSelection_TensionFunctional` to alignment between agents, overseers, and institutions in artificial systems.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is confined to the effective layer. It defines state spaces, observables, invariants, singular sets, and encoding classes for Q073, without specifying any deep TU generative rules or mappings from raw data to internal fields.

### 3.1 State space

Let

```txt
M
```

be the semantic state space for Q073. Each state `m` in `M` represents a coarse-grained evolutionary configuration over a finite time window, including:

* a finite list of organizational levels, such as:

  * level 1: genetic elements,
  * level 2: cells,
  * level 3: organisms,
  * level 4: groups or colonies,
  * level 5: societies,

* a finite set of functional roles at each level (for example metabolic roles, reproductive roles, defense roles),

* continuous summaries of population densities, resource distributions, and interaction rates for each level and role.

Minimal assumptions:

* For any finite choice of levels, roles, and time window, there exist states `m` in `M` that encode the relevant configuration.
* Internal details of how these encodings are constructed from empirical data or simulations are not described here.

### 3.2 Effective fields and observables

At the effective layer, we introduce the following observables and fields on `M`.

1. Cross-level fitness contributions

```txt
fitness_i(m) in R
```

* For each level index `i`, `fitness_i(m)` summarizes how selection acts on units at level `i` within the configuration `m`.
* It may include combined effects of survival, reproduction, and transmission.

2. Interaction structure at each level

```txt
interaction_graph_i(m)
```

* Effective descriptor of who interacts with whom at level `i`.
* For Q073, it is treated as a compressed object that can be summarized by derived scalars such as clustering, connectivity, or motif frequencies.

3. Multi-level information integration

```txt
info_integration_L(m) >= 0
```

* Scalar that summarizes how strongly decisions or behaviors at a higher level depend on information aggregated across `L` lower levels.
* Values near zero indicate weak cross-level integration; larger values indicate stronger integration.

4. Conflict and cooperation summaries

```txt
conflict_cost_i(m)     >= 0
cooperation_gain_i(m)  >= 0
```

* For each level `i`:

  * `conflict_cost_i(m)` measures effective losses due to conflict between units at level `i` and higher-level organization.
  * `cooperation_gain_i(m)` measures effective gains due to cooperative structures at or above level `i`.

5. Invariants

We define two invariants that help interpret configurations.

* Cross-level alignment index

  ```txt
  I_align(m) = sum over i of w_i * A_i(m)
  ```

  where:

  * `w_i >= 0` are fixed weights with `sum over i of w_i = 1`,
  * `A_i(m)` is an alignment score at level `i`, defined from `fitness_i(m)`, `conflict_cost_i(m)`, and `cooperation_gain_i(m)`, with normalization

    ```txt
    0 <= A_i(m) <= 1
    ```

  so that `I_align(m)` lies in `[0, 1]` and increases when incentives at different levels are more aligned.

* Information integration index

  ```txt
  I_info(m) = g(info_integration_L(m))
  ```

  for a simple nondecreasing function `g` such that

  ```txt
  I_info(m) >= 0
  ```

  and higher `I_info(m)` indicates stronger multi-level information integration.

These invariants are not assumed to be conserved. They are used to distinguish high-tension pre-transition configurations from lower-tension post-transition configurations.

6. Transition tension observable (informal placeholder)

We introduce a nonnegative scalar observable

```txt
Tension_transition(m) >= 0
```

which summarizes, at the effective layer, the overall incentive_tension for multi-level organization in configuration `m`. Its detailed decomposition into components will be specified in Section 4.1. All references to transition tension in the tensor and experiments use this scalar.

### 3.3 Effective tension tensor components

Consistent with the TU core decisions, we introduce an effective tension tensor:

```txt
T_ij(m) = S_i(m) * C_j(m) * Tension_transition(m) * lambda(m) * kappa
```

where:

* `S_i(m)` are source-like factors for level `i`, summarizing how strongly selection and innovation are pushing configurations at that level.
* `C_j(m)` are receptivity-like factors for level `j`, summarizing how capable the structure at that level is of absorbing and stabilizing new cooperative patterns.
* `Tension_transition(m)` is the nonnegative scalar transition tension observable described above and defined in detail in Section 4.1.
* `lambda(m)` is a convergence-state factor indicating whether the local evolutionary dynamics near `m` are convergent, recursive, divergent, or chaotic.
* `kappa` is a scaling constant for the magnitude of tension in Q073.

The detailed indexing of `i` and `j` is not specified at this layer; it is sufficient that, for each `m` in `M`, `T_ij(m)` is finite wherever needed.

### 3.4 Singular set and domain restrictions

Some observables may be undefined or inconsistent in certain coarse-grained descriptions. To handle this, we define a singular set:

```txt
S_sing = {
  m in M :
    Tension_transition(m) is undefined or not finite, or
    any fitness_i(m), conflict_cost_i(m), cooperation_gain_i(m), info_integration_L(m)
    is undefined or not finite
}
```

We restrict all Q073 reasoning at the effective layer to the regular subset:

```txt
M_reg = M \ S_sing
```

When an experiment or protocol would produce a state in `S_sing`, this is treated as “out of domain” for Q073. Such states do not count as evidence for or against any particular claim about mechanisms of major transitions.

### 3.5 Semantics

The metadata field `Semantics: hybrid` is implemented as follows:

* Discrete indices for levels, roles, and units (for example level labels, role categories, group identifiers).
* Continuous-valued summaries for densities, fitness contributions, interaction strengths, conflict and cooperation scores, and information integration indices.

This hybrid structure is used consistently in all observables and in all experiment patterns defined in Section 6.

### 3.6 Encoding class and fairness constraints

To make Q073 encodings auditable and comparable, we define an encoding class

```txt
E = (D, F, W, L)
```

with the following components:

1. `D` (data-to-state mapping)

   * A family of rules that map raw data or simulation outputs into states `m_data` in `M_reg`.

   * Examples include:

     * procedures that aggregate digital evolution logs into level structures, fitness summaries, and interaction descriptors;
     * procedures that encode microbial community experiments into the observables listed in Section 3.2.

   * `D` must be specified **before** any tension analysis and must not be tuned after seeing desired or undesired tension patterns.

2. `F` (tension functional family)

   * A family of functional forms that map observables

     ```txt
     { fitness_i, conflict_cost_i, cooperation_gain_i, info_integration_L }
     ```

     into the component terms `DeltaS_misalignment(m)`, `DeltaS_coop(m)`, `DeltaS_info(m)` and their combination `Tension_transition(m)` as defined in Section 4.1.

   * `F` must be chosen so that each term is well defined, nonnegative, and interpretable across all states in `M_reg`.

3. `W` (weights and thresholds)

   * A set of admissible parameter choices for:

     ```txt
     alpha, beta, gamma,
     u_ij, v_i,
     I_info_target
     ```

   * Each admissible encoding instance must pick a point in `W` **before** computing any tension values for the systems under study.

   * Retuning parameters in response to observed results is treated as defining a **new** encoding instance, which must be evaluated separately.

4. `L` (library of model and environment classes)

   * A set of model classes and environment classes that Q073 encodings may be applied to in experiments, including:

     * digital evolution landscapes with and without mechanisms that support multi-level organization,
     * empirical or experimental microbial systems with and without emergent higher-level traits.

   * For each experiment, the relevant subset of `L` must be declared in advance.

An encoding instance for Q073 consists of a specific choice

```txt
E* = (D*, F*, W*, L*)
```

that satisfies the TU Effective Layer, TU Encoding and Fairness, and TU Tension Scale charters. All experiments in Section 6 are understood to operate under a fixed admissible encoding instance `E*`. Changing `E*` defines a new encoding that must be evaluated on its own terms.

---

## 4. Tension principle for this problem

This block states how Q073 is formulated as a tension problem at the effective layer.

### 4.1 Core transition tension functional

We define an effective transition tension functional on `M_reg`:

```txt
Tension_transition(m) =
  alpha * DeltaS_misalignment(m) +
  beta  * DeltaS_coop(m) +
  gamma * DeltaS_info(m)
```

where:

* `alpha > 0`, `beta > 0`, `gamma > 0` are fixed coefficients chosen once for a given encoding instance `E*`,
* `DeltaS_misalignment(m)` summarizes misalignment of fitness across levels,
* `DeltaS_coop(m)` summarizes net conflict cost minus cooperation gain,
* `DeltaS_info(m)` summarizes deficiencies in information integration.

Each term is nonnegative, so

```txt
Tension_transition(m) >= 0
```

for all `m` in `M_reg`.

A simple implementation, within the family `F*`, is:

```txt
DeltaS_misalignment(m) =
  sum over i < j of u_ij * |fitness_i(m) - f_ij_ref(m)|

DeltaS_coop(m) =
  sum over i of v_i * max(0, conflict_cost_i(m) - cooperation_gain_i(m))

DeltaS_info(m) =
  max(0, I_info_target - I_info(m))
```

with:

* `u_ij >= 0`, `v_i >= 0` fixed weights,
* `f_ij_ref(m)` representing reference fitness contributions at level `i` compatible with stable higher-level units, given the configuration at level `j`,
* `I_info_target > 0` a target integration level.

For any admissible encoding instance `E*`, all of `alpha`, `beta`, `gamma`, `u_ij`, `v_i`, and `I_info_target` must lie inside the admissible set `W*` specified in Section 3.6. Retuning them after seeing tension results constitutes a different encoding.

### 4.2 Major transitions as tension-reducing reorganizations

At the effective layer, Q073 encodes the following principle:

* A major evolutionary transition corresponds to a reorganization of organizational levels, roles, and information channels such that:

  * `Tension_transition(m_pre)` is high for pre-transition states,
  * `Tension_transition(m_post)` is significantly lower for post-transition states,

  across a nontrivial range of environments and perturbations, while global adaptability does not decrease.

In this view, mechanisms of major transitions are:

* ways of reconfiguring who reproduces, who controls reproduction, and how information flows, so that cross-level tensions are systematically reduced and higher-level units become stable.

### 4.3 Failure modes and limits

The same functional allows description of failure modes:

* If, for a given ecological and mutational regime, all accessible configurations `m` with strong cooperation or new levels of organization retain high `Tension_transition(m)`, then mechanisms of major transitions are blocked or severely constrained.
* If transitions occur but `Tension_transition(m_post)` is only temporarily reduced and then rises again under small perturbations, the transition is fragile and unlikely to persist over macroevolutionary timescales.

Q073 does not assert that all accessible transitions will occur. It only structures how to describe when mechanisms are available, blocked, robust, or fragile.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer:

* World T: environments and parameters that support robust mechanisms for major transitions.
* World F: environments and parameters that block or severely limit such mechanisms.

All references to tension in these worlds are understood as tension values computed under a fixed admissible encoding instance `E*`.

### 5.1 World T (transition-enabled world)

In World T, the following patterns are observed for states `m_T` in `M_reg` that represent the long-term history of life:

1. Existence of multi-level stable units

   * Over time, new higher-level units (for example stable multicellular lineages, eusocial colonies) appear and persist.
   * For many such `m_T`, there are identifiable pre-transition states `m_pre` and post-transition states `m_post` with

     ```txt
     Tension_transition(m_post) << Tension_transition(m_pre)
     ```

     under the same encoding parameters.

2. Cross-level alignment improves with transitions

   * For higher-level units after transitions:

     ```txt
     I_align(m_post) > I_align(m_pre)
     ```

     for a range of pre and post pairs, indicating better alignment between lower-level and higher-level incentives.

3. Information integration becomes robust

   * For post-transition states, `I_info(m_post)` exceeds a threshold `I_info_target` and remains above this threshold under moderate perturbations to interaction structures and environments.

4. Repeated innovation

   * Multiple distinct transitions occur over time, each reducing tension in its own region of configuration space, leading to an overall increase in organizational depth and diversity.

### 5.2 World F (transition-blocked world)

In World F, environments and parameters are such that mechanisms for major transitions fail to produce robust higher-level units.

1. Persistent high transition tension

   * For all states `m_F` that reflect the long-term history:

     ```txt
     Tension_transition(m_F) >= delta_block
     ```

     for some `delta_block > 0`, and attempts to form higher-level units do not reduce this tension sustainably.

2. Misalignment cannot be resolved

   * For any attempted configuration that resembles a higher-level unit, either:

     * lower-level fitness is severely compromised, or
     * higher-level structures collapse quickly.

   * There are no stable pairs `m_pre`, `m_post` with sustained tension reduction.

3. Information integration remains weak

   * Attempts to integrate information across levels either do not emerge or are fragile, with

     ```txt
     I_info(m_F) << I_info_target
     ```

     in most states that resemble complex organizations.

4. Rich microevolution without major transitions

   * Lower-level evolution, for example within single-cell lineages, may be rich, but durable transitions to new higher-level individuals are absent or extremely rare.

### 5.3 Interpretive note

These counterfactual worlds do not construct detailed microdynamics or specify how states in `M` are derived from data. They only assert that, if faithful encodings of histories are available under an admissible encoding instance `E*`, then the patterns of `Tension_transition`, `I_align`, and `I_info` would differ systematically between transition-enabled and transition-blocked worlds.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that test Q073 encodings at the effective layer. They do not prove or disprove any particular historical claim, but they can falsify specific choices of observables and tension functionals within the encoding class `E`.

All experiments in this section are understood to be carried out under a fixed admissible encoding instance

```txt
E* = (D*, F*, W*, L*)
```

as defined in Section 3.6.

### Experiment 1: Digital evolution landscapes for transitions

**Goal**

Test whether a given implementation of `Tension_transition` can distinguish simulated environments that support major transitions from environments that block them.

**Setup**

* Use a digital evolution platform in which agents reproduce, interact, and can evolve cooperative structures.

* Define two classes of simulation environments, both belonging to the library component `L*` of the chosen encoding:

  * Class T: environments known from prior work or design to allow the evolution of higher-level units, such as stable cooperative groups with division of labor.
  * Class F: environments tuned so that cooperation is unstable or multi-level units cannot persist.

* For each run, construct an effective state `m_data` in `M_reg` using the data-to-state mapping `D*`. These states summarize:

  * organizational levels present,
  * interaction patterns,
  * cross-level fitness contributions,
  * conflict and cooperation summaries,
  * information integration estimates.

**Protocol**

1. For a collection of runs in Class T and Class F, sample time points representing pre-transition, transition, and post-transition stages when applicable.

2. For each sampled time point, derive the corresponding `m_data` state via `D*`.

3. Compute `DeltaS_misalignment(m_data)`, `DeltaS_coop(m_data)`, `DeltaS_info(m_data)`, and then `Tension_transition(m_data)` using the tension functional family `F*` and the parameter choice in `W*`.

4. Compare distributions of `Tension_transition` between:

   * pre and post states in Class T,
   * comparable states in Class F.

5. Optionally, repeat computations under admissible parameter variations within `W*` that are declared in advance.

**Metrics**

* Mean and variance of `Tension_transition` for pre and post states in Class T.
* Mean and variance of `Tension_transition` for comparable states in Class F.
* Effect size of tension reduction across transitions in Class T compared to changes in Class F.
* Robustness of the observed differences under admissible parameter variations.

**Falsification conditions**

* If, for all admissible parameter choices in `W*`, Class T and Class F show no systematic difference in `Tension_transition` patterns, the current encoding instance `E*` for Q073 is considered falsified or too weak to capture mechanisms of major transitions.
* If Class F environments, which lack stable higher-level units by design, regularly display lower `Tension_transition` than Class T post-transition states, the encoding instance is considered misaligned with the intended incentive_tension interpretation.

**Semantics implementation note**

The experiment uses hybrid semantics consistent with Section 3.5: discrete indices for levels, roles, and agents, combined with continuous summaries for densities, fitness contributions, and integration scores.

**Boundary note**

Falsifying a particular encoding instance `E*` at the effective layer does not constitute a solution to the canonical problem of major evolutionary transitions. It also does not claim that no alternative encoding or model class could succeed. It only shows that this specific choice of `D*`, `F*`, `W*`, and `L*` fails to capture the intended tension patterns.

---

### Experiment 2: Multi-level selection in microbial communities

**Goal**

Assess whether the Q073 tension encoding can distinguish microbial systems that exhibit emergent higher-level organization from systems that remain purely lower-level.

**Setup**

* Select empirical or experimental datasets on evolving microbial communities, including:

  * systems in which group-level traits such as biofilm formation, spatial structure, or division of labor are known to emerge and persist,
  * control systems in which such group-level traits are absent or transient.

* For each system, construct effective states `m_data` in `M_reg` using `D*`, describing:

  * levels (cells, microcolonies, macro-colonies),
  * interaction patterns (for example local cooperation, cheating, spatial proximity),
  * inferred fitness contributions at different levels,
  * conflict and cooperation summaries,
  * information integration measures derived from observed coordination.

**Protocol**

1. For each system, select time points representative of initial, intermediate, and late stages of evolution.

2. Encode each selected time point as a state `m_data` in `M_reg` via `D*`.

3. Compute `Tension_transition(m_data)` for each time point using `F*` and `W*`.

4. Group results into:

   * systems with emergent higher-level traits,
   * systems without such traits.

5. Compare tension trajectories and steady-state values across the two groups.

**Metrics**

* For systems with emergent higher-level traits:

  * change in `Tension_transition` over time,
  * relation between tension reduction and observed stability of group-level traits.

* For control systems:

  * lack of sustained tension reduction,
  * persistence of high `DeltaS_misalignment` or `DeltaS_coop`.

* Separation between tension profiles of the two groups.

**Falsification conditions**

* If systems with clear emergent higher-level traits do not show any systematic tension reduction compared to controls, the encoding instance `E*` is considered weak or misaligned and should be revised.
* If control systems systematically show lower `Tension_transition` than systems with stable higher-level traits, the encoding contradicts the intended interpretation of major transitions and is considered falsified.

**Semantics implementation note**

The analysis uses hybrid semantics: discrete labels for levels and traits, continuous-valued summaries for fitness, interaction strengths, and integration metrics, consistent with the metadata choice in Section 3.5.

**Boundary note**

Falsifying a particular encoding instance `E*` for Q073 shows that this way of summarizing and scoring multi-level organization does not track emergent higher-level traits in the tested systems. It does not provide a complete explanation of any specific transition, and it does not preclude alternative encodings or model families from succeeding.

---

## 7. AI and WFGY engineering spec

This block describes how Q073 can be used to design and evaluate AI systems within the WFGY framework at the effective layer.

### 7.1 Training signals

The following training signals can be derived from Q073 observables under a chosen encoding instance `E*`.

1. `signal_multilevel_alignment`

   * Definition: a scalar signal constructed from `I_align(m)` and `DeltaS_misalignment(m)`, such as

     ```txt
     signal_multilevel_alignment(m) =
       I_align(m) - c_misalign * DeltaS_misalignment(m)
     ```

     with a fixed coefficient `c_misalign > 0`.

   * Purpose: reward internal representations that reflect higher alignment between units at different levels when the context describes successful major transitions or stable multi-level organizations.

2. `signal_cooperation_stability`

   * Definition: a penalty proportional to `DeltaS_coop(m)` over contexts where long-lived cooperative units are described.

   * Purpose: discourage reasoning patterns that imply unstable cooperation in scenarios where persistent higher-level organizations are assumed.

3. `signal_transition_tension_score`

   * Definition: directly equal to `Tension_transition(m)` treated as an auxiliary loss or regularization term.

   * Purpose: provide a continuous indicator of how well a model’s internal state matches a low-tension configuration compatible with major transitions.

4. `signal_transition_contrast`

   * Definition: a contrastive signal computed as the difference in `Tension_transition` between pairs of contexts labeled as pre-transition and post-transition.

   * Purpose: encourage the model to recognize and separate configurations before and after major transitions.

### 7.2 Architectural patterns

Q073 suggests several AI module patterns.

1. `MultiLevelSelectionHead`

   * Role: given an internal embedding of a biological or organizational scenario, estimate

     * which levels are relevant,
     * approximate `fitness_i(m)` and cross-level alignment indicators.

   * Interface:

     * Input: contextual embedding representing a description of an evolutionary or organizational system.
     * Output: level-wise alignment scores and a summary of `I_align(m)`.

2. `TransitionPatternDetector`

   * Role: detect signatures of major transitions in a sequence of states, such as

     * emergence of new levels,
     * reduction of conflict and increase of cooperation gains,
     * increased information integration.

   * Interface:

     * Input: sequence of state-like embeddings or scenario descriptions.
     * Output: scores indicating likelihood and type of transition.

3. `OrganizationalLevel_Encoder`

   * Role: produce `OrganizationalLevel_Descriptor` objects from text or structured data as defined in Section 8.1.

   * Interface:

     * Input: description of a system’s actors, interactions, and control channels.
     * Output: compact representation of organizational levels that can be passed to tension evaluation modules.

### 7.3 Evaluation harness

An evaluation harness for AI systems using Q073 modules might include:

1. Task families

   * Explanatory tasks:

     * explain why certain transitions occurred, for example unicellular to multicellular, in terms of conflicts, cooperation, and information integration.

   * Predictive tasks:

     * judge whether a described system is likely to support a future major transition under specified conditions.

2. Conditions

   * Baseline condition:

     * the model operates without explicit Q073-derived modules or signals.

   * TU-augmented condition:

     * the model uses `MultiLevelSelectionHead`, `TransitionPatternDetector`, and associated signals.

3. Metrics

   * Consistency of multi-level reasoning:

     * frequency of contradictions in fitness definitions across levels.

   * Use of structured concepts:

     * fraction of explanations that explicitly mention mechanisms aligned with Q073, such as conflict suppression, division of labor, and information integration.

   * Robustness:

     * stability of answers when scenarios are perturbed in ways that should or should not affect transition feasibility.

### 7.4 60-second reproduction protocol

A minimal protocol for external users to experience the impact of Q073 encoding.

* Baseline setup:

  * Prompt: ask an AI system to explain “What are major evolutionary transitions and why did they happen?” without any mention of tension or multi-level selection.
  * Observation: check whether the explanation is a loose list of historical events or a structured account of mechanisms.

* Q073-encoded setup:

  * Prompt: same question, with an instruction to organize the explanation around

    * incentives at different levels,
    * cooperation and conflict management,
    * information integration and new levels of individuality.

  * Observation: check whether the explanation

    * identifies conflicts between lower and higher levels,
    * explains how cooperation became stable,
    * highlights changes in information storage and control.

* Comparison metric:

  * Use a simple rubric to rate

    * clarity of multi-level structure,
    * explicit discussion of mechanisms,
    * avoidance of circular or purely narrative explanations.

* What to log:

  * Prompts, full responses, and any Q073-derived tension scores or module outputs.
  * This allows later inspection of how Q073 components influenced the reasoning, without exposing any deep TU generative rules.

---

## 8. Cross problem transfer template

This block describes reusable components from Q073 and their direct reuse targets.

### 8.1 Reusable components produced by this problem

1. ComponentName: `MultiLevelSelection_TensionFunctional`

   * Type: functional

   * Minimal interface:

     ```txt
     Inputs: {
       fitness_levels: vector of fitness_i values across levels,
       conflict_costs: vector of conflict_cost_i values,
       cooperation_gains: vector of cooperation_gain_i values,
       info_integration: scalar info_integration_L
     }
     Output: {
       Tension_transition: nonnegative scalar,
       decomposed_terms: (DeltaS_misalignment, DeltaS_coop, DeltaS_info)
     }
     ```

   * Preconditions:

     * Inputs must be derived from a coherent description of a multi-level system where levels and roles are well defined.
     * All inputs must be finite real numbers.

2. ComponentName: `OrganizationalLevel_Descriptor`

   * Type: field

   * Minimal interface:

     ```txt
     Inputs: {
       units: list of entities at each level,
       interactions: summary of interaction patterns,
       control_channels: summary of who influences whom
     }
     Output: {
       levels: structured list of organizational levels,
       role_map: mapping from units to roles,
       topology_summary: compact representation of interaction and control structure
     }
     ```

   * Preconditions:

     * There must be a finite and identifiable set of units and interactions.
     * Control channels must be described at least qualitatively.

3. ComponentName: `TransitionScenario_Template`

   * Type: experiment_pattern

   * Minimal interface:

     ```txt
     Inputs: {
       model_class: description of biological, social, or artificial systems,
       environment_params: key parameters controlling interactions and selection pressures
     }
     Output: {
       world_T_spec: scenario with mechanisms enabling major transitions,
       world_F_spec: scenario with mechanisms blocked,
       evaluation_protocol: how to compute and compare Tension_transition
     }
     ```

   * Preconditions:

     * The model class must support clear identification of levels, interactions, and selection pressures.
     * It must be possible to vary environment parameters to enable or block transitions.

### 8.2 Direct reuse targets

1. Target: Q080 (Limits of biosphere adaptability, BH_BIO_ADAPT_L3_080)

   * Reused component: `OrganizationalLevel_Descriptor`.
   * Why it transfers: global adaptability depends on how many organizational levels exist and how they distribute functions; this descriptor quantifies that structure.
   * What changes: emphasis shifts from mechanisms of transitions to the relation between organizational depth and adaptability limits.

2. Target: Q098 (Anthropocene system dynamics, BH_EARTH_ANTHROPOCENE_L3_098)

   * Reused component: `TransitionScenario_Template`.
   * Why it transfers: human-driven systemic changes can be framed as transitions or failed transitions in socio-ecological organization.
   * What changes: `model_class` becomes coupled human–environment systems rather than purely biological populations.

3. Target: Q107 (Mechanisms of large scale collective action, BH_SOC_COLLECTIVE_L3_107)

   * Reused component: `MultiLevelSelection_TensionFunctional`.
   * Why it transfers: large-scale collective action problems are governed by misaligned incentives between individuals, organizations, and institutions, analogous to multi-level selection.
   * What changes: fitness and cooperation are interpreted in terms of payoffs, norms, and institutional stability instead of reproduction.

4. Target: Q125 (Multi agent AI dynamics, BH_AI_MULTIAGENT_L3_125)

   * Reused components: `TransitionScenario_Template` and `MultiLevelSelection_TensionFunctional`.
   * Why it transfers: emergent higher-level AI organizations, for example coalitions or institutions of agents, can be studied with the same transition-enabled versus transition-blocked scenarios and tension functionals.
   * What changes: levels correspond to agents, clusters of agents, and meta-level coordination mechanisms within AI ecosystems.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * Q073 provides a coherent effective-layer encoding of mechanisms of major transitions, including:

    * state space `M`,
    * observables and `Tension_transition`,
    * an explicit encoding class `E = (D, F, W, L)`,
    * at least two discriminating experiments with falsification conditions.

* N_level: N1

  * Q073 provides:

    * a structured narrative in terms of World T and World F,
    * clear graph placement and transfer components,
    * an elementary explanation that aligns with the encoding.

### 9.2 Next measurable step toward E2

To reach E2, at least one of the following should be implemented and documented under a clearly specified encoding instance `E*`:

1. A working prototype that applies `MultiLevelSelection_TensionFunctional` to real or simulated systems, for example digital evolution and microbial communities, producing tension profiles for pre and post transitions and making the results publicly available.
2. A systematic comparative study that:

   * defines a library of model classes and environments, both transition-enabled and transition-blocked,
   * applies Q073 encodings to each case,
   * reports success and failure cases, and refines the encoding based on falsification results.

Both steps operate solely at the effective layer, using observable summaries, and do not require exposing any deep TU generative rule.

### 9.3 Long-term role in the TU program

In the broader Tension Universe program, Q073 is intended to:

* Serve as the central node for understanding how multi-level incentive_tension can be reorganized to create new higher-level individuals.

* Provide templates for analyzing transitions in other domains, including

  * socio-technical systems,
  * economic and political structures,
  * multi-agent AI ecosystems.

* Help calibrate which aspects of major transitions are universal and which are substrate-specific, using the same tension-based descriptors.

---

## 10. Elementary but precise explanation

Major evolutionary transitions are moments in the history of life when the basic units of evolution changed. Examples include:

* cells joining to form multicellular organisms,
* individual insects forming eusocial colonies,
* human groups developing language and complex societies.

Before a transition, there are many small units that each try to survive and reproduce on their own. They can cooperate, but they also have reasons to cheat or compete. After a successful transition, many of these units behave as parts of a larger individual that has its own way to survive and reproduce.

In the Tension Universe view, this is described with a transition tension number.

* For a given configuration of life, a state is built that summarizes:

  * which levels exist, for example genes, cells, organisms, groups,
  * how they interact,
  * how well their incentives line up,
  * how much information is shared and used across levels.

* From this state, a scalar `Tension_transition` is computed:

  * high tension means strong conflicts between levels, unstable cooperation, and weak information integration,
  * low tension means better alignment, stable cooperation, and strong information integration.

A major transition can then be read as:

* moving from a high-tension configuration with many conflicts and fragile groups
* to a low-tension configuration where cooperation is stable, roles are specialized, and information flows well,

without losing the ability of the system to adapt and evolve.

Two kinds of worlds can be imagined:

* In a transition-enabled world, it is possible to find ways to reorganize life so that the tension drops and new higher-level individuals become stable.
* In a transition-blocked world, any attempt at such reorganization either fails quickly or keeps tension high.

Q073 does not claim to have a final theory of how every transition actually happened. Instead, it provides:

* a way to measure how aligned or misaligned different levels are,
* a way to describe when a proposed mechanism truly reduces tension,
* tools that can be applied not only to biological evolution, but also to large-scale cooperation in human societies and multi-agent AI systems.

In this sense, Q073 is a structured way to talk about how small things become parts of larger things, in a form that can be checked, compared, and tested rather than only listed as a sequence of historical events.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S-problem collection.

### Scope of claims

* The goal of this document is to specify an **effective-layer encoding** of the Q073 problem on mechanisms of major evolutionary transitions.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved, nor as a complete historical reconstruction of any specific transition.

### Effective-layer boundary

* All objects used here, including the state space `M`, observables, invariants, tension scores, counterfactual worlds, and experiment patterns, live at the effective layer of the TU framework.
* No deep-layer TU axiom system, generative rule, or raw data mapping is specified. Any such mapping belongs to separate work that instantiates an encoding instance `E* = (D*, F*, W*, L*)`.
* The same canonical problem can have multiple TU encodings. This page only describes one family of encodings.

### Encoding and fairness

* Any concrete use of this page must declare a specific encoding instance `E*` within the encoding class `E = (D, F, W, L)` defined in Section 3.6.
* All choices of data-to-state mapping `D*`, functional forms `F*`, and parameter sets `W*` must be fixed **before** computing tension values for the systems under study.
* Retuning `D*`, `F*`, or `W*` in response to observed results defines a new encoding instance that must be evaluated separately and cannot be retroactively applied to previous experiments.
* Comparisons between systems, environments, or models are only meaningful when performed under the same declared encoding instance `E*`.

### Falsifiability and experiments

* The experiments in Section 6 are designed to **falsify or refine** particular encoding instances of Q073 at the effective layer.
* If an encoding instance `E*` fails the falsification criteria, this indicates that the corresponding summary choice for `M`, observables, and `Tension_transition` is inadequate for the intended role of Q073.
* Falsifying an encoding instance does not solve the canonical problem and does not rule out the existence of other encodings or models that could succeed.
* Positive experimental support for an encoding instance, when obtained under transparent and reproducible conditions, provides evidence that the corresponding tension structure is a useful tool for organizing reasoning about major transitions, but it does not elevate the encoding to a fundamental theory of evolution.

### Charter relations

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

