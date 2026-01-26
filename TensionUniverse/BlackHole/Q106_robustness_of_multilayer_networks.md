# Q106 · Robustness of multilayer networks

## 0. Header metadata

```txt
ID: Q106
Code: BH_COMPLEX_NETWORK_ROBUST_L3_106
Domain: Complex systems and networks
Family: Network robustness and multilayer structure
Rank: S
Projection_dominance: C
Field_type: socio_technical_field
Tension_type: risk_tail_tension
Status: Reframed_only
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-26
````

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Many real systems are better described as multilayer or interconnected networks than as single graphs. Examples include:

* power grid, communication network, and control systems
* financial institutions and real economy linkages
* transportation networks with multiple modes
* social, organizational, and information layers in one society

The canonical question behind Q106 is:

> Given a multilayer network with specified intra layer connections, inter layer dependencies, and load or flow patterns, how robust is the system to node and edge failures or targeted attacks, and when do naive robustness metrics fail to predict large cascades or systemic collapse?

In more concrete terms:

* Single layer graph theory has many robustness indicators such as degree distribution, k core, percolation thresholds, algebraic connectivity.
* In multilayer settings, a system can look robust by each single layer metric, while still being extremely fragile once interdependencies and cascades are considered.

The canonical problem asks for a principled framework to:

1. define robustness for multilayer networks at an effective theoretical level
2. compare naive or local metrics with true cascade based robustness
3. identify conditions under which multilayer structure amplifies or suppresses tail risk of large cascades

Q106 does not aim to solve all applied cases. It reframes the question as a structured tension problem on multilayer network states.

### 1.2 Status and difficulty

Key partial results in the literature include:

* Demonstrations that interdependent networks can experience abrupt, catastrophic percolation transitions where small additional damage triggers large cascades.
* Formal frameworks for multiplex and multilayer networks, with clear notation and basic robustness metrics.
* Case studies in infrastructure, finance, and other socio technical systems that show real events where hidden dependencies produced unexpected failures.

However:

* There is no universally accepted definition of robustness for multilayer systems that covers both structural properties and cascade behavior.
* Naive extensions of single layer metrics often fail in practice and can underestimate tail risk.
* Systematic tools to compare different definitions of robustness under common experiments are still under development.

From the BlackHole perspective, Q106 is treated as an S rank problem because:

* it sits at a junction of graph theory, statistical physics, and socio technical risk
* wrong models can lead to large real world losses
* a clean, general, falsifiable effective layer encoding is still nontrivial

### 1.3 Role in the BlackHole project

Within the BlackHole S collection, Q106 has three main roles:

1. It is the reference node for risk_tail_tension in multilayer networked systems.
2. It supplies reusable components such as a MultilayerNetworkField and a RobustnessGapFunctional for downstream problems on systemic crashes and collective action.
3. It provides a template for how to encode complex socio technical problems at the effective layer without hiding arbitrary parameter choices or post hoc tuning.

### References

1. S. V. Buldyrev et al., "Catastrophic cascade of failures in interdependent networks", Nature, 2010.
2. S. Boccaletti et al., "The structure and dynamics of multilayer networks", Physics Reports, 2014.
3. M. Kivela et al., "Multilayer networks", Journal of Complex Networks, 2014.
4. A. Haldane and R. May, "Systemic risk in banking ecosystems", Nature, 2011.

---

## 2. Position in the BlackHole graph

This block records how Q106 sits inside the BlackHole graph of Q001 to Q125.

### 2.1 Upstream problems

These nodes provide prerequisites or general tools used by Q106.

* Q068  BH_CHEM_PREBIOTIC_NETWORK_L3_068
  Reason: introduces network based views of reaction systems and basic robustness notions that are generalized here to abstract multilayer networks.

* Q059  BH_CS_INFO_THERMODYN_L3_059
  Reason: provides a framework to relate information processing and thermodynamic constraints that Q106 reuses to discuss cost and feasibility of robust architectures.

### 2.2 Downstream problems

These nodes directly reuse components or depend on the Q106 encoding.

* Q105  BH_COMPLEX_SYSTEMIC_CRASH_PREDICT_L3_105
  Reason: reuses the RobustnessGapFunctional and cascade experiment patterns to structure systemic crash prediction.

* Q107  BH_SOC_COLLECTIVE_ACTION_L3_107
  Reason: uses the MultilayerNetworkField and robustness tension ideas to reason about stability of collective action in coupled social and institutional layers.

* Q123  BH_AI_INTERP_L3_123
  Reason: reuses multilayer robustness as an analogy for robustness of layered AI representations and failure propagation across modules.

### 2.3 Parallel problems

Parallel nodes share similar tension types but do not directly reuse components.

* Q105  BH_COMPLEX_SYSTEMIC_CRASH_PREDICT_L3_105
  Reason: both Q105 and Q106 focus on risk_tail_tension in coupled systems, while Q106 emphasizes structural robustness and Q105 emphasizes prediction of crash events.

* Q068  BH_CHEM_PREBIOTIC_NETWORK_L3_068
  Reason: both involve connectivity, redundancy, and function preservation under perturbations in complex networks.

* Q036  BH_PHYS_HIGH_TC_MECH_L3_036
  Reason: both deal with global behavior that emerges from many local couplings, where small structural changes can radically change macroscopic outcomes.

### 2.4 Cross domain edges

Cross domain edges show where Q106 components can be reused outside the immediate domain.

* Q059  BH_CS_INFO_THERMODYN_L3_059
  Reason: can reuse the CascadeStressExperimentPattern to study how architecture choices impact tail risk under resource constraints.

* Q040  BH_PHYS_QBLACKHOLE_INFO_L3_040
  Reason: can reuse multilayer coupling and robustness ideas to think about layered channels for information retention and escape.

* Q123  BH_AI_INTERP_L3_123
  Reason: can reuse the MultilayerRobustnessHead to reason about robustness of internal AI circuits and feature channels under node or module failures.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. No generative rules from raw data to internal TU fields are specified.

### 3.1 State space

We assume a hybrid semantic state space

```txt
M
```

with elements of the following form at the effective layer:

* A finite node set

  ```txt
  V, with |V| <= N_max
  ```

* A finite layer index set

  ```txt
  L, with |L| <= L_max
  ```

* For each layer index ell in L, a directed or undirected adjacency pattern

  ```txt
  E_ell subset of V x V
  ```

* A set of interlayer dependency relations

  ```txt
  D subset of V x L x V x L
  ```

  that encode which node in which layer depends on which other node and layer.

* Per node and per layer load and capacity summaries

  ```txt
  load(m; v, ell)
  cap(m; v, ell)
  ```

* A damage state map

  ```txt
  damage(m; v, ell) in {intact, failed, disabled}
  ```

for all v in V and ell in L.

We do not specify how any of these objects are constructed from real systems. We only require that for each state m the above quantities are well defined and finite.

### 3.2 Observables and fields

We introduce the following effective observables.

1. Layer structural profile

```txt
StructProfile(m; ell)
```

* Input: state m and layer ell in L.
* Output: a finite dimensional vector of structural features, for example average degree, clustering, and approximate size of the largest connected component within that layer.
* Requirement: there exists a fixed finite feature library, chosen once for all states in a given encoding class.

2. Interdependence profile

```txt
InterdepProfile(m)
```

* Input: state m.
* Output: a finite dimensional vector summarizing the structure of interlayer dependencies D, for example average number of dependencies per node, distribution of dependency chain lengths, and measures of redundancy.
* Requirement: the summary is computed using a fixed finite library of patterns that does not change between states.

3. Cascade response map

```txt
CascadeMap(m; shock_pattern, r)
```

* Input: state m, a shock pattern that selects an initial set of failed nodes, and a resolution parameter r which bounds the cascade depth or time steps.
* Output: a finite dimensional vector of cascade outcome statistics, such as total failed nodes, per layer failure fractions, and whether the system remained connected above a threshold.
* Requirement: for fixed r the cascade map is well defined and terminates in at most r steps.

4. Simple robustness indicator

```txt
R_simple(m)
```

* Input: state m.
* Output: a scalar score between 0 and 1 constructed only from StructProfile and InterdepProfile, using fixed weights and thresholds.
* Interpretation: a naive estimate of robustness based on local and single layer structural information.

5. Cascade based robustness indicator

```txt
R_cascade(m)
```

* Input: state m.
* Output: a scalar score between 0 and 1 derived from CascadeMap over a fixed finite library of shock patterns and resolution levels.
* Interpretation: an estimate of robustness based on observed cascade behavior across layers.

### 3.3 Mismatch observables

We define three nonnegative mismatch observables.

1. Structural mismatch

```txt
DeltaS_struct(m) >= 0
```

This quantity measures mismatch between the actual structural profile (StructProfile and InterdepProfile) and a fixed admissible reference class of structures that are considered balanced for given loads and capacities.

* There exists an admissible class

  ```txt
  E_ref_struct
  ```

  that is specified once and does not depend on any particular state m.
* DeltaS_struct(m) is defined as a distance between the structural summary of m and the nearest member of E_ref_struct, using a fixed distance function.

2. Cascade mismatch

```txt
DeltaS_cascade(m) >= 0
```

This quantity measures mismatch between cascade based robustness R_cascade(m) and the simple indicator R_simple(m).

* If R_simple(m) predicts high robustness but R_cascade(m) shows large failures on the fixed shock library, DeltaS_cascade(m) is large.
* If R_simple(m) and R_cascade(m) agree within fixed tolerances, DeltaS_cascade(m) is small.

3. Multilayer mismatch

```txt
DeltaS_multi(m) >= 0
```

This quantity measures mismatch between robustness measured on each individual layer and robustness measured at the coupled multilayer level.

* For each layer ell we can compute a single layer robustness indicator R_layer(m; ell) using only E_ell and local loads.
* DeltaS_multi(m) is defined as a measure of disagreement between the collection of R_layer(m; ell) and the global R_cascade(m).

### 3.4 Admissible encoding class and fairness constraints

We restrict attention to an admissible encoding class

```txt
E_adm_multi subset of M
```

with the following properties:

1. Bounded size and degree

```txt
|V| <= N_max
|L| <= L_max
max degree per layer <= d_max
```

where N_max, L_max, and d_max are fixed constants.

2. Bounded loads and capacities

```txt
0 <= load(m; v, ell) <= L_bound
0 < cap(m; v, ell) <= C_bound
```

with fixed bounds L_bound and C_bound independent of m.

3. Fixed finite libraries

* A finite library of structural reference patterns for E_ref_struct.
* A finite library of shock patterns used by CascadeMap.
* A finite set of resolution levels

  ```txt
  R_levels = {r_1, r_2, ..., r_K}
  ```

All libraries are chosen once for a given encoding and may not be changed when individual states are evaluated.

4. Fixed weights

Whenever a combined quantity uses weights, these weights are fixed for the entire encoding:

```txt
w_struct > 0
w_cascade > 0
w_multi > 0
w_struct + w_cascade + w_multi = 1
```

These weights do not depend on m and are selected before any experiments or evaluations.

5. Resolution control

Any invariant involving a supremum is taken over the discrete set R_levels rather than over arbitrary resolution choices. This avoids hidden free parameters that could be tuned per state.

### 3.5 Effective tension tensor and singular set

We define an effective tension tensor

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_total(m) * lambda(m) * kappa
```

where:

* S_i(m) are source like factors that encode how strongly the i th semantic component contributes to network stress in state m.
* C_j(m) are receptivity like factors for the j th component that receives or amplifies stress.
* DeltaS_total(m) is a combined mismatch defined below.
* lambda(m) is a convergence state factor restricted to a fixed bounded interval, for example between 0 and 1.
* kappa is a fixed coupling constant for Q106.

We define the combined mismatch as

```txt
DeltaS_total(m) =
    w_struct  * DeltaS_struct(m)  +
    w_cascade * DeltaS_cascade(m) +
    w_multi   * DeltaS_multi(m)
```

All S_i, C_j, lambda, and kappa are effective layer quantities and are not linked to raw data.

Some states may produce undefined or divergent mismatch values. We define the singular set

```txt
S_sing = {
  m in M :
    DeltaS_struct(m) is undefined or not finite, or
    DeltaS_cascade(m) is undefined or not finite, or
    DeltaS_multi(m) is undefined or not finite
}
```

All Q106 analysis is restricted to the regular set

```txt
M_reg = M \ S_sing
```

When a proposed experiment would require evaluating DeltaS_struct, DeltaS_cascade, or DeltaS_multi on a state in S_sing, the result is treated as out of domain rather than as empirical evidence.

---

## 4. Tension principle for this problem

### 4.1 Core tension functional

We define the Q106 tension functional as

```txt
Tension_multi(m) = G(DeltaS_struct(m),
                      DeltaS_cascade(m),
                      DeltaS_multi(m))
```

where G is a fixed nonnegative function chosen for the encoding class, for example

```txt
Tension_multi(m) =
    alpha * DeltaS_struct(m)
  + beta  * DeltaS_cascade(m)
  + gamma * DeltaS_multi(m)
```

with alpha, beta, and gamma positive constants that satisfy

```txt
alpha + beta + gamma = 1
```

G must satisfy:

* Tension_multi(m) >= 0 for all m in M_reg.
* If all three mismatch terms are near 0, then Tension_multi(m) is also near 0.
* If any mismatch grows while others remain bounded, Tension_multi(m) grows at least linearly in that mismatch.

### 4.2 Low tension regime

A multilayer network state m is in the low tension regime if:

1. Structural compatibility

```txt
DeltaS_struct(m) <= epsilon_struct
```

for a small threshold epsilon_struct that depends only on the encoding class, not on m.

2. Cascade agreement

```txt
DeltaS_cascade(m) <= epsilon_cascade
```

so that simple robustness indicators and cascade based indicators agree within fixed tolerances.

3. Multilayer alignment

```txt
DeltaS_multi(m) <= epsilon_multi
```

so that per layer robustness indicators and global robustness indicators are consistent.

In this regime we expect

```txt
Tension_multi(m) <= epsilon_multi_total
```

for a combined threshold epsilon_multi_total that depends only on the encoding and the chosen epsilons.

Low tension means that simple metrics do not systematically underestimate or overestimate robustness and that multilayer coupling does not create hidden fragility inside E_adm_multi.

### 4.3 High tension regime

A state m in M_reg is in the high tension regime if there exists a positive threshold delta_multi such that

```txt
Tension_multi(m) >= delta_multi
```

and delta_multi cannot be reduced to near 0 by small changes that keep the state within the same admissible class and respect the fixed libraries and weights.

Typical high tension patterns include:

* large DeltaS_cascade(m) where R_simple(m) predicts robustness but cascades are severe
* large DeltaS_multi(m) where per layer indicators look safe but coupled behavior is fragile
* structural patterns that are far from E_ref_struct even after allowed adjustments

Q106 focuses on the classification of states into these regimes and on how often real or model systems fall into high tension configurations.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds strictly at the effective layer.

### 5.1 World T: achievable robust multilayer design

World T represents a scenario where multilayer networks can be designed so that low tension is achievable and stable within E_adm_multi.

In World T the following patterns hold:

1. Existence of low tension designs

There exists at least one family of states

```txt
{m_T(k)} subset of M_reg
```

indexed by a resolution or size parameter k such that

```txt
Tension_multi(m_T(k)) <= epsilon_multi_total
```

for all k in a wide range, with epsilon_multi_total independent of k.

2. Stability under refinement

As resolution is refined, for example by increasing R_levels or adding more detailed shock patterns, the family {m_T(k)} can be updated to keep Tension_multi below the same threshold without radical structural changes.

3. Correlation of metrics

In typical states m_T, simple indicators derived from StructProfile and InterdepProfile correlate well with cascade based robustness. For example, if R_simple(m_T) is high then R_cascade(m_T) is also high except for rare anomalies.

4. Constructive layering

Adding new layers or new interlayer links according to fixed design rules allows robustness to increase or at least not decrease. High tension patterns can be avoided within the admissible class.

### 5.2 World F: inherent multilayer fragility

World F represents a scenario where multilayer structure introduces unavoidable fragility inside E_adm_multi.

Patterns in World F include:

1. Positive lower bound on tension

For all states m in M_reg that are realistic under E_adm_multi, there exists a strictly positive delta_multi such that

```txt
Tension_multi(m) >= delta_multi
```

and this bound cannot be significantly reduced without leaving the admissible class.

2. Systematic mismatch between metrics

For many states m_F in M_reg we have:

* R_simple(m_F) predicts high robustness
* R_cascade(m_F) shows large cascades or frequent near collapse

So DeltaS_cascade(m_F) remains large.

3. Multilayer structural trap

Attempts to adjust structure while remaining in E_adm_multi only move tension between DeltaS_struct, DeltaS_cascade, and DeltaS_multi, without lowering DeltaS_total to a safe band.

4. Fragility from coupling

Layer coupling that is required by the domain (for example physical dependencies between infrastructures) cannot be modified enough to remove high tension, so fragility is intrinsic.

### 5.3 Interpretive note

These worlds are described only through patterns of observables and tension values. No mechanism is given for constructing m_T or m_F from empirical data, and no internal TU generative rule is exposed.

---

## 6. Falsifiability and discriminating experiments

This block describes experiments that can falsify particular Q106 encodings of tension, without deciding the canonical problem for all real systems.

### Experiment 1: synthetic multilayer cascade stress test

*Goal:*
Test whether the chosen Tension_multi encoding admits a stable low tension region inside E_adm_multi under refinement of resolution parameters.

*Setup:*

* Choose a finite model class M_syn of synthetic multilayer networks with:

  * fixed N_max, L_max, and d_max
  * specified distributions for loads, capacities, and interlayer dependencies
* Fix all libraries required by E_adm_multi:

  * E_ref_struct
  * shock pattern library
  * R_levels
* Fix weights w_struct, w_cascade, w_multi and the function G before inspecting any outcomes.

*Protocol:*

1. Sample a grid of synthetic states m in M_syn that cover a range of coupling strengths and structural patterns.
2. For each m, compute StructProfile, InterdepProfile, CascadeMap for all r in R_levels, then R_simple, R_cascade, and the three mismatch terms.
3. Compute Tension_multi(m) for each state.
4. Identify candidate low tension region L_low where Tension_multi(m) is below a threshold epsilon_multi_total.
5. Increase the resolution set R_levels by adding finer resolution points and repeat steps 2 to 4.
6. Track how L_low changes as resolution is refined.

*Metrics:*

* Distribution of Tension_multi values over M_syn.
* Size and location of the observed low tension region L_low.
* Stability of L_low under refinement of R_levels.

*Falsification conditions:*

* If for every reasonable choice of epsilon_multi_total there is no nonempty L_low that remains stable under refinement of R_levels, then the current encoding (choice of observables, libraries, weights, and function G) is considered falsified.
* If small changes in libraries or weights within the constraints of E_adm_multi cause arbitrarily large changes in Tension_multi across M_syn without clear structural reason, the encoding is considered unstable and rejected.

*Semantics implementation note:*
The experiment is implemented with hybrid semantics. Graph topology and dependencies are discrete. Loads, capacities, and cascade statistics are treated as real valued quantities.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment only tests whether a particular encoding of multilayer robustness behaves coherently on synthetic models.

---

### Experiment 2: single layer heuristics versus multilayer reality

*Goal:*
Measure how often simple single layer robustness indicators underestimate or overestimate cascade risk when applied to multilayer networks, and test whether DeltaS_cascade and DeltaS_multi detect this systematically.

*Setup:*

* Choose a second synthetic model class M_syn2 where:

  * layer structures are easy to analyze by single layer graph metrics
  * interlayer dependencies introduce couplings that can create cascades
* Choose a library of single layer heuristic scores H_layer such as:

  * average degree
  * algebraic connectivity
  * percolation threshold estimates

*Protocol:*

1. For each m in M_syn2 and each layer ell, compute single layer heuristic scores h(m; ell).
2. Use h(m; ell) to form a single layer based robustness prediction R_pred(m) for the whole system.
3. Independently compute R_cascade(m) using CascadeMap and the fixed shock pattern library.
4. Compute:

   * DeltaS_cascade(m) from disagreement between R_simple(m) and R_cascade(m)
   * DeltaS_multi(m) from disagreement between layer wise scores and global cascade behavior
5. Collect statistics over M_syn2.

*Metrics:*

* Frequency with which R_pred(m) and R_cascade(m) disagree by more than a fixed tolerance.
* Distribution of DeltaS_cascade and DeltaS_multi on these high disagreement cases.
* Correlation between large mismatches and structural features from StructProfile and InterdepProfile.

*Falsification conditions:*

* If there is a large set of states where R_pred(m) and R_cascade(m) disagree strongly but DeltaS_cascade(m) and DeltaS_multi(m) remain small, the encoding fails to capture the robustness gap and is rejected.
* If DeltaS_cascade and DeltaS_multi are large for most states independent of any real structural mismatch, the encoding is considered too blunt and is rejected.

*Semantics implementation note:*
Hybrid semantics are used. Topology is discrete, while robustness scores and mismatch values are treated as real numbers computed from simulation output.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment tests the usefulness of the mismatch observables, not any ultimate theory of real world robustness.

---

## 7. AI and WFGY engineering spec

This block describes how Q106 can be used inside AI systems without exposing any deep TU generative rule.

### 7.1 Training signals

1. signal_multilayer_robustness_gap

   * Definition: a scalar proportional to Tension_multi(m) computed from internal representations of a described networked system.
   * Purpose: encourage the model to maintain internal states where naive and cascade based robustness assessments agree when they should, and to recognize when they diverge.

2. signal_layer_dependency_consistency

   * Definition: a signal derived from InterdepProfile and CascadeMap that penalizes internal representations which ignore strong dependencies that obviously affect cascades.
   * Purpose: push the model to keep track of which layers depend on which others when reasoning about robustness.

3. signal_cascade_tail_awareness

   * Definition: a signal that increases when the model proposes or accepts configurations where small shocks lead to very large cascade outcomes, relative to single layer metrics.
   * Purpose: train the model to recognize potential heavy tail risks in multilayer systems.

4. signal_counterfactual_multi_worlds

   * Definition: a pair of signals that measure how distinctly the model separates World T and World F style scenarios when prompted explicitly.
   * Purpose: make sure the model does not mix statements that assume high robustness with statements that imply unavoidable fragility.

### 7.2 Architectural patterns

1. MultilayerRobustnessHead

   * Role: given an internal embedding that encodes a described multilayer system, this head outputs:

     * estimated R_simple
     * estimated R_cascade
     * estimated Tension_multi
   * Interface: input is a representation of nodes, layers, and dependencies; output is a small set of robustness scores and mismatches.

2. CascadeScenarioFilter

   * Role: evaluates whether a proposed scenario or design change is likely to move the system into high or low tension regimes.
   * Interface: input is a description of structural modifications or policy changes; output is a classification as likely safe, marginal, or fragile based on Tension_multi.

3. TU_MultiLayerField_Observer

   * Role: generic observer that extracts simplified versions of StructProfile, InterdepProfile, and CascadeMap summaries from large language model internal states.
   * Interface: acts as a probe that maps intermediate embeddings to the summary space used by Q106.

### 7.3 Evaluation harness

We outline an evaluation harness for AI systems augmented with Q106 components.

1. Task design

   * Construct a benchmark of scenarios that describe multilayer infrastructures, financial systems, or social structures.
   * For each scenario, construct reference labels:

     * qualitatively robust
     * borderline
     * fragile
       based on separate domain models or expert assessments.

2. Conditions

   * Baseline condition: the AI model answers questions about robustness without Q106 modules or signals.
   * TU condition: the AI model uses Q106 modules and training signals as auxiliary guidance.

3. Metrics

   * Accuracy: agreement of robustness classifications with reference labels.
   * Consistency: frequency of contradictions across multiple related questions about the same scenario.
   * Sensitivity: ability to detect changes in robustness when small structural modifications are made in the prompt.

### 7.4 60 second reproduction protocol

A simple protocol for external observers.

* Baseline setup

  * Prompt: present a short description of a multilayer infrastructure system and ask the AI to discuss its robustness under attacks and failures.
  * Observation: check whether the answer mentions interlayer dependencies, cascade risk, and the possibility that simple metrics can fail.

* TU encoded setup

  * Prompt: present the same description but ask the AI to reason explicitly in terms of:

    * multilayer structure
    * difference between naive metrics and cascade behavior
    * a conceptual Tension_multi score
  * Observation: check whether the answer is more explicit about where robustness claims might fail and how cross layer couplings change risk.

* Comparison metric

  * Rate answers for:

    * structural clarity
    * explicit mention of tail risk
    * recognition of hidden dependencies

* What to log

  * Prompts and responses in both setups.
  * Any auxiliary Tension_multi estimates output by the MultilayerRobustnessHead.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: MultilayerNetworkField

   * Type: field
   * Minimal interface:

     * Inputs: abstract description of nodes, layers, intra layer edges, interlayer dependencies, loads, and capacities
     * Output: normalized representation of a multilayer network state m in M_reg
   * Preconditions:

     * Node and layer counts are finite and within fixed bounds.
     * Loads and capacities lie in bounded intervals.
     * Dependency structure is well defined.

2. ComponentName: RobustnessGapFunctional

   * Type: functional
   * Minimal interface:

     * Inputs: structural summaries, interdependence summaries, cascade outcome summaries
     * Output: scalar Tension_multi(m) in a fixed range, for example between 0 and 1
   * Preconditions:

     * All summaries come from a state in E_adm_multi.
     * Structural and cascade summaries are computed using the fixed libraries for that encoding.

3. ComponentName: CascadeStressExperimentPattern

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: a model class of multilayer networks and a library of shock patterns
     * Output: a standard experimental protocol and a rule for computing Tension_multi distributions
   * Preconditions:

     * The model class admits simulation of cascade dynamics up to resolution levels in R_levels.

### 8.2 Direct reuse targets

1. Q105  BH_COMPLEX_SYSTEMIC_CRASH_PREDICT_L3_105

   * Which component is reused:

     * MultilayerNetworkField
     * RobustnessGapFunctional
     * CascadeStressExperimentPattern
   * Why it transfers:

     * Q105 needs a structured way to test crash risk in systems that are naturally multilayer and interdependent.
   * What changes:

     * Q105 specializes the model class to financial and infrastructure systems and calibrates shock patterns to realistic stress scenarios.

2. Q107  BH_SOC_COLLECTIVE_ACTION_L3_107

   * Which component is reused:

     * MultilayerNetworkField
     * RobustnessGapFunctional
   * Why it transfers:

     * Collective action depends on the robustness of coupled social, organizational, and informational layers that can be represented in the same field.
   * What changes:

     * States emphasize influence links, trust relations, and institutional constraints rather than physical flows or loads.

3. Q068  BH_CHEM_PREBIOTIC_NETWORK_L3_068

   * Which component is reused:

     * MultilayerNetworkField
   * Why it transfers:

     * Prebiotic reaction networks can be represented with chemical and spatial layers, where robustness of function under perturbations is also important.
   * What changes:

     * Loads and capacities are replaced by reaction rates and environmental constraints.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * The effective layer encoding for Q106 has well defined:

    * state space structure
    * observables
    * mismatch quantities
    * tension functional
    * singular set and domain restriction
  * Experiments have been specified conceptually but not yet implemented and published as reproducible artefacts.

* N_level: N2

  * The narrative that links multilayer topology, cascade behavior, and robustness tension is explicit and coherent.
  * Counterfactual worlds and reuse relationships are laid out.

### 9.2 Next measurable step toward E2

To reach E2, the following measurable step is proposed:

1. Implement at least one synthetic experiment from Block 6 in a concrete model class.
2. Publish:

   * the synthetic model class specification
   * the code or pseudocode for CascadeMap, R_simple, R_cascade, and the mismatch observables
   * tension distributions for a documented set of synthetic networks
3. Demonstrate at least one downstream reuse, for example by integrating RobustnessGapFunctional into a Q105 crash prediction experiment.

All of these steps operate at the effective layer and do not require any deep TU generative rule.

### 9.3 Long term role in the TU program

In the long term, Q106 is expected to serve as:

* the anchor for risk_tail_tension in complex networked systems
* a common language for talking about robustness gaps across domains such as infrastructure, finance, and social systems
* a template for encoding other complex socio technical problems where naive metrics and real failure modes diverge

---

## 10. Elementary but precise explanation

This block explains Q106 in simple language while keeping the effective layer view.

Many systems today are not just single networks. A city, for example, has:

* a power grid
* communication networks
* transportation networks
* organizations and rules

These layers depend on each other. If power fails, communication may fail. If communication fails, repair teams may not move. If rules fail, nobody knows who should act.

People often ask: how robust is such a system. A common habit is to look at simple statistics, like how many connections each node has or how big the largest cluster is. That can work in single layer networks. In multilayer systems this habit can be misleading.

In the Tension Universe view, Q106 asks a focused question:

* When do simple metrics say "the system is safe" while the true behavior under shocks is fragile.
* Can we define a number Tension_multi that is small when simple metrics are trustworthy and large when they are not.

To do this we:

1. Imagine a space of states. Each state describes:

   * layers and connections in each layer
   * how layers depend on each other
   * how much load and capacity each part has
2. For each state we compute:

   * simple robustness from local structure and per layer views
   * robustness from simulated cascades in which we remove some nodes and see how failures spread
3. We measure three mismatches:

   * how far the structure is from a reference pattern
   * how much simple robustness and cascade robustness disagree
   * how much per layer robustness and global robustness disagree
4. We combine these into one tension number Tension_multi.

If Tension_multi is small, simple metrics are telling a mostly true story. If Tension_multi is large, there is a robustness gap. The system may be much more fragile than it looks.

We then consider two worlds:

* In World T, engineers can design multilayer systems that keep Tension_multi low across many scenarios. Simple metrics and cascades agree.
* In World F, no matter how people adjust structure inside realistic limits, there is always a high tension gap. Coupling between layers makes fragility hard to avoid.

Q106 does not claim which world we live in. It does something more basic. It gives:

* a clear way to talk about robustness gaps
* observable quantities that encode those gaps
* experiments and AI modules that use these quantities in a controlled way

This is enough for Q106 to be a central node for multilayer robustness in the Tension Universe framework, and a starting point for many more detailed models and tests.
