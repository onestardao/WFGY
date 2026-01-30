# Q096 · Earthquake predictability

## 0. Header metadata

```txt
ID: Q096
Code: BH_EARTH_QUAKE_FORECAST_L3_096
Domain: Earth system and climate
Family: Solid Earth and seismology
Rank: S
Projection_dominance: P
Field_type: solid_earth_field
Tension_type: predictability_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Encoding_key: TU_BH_Q096_EQ_v1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

More precisely:

* The purpose of this page is to specify one effective layer encoding of the earthquake predictability problem, labelled by the encoding key `TU_BH_Q096_EQ_v1`.
* This encoding is treated as a single element
  `e* in A_enc(Q096)`
  where `A_enc(Q096)` is a finite family of admissible effective encodings defined in Section 3.6.
* All objects introduced in this document live at the effective layer. This includes:

  * state spaces and domains such as `M_quake` and `M_reg`,
  * observables such as forecast rate fields, count distributions, scoring summaries, mismatch scalars, and tension functionals,
  * invariants and envelopes such as `DeltaS_pred`, `Tension_EQ`, `E_pred`, and `I_contrast`,
  * counterfactual worlds (World T and World F),
  * engineering components, training signals, and transfer templates.

The following are explicitly out of scope for this page:

* We do not specify any TU core axiom system or deep generative rule.
* We do not define any explicit mapping from raw seismic catalogs, geodetic data, or physical simulations into TU internal fields. We only assume that for the purposes of this encoding there exist coherent effective states that summarise such data.
* We do not claim to prove or disprove the canonical scientific statement about earthquake predictability described in Section 1.
* We do not introduce any new theorem in seismology, statistics, or TU mathematics beyond what is already established in the cited literature.

The header field `Semantics: hybrid` means that:

* underlying physical quantities such as stress, strain, and seismic waves are regarded as continuous fields in space and time, but
* the observables used in this encoding are discrete summaries over region horizon pairs, such as event counts, forecast distributions, and scores.

Throughout this page:

* all uses of model libraries, scoring rules, benchmark gains, and threshold parameters are understood to be those attached to the specific encoding element `e*` selected by `Encoding_key`, as made explicit in Section 3.6,
* all experiments and tension analyses are restricted to the regular domain `M_reg` defined in Section 3.5,
* no statement here should be cited as evidence that earthquakes are deterministically predictable, nor as a guarantee about operational forecast performance.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical question of earthquake predictability can be stated in an effective form as follows:

> To what extent, and on what spatial and temporal scales, can the future occurrence of damaging earthquakes be forecast in a way that is
>
> * statistically reliable,
> * physically interpretable,
> * and useful for risk reduction decisions,
>
> beyond what is achievable by time independent or trivial reference models?

Here, “forecast” is interpreted in the modern seismological sense:

* as a probabilistic statement about the number, locations, magnitudes, and times of earthquakes over specified windows,
* not as a deterministic prediction of a single event with exact time, place, and magnitude.

The problem decomposes into several tightly coupled questions:

1. Whether strong short term predictability exists on scales of hours to days beyond aftershock clustering and simple empirical rules.
2. How much medium term predictability on scales of months to years can be extracted from seismicity patterns, stress transfer, and fault system models.
3. How to integrate long term geological and geodetic information into multi decade hazard fields.
4. How to test claims of predictability in a prospective and reproducible way.

Within the BlackHole project, Q096 focuses on the fundamental limits and structures of predictability, not on any single algorithm or operational system.

### 1.2 Status and difficulty

The current scientific consensus distinguishes sharply between:

* Deterministic prediction
  Statements of the form “There will be a magnitude 7.5 earthquake within 10 km of this city at a given clock time tomorrow.” Major geological surveys and seismological societies repeatedly state that such predictions are not currently possible and may be fundamentally unattainable with present knowledge and data.

* Probabilistic forecasting
  Time dependent and location dependent probabilities of earthquake occurrence, evaluated over finite windows. This includes long term hazard maps, short term clustering models, and operational earthquake forecasting (OEF) frameworks.

Operational practice is organised around the second notion. In particular:

* National agencies emphasise that earthquakes cannot be predicted in a deterministic sense, while at the same time they treat probabilistic assessments and hazard maps as essential tools for risk management.
* Research programs such as the Collaboratory for the Study of Earthquake Predictability (CSEP) have established global experiments to test earthquake forecast models prospectively with standardised metrics.
* The field of OEF has developed guidelines for how time dependent seismicity models should be evaluated and, when appropriate, communicated for civil protection.

The deep difficulty of Q096 arises from the combination of:

* strong heterogeneity and complexity of fault systems,
* limited observational windows in both space and time,
* strong clustering and heavy tail behaviour of seismic sequences,
* and substantial societal pressure for simple yes or no answers that the physics does not obviously support.

There is no consensus answer to the core question “how predictable are earthquakes, in principle.” The field remains active, with ongoing work on physical models, statistical models, and testing frameworks.

### 1.3 Role in the BlackHole project

Within the BlackHole S collection, Q096 serves as

1. The flagship predictability_tension node for geohazards. It encodes how far the real Earth lies between “essentially unpredictable” and “moderately to strongly predictable” regimes for earthquakes.

2. A template for multi scale hazard fields that couple

   * short term aftershock and swarm dynamics,
   * medium term regional seismicity rates,
   * and long term tectonic loading and fault structures.

3. A bridge from fundamental geophysics to societal decision making, because the value of any predictability is only realised through changes in building codes, response plans, and real time actions.

4. A reference point for other hazard predictability problems that reuse its components, such as hurricanes, compound extremes, wildfires, and space weather.

### References

1. United States Geological Survey (USGS), “Can you predict earthquakes?”, Earthquake Hazards Program, official public FAQ, accessed 2026.
2. T. H. Jordan, “Earthquake predictability, brick by brick”, Seismological Research Letters, 77(1):3 to 6, 2006.
3. G. M. Marzocchi and T. H. Jordan, “Operational Earthquake Forecasting: State of knowledge and guidelines for utilization”, Annals of Geophysics, 54(4):315 to 342, 2011.
4. D. Schorlemmer et al., “The Collaboratory for the Study of Earthquake Predictability (CSEP): A global earthquake predictability experiment”, Seismological Research Letters, 81(5):861 to 867, 2010.

---

## 2. Position in the BlackHole graph

This block records how Q096 sits inside the BlackHole graph among Q001 to Q125. Each edge is listed with a one line reason that points to a concrete component or tension type at the effective layer.

### 2.1 Upstream problems

These nodes provide prerequisites or general frameworks that Q096 relies on at the effective layer.

* Q091 (BH_EARTH_MULTI_HAZARD_FIELD_L3_091)
  Reason: supplies the general multi hazard field formalism that Q096 specialises to seismic hazard fields.

* Q092 (BH_EARTH_TAIL_RISK_CASCADES_L3_092)
  Reason: provides tools for modelling heavy tails and cascading risk that are essential for clustered seismicity and aftershock sequences.

* Q093 (BH_EARTH_TIPPING_POINTS_CEE_L3_093)
  Reason: contributes general methods for dealing with non linear transitions and regime shifts, relevant for changes in fault system state.

### 2.2 Downstream problems

Downstream nodes reuse components or depend directly on Q096 predictability structures.

* Q095 (BH_EARTH_BIODIVERSITY_L3_095)
  Reason: uses Q096 multi scale hazard descriptors as one class of physical stress inputs that interact with biodiversity tension and recovery windows.

* Q097 (BH_EARTH_GIGAFIRE_REGIME_L3_097)
  Reason: reuses predictability_tension structures for large wildfires by analogy with clustered and heavy tail behaviour under limited forecast skill.

* Q099 (BH_SPACE_SPACE_WEATHER_CASCADE_L3_099)
  Reason: adapts the predictability_tension envelope to space weather events using Q096 as a calibration reference for rare and high impact phenomena.

### 2.3 Parallel problems

Parallel nodes share similar tension types but do not directly reuse specific components.

* Q094 (BH_EARTH_HURRICANE_PATTERN_L3_094)
  Reason: both Q096 and Q094 address hazard fields where limited predictability and societal demand for forecasts create strong predictability_tension.

* Q098 (BH_EARTH_GRAVITY_WAVE_COUPLING_L3_098)
  Reason: both treat wave like phenomena where partial and scale dependent predictability must be encoded under severe observational limits.

### 2.4 Cross domain edges

Cross domain edges connect Q096 to nodes in other domains that reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: reuses Q096 predictability envelope constructs for evaluating forecast models and scoring rules in information theoretic terms.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: uses earthquake predictability as a case study for interpreting how AI models represent hazard, uncertainty, and heavy tail events in internal states.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observable fields and invariants,
* tension scores,
* singular sets and domain restrictions,
* the admissible encoding family `A_enc(Q096)` selecting which parameter sets are allowed.

We do not describe any hidden generative rule or any mapping from raw data to internal TU fields.

### 3.1 State space

We assume a state space

```txt
M_quake
```

where each state `m` in `M_quake` represents a coherent seismic regime configuration over a specified region and time horizon.

At the effective layer, a state encodes:

* summaries of past seismicity such as event counts, locations, magnitudes, and clustering indicators,
* current time varying estimates of stress and strain at a coarse level,
* a set of candidate forecast models and their parameters, restricted to a finite library,
* coarse descriptors of exposure or risk relevant zones.

We do not specify how these summaries are computed from catalogs, geodetic measurements, or physical simulations. We only require that:

* for each region `R` and time horizon `H` in a fixed library of region horizon pairs, there exist states in `M_quake` that encode

  * a forecast distribution of earthquake numbers and magnitudes, and
  * matching observable summaries of actual or simulated seismicity.

### 3.2 Forecast and observation observables

Given the encoding element `e* in A_enc(Q096)` selected by the header `Encoding_key`, we introduce the following observables on `M_quake`.

1. Forecast rate field

```txt
lambda_fore(m; R, H, M_min)
```

* Input: state `m`, region `R`, time horizon `H`, minimum magnitude `M_min`.
* Output: a nonnegative scalar representing the forecast average rate of earthquakes with magnitude at least `M_min` in region `R` over horizon `H`, for the forecast bundle associated with `e*`.

2. Forecast count distribution

```txt
P_fore(m; R, H, M_min; k)
```

* Input: state `m`, region `R`, horizon `H`, minimum magnitude `M_min`, integer `k >= 0`.
* Output: the forecast probability of observing exactly `k` such events in that space time window.

For each fixed `(m, R, H, M_min)` the function of `k` is a discrete distribution that sums to 1.

3. Observed count summary

```txt
N_obs(m; R, H, M_min)
```

* Input: state `m`, region `R`, horizon `H`, minimum magnitude `M_min`.
* Output: an integer count summarising the number of events actually realised in the corresponding window, as encoded in `m`.

4. Scoring rule library

We assume a finite library of proper scoring rules for count forecasts associated with `e*`:

```txt
L_eq_score(e*) = { S_1, S_2, ..., S_K }
```

Each `S_j` is a function that takes a forecast distribution and an observed count and returns a real valued score

```txt
S_j( P_fore(m; R, H, M_min; ·), N_obs(m; R, H, M_min) )
```

The library `L_eq_score(e*)` is fixed in advance and does not depend on the particular state or dataset. It includes at least one strictly proper scoring rule.

5. Model library

We assume a finite library of seismicity forecast models attached to `e*`:

```txt
L_eq_model(e*) = { M_1, M_2, ..., M_L }
```

For each model `M_l` and each region horizon pair, there is a corresponding forecast encoded within `m`. The library is fixed before any evaluation and cannot be tuned on an event by event basis.

### 3.3 Predictability mismatch observables

Using the scoring and model libraries for the chosen encoding `e*`, we define several mismatch observables.

1. Model performance observable

```txt
Perf(m; M_l, S_j; e*) = average_score over a test set
```

For each model `M_l` and scoring rule `S_j`, `Perf(m; M_l, S_j; e*)` summarises the performance of `M_l` over a fixed prospective or retrospective test set encoded in `m`.

2. Best known performance

```txt
Perf_best(m; S_j; e*) = max over l in {1,...,L} Perf(m; M_l, S_j; e*)
```

3. Reference or trivial performance

We define a simple reference model `M_ref(e*)` such as a time independent Poisson model with spatial smoothing. Its performance is

```txt
Perf_ref(m; S_j; e*)
```

4. Predictability gain observable

```txt
Gain(m; S_j; e*) = Perf_best(m; S_j; e*) - Perf_ref(m; S_j; e*)
```

This measures how much better the best model in the library performs, relative to the trivial reference, under scoring rule `S_j`.

5. Predictability mismatch scalar

The encoding element `e*` also specifies benchmark gains

```txt
Target_gain_j(e*)  for j = 1,...,K
```

based on historical experiments. These benchmarks are chosen in advance and are not tuned per dataset.

We define an effective nonnegative mismatch observable

```txt
DeltaS_pred(m; e*) = max over j in {1,...,K} G_j(m; e*)
```

where each component `G_j(m; e*)` is constructed as

```txt
G_j(m; e*) = max( 0, Target_gain_j(e*) - Gain(m; S_j; e*) )
```

Properties:

* `DeltaS_pred(m; e*) >= 0` for all `m`,
* `DeltaS_pred(m; e*) = 0` if for all scoring rules the best model meets or exceeds the target gains.

For notational convenience, later sections often write `DeltaS_pred(m)` with the understanding that this means `DeltaS_pred(m; e*)` for the fixed encoding selected by `Encoding_key`.

### 3.4 Tension components and invariants

The encoding element `e*` specifies a positive scale factor `alpha(e*) > 0`. We define an effective predictability tension scalar

```txt
Tension_EQ(m; e*) = alpha(e*) * DeltaS_pred(m; e*)
```

To align with TU notation, we also define a derived scalar

```txt
DeltaS_eq(m) = Tension_EQ(m; e*)
```

which is the default predictability_tension score for Q096 in this encoding.

For completeness, we embed this scalar into a TU style tension tensor over `M_quake`:

```txt
T_ij(m; e*) = S_i(m) * C_j(m) * Tension_EQ(m; e*) * lambda_state(m) * kappa_eq(e*)
```

where:

* `S_i(m)` is an effective source weight that represents the intensity of the i th hazard source component such as tectonic loading or catalog completeness. These weights are dimensionless and bounded.
* `C_j(m)` is an effective coupling weight that represents the sensitivity of the j th downstream component such as civil protection decisions or infrastructure planning. These weights are also dimensionless and bounded.
* `lambda_state(m)` is a bounded scalar in a fixed interval that encodes the local reasoning regime for this state such as convergent, recursive, divergent, or chaotic. The details of this classification remain at the effective layer.
* `kappa_eq(e*)` is a coupling constant associated with the encoding element `e*` that fixes the overall scale of predictability_tension in the tensor representation.

From this tensor we extract invariants such as

1. Multi scale predictability envelope

```txt
E_pred(m; e*) = vector of Gains and DeltaS_pred across region-horizon families
```

2. Predictability contrast invariant

```txt
I_contrast(m; e*) = difference between best and worst model gains
```

which measures structural diversity in the model library.

When no confusion arises, we again write `Tension_EQ(m)`, `E_pred(m)`, and `I_contrast(m)` with the understanding that they refer to the chosen encoding `e*`.

### 3.5 Singular set and domain restrictions

Some states may be unfit for meaningful predictability analysis at the effective layer. Examples include:

* catalogs with severe gaps or mis located events,
* forecast libraries that collapse to trivial or ill defined distributions,
* scoring evaluations based on too few events,
* states where benchmark gains cannot be estimated coherently.

We collect such states in a singular set

```txt
S_sing = { m in M_quake :
           DeltaS_pred(m; e*) is undefined, or
           some Perf(m; M_l, S_j; e*) is undefined over the required test set, or
           basic count or rate observables are not finite }
```

We then define the regular domain

```txt
M_reg = M_quake \ S_sing
```

All Q096 related tension analysis and all experiments in Section 6 are restricted to `m in M_reg`. When an experiment attempts to evaluate `DeltaS_pred(m; e*)` for `m in S_sing`, the state is treated as out of domain and does not count as evidence for or against any predictability hypothesis.

### 3.6 Admissible encoding class A_enc(Q096)

We now state the admissible encoding class more explicitly.

* `A_enc(Q096)` is a finite set of encoding elements

  ```txt
  A_enc(Q096) = { e_1, e_2, ..., e_Lenc }
  ```

  where each `e_r` packages a coherent choice of effective layer ingredients for Q096.

For each encoding element `e in A_enc(Q096)` we associate:

* a finite seismic forecast model library `L_eq_model(e)`,
* a finite scoring rule library `L_eq_score(e)` for count forecasts,
* benchmark gains `Target_gain_j(e)` for each scoring rule,
* a positive scale factor `alpha(e)`,
* predictability thresholds `epsilon_EQ(e)` and `delta_EQ(e)` used in the low and high tension principles,
* a library of region horizon pairs and magnitude thresholds for which the encoding is intended to apply,
* a coupling constant `kappa_eq(e)` for the tensor representation.

The header field

```txt
Encoding_key: TU_BH_Q096_EQ_v1
```

selects one distinguished encoding element

```txt
e* in A_enc(Q096)
```

and all quantities in this document that depend on model libraries, scoring rules, benchmark gains, scale factors, or thresholds are understood to be computed relative to `e*`.

In particular:

* `L_eq_model`, `L_eq_score`, `Target_gain_j`, `alpha`, `epsilon_EQ`, `delta_EQ`, and `kappa_eq` without explicit `e` argument always mean `L_eq_model(e*)`, `L_eq_score(e*)`, and so on,
* all experiments in Section 6 refer to the encoding element `e*`,
* falsification statements in Section 6 concern the adequacy of `e*` as an effective layer encoding for Q096 under the specified tests, not the existence of other encodings in `A_enc(Q096)` and not the underlying physics of earthquakes.

---

## 4. Tension principle for this problem

### 4.1 Core tension statement

At the effective layer, Q096 is encoded as a statement about the predictability_tension scalar

```txt
Tension_EQ(m; e*) = alpha(e*) * DeltaS_pred(m; e*)
```

for world representing states `m` in the regular domain `M_reg`.

Intuitively:

* If the real Earth is strongly predictable at the tested scales, then there should exist encodings and model libraries in `A_enc(Q096)` such that the corresponding `DeltaS_pred(m; e)` is small and remains small as test sets are extended.
* If the Earth is only weakly predictable or nearly unpredictable at those scales, then even the best model libraries in `A_enc(Q096)` will leave `DeltaS_pred(m; e)` significantly larger than zero across large parts of the region horizon space, under reasonable constraints on library size and evaluation protocols.

The present page considers one such encoding element `e*` and treats its tension scalar as the default

```txt
DeltaS_eq(m) = Tension_EQ(m; e*)
```

for Q096.

### 4.2 Low tension principle (predictable world)

The encoding element `e*` specifies a nonnegative threshold `epsilon_EQ(e*)`. We define a low tension principle:

> In a predictability friendly world, there exist encodings of seismic regime states and forecast libraries such that for a wide range of operationally relevant region horizon pairs
>
> * the best models consistently achieve target gains over trivial references,
> * these gains remain stable or improve as tests are extended,
> * and the overall predictability mismatch `DeltaS_pred(m; e*)` stays within a narrow band across those scales.

Formally, for world representing states `m_T in M_reg` that approximate this scenario we expect

```txt
DeltaS_pred(m_T; e*) <= epsilon_EQ(e*)
```

for a threshold `epsilon_EQ(e*)` that does not grow without bound as more data are collected or as tests are repeated within the domain of the encoding.

### 4.3 High tension principle (weakly predictable world)

The encoding element `e*` also specifies a positive lower bound `delta_EQ(e*)`. We define a complementary high tension scenario:

> In a weakly predictable world, no matter how the forecast library and scoring rules are refined within the constraints that define `A_enc(Q096)`, there remains a strictly positive gap between achievable performance and target gains.

Formally, for world representing states `m_F in M_reg` that approximate this scenario we expect

```txt
DeltaS_pred(m_F; e*) >= delta_EQ(e*)
```

for some `delta_EQ(e*) > 0` that cannot be driven arbitrarily close to zero without violating constraints such as

* finite and pre specified model and score libraries,
* prospective evaluation protocols,
* stable benchmark definitions that are not tuned after seeing the test outcomes.

Under this principle, Q096 asks whether for the actual Earth at the scales and regions of interest:

* there exist encoding elements `e` for which the low tension regime is a good description,
* the high tension regime is unavoidable,
* or the boundary between these regimes can be sharply characterised in terms of observables and invariants at the effective layer.

---

## 5. Counterfactual tension worlds

We outline two counterfactual worlds described only through observables, invariants, and the encoding element `e*`. These are scenario classes, not claims about the actual Earth.

### 5.1 World T (moderate to strong predictability)

In World T:

1. Forecast libraries contain models that consistently outperform trivial references over a broad range of regions and horizons.

2. For the encoding `e*`, the gain observable satisfies

   ```txt
   Gain(m_T; S_j; e*) >= Target_gain_j(e*) - small_margin_j
   ```

   for each scoring rule in the library and for most operational contexts, where the margins `small_margin_j` are small compared to the corresponding benchmarks.

3. The mismatch scalar satisfies

   ```txt
   DeltaS_pred(m_T; e*) <= epsilon_EQ(e*)
   ```

   and does not grow significantly as test windows are extended, except within a controlled fluctuation band.

4. New data tend to confirm the earlier view of moderate to strong predictability. Recalibrations refine models but do not erase their comparative advantage over trivial references.

### 5.2 World F (persistent weak predictability)

In World F:

1. No model in the library can maintain a significant performance advantage over the trivial reference model across extended tests.

2. For many scoring rules and contexts, the gain observable satisfies

   ```txt
   Gain(m_F; S_j; e*) <= Target_gain_j(e*) - gap_j
   ```

   for some strictly positive gaps `gap_j`.

3. The mismatch scalar satisfies

   ```txt
   DeltaS_pred(m_F; e*) >= delta_EQ(e*)
   ```

   and remains above this level even after library revision and recalibration, as long as revisions stay within the admissible class `A_enc(Q096)`.

4. Attempts to construct more complex models often lead to overfitting. Performance gains in one time window are lost or reversed in future windows.

### 5.3 Interpretive note

World T and World F do not assert anything about the deep physics of faults or stress. They only describe how the observable performance of coherent forecast libraries associated with elements of `A_enc(Q096)` would behave in the long run.

Q096 uses these worlds as reference frames for stating what it would mean for earthquake predictability to be structurally present or structurally absent at the tested scales. The existence or non existence of such worlds in reality is an empirical question that lies beyond the scope of this effective layer encoding.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can

* test whether the selected encoding element `e*` is coherent and useful at the effective layer,
* distinguish between different parameter choices for `Tension_EQ`,
* reveal encodings that fail to align with empirical earthquake forecast performance.

These experiments do not solve the canonical problem in Section 1. They only evaluate the chosen effective layer encoding.

Unless otherwise stated, all states are restricted to the regular domain `M_reg`.

### Experiment 1: Prospective CSEP style test as a TU encoding probe

**Goal**
Evaluate whether the Q096 predictability_tension encoding associated with `e*` aligns with the actual performance of earthquake forecast models in prospective testing.

**Setup**

* Select one or more CSEP style regions such as California or Italy, with predefined spatial grids, magnitude thresholds, and time windows.
* Fix the model library `L_eq_model(e*)` including both simple and advanced models.
* Fix the scoring library `L_eq_score(e*)` that includes at least one strictly proper scoring rule for count forecasts.
* Fix benchmark gains `Target_gain_j(e*)` and thresholds `epsilon_EQ(e*)` and `delta_EQ(e*)` before looking at the test outcomes.

**Protocol**

1. For each test window, submit forecasts from all models in `L_eq_model(e*)` according to the specified format.
2. After the window closes, record observed counts, construct a state `m in M_reg` encoding the forecasts and outcomes, and compute scores `Perf(m; M_l, S_j; e*)` for each model and rule.
3. For that state, update `Gain(m; S_j; e*)`, `DeltaS_pred(m; e*)`, and the predictability envelope `E_pred(m; e*)`.
4. Track the evolution of `DeltaS_pred(m; e*)`, `DeltaS_eq(m)`, and `I_contrast(m; e*)` as the number of windows grows.

**Metrics**

* Time series of `Gain(m; S_j; e*)` for each scoring rule.
* Time series of `DeltaS_pred(m; e*)` and `DeltaS_eq(m)` as scalar indicators of predictability_tension.
* The contrast invariant `I_contrast(m; e*)` as a measure of diversity and separation among models.

**Falsification conditions**

The encoding element `e*` is considered falsified or incomplete at the effective layer if either of the following occurs across multiple regions and time scales:

1. Persistent high mismatch

   * `DeltaS_pred(m; e*)` stays large or grows without stabilising, despite reasonable library revisions that stay within `A_enc(Q096)` and conform to the constraints declared in Section 3.6.

2. Structural instability

   * trivial modifications of scoring definitions or model weighting can arbitrarily reduce `DeltaS_pred(m; e*)` without any corresponding improvement in prospective performance under established seismological metrics.

In either case, the conclusion is that the specific effective layer encoding `e*` is rejected or must be revised. This does not imply any conclusion about:

* the existence of other encoding elements `e` in `A_enc(Q096)` that might succeed, or
* the underlying physical question of whether earthquakes are predictable.

**Semantics implementation note**

All forecasts, counts, and scores are treated in the hybrid sense described in the header:

* physical fields are continuous in space and time,
* forecast and observation observables are discrete summaries over fixed grid cells and windows.

**Boundary note**

Falsifying the TU encoding element `e*` does not solve and does not refute the canonical scientific question of earthquake predictability. It only constrains which effective layer encodings are compatible with observed forecast performance under the chosen rules.

---

### Experiment 2: Stress test under major sequence or swarm

**Goal**
Test whether the Q096 predictability_tension encoding associated with `e*` can detect and characterise changes in forecast skill during a major earthquake sequence or swarm.

**Setup**

* Choose a region where a large mainshock and aftershock sequence, or a prolonged swarm, has occurred within the available catalog.
* Construct three sets of test windows:

  * pre sequence windows representing a background regime,
  * sequence windows representing a high activity regime,
  * post sequence windows representing a relaxation regime, if available.
* Use the same model and scoring libraries `L_eq_model(e*)` and `L_eq_score(e*)` as in Experiment 1.

**Protocol**

1. For pre sequence windows, define states `m_pre in M_reg`, compute `Gain(m_pre; S_j; e*)` and `DeltaS_pred(m_pre; e*)`.
2. For sequence windows, define states `m_seq in M_reg`, compute the same quantities, now reflecting performance under extreme clustering.
3. For post sequence windows, define states `m_post in M_reg` and compute the same observables to examine relaxation behaviour.
4. Compare the behaviour of `DeltaS_pred(m; e*)`, `DeltaS_eq(m)`, and `I_contrast(m; e*)` between the background, sequence, and post sequence regimes.

**Metrics**

* Differences in `DeltaS_pred(m; e*)` and `DeltaS_eq(m)` between pre sequence, sequence, and post sequence regimes.
* Changes in model ranking and performance contrast `I_contrast(m; e*)`.
* Stability of models that explicitly incorporate clustering compared to models that do not.

**Falsification conditions**

The encoding element `e*` is considered misaligned for this aspect of the problem if:

1. No regime sensitivity

   * the encoding fails to register any significant change in predictability_tension between background and sequence regimes, even when performance differences are large under standard seismological metrics.

2. Erasable tension

   * the encoding can be tuned after seeing the data to erase any tension signal from known difficult regimes without corresponding gains in forecast reliability.

In such cases, the conclusion is that the current choice of observables, benchmarks, and thresholds in `e*` does not capture the difficulty of sequences and swarms at the effective layer.

**Semantics implementation note**

Counts and scores are again treated as discrete summaries. The underlying stress evolution and clustering processes are interpreted as continuous fields whose detailed representation is external to this block.

**Boundary note**

As in Experiment 1, falsifying the encoding element `e*` does not settle the question of whether earthquakes are fundamentally predictable. It only tests whether the selected effective layer observables and thresholds respond meaningfully to regimes that seismologists already regard as challenging.

---

## 7. AI and WFGY engineering spec

This block describes how Q096 can be used as an engineering module inside AI systems within the WFGY framework, while remaining strictly at the effective layer.

All training signals and architectural components below are derived from observables introduced in Sections 3 to 6. None of them require access to any TU core axiom system or hidden generative rule.

### 7.1 Training signals

We define several training signals derived from Q096 observables and invariants associated with `e*`.

1. `signal_hazard_calibration`

   * Definition: a penalty proportional to miscalibration of forecast probabilities relative to observed counts in seismic contexts, derived from gaps between model implied forecasts and the observed performance scores.
   * Purpose: encourage models to represent earthquake hazard with realistic calibration rather than overconfident narratives.

2. `signal_predictability_envelope`

   * Definition: a scalar derived from `DeltaS_pred(m; e*)` or `DeltaS_eq(m)` that measures distance from a low tension predictability envelope.
   * Purpose: encourage AI systems to respect known limits of predictability and to distinguish between regimes where forecast gains exist and regimes where they do not.

3. `signal_model_diversity`

   * Definition: a signal based on `I_contrast(m; e*)`, rewarding internal representations that support genuinely diverse model hypotheses where justified by data.
   * Purpose: prevent premature collapse onto a single untested forecast narrative when the encoding suggests that model diversity is still valuable.

4. `signal_warning_coherence`

   * Definition: a penalty applied when suggested risk communications imply deterministic certainty or strong short term prediction in regimes where the predictability envelope indicates weak or no skill.
   * Purpose: align natural language risk statements with the constraints implied by `DeltaS_pred`, `E_pred`, and `I_contrast`.

### 7.2 Architectural patterns

We outline module patterns that reuse Q096 components without exposing deeper TU structures.

1. `EQ_PredictabilityHead`

   * Role: given internal representations of a seismic decision context, outputs estimates of `DeltaS_pred(m; e*)`, `DeltaS_eq(m)`, and `I_contrast(m; e*)` as auxiliary channels.
   * Interface:

     * Inputs: task embeddings summarising region, horizon, magnitude threshold, and forecast context.
     * Outputs: a small vector of tension metrics that can be used for calibration and gating.

2. `MultiScaleHazardEncoder_EQ`

   * Role: builds compressed descriptors of seismic hazard fields over multiple scales in space and time, consistent with the region horizon library associated with `e*`.
   * Interface:

     * Inputs: raw or summarised hazard maps and catalog summaries.
     * Outputs: low dimensional embeddings that serve as inputs to forecast or decision modules.

3. `ForecastLibraryController_EQ`

   * Role: manages a finite internal library of forecast modes or hypotheses mirroring `L_eq_model(e*)` and tracks their relative performance through time.
   * Interface:

     * Inputs: context embeddings and outcome summaries.
     * Outputs: updated weights or scores over forecast modes, and derived tension metrics.

### 7.3 Evaluation harness

We propose an evaluation harness for AI systems augmented with Q096 modules.

1. Task selection

   * Combine question sets on earthquake science, risk communication, and emergency planning.
   * Include both technical questions about forecast models and tests, and layperson questions about “prediction” and safety advice.

2. Conditions

   * Baseline condition:

     * the AI system responds without explicit Q096 modules, using only general training.
   * TU augmented condition:

     * the AI system uses `EQ_PredictabilityHead` and `MultiScaleHazardEncoder_EQ` as auxiliary components and uses their outputs in reasoning and generation.

3. Metrics

   * Factual accuracy on technical questions about forecast limits and testing frameworks.
   * Calibration of verbal risk statements against known forecast uncertainties and the predictability envelope implied by `e*`.
   * Consistency across scenarios, measured by whether the system maintains the same predictability envelope when equivalent hazard information is presented in different framings.

### 7.4 Sixty second reproduction protocol

A minimal interactive protocol allows external users to experience the impact of Q096 style reasoning in an AI system.

* Baseline setup

  * Prompt: ask the AI “Can we predict earthquakes?” with natural follow up questions about short term and long term forecasts.
  * Observation: record whether the system confuses deterministic prediction with probabilistic forecasting, or overstates predictability.

* TU encoded setup

  * Prompt: ask the same questions but explicitly instruct the AI to reason using:

    * a finite library of forecast models,
    * explicit performance tests over time,
    * and a predictability_tension envelope similar to Q096.
  * Observation: record whether the answer now:

    * distinguishes deterministic prediction from probabilistic forecasting,
    * refers to constraints from prospective tests in a way consistent with `DeltaS_pred` and `DeltaS_eq`.

* Comparison metric

  * Use a simple rubric to rate:

    * clarity in describing what can and cannot be forecasted,
    * calibration of confidence statements,
    * explicit reference to the limits of forecast skill.

* Logs

  * Retain prompts, responses, and any exposed tension metrics for both conditions. These logs provide input for refining future encoding elements in `A_enc(Q096)`.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

All components listed here are defined relative to the encoding element `e*` selected by `Encoding_key`. If a different encoding element is chosen, these components must be recalibrated.

1. ComponentName: `PredictabilityEnvelope_EQ`

   * Type: functional

   * Minimal interface:

     ```txt
     inputs:
       summaries of L_eq_model(e*) forecasts,
       scoring results under L_eq_score(e*),
       benchmark gains Target_gain_j(e*)
     outputs:
       scalar and vector indicators of predictability_tension
       such as DeltaS_pred(m; e*), DeltaS_eq(m), and E_pred(m; e*)
     ```

   * Preconditions:

     * inputs correspond to a coherent set of prospective or retrospective forecast tests over defined region horizon pairs within the domain of `e*`.

2. ComponentName: `HazardField_MultiScale_Descriptor_EQ`

   * Type: field

   * Minimal interface:

     ```txt
     inputs:
       region-horizon grids compatible with e*,
       long term hazard estimates,
       time varying rate fields
     output:
       compressed descriptors of multi scale seismic hazard
       suitable for reuse in other hazard problems
     ```

   * Preconditions:

     * grids and rates are defined according to a fixed partition and magnitude threshold scheme associated with `e*`.

3. ComponentName: `ProspectiveForecast_Experiment_Template_EQ`

   * Type: experiment_pattern

   * Minimal interface:

     ```txt
     inputs:
       region specification,
       model library L_eq_model(e*),
       scoring library L_eq_score(e*),
       test schedule
     output:
       experiment design including:
         forecast submission rules,
         evaluation steps,
         predictability_tension observables
     ```

   * Preconditions:

     * the experiment is feasible with existing catalog and computational resources.

### 8.2 Direct reuse targets

1. Q095 (Drivers of biodiversity loss and recovery)

   * Reused component: `HazardField_MultiScale_Descriptor_EQ`.
   * Why it transfers: biodiversity loss and recovery are influenced by physical shocks including earthquakes. Q095 needs multi scale hazard descriptors as one class of inputs in its biodiversity tension functional.
   * What changes: the descriptor is combined with hazard descriptors for floods, heat extremes, and other drivers to form joint state representations for ecosystems.

2. Q094 (Hurricane pattern shifts and landfall risk)

   * Reused component: `PredictabilityEnvelope_EQ` as a template.
   * Why it transfers: both problems address predictability versus uncertainty for high impact events, with tension between model skill and societal expectations.
   * What changes: forecast models become hurricane models, and region horizon grids are adapted to ocean basins and seasons instead of fault zones.

3. Q097 (Gigafire regimes)

   * Reused component: `ProspectiveForecast_Experiment_Template_EQ`.
   * Why it transfers: the same pattern of prospective testing with fixed model libraries and scoring rules can be applied to wildfire spread and ignition forecasts.
   * What changes: observables track fire counts, burned area, and intensity statistics instead of earthquake counts and magnitudes, but the experiment structure remains similar.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * The Q096 encoding specifies state spaces, observables, a predictability mismatch scalar, and a tension functional associated with the encoding element `e*`.
  * It includes concrete experiment templates but does not yet require full implementation details or large scale deployments.

* N_level: N1

  * The narrative describes how seismic forecast performance relates to predictability_tension, with explicit reference to forecast libraries and test regimes.
  * Counterfactual worlds and transfer patterns are sketched but not yet fully instantiated across all BlackHole nodes.

### 9.2 Next measurable step toward E2

To move from E1 to E2 for this encoding element `e*`, at least one of the following should be realised:

1. Reference implementation

   * Implement a working prototype that ingests published CSEP or OEF style forecast and observation data, computes `DeltaS_pred(m; e*)`, `DeltaS_eq(m)`, and related invariants, and publishes predictability_tension profiles as open data.

2. TU augmented AI pilot

   * Deploy a pilot AI system that uses Q096 derived signals to improve calibration and communication of earthquake risk compared with a baseline system, with evaluation on realistic user tasks.

Both steps remain at the effective layer, operating on published summaries and forecast archives rather than exposing any deeper TU construction rules.

### 9.3 Long term role in the TU program

Over the longer term, Q096 is intended to:

* anchor geohazard predictability questions as instances of predictability_tension on multi scale hazard fields,
* provide a common language for comparing forecast skill and limitations across hazards,
* serve as a testbed for AI systems that must reason responsibly about rare but devastating events.

Success would mean that for serious debates about “whether earthquakes can be predicted” there exists a clear framing in terms of Q096 invariants and experiments that separates effective layer evidence from speculation about deeper physics.

---

## 10. Elementary but precise explanation

This block gives an explanation for non experts while staying consistent with the effective layer encoding.

People often ask whether we can predict earthquakes. The honest scientific answer is careful rather than simple.

* We cannot say exactly when and where a big earthquake will strike, in the same precise way we can predict a solar eclipse.
* We can say that some places are much more likely to have earthquakes than others, and that after a big event more earthquakes are likely nearby for some time.

Modern seismology treats this as a forecasting question. Instead of saying “There will be a magnitude 7 event here tomorrow,” scientists build models that say things like

* “In this region, over the next year, the chance of a damaging earthquake is about X percent.”

Q096 takes this practical view and asks:

* How much better than a very simple background model can we do, in repeated and fair tests?
* Do our best models really beat a simple reference model in the long run?
* When we think we have found patterns, do they keep working when tested in future windows?

In the Tension Universe picture, we imagine a space of world states where each state summarises:

* what our forecast models said for a set of regions and time windows,
* what actually happened in those windows,
* and how we scored the models.

From this information the encoding builds a number `DeltaS_pred(m; e*)` that measures how far we are from a world where earthquakes are clearly predictable at the tested scales. If this number can be kept small and stable across many tests, the world looks predictability friendly for those scales. If the number stays large, even after careful model building, the world looks stubbornly unpredictable for those scales.

This does not prove any deep theorem about faults. It does something more practical:

* It forces us to write down what we mean by “predictable” in terms that can be tested repeatedly.
* It forces us to compare models fairly, without changing the rules after seeing the data.
* It gives us a way to carry lessons about predictability from earthquakes to other hazards and into AI systems that communicate risk to the public.

Q096 is therefore not a magic prediction recipe. It is a rigorous way to talk about what prediction could mean, how far we have come, and how far we might still be from the limits of what is physically and statistically possible for earthquakes at the scales where people need decisions.

---

## Tension Universe effective layer footer

This page is part of the WFGY / Tension Universe S problem collection and encodes the Q096 earthquake predictability problem at the effective layer.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of Q096 in terms of state spaces, observables, tension scores, and experiment templates.
* It does not claim to prove or disprove the canonical scientific statement about earthquake predictability in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that earthquakes are deterministically predictable or that any specific operational forecasting scheme is sufficient for risk management.

### Effective layer boundary

* All objects used here such as state spaces `M_quake` and `M_reg`, observables, invariants, tension scores, and counterfactual worlds live at the effective layer.
* No mapping is given from raw seismic catalogs, geodetic data, or physical simulations to TU internal fields. Any such mappings, if implemented, must be specified in separate and independently documented pipelines.
* No TU core axiom system, deep generative rule, or semantic curvature structure is exposed or assumed beyond what is needed to interpret the effective layer variables on this page.

### Encoding and thresholds

* The header field `Encoding_key: TU_BH_Q096_EQ_v1` selects a single encoding element `e* in A_enc(Q096)` as defined in Section 3.6.
* All uses of model libraries, scoring rules, benchmark gains, scale factors, and thresholds in this document refer to the chosen element `e*`.
* The tension scalar `DeltaS_eq(m)` is defined as `Tension_EQ(m; e*)` and represents one possible predictability_tension score for Q096. Other encoding elements in `A_enc(Q096)` may lead to different tension scores.

### Relation to experiments and falsifiability

* The experiment templates in Section 6 describe how to test whether the chosen encoding element `e*` is coherent and useful at the effective layer.
* Falsifying `e*` under those experiments means rejecting this particular choice of observables, thresholds, and libraries. It does not rule out other encoding elements in `A_enc(Q096)`.
* Passing those experiments does not establish that earthquake predictability is “solved.” It only shows that the chosen effective layer encoding is consistent with the tested data and protocols.

### Relation to external science and policy

* Nothing in this document overrides or replaces official guidance from seismological agencies, geological surveys, or civil protection authorities.
* Any operational use of Q096 style quantities in real world decision processes must respect domain specific standards, local regulations, and ethical review.

### Linked charters

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
