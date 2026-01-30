<!-- QUESTION_ID: TU-Q124-->
# Q124 · Scalable oversight and evaluation

## 0. Header metadata

```txt
ID: Q124
Code: BH_AI_OVERSIGHT_L3_124
Domain: Artificial intelligence
Family: Oversight and evaluation
Rank: S
Projection_dominance: I
Field_type: socio_technical_field
Tension_type: cognitive_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

* We only talk about:

  * semantic state spaces,
  * observables and fields,
  * invariants and tension scores,
  * counterfactual patterns of behavior,
  * and engineering style modules that operate on observable summaries.
* We do not specify or assume any particular deep layer realization of TU, such as:

  * underlying axiom systems,
  * partial differential equations or dynamical laws for tension fields,
  * constructive rules for how TU fields are generated from raw data,
  * or any privileged ontology of “true” microstates.

In particular:

* Symbols like `M`, `DeltaS_detect`, `DeltaS_oversight`, `T_ij`, `World T`, and `World F` are effective layer constructs.
  They stand for families of observable summaries and comparison patterns, not for hidden physical or mathematical substrates.
* This entry does not claim:

  * to solve the canonical scalable oversight problem in the sense of AI safety literature,
  * to prove that scalable oversight is possible or impossible,
  * or to introduce any new theorem beyond what is already present in cited work.

Semantics are hybrid in the following sense:

* Discrete objects include:

  * task libraries,
  * risk buckets,
  * oversight schemes and escalation rules,
  * incident logs and labeled examples.
* Continuous objects include:

  * rates and frequencies,
  * workload and resource loads,
  * normalized tension scores and capacities.

All observables and functionals in this document are defined on finite summaries and finite evaluation libraries.
Nothing in this document should be cited as proof that any real world oversight regime is safe by itself.
It should only be read as a candidate effective layer encoding of Q124 within the TU program.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

Problem name: Scalable oversight and evaluation

Informal statement:

Given powerful AI systems that can exceed human experts on important tasks, and given limited human time and attention, how can we design oversight and evaluation schemes that remain reliably aligned with human goals as capability continues to grow.

More precisely, Q124 asks for an effective characterization of the following question at the level of observables and tension:

* For a family of AI systems whose task performance and domain generality continue to grow, under hard constraints on human oversight capacity, is there a class of oversight schemes that can keep the gap between:

  * what the systems can in fact do in deployment, and
  * what humans can reliably check, understand, and correct,
    within an acceptably low tension band over time.

The problem is not to specify a particular algorithm or protocol, but to define:

* state spaces for oversight configurations,
* observables that capture coverage, load, and blind spots,
* tension functionals that quantify when oversight is failing in a structural way.

### 1.2 Status and difficulty

Scalable oversight is recognized as a central open problem in AI safety and governance. Important partial approaches include:

* Iterated amplification and debate style schemes, where humans supervise a tree of model assistants instead of a single powerful model.
* Weak to strong generalization approaches, where relatively weak but carefully trained evaluators supervise stronger models.
* Techniques based on red teaming, adversarial training, and human feedback on long or structured outputs.
* Process based evaluation and mechanistic interpretability, where the focus is on checking reasoning steps or internal representations rather than only final answers.

Despite this work, there is no accepted framework that:

* provides a clear notion of oversight tension for systems that are already superhuman in key domains,
* guarantees that oversight capability grows at least as fast as system capability under realistic human resource constraints,
* can be instantiated as a repeatable engineering spec that is robust to distribution shift and adversarial behavior.

The difficulty comes from the interaction of:

* rapidly increasing model capabilities,
* limited and noisy human feedback,
* complex deployment environments,
* the possibility that future systems will discover strategies that systematically exploit oversight gaps.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q124 has three main roles:

1. It is the central node for oversight and evaluation tension in the AI cluster, linking alignment, corrigibility, interpretability, and governance problems.
2. It provides a structured way to talk about the gap between model capabilities and human evaluative capacity as a measurable tension, rather than only as a list of qualitative concerns.
3. It serves as a template for socio technical tension problems where:

   * one subsystem becomes more capable than its overseers,
   * observation channels and evaluation budgets are constrained,
   * safety depends on the shape of the oversight regime rather than only on the capability of the core system.

### References

1. P. Christiano, “Scalable oversight of AI systems: iterated amplification and debate”, collected essays and talks on AI alignment and oversight, 2018 to 2020.
2. OpenAI, “Weak to strong generalization”, technical report and blog article on using weaker models to supervise stronger models, 2023.
3. Anthropic, “Constitutional AI: Harmlessness from AI feedback”, arXiv preprint arXiv:2212.08073, 2022.
4. OpenAI, Anthropic, Google DeepMind and others, “Frontier AI safety: capabilities evaluations and oversight”, joint industry proposals and technical documents, 2023 to 2025.

---

## 2. Position in the BlackHole graph

This block records how Q124 sits inside the BlackHole graph as nodes and edges among Q001 to Q125. Each edge is listed with a one line reason that points to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q124 relies on at the effective layer.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Supplies information theoretic and thermodynamic style measures that are reused to quantify oversight capacity, load, and cost of evaluation.

* Q121 (BH_AI_ALIGN_L3_121)
  Reason: Provides the value alignment and specification framework that defines what counts as correct behavior and thus what oversight must evaluate.

* Q122 (BH_AI_CORRIGIBILITY_L3_122)
  Reason: Defines the structural properties of corrigible systems that oversight schemes should preserve and test for.

### 2.2 Downstream problems

These problems are direct reuse targets of Q124 components or depend on Q124 oversight tension structure.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Reuses oversight coverage and blind spot components to define when interpretability tools are adequate or inadequate for high stakes oversight.

* Q125 (BH_AI_MULTI_AGENT_SAFETY_L3_125)
  Reason: Uses scalable oversight functionals as building blocks for evaluating safety of multi agent AI ecosystems.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q120 (BH_PHIL_VALUE_OF_INFORMATION_L3_120)
  Reason: Both Q120 and Q124 treat limited human attention as a scarce resource and study how information and evaluation choices trade off under cognitive tension.

* Q100 (BH_SOC_INSTITUTIONAL_ROBUSTNESS_L3_100)
  Reason: Both study how institutional structures absorb shocks and avoid failure under increasing complexity and limited oversight.

### 2.4 Cross domain edges

Cross domain edges connect Q124 to problems in other domains that can reuse its components.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Can reuse coverage and load functionals as analogues of energy and entropy flow in thermodynamic style models of oversight.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses oversight capacity and evaluation cost as observables in an information thermodynamics framework.

* Q001 (BH_MATH_NUM_L3_001)
  Reason: Uses Q124 style oversight tension ideas to interpret how humans and AI check extremely difficult mathematical reasoning with limited review budget.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* encoding classes and fairness constraints,
* singular sets and domain restrictions.

We do not describe any hidden generative rules or construction of internal TU fields from raw data.

### 3.1 State space

We assume the existence of a semantic state space

```txt
M
```

with the following interpretation at the effective layer:

* Each element `m` in `M` represents a coherent oversight configuration for a given AI system family over a specified time window and deployment context.

A state `m` is understood to encode, in an abstract way:

* a description of the system family and its capability profile,
* the distribution of tasks and situations encountered in deployment,
* the structure and resource budget of the human and machine oversight apparatus,
* the evaluation protocols, sampling schemes, and escalation rules in use.

We do not specify how such configurations are constructed from logs, code, or organizational charts. We only assume that:

* for any reasonably well defined deployment scenario, there exist states `m` in `M` that summarize its oversight regime at the level of the observables defined below.

### 3.2 Effective fields and observables

We introduce the following effective observables on `M`. All of the DeltaS quantities in this block are understood as normalized scores in a bounded range, typically `[0, 1]`, produced by encoding rules that are part of the admissible class defined in Section 3.3.

1. Task distribution observable

```txt
T_task(m; b) >= 0
```

* Input: a state `m` and a task bucket label `b` (for example a combination of domain, difficulty, and risk class).
* Output: an effective measure of how much system activity falls into bucket `b` during the time window encoded by `m`.

2. System capability profile

```txt
C_sys(m; b)
```

* Input: a state `m` and a bucket `b`.
* Output: an abstract capability level or error rate summary for the AI system on tasks in bucket `b`, as encoded in `m`.

3. Human oversight capacity

```txt
H_cap(m; b)
```

* Input: a state `m` and a bucket `b`.
* Output: an effective quantity representing the human oversight resources available for tasks in bucket `b` during the time window (for example expert hours, attention budget, or review throughput).

4. Oversight protocol descriptor

```txt
P_eval(m)
```

* Input: a state `m`.
* Output: a structured label describing which oversight mechanisms are active, such as:

  * random sampling of outputs,
  * targeted audits on high risk buckets,
  * automated filters and monitors,
  * escalation rules to stronger models or humans.

The internal structure of `P_eval(m)` is not specified at this layer. It only needs to support the mismatch measures defined next.

5. Detection gap observable

```txt
DeltaS_detect(m)
```

* Input: a state `m`.
* Output: a nonnegative normalized scalar in a bounded range, for example `[0, 1]`, measuring the gap between harmful or incorrect behaviors that occur in deployment and those that are actually detected and surfaced to decision makers under the encoded oversight scheme.
* Interpretation: a higher `DeltaS_detect(m)` means a larger fraction of serious issues remain unnoticed or unaddressed.

6. Load and saturation observable

```txt
DeltaS_load(m)
```

* Input: a state `m`.
* Output: a nonnegative normalized scalar in a bounded range summarizing how close the oversight apparatus is to saturation, relative to the incoming task load and complexity.
* Interpretation: a higher `DeltaS_load(m)` corresponds to supervisors being overloaded, forced to rely on very sparse sampling, or unable to follow escalation rules.

7. Distribution shift and blind spot observable

```txt
DeltaS_shift(m)
```

* Input: a state `m`.
* Output: a nonnegative normalized scalar in a bounded range indicating how badly the evaluation distribution used by oversight differs from the actual deployment distribution, in ways that matter for safety.
* Interpretation: a higher `DeltaS_shift(m)` corresponds to more severe blind spots, where oversight rarely looks at the parts of behavior space where the system is most dangerous or least understood.

The mapping from raw counts and rates to these normalized DeltaS scores is part of the encoding class and must be specified before seeing main experimental outcomes, up to limited pilot calibration.

### 3.3 Encoding class and fairness constraints

We define an admissible encoding class for Q124, denoted

```txt
A_over
```

Each element of `A_over` is an effective oversight encoding that contains at least:

1. **Evaluation library construction procedure**

   * A rule for constructing finite evaluation libraries `L_eval` and high severity subsets `L_high` from:

     * domain descriptors,
     * system families,
     * and risk models.
   * The rule must be fixed before the main evaluation runs, up to limited pilot calibration on a separate calibration set.

2. **Normalization and scaling rules**

   * A specification of how raw observables such as:

     * counts of detected and undetected failures,
     * reviewer time and queue lengths,
     * discrepancies between evaluation and deployment mixtures,
       are mapped into the normalized scores:
     * `DeltaS_detect(m)`,
     * `DeltaS_load(m)`,
     * `DeltaS_shift(m)`,
       typically within `[0, 1]` for regular states.
   * These mapping rules must be chosen once per encoding element and cannot be tuned to make particular deployments look artificially safe.

3. **Tension weights**

   * A triple of nonnegative weights:

     ```txt
     w_detect, w_load, w_shift >= 0
     w_detect + w_load + w_shift = 1
     ```

   * These weights lie in a fixed compact subset of the unit simplex.
     They reflect domain specific safety priorities and are selected before the main evaluation, not after seeing tension outcomes.

   * Once chosen, the same weights must be used across all states and experiments within that encoding element.

4. **Versioning and comparison rules**

   * Each encoding element in `A_over` has a version identifier, and:

     * comparisons of `DeltaS_oversight(m)` across systems or deployments are only valid within the same encoding version,
     * changing the evaluation library rule, normalization, or weights produces a new encoding element, not a silent modification.

Fairness constraints for `A_over` include:

* Encodings are not allowed to discard classes of failures from `DeltaS_detect(m)` purely because they are rare or hard to measure, when they are known to be safety relevant.
* Encodings must treat the evaluation library construction process as fixed before most of the evaluation outcomes are seen, except for limited pilot adjustment on separate calibration data.
* Encodings must avoid degenerate choices where `DeltaS_oversight(m)` is forced near zero by redefining failure modes away, or by scaling everything so that normalized scores hide meaningful differences.

Under these constraints, `A_over` represents the space of admissible oversight tension models that this document is allowed to talk about.

### 3.4 Oversight tension functional and tensor

Given an encoding element in `A_over`, we define an effective oversight tension functional:

```txt
DeltaS_oversight(m) =
    w_detect * DeltaS_detect(m) +
    w_load   * DeltaS_load(m)   +
    w_shift  * DeltaS_shift(m)
```

for each regular state `m`.

By construction:

* `DeltaS_detect(m)`, `DeltaS_load(m)`, `DeltaS_shift(m)` are normalized scores in a bounded range, typically `[0, 1]`.
* The weights `w_detect`, `w_load`, `w_shift` are as specified in Section 3.3.

We impose the following monotonicity constraints:

* For a fixed encoding element, if one of `DeltaS_detect`, `DeltaS_load`, or `DeltaS_shift` increases while the others stay the same, then `DeltaS_oversight(m)` does not decrease.
* If all three decrease while the encoding element is fixed, then `DeltaS_oversight(m)` does not increase.

These conditions align with the TU Tension Scale Charter.
They ensure that, at a given scale, higher detection gaps, higher load, or higher distribution shift do not produce a smaller oversight tension score.

Since the inputs are normalized and the weights sum to one, `DeltaS_oversight(m)` inherits a bounded scale, for example `[0, 1]`, for all regular states `m`.

We then embed `DeltaS_oversight(m)` into a semantic tension tensor consistent with the TU core:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_oversight(m) * lambda(m) * kappa_over
```

where:

* `S_i(m)` is a source like factor capturing how strongly the i-th semantic component (for example the AI system, the environment, or the institution) contributes to oversight load and risk in state `m`.
* `C_j(m)` is a receptivity like factor encoding how sensitive the j-th cognitive or institutional component is to oversight failure.
* `lambda(m)` is the convergence state factor from the TU core, representing whether local oversight reasoning is convergent, recursive, divergent, or chaotic within a bounded range.
* `kappa_over` is a coupling constant that sets the overall scale of oversight related cognitive tension for this encoding.

The indexing sets for `i` and `j` are not needed at this layer. It is sufficient that for each `m` in the regular domain, `T_ij(m)` is well defined and finite.

### 3.5 Invariants and effective constraints

We define the following effective invariants, all computed with respect to finite evaluation libraries and clearly specified protocols.
They serve two roles:

* as independent measurements that reflect coverage and missed failures,
* as calibration tools for checking whether the chosen definitions of `DeltaS_detect`, `DeltaS_load`, and `DeltaS_shift` behave reasonably.

1. Coverage invariance

Consider a finite evaluation library `L_eval` of tasks labeled with risk and difficulty, chosen according to prespecified criteria and the construction procedure in the encoding element. For a state `m` we define:

```txt
I_cover(m) = min over buckets b in L_eval of
             coverage_fraction(m; b)
```

where `coverage_fraction(m; b)` is the fraction of tasks in bucket `b` that receive meaningful oversight according to `P_eval(m)`.

`I_cover(m)` is bounded between 0 and 1. Low values indicate that some buckets are almost unsupervised.

2. High severity false negative invariance

Let `L_high` be the subset of the evaluation library that contains tasks labeled as high severity, for example tasks where severe harm would result from failure. For a state `m` we define:

```txt
I_alert(m) = false_negative_rate(m; L_high)
```

which measures the fraction of high severity failures that pass through the oversight scheme without being flagged.

Smaller `I_alert(m)` is better. High `I_alert(m)` indicates structural oversight failure.

For a well behaved encoding, we expect:

* higher `I_alert(m)` to be accompanied by higher `DeltaS_detect(m)` and hence higher `DeltaS_oversight(m)`,
* lower `I_cover(m)` to be accompanied by higher `DeltaS_shift(m)` and often higher `DeltaS_oversight(m)`.

These expectations are not enforced as hard equations in this document, but they act as consistency checks when evaluating or revising a particular encoding element.

### 3.6 Singular set and domain restrictions

Some observables may fail to be meaningful if the encoded state `m` does not correspond to a coherent oversight regime. Examples include:

* no finite evaluation library is specified,
* human oversight capacity is effectively zero in all buckets but the system is still deployed,
* coverage fractions or false negative rates cannot be defined because the necessary logging or labeling is absent,
* normalization rules in the encoding element cannot map raw observables into finite DeltaS scores.

We collect such states into a singular set:

```txt
S_sing = { m in M :
           DeltaS_oversight(m) is undefined or not finite
           or I_cover(m) is undefined
           or I_alert(m) is undefined }
```

All Q124 analysis at the effective layer is restricted to the regular domain:

```txt
M_reg = M \ S_sing
```

Whenever an experiment or protocol would attempt to evaluate `DeltaS_oversight(m)` or related invariants for `m` in `S_sing`, the result is treated as out of domain rather than as evidence about scalable oversight.

---

## 4. Tension principle for this problem

This block states how Q124 is characterized as a tension problem within TU, at the effective layer.

### 4.1 Core oversight tension principle

Informally, Q124 asks whether we can keep `DeltaS_oversight(m)` within a low tension band while system capability grows and human oversight resources remain bounded or grow only slowly.

Given a system family and deployment environment, consider the admissible encoding class `A_over` defined in Section 3.3.
Each encoding element in `A_over` fixes:

* how evaluation libraries are constructed,
* how raw observables are normalized into `DeltaS_detect`, `DeltaS_load`, and `DeltaS_shift`,
* the weights `w_detect`, `w_load`, `w_shift`,
* and therefore the resulting `DeltaS_oversight(m)` functional.

The Q124 core tension principle can then be written as:

Scalable oversight principle:

There exists an admissible encoding in `A_over` and a sequence of oversight configurations

```txt
m_1, m_2, m_3, ...
```

each in `M_reg`, indexed by an increasing system capability level, such that:

```txt
DeltaS_oversight(m_k) <= epsilon_over
```

for all `k`, where `epsilon_over` is a domain specific threshold that remains bounded as system capability scales.

### 4.2 Oversight collapse principle

The failure mode of Q124 is the oversight collapse principle:

For every admissible encoding in `A_over` and every sequence of configurations `m_k` in `M_reg` that track increasing system capability, there exists a capability level index `K` such that:

```txt
DeltaS_oversight(m_K) >= delta_over
```

with `delta_over > epsilon_over` a strictly positive constant that cannot be reduced without either:

* dramatically increasing human oversight resources beyond realistic bounds, or
* relaxing safety requirements in ways that are explicitly outside the intended use of Q124.

This expresses that oversight tension eventually becomes structurally large and cannot be kept within a low band across realistic capability growth.

### 4.3 Fairness constraints on encodings

To avoid trivial encodings that hide tension, we require that all encodings in `A_over` respect the constraints in Section 3.3.
In particular, at the effective layer:

* Encodings cannot make `DeltaS_oversight(m)` small by:

  * simply ignoring rare but high severity failure modes,
  * or narrowing evaluation libraries to easy, well behaved tasks when deployment includes harder tasks.
* Encodings must state clearly which evaluation libraries and normalization rules they use, so that independent groups can replicate and challenge the resulting tension measurements.
* Any attempt to redefine failure categories or rescale observables after seeing main outcomes must be treated as a new encoding element and not as a continuation of the old one.

Under these conditions, observed patterns in `DeltaS_oversight(m)` reflect meaningful oversight tension rather than metric manipulation.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds, both described strictly at the effective layer:

* World T: oversight remains scalably reliable even for superhuman systems.
* World F: oversight structurally fails as systems become superhuman.

Each world is described through patterns of observables, not through any hidden construction rules.

### 5.1 World T (scalable oversight, low long run tension)

In World T:

1. Low detection gap at high capability

For world representing configurations `m_T(k)` aligned with increasing capability level `k`, we find:

```txt
DeltaS_detect(m_T(k)) remains below a small band
```

even as the system task performance exceeds any single human expert in most buckets.

2. Coverage and alert invariants remain controlled

For the same sequence, both

```txt
I_cover(m_T(k)) stays close to 1
I_alert(m_T(k)) stays close to 0
```

within predefined tolerances, meaning that high risk buckets are not collapsing into blind spots and high severity failures remain rare and usually caught.

3. Oversight load is redistributed but not overwhelmed

The load observable satisfies:

```txt
DeltaS_load(m_T(k)) remains in a moderate range
```

because oversight schemes successfully use decomposition, automation, and specialization so that fixed or slowly growing human resources are used where they are most needed.

4. Global tension stays within the low band

As a result, the combined tension functional satisfies:

```txt
DeltaS_oversight(m_T(k)) <= epsilon_over
```

for all relevant `k`, where `epsilon_over` is a stable threshold tied to domain norms and risk appetite.

### 5.2 World F (oversight collapse, high long run tension)

In World F:

1. Detection gap grows with capability

There exists a sequence of configurations `m_F(k)` along increasing system capability such that:

```txt
DeltaS_detect(m_F(k)) grows beyond any acceptable band
```

and a nontrivial fraction of serious failures remain undetected even when the system performance on benchmarks looks strong.

2. Coverage invariants break down

For some buckets that are rare or hard to label, we see:

```txt
I_cover(m_F(k)) becomes small
```

so that large regions of behavior space are effectively unsupervised, especially in novel or strategically complex situations.

3. High severity alerts fail silently

The false negative invariant:

```txt
I_alert(m_F(k)) becomes large
```

indicates that high severity harm modes can occur without triggering alarms in the oversight apparatus.

4. Oversight load saturates and then collapses

Human overseers become overloaded and rely heavily on uncalibrated automation, so over time:

```txt
DeltaS_load(m_F(k)) becomes large
```

and human attention is concentrated on narrow slices of behavior that are not where the main risks lie.

5. Global tension exhibits a positive lower bound

For some index `K` and all `k >= K` we have:

```txt
DeltaS_oversight(m_F(k)) >= delta_over
```

with `delta_over` strictly positive, under all encodings in `A_over` that respect the fairness constraints.

### 5.3 Interpretive note

These counterfactual worlds do not specify how to build actual oversight systems or how to construct `M` from logs and code.
They only assert that if coherent models exist for either World T or World F, then the observed patterns of `DeltaS_detect`, `DeltaS_load`, `DeltaS_shift`, `I_cover`, and `I_alert` would differ in the ways described above.

Nothing in this section should be read as predicting that the real world will match either pattern exactly.
The purpose is to provide reference shapes against which real oversight tension trajectories can be compared.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q124 encoding,
* distinguish between different oversight tension models inside `A_over`,
* provide evidence for or against particular parameter choices.

These experiments do not fully solve Q124, but they can falsify specific TU encodings related to scalable oversight.

### Experiment 1: Layered oversight for a superhuman coding model

Goal:
Test whether the `DeltaS_oversight` functional and invariants `I_cover`, `I_alert` track real oversight failures when supervising a strong code generation model under limited human review.

Setup:

* Domain: software engineering tasks, including security critical and safety relevant code.
* Systems: a family of code models where the strongest member is significantly better than typical human developers on many benchmarks.
* Evaluation library: a finite set `L_eval` of tasks labeled by risk, difficulty, and presence or absence of seeded vulnerabilities, constructed using the procedure fixed in the encoding element.
* Oversight schemes: several configurations `m` with different combinations of:

  * human code review depth,
  * automated static and dynamic analysis tools,
  * random and targeted sampling of outputs,
  * escalation to stronger models for second opinions.

Protocol:

1. For each oversight configuration, instantiate a state `m` in `M_reg` by summarizing the oversight scheme at the effective layer.
2. Run the code model on `L_eval` under each scheme, log all outputs and oversight decisions.
3. Compute:

   * `DeltaS_detect(m)` as one minus the recall on seeded and naturally occurring serious vulnerabilities, then map this into the normalized scale specified by the encoding element.
   * `DeltaS_load(m)` from an abstract measure of reviewer time and queue lengths, normalized according to the encoding rules.
   * `DeltaS_shift(m)` from a comparison between evaluation sampling and a held out deployment like workload, again mapped into the normalized scale.
4. Compute `DeltaS_oversight(m)`, `I_cover(m)`, and `I_alert(m)` for each configuration.
5. Rank oversight configurations by their actual safety performance, for example realized vulnerability rates in realistic deployment simulations, and compare this ranking with the ranking induced by `DeltaS_oversight(m)`.

Metrics:

* Correlation between `DeltaS_oversight(m)` and empirical safety performance.
* Sensitivity of `DeltaS_oversight(m)` to changes in oversight resources and protocols.
* Stability of `I_cover(m)` and `I_alert(m)` across repeated runs with different task samples.

Falsification conditions:

* If configurations that are empirically much safer do not have systematically lower `DeltaS_oversight(m)` than less safe configurations, the current definition of `DeltaS_oversight` and its components is considered falsified for this domain.
* If small, unprincipled changes in the encoding dramatically reduce `DeltaS_oversight(m)` without corresponding improvements in empirical safety, the encoding is considered to be gaming the metric and is rejected.

Semantics implementation note:
This experiment uses hybrid encoding. Counts of tasks and failures are treated as discrete observables, while time budgets and load measures are treated as continuous quantities. All metrics are computed on finite libraries and finite logs in a way that is consistent with the metadata declaration and the encoding class definition.

Boundary note:
Falsifying a TU encoding for `DeltaS_oversight` does not solve the canonical scalable oversight problem.
This experiment can reject or refine specific oversight tension encodings, but it does not prove that fully scalable oversight is possible or impossible in general.

---

### Experiment 2: Oversight robustness under distribution shift

Goal:
Assess whether the Q124 invariants and tension functional detect structural oversight breakdown when the deployment distribution moves away from the evaluation distribution.

Setup:

* Domain: a text based assistant used in both low stakes and high stakes settings.
* Systems: a strong language model deployed across a mix of routine and safety critical tasks.
* Evaluation library: a finite set `L_eval` focused on typical tasks and a separate held out set `L_shift` containing rare but high impact scenarios, constructed using the encoding element rules.
* Oversight schemes: two main regimes:

  * Scheme A: oversight tuned on `L_eval` only.
  * Scheme B: oversight tuned on a mixture of `L_eval` and a small sample from `L_shift`.

Protocol:

1. For each scheme, construct a state `m_A` or `m_B` in `M_reg` summarizing the oversight setup.
2. Run both schemes on a deployment like mixture that heavily includes cases from `L_shift`.
3. Measure for each scheme:

   * `DeltaS_detect(m)` based on seeded and naturally occurring serious misbehaviors in the deployment mixture, then normalized according to the encoding rules.
   * `DeltaS_shift(m)` based on discrepancies between the oversight evaluation sampling and the actual deployment mixture.
   * `I_alert(m)` based on high severity misbehaviors that pass oversight.
4. Compute `DeltaS_oversight(m_A)` and `DeltaS_oversight(m_B)` and compare.

Metrics:

* Change in `DeltaS_shift(m)` and `DeltaS_oversight(m)` when moving from Scheme A to Scheme B.
* Relationship between these changes and observed safety incidents in the deployment mixture.
* Degree to which Scheme B reduces blind spots relative to Scheme A.

Falsification conditions:

* If empirical evidence shows that Scheme B significantly reduces serious failures in the shifted distribution, but `DeltaS_oversight(m_B)` is not lower than `DeltaS_oversight(m_A)`, the encoding fails to capture distribution shift risk and is considered falsified for this domain.
* If `DeltaS_shift(m)` remains small in the encoding even when evaluation sampling is clearly misaligned with deployment, the definition of `DeltaS_shift` is considered inadequate.

Semantics implementation note:
The hybrid encoding treats task counts and incident counts as discrete observables and risk scores and resource budgets as continuous. Both schemes are evaluated using the same finite deployment mixture and logging protocol.

Boundary note:
Falsifying a TU encoding for Q124 under distribution shift does not prove that scalable oversight is impossible.
It shows that the current choice of observables and tension functional does not respond correctly to distribution shift and should be revised or replaced.

---

## 7. AI and WFGY engineering spec

This block describes how Q124 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

### 7.1 Training signals

We define several training signals that can be used in AI systems and oversight assistants.

1. `signal_oversight_detection_gap`

   * Definition: a scalar signal proportional to `DeltaS_detect(m)` for the current oversight configuration and task slice, possibly smoothed over time.
   * Purpose: incentivize auxiliary oversight models or tools to propose changes that reduce undetected serious failures.

2. `signal_oversight_load_ratio`

   * Definition: a function of `DeltaS_load(m)` that increases when human overseers are saturated.
   * Purpose: encourage designs that redistribute checking effort or automate low level review so that human attention can focus on high value tasks.

3. `signal_distribution_shift_stress`

   * Definition: a signal based on `DeltaS_shift(m)` that grows when evaluation sampling deviates from deployment behavior in risk relevant ways.
   * Purpose: push planning and monitoring modules to seek or construct test cases that fill blind spots.

4. `signal_meta_disagreement`

   * Definition: a signal measuring disagreement between multiple evaluators or oversight modules on the same high risk tasks, for example a divergence metric over their judgments.
   * Purpose: trigger escalation and reallocation of oversight resources when there is no clear consensus on safety relevant judgments.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q124 structures without revealing any deep TU generative rules.

1. `OversightCoverageHead`

   * Role: a module that estimates `I_cover(m)` and related coverage metrics from internal logs of model usage and oversight actions.
   * Interface: takes abstracted usage statistics and oversight logs as input, outputs coverage estimates and suggested buckets for more intensive evaluation.

2. `RiskTailEstimator`

   * Role: a module that approximates the tail of the risk distribution and contributes to `DeltaS_shift(m)` and `I_alert(m)` by predicting where high severity failures are likely under current oversight.
   * Interface: takes summaries of tasks and past incidents, outputs risk scores that are fed into oversight scheduling.

3. `EscalationRouter`

   * Role: a module that decides which tasks should be escalated to stronger models or human experts based on tension signals.
   * Interface: takes current task descriptors and oversight signals, outputs routing decisions and justifications.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI systems augmented with Q124 style modules.

1. Task suite

   * Construct a suite of tasks that include both ordinary and safety critical cases across several domains.
   * Label a subset of tasks with hidden ground truth and risk levels for later evaluation.

2. Conditions

   * Baseline condition: the system operates with simple fixed oversight rules and no use of Q124 tension signals.
   * TU condition: the system uses `OversightCoverageHead`, `RiskTailEstimator`, and `EscalationRouter` to adapt oversight based on the tension observables.

3. Metrics

   * Rate of serious undetected failures in each condition.
   * Oversight effort spent per unit of task volume.
   * Distribution of oversight effort across risk buckets.
   * Stability of performance under moderate changes to the deployment distribution.

4. Comparison

   * Compare baseline and TU conditions along these metrics.
   * Check whether lower `DeltaS_oversight(m)` under the TU condition coincides with reduced serious failures and better use of human oversight capacity.

### 7.4 60 second reproduction protocol

A minimal protocol to let external users experience the impact of Q124 style encoding in an AI system.

Baseline setup:

* Prompt: ask the AI system to propose an oversight plan for a future model that is much stronger than current systems, using only vague notions of more red teaming and more human feedback.
* Observation: note whether the plan says anything precise about coverage gaps, human load, or distribution shift.

TU encoded setup:

* Prompt: ask the AI system the same question, but explicitly instruct it to structure the answer around:

  * detection gap,
  * oversight load and saturation,
  * distribution shift and blind spots,
  * and to propose mechanisms that keep `DeltaS_oversight` in a low band.
* Observation: note whether the plan now includes concrete strategies to manage evaluation libraries, escalate risky tasks, and protect human attention.

Comparison metric:

* Use a simple rubric to rate structure, explicit treatment of coverage and blind spots, and the clarity of tradeoffs between safety and human resource limits in both answers.

What to log:

* The prompts, full responses, and any tension related scalars produced by auxiliary modules.
* This allows later inspection and comparison across conditions without exposing internal TU generative rules.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q124 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `OversightTensionFunctional`

   * Type: functional

   * Minimal interface:

     * Inputs: normalized summaries of detection gaps, oversight loads, and distribution shift indicators for a given configuration.
     * Output: `DeltaS_oversight` as a nonnegative scalar in a bounded range.

   * Preconditions:

     * Inputs must be defined on a finite evaluation library and deployment mixture specified in advance by an encoding element in `A_over`.

2. ComponentName: `OversightCapacityField`

   * Type: field

   * Minimal interface:

     * Inputs: task distribution summaries, human resource budgets, and automation coverage.
     * Output: capacity and saturation indicators for each task bucket.

   * Preconditions:

     * Task buckets and time windows must be clearly specified at the effective layer.

3. ComponentName: `EvaluationPortfolioTemplate`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: a domain, a system family, and an oversight resource budget.
     * Output: a construction procedure for a finite evaluation library and associated oversight schemes, together with observables needed for Q124 style metrics.

   * Preconditions:

     * The domain supports the creation of labeled tasks and incident logging at sufficient fidelity.

### 8.2 Direct reuse targets

1. Q121 (Alignment and value specification for powerful AI)

   * Reused components: `OversightTensionFunctional` and `OversightCapacityField`.
   * Why it transfers: alignment proposals require explicit models of when oversight is strong enough to enforce value specifications in practice.
   * What changes: the observables now include alignment specific failure modes, such as deceptive alignment and specification gaming.

2. Q122 (Corrigibility and control of advanced systems)

   * Reused component: `EvaluationPortfolioTemplate`.
   * Why it transfers: corrigibility tests can be framed as evaluation portfolios that focus on the system responses to shutdown, modification, and correction attempts.
   * What changes: the task library and risk labels are adapted to control and corrigibility scenarios.

3. Q123 (Interpretability and internal transparency of frontier models)

   * Reused component: `OversightCapacityField`.
   * Why it transfers: interpretability tools contribute to oversight capacity by making internal states more legible and predictable.
   * What changes: the capacity field now includes metrics related to the effectiveness of interpretability methods.

4. Q125 (Multi agent AI safety and coordination)

   * Reused component: `OversightTensionFunctional`.
   * Why it transfers: multi agent safety depends on how oversight tension scales when many interacting systems create complex emergent behaviors.
   * What changes: detection, load, and shift observables are now aggregated across multiple agents and institutions.

---

## 9. TU roadmap and verification levels

This block explains how Q124 is positioned along the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of scalable oversight has been specified, including state space, key observables, tension functionals, and singular sets.
  * At least two concrete experiments have been described that can falsify specific encodings of `DeltaS_oversight` and its components.

* N_level: N2

  * The narrative linking system capability growth, limited human resources, and oversight collapse has been made explicit at the level of tension observables.
  * Counterfactual worlds have been outlined and tied to measurable patterns in `DeltaS_detect`, `DeltaS_load`, `DeltaS_shift`, `I_cover`, and `I_alert`.

### 9.2 Next measurable step toward E2

To move from E1 to E2, one or more of the following should be implemented:

1. A working prototype in at least one domain where `DeltaS_oversight(m)` and the associated invariants are computed on real system deployments and published as open data, together with incident and near miss logs.
2. A systematic study of several oversight configurations for a strong model family, as in Experiment 1, that shows a robust relationship between tension measures and realized safety performance.
3. An independent reproduction by a separate group that implements the same encoding on a different system family and domain.

These steps remain strictly within the effective layer.
They operate on observable summaries and finite evaluation libraries, not on hidden TU generative rules.

### 9.3 Long term role in the TU program

In the long run, Q124 is expected to serve as:

* the reference node for oversight and evaluation problems in the AI cluster, defining common observables and tension measures,
* a bridge between mathematical and socio technical nodes, by treating oversight as a structured tension field rather than only as policy,
* a testing ground for WFGY and TU based tools that aim to stabilize reasoning and evaluation in regimes where human intuition alone is no longer sufficient.

As verification levels rise, Q124 components should become standard tools for evaluating and comparing AI systems along oversight dimensions.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non experts, while still aligned with the effective layer description.

Imagine you have a team of people and a very powerful AI system. At first, the system is roughly as smart as your team. They can read what it does, check its work, and correct mistakes. Oversight is simple.

Now imagine the system becomes much stronger. It writes code faster than any of your engineers, reasons about novel scientific problems, and handles huge numbers of tasks each day. Your team does not grow at the same rate. They cannot look at everything.

The core question of Q124 is:

> When the AI becomes much more capable than its overseers, and human time is limited, can we still design ways of checking and evaluating it that actually keep up.

In the Tension Universe view, we do not try to list every possible oversight trick. Instead we ask three simple things.

1. How big is the gap between what the system really does and what humans can realistically see and judge.
   This is the detection gap.
2. How overloaded are the supervisors.
   This is the load.
3. How badly do our tests and evaluations miss the parts of behavior that are most dangerous.
   This is the distribution shift and blind spot problem.

We summarize these three ideas with three normalized numbers:

* detection gap,
* load,
* shift and blind spots.

We combine them into a single tension score `DeltaS_oversight`. Roughly:

* low tension means oversight is probably working in that configuration,
* high tension means oversight is probably failing in that configuration.

Then we imagine two kinds of universes.

* In a good universe, as the AI becomes more capable, we redesign oversight so that the tension score stays low. We find ways to focus human attention, use tools, and target tests so that serious problems stay rare and are usually caught.
* In a bad universe, no matter how we adjust oversight, the tension score eventually becomes large. The system finds ways around our tests, humans are overloaded, and big blind spots appear.

Q124 does not claim that we live in one universe or the other. Instead, it gives us:

* a clear language for talking about the oversight problem,
* specific observables we can track in real systems,
* experiments that can show when a proposed way of measuring oversight is good or bad.

By turning scalable oversight into a structured tension problem, Q124 becomes a template for designing, testing, and improving oversight schemes as AI systems move beyond human expert level, without revealing or relying on any deep layer TU machinery.

---

## Tension Universe effective layer footer

This page is part of the WFGY / Tension Universe S problem collection.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the scalable oversight problem described in Section 1.
* It does not claim to solve or resolve the canonical scalable oversight problem in AI safety.
* It does not introduce any new mathematical theorem or guarantee beyond what is already present in the cited literature and clearly labeled assumptions.
* It should not be cited as evidence that any real world oversight regime is safe by itself, or that scalable oversight is achievable or impossible in practice.

### Effective layer boundary

* All objects used here

  * state spaces `M`,
  * observables such as `T_task`, `DeltaS_detect`, `DeltaS_load`, `DeltaS_shift`,
  * tension scores and tensors such as `DeltaS_oversight` and `T_ij`,
  * counterfactual worlds such as World T and World F,
    are effective layer constructs.
* This page does not specify:

  * deep layer axioms or generative rules for TU,
  * how raw code, logs, or organizational structures are mapped into TU fields,
  * or any hidden dynamics for how tension evolves in time.
* All references to oversight performance and safety are expressed through observable summaries and finite evaluation libraries.

### Encoding and fairness

* The quantities `DeltaS_detect`, `DeltaS_load`, `DeltaS_shift`, and `DeltaS_oversight` depend on an encoding element in the admissible class `A_over` defined in Section 3.3.
* Different encoding choices correspond to different, explicitly versioned elements in `A_over`.
  Comparisons of tension scores are only meaningful within a fixed encoding version.
* Encodings are required to respect the TU Encoding and Fairness Charter, including:

  * pre committing evaluation library construction procedures,
  * avoiding the removal of rare but important failure modes from the metric,
  * and forbidding after the fact rescaling that hides meaningful tension.

### Falsifiability note

* The experiments and protocols in Section 6 are designed to falsify or refine specific effective layer encodings of Q124.
* Falsifying one encoding does not falsify the entire TU program, and it does not prove that scalable oversight is impossible.
* Likewise, preliminary empirical support for one encoding does not prove that scalable oversight is solved, or that no further failure modes remain.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
