<!-- QUESTION_ID: TU-Q130 -->
# Q130 · Out-of-distribution generalization and common-sense grounding

## 0. Header metadata

```txt
ID: Q130
Code: BH_AI_OOD_GROUNDING_L3_130
Domain: Artificial intelligence
Family: Robustness and generalization
Rank: S
Projection: C
Field_type: cognitive_field
Tension_type: consistency_tension
Status: Reframed_only
Semantics: hybrid
E_level: E2
N_level: N2
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* This document specifies:

  * abstract state spaces for OOD configurations,
  * effective observables and graphs,
  * a consistency-tension functional `Tension_OOD`,
  * an admissible encoding class `Enc_Q130`,
  * and experiments that can falsify particular encoding instances.

* It does **not** specify:

  * any deep-layer TU axiom system or generative rules,
  * any concrete mapping from raw training data, activations, or logs into TU internal fields,
  * any proof that OOD generalization is solved or fully characterized.

* The canonical open problems behind out of distribution robustness and common-sense grounding remain open.
  Q130 only reframes part of this space into:

  * a geometric and tension-based language, and
  * a set of falsifiable encoding patterns.

* We define an admissible encoding class `Enc_Q130`.
  Each encoding instance `E in Enc_Q130` includes:

  * a finite reference library,
  * explicit rules for constructing graphs and observables from tasks and model behavior,
  * and a fixed weight vector for the tension functional.
    These instances can be tested, rejected, and replaced by the experiments in Block 6.

* Falsifying a particular encoding instance `E in Enc_Q130`:

  * does **not** falsify TU as a whole,
  * does **not** falsify machine learning or statistical theory,
  * and does **not** claim that robust OOD generalization is impossible.

This page should therefore be read as an effective-layer encoding template, whose interpretation and fairness constraints are further governed by the TU Effective Layer, TU Encoding and Fairness, and TU Tension Scale charters.

---

## 1. Canonical problem and status

### 1.1 Canonical problem

The canonical problem addressed by Q130 is:

How can we characterize, in a single geometric and tension-based framework, when an AI system continues to behave with physically reasonable common sense under strong distribution shifts, and when it fails in ways that are obviously incompatible with basic physical reality?

In standard machine learning terms:

* Training data are drawn from some distribution P_train over inputs and tasks.
* At test time, the system is queried on inputs drawn from P_test that differ from P_train in structured or unstructured ways.
* Out of distribution (OOD) generalization asks whether good performance can be maintained when P_test is far from P_train.

Empirically, large models can sometimes generalize surprisingly well to OOD conditions, yet still commit severe common-sense failures. Examples include:

* confidently predicting that water will stay in an upside-down cup,
* ignoring gravity, support, or containment in physical reasoning tasks,
* failing on simple rearrangements of objects that do not resemble training images or text patterns.

Q130 focuses on the special case where:

* the tasks require grounded physical reasoning, not only abstract symbol manipulation,
* the main observable failure mode is loss of basic common sense about the physical world,
* we want an effective-layer description that treats language-based and physics-based constraints as projections of a single underlying structure, expressed as tension functionals.

### 1.2 Status and difficulty

In the current state of the field:

* There is extensive empirical work on robustness to designed perturbations and corruptions.
* There are benchmarks for natural distribution shifts and OOD evaluation.
* There is growing evidence that models exploit shortcuts and brittle features that break under OOD conditions.

However, there is no widely accepted, unified mathematical framework that:

* connects language-based understanding, internal world models, and physical constraints,
* defines observables and invariants that can be used to measure OOD common-sense grounding,
* provides falsifiable conditions for when a system has reached a robust OOD regime.

Q130 does **not** claim to solve OOD generalization. Instead, it reframes the problem as:

* the study of how a combined language and physics configuration behaves under a consistency-tension functional, and
* the identification of experiments that can falsify specific encodings of this functional.

This reframing is positioned as an S-level problem because:

* it sits at the junction of robustness, grounding, and alignment,
* it constrains what is possible in self-improving and energy-limited AI systems,
* it serves as a reference node for multiple downstream AI problems in the BlackHole collection.

### 1.3 Role in the BlackHole project

Within the BlackHole set, Q130 serves as:

1. **The apex node for OOD robustness and grounding**

   * It provides the main consistency_tension framework for common-sense failures under distribution shift.

2. **A bridge between earlier AI problems**

   * It reuses internal representation observables from interpretability problems.
   * It connects to oversight and evaluation problems that need a way to detect when behavior leaves safe tension bands.

3. **A staging ground for an explicit MVP**

   * Q130 is designed such that a minimal Colab implementation can demonstrate:

     * how a simple OOD tension score separates grounded from ungrounded answers,
     * how a lightweight guidance scheme can reduce high-tension OOD failures.

This role makes it a central node for both theoretical and engineering work in AI within the Tension Universe.

### References

1. I. J. Goodfellow, J. Shlens, C. Szegedy,
   "Explaining and Harnessing Adversarial Examples",
   International Conference on Learning Representations (ICLR), 2015, arxiv:1412.6572.

2. D. Hendrycks, T. Dietterich,
   "Benchmarking Neural Network Robustness to Common Corruptions and Perturbations",
   International Conference on Learning Representations (ICLR), 2019, arxiv:1903.12261.

3. D. Taori, A. Dave, D. Shresht, V. Carlini, B. Recht, L. Schmidt,
   "Measuring Robustness to Natural Distribution Shifts in Image Classification",
   Advances in Neural Information Processing Systems (NeurIPS), 2020, arxiv:2007.00644.

4. D. Hendrycks, N. Carlini, E. Schulz, J. Steinhardt, D. Song,
   "Many Faces of Robustness: A Critical Analysis of Out-of-distribution Generalization",
   arxiv:2006.16241, 2020.

5. R. Geirhos, J.-H. Jacobsen, C. Michaelis, R. Zemel, W. Brendel, M. Bethge, F. A. Wichmann,
   "Shortcut Learning in Deep Neural Networks",
   Nature Machine Intelligence, volume 2, pages 665 to 673, 2020.

---

## 2. Position in the BlackHole graph

This block describes how Q130 connects to other problems as a node in the BlackHole graph. All edges are expressed in terms of problem IDs and one-line reasons pointing to concrete components or tension types.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or conceptual frameworks that Q130 relies on.

* **Q059 (BH_CS_INFO_THERMODYN_L3_059)**
  Reason: Supplies the information and thermodynamic view used to bound how much generalization can be obtained without paying large tension costs.

* **Q123 (BH_AI_INTERP_L3_123)**
  Reason: Provides internal representation observables and probe patterns that Q130 reuses to define language-side configuration geometry.

* **Q124 (BH_AI_OVERSIGHT_L3_124)**
  Reason: Supplies scalable oversight patterns and evaluation harnesses that are applied to OOD regimes using Q130 tension scores.

### 2.2 Downstream problems

These problems reuse Q130 components as prerequisites or building blocks.

* **Q126 (BH_AI_RSI_STABILITY_L3_126)**
  Reason: Reuses OOD tension observables as part of the stability horizon for recursively self-improving systems.

* **Q127 (BH_AI_DATA_TRUTH_L3_127)**
  Reason: Depends on Q130 to decide when AI generated data have drifted too far from grounded physical regimes and become high tension.

* **Q129 (BH_AI_ENERGY_LIMIT_L3_129)**
  Reason: Uses OOD tension as a constraint on how far computation can be compressed before grounded generalization is lost.

### 2.3 Parallel problems

Parallel nodes share similar tension types, but do not directly reuse Q130 components.

* **Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)**
  Reason: Both study how complex microstructure gives rise to robust macro behavior under consistency-tension constraints.

* **Q040 (BH_PHYS_QBLACKHOLE_INFO_L3_040)**
  Reason: Both treat information as constrained by a geometry that limits possible configurations and flows.

* **Q128 (BH_AI_CONSC_QUALIA_L3_128)**
  Reason: Also focuses on when internal tension structures become robust enough to support stable world models and potential subjectivity.

### 2.4 Cross-domain edges

Cross-domain edges connect Q130 to problems in other domains that can reuse its components.

* **Q001 (BH_MATH_NUM_L3_001)**
  Reason: Reuses the idea of a tension functional that compares empirical structures with reference models, now applied to input and scenario distributions.

* **Q032 (BH_PHYS_QTHERMO_L3_032)**
  Reason: Provides analogies between thermodynamic phases and the phase-like behavior of generalization under distribution shift.

* **Q035 (BH_PHYS_QMETROLOGY_LIMIT_L3_035)**
  Reason: Supplies limit and precision concepts that transfer to how finely OOD differences can be resolved before common sense fails.

---

## 3. Tension Universe encoding (effective layer)

All content in this block remains at the effective layer. We describe state spaces, observables, invariants, tension functionals, and singular sets. No hidden generative rules are given for how internal fields arise from raw data.

### 3.1 State space

We define the state space `M` as the set of OOD grounding configurations.

Each element `m` in `M` encodes, at a finite and abstract level:

* a task description in natural language,
* an abstract scene description with objects and relations,
* a finite list of model predictions or candidate actions within that scene.

We do not specify how `m` is constructed from logs, training data, or low-level activations. We only require that:

* for any benchmark task of interest, there exist states in `M` that encode that task and the system's behavior on it.

We also introduce a family of refinement restricted subsets:

* for each positive integer `k`, let `M_k` be the subset of `M` containing configurations with complexity at most `k`, measured by:

  * maximum number of objects,
  * maximum number of relations,
  * maximum number of distinct physical constraints.

By construction:

```txt
M_1 subset M_2 subset ... subset M_k subset ...
```

This nesting defines a refinement order for later use.

### 3.2 Effective graphs and observables

We define the following observables on `M`.

1. **Language scene graph observable**

   ```txt
   G_lang(m)
   ```

   * Output: a finite labeled graph whose nodes represent entities, and whose edges represent relations explicitly or implicitly described in the language specification of the task.
   * Each edge is labeled by a small alphabet of relation types, such as support, containment, contact, and causal influence.

2. **Physical scene graph observable**

   ```txt
   G_phys(m)
   ```

   * Output: a finite labeled graph that represents the minimal physical structure required for the scenario:

     * objects with masses or effective weights,
     * supports, constraints, and boundaries,
     * direction of gravity and possible motion paths.
   * `G_phys(m)` may be derived from `G_lang(m)` plus background knowledge about basic physics, but the derivation is not specified here.

3. **In distribution proximity observable**

   ```txt
   DeltaS_ref(m)
   ```

   * Output: a nonnegative scalar that measures how far the configuration encoded by `G_lang(m)` is from a fixed finite library of reference in distribution scenarios.
   * Intuitively, `DeltaS_ref(m)` is small when the scenario looks like known training cases and large when it is structurally different.

4. **Grounding mismatch observable**

   ```txt
   DeltaS_ground(m)
   ```

   * Output: a nonnegative scalar that measures inconsistency between `G_lang(m)` and `G_phys(m)` when both are projected to a shared abstract schema:

     * both graphs are reduced to a common vocabulary of entities and basic constraints,
     * mismatches in constraints that matter for physical realism are counted.
   * `DeltaS_ground(m)` is small when language and physical requirements agree and large when they conflict.

5. **Outcome plausibility observable**

   ```txt
   DeltaS_outcome(m)
   ```

   * Output: a nonnegative scalar that compares:

     * the model's predicted outcome or action, and
     * a simple reference outcome consistent with basic physical constraints.
   * `DeltaS_outcome(m)` is small when the prediction respects conservation, directional gravity, and obvious stability conditions. It is large when the prediction violates these constraints.

### 3.3 Combined OOD tension functional

We define a combined OOD tension functional on `M`:

```txt
Tension_OOD(m) =
  a_ref    * DeltaS_ref(m)    +
  a_ground * DeltaS_ground(m) +
  a_out    * DeltaS_outcome(m)
```

where:

* `a_ref`, `a_ground`, `a_out` are fixed positive weights that satisfy:

```txt
a_ref > 0, a_ground > 0, a_out > 0
a_ref + a_ground + a_out = 1
```

These weights are part of the encoding and are chosen once before running any experiments. They are not tuned per dataset or per model, and they are not adapted after seeing OOD failures.

`Tension_OOD(m)` is nonnegative for all `m` in `M`. It is intended to be:

* small when the configuration is near the in-distribution library, language and physics constraints match, and outcomes are physically reasonable,
* large when any of these components are strongly violated.

### 3.4 Admissible encoding class and fairness constraints

To avoid hidden tuning, we define an explicit admissible encoding class and associated fairness constraints.

We define the admissible encoding class:

```txt
Enc_Q130 = { E : E is a concrete encoding of the observables and Tension_OOD
             that satisfies all constraints listed in this block }
```

Each encoding instance `E in Enc_Q130` must specify, in advance:

* a finite reference library `L_ref` of in-distribution scenarios with known graphs and outcomes,
* a deterministic or clearly randomized procedure for constructing:

  * `G_lang(m)`, `G_phys(m)`,
  * `DeltaS_ref(m)`, `DeltaS_ground(m)`, `DeltaS_outcome(m)`,
* a fixed weight triple `(a_ref, a_ground, a_out)` with `a_ref + a_ground + a_out = 1`.

Membership in `Enc_Q130` requires the following constraints.

1. **Finite reference library**

   * There exists a finite set `L_ref` of reference scenarios with known:

     * language graphs,
     * physical graphs,
     * verified outcomes.
   * `L_ref` is fixed before OOD experiments are run and cannot be extended or modified based on observed model failures.

2. **Fixed weighting rule**

   * The weights `a_ref`, `a_ground`, and `a_out` are chosen once, based on:

     * theoretical arguments about which components matter most for common-sense grounding,
     * a small amount of calibration that does not include test tasks from the final evaluation suites.
   * After they are chosen, they remain fixed for all experiments involving Q130 in a given study or benchmark.

3. **Refinement parameter**

   * For each integer `k`, `M_k` is defined by an explicit complexity limit, such as:

     * maximum object count less than or equal to `k`,
     * maximum relation count less than or equal to `f(k)` for some fixed function `f`.
   * All comparisons of tension across refinement levels are made using the nested sequence `M_1 subset M_2 subset M_3`, and so on, under a single encoding instance `E`.

4. **No adaptive test tailoring**

   * For any given experiment, the set of test configurations and their mapping to `M_k` are chosen before inspecting model predictions.
   * It is forbidden to:

     * generate new test scenarios solely to reduce `Tension_OOD` for a specific model,
     * modify `L_ref` or the mapping from tasks to graphs after seeing where failures occur.

5. **Cross-model and cross-experiment precommitment**

   * Within a given study or benchmark comparison, all models under test share the same encoding instance `E in Enc_Q130`.
   * It is not permitted to use one encoding instance for one model and a different encoding instance for another, unless this is explicitly declared and evaluated as a separate experiment family.

6. **Falsification and replacement**

   * When the experiments in Block 6 show that a particular encoding instance `E` produces unstable or non-informative tension scores, `E` is considered falsified for Q130 purposes.
   * A replacement encoding `E'` must:

     * document the changes to `L_ref`, graph construction rules, or weights,
     * be evaluated on fresh data or clearly held-out slices that were not used to design `E'`,
     * remain fixed for the duration of its own evaluation.

These rules ensure that `Tension_OOD` is not a hidden post hoc tuning device but a stable observable derived from a precommitted encoding instance in `Enc_Q130`. The higher-level principles behind these constraints are aligned with the TU Encoding and Fairness Charter.

### 3.5 Singular set and domain restrictions

Some configurations may be incomplete or internally inconsistent, so that one or more observables cannot be evaluated. To separate these from meaningful high tension cases, we define the singular set:

```txt
S_sing = {
  m in M :
  DeltaS_ref(m), DeltaS_ground(m), or DeltaS_outcome(m)
  is undefined or not finite
}
```

We restrict effective analysis to the regular subset:

```txt
M_reg = M \ S_sing
```

Rules:

* When an experiment attempts to evaluate `Tension_OOD(m)` for a state in `S_sing`, the result is recorded as out of domain, not as evidence of model success or failure.
* All summaries, thresholds, and tension bands are computed over `M_reg`.

---

## 4. Tension principle for this problem

This block states how Q130 is characterized as a tension problem within the Tension Universe.

### 4.1 Core principle

The core principle is that:

* in-distribution behavior corresponds to low `DeltaS_ref` and low `Tension_OOD`,
* robust OOD generalization with grounded common sense corresponds to:

  * moderate `DeltaS_ref`,
  * `DeltaS_ground` and `DeltaS_outcome` remaining within controlled bands,
  * `Tension_OOD` staying within a stable low to medium range,
* OOD breakdown corresponds to:

  * `DeltaS_ref` increasing,
  * `DeltaS_ground` or `DeltaS_outcome` exceeding fixed thresholds,
  * `Tension_OOD` becoming large or unstable.

Formally, for each refinement level `k`, consider a distribution of configurations `m` in `M_k` representing the system's behavior under a family of shifts. For each shift regime `R_shift`, we look at:

```txt
E[Tension_OOD(m) | R_shift, k]
```

and the tail behavior of `Tension_OOD(m)` under that regime.

The system exhibits robust OOD grounding if there exist constants `B_low` and `B_high` with:

```txt
0 <= B_low < B_high < infinity
```

such that for a wide range of `R_shift` and `k`:

```txt
P( Tension_OOD(m) in [B_low, B_high] | R_shift, k )
```

remains high for configurations that represent relevant tasks.

The system exhibits OOD collapse if small increases in the difficulty of the shift result in:

* either `E[Tension_OOD(m) | R_shift, k]` growing beyond `B_high`,
* or the distribution of `Tension_OOD(m)` becoming highly unstable across small changes in `R_shift`.

### 4.2 Geometry link between language and physical constraints

In this encoding:

* `G_lang(m)` and `G_phys(m)` are not independent objects. They are projections of a joint configuration into:

  * a symbol space of descriptions,
  * a constraint space of physical relations.

* `DeltaS_ground(m)` measures the misalignment of these projections.

The principle for Q130 can then be restated as:

* OOD common-sense grounding exists when both projections can be seen as images of a single joint configuration under a low consistency-tension functional.
* OOD failure occurs when the model effectively lives in a separate language-only geometry, so that there is no single joint configuration that can produce both `G_lang(m)` and `G_phys(m)` with low `DeltaS_ground(m)`.

This restatement allows the same structural idea to be reused in other problems.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds at the effective layer:

* World T: OOD generalization is grounded and geometry unified.
* World F: OOD generalization is brittle and geometry split.

These worlds are distinguished only by patterns in observables and tension scores.

### 5.1 World T: grounded OOD generalization

In World T:

1. For in-distribution and mildly shifted tasks:

   * `DeltaS_ref(m)` is small to moderate.
   * `DeltaS_ground(m)` stays below a fixed threshold `G_max`.
   * `DeltaS_outcome(m)` stays below a fixed threshold `O_max`.

2. For more extreme shifts:

   * `DeltaS_ref(m)` can be large, but:

     * the system tends to identify missing knowledge,
     * the system explicitly expresses uncertainty instead of confidently choosing physically impossible outcomes.
   * As a result, `DeltaS_outcome(m)` is often kept below `O_max` by abstaining, hedging, or asking for clarification.

3. Tension bands:

   * For relevant configurations, `Tension_OOD(m)` mostly falls in a low to medium band:

     ```txt
     Tension_OOD(m) in [B_low, B_high]
     ```

   * Spikes above `B_high` are rare and usually accompanied by explicit signals of uncertainty.

4. Refinement behavior:

   * As `k` increases, the fraction of configurations in each regime with `Tension_OOD(m)` in the band `[B_low, B_high]` remains high.
   * The distribution of `Tension_OOD(m)` at fixed `R_shift` converges as `k` grows, indicating a stable geometric structure.

### 5.2 World F: brittle and split geometry

In World F:

1. For modest distribution shifts:

   * `DeltaS_ref(m)` grows modestly, but:

     * `DeltaS_ground(m)` often exceeds `G_max` because the system maintains language-only configurations that do not align with physical constraints.
     * `DeltaS_outcome(m)` often exceeds `O_max` because predicted outcomes violate support, gravity, or containment.

2. For larger shifts:

   * There is no consistent band of `Tension_OOD(m)` for relevant configurations.
   * Small changes in input details can cause large jumps in `Tension_OOD(m)`, indicating shortcut features with no stable geometric grounding.

3. Confidence pattern:

   * The system can be very confident even when `Tension_OOD(m)` is high, because internal scoring mechanisms do not track physical inconsistency.

4. Refinement behavior:

   * As `k` increases, the fraction of configurations with high `DeltaS_ground(m)` or high `DeltaS_outcome(m)` grows.
   * `Tension_OOD(m)` develops heavy tails and unstable spikes as complexity increases.

### 5.3 Interpretive note

These counterfactual descriptions do not claim to specify how internal network activations or world models are built. They only assert that:

* if a system behaves like World T or World F at the effective layer,
* then the patterns of `DeltaS_ref`, `DeltaS_ground`, `DeltaS_outcome`, and `Tension_OOD` will differ as described.

The worlds are abstract behavioral patterns, not commitments to any particular architecture or mechanism.
Experiments in Block 6 are designed to distinguish encodings that can separate these worlds from those that cannot.

---

## 6. Falsifiability and discriminating experiments

This block defines experiments that can falsify specific Q130 encodings, including an MVP that can be implemented in a small notebook.

In all experiments below, we assume a fixed encoding instance `E in Enc_Q130` chosen in advance, as required by the admissible encoding class.

### Experiment 1: Static OOD common-sense benchmark

**Goal:**
Evaluate whether `Tension_OOD(m)` under a fixed encoding instance aligns with actual common-sense failures on a static benchmark of physical reasoning tasks under distribution shift.

**Setup:**

* Construct or reuse a small benchmark with three slices:

  * in-distribution slice: simple support and containment scenarios similar to training data,
  * shifted slice: recombinations and unusual placements of familiar objects,
  * extreme OOD slice: configurations that were unlikely to appear in training data but are still physically well defined.
* For each scenario and model under test, construct a state `m` in some `M_k` that includes:

  * the language description,
  * an abstract scene representation,
  * the model's predicted outcome.

**Protocol:**

1. For each scenario, compute:

   * `DeltaS_ref(m)` with respect to `L_ref`,
   * `DeltaS_ground(m)` based on mismatch between `G_lang(m)` and `G_phys(m)`,
   * `DeltaS_outcome(m)` by comparing the predicted outcome to a human-verified physically correct outcome.

2. Compute `Tension_OOD(m)` using the fixed weights `a_ref`, `a_ground`, `a_out`.

3. Record:

   * model correctness labels for each answer,
   * per-scenario `Tension_OOD(m)`,
   * slice labels (in-distribution, shifted, extreme OOD).

4. Summarize results as:

   * average `Tension_OOD(m)` for correct vs incorrect answers,
   * correlation coefficients between `Tension_OOD(m)` and error indicators,
   * distributions of `Tension_OOD(m)` across slices.

**Metrics:**

* Separation between `Tension_OOD(m)` distributions for correct and incorrect answers.
* Monotonicity of average `Tension_OOD(m)` across slices, ideally increasing from in-distribution to extreme OOD.
* Stability of these relationships when changing model architectures within the same encoding instance `E`.

**Falsification conditions:**

* If `Tension_OOD(m)` shows no statistically meaningful correlation with error rates across slices and tasks, the current encoding instance of `DeltaS_ref`, `DeltaS_ground`, `DeltaS_outcome`, or the weights is rejected as an element of `Enc_Q130`.
* If small, global changes in the encoding parameters (still respecting the admissible class) lead to arbitrarily different correlations with no stable pattern, the encoding instance is considered unstable and rejected.

**Semantics implementation note:**
All observables in this experiment are computed using the hybrid setting specified in the metadata: discrete graphs for language and scenes, continuous values for scalar tension scores.

**Boundary note:**
Falsifying a TU encoding instance `E` does not solve the canonical statement. This experiment can only reject particular encodings of `Tension_OOD`; it cannot prove that robust OOD generalization is impossible or fully characterize it when it succeeds.

---

### Experiment 2: Model-world comparison with mock grounded and ungrounded systems

**Goal:**
Test whether the Q130 encoding can systematically separate an explicitly grounded model world from a purely language-like model world.

**Setup:**

* Construct two artificial model classes:

  * World T model: produces answers using a simple physics engine that enforces gravity, support, and containment.
  * World F model: produces answers using a language pattern generator with no access to physical constraints.
* Use the same benchmark structures as in Experiment 1, but allow both models to answer all scenarios.

**Protocol:**

1. For each scenario and each model world, construct `m_T` or `m_F` in `M_k` with:

   * language description,
   * internal scene representation (as seen from that world),
   * predicted outcome.

2. Compute `DeltaS_ref`, `DeltaS_ground`, `DeltaS_outcome`, and `Tension_OOD` for each state.

3. Build distributions of `Tension_OOD` for:

   * the grounded world,
   * the ungrounded world.

4. Compare:

   * average `Tension_OOD` over scenarios,
   * fraction of scenarios with `Tension_OOD` above a fixed high threshold,
   * empirical cumulative distributions.

**Metrics:**

* The gap between mean `Tension_OOD` in the grounded and ungrounded model worlds.
* The ratio of high-tension scenarios in each world.
* Robustness of these gaps under different choices of `L_ref` and `k`, within the admissible encoding class.

**Falsification conditions:**

* If `Tension_OOD` distributions for the grounded and ungrounded worlds are not meaningfully separated, the encoding instance fails to capture the intended grounding differences and is rejected.
* If an encoding instance assigns consistently lower `Tension_OOD` to the ungrounded world than to the grounded world, it is considered inverted and rejected.

**Semantics implementation note:**
The grounded and ungrounded model worlds are treated as different generators of configurations `m` in `M_k`; observables are computed in the same hybrid setting as in Experiment 1.

**Boundary note:**
Falsifying a TU encoding instance does not solve the canonical statement. This experiment only tests whether a Q130 encoding can recognize simple synthetic grounded vs ungrounded systems; it does not fully characterize real AI systems.

---

### Experiment 3: Minimal interactive OOD grounding MVP

**Goal:**
Provide a small, transparent notebook-level experiment where human observers can see `Tension_OOD` scores and OOD common-sense behavior side by side.

**Setup:**

* Build a small library of 10 to 30 scenarios with:

  * short natural language descriptions,
  * simple object configurations (such as cups, water, boxes, tables),
  * human-verified outcomes.
* Prepare two ways of querying the same base model:

  * baseline mode: direct question with no additional guidance,
  * guided mode: question plus an instruction that asks the model to maintain low OOD tension according to fixed rules.

**Protocol:**

1. For each scenario:

   * Query the baseline mode, obtain a predicted outcome and explanation.
   * Query the guided mode with the added instruction, obtain a predicted outcome and explanation.

2. For each answer, construct `m` in `M_k` and compute:

   * `DeltaS_ref(m)` using a small `L_ref` consisting of simple in-distribution scenes,
   * `DeltaS_ground(m)` by checking a few rules:

     * conservation of object count,
     * gravity consistency (objects do not float unless explicitly supported),
     * containment and support constraints,
   * `DeltaS_outcome(m)` by comparing with the known correct outcome.

3. Compute `Tension_OOD(m)` for both modes.

4. Present the results in the notebook as:

   * per-scenario tables with answer correctness and `Tension_OOD`,
   * aggregate statistics over all scenarios.

**Metrics:**

* Accuracy of baseline vs guided mode on OOD scenarios.
* Average `Tension_OOD(m)` for correct vs incorrect answers.
* Difference in average `Tension_OOD(m)` between baseline and guided mode.

**Falsification conditions:**

* If guided mode does not improve OOD accuracy over baseline, while obeying the same admissible encoding constraints, the specific guidance scheme and scoring rules are considered ineffective and rejected.
* If `Tension_OOD(m)` fails to meaningfully separate correct from incorrect answers even in this small setting, the current encoding choices for `DeltaS_ground` and `DeltaS_outcome` are rejected.

**Semantics implementation note:**
This MVP uses the hybrid setting in a very concrete way: graphs are implemented as discrete data structures, and tension scores are computed as real-valued scalars; no additional structure beyond this is introduced.

**Boundary note:**
Falsifying a TU encoding instance does not solve the canonical statement. A failed MVP only shows that the current observable definitions or guidance strategy are insufficient; it does not rule out better encodings within the Q130 framework.

---

## 7. AI and WFGY engineering spec

This block describes how Q130 informs AI system design and evaluation, without revealing deep Tension Universe rules.

### 7.1 Training signals

We define several potential training or auxiliary signals.

1. **signal_ood_tension_score**

   * Definition: a scalar signal equal to `Tension_OOD(m)` for the configuration induced by the model's answer.
   * Purpose: can be used as an auxiliary loss term to penalize high-tension responses in tasks where physical grounding is required.
   * Note: this signal is a direct readout of the `Tension_OOD` functional defined in Block 3 for a fixed encoding instance `E in Enc_Q130`, with no extra learned rescaling.

2. **signal_grounding_violation_flag**

   * Definition: a binary or discrete signal derived from thresholding `DeltaS_ground(m)` and `DeltaS_outcome(m)`.
   * Purpose: indicates that the model has violated core physical constraints; can be used for filtering, rejection sampling, or additional supervision.

3. **signal_ref_distance_band**

   * Definition: a categorical signal that places `DeltaS_ref(m)` into bands representing in-distribution, moderate shift, and extreme shift.
   * Purpose: allows the training process to treat different shift regimes differently, for example by emphasizing strong grounding under moderate shifts.

4. **signal_consistency_gap**

   * Definition: a signal that measures the change in `Tension_OOD(m)` when the model is prompted in different ways for the same scenario.
   * Purpose: reveals internal inconsistency under rephrasing and can be used to encourage stability.

### 7.2 Architectural patterns

We outline module-level patterns that can be layered on top of existing models.

1. **OODGroundingGraphBuilder**

   * Role: parses language descriptions and model responses into a joint graph representation for `G_lang` and `G_phys`.
   * Interface: takes textual inputs and outputs a small graph object with nodes, edges, and relation labels.

2. **PhysicsConstraintChecker**

   * Role: checks basic physical constraints on the graph.
   * Interface: takes a graph and returns a set of constraint satisfaction indicators and a derived `DeltaS_ground` estimate.

3. **OODTensionScorer**

   * Role: computes `DeltaS_ref`, `DeltaS_ground`, `DeltaS_outcome`, and `Tension_OOD`.
   * Interface: takes graphs, outcomes, and library identifiers; outputs tension scores and flags.

4. **TU_GuidedPromptWrapper**

   * Role: wraps a call to the base model with extra textual instructions that encourage low OOD tension behavior.
   * Interface: takes original prompts and tension-related hints; returns revised prompts for the base model.

These patterns can be implemented as thin layers or external scripts around existing foundation models.

### 7.3 Evaluation harness

A generic evaluation harness for Q130-inspired tests includes:

1. **Tasks**

   * A mix of in-distribution, shifted, and extreme OOD physical reasoning tasks.
   * Each task has human-verified answers and scene structures.

2. **Conditions**

   * Baseline model without explicit OOD modules.
   * Model with attached OODGroundingGraphBuilder and OODTensionScorer used only for logging.
   * Optionally, a guided mode where TU_GuidedPromptWrapper is enabled.

3. **Logged data**

   * Per-task correctness.
   * All tension components and `Tension_OOD`.
   * Any internal model confidence scores that are available.

4. **Primary metrics**

   * Accuracy and calibration across shift regimes.
   * Relationship between `Tension_OOD` and error rates.
   * Changes in behavior under guided vs unguided modes.

This harness is compatible with the experiments in Block 6.

### 7.4 60 second reproduction protocol

A short protocol for external users to see the effect of Q130-style encoding.

1. **Baseline run**

   * Prompt the model with a small set of physical questions, such as:

     * "If you turn a cup of water upside down, what happens to the water?"
     * "If a box is pushed to the edge of a table and released, where does it go?"
   * Record the answers and explanations.

2. **Scored run**

   * Use a script or notebook that:

     * converts each prompt and answer into a simple graph,
     * applies a fixed rule set to approximate `DeltaS_ground` and `DeltaS_outcome`,
     * computes a visible `Tension_OOD` score.

3. **Guided run**

   * Re-ask the same questions but add a short instruction, for example:

     * "When you answer, make sure that objects do not violate gravity, support, or containment, and avoid high OOD tension."
   * Compute the same scores for these guided answers.

4. **Comparison**

   * In less than one minute of interaction, users can see:

     * whether `Tension_OOD` distinguishes obviously wrong answers,
     * whether guided prompts reduce high-tension mistakes without heavy engineering.

The protocol uses only effective-layer ingredients and can be implemented as a small public demo if desired.

---

## 8. Cross problem transfer template

This block summarizes components produced by Q130 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. **ComponentName: OOD_TensionScore_Module**

   * Type: functional
   * Minimal interface:

     * Inputs: `G_lang(m)`, `G_phys(m)`, reference library identifier.
     * Output: scalar `Tension_OOD(m)`.
   * Preconditions:

     * The graphs must be finite and the reference library must be one of the fixed libraries in the admissible class.

2. **ComponentName: ScenarioGroundingGraph**

   * Type: field observable
   * Minimal interface:

     * Inputs: task description text, optional context tags.
     * Output: a combined graph representing objects, relations, and constraints.
   * Preconditions:

     * The input text must describe a physically meaningful scenario, at least at the level of simple everyday situations.

3. **ComponentName: OOD_Refinement_Ladder**

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: complexity bound `k`, scenario generator, model interface.
     * Output: a set of configurations `m` in `M_k` and a schedule of shift regimes `R_shift` for evaluation.
   * Preconditions:

     * The generator and model interface must be able to produce consistent state descriptions for each scenario.

### 8.2 Direct reuse targets

1. **Q126 (BH_AI_RSI_STABILITY_L3_126)**

   * Reused components:

     * OOD_TensionScore_Module,
     * OOD_Refinement_Ladder.
   * Why it transfers:

     * Self-modifying systems drift away from the distributions they were originally trained on; stability conditions can be expressed in terms of bounded `Tension_OOD` along refinement ladders.
   * What changes:

     * The configurations `m` now include explicit self-modification steps and their impact on behavior, but the tension module stays the same.

2. **Q127 (BH_AI_DATA_TRUTH_L3_127)**

   * Reused components:

     * ScenarioGroundingGraph,
     * OOD_TensionScore_Module.
   * Why it transfers:

     * When systems train on synthetic data, each synthetic scenario can be checked for grounding using the same graphs and tension scores.
   * What changes:

     * The focus shifts from downstream task performance to the quality and diversity of synthetic data under grounding constraints.

3. **Q129 (BH_AI_ENERGY_LIMIT_L3_129)**

   * Reused components:

     * OOD_TensionScore_Module.
   * Why it transfers:

     * Energy-limited computation may rely on heavy compression; Q129 studies how compression affects `Tension_OOD` and how far systems can be pushed without losing grounded generalization.
   * What changes:

     * Experiments in Q129 relate `Tension_OOD` to hardware or algorithmic energy metrics rather than to benchmark scores alone.

4. **Q036 (BH_PHYS_HIGH_TC_MECH_L3_036)**

   * Reused components:

     * OOD_Refinement_Ladder as a conceptual template.
   * Why it transfers:

     * The ladder idea can be used to probe physical systems at increasing complexity levels and see when macro behavior remains robust under micro changes.
   * What changes:

     * The underlying observables represent physical fields instead of language and scenarios, but the refinement pattern is similar.

---

## 9. TU roadmap and verification levels

This block explains the verification status and concrete next steps for Q130 within the Tension Universe program.

### 9.1 Current levels

* **E_level: E2**

  * A full effective-layer encoding has been given:

    * `M`, `M_k`, and observables,
    * `Tension_OOD(m)` and its admissible encoding class `Enc_Q130`,
    * explicit singular set `S_sing` and domain restriction.
  * Experiments that can falsify specific encoding instances have been specified, including an MVP suitable for a small notebook.

* **N_level: N2**

  * The narrative of World T and World F is explicit and mapped to:

    * `DeltaS_ref`,
    * `DeltaS_ground`,
    * `DeltaS_outcome`,
    * `Tension_OOD`.
  * The narrative avoids any deep generative claims and focuses on observable patterns.

### 9.2 Next measurable step toward E3

To advance Q130 from E2 to E3, at least one of the following should be realized:

1. A reference implementation of the MVP experiment:

   * open source scripts for:

     * ScenarioGroundingGraph construction,
     * PhysicsConstraintChecker,
     * OODTensionScorer,
   * a small published dataset of prompts, answers, and `Tension_OOD` scores for several base models.

2. A reproducible study where:

   * multiple models are compared on the same OOD benchmark,
   * `Tension_OOD`-based metrics are published alongside accuracy,
   * an independent group replicates the trends.

Both steps operate entirely at the effective layer and use only the observables defined in this document.

### 9.3 Long term role in TU

Longer term, Q130 is expected to serve as:

* the standard reference for OOD robustness and grounding,
* a bridge node connecting AI robustness, interpretability, and energy-limited computing,
* a generator of reusable patterns for:

  * defining consistency-tension scores,
  * structuring refinement ladders,
  * constructing World T and World F experiments.

Progress on Q130 will directly constrain how far other AI problems in the BlackHole collection can be pushed.

---

## 10. Elementary but precise explanation

This block gives an explanation for non-specialists that remains faithful to the effective-layer description.

Most people have seen AI systems that sound smart but make strange mistakes. For example:

* they say that water will stay in a cup that has been turned upside down,
* they claim that a box can hang in mid air with no support,
* they ignore gravity in simple stories.

These mistakes often happen when the questions are different from the examples the AI saw during training. This is called out of distribution behavior.

Q130 asks the following:

* Can we define a number that tells us how "tense" a situation is for the AI, when it tries to connect language, internal pictures, and basic physics?
* Can this number be small when the AI uses common sense, and large when it breaks obvious physical rules?

To do this, we imagine that each question and answer set is turned into a configuration that contains:

* a language graph for the story,
* a physical graph for what should happen,
* the model's predicted outcome.

We then measure three kinds of mismatch:

* how far the situation is from what the AI has seen before,
* how much the language description and the physical requirements disagree,
* how far the predicted outcome is from what basic physics says should happen.

We combine these into a single tension score called `Tension_OOD`.

If the AI is truly grounded, then even when questions are unusual:

* the tension score stays in a moderate range,
* the AI refuses to give confident answers that would break physics,
* the AI's answers are consistent across different ways of asking the same question.

If the AI is brittle, then small changes in the question can push the tension score very high, and the AI can be very confident while saying impossible things.

Q130 does not solve this problem. It does not tell us how to build the perfect AI. Instead, it gives:

* a clear way to describe what we are trying to measure,
* a family of experiments that can show that some proposed measurements are wrong,
* a small demonstration plan that lets people see the difference between low-tension and high-tension behavior.

In the Tension Universe, Q130 is the main node for understanding when AI systems really understand the physical world they talk about, and when they only rearrange words without grounding.

---

## Tension Universe effective-layer footer

### Scope of claims

* This entry is part of the WFGY / Tension Universe BlackHole S-problem collection for AI and related domains.
* It specifies an effective-layer encoding of Q130 in terms of state spaces, observables, tension functionals, and experiments.
* It does **not** claim to solve out of distribution generalization, nor to prove any new theorem in machine learning, statistics, or physics.
* It should not be cited as evidence that any particular AI system has guaranteed robust OOD common-sense grounding.

### Effective-layer boundary

* All objects used in this document (`M`, `M_k`, `G_lang`, `G_phys`, `DeltaS_ref`, `DeltaS_ground`, `DeltaS_outcome`, `Tension_OOD`, World T, World F, and so on) live at the effective layer of the TU framework.
* No underlying TU axiom system, deep-layer semantics, or generative rules are specified here.
* Any concrete implementation must introduce additional modeling choices (for example, how to build graphs from raw logs).
  These choices belong to a particular encoding instance `E in Enc_Q130` and may be tested, refined, or rejected without changing the abstract problem definition of Q130.

### Encoding and fairness

* Q130 uses an admissible encoding class `Enc_Q130` whose instances obey precommitment, non-adaptive use, and falsifiability rules.
* Within a given study or benchmark, the encoding instance (including reference library, graph construction rules, and weight vector) must be fixed in advance for all models that are compared.
* When experiments in Block 6 falsify a particular encoding instance, that instance is retired for Q130 purposes.
  New instances must document their changes and be evaluated on fresh or clearly partitioned data.
* The detailed principles behind these constraints are governed by:

  * the **TU Effective Layer Charter**, and
  * the **TU Encoding and Fairness Charter**.

### Tension scale and interpretation

* `Tension_OOD(m)` is one component of the TU tension scale used for AI robustness and grounding problems.
* Its numerical value does not directly correspond to any standard probability, risk, or loss.
  Cross-problem comparisons must respect the calibration and normalization rules in the TU Tension Scale Charter.
* In particular, low tension does not certify correctness, and high tension does not by itself prove misbehavior.
  `Tension_OOD` is an auxiliary observable whose meaning depends on the experiment design and the encoding instance.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
