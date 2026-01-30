# Q040 · Black hole information problem

## 0. Header metadata

```txt
ID: Q040
Code: BH_PHYS_QBLACKHOLE_INFO_L3_040
Domain: Physics
Family: Quantum gravity / black hole physics
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Encoded_E1_Open
Semantics: continuous
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this page are made strictly at the effective layer of the Tension Universe (TU) framework.

* We only specify state spaces, observables, invariants, tension scores, counterfactual worlds and engineering modules at the effective layer.
* We do not specify any deep TU generative rules, axiom systems or constructive procedures that would generate these objects from more primitive mathematical structure.
* We do not claim to prove or disprove the canonical black hole information problem stated in Section 1.
* We do not select or endorse any particular microscopic model of quantum gravity as correct. All references to candidate theories are treated as external input.
* All encodings used here belong to an admissible encoding class `E_BH` for Q040. This class is constrained by the TU Encoding and Fairness Charter and by the rules stated in Block 3.
* Any attempt to interpret tension values as direct physical measurements of real black holes lies outside the intended scope of this document.

The three principles that appear in this page, namely unitarity, semiclassical effective field theory outside the horizon and horizon regularity for infalling observers, are treated as effective layer principles inside the encoding. They are not asserted as axioms of TU itself.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The black hole information problem asks whether the formation and complete evaporation of a black hole is compatible with unitary quantum evolution.

In standard semiclassical gravity, Hawking style calculations indicate that:

* A black hole formed from a pure quantum state emits Hawking radiation that is exactly thermal at leading order.
* If the black hole completely evaporates, the outgoing radiation is described by a mixed state.
* The mapping from the initial pure state to the final mixed state is non unitary.

On the other hand, basic quantum theory demands that:

* Isolated systems evolve by unitary transformations.
* Pure states should remain pure under exact time evolution.

The canonical black hole information problem is therefore:

> Can black hole formation and evaporation be described in a way that is exactly compatible with unitary quantum mechanics, while also respecting the usual principles of semiclassical gravity and horizon regularity, or does black hole evaporation fundamentally destroy information?

Different formulations of the paradox emphasize different subsets of assumptions, such as locality, effective field theory outside the horizon and the experience of infalling observers.

### 1.2 Status and difficulty

Key points about the current status:

* Hawking’s original calculation indicates a breakdown of predictability and apparent information loss in black hole evaporation if taken at face value within semiclassical gravity.

* Many candidate resolutions have been proposed, including:

  * information recovery through subtle correlations in Hawking radiation,
  * holographic dualities where black hole evolution is described by a unitary boundary theory,
  * modifications of horizon structure such as firewalls or fuzzballs,
  * nonlocal effects in quantum gravity or other departures from standard locality assumptions.

* No consensus resolution has been achieved that is simultaneously:

  * fully derived from a complete theory of quantum gravity,
  * demonstrably compatible with all known consistency requirements,
  * widely accepted as the definitive answer.

The problem is regarded as central and extremely difficult. It touches:

* the foundations of quantum gravity,
* the meaning of entropy and information in gravitational systems,
* the consistency of semiclassical approximations and coarse grained descriptions.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q040 plays three structural roles:

1. It is the canonical example of a consistency_tension problem where apparently reasonable principles cannot all hold simultaneously at face value.
2. It anchors a family of problems about information, entropy and predictability in extreme gravitational settings, including quantum gravity unification and thermodynamic limits.
3. It provides reusable patterns for:

   * encoding triads of principles as tension functionals,
   * constructing counterfactual worlds where different subsets of principles are taken as fundamental,
   * designing falsifiable tests for effective encodings that stop short of claiming a full resolution.

### References

1. S. W. Hawking, “Particle creation by black holes”, Communications in Mathematical Physics 43 (1975), 199–220.
2. S. W. Hawking, “Breakdown of predictability in gravitational collapse”, Physical Review D 14 (1976), 2460–2473.
3. J. Preskill, “Do black holes destroy information?”, lecture notes and review articles from the early 1990s, widely circulated in the quantum gravity community.
4. D. Harlow, “Jerusalem lectures on black holes and quantum information”, Reviews of Modern Physics 88 (2016), 015002.
5. S. Ryu, T. Takayanagi, “Holographic derivation of entanglement entropy from AdS/CFT”, Physical Review Letters 96 (2006), 181602.

---

## 2. Position in the BlackHole graph

This block records how Q040 sits in the BlackHole graph. Each edge is given as a Q node with a one line reason that points to a concrete component or tension type. When a link is naturally bidirectional, this is stated explicitly rather than treated as an accident.

### 2.1 Upstream problems

These problems provide prerequisites, tools or background frameworks for Q040.

* Q021 (BH_PHYS_QGR_UNIFICATION_L3_021)
  Reason: Supplies candidate quantum gravity frameworks whose effective descriptions feed into the state space and observables used in the black hole information encoding.

* Q032 (BH_PHYS_QTHERMO_FOUNDATIONS_L3_032)
  Reason: Provides tools to model entropy, coarse graining and quantum thermodynamic arrows that Q040 uses to define information related tension. Q040 also feeds back into Q032 as an extreme test case, which creates an intentional bidirectional relation.

* Q033 (BH_PHYS_QGR_MODEL_SELECTION_L3_033)
  Reason: Contributes selection criteria for quantum gravity theories. Q040 specializes those criteria to the requirement of information preservation in black hole evaporation.

### 2.2 Downstream problems

These problems reuse Q040 components or depend on Q040’s tension structure.

* Q050 (BH_COSM_MULTIVERSE_TESTS_L3_050)
  Reason: Reuses information conservation tension patterns to constrain how information flows across cosmological horizons in multiverse scenarios.

* Q032 (BH_PHYS_QTHERMO_FOUNDATIONS_L3_032)
  Reason: Uses Q040’s black hole information tension as an extreme test case for general statements about quantum thermodynamics and irreversibility, closing the bidirectional edge mentioned above.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)
  Reason: Both Q036 and Q040 address strongly coupled quantum many body systems where microscopic unitarity must be reconciled with emergent thermodynamic behavior.

* Q039 (BH_PHYS_QTURBULENCE_L3_039)
  Reason: Both Q039 and Q040 concern complex dynamical fields where coarse grained descriptions appear to lose information unless tension between microstates and macrostates is carefully tracked.

### 2.4 Cross domain edges

Cross domain edges connect Q040 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses black hole information conservation tension components as templates for energy information tradeoffs in ultimate thermodynamic limits.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Adapts the triad of principles in Q040 into triads of safety constraints for long horizon AI systems.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Uses the idea of hidden versus observable information tension in black hole evaporation as a structural analogy for interpretability tension in large AI models.

---

## 3. Tension Universe encoding (effective layer)

All content in this block stays at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden TU generative rules or any mapping from raw microphysical data to internal TU fields.

### 3.1 State space

We assume an effective state space

```txt
M_BH
```

with the following interpretation:

* Each element `m` in `M_BH` represents a coarse grained configuration of:

  * a black hole or a family of black holes,
  * their near horizon region,
  * the outgoing radiation,
  * the relevant environment,
    over a specified time window or set of time windows.

For each state `m`:

* The internal details of the underlying quantum gravity microstates are not represented.
* Instead, `m` carries summarized information about:

  * macroscopic parameters of the black hole such as mass, angular momentum, charge and horizon area,
  * coarse entanglement structure between interior, near horizon and far radiation degrees of freedom,
  * which physical principles are being treated as valid in that configuration, such as unitarity, semiclassical effective field theory outside the horizon or regularity of the horizon for infalling observers.

We do not specify how these summaries are constructed from microscopic models or from observational data. We only assume that for every physically relevant scenario there exist states in `M_BH` that encode the corresponding summaries in a coherent way.

### 3.2 Effective fields and observables

We introduce the following real valued observables on `M_BH` at the effective layer.

1. Black hole entropy observable

```txt
S_BH(m; W) >= 0
```

* Input: a state `m` and a time window `W` during which a black hole exists.
* Output: a coarse grained entropy associated with the black hole in that window, typically proportional to horizon area or an equivalent effective measure.
* Interpretation: an effective Bekenstein Hawking type entropy or a compatible effective entropy in models where area is not the only relevant quantity.

2. Radiation entropy observable

```txt
S_rad(m; W) >= 0
```

* Input: a state `m` and a time window `W` that intersects the evaporation process.
* Output: an entanglement entropy or von Neumann entropy assigned to the outgoing radiation subsystem in that window.
* Interpretation: a coarse grained summary of how much information appears to be carried by the radiation.

3. Unitarity compatibility indicator

```txt
C_unitarity(m) in [0, 1]
```

* Input: a state `m` encoding an evaporation history.
* Output: a scalar that reflects how close the encoded history is to a unitary Page curve compatible evolution.
* Values near `1` indicate high compatibility with unitarity at the level of entropy histories. Values near `0` indicate strong deviation.

4. Semiclassical compatibility indicator

```txt
C_semiclassical(m) in [0, 1]
```

* Input: a state `m` encoding near horizon and exterior field configurations.
* Output: a scalar that reflects how closely the encoded behavior matches expectations from semiclassical effective field theory outside the horizon.
* Values near `1` indicate that semiclassical approximations are trusted in the region and time windows represented in `m`.

5. Horizon regularity indicator

```txt
C_horizon_regular(m) in [0, 1]
```

* Input: a state `m` encoding horizon properties.
* Output: a scalar indicating how well the horizon satisfies regularity or no drama conditions as experienced by infalling observers.
* Values near `1` correspond to a smooth horizon. Values near `0` correspond to large deviations from smoothness.

All of these observables are treated as well defined maps from `M_BH` to real intervals at the effective layer. The details of how they are computed from fundamental degrees of freedom are not specified here.

### 3.3 Mismatch observables

We define three nonnegative mismatch observables that measure how far a state `m` deviates from certain reference patterns.

1. Page curve mismatch

```txt
DeltaInfo_Page(m) >= 0
```

* Input: a state `m` that encodes an evaporation history.
* Output: a scalar that measures the deviation of the encoded radiation entropy history from a fixed reference family of Page curve templates that are consistent with unitary evaporation.
* Interpretation: small values indicate that the history resembles a unitary Page curve. Large values indicate that entropy histories look more like monotonically increasing Hawking style behavior.

The reference Page curves are taken from a fixed, finite library of templates decided in advance. The choice of template for a given scenario is determined by coarse parameters such as total entropy and evaporation time, not by the detailed noise in the observed or simulated entropy history.

2. Semiclassical mismatch

```txt
DeltaInfo_semiclass(m) >= 0
```

* Input: a state `m` encoding near horizon and exterior fields.

* Output: a scalar that measures the deviation between:

  * the encoded coarse grained field behavior in `m`,
  * and a fixed collection of semiclassical predictions for the same regime.

* Interpretation: small values indicate that the encoded state is compatible with semiclassical evolution. Large values indicate breakdowns of semiclassical expectations or uncontrolled corrections.

3. Horizon consistency mismatch

```txt
DeltaInfo_horizon(m) >= 0
```

* Input: a state `m` encoding horizon and entanglement structure.
* Output: a scalar that measures the extent to which horizon regularity, global unitarity and semiclassical behavior can be simultaneously satisfied in the encoded configuration.
* Interpretation: small values indicate that the triad of principles appears mutually compatible at the encoded level. Large values indicate strong tension or apparent contradiction.

### 3.4 Admissible encoding class and fairness constraints

To avoid trivializing the tension functional by post hoc choices, we work with an admissible encoding class.

Let `E_BH` denote the class of admissible encodings for Q040. This class is a member of the TU admissible encoding space described in the TU Encoding and Fairness Charter. Each element of `E_BH` specifies:

* how entropy histories are summarized into inputs for `DeltaInfo_Page`,
* how semiclassical expectations are summarized for `DeltaInfo_semiclass`,
* how combined horizon, unitarity and locality constraints are summarized for `DeltaInfo_horizon`.

We impose the following fairness constraints.

1. Finite template library

   * The reference Page curve templates and semiclassical prediction sets form a finite library decided independently of the detailed noise of any particular data set.
   * For a given physical scenario, the choice of template is determined only by coarse parameters such as total entropy scale and characteristic time scales. It does not depend on detailed features of the measured or simulated curve.

2. Fixed weights and normalization

   * When we combine mismatches into a single tension value, we use weights that obey:

     ```txt
     w_Page > 0, w_semiclass > 0, w_horizon > 0
     w_Page + w_semiclass + w_horizon = 1
     ```

   * These weights are fixed once for all experiments conducted under a given encoding in `E_BH`. They are not adjusted after inspecting the outcomes of particular experiments or toy models.

3. Stability under refinement

   * If encodings are refined by using longer time windows, finer time resolution or more detailed field summaries, the basic library of templates and the weight ranges remain the same.
   * Refinement may change the numerical values of mismatches. It is not allowed to redefine the quantities in a way that erases genuine tension that was already present at coarser levels.

Any encoding that violates these constraints is considered outside `E_BH` and must not be used when defining or interpreting information tension values for Q040.

### 3.5 Effective tension tensor components

Consistent with the TU core decisions, we assume an effective semantic tension tensor `T_ij` on `M_BH` of the form:

```txt
T_ij(m) = S_i(m) * C_j(m) * Tension_BH_Info(m) * lambda(m) * kappa_BH
```

where:

* `S_i(m)` is a source like factor that measures how strongly the ith semantic component in `m` acts as a driver of dynamics or inference.
* `C_j(m)` is a receptivity like factor that measures how sensitive the jth downstream component, for example physical predictions, interpretations or AI modules, is to information tension in `m`.
* `Tension_BH_Info(m)` is the scalar consistency tension functional defined in Block 4.
* `lambda(m)` is a convergence state factor that indicates whether local reasoning around `m` is convergent, recursive, divergent or chaotic within a fixed bounded interval.
* `kappa_BH` is a fixed coupling constant that sets the overall scale of information tension for Q040.

The detailed index sets of `i` and `j` are not needed at the effective layer. It is sufficient that `T_ij(m)` is well defined and finite for all relevant indices and all `m` in the regular domain.

### 3.6 Singular set and domain restrictions

Certain observables may become undefined or unbounded if the encoded configuration is inconsistent or incomplete. We define the singular set:

```txt
S_sing_BH = {
  m in M_BH :
  S_BH(m; W), S_rad(m; W), DeltaInfo_Page(m),
  DeltaInfo_semiclass(m), or DeltaInfo_horizon(m)
  is undefined, not finite, or internally inconsistent
  for some relevant window W
}
```

For Q040 we set:

```txt
S_sing = S_sing_BH
```

and restrict all information tension analysis to the regular domain:

```txt
M_BH_reg = M_BH \ S_sing
```

Whenever an experiment or protocol would require evaluating `Tension_BH_Info(m)` for `m` in `S_sing`, the result is treated as out of domain. Such evaluations must not be used as evidence for or against any candidate resolution of the black hole information problem or for or against any specific microscopic theory.

---

## 4. Tension principle for this problem

This block states how Q040 is encoded as a consistency_tension problem at the effective layer.

### 4.1 Core tension functional

We define an effective information tension functional:

```txt
Tension_BH_Info(m) =
  w_Page      * DeltaInfo_Page(m)
+ w_semiclass * DeltaInfo_semiclass(m)
+ w_horizon   * DeltaInfo_horizon(m)
```

with the weights satisfying the fairness constraints in Block 3:

```txt
w_Page > 0
w_semiclass > 0
w_horizon > 0
w_Page + w_semiclass + w_horizon = 1
```

Properties:

* `Tension_BH_Info(m) >= 0` for all `m` in `M_BH_reg`.
* If all three mismatches are small, `Tension_BH_Info(m)` is small.
* If any mismatch grows large, `Tension_BH_Info(m)` grows accordingly.
* Because the admissible encoding class `E_BH` and weight constraints are fixed in advance, `Tension_BH_Info` cannot be driven to zero for all states by post hoc parameter tuning.

The three principles that feed into these mismatches, namely global unitarity, semiclassical gravity outside the horizon and horizon regularity for infalling observers, are treated as effective layer principles only. TU does not commit to any one of them as an ultimate axiom of reality. Q040 simply encodes how they stand in tension when they are all imposed at the same time in a given description.

### 4.2 Information preservation as a low tension principle

At the effective layer, the black hole information problem can be reformulated as a low tension principle:

> There exist world representing states in `M_BH_reg` whose black hole formation and evaporation histories keep `Tension_BH_Info` in a narrow low tension band across the entire process, while honoring the basic principles of quantum mechanics and semiclassical gravity in their intended regimes.

More concretely, for an admissible encoding in `E_BH` and a physically reasonable family of time windows that cover the evaporation process, we expect that:

```txt
For the actual universe:

There exist states m_true in M_BH_reg such that
Tension_BH_Info(m_true) <= epsilon_BH
```

for some small threshold `epsilon_BH` that:

* depends on the precision of the encoding and available information,
* does not grow without bound as encodings are refined and data quality improves.

In this view, Q040 asks whether the universe admits such globally low tension configurations or whether tension inevitably accumulates beyond any small fixed band as we push towards complete evaporation.

### 4.3 Information loss as persistent high tension

If black hole evaporation really destroys information in a fundamental way, then in any encoding in `E_BH` that remains faithful to the actual behavior we should eventually see persistent high tension.

Formally, this would mean that for any admissible encoding and for any states `m_false` that represent the actual universe at sufficient resolution, there exists a positive constant `delta_BH` such that:

```txt
Tension_BH_Info(m_false) >= delta_BH > 0
```

for some late stage of the evaporation history, and `delta_BH` cannot be reduced arbitrarily by refining the encoding within `E_BH`.

Thus the effective statement of Q040 is:

* In a world with fundamental information loss, information tension can never be kept uniformly small across the full evaporation history without breaking at least one of the encoded principles.
* In a world where information is preserved and the principles are reconciled, there should exist encodings and states where tension remains in a controlled low band as we move to finer descriptions.

This block does not claim that we know which type of world we inhabit. It only states how the two possibilities manifest as different tension patterns inside the TU framework.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds, both staying strictly at the effective layer.

* World T: a world where black hole evolution is effectively unitary and all three principles are reconciled by some consistent mechanism.
* World F: a world where information is truly lost in black hole evaporation and no consistent reconciliation exists.

Both worlds are described using the same admissible encoding class `E_BH`. They differ only in the tension patterns and observable summaries that can be achieved.

### 5.1 World T (unitary black hole world)

Assumptions in World T:

1. Global evolution of black hole formation and evaporation is unitary.
2. There exists at least one quantum gravity framework that realizes this unitarity and matches low energy physics.
3. Semiclassical effective field theory outside the horizon remains valid within its usual domain of applicability, up to controlled corrections.
4. Infalling observers crossing the horizon experience no violent deviations from smooth geometry.

Effective layer consequences:

1. Page curve behavior

   * For world representing states `m_T` in `M_BH_reg`, the radiation entropy history encoded in `S_rad(m_T; W)` follows a Page curve pattern within the resolution of the summaries.
   * `DeltaInfo_Page(m_T)` can be kept small across the entire evaporation history at achievable resolutions.

2. Semiclassical compatibility

   * In regions and times where semiclassical predictions are expected to hold, `DeltaInfo_semiclass(m_T)` is small.
   * Deviations from semiclassical behavior are localized and consistent with the chosen quantum gravity model, rather than arbitrary.

3. Horizon regularity

   * `C_horizon_regular(m_T)` stays close to `1` for relevant states, and `DeltaInfo_horizon(m_T)` remains small once the appropriate resolution and domain are chosen.

4. Global tension pattern

   * For some small `epsilon_BH` and for encodings in `E_BH` that match the underlying physics, we can achieve:

     ```txt
     Tension_BH_Info(m_T) <= epsilon_BH
     ```

     across all time windows covering the evaporation process, within the accuracy of the summaries.

### 5.2 World F (information destroying world)

Assumptions in World F:

1. The effective semiclassical Hawking calculation accurately describes black hole evaporation even at very late times.
2. There is no underlying quantum gravity mechanism that restores unitarity for the global process.
3. The mapping from initial pure states to final radiation states is genuinely non unitary.

Effective layer consequences:

1. Radiation entropy history

   * For world representing states `m_F`, `S_rad(m_F; W)` grows approximately monotonically until evaporation completes and then saturates at a high value.
   * There is no Page curve style decrease, so `DeltaInfo_Page(m_F)` remains large once the black hole has shrunk significantly.

2. Semiclassical compatibility

   * `DeltaInfo_semiclass(m_F)` can remain small, because semiclassical predictions are treated as exact in their domain.
   * This means semiclassical evolution and information loss appear mutually consistent within the narrow gravitational description.

3. Horizon regularity and principle conflict

   * If the horizon remains smooth and semiclassical outside the horizon, but global evolution is non unitary, then any attempt to encode all three principles as simultaneously valid leads to large `DeltaInfo_horizon(m_F)`.
   * Alternatively, if horizon regularity is sacrificed in favor of mechanisms like firewalls or fuzzballs, other forms of tension appear in observables related to infalling observers.

4. Global tension pattern

   * For any admissible encoding in `E_BH` that remains faithful to the above behavior, there exists a positive lower bound `delta_BH` such that:

     ```txt
     Tension_BH_Info(m_F) >= delta_BH
     ```

     for sufficiently late stages. This bound cannot be made arbitrarily small by refining the encoding while keeping the assumed evolution and principle set.

### 5.3 Interpretive note

These two worlds should be read as structured summaries of what low tension and high tension patterns would look like under different global assumptions about information preservation. They do not specify or favor any particular microscopic mechanism, and they do not provide a decision procedure for which world is ours.

Both worlds use the same encoding class `E_BH`. The difference lies in which regions of `M_BH_reg` are judged to correspond to the actual universe and in the tension patterns that arise for those regions.

Their purpose is to:

* make the conflict between principles explicit in terms of well defined observables,
* provide templates for experiments and AI modules that test encodings of the conflict.

---

## 6. Falsifiability and discriminating experiments

This block gives experiments and protocols that:

* test the coherence and usefulness of the Q040 encoding,
* discriminate between unitary style and non unitary style behaviors in toy models or partial theories,
* can falsify specific choices of encoding parameters or template libraries.

These experiments test only encodings in `E_BH`. They do not test the real universe directly and they do not decide whether the actual universe is more like World T or World F. None of these experiments prove or disprove the canonical statement. They only evaluate TU encodings at the effective layer.

### Experiment 1: Page curve tension in toy evaporation models

*Goal*

Evaluate whether the `Tension_BH_Info` functional, under admissible encodings, systematically assigns lower tension to unitary style toy models than to non unitary style toy models of black hole evaporation.

*Setup*

* Construct two families of toy models for evaporation:

  * Family U: toy models where a pure state undergoes evolution via random unitary circuits that reproduce a Page curve style entropy history for a chosen subsystem.
  * Family N: toy models where a pure state evolves via channels that gradually discard information into an inaccessible reservoir, producing monotonic entropy growth without a Page curve.

* For each model instance, we assume that it can be summarized into a state `m` in `M_BH_reg`, with:

  * a coarse grained radiation entropy history,
  * indicators for which principles are intended to hold in that scenario.

*Protocol*

1. Fix an admissible encoding in `E_BH` before inspecting which models belong to Family U or Family N. This includes:

   * a finite library of reference Page curves for the relevant entropy scale and time range,
   * weights `w_Page`, `w_semiclass`, `w_horizon` that satisfy the constraints in Block 3.

2. For each model in Family U:

   * construct the corresponding state `m_U` in `M_BH_reg` without using labels from the family to tune the encoding,
   * compute `DeltaInfo_Page(m_U)`, `DeltaInfo_semiclass(m_U)`, `DeltaInfo_horizon(m_U)` as defined in Block 3,
   * compute `Tension_BH_Info(m_U)`.

3. For each model in Family N:

   * construct the corresponding state `m_N` in `M_BH_reg`,
   * compute the same quantities,
   * compute `Tension_BH_Info(m_N)`.

4. Collect the distributions of `Tension_BH_Info` over Family U and Family N.

*Metrics*

* Mean tension values:

  * `mean_U = average of Tension_BH_Info(m_U)` over Family U.
  * `mean_N = average of Tension_BH_Info(m_N)` over Family N.

* Separation metric:

  * `Delta_mean = mean_N - mean_U`.

* Overlap of distributions, for example the fraction of models where `Tension_BH_Info(m_N) < Tension_BH_Info(m_U)`.

*Falsification conditions*

* If, for all reasonable choices of encodings within `E_BH`, the difference `Delta_mean` is non positive or negligible and the overlap remains large, then the current encoding is considered falsified as a useful information tension measure.
* If there exist encodings within `E_BH` that make Family U appear systematically higher tension than Family N, without any clear mathematical justification for inverting the ordering, those encodings are rejected as misaligned with the intended semantics of Q040.

*Semantics implementation note*

The experiment treats entropy histories and tension values as real valued functions defined on time windows, consistent with the continuous field interpretation of the metadata. Discrete numerical simulations are viewed as approximations to these continuous quantities.

*Boundary note*

Falsifying a TU encoding in this experiment does not solve the canonical black hole information problem. It only shows that a particular choice of templates and weights does not meaningfully distinguish unitary style and non unitary style toy models.

---

### Experiment 2: Holographic Page curve consistency

*Goal*

Test whether the Q040 encoding can assign low information tension to holographic models where Page curve behavior and unitarity are believed to be manifest.

*Setup*

* Consider a class of holographic models where:

  * black hole formation and evaporation can be represented in a dual boundary theory,
  * entanglement entropy of radiation subsystems can be computed or approximated using methods such as the island formula.

* For each such scenario, assume that the holographic data can be summarized into a state `m_holo` in `M_BH_reg`, including:

  * a coarse grained radiation entropy history,
  * indicators for when semiclassical gravity is expected to break down in the bulk,
  * horizon regularity indicators as encoded in the dual description.

*Protocol*

1. Fix an admissible encoding in `E_BH` that includes:

   * a library of reference Page curves suitable for the holographic entropy scales,
   * explicit rules for when semiclassical expectations are trusted in the bulk description.

2. For each holographic scenario:

   * construct the corresponding state `m_holo` in `M_BH_reg` without tuning the encoding individually to each scenario,
   * compute `DeltaInfo_Page(m_holo)`, `DeltaInfo_semiclass(m_holo)`, `DeltaInfo_horizon(m_holo)`,
   * compute `Tension_BH_Info(m_holo)`.

3. Examine how `Tension_BH_Info(m_holo)` behaves as:

   * the complexity of the holographic scenario increases,
   * the resolution or time coverage of the entropy summaries is refined.

*Metrics*

* Maximum tension over the evaporation history for each scenario.
* Distribution of tension values at different stages such as early times, around Page time and late times.
* Sensitivity of tension values to admissible changes within `E_BH`, such as modest adjustments of weights and template choices.

*Falsification conditions*

* If, for all encodings in `E_BH` that are compatible with holographic expectations, `Tension_BH_Info(m_holo)` cannot be kept within a moderate band for any realistic choice of parameters, the encoding is judged incompatible with holographic Page curve behavior and is rejected for Q040.
* If small, justified changes in encoding parameters produce large, unstructured swings in `Tension_BH_Info(m_holo)` that are not tied to any physical transition, the encoding is considered unstable at the effective layer.

*Semantics implementation note*

The experiment treats entropies, tensions and time parameters as continuous real valued quantities, again in line with the continuous field interpretation declared in the metadata. Discrete approximations used in numerical implementations are regarded as approximations to this continuous picture.

*Boundary note*

Agreement or disagreement between tension values and holographic expectations tests the chosen encoding, not the fundamental truth of any specific holographic model or of holography as a whole.

---

## 7. AI and WFGY engineering spec

This block describes how Q040 can be used as a module inside AI systems built with WFGY principles. All descriptions remain at the effective layer and do not reveal any hidden TU generative rules. The modules defined here are engineering constructs that reuse effective layer objects, not parts of TU’s deep mathematical structure.

### 7.1 Training signals

We define several training signals that help AI models represent and reason about black hole information tension.

1. `signal_bh_unitarity_tension`

   * Definition: a scalar signal derived from `Tension_BH_Info(m)` whenever the model’s internal state corresponds to a black hole evaporation scenario.
   * Purpose: penalize internal representations that implicitly combine assumptions about black holes in a way that yields high information tension, while rewarding representations that keep tension in a low band when the context assumes unitarity.

2. `signal_page_curve_shape`

   * Definition: a signal computed from a compact descriptor of the model’s implied entropy history for radiation, compared to fixed Page curve templates.
   * Purpose: encourage the model to recognize and distinguish Page curve style profiles from monotonically growing entropy profiles in qualitative reasoning.

3. `signal_principle_conflict_flag`

   * Definition: a signal that activates when the model’s internal representation suggests that:

     * global unitarity is assumed,
     * semiclassical gravity is assumed to hold everywhere outside the horizon,
     * infalling observers are assumed to see a smooth horizon,

     but no mechanism or tradeoff is acknowledged.

   * Purpose: nudge the model to either:

     * treat one of the assumptions as approximate, or
     * explicitly note the tension instead of silently combining them.

4. `signal_world_T_vs_world_F_consistency`

   * Definition: a signal that measures how consistently the model maintains separate reasoning tracks when prompted under World T versus World F assumptions.
   * Purpose: reduce uncontrolled mixing of assumptions and encourage explicit conditional reasoning.

### 7.2 Architectural patterns

We outline module patterns that reuse Q040 components.

1. `BH_InfoTensionHead`

   * Role: given an internal representation of a physical scenario that involves gravity and quantum information, this head estimates `Tension_BH_Info(m)` and its decomposition.
   * Interface:

     * Inputs: hidden representations associated with a description of black hole formation, evaporation or related processes.
     * Outputs: a scalar `tension_value` and a short vector with approximate contributions from `DeltaInfo_Page`, `DeltaInfo_semiclass` and `DeltaInfo_horizon`.

2. `PrincipleTriadChecker`

   * Role: track which subsets of the triad of principles, namely unitarity, semiclassical validity and horizon regularity, are being assumed in the current reasoning chain.
   * Interface:

     * Inputs: internal tags or embeddings that reflect which principles the model is currently treating as active.
     * Outputs: a discrete or low dimensional flag indicating:

       * which subset of principles is currently assumed,
       * whether this subset is known to be in high tension given the context and the Q040 encoding.

3. `EntropyHistoryEncoder`

   * Role: compress the model’s internal picture of entropy flow in a scenario into a small descriptor usable by `signal_page_curve_shape`.
   * Interface:

     * Inputs: sequences of internal states associated with time steps in an evaporation or analog process.
     * Outputs: a small vector summarizing qualitative features such as growth, saturation and possible decrease.

### 7.3 Evaluation harness

We propose an evaluation harness to measure the impact of these modules.

1. Task selection

   * Build a benchmark of questions involving:

     * conceptual explanations of the black hole information problem,
     * comparisons between different proposed resolutions,
     * analogies between black hole information and information flow in non gravitational systems.

2. Conditions

   * Baseline condition:

     * The model answers questions using generic physics and reasoning abilities, without explicit Q040 based signals or modules.

   * TU enhanced condition:

     * The same model is augmented with `BH_InfoTensionHead`, `PrincipleTriadChecker` and the training signals described above.

3. Metrics

   * Consistency:

     * how often the model gives mutually compatible answers when asked the same question under different phrasings.

   * Explicit recognition of tradeoffs:

     * frequency with which the model mentions that certain combinations of assumptions are in tension rather than silently accepting them.

   * Stability under counterfactual prompts:

     * how well the model distinguishes reasoning under prompts like “assume unitarity and holography” versus prompts like “assume Hawking’s original semiclassical calculation is exact”.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to see the effect of the Q040 encoding.

* Baseline setup

  * Prompt the model:

    * “Explain the black hole information problem and why it is considered a paradox.”

  * Collect the answer and note:

    * whether unitarity, semiclassical gravity and horizon regularity are all mentioned,
    * whether any tension between them is made explicit.

* TU encoded setup

  * Prompt the same model with Q040 modules active:

    * “Explain the black hole information problem using the idea of information tension between unitarity, semiclassical gravity and the regularity of the horizon for infalling observers. Make clear which principles are in conflict.”

  * Collect the answer and any tension scores produced by `BH_InfoTensionHead` or related modules.

* Comparison metric

  * Rate the two answers, baseline and TU enhanced, on:

    * clarity of the roles played by each principle,
    * explicitness of the tradeoffs,
    * internal consistency across follow up questions.

* What to log

  * The exact prompts,
  * full model responses,
  * auxiliary tension estimates and triad flags.

  These logs allow external auditing of how Q040 shaped the reasoning, without exposing any hidden TU generative rules. Users should be explicitly told that information tension is a diagnostic score inside the encoding, not a direct measurement of any real black hole.

---

## 8. Cross problem transfer template

This block records reusable components produced by Q040 and their direct reuse targets.

### 8.1 Reusable components produced by this problem

1. ComponentName: `InfoConservationTension_BH`

   * Type: functional

   * Minimal interface:

     * Inputs:

       * `entropy_history`: coarse summaries of black hole and radiation entropy over time windows,
       * `principle_flags`: indicators for which principles are assumed to hold in the scenario.

     * Output:

       * `tension_value`: a nonnegative scalar equal to `Tension_BH_Info(m)` in Q040.

   * Preconditions:

     * The inputs must be coherent summaries of a single evaporation style process.
     * The principle flags must be interpretable in terms of unitarity, semiclassical validity and horizon regularity.

2. ComponentName: `PageCurveShape_Descriptor`

   * Type: observable or descriptor

   * Minimal interface:

     * Inputs:

       * `entropy_history`: a sequence or coarse summary of subsystem entropy over a process.

     * Output:

       * `shape_features`: a compact descriptor that captures qualitative features such as:

         * monotonic growth versus growth and decrease,
         * presence of a peak near a characteristic time,
         * relative height and width of that peak.

   * Preconditions:

     * The entropy history must be defined over a well ordered set of time windows with consistent normalization.

3. ComponentName: `PrincipleTriad_StateFlag`

   * Type: field

   * Minimal interface:

     * Inputs:

       * `context_assumptions`: a representation of which physical or logical principles are assumed in the current reasoning context.

     * Output:

       * `triad_flag`: a structured flag indicating:

         * which subset of the triad {unitarity, semiclassical validity, horizon regularity} is currently active,
         * whether that subset is known to be in high potential tension according to Q040.

   * Preconditions:

     * The context assumptions must be parseable into the triad vocabulary.

### 8.2 Direct reuse targets

1. Q021 (Quantum gravity unification)

   * Reused component:

     * `InfoConservationTension_BH`

   * Why it transfers:

     * Candidate quantum gravity theories must provide evaporation scenarios. Q021 can use `InfoConservationTension_BH` to quantify how well each candidate reconciles information conservation with gravitational dynamics.

   * What changes:

     * The entropy histories and principle flags are derived from specific candidate theories rather than from general effective considerations.

2. Q032 (Quantum foundations of thermodynamics)

   * Reused components:

     * `PageCurveShape_Descriptor`,
     * `InfoConservationTension_BH`

   * Why it transfers:

     * Q032 studies how quantum thermodynamic arrows emerge in complex systems. Black hole evaporation in Q040 provides an extreme regime for testing whether thermodynamic arrows can coexist with microscopic unitarity.

   * What changes:

     * Entropy histories may include additional subsystems, but the same descriptors and tension metrics can be applied.

3. Q059 (Ultimate thermodynamic cost of information processing)

   * Reused component:

     * `InfoConservationTension_BH`

   * Why it transfers:

     * Q059 examines limits on information processing under energetic and thermodynamic constraints. Q040’s treatment of information tension in black holes offers a template for quantifying information preservation under extreme conditions.

   * What changes:

     * The physical system is not necessarily a black hole, but the notion of information conservation tension remains applicable.

4. Q121 (AI alignment problem)

   * Reused component:

     * `PrincipleTriad_StateFlag`

   * Why it transfers:

     * In AI alignment, one often faces triads of constraints such as performance, safety and autonomy that may not be simultaneously satisfiable. The triad flag pattern from Q040 can be repurposed to track which subsets of alignment constraints are being assumed at once.

   * What changes:

     * The triad elements become AI specific principles rather than physical ones, while the tension concept remains.

---

## 9. TU roadmap and verification levels

This block explains how Q040 fits into the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective layer encoding of the black hole information problem has been given.
  * State space, observables, mismatch measures and a scalar tension functional are clearly defined.
  * At least two discriminating experiments are specified, with explicit falsification conditions for encodings in `E_BH`.

* N_level: N1

  * The narrative clearly identifies:

    * the three main principles,
    * their roles in the paradox,
    * how they map to observables and tension measures.

  * Counterfactual World T and World F are described at the effective layer as distinct tension patterns.

### 9.2 Next measurable step toward E2

To advance Q040 from E1 to E2, at least one of the following concrete implementations should be completed.

1. Toy model implementation

   * Build explicit random circuit and non unitary channel toy models as in Experiment 1.

   * Implement a software module that:

     * summarizes those models into entropy histories and principle flags,
     * computes `DeltaInfo_Page`, `DeltaInfo_semiclass`, `DeltaInfo_horizon`,
     * outputs `Tension_BH_Info` for each model.

   * Publish the resulting tension distributions for Family U and Family N as open data, along with the chosen encoding parameters.

2. Holographic case study

   * Select one or more holographic scenarios where Page curves have been computed.
   * Implement a pipeline that summarizes these scenarios into states in `M_BH_reg`.
   * Compute tension values as in Experiment 2 and release the results along with a clear description of the encoding.

Both steps remain at the effective layer, since they operate on entropy summaries and principle indicators without exposing any deeper TU generative rules.

### 9.3 Long term role in the TU program

In the long term, Q040 is expected to serve as:

* A reference node for consistency_tension problems where multiple fundamental principles interact.

* A template for encoding paradoxes in other areas, such as:

  * cosmology, including horizon information and multiverse measures,
  * condensed matter, including emergent irreversibility in strongly coupled systems,
  * AI alignment, including tradeoffs among alignment constraints.

* A calibration ground for:

  * assessing whether TU style encodings genuinely sharpen paradoxes,
  * or whether they merely relabel them without adding measurable structure.

As the program progresses, Q040 can be revisited with:

* more detailed admissible encoding libraries,
* additional experiments that include partial astrophysical data,
* tighter connections to quantum gravity proposals that survive separate scrutiny in Q021 and Q033.

---

## 10. Elementary but precise explanation

The classical version of the black hole information problem can be stated in simple terms.

* Quantum mechanics says that if you know the exact state of a system, and the system is isolated, then its evolution is reversible and preserves information.
* Calculations in semiclassical gravity say that black holes radiate like hot objects and eventually evaporate, with radiation that looks purely thermal.
* If you throw something into a black hole and wait long enough, the outgoing radiation seems to forget what you put in.

So the question is:

> Does the universe really throw away information when black holes evaporate, or is there some deeper description where everything is still reversible?

In the Tension Universe view, we do not try to guess the final answer. Instead, we focus on how to describe the conflict in a structured way.

We treat each possible description of a black hole and its radiation as a state. For each state we ask:

* How does the entropy of the black hole and the radiation change over time?
* Does this look like a Page curve, where entropy first goes up and then comes back down, as expected in a unitary evolution?
* Or does entropy just keep increasing until the black hole disappears, like in Hawking’s original picture?
* Are we assuming that quantum mechanics is exactly unitary?
* Are we assuming that ordinary semiclassical gravity works outside the horizon?
* Are we assuming that nothing special happens when you fall through the horizon?

From these ingredients we build a single number, the information tension, that:

* is small when the story about the black hole is compatible with all the assumptions,
* is large when the story forces those assumptions into conflict.

Then we imagine two kinds of worlds.

* In one kind of world, black holes preserve information. In that world we expect to find descriptions where information tension stays small across the whole life of the black hole.
* In the other kind of world, black holes really destroy information. In that world, any honest description that keeps the usual assumptions will eventually show high information tension.

This does not tell us which world is real and it does not provide a proof. What it does provide is:

* a clear dictionary between principles, such as unitarity, semiclassical gravity and horizon regularity, and observables, such as entropy histories and correlation patterns,
* a way to test whether a proposed encoding or toy model is at least internally consistent,
* reusable tools for other problems where important principles seem to clash.

Q040 is therefore the place where the black hole information problem is rewritten as a question about measurable information tension, rather than as a purely verbal paradox.

---

## Tension Universe effective-layer footer

This page is part of the WFGY / Tension Universe S-problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the named problem.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here, including state spaces `M`, observables, invariants, tension scores and counterfactual worlds, live at the effective layer of the Tension Universe program.
* No deep TU generative rules, axiom systems or construction procedures are exposed in this document.
* Any mapping from raw physical data or microphysical models into the effective objects is left implicit and can vary between admissible encodings inside the same encoding class.

### Encoding and fairness

* The encoding class `E_BH` used in this page is a member of the TU admissible encoding space described in the TU Encoding and Fairness Charter.
* All template libraries, weight choices and refinement rules are fixed before experiments are evaluated and are shared across comparable scenarios.
* Encodings that violate these constraints are outside `E_BH` and must not be used when reporting or interpreting tension values for Q040.

### Tension scale

* Information tension values such as `Tension_BH_Info(m)` are dimensionless diagnostics that quantify how strongly the encoded configuration strains the selected principles.
* These values are not direct physical observables and do not measure any real gravitational field or device output.
* Comparisons of tension values are meaningful only within a fixed encoding class and a fixed choice of scale parameter for this problem.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
