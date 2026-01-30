# Q104 · Dynamics of wealth and income inequality

---

## 0. Header metadata

```txt
ID: Q104
Code: BH_ECON_INEQUALITY_DYN_L3_104
Domain: Economics
Family: Wealth and income distribution; long run dynamics
Rank: S
Projection_dominance: I
Field_type: socio_technical_field
Tension_type: incentive_tension
Status: Open_structural_puzzle
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

More precisely:

* This document only specifies:

  * state spaces and observables for long run inequality regimes,
  * admissible inequality encodings and mismatch functionals,
  * a tension tensor used for bookkeeping,
  * world templates, experiments, and AI engineering interfaces that depend on those objects.

* This document does not:

  * define or expose any deep TU axiom system or generative field equations,
  * modify the canonical economic and statistical definitions of inequality,
  * claim to prove or solve the canonical inequality dynamics problem described in Section 1,
  * introduce any new theorem about real world economies.

* All inequality tension quantities are defined relative to:

  * explicit encoding classes `E_ineq`,
  * explicit baselines and reference libraries,
  * explicit weights and constraint descriptors.

Changing these elements is treated as changing the encoding, not as retuning the same object.

* The tensor `T_ij(m)` defined in Section 3 is used only as a bookkeeping device for inequality tension accounting at the effective layer. It is not a field equation and it is not a dynamical law.

Any interpretation of this document must respect these boundaries. It may be used to design and test effective layer encodings and experiments, but not as evidence that TU has determined the true dynamics or ethics of inequality.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical inequality dynamics problem can be stated as follows.

Consider a society with:

* a distribution of wealth and income across individuals or households,
* an intergenerational structure (parents, children, cohorts),
* macroeconomic conditions (growth, shocks, structural change),
* institutions (tax systems, education, labor markets, finance, social insurance).

The central questions are:

1. Why do some societies exhibit persistent high wealth and income concentration at the top, while others sustain more compressed distributions?
2. How do mobility patterns, both within cohorts and across generations, interact with static inequality measures?
3. Under what conditions do technological change, globalization, and policy produce:

   * convergent dynamics, where inequality stabilizes within a moderate band,
   * divergent dynamics, where inequality and concentration keep drifting upward,
   * regime shifts, where inequality abruptly changes level and structure?

At a classical level, Q104 is not asking for a single microfounded model. It asks for:

* a coherent description of the long run patterns of wealth and income inequality,
* a structural understanding of which combinations of mechanisms and constraints can explain them,
* a way to distinguish inequality that is plausibly justified by constraints and trade offs from inequality that remains puzzling even after constraints are taken into account.

### 1.2 Status and difficulty

There is no single accepted theory of long run inequality dynamics. Instead, several partial frameworks coexist.

Empirical literatures cover:

* top income and wealth shares over more than a century in several countries,
* Gini and related indices across time and countries,
* measures of social and intergenerational mobility.

Theoretical literatures cover:

* dynamic models of capital accumulation and savings,
* heterogeneous agent macroeconomics with incomplete markets,
* political economy of redistribution,
* skill biased technological change and globalization,
* institutional and historical accounts of inequality regimes.

Points of partial consensus include:

* inequality levels and trajectories differ markedly across countries and time, even with broadly similar technologies,
* institutions and policies matter for distributional outcomes,
* mobility and opportunity can diverge from static inequality measures.

Open difficulties include:

* disentangling the contributions of technology, policy, and shocks,
* dealing with measurement limitations, especially at the top of the distribution,
* assessing which inequality levels are inevitable given constraints and which are regime choices,
* integrating macro constraints such as climate and planetary boundaries into long run inequality analysis.

Q104 is therefore a structural, long horizon, multi factor problem. It is not about a single scalar inequality index. It is about the joint dynamics of:

* distribution shape,
* mobility,
* constraints,
* institutions and incentives.

### 1.3 Role in the BlackHole project

Within the BlackHole S-collection, Q104 plays several roles.

1. It is the primary node for long run wealth and income inequality regimes, at the same level as:

   * Q103 (long run productivity slowdown),
   * Q098 (Anthropocene system dynamics),
   * Q101 (equity premium puzzle).

2. It anchors the distributional branch of socio technical problems:

   * providing inequality regimes and tension measures that feed into financial stability (Q105),
   * interacting with global migration (Q109),
   * interacting with climate and planetary constraints (Q091, Q098),
   * feeding into AI impact and policy nodes (Q121, Q124).

3. It is the canonical example of incentive_tension in a socio technical field:

   * tension between incentives at the micro level, for example returns to capital, gig work, bargaining power,
   * and macro level distribution patterns and social objectives.

Q104 is not intended to solve inequality in a policy sense. At the effective layer, it encodes how to:

* describe inequality regimes as states,
* measure tension between observed distributions and constraint compatible baselines,
* compare worlds with different inequality dynamics.

### References

1. Thomas Piketty, Capital in the Twenty-First Century, Harvard University Press, 2014.
2. Anthony B. Atkinson, Inequality: What Can Be Done?, Harvard University Press, 2015.
3. World Inequality Database (WID), official online database and documentation on income and wealth inequality indicators.
4. OECD, Income inequality and related indicator documentation, official statistics pages on inequality and redistribution.

---

## 2. Position in the BlackHole graph

This block records Q104’s edges in the BlackHole graph, using only Q identifiers and one line reasons per edge.

### 2.1 Upstream problems

These nodes provide constraints, tools, or background regimes that Q104 imports at the effective layer.

* Q103
  Reason: Supplies long run productivity and growth regimes which serve as macro constraints for feasible inequality paths.

* Q098
  Reason: Provides Anthropocene level environmental and resource constraints that shape the long run feasible set of income and wealth distributions.

* Q091
  Reason: Links climate sensitivity and damage to long horizon output and capital paths that bound sustainable inequality.

### 2.2 Downstream problems

These nodes directly reuse Q104 components or treat Q104 tension variables as inputs.

* Q101
  Reason: Reuses inequality tension indices and wealth concentration observables when defining asset pricing and risk bearing puzzles.

* Q105
  Reason: Uses high inequality tension regimes as part of fragility and systemic crash risk indicators.

* Q109
  Reason: Uses persistent inequality and mobility gaps as drivers of migration incentives and destination choices.

### 2.3 Parallel problems

These nodes share similar tension types or field types but lack direct component dependence.

* Q121
  Reason: Both Q104 and Q121 involve distributional consequences of powerful technologies and tension between potential gains and realized welfare.

### 2.4 Cross-domain edges

These edges connect Q104 to nodes in other domains via shared observables or components.

* Q091
  Reason: Uses inequality specific constraints derived from climate sensitivity scenarios when evaluating distributional paths.

* Q092
  Reason: Interacts through social cost and damage functions where inequality affects vulnerability and adaptation capacity.

* Q098
  Reason: Reuses inequality regimes and tension levels as part of socio ecological resilience and transition narratives.

* Q121
  Reason: Reuses inequality tension components when assessing how AI deployment affects social stratification and opportunity.

* Q124
  Reason: Uses Q104 components as part of oversight and governance schemes for managing the distributional impact of AI and technology.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state space,
* observables and fields,
* mismatch functionals and admissible encoding class,
* tension tensor form,
* invariants and singular sets.

We do not describe any hidden generative rules or any mapping from raw micro data to TU internal fields.

### 3.1 State space

We posit a state space:

```txt
M
```

where each state `m` in `M` represents a long run inequality regime state for a given society and time window.

For each `m`, the encoding contains:

* wealth distribution summary:

  * indices of concentration, for example top share vectors, tail indicators,
  * overall dispersion indicators,

* income distribution summary:

  * separation between labor income, capital income, transfers, and other components,
  * dispersion indicators for each component,

* mobility and persistence summary:

  * measures of intra cohort and intergenerational mobility,
  * indicators of segregation and stratification,

* structural and institutional summary:

  * tax and transfer system descriptors,
  * core labor market and financial market regime labels,
  * education and skill distribution descriptors,

* macro and constraint background:

  * growth regime tags imported from Q103,
  * constraint vectors imported from Q091 and Q098, for example emission constraints, damage levels,

* inequality regime label:

  * a discrete label `R_regime_ineq(m)` such as compressed middle, dualized labor market, top heavy concentration, inequality trap.

The representation within each `m` uses:

* continuous quantities for distribution statistics, mobility indices, and macro aggregates,
* discrete labels for regimes, institutional types, and classes.

No assumption is made here about how these summaries are computed from underlying micro data.

### 3.2 Effective fields and observables

We define the following effective fields and observables on `M`.

1. Wealth distribution descriptor

```txt
D_wealth(m)
```

* A vector or structured descriptor encoding wealth distribution patterns in state `m`.
* Includes, at minimum, top share indicators, dispersion measures, and a tail behavior summary.

2. Income distribution descriptor

```txt
D_income(m)
```

* A descriptor analogous to `D_wealth(m)`, but for income flows.

3. Mobility descriptor

```txt
M_mobility(m)
```

* Encodes mobility indicators, including:

  * transition probabilities across income or wealth quantiles,
  * intergenerational elasticity or related measures,
  * qualitative regime tags such as high mobility or low mobility.

4. Structural constraint vector

```txt
C_struct(m)
```

* A vector encoding:

  * macro constraints from Q103, for example growth regime tags, output constraints,
  * environmental and resource constraints from Q091 and Q098,
  * demographic and technological background.

5. Regime label

```txt
R_regime_ineq(m)
```

* A discrete label summarizing the qualitative inequality regime in state `m`, derived from `D_wealth(m)`, `D_income(m)`, `M_mobility(m)`, and `C_struct(m)`.

### 3.3 Admissible inequality encoding class

We define an admissible inequality encoding class `E_ineq` at the effective layer.

Each element of `E_ineq` is an encoding scheme that:

* assigns baselines and reference profiles for:

  * distribution levels,
  * mobility patterns,
  * constraint consistent trade offs,

* defines mismatch functionals that compare actual descriptors with these baselines.

We do not specify how elements of `E_ineq` are constructed. Instead, we impose constraints that must hold for any admissible encoding.

We fix a finite reference library:

```txt
L_ref_ineq
```

containing documented historical episodes, including:

* low inequality regimes with well studied policies and institutions,
* high inequality regimes,
* episodes of rising and falling inequality under known constraints.

Constraints on baselines:

* Baseline distributions and mobility profiles must be constraint compatible:

  * they must satisfy macro constraints encoded in `C_struct(m)`,
  * they must respect basic accounting identities, for example totals must match aggregates,
  * they must be robust to small changes in measurement thresholds.

* Baselines must be state independent within a regime and constraint class:

  * for a given combination of macro constraints and norm profiles, the baseline is fixed,
  * the baseline cannot be tuned separately for each state to match observed inequality.

Constraints on mismatch functionals:

We define three nonnegative mismatch functionals:

```txt
DeltaS_level(m)        >= 0
DeltaS_mobility(m)     >= 0
DeltaS_consistency(m)  >= 0
```

interpreted as:

* `DeltaS_level(m)`: mismatch between actual concentration patterns in `D_wealth(m)` and `D_income(m)` and constraint compatible baselines,
* `DeltaS_mobility(m)`: mismatch between actual `M_mobility(m)` and baseline mobility profiles under similar constraints and norms,
* `DeltaS_consistency(m)`: mismatch capturing cases where high inequality appears inconsistent with resource scarcity, risk bearing needs, or other structural justifications encoded in `C_struct(m)`.

Each mismatch functional must satisfy:

* dependence only on:

  * `D_wealth(m)`, `D_income(m)`, `M_mobility(m)`, `C_struct(m)`,
  * baselines chosen from `L_ref_ineq` given constraint class,

* independence from state specific tuning:

  * baselines cannot depend on detailed inequality values in the particular `m` under evaluation,
  * baselines are selected by rule from constraint class, not by outcome matching.

For each encoding `e` in `E_ineq`, we associate a fixed choice of:

* reference library version,
* baseline selection rules,
* mismatch functional definitions.

If any of these are altered in a way that depends on the observed pattern of `Tension_ineq(m)` or on particular states in `M`, this is treated as defining a new encoding `e'` rather than retuning `e`.

### 3.4 Inequality tension tensor

We define a combined inequality tension:

```txt
DeltaS_ineq_total(m) =
  w_level * DeltaS_level(m) +
  w_mob   * DeltaS_mobility(m) +
  w_cons  * DeltaS_consistency(m)
```

with weights satisfying:

```txt
w_level >= 0
w_mob   >= 0
w_cons  >= 0
w_level + w_mob + w_cons = 1
```

The weights are:

* fixed once per encoding `e` in `E_ineq`,
* independent of the state `m`,
* chosen by explicit rule before evaluating any particular dataset,
* not adjusted afterwards in response to observed inequality tension values.

The inequality tension tensor on `M` is defined at the effective layer as:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_ineq_total(m)
          * lambda_regime_ineq(m) * kappa_ineq
```

where:

* `S_i(m)` indexes source factors, for example wage structure, capital market structure, institutional features,
* `C_j(m)` indexes receptor factors, for example social cohesion, political stability, macro performance,
* `lambda_regime_ineq(m)` is a regime dependent factor, with values in a bounded interval, encoding whether inequality dynamics are convergent, trapped, or chaotic,
* `kappa_ineq` is a fixed scale factor for inequality tension.

We do not specify the detailed indexing sets for `i` and `j`. It is sufficient that for each `m` in `M`, the tensor components are finite and well defined.

In this document, `T_ij(m)` is a bookkeeping tensor for inequality tension accounting at the effective layer. It is not a field equation, it is not a law of motion, and no claim is made that real world inequality follows any differential equation built from `T_ij`.

### 3.5 Invariants and domain restrictions

We define the following invariants and singular set.

1. Inequality tension index for a given encoding `e` in `E_ineq`:

```txt
I_ineq_e(m) = DeltaS_ineq_total(m)
```

for all `m` in `M` where the mismatch functionals are defined. Whenever `I_ineq_e` is used, the index `e` is conceptually part of the object. Different encodings are not compared on an absolute numerical scale without explicit mapping rules.

2. Regime level invariants:

* The distribution of `I_ineq_e(m)` across states sharing the same constraint class and regime label `R_regime_ineq(m)`.
* The persistence of high tension for a given society across time windows under refinement.

3. Refinement sequences:

We consider sequences of states:

```txt
m_r in M
```

indexed by a resolution parameter `r`, where higher `r` corresponds to:

* more detailed distribution splits,
* finer measurement of mobility,
* more resolved constraints.

For an admissible encoding `e` in `E_ineq`, we require that:

```txt
sup over r of I_ineq_e(m_r) < infinity
```

for any refinement sequence representing the same underlying society and regime.

This prevents trivial divergence of mismatch values from being treated as structural high tension.

4. Singular set:

We define a singular set:

```txt
S_sing = { m in M :
  core distribution or mobility descriptors are structurally missing,
  structurally inconsistent, or dominated by measurement breakdown }
```

The regular domain is:

```txt
M_reg = M \ S_sing
```

All inequality tension analysis for Q104 is restricted to `M_reg`. Whenever an experiment would require evaluation of `DeltaS_ineq_total(m)` for `m` in `S_sing`, the result is treated as out of domain rather than informative evidence.

---

## 4. Tension principle for this problem

This block encodes Q104 as a tension principle at the effective layer.

### 4.1 Core inequality tension functional

We define the inequality tension functional:

```txt
Tension_ineq(m) = DeltaS_ineq_total(m)
```

for all `m` in `M_reg` and for any fixed admissible encoding `e` in `E_ineq`.

By construction:

```txt
Tension_ineq(m) >= 0
```

and:

* small values indicate:

  * distribution levels close to constraint compatible baselines,
  * mobility patterns close to baselines,
  * consistency between inequality and structural constraints,

* large values indicate:

  * inequality levels or mobility patterns far from baselines,
  * or apparent contradiction between inequality and structural constraints.

### 4.2 Low-tension principle for inclusive dynamics

At the effective layer, a low-tension inequality world satisfies:

For each major society and broad time window, there exists a refinement sequence:

```txt
m_r in M_reg
```

and an admissible encoding `e` in `E_ineq` such that:

```txt
sup over r of Tension_ineq(m_r) <= epsilon_ineq
```

for a small threshold `epsilon_ineq` that:

* may depend on the constraint class, for example stricter constraints can allow somewhat higher tension,
* remains bounded and moderate as resolution increases.

Informally:

* after adjusting for macro constraints and plausible trade offs, inequality tension can be kept in a low band,
* high inequality episodes are either transient or clearly tied to constraints, shocks, or explicit policy choices.

### 4.3 High-tension inequality trap

A high-tension inequality trap world satisfies:

For some societies and constraint classes, for every admissible encoding `e` in `E_ineq` and for every refinement sequence:

```txt
m_r in M_reg
```

representing those societies, there exists a strictly positive `delta_ineq` such that:

```txt
inf over r of Tension_ineq(m_r) >= delta_ineq > 0
```

In words:

* persistent high inequality and low mobility cannot be explained away by:

  * measurement noise,
  * plausible constraint based baselines,
  * modest disagreements about weights,

* there is a residual tension that remains across refinements and admissible encodings.

### 4.4 Q104 in TU terms

Q104, at the effective layer, is the structured question:

> For which societies, constraint regimes, and historical paths does the inequality world look low tension, and for which does it look trapped in high tension, under admissible encodings in `E_ineq`?

The problem is then:

* to define and stress test `E_ineq`,
* to map real and model worlds to states in `M_reg`,
* to study the structure of low and high tension regimes.

---

## 5. Counterfactual tension worlds

We describe two counterfactual world templates at the effective layer.

* World T: inclusive dynamics with low inequality tension.
* World F: structural inequality trap with persistent high inequality tension.

These are templates for observable patterns, not specifications of generative mechanisms.

### 5.1 World T (inclusive dynamics, low inequality tension)

In World T:

1. Distribution patterns:

   * For most societies and time windows, `D_wealth(m)` and `D_income(m)` lie within moderate concentration bands when measured relative to constraint compatible baselines.
   * Extreme concentration episodes occur, but are short lived or clearly reversible.

2. Mobility and opportunity:

   * `M_mobility(m)` indicates high or at least moderate mobility across cohorts.
   * Intergenerational elasticity is moderate; opportunities are not tightly bound to parental status.
   * Social and geographic mobility paths are open for large fractions of the population.

3. Consistency with constraints:

   * High inequality periods coincide with recognizably tight constraints:

     * severe shocks,
     * rapid structural transitions,
     * binding climate or resource limits.

   * When constraints relax or policies adjust, `DeltaS_consistency(m)` tends to decrease.

4. Inequality tension:

   * For societies operating under stable constraints, refinement sequences `m_r` with fixed `e` in `E_ineq` satisfy:

     ```txt
     Tension_ineq(m_r) <= epsilon_ineq
     ```

     for modest `epsilon_ineq` that does not grow with resolution.
   * The spatial and temporal pattern of high tension states is sparse.

### 5.2 World F (structural inequality trap, high inequality tension)

In World F:

1. Distribution patterns:

   * Many advanced societies exhibit very high concentration in `D_wealth(m)` and `D_income(m)`, sustained over multiple generations.
   * Measured top shares and tails remain elevated even when macro constraints are mild.

2. Mobility and opportunity:

   * `M_mobility(m)` indicates low mobility and strong intergenerational persistence.
   * There are clear patterns of class, region, and group locked into persistent disadvantage.
   * Segregation indicators remain high even under growth.

3. Consistency with constraints:

   * High inequality frequently coincides with:

     * substantial slack in macro constraints,
     * abundant capital and slack resources,
     * weak links between risk bearing and realized returns.

   * For such states, any reasonable `DeltaS_consistency(m)` remains large.

4. Inequality tension:

   * For many societies and time windows, for every admissible `e` in `E_ineq`, refinement sequences `m_r` satisfy:

     ```txt
     Tension_ineq(m_r) >= delta_ineq
     ```

     with `delta_ineq` strictly positive and stable across refinements.
   * High tension regions in the space of societies and times appear as thick bands, not isolated points.

### 5.3 Interpretive note

These world templates:

* do not claim to specify unique causes,
* do not specify any micro generative rule for how inequality arises,
* only describe observable patterns that admissible encodings in `E_ineq` must be able to represent.

They are intended to guide the design and stress testing of inequality tension encodings, not to provide historical judgments or policy prescriptions.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments that:

* test the coherence and usefulness of Q104 encodings,
* discriminate between different encodings within `E_ineq`,
* provide empirical constraints on how inequality tension is defined.

Falsification applies to encodings and models, not to the canonical statement itself.

### Experiment 1: Cross-country panel inequality tension profiling

Goal:
Assess whether a given encoding in `E_ineq` produces nontrivial, stable inequality tension profiles across countries and time.

Setup:

* Data: cross-country panel of:

  * wealth and income distribution summaries,
  * mobility indicators,
  * macro constraints such as growth, shocks, climate and resource indicators,
  * institutional descriptors,
    over a fixed horizon, for example several decades.

* Encoding: fix a specific encoding `e` in `E_ineq`:

  * baselines chosen from `L_ref_ineq` by rule based on constraint class,
  * weights `w_level`, `w_mob`, `w_cons` fixed before evaluation.

Protocol:

1. For each country and time window with sufficient data, construct a state `m` in `M_reg` using the observable descriptors.

2. Compute `DeltaS_level(m)`, `DeltaS_mobility(m)`, `DeltaS_consistency(m)` and then `Tension_ineq(m)` under encoding `e`.

3. Record the distribution of `Tension_ineq(m)`:

   * across countries at a fixed time,
   * across time for a fixed country.

4. Perform basic stability checks:

   * refine measurement, for example more quantile bins, more detailed mobility measures, to obtain sequences `m_r`,
   * recompute `Tension_ineq(m_r)` and check how values change with resolution.

Metrics:

* Empirical distribution of `Tension_ineq(m)` across all `m` in the panel.
* Cross country variance and cross time variance.
* Maximum relative change in `Tension_ineq(m_r)` under resolution refinement.
* Fraction of states with `Tension_ineq(m)` lying in a very narrow band near zero.

Falsification conditions:

* Triviality rejection:
  If for at least a large majority of states in the panel, for example 80 percent, `Tension_ineq(m)` lies in a fixed very small band around zero, despite large differences in observed inequality and mobility, then encoding `e` is rejected as trivial.

* Instability rejection:
  If for more than a fixed fraction of refinement sequences `m_r`, for example 20 percent, the ratio

  ```txt
  max_r Tension_ineq(m_r) / min_r Tension_ineq(m_r)
  ```

  exceeds a fixed large threshold, for example 10, without a structural explanation such as a detected measurement transition, encoding `e` is rejected as unstable.

* Constraint violation rejection:
  If, in order to keep `Tension_ineq(m)` low for high inequality states, encoding `e` is forced to choose baselines that violate macro constraints encoded in `C_struct(m)`, then `e` is rejected as constraint inconsistent.

Semantics implementation note:
This experiment uses only the mixed representation of continuous distribution and mobility quantities with discrete regime labels defined in the state space and observables description in Section 3. No additional representation choices are introduced here.

Boundary note:
Rejecting an encoding in this experiment does not solve the canonical inequality dynamics problem. It only shows that a particular effective layer encoding is not compatible with the observed cross-country panel under the stated constraints.

---

### Experiment 2: Constraint and norm consistent baseline family

Goal:
Test whether inequality tension encodings can keep tension low using baselines that are consistent with both constraints and stated social norms, without tuning baselines per state.

Setup:

* Data: a set of historical episodes for multiple societies, including:

  * inequality and mobility descriptors,
  * macro constraints and shocks,
  * documentation of stated social norms or policy targets such as official goals regarding opportunity and distribution.

* Baselines: define a small family of candidate baseline specifications:

  * each baseline `b_k` maps a constraint class and norm profile to a distribution and mobility profile,
  * baselines are defined globally, not per state.

Protocol:

1. For each episode, assign a constraint class and norm profile based on `C_struct(m)` and documented policy goals.

2. For each baseline `b_k` in the family:

   * determine baseline distributions and mobility profiles implied by `b_k` for that class,
   * compute `DeltaS_level(m)`, `DeltaS_mobility(m)`, `DeltaS_consistency(m)`, and `Tension_ineq(m)` using these baselines.

3. Compare tension levels across baselines:

   * for each episode, record the minimum `Tension_ineq(m)` achieved across baselines,
   * track which baselines are constraint consistent.

Metrics:

* Distribution of minimum `Tension_ineq(m)` across episodes.
* Number of episodes for which any baseline in the family keeps tension below a moderate threshold `epsilon_ineq`.
* Number of episodes requiring baselines that violate constraints in order to reduce tension.

Falsification conditions:

* Per state tuning rejection:
  If the only way to keep `Tension_ineq(m)` low for high inequality episodes is to define baselines that are effectively tuned to match those episodes on a one by one basis, rather than selected from a global family, the encoding is rejected as violating state independence constraints.

* Constraint incompatible baseline rejection:
  If, for many episodes, the only baselines that keep `Tension_ineq(m)` low require obvious violations of constraints, for example total wealth or income exceeding macro aggregates or mobility patterns unsupported by data, the encoding and baseline family are rejected as constraint incompatible.

Semantics implementation note:
This experiment uses the same mixed representation and invariants defined in Section 3 and does not introduce any new representation assumptions.

Boundary note:
Rejecting particular baselines or baseline families in this experiment does not determine which inequality dynamics actually occur in the real world. It only constrains which combinations of baselines and encodings are compatible with documented constraints and norms.

---

## 7. AI and WFGY engineering spec

This block describes how Q104 can be used as an engineering module for AI systems within WFGY, at the effective layer.

### 7.1 Training signals

We define training signals that can be derived from Q104 observables and mismatch functionals.

1. `signal_ineq_gap`

   * Definition: a scalar signal proportional to `DeltaS_level(m)` for the current encoded social context.
   * Purpose: penalize reasoning patterns or proposals that implicitly ignore large distributional gaps relative to constraint compatible baselines.

2. `signal_mobility_tension`

   * Definition: a signal proportional to `DeltaS_mobility(m)` when the model outputs claim high opportunity but the encoded mobility descriptors suggest otherwise.
   * Purpose: encourage the model to keep claims about opportunity and mobility consistent with inequality and mobility data.

3. `signal_constraint_fairness`

   * Definition: a signal combining `DeltaS_consistency(m)` with constraint descriptors from `C_struct(m)`.
   * Purpose: penalize arguments that justify inequality by appealing to constraints that, under the encoded structure, do not actually bind.

4. `signal_regime_shift_alert`

   * Definition: a signal that activates when the model’s narrative implies a transition between inequality regimes `R_regime_ineq(m)` without corresponding changes in constraints or institutions.
   * Purpose: prompt the model to check whether claimed regime shifts are supported by structural changes.

### 7.2 Architectural patterns

We outline module patterns that reuse Q104 components without exposing any deep generative rules.

1. `InequalityTensionHead`

   * Role: an auxiliary head that, given an internal embedding of a social or policy context, outputs an estimate of `DeltaS_ineq_total(m)` and its decomposition.
   * Interface:

     * Inputs: internal embedding of the current context, plus optional explicit inequality and mobility descriptors.
     * Outputs: `t_hat_total`, `t_hat_level`, `t_hat_mobility`, `t_hat_consistency`.

2. `MobilityFieldObserver`

   * Role: a module that extracts a structured `M_mobility` descriptor from internal representations.
   * Interface:

     * Inputs: embeddings of narratives or data about intergenerational or intra cohort outcomes.
     * Outputs: a low dimensional representation of mobility patterns, suitable for mismatch evaluation.

3. `ConstraintAwareScenarioModule`

   * Role: a module that evaluates policy or scenario descriptions against constraint descriptors `C_struct(m)` and inequality tension indices.
   * Interface:

     * Inputs: scenario description, constraint vector, inequality and mobility descriptors.
     * Outputs: qualitative flags and scores indicating whether the scenario moves towards lower or higher inequality tension under constraints.

### 7.3 Evaluation harness

We define an evaluation harness for AI systems using Q104 modules.

1. Task selection:

   * Questions about long run inequality trends in specific countries.
   * Comparative questions about different policy regimes and their distributional impact.
   * Scenario questions combining climate constraints, growth, and inequality.

2. Conditions:

   * Baseline condition:

     * The AI system operates without explicit Q104 modules.
     * It answers questions using general knowledge and internal heuristics.

   * TU condition:

     * The system uses `InequalityTensionHead`, `MobilityFieldObserver`, and `ConstraintAwareScenarioModule`.
     * Training uses Q104 derived signals to stabilize distributional reasoning.

3. Metrics:

   * Structural coherence:

     * consistency between descriptions of inequality, mobility, and constraints within a single answer,
     * explicit mention of trade offs when relevant.

   * Cross scenario consistency:

     * stability of inequality narratives when constraints are held fixed and only policies change,
     * appropriate shifts in narratives when constraints change.

   * Expert evaluation:

     * expert ratings on whether the AI’s answers correctly capture known distributional facts and tensions for selected cases.

### 7.4 60-second reproduction protocol

A minimal protocol to let external users probe the impact of Q104 encoding in an AI system.

* Baseline setup:

  * Prompt:
    Explain how wealth and income inequality have evolved in country X over the last decades, and what role economic constraints and policy have played.
  * Observation: record whether the answer:

    * mentions both inequality and mobility,
    * connects them to constraints,
    * acknowledges uncertainty and contested points.

* TU encoded setup:

  * Prompt: same as above, but with an added instruction:
    Use an explicit notion of inequality tension between what is feasible under constraints and what is actually observed, and explain which parts of the story correspond to high or low tension.
  * Observation: record whether the answer:

    * introduces a clear inequality tension concept,
    * separates constraint driven and policy driven contributions,
    * highlights inequality trap patterns where relevant.

* Comparison metric:

  * Use a rubric with scores for:

    * structural clarity,
    * explicit attention to distribution and mobility,
    * correct use of constraint information.

* What to log:

  * Full prompts and outputs under both conditions.
  * Any inequality tension scores generated by Q104 modules, if available.
  * This allows later inspection and comparison without exposing any deep TU generative rule.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q104 and their direct reuse targets.

### 8.1 Reusable components produced by this problem

1. ComponentName: `InequalityTensionIndex`

   * Type: functional
   * Minimal interface:

     * Inputs: `D_wealth`, `D_income`, `M_mobility`, `C_struct` for a state `m`, plus fixed encoding parameters in `E_ineq`.
     * Output: scalar `DeltaS_ineq_total(m)` and its decomposition into `DeltaS_level(m)`, `DeltaS_mobility(m)`, `DeltaS_consistency(m)`.
   * Preconditions:

     * All descriptors are defined and belong to `M_reg`.
     * Encoding parameters are fixed and constraint compatible.

2. ComponentName: `MobilityRegimeMap`

   * Type: field
   * Minimal interface:

     * Inputs: mobility and stratification indicators for a society and time window.
     * Output: a compact representation of mobility regimes, including regime labels and key parameters.
   * Preconditions:

     * Data quality sufficient to distinguish broad mobility regimes.
     * Mapping rules calibrated once and shared across societies.

3. ComponentName: `ConstraintCompatibleBaselineGenerator`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: constraint vector `C_struct(m)`, norm profile, reference library `L_ref_ineq`.
     * Output: candidate baseline distribution and mobility profiles compatible with constraints and norms.
   * Preconditions:

     * Constraint and norm descriptors are available.
     * Reference library contains episodes spanning similar constraint classes.

### 8.2 Direct reuse targets

1. Q101, equity premium puzzle

   * Reused component: `InequalityTensionIndex`.
   * Why it transfers: Q101 needs information about who bears risk and how wealth is concentrated to frame puzzles about returns; inequality tension provides structured inputs.
   * What changes: Q101 focuses on how high inequality tension interacts with asset pricing and risk premia, rather than on inequality itself.

2. Q105, prediction of systemic crashes

   * Reused component: `InequalityTensionIndex` and `MobilityRegimeMap`.
   * Why it transfers: some crash narratives rely on prolonged high inequality tension and low mobility; these components supply measurable inputs.
   * What changes: Q105 links inequality tension to fragility indicators and crisis probabilities.

3. Q109, global migration patterns

   * Reused component: `MobilityRegimeMap`.
   * Why it transfers: persistent low mobility regimes and inequality gaps across regions are drivers of migration; mobility regimes summarize these conditions.
   * What changes: Q109 extends the mapping to include cross border differentials and migration cost structures.

4. Q121, AI alignment and social impact

   * Reused component: `ConstraintCompatibleBaselineGenerator`.
   * Why it transfers: Q121 needs baselines for fair distributional outcomes under constraints when evaluating AI deployment; this generator supplies them.
   * What changes: constraint vectors are extended to include AI capability and deployment patterns.

---

## 9. TU roadmap and verification levels

### 9.1 Current verification levels

* E_level: E1

  * An effective layer encoding of inequality dynamics has been specified, including:

    * state space `M`,
    * observables `D_wealth`, `D_income`, `M_mobility`, `C_struct`, `R_regime_ineq`,
    * mismatch functionals `DeltaS_level`, `DeltaS_mobility`, `DeltaS_consistency`,
    * inequality tension tensor `T_ij`,
    * singular set `S_sing` and regular domain `M_reg`.

  * Experiments have been specified with explicit falsification conditions for encodings.

* N_level: N2

  * A narrative framing inequality as tension between feasible inclusive configurations and observed distributions under constraints is explicit.
  * Counterfactual worlds, inclusive dynamics and inequality trap, are defined at the level of observables and tension patterns.

These verification level labels are intended to align with the TU charters listed in the footer, which define what E1 and N2 mean for effective layer encodings and narratives.

### 9.2 Next measurable step toward E2

To move from E1 to E2 for Q104, at least one of the following should be carried out and documented.

1. Prototype implementation of `E_ineq` on real data

   * Choose a concrete encoding `e` in `E_ineq` with explicit baselines and weights.
   * Compute `Tension_ineq(m)` for a cross-country panel and publish:

     * definitions of all descriptors and baselines,
     * the resulting tension profiles,
     * basic stability checks under refinement.

2. Stress testing encodings across historical episodes

   * Use the baseline family setup from Experiment 2.
   * Document which baselines are constraint compatible and how `Tension_ineq(m)` behaves across episodes.
   * Identify patterns where high tension is robust to encoding choices.

Both steps operate purely at the effective layer and do not require any exposure of deep TU generative rules.

### 9.3 Long term role in the TU program

In the longer term, Q104 is expected to function as:

* the central node for inequality related tension in socio technical systems,
* a source of reusable components for problems involving:

  * financial stability,
  * migration,
  * climate justice,
  * AI impact and governance,
* a calibration ground for how TU encodings handle:

  * contested social objectives,
  * distributional trade offs under constraints,
  * mixtures of continuous and discrete structures.

---

## 10. Elementary but precise explanation

This section explains Q104 in more accessible terms while staying aligned with the effective layer.

Wealth and income inequality is about how money, assets, and chances in life are spread across people. Some societies end up with a small group owning and earning a lot, while many others struggle. Other societies manage to keep gaps smaller and mobility higher.

There are many reasons people have proposed for why this happens:

* how fast the economy grows,
* how technology changes work,
* how taxes and transfers are designed,
* how strong unions and labor protections are,
* how education and health systems work,
* shocks such as crises and wars.

The problem is that these explanations do not fit together into a single clean picture. In some countries, inequality is high even when the economy is rich and growing. In others, inequality is lower even though they face hard constraints.

In the Tension Universe view, we do not try to write the final story of inequality. Instead, we do something narrower and more controlled.

* We define a way to encode the state of a society:

  * what the wealth and income distributions look like,
  * how easy it is to move up or down across generations,
  * what constraints the society faces,
  * what its institutions look like.

* We define a way to measure inequality tension:

  * we pick a set of baselines for distributions and mobility that are:

    * realistic given the society’s constraints,
    * consistent with what it claims to value,
  * we measure how far the actual distributions and mobility are from these baselines.

If the actual world is close to what is feasible and fair under constraints, then inequality tension is low. If the actual world stays far from any such baseline, even when constraints are mild, then inequality tension is high.

We then imagine two kinds of worlds.

* In an inclusive dynamics world, tension can be kept low once we adjust for real constraints. High inequality episodes are specific and understandable.

* In an inequality trap world, there is always a gap left over. No reasonable way of choosing baselines can make the tension go away, even after we account for constraints and norms.

Q104 is about formalizing this idea at the effective layer.

* It specifies what counts as a state,
* which observables we use,
* how we define tension,
* how we stress test these definitions with data.

It does not tell us which policies to adopt or which society is better. Instead, it gives us a structured language for saying:

* here, inequality looks like a reasonable outcome of hard constraints,
* and here, inequality looks like a puzzle that is not explained by constraints alone.

This language can then be reused in other problems that need to reason about distribution and fairness under limits, from financial stability to climate justice and the social impact of AI.

---

## Tension Universe effective-layer footer

This page is part of the WFGY / Tension Universe S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem in economics or inequality research has been solved.

### Effective-layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores, counterfactual worlds, and AI modules, live at the Tension Universe effective layer.
* No TU axioms, generative rules, or deep field equations are specified or assumed beyond what is needed to define effective layer encodings.
* The tensor `T_ij(m)` is a bookkeeping device for semantic and distributional tension accounting and is not a law of motion.
* Mentions of worlds such as World T and World F describe observable patterns and tension profiles, not metaphysical claims about the universe.

### Encoding and fairness conventions

* All tension indices in this document are defined relative to explicit encoding classes such as `E_ineq`, explicit baselines drawn from reference libraries such as `L_ref_ineq`, and explicit weight choices.
* Encodings that tune baselines or weights separately for each state in order to hide tension are treated as different encodings and fall outside the definition of a fixed `e` in `E_ineq`.
* Changing weights, reference libraries, or baseline selection rules in response to observed outcomes is considered a change of encoding, not a harmless calibration step.
* The experiments in Section 6 are designed so that encodings can be falsified if they become trivial, unstable, or inconsistent with constraints. This is a property of the encoding, not of the world.

### Engineering and AI use

* Components defined here, such as inequality tension indices and mobility regime maps, may be used as training signals, auxiliary heads, or evaluation metrics inside AI systems.
* Using these components does not guarantee fairness, safety, or correctness. It only adds a structured, testable layer of constraint aligned with the TU charters.
* Any deployment that relies on Q104 should log which encoding `e` in `E_ineq` is used, which reference library version is active, and which experiments have been passed, to keep the effective layer behavior auditable.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
