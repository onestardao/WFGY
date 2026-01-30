<!-- QUESTION_ID: TU-Q107 -->
# Q107 · Large-scale collective action mechanisms

## 0. Header metadata

```txt
ID: Q107
Code: BH_SOC_COLLECTIVE_ACTION_L3_107
Domain: Economics / Social and complex systems
Family: Collective action and public goods
Rank: S
Projection_dominance: C
Field_type: socio_technical_field
Tension_type: incentive_tension
Status: Open (effective-layer reframing only)
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-30
````

---

## 0. Effective layer disclaimer

This entry works strictly at the effective layer of the Tension Universe (TU) framework.

1. **Scope of claims**

   * The goal is to specify an effective-layer encoding for a family of collective action problems.
   * It does not claim to solve the canonical collective action problem from economics, game theory, or political science.
   * It does not claim that any particular real world movement, treaty, or institution will succeed or fail.

2. **No new base axioms or theorems**

   * This document does not introduce any new formal axiom system beyond what is already assumed in the TU charters.
   * It does not state or prove any new mathematical theorem about equilibria, games, or social choice.
   * It should not be cited as evidence that the underlying canonical problem has been resolved.

3. **No explicit generative mapping**

   * Objects such as `M_CA`, `Par_CA`, `Incentive_CA`, `Belief_CA`, and `Tension_CA` are defined only as effective-layer fields and observables.
   * No rule is given for how to map raw empirical data, survey responses, or micro level events into these internal TU objects.
   * Any such mapping, if used in applications, must be documented separately and is outside the scope of this page.

4. **Encoding class and finite design choices**

   * All encodings described here are drawn from an admissible encoding class with:

     * finite libraries of reference functions
     * finite sets of allowed weights and tension thresholds
     * fixed semantics compatible with the TU charters
   * Once a particular encoding is chosen for an experiment or application, its components are held fixed and are not tuned post hoc.

5. **Counterfactual worlds as patterns, not physics**

   * World T and World F are defined as patterns of observables and tension values over families of effective states.
   * They are not claims about the unique true nature of our universe, but diagnostic lenses for reasoning about robustness and fragility of collective action.

The formal constraints on effective-layer work, encoding fairness, and tension scales are governed by:

* TU Effective Layer Charter
* TU Encoding and Fairness Charter
* TU Tension Scale Charter

which are referenced explicitly in the footer of this page.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q107 is:

How can large populations of agents sustain costly collective action at scale, in settings where individual level incentives favor free riding or passive behavior, and where the benefits of success are diffuse and non excludable.

Concrete instances include:

* provision of public goods at national or global scale
* participation in social movements and protests
* climate mitigation efforts that require widespread costly behavior change
* maintenance of shared resources such as fisheries or forests

The tension arises because:

* each individual often faces a net cost of participation relative to free riding
* collective success requires a critical mass of contributors
* coordination, trust, and institutions can change the effective incentives, but not without further cost

Q107 treats this as a structured open problem about the mechanisms and conditions that allow large scale collective action to emerge and persist in spite of the free rider problem.

### 1.2 Status and difficulty

The basic free rider problem is well formalized in game theory and economics. However, there is no single unified theory that:

* predicts when large scale collective action should succeed or fail across domains
* quantitatively accounts for the observed variety of successful mechanisms in the field
* explains why some institutions or network structures support cooperation while seemingly similar ones do not

Partial progress includes:

* formal models of public goods games and repeated games that show conditions for cooperation
* empirical and field work on commons governance that identifies patterns of successful institutions
* experimental evidence on how communication, monitoring, and sanctioning change behavior
* network models of diffusion and coordination

Despite this, several aspects remain open:

* a general mechanism level classification that works across environmental, political, and economic cases
* predictive criteria for robustness under shocks, scale up, and technological change
* a common language that connects formal models, experiments, and field institutional analysis

From the TU perspective, this entry should be read as an effective-layer reframing only. It does not close the canonical collective action problem, and it does not compete with or override existing theories. Instead, it provides an encoding that is designed to be testable, falsifiable, and reusable across domains.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q107 plays three roles:

1. It is the flagship example of an `incentive_tension` problem in socio technical systems, where individual and group incentives interact across large networks.
2. It anchors the cluster of problems about inequality, institutional stability, polarization, and multi agent AI coordination that all rely on coordinated costly actions.
3. It provides a test bed for Tension Universe encodings of:

   * incentive fields
   * belief and expectation fields
   * network coupled participation states
   * tension functionals that measure the gap between predicted and observed participation at scale

### References

1. Mancur Olson, “The Logic of Collective Action: Public Goods and the Theory of Groups”, Harvard University Press, 1965.
2. Elinor Ostrom, “Governing the Commons: The Evolution of Institutions for Collective Action”, Cambridge University Press, 1990.
3. Russell Hardin, “Collective Action”, Johns Hopkins University Press, 1982.
4. Standard encyclopedia level entry on “Collective action problem” or “Free rider problem” summarizing formal models and empirical findings.

---

## 2. Position in the BlackHole graph

This block records how Q107 is located within the BlackHole graph over Q001 to Q125. Each edge is given with a one line reason that references a specific component type or tension type.

### 2.1 Upstream problems

Problems that provide prerequisites, tools, or structural framing for Q107.

* Q101 · `BH_ECON_EQUITY_PREM_L3_101`
  Reason: Provides baseline models of individual risk and return preferences that feed into net incentives for participation in collective action.

* Q104 · `BH_ECON_INEQUALITY_DYN_L3_104`
  Reason: Long run inequality dynamics shape who can afford to participate and how costs and benefits are distributed.

* Q106 · `BH_COMPLEX_NETWORK_ROBUST_L3_106`
  Reason: Supplies multilayer network robustness tools that Q107 reuses to model how participation and norms propagate.

### 2.2 Downstream problems

Problems that directly reuse Q107 components or depend on its incentive tension structure.

* Q108 · `BH_SOC_POLARIZATION_L3_108`
  Reason: Uses the Q107 collective action tension functional to model how coordinated political mobilization contributes to polarization.

* Q109 · `BH_SOC_MIGRATION_L3_109`
  Reason: Treats large migration waves as large scale collective decisions that reuse Q107 incentive and coordination fields.

* Q110 · `BH_SOC_INSTITUTION_EVOL_L3_110`
  Reason: Depends on Q107 structures to explain how repeated collective action feeds back into institutional evolution.

* Q125 · `BH_AI_MULTIAGENT_L3_125`
  Reason: Uses Q107 components as templates for multi agent AI coordination and conflict in socio technical environments.

### 2.3 Parallel problems

Problems with similar tension type but without direct component reuse.

* Q105 · `BH_COMPLEX_SYSTEMIC_CRASH_PREDICT_L3_105`
  Reason: Both Q105 and Q107 study sharp macro transitions triggered by many local decisions under tension in networks.

* Q098 · `BH_EARTH_ANTHROPOCENE_L3_098`
  Reason: Both involve many agents whose actions must align or fail to align with environmental constraints, under incentive_tension.

### 2.4 Cross domain edges

Edges that connect Q107 to other domains through reusable patterns.

* Q121 · `BH_AI_ALIGNMENT_L3_121`
  Reason: Frames alignment as collective action between human and AI agents with conflicting or partially aligned incentives.

* Q122 · `BH_AI_CONTROL_L3_122`
  Reason: Uses collective action templates to model how distributed human actors must coordinate control interventions on AI systems.

* Q059 · `BH_CS_INFO_THERMODYN_L3_059`
  Reason: Reuses ideas about the information and energetic cost of coordination in large systems.

All edges are intended to be assembled into an adjacency list when the full BlackHole graph is built.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is strictly at the effective layer. We only specify:

* state space structure
* observables and fields
* invariants and tension functionals
* singular sets and domain restrictions
* admissible encoding classes and fairness constraints

We do not describe how internal TU fields are generated from raw data. We only assume that suitable effective states and observables exist.

### 3.1 State space

We assume a parameter space:

```txt
Par_CA subset-of R^k
```

for some finite integer `k`, which holds all continuous valued parameters such as payoffs, beliefs, and network weights. For the purposes of this problem:

* all effective scalar quantities drawn from `Par_CA` are assumed finite
* whenever we need explicit bounds, values will be restricted to fixed intervals such as `[0, C_max]` or `[0, 1]` specified by the encoding

We define the effective state space:

```txt
M_CA
```

as a set of socio technical configurations. Each state:

```txt
m in M_CA
```

encodes, at the effective layer:

* a finite set of agents with types and roles
* a finite interaction network over these agents, possibly with multiple layers
* a vector of payoff and cost parameters drawn from `Par_CA`
* a vector of belief and expectation parameters drawn from `Par_CA`
* a participation configuration that records which agents are contributing
* an outcome configuration that records public good provision or collective outcome level
* an institutional configuration that records rules, norms, and mechanisms at a coarse level

We treat `M_CA` as a set with enough structure for the observables below to be well defined as maps from `M_CA` to `Par_CA` or to finite discrete sets. We do not specify any deeper topology or sigma algebra, because we do not need suprema over free continuous families in this problem.

### 3.2 Incentive and participation observables

We define the following observables on `M_CA`.

1. Population size observable

```txt
N_agents(m) in {1, 2, 3, ...}
```

Number of agents in the configuration represented by `m`.

2. Participation fraction observable

```txt
p_part(m) = N_participating(m) / N_agents(m)
```

where `N_participating(m)` is the number of agents marked as participating in the collective action in `m`. This is a rational number in `(0, 1]` when participation is non empty.

3. Individual cost observable

```txt
C_indiv(m) in Par_CA
```

An effective scalar that encodes the average individual net cost of participation relative to a neutral baseline in the configuration `m`. We assume:

```txt
C_indiv(m) >= 0
C_indiv(m) <= C_max
```

for some fixed bound `C_max` selected with the encoding.

4. Public benefit observable

```txt
B_public(m) in Par_CA
```

An effective scalar for the level of public benefit or collective outcome achieved in configuration `m`. We assume:

```txt
B_public(m) >= 0
B_public(m) <= B_max
```

for some fixed bound `B_max` selected with the encoding.

5. Local incentive field observable

We define a field:

```txt
Incentive_CA(m; i)
```

where `i` indexes agent types or groups. For each `i`:

* `Incentive_CA(m; i)` is a scalar in `Par_CA` that encodes the net incentive for agents of type `i` to participate, given the current configuration of costs, benefits, and institutions.
* For each encoding, there is a fixed bounded interval `[I_min, I_max]` such that `Incentive_CA(m; i)` lies inside that interval for all regular states.

6. Belief and expectation field observable

We define:

```txt
Belief_CA(m; i)
```

as the expected participation fraction among neighbors of type `i` as encoded in `m`. This is a rational number in `[0, 1]`.

7. Network coupling descriptor

We define a coarse observable:

```txt
Network_CA(m)
```

which is a finite tuple describing:

* degree distribution summary
* clustering summary
* presence or absence of key structural motifs relevant for coordination

This descriptor lives in a finite product of `Par_CA` and discrete sets.

All these observables are defined directly on `M_CA` at the effective layer. We do not specify how they are computed from raw social or experimental data.

### 3.3 Mismatch observables

We now define mismatches between observed quantities and reference values.

To avoid free tuning, we first fix an admissible class of reference incentive models:

```txt
E_CA_ref
```

An element of `E_CA_ref` is a mapping:

```txt
RefIncentive_CA: M_CA -> Par_CA
```

with the following constraints:

1. Symmetry: agents of the same type under the same payoff parameters and network neighborhood are assigned the same incentive value.
2. Locality: `RefIncentive_CA(m)` depends only on payoff parameters, network descriptors, and institutional configuration in `m`, not on the realized participation configuration itself.
3. Boundedness: for all `m` in `M_CA`, `RefIncentive_CA(m)` is finite and lies in a fixed interval `[0, C_max]` that does not depend on `m`.

We also consider a class of reference expectation models:

```txt
E_CA_belief
```

An element of `E_CA_belief` is a mapping:

```txt
RefBelief_CA: M_CA -> [0, 1]
```

that encodes, for each configuration, the participation fraction that a benchmark rational expectations model would predict, given a reference incentive model and `Network_CA(m)`. We only use the following properties:

* `RefBelief_CA(m)` lies in `[0, 1]` for all `m`.
* It depends on incentives, networks, and institutions, but not on the realized participation in `m`.

For a given encoding (defined in 3.4), we choose and fix one `RefIncentive_CA` in `E_CA_ref` and one `RefBelief_CA` in `E_CA_belief`.

Using this, we define:

1. Incentive mismatch

```txt
EffectiveIncentive_CA(m) = average over i of Incentive_CA(m; i),
                           weighted by population share
DeltaS_incentive(m) = abs(EffectiveIncentive_CA(m) - RefIncentive_CA(m))
DeltaS_incentive(m) >= 0
```

2. Expectation mismatch

```txt
ExpectedParticipation_CA(m) = RefBelief_CA(m)
ActualParticipation_CA(m)   = p_part(m)
DeltaS_expectation(m)       = abs(ActualParticipation_CA(m) - ExpectedParticipation_CA(m))
DeltaS_expectation(m) >= 0
```

3. Combined collective action mismatch

We will use global weights:

```txt
w_incentive   in [0.3, 0.7]
w_expectation in [0.3, 0.7]
w_incentive + w_expectation = 1
```

The pair `(w_incentive, w_expectation)` is chosen once for each encoding from a finite set of allowed pairs specified by the TU Tension Scale Charter. For a fixed encoding, they remain constant across all states and experiments.

We define:

```txt
DeltaS_CA(m) = w_incentive   * DeltaS_incentive(m)
             + w_expectation * DeltaS_expectation(m)
```

By construction:

```txt
DeltaS_CA(m) >= 0
DeltaS_CA(m) = 0
```

only when both incentive and expectation mismatches vanish.

### 3.4 Encoding class and fairness constraints

To make the encoding choices explicit and finite, we introduce an admissible encoding class:

```txt
E_CA_enc
```

Each element:

```txt
e_CA in E_CA_enc
```

is a finite tuple:

```txt
e_CA = (
  RefIncentive_CA,
  RefBelief_CA,
  w_incentive, w_expectation,
  G_CA, a_CA, b_CA,
  epsilon_CA, delta_CA,
  C_min, p_thresh
)
```

subject to the following constraints:

1. **Reference functions**

   * `RefIncentive_CA` is selected from a finite library inside `E_CA_ref`.
   * `RefBelief_CA` is selected from a finite library inside `E_CA_belief`.

2. **Weights and tension functional**

   * `(w_incentive, w_expectation)` is selected from a finite set of rational pairs in `[0, 1]^2` that satisfy the constraints in 3.3.
   * `G_CA` is selected from a finite library of nonnegative functions of two arguments that are linear or piecewise linear in each argument.
   * `a_CA` and `b_CA` are nonnegative rational constants with `a_CA > 0`, `b_CA > 0`, and `a_CA + b_CA` lying in a fixed bounded interval, chosen from a finite set.

3. **Thresholds and scales**

   * `epsilon_CA` (low tension threshold) is chosen from a finite tension scale grid specified by the TU Tension Scale Charter.
   * `delta_CA` (high tension threshold) is chosen from the same or another finite grid, with `delta_CA > epsilon_CA`.
   * `C_min` (non trivial cost threshold) and `p_thresh` (minimum participation fraction for success) are chosen from finite sets of economically and behaviorally meaningful values.

4. **Admissible state subset**

   For each encoding `e_CA`, we may define an admissible subset:

   ```txt
   M_CA_adm(e_CA) subset-of M_CA
   ```

   given by bounds on agent counts, payoffs, and network descriptors. All experiments and evaluations with this encoding are restricted to:

   ```txt
   M_CA_reg(e_CA) = M_CA_adm(e_CA) \ S_sing_CA
   ```

   where `S_sing_CA` is defined in 3.6.

Once an encoding `e_CA` is fixed for an experiment, all of its components are held fixed. Any change to reference functions, weights, thresholds, or the functional form of `G_CA` is treated as selecting a new encoding `e_CA'` and requires a separate experiment.

### 3.5 Effective tension tensor and invariants

For a fixed encoding `e_CA`, we adopt an effective tension tensor:

```txt
T_ij_CA(m; e_CA) = S_i_CA(m) * C_j_CA(m) * DeltaS_CA(m) * lambda_CA(m) * kappa_CA
```

where:

* `S_i_CA(m)` is a source like factor for the ith semantic or social source component in configuration `m` (for example, strength of institutional rules).
* `C_j_CA(m)` is a receptivity factor for the jth downstream component (for example, sensitivity of political outcomes to participation).
* `DeltaS_CA(m)` is the combined mismatch defined in 3.3 for the chosen encoding.
* `lambda_CA(m)` is a convergence state factor in a fixed interval, indicating whether local reasoning about incentives is convergent, recursive, divergent, or chaotic.
* `kappa_CA` is a fixed coupling constant setting the scale for incentive_tension in Q107 and is treated as part of the encoding.

We do not need the full tensor in this problem. We mainly use scalar invariants:

1. Participation adequacy invariant

```txt
I_part_CA(m) = DeltaS_expectation(m)
```

Interpreted as a measure of how surprising the observed participation is, relative to the reference expectation model.

2. Incentive adequacy invariant

```txt
I_incent_CA(m) = DeltaS_incentive(m)
```

Interpreted as a measure of how far the effective incentives are from the level that would rationally support observed participation.

Both invariants are nonnegative scalars that can be compared across configurations inside the same encoding.

### 3.6 Singular set and domain restrictions

Some configurations may make the observables undefined or ill posed, for example:

* `N_agents(m) = 0`
* costs or benefits not finite
* missing or inconsistent network descriptors
* no well defined participation state

We define the singular set:

```txt
S_sing_CA = {
  m in M_CA :
  N_agents(m) = 0
  or C_indiv(m) not in Par_CA
  or B_public(m) not in Par_CA
  or any required observable is undefined
}
```

For each encoding `e_CA`, we restrict all Q107 analysis to the regular subset:

```txt
M_CA_reg(e_CA) = M_CA_adm(e_CA) \ S_sing_CA
```

Any attempt to evaluate `DeltaS_CA(m)` or derived tension quantities for `m` in `S_sing_CA` is treated as out of domain, not as evidence about collective action mechanisms.

---

## 4. Tension principle for this problem

This block states how Q107 is characterized as an incentive_tension problem at the effective layer, relative to a fixed encoding `e_CA in E_CA_enc`.

### 4.1 Core tension functional

For a fixed encoding `e_CA`, we define the collective action tension functional:

```txt
Tension_CA(m; e_CA) = G_CA(DeltaS_incentive(m), DeltaS_expectation(m))
```

where `G_CA` and coefficients `a_CA`, `b_CA` are taken from the encoding. A simple example in the encoding library is:

```txt
Tension_CA(m; e_CA) = a_CA * DeltaS_incentive(m)
                    + b_CA * DeltaS_expectation(m)
```

with constants:

```txt
a_CA > 0
b_CA > 0
```

These constants are chosen once with the encoding and remain fixed. We require:

* `Tension_CA(m; e_CA) >= 0` for every `m` in `M_CA_reg(e_CA)`
* `Tension_CA(m; e_CA)` is small when both mismatches are small
* `Tension_CA(m; e_CA)` grows when either mismatch grows while the other is held fixed

We do not allow `G_CA` to depend on outcome labels such as success or failure. It only depends on the two mismatch quantities.

### 4.2 Large scale collective action as low tension principle

At the effective layer, Q107 can be framed, for a fixed encoding `e_CA`, as the following principle:

There exist configurations:

```txt
m_good in M_CA_reg(e_CA)
```

with:

* large population size `N_agents(m_good)` above a domain specific threshold
* participation fraction `p_part(m_good)` above a threshold `p_thresh(e_CA)` for successful collective action
* non trivial participation costs `C_indiv(m_good)` above a minimal cost level `C_min(e_CA)`

such that:

```txt
Tension_CA(m_good; e_CA) <= epsilon_CA(e_CA)
```

for a small threshold `epsilon_CA(e_CA)` that is chosen from a finite tension scale grid and does not grow without bound when we refine our description of incentives, beliefs, and networks within the same encoding class.

Informally, world class collective action corresponds to states where many agents participate despite real costs, and where the effective tension between incentives, beliefs, and observed participation can be made consistently small under a fixed encoding.

### 4.3 Fragile collective action as persistent high tension

Failure to sustain large scale collective action corresponds, at the effective layer, to the following pattern in a fixed encoding `e_CA`:

For configurations:

```txt
m_fragile in M_CA_reg(e_CA)
```

that are otherwise similar in scale and cost to `m_good`, but with:

* observed participation fraction high only briefly or not at all
* no robust mechanisms stabilizing beliefs and incentives

the tension functional satisfies:

```txt
Tension_CA(m_fragile; e_CA) >= delta_CA(e_CA)
```

for some strictly positive `delta_CA(e_CA)` that is chosen from a finite tension scale grid and remains bounded away from zero when we refine the encoding inside the same admissible class. Both:

* `DeltaS_incentive(m_fragile)`
* `DeltaS_expectation(m_fragile)`

stay large on average.

In these states, the system appears to require levels of trust, norm strength, or payoff alignment that are not actually present, so the mismatch and therefore tension remain high.

Q107 then studies which mechanisms and institutional patterns correspond to low tension high participation states, and which ones trap systems in high tension low participation regimes.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer. They are not generative models. They are patterns of observables and tension values across configurations, evaluated under a fixed encoding `e_CA`.

* World T: robust large scale collective action
* World F: fragile or absent large scale collective action

### 5.1 World T (robust collective action)

In World T, we consider a family of regular states:

```txt
m_T in M_CA_reg(e_CA)
```

with the following patterns.

1. High participation under non trivial cost

For many `m_T`:

```txt
N_agents(m_T) is large
C_indiv(m_T) >= C_min(e_CA) > 0
p_part(m_T) >= p_thresh(e_CA)
```

for thresholds `C_min(e_CA)` and `p_thresh(e_CA)` that represent meaningful cost and participation and are part of the encoding.

2. Low and stable tension

For these states:

```txt
Tension_CA(m_T; e_CA) <= epsilon_CA(e_CA)
```

for some small `epsilon_CA(e_CA)` in the low tension band specified by the tension scale. When we refine the representation of incentives and beliefs within the same encoding class, `Tension_CA(m_T; e_CA)` remains within a narrow band rather than drifting upward.

3. Shock resilience

When exogenous shocks change payoff parameters or network structure moderately, there exist sequences of states `m_T_prime` in `M_CA_reg(e_CA)` where:

* participation fraction remains above `p_thresh(e_CA)` after adaptation
* tension `Tension_CA(m_T_prime; e_CA)` remains in the low band after a transient adjustment period

4. Institutional patterns

In World T, there are many configurations `m_T` with institutional configurations that consistently compress:

* `DeltaS_incentive(m_T)`
* `DeltaS_expectation(m_T)`

by aligning incentives, improving information, and providing credible monitoring and sanctioning.

### 5.2 World F (fragile collective action)

In World F, we consider a family of regular states:

```txt
m_F in M_CA_reg(e_CA)
```

with the following patterns.

1. Low participation or rapid collapse

Even when `N_agents(m_F)` and payoff parameters are similar to those in World T, we often observe:

```txt
p_part(m_F) < p_thresh(e_CA)
```

or brief early participation followed by rapid decline to low levels.

2. Persistent high tension

For these states:

```txt
Tension_CA(m_F; e_CA) >= delta_CA(e_CA)
```

for some positive `delta_CA(e_CA)` that remains bounded away from zero when we refine the encoding within the fixed class. Both:

* `DeltaS_incentive(m_F)`
* `DeltaS_expectation(m_F)`

stay large on average.

3. Shock sensitivity

Small shocks in costs or network structure generate large changes in participation, often amplifying high tension states and leading to long periods with low collective action.

4. Weak or misaligned institutions

Institutional configurations in `m_F` often fail to reduce mismatch. For example:

* norms are not internalized
* sanctions are too weak or misdirected
* information about others participation is noisy or delayed

so mechanisms that could lower tension do not activate effectively.

### 5.3 Interpretive note

The World T and World F descriptions do not specify how states in `M_CA` are generated from micro level data. They only assert that if we can construct effective descriptions of worlds with robust or fragile collective action, then the pattern of observables and `Tension_CA` values will differ as above for a fixed encoding `e_CA`.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can test and falsify specific Q107 encodings at the effective layer. They do not solve the canonical problem. They only test whether a given encoding of incentives, beliefs, and tension is coherent and useful.

In every experiment below, we first fix a single encoding:

```txt
e_CA in E_CA_enc
```

including its reference functions, weights, thresholds, and tension functional, before inspecting any outcomes. All quantities in the experiment are then computed with this fixed `e_CA`. Any change to these choices defines a new encoding and requires a new experiment.

### Experiment 1: Laboratory network public goods games

*Goal:*
Evaluate whether the proposed `Tension_CA` encoding correctly labels laboratory regimes known to support or fail large scale cooperation as low or high tension.

*Setup:*

* Fix an encoding `e_CA in E_CA_enc` as described above.

* Use repeated public goods or threshold contribution games in controlled laboratory settings.

* Construct multiple treatments that vary:

  * network topology (for example, lattice, random graph, highly clustered network)
  * information about others contributions
  * availability of costly punishment or reward mechanisms

* From the published or measured data, define for each treatment an effective state:

  ```txt
  m_lab in M_CA_reg(e_CA)
  ```

  that encodes average participation, payoff parameters, network summaries, and institutional rules.

*Protocol:*

1. For each treatment, identify the corresponding `m_lab`.

2. Using the fixed `RefIncentive_CA`, `RefBelief_CA`, weights, and `G_CA` in `e_CA`, compute:

   ```txt
   DeltaS_incentive(m_lab)
   DeltaS_expectation(m_lab)
   Tension_CA(m_lab; e_CA)
   ```

3. Classify each treatment as:

   * empirically high cooperation (observed `p_part(m_lab)` above a threshold chosen from the finite set associated with `p_thresh(e_CA)`)
   * empirically low cooperation (observed `p_part(m_lab)` below that threshold)

4. Compare `Tension_CA(m_lab; e_CA)` distributions between these two empirical groups.

*Metrics:*

* Mean and median `Tension_CA(m_lab; e_CA)` for high cooperation versus low cooperation treatments.
* Fraction of high cooperation treatments with `Tension_CA(m_lab; e_CA)` below a pre declared low tension band associated with `epsilon_CA(e_CA)` and the tension scale.
* Fraction of low cooperation treatments with `Tension_CA(m_lab; e_CA)` above a pre declared high tension band associated with `delta_CA(e_CA)`.
* Stability of these patterns when the encoding is applied to new datasets or additional treatments.

*Falsification conditions:*

* If a large majority of high cooperation treatments are assigned `Tension_CA(m_lab; e_CA)` in the high tension band while many low cooperation treatments fall in the low tension band, the current encoding of `DeltaS_incentive`, `DeltaS_expectation`, or `Tension_CA` is considered falsified at the effective layer.
* If moderate changes in experimental details that should not alter the logic of cooperation lead to extreme and inconsistent changes in `Tension_CA(m_lab; e_CA)` without clear theoretical reason, the encoding is considered unstable and rejected.

*Semantics implementation note:*
Quantities are represented using hybrid semantics as declared in the metadata, with continuous fields for payoffs and beliefs and discrete labels for participation and institutions. No alternative semantics is introduced in this experiment.

*Boundary note:*
Falsifying a TU encoding for collective action does not solve the canonical problem. This experiment can reject specific Q107 encodings but cannot by itself provide a general theory of large scale collective action.

---

### Experiment 2: Field data from commons governance

*Goal:*
Test whether the Q107 encoding can distinguish long lived successful commons governance regimes from failed or collapsed cases, using field data.

*Setup:*

* Fix an encoding `e_CA in E_CA_enc` (which may or may not be the same as in Experiment 1).

* Use datasets inspired by classic commons case studies, such as irrigation systems, fisheries, or forest user groups.

* For each case, identify:

  * approximate number of participants
  * typical contribution costs relative to income or alternatives
  * observed participation rates over time
  * institutional features such as monitoring, local rule making, and sanctioning

* For each case, define an effective state:

  ```txt
  m_field in M_CA_reg(e_CA)
  ```

  encoding these summaries.

*Protocol:*

1. For each case, assign `m_field` and compute:

   ```txt
   DeltaS_incentive(m_field)
   DeltaS_expectation(m_field)
   Tension_CA(m_field; e_CA)
   ```

   using the same fixed reference maps, weights, and `G_CA` as in the chosen encoding.

2. Label each case as:

   * successful long lived governance (sustained collective action and resource health)
   * failed or collapsed governance (repeated breakdowns or resource depletion)

3. Compare tension patterns between the two groups.

*Metrics:*

* Distribution of `Tension_CA(m_field; e_CA)` in successful versus failed cases.
* Correlation between `Tension_CA(m_field; e_CA)` and independent assessments of governance quality or resource outcomes.
* Robustness of results under different reasonable choices of thresholds for success and failure, taken from the finite threshold sets attached to the encoding.

*Falsification conditions:*

* If a large proportion of clearly successful long lived commons cases produce `Tension_CA(m_field; e_CA)` in the high tension band, while many failed cases produce low tension values, the current Q107 encoding is considered misaligned with empirical evidence and must be revised.
* If including additional institutional detail in `m_field` consistently drives `Tension_CA(m_field; e_CA)` away from low tension for successful cases, instead of stabilizing it, the encoding is considered structurally flawed.

*Semantics implementation note:*
The same hybrid semantics as declared in the metadata is used. Continuous features capture averaged costs and benefits. Discrete features capture institutional categories and participation states. No deep mapping from raw field records to internal TU fields is specified.

*Boundary note:*
Falsifying a TU encoding does not solve the canonical problem. The experiment tests one effective encoding against empirical patterns but does not fully resolve the mechanisms of collective action.

---

## 7. AI and WFGY engineering spec

This block specifies how Q107 can be used as an engineering module for AI systems in the WFGY framework, at the effective layer and under a fixed encoding `e_CA`.

### 7.1 Training signals

We define several training signals that reuse Q107 observables.

1. `signal_free_rider_tension`

   * Definition: a nonnegative signal proportional to `DeltaS_incentive(m)` in contexts where the model discusses collective action or public goods.
   * Purpose: penalize internal states where the model implicitly assumes stable high cooperation while incentives remain far from the reference levels that could support such cooperation.

2. `signal_expectation_alignment`

   * Definition: a signal proportional to `DeltaS_expectation(m)`, applied when the model makes predictions about others participation.
   * Purpose: encourage the model to keep its narrative about expectations and actual participation consistent and to be explicit when it assumes unusual belief patterns.

3. `signal_CA_tension_total`

   * Definition: equal to `Tension_CA(m; e_CA)` when the model is in a socio technical collective action context.
   * Purpose: provide a scalar that can be minimized in reasoning tasks where the scenario explicitly describes robust successful collective action.

4. `signal_mechanism_explicitness`

   * Definition: a qualitative signal that is high when explanations list concrete mechanisms (communication, monitoring, sanctions, reputation, repeated interaction) that could reduce `DeltaS_incentive` and `DeltaS_expectation`, and low when explanations appeal only to vague goodwill.
   * Purpose: push the model to connect low tension claims to explicit mechanism patterns.

All of these signals are computed from effective-layer summaries of scenarios and do not require exposing any deep TU generative rule.

### 7.2 Architectural patterns

We outline module patterns that reuse Q107 components.

1. `CollectiveActionHead_CA`

   * Role: auxiliary head that takes internal representations of a socio technical scenario and outputs estimates of:

     * `DeltaS_incentive`
     * `DeltaS_expectation`
     * `Tension_CA`

   * Interface:

     * Inputs: context embeddings or structured scenario representations.
     * Outputs: three scalars and optional intermediate features.

2. `MechanismLibrary_CA`

   * Role: module that stores a library of mechanism patterns observed in Q107 like problems, such as local monitoring, graduated sanctions, or participatory rule making.
   * Interface:

     * Inputs: partial description of a scenario.
     * Outputs: candidate mechanisms and their expected impact on incentive and expectation mismatches.

3. `NormEvolutionObserver_CA`

   * Role: module that tracks how norms and institutions in a narrative are likely to change `DeltaS_CA(m)` over time.
   * Interface:

     * Inputs: multi step description of a process.
     * Outputs: sequence of predicted tension values and notes on mechanism activation.

These modules operate purely at the effective layer on internal representations. They do not implement or reveal any deep TU generative rules.

### 7.3 Evaluation harness

We propose an evaluation harness for AI systems that integrate Q107 components.

1. Task selection

   * Include question sets about:

     * climate cooperation and international agreements
     * large protests and social movements
     * commons governance and local public goods

2. Conditions

   * Baseline condition: model answers questions without explicit Q107 modules or signals.
   * TU condition: model uses `CollectiveActionHead_CA` and Q107 signals during reasoning.

3. Metrics

   * Structural consistency: fraction of outputs where the stated incentives, beliefs, and participation levels form a coherent narrative without obvious free rider contradictions.
   * Mechanism richness: number and variety of concrete mechanisms cited in successful collective action scenarios.
   * Counterfactual robustness: stability of reasoning when prompts switch between high cost and low cost variants, or between presence and absence of institutions.

4. Comparison

   * Compare baseline and TU conditions on these metrics.
   * Optionally, ask human evaluators familiar with collective action literature to blind rate which outputs better match known patterns.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to feel the impact of Q107 encoding.

* Baseline setup

  * Prompt: ask the AI to explain why large scale climate cooperation is difficult and what could make it succeed, with no mention of tension.
  * Observation: record whether the answer mixes vague moral appeals with limited discussion of incentives, beliefs, and networks.

* TU encoded setup

  * Prompt: ask the same question but explicitly instruct the AI to:

    * identify costs of participation
    * describe how beliefs about others participation matter
    * use a notion of incentive tension between predicted and observed cooperation

  * Observation: record whether the explanation includes clearer articulation of:

    * incentive mismatches
    * expectation mismatches
    * mechanisms that can reduce both

* Comparison metric

  * Rate both versions on:

    * clarity about free rider pressure
    * explicitness of mechanisms
    * consistency between described incentives and predicted outcomes

* What to log

  * The full prompts and outputs.
  * Any auxiliary estimates of `Tension_CA(m; e_CA)` produced by the `CollectiveActionHead_CA`.

This protocol does not require access to internal TU implementation. It only uses Q107 as an interpretive and structuring lens.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q107 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `CollectiveActionTensionFunctional_CA`

   * Type: functional

   * Minimal interface:

     * Inputs:

       * `participation_summary`
         fraction of contributing agents and scale of population

       * `incentive_summary`
         average net cost or benefit of participation relative to free riding

       * `belief_summary`
         expected participation fraction based on beliefs or common knowledge

     * Output:

       * `tension_value` in `Par_CA`, a nonnegative scalar

   * Preconditions:

     * Summaries are internally consistent for a single collective action context.
     * Costs and benefits are finite and defined on the same time horizon.

2. ComponentName: `IncentiveNetworkField_CA`

   * Type: field

   * Minimal interface:

     * Inputs:

       * `agent_types`
       * `network_structure`
       * `payoff_parameters`
       * `institutional_descriptors`

     * Output:

       * a finite collection of local incentive values for each type or group

   * Preconditions:

     * Network is finite and well defined.
     * Payoffs and institutional descriptors are finite and lie in `Par_CA` or discrete label sets.

3. ComponentName: `CounterfactualCollectiveWorlds_CA`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs:

       * `scenario_class` describing a family of collective action settings

     * Output:

       * a pair of experiment blueprints:

         * `World_T_CA` blueprint with high participation and low tension targets
         * `World_F_CA` blueprint with failure and high tension targets

   * Preconditions:

     * Scenario class allows construction of effective summaries in `M_CA_reg(e_CA)`.

### 8.2 Direct reuse targets

1. Target: Q108 · `BH_SOC_POLARIZATION_L3_108`

   * Reused component: `CollectiveActionTensionFunctional_CA`.
   * Why it transfers: political polarization often involves costly participation in partisan actions that resemble collective action around group identity.
   * What changes:

     * `participation_summary` includes metrics like turnout, activism, and online activity.
     * `incentive_summary` includes identity payoffs and perceived gains from polarization.

2. Target: Q110 · `BH_SOC_INSTITUTION_EVOL_L3_110`

   * Reused component: `IncentiveNetworkField_CA`.
   * Why it transfers: institutional evolution is driven by how rules change incentives and expectations over repeated collective actions.
   * What changes:

     * New slow dynamics are added on institutional descriptors.
     * Tension trajectories are tracked across multiple periods instead of single states.

3. Target: Q125 · `BH_AI_MULTIAGENT_L3_125`

   * Reused components: `CollectiveActionTensionFunctional_CA`, `IncentiveNetworkField_CA`, and `CounterfactualCollectiveWorlds_CA`.
   * Why it transfers: multi agent AI systems can face collective action style coordination and free rider issues with respect to shared safety goals or resource use.
   * What changes:

     * Agents become AI systems or AI plus human teams.
     * Payoff parameters include alignment and safety metrics instead of purely economic payoffs.

---

## 9. TU roadmap and verification levels

This block explains how Q107 is positioned on the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* `E_level: E1`

  * An effective encoding class has been specified:

    * state space `M_CA`
    * key observables for incentives, beliefs, and participation
    * mismatch quantities `DeltaS_incentive` and `DeltaS_expectation`
    * combined tension `DeltaS_CA` and `Tension_CA(m; e_CA)`
    * an admissible encoding class `E_CA_enc` with finite libraries and fixed thresholds

  * No full implementation or public code has yet been provided for computing these quantities from data.

* `N_level: N1`

  * A coherent narrative describes:

    * the free rider tension
    * the role of network and institutions
    * the contrast between robust and fragile collective action worlds
    * how Q107 components can be reused in other problems

### 9.2 Next measurable step toward E2 and N2

To reach `E2`, the following concrete steps are proposed:

1. Implement a simple tool that, given summarized data from laboratory or field studies, constructs states in `M_CA_reg(e_CA)` and computes:

   ```txt
   DeltaS_incentive(m)
   DeltaS_expectation(m)
   Tension_CA(m; e_CA)
   ```

   for a fixed encoding `e_CA`.

2. Apply this tool to at least one publicly available dataset from collective action experiments and one from commons governance, and publish the resulting tension profiles together with the encoding specification.

To reach `N2`, the following narrative improvements are proposed:

1. Provide detailed case studies of:

   * one robust World T like system
   * one fragile World F like system

   and explicitly map which mechanisms act on `DeltaS_incentive` and `DeltaS_expectation` in each case.

2. Use Q107 components in at least one downstream problem description, such as Q108 or Q110, with explicit references to shared components and concrete cross problem transfer.

### 9.3 Long term role in the TU program

In the longer term, Q107 is expected to serve as:

* the central node for all problems that involve large numbers of agents solving or failing to solve incentive_tension at scale
* a bridge between economic models of public goods, empirical institutional analysis, and AI multi agent coordination
* a calibration point for how TU style encodings can handle social and institutional complexity without claiming full predictive or generative power

Q107 will also act as a reference when evaluating whether new socio technical case studies can be integrated into a unified tension based framework.

---

## 10. Elementary but precise explanation

This block is written for non experts while staying faithful to the effective layer description.

Many important human achievements require large groups of people to do costly things together. Examples include:

* paying taxes to fund public services
* following rules that protect common resources
* joining protests, strikes, or campaigns
* changing behavior for climate or public health reasons

Individually, it is often cheaper to stay home, keep your money, and let others do the work. This is the free rider problem.

Q107 asks:

* How do we know when people will actually cooperate at large scale.
* What kinds of rules, norms, and networks make cooperation robust instead of fragile.
* How can we describe this in a way that is precise and testable, without pretending to have a single magic formula.

In the Tension Universe view, we imagine a space of possible worlds. Each world is described by:

* how many people are involved
* how many of them are participating
* how costly participation is
* what people believe about others participation
* how people are connected in networks
* what rules and institutions exist

For each world, we measure two gaps:

1. Incentive gap: is the actual incentive for people to join close to the level that would normally support the observed participation, or is there a big mismatch.

2. Expectation gap: are people beliefs about others participation close to what actually happens, or is there a big mismatch.

We combine these into a single number called `Tension_CA(m; e_CA)`.

* If `Tension_CA` is small, then the world looks self consistent. People incentives and beliefs fit the observed cooperation.
* If `Tension_CA` is large, then the world looks strained. Cooperation exists in a way that seems unlikely to last, or cooperation is failing in a way that contradicts normal expectations.

We then compare two kinds of worlds.

* In robust worlds, many people cooperate for a long time even though it is costly, and `Tension_CA` can be kept small because institutions, norms, and information are doing the right work.

* In fragile worlds, cooperation either never gets going or collapses quickly, and `Tension_CA` stays large because incentives and beliefs are not aligned with what is required.

Q107 does not try to replace all social science with one equation. Instead it gives:

* a precise way to talk about the tension in large scale cooperation
* a checklist for what data and experiments can tell us about this tension
* reusable tools that help AI systems think more clearly about incentives, beliefs, and institutions whenever collective action is involved

In this sense, Q107 is a building block for understanding how groups act together in a structured and testable way, rather than a final answer to why any particular movement or policy succeeds or fails.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** S problem collection.

### Scope of claims

* The goal of this document is to specify an effective-layer encoding of the Q107 collective action problem.
* It does not prove or disprove any canonical statement about the possibility or impossibility of large scale collective action.
* It does not claim that the corresponding open problems in economics, political science, or sociology have been solved.
* It should not be cited as evidence that any specific collective action mechanism will succeed or fail in the real world.

### Effective-layer boundary

* All objects used here (state spaces `M_CA`, parameter spaces `Par_CA`, incentive and belief fields, mismatch quantities, tension values, and counterfactual worlds) live at the effective layer of the TU framework.
* No explicit generative mapping from raw social data to these internal objects is provided in this document.
* Any such mapping used in applications must be documented separately and may be evaluated or rejected without altering the definitions given here.

### Encoding and fairness

* All encodings are drawn from an admissible class `E_CA_enc` with finite libraries of reference functions, finite sets of allowed weights, and finite grids of tension thresholds.
* Once an encoding `e_CA` is fixed for an experiment or application, its components are held fixed and are not tuned based on observed outcomes.
* Changing reference functions, weights, or thresholds corresponds to selecting a new encoding and requires new experiments if comparisons are to remain valid.

### Experiments and falsifiability

* The experiments in Section 6 are designed to falsify or support particular encodings at the effective layer.
* Falsifying an encoding does not falsify the canonical collective action problem or any real world theory. It only shows that a specific TU encoding fails to capture observed patterns or behaves inconsistently.
* Passing these experiments does not prove that the encoding is uniquely correct, only that it is coherent under the specified tests.

### Engineering use

* The AI and WFGY engineering patterns in Section 7 describe how Q107 components can be used as diagnostic and structuring tools inside AI systems.
* They do not provide guarantees about real world outcomes. They are intended to reduce internal contradictions and make incentive and belief structures more explicit in reasoning processes.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)

