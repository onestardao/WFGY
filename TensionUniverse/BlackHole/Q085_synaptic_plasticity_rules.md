# Q085 · General rules of synaptic plasticity

## 0. Header metadata

```txt
ID: Q085
Code: BH_NEURO_PLASTICITY_RULES_L3_085
Domain: Neuroscience
Family: Synaptic plasticity and learning rules
Rank: S
Projection_dominance: M
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-25
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q085 can be stated as follows:

> Are there general rules of synaptic plasticity that describe how synapses change their strength in response to activity, in a way that is sufficiently universal across brain regions, cell types, and species to count as genuine "laws" of learning in the brain, while remaining compatible with stability, biophysical constraints, and behavioral function?

More concretely, the question asks:

1. Whether synaptic changes can be summarized by a relatively small set of rule templates, such as:
   - Hebbian like rules ("cells that fire together wire together"),
   - spike timing dependent plasticity (STDP),
   - three factor rules involving pre, post, and modulatory signals,
   - homeostatic and metaplasticity mechanisms.
2. Whether these templates can be applied across many circuits without causing instability or loss of function.
3. How these rules balance local information (pre and post activity) with global constraints (energy, safety, network performance).

The "general rules" need not be identical in every synapse. The question is whether there is a compact family of rule types and parameters that account for most synaptic changes observed in healthy nervous systems.

### 1.2 Status and difficulty

Empirically, many types of synaptic plasticity have been observed:

- long term potentiation (LTP),
- long term depression (LTD),
- timing dependent rules (STDP),
- rate based plasticity,
- neuromodulator gated learning,
- homeostatic synaptic scaling,
- metaplasticity (plasticity of plasticity).

However:

- These phenomena vary widely across brain regions, cell types, and developmental stages.
- Detailed rules often depend on experimental conditions (for example spike timing windows, firing rates, neuromodulatory context).
- Simple textbook rules are often only approximate descriptions.

The difficulty of the problem is that:

1. It is not clear whether all of this diversity can be compressed into a small family of rule templates without losing essential structure.
2. Any proposed general rule must be checked against:
   - the need for long term network stability,
   - limitations on energy and molecular resources,
   - the ability to support learning across many tasks and timescales.

There is no accepted "final" theory that captures synaptic plasticity as a small set of general laws with the same status as, for example, Ohm's law in simple electrical circuits.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q085 serves as:

1. The central node for how local synaptic changes are organized and constrained by global function in the brain.
2. A bridge between:
   - Q083 (neural coding and representations),
   - Q084 (memory storage and retention),
   - Q089 (predictive coding and inference),
   - Q087 (neurodegeneration and breakdown of plasticity).
3. A template for framing adaptation rules in AI systems:
   - learning rule design,
   - stability under continual learning,
   - analogies to alignment and oversight constraints in artificial agents.

In the Tension Universe view, Q085 is the place where "local learning rules" are explicitly tied to tension between:

- local synaptic dynamics,
- circuit stability,
- task performance,
- and biophysical limits.

### References

1. Kandel ER, Schwartz JH, Jessell TM, Siegelbaum SA, Hudspeth AJ. Principles of Neural Science. 5th edition. McGraw Hill, 2013. Chapters on synaptic plasticity and learning (for example Chapter 67).
2. Caporale N, Dan Y. Spike timing dependent plasticity: a Hebbian learning rule. Annual Review of Neuroscience. 2008;31:25 46.
3. Turrigiano GG, Nelson SB. Homeostatic plasticity in the developing nervous system. Nature Reviews Neuroscience. 2004;5(2):97 107.
4. Gerstner W, Kistler WM, Naud R, Paninski L. Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition. Cambridge University Press, 2014. Chapters on synaptic plasticity and learning rules.

---

## 2. Position in the BlackHole graph

This block records how Q085 sits inside the BlackHole graph among Q001–Q125. Each edge is listed with a one line reason pointing to a concrete component or tension pattern.

### 2.1 Upstream problems

These problems provide prerequisites or background frameworks that Q085 depends on at the effective layer.

- Q081 (BH_NEURO_CONSCIOUS_HARD_L3_081)  
  Reason: Sets global constraints on what kinds of neural processes must ultimately support conscious experience, which plasticity rules need to respect at scale.

- Q083 (BH_NEURO_CODE_L3_083)  
  Reason: Defines neural coding schemes that plasticity rules must read and transform when updating synaptic weights.

- Q084 (BH_NEURO_MEMORY_STORE_L3_084)  
  Reason: Specifies memory storage and retention requirements that general plasticity rules must satisfy in order to avoid catastrophic forgetting or instability.

### 2.2 Downstream problems

These problems directly reuse components or depend on Q085's tension structure.

- Q087 (BH_NEURO_DEGEN_DISEASE_L3_087)  
  Reason: Reuses SynapticStabilityIndex and PlasticityRuleSignature to model how plasticity failures lead to neurodegenerative changes.

- Q089 (BH_NEURO_PREDICTIVE_CODE_L3_089)  
  Reason: Uses PlasticityRuleSignature and PlasticityWorldTemplate to define how predictive coding updates are implemented in synapses.

- Q090 (BH_NEURO_SOC_BRAIN_L3_090)  
  Reason: Depends on general plasticity rules to explain how social cognition and higher order circuits adapt over development and experience.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

- Q082 (BH_NEURO_BINDING_L3_082)  
  Reason: Both study consistency_tension between local neural events and global coherent patterns, but Q082 focuses on feature binding, while Q085 focuses on weight changes.

- Q088 (BH_NEURO_DEV_PATTERN_L3_088)  
  Reason: Both examine how local rules give rise to organized structure, but Q088 focuses on developmental pattern formation rather than ongoing learning.

### 2.4 Cross domain edges

Cross domain edges connect Q085 to problems in other domains that can reuse its components.

- Q057 (BH_CS_RL_GENERALIZATION_L3_057)  
  Reason: Uses PlasticityRuleSignature as a biological template for reinforcement learning update rules and their generalization limits.

- Q121 (BH_AI_ALIGNMENT_L3_121)  
  Reason: Applies SynapticStabilityIndex like measures to constrain long term parameter updates in aligned AI systems.

- Q124 (BH_AI_OVERSIGHT_L3_124)  
  Reason: Reuses PlasticityWorldTemplate as an experiment pattern for oversight of powerful adaptive AI that continuously updates internal parameters.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

- state spaces,
- effective fields and observables,
- invariants and tension quantities,
- singular sets and domain restrictions.

We do not describe any hidden generative rules or any mapping from raw biological data to internal TU fields.

### 3.1 State space

We posit a state space:

```txt
M
```

with the following interpretation:

- Each state `m` in `M` represents a "plasticity world snapshot" at the scale of:
  - a local population or microcircuit,
  - over a finite observation window.

For each state `m` we assume the existence of:

1. A description of synaptic weight changes over that window for a selected set of synapses.
2. A summary of pre and post neuronal activity patterns and relevant modulatory signals in that window.
3. A coarse description of circuit level function during and shortly after that window (for example whether firing statistics and basic behavioral outputs remain within acceptable ranges).

We do not specify how biological recordings, simulations, or models are encoded into `m`. We only require that:

- For each experimental or model context of interest, there exist states in `M` that encode the required summaries in a well defined way.

### 3.2 Hybrid field implementation

Because the metadata semantics are hybrid, we conceptually split each `m` into:

1. A continuous part:
   - synaptic weights and their changes,
   - average firing rates over time bins,
   - real valued modulatory levels,
   - aggregated measures of stability and task performance.

2. A discrete part:
   - individual spike event times,
   - discrete trial events,
   - categorical labels for context or task conditions.

The effective observables below are defined as functions of these continuous and discrete parts, but we do not expose any rule for constructing those parts from raw data. The coupling is assumed to proceed through simple interfaces such as:

- counting spikes in time windows,
- averaging rate like quantities,
- aggregating over finite sets of synapses or neurons.

### 3.3 Effective observables and fields

We introduce the following effective observables on `M`. All are real valued, bounded, and defined on a regular subset described below.

1. Plasticity rule signature

```txt
RuleSignature(m; region) in R^k_sig
```

- Input: a state `m` and a labeled region or cell population.
- Output: a low dimensional vector that summarizes which plasticity rule template best describes synaptic changes in that region during the observation window.
- Examples of template features:
  - sensitivity to pre vs post firing rates,
  - dependence on precise spike timing,
  - presence of neuromodulator gating,
  - strength of homeostatic components.
- We assume a finite library of templates and a fixed mapping from observed changes to this signature.

2. Synaptic stability index

```txt
StabilityIndex(m; circuit) in [0, 1]
```

- Input: a state `m` and a labeled circuit or network.
- Output: a scalar index where:
  - values near 1 indicate high stability under continued application of observed plasticity rules,
  - values near 0 indicate that continued application leads to runaway excitation, quiescence, or loss of function over relevant timescales.
- Defined through a standardized stability test applied to the encoded circuit summaries.

3. Task generalization score

```txt
GeneralizationScore(m; task_family) in [0, 1]
```

- Input: a state `m` and a family of related tasks or inputs.
- Output: a scalar describing how well the observed plasticity rules support learning across that task family without major retuning.

4. Biophysical feasibility index

```txt
BioFeasibility(m; region) in [0, 1]
```

- Input: a state `m` and a region or preparation.
- Output: a scalar describing how compatible the implied synaptic changes are with known biophysical constraints such as:
  - resource limits,
  - receptor trafficking rates,
  - structural remodeling bounds.
- Values near 1 indicate good compatibility; values near 0 indicate strong tension with known limits.

### 3.4 Tension quantities

We define three nonnegative tension quantities on the regular domain.

1. Local global consistency tension

```txt
DeltaS_local_global(m) >= 0
```

- Measures mismatch between:
  - the local RuleSignature across synapses in the circuit,
  - and the global StabilityIndex.
- Constructed so that:
  - small values occur when a simple local rule template coexists with high circuit stability,
  - large values occur when local rules imply instability or require fine tuned global corrections.

2. Generalization tension

```txt
DeltaS_generalization(m) >= 0
```

- Measures the tension between:
  - the simplicity of the effective rule templates encoded in RuleSignature,
  - and the GeneralizationScore across the task family.
- Small values: simple rules generalize well.
- Large values: either rules are complex and overfitted, or simple rules perform poorly.

3. Biophysical constraint tension

```txt
DeltaS_biophysical(m) >= 0
```

- Measures mismatch between:
  - implied synaptic changes per unit time,
  - and BioFeasibility indices.
- Small values: rules operate comfortably within known constraints.
- Large values: rules would require sustained changes incompatible with known biology.

### 3.5 Singular set and domain restrictions

Some encodings or contexts can lead to ill defined or unbounded observables. We therefore define:

```txt
S_sing = { m in M :
           at least one of
           RuleSignature, StabilityIndex,
           GeneralizationScore, BioFeasibility,
           DeltaS_local_global, DeltaS_generalization,
           DeltaS_biophysical
           is undefined or not finite }
```

and the regular domain:

```txt
M_reg = M \ S_sing
```

All tension analysis for Q085 is restricted to `M_reg`. If an experimental or model state maps into `S_sing`, this is treated as "out of domain" for this encoding and not as evidence about whether general plasticity rules exist.

---

## 4. Tension principle for this problem

This block states how Q085 is represented as a tension problem in TU, purely at the effective layer.

### 4.1 Core plasticity tension functional

We define a combined plasticity tension functional:

```txt
Tension_plasticity(m) =
    w_local_global * DeltaS_local_global(m)
  + w_generalization * DeltaS_generalization(m)
  + w_bio * DeltaS_biophysical(m)
```

with the following constraints:

- `w_local_global`, `w_generalization`, `w_bio` are nonnegative real numbers.
- They satisfy `w_local_global + w_generalization + w_bio = 1`.
- The triple `(w_local_global, w_generalization, w_bio)` is fixed in advance as part of this encoding and does not depend on the particular state `m` or on the experimental data used later.

This functional is required to satisfy:

- `Tension_plasticity(m) >= 0` for all `m` in `M_reg`.
- `Tension_plasticity(m)` is small when all three component tensions are small.
- `Tension_plasticity(m)` becomes large if any component remains large despite reasonable attempts to adjust rule templates within a predefined library.

### 4.2 Admissible rule template library

To avoid trivial tuning, we fix in advance a finite library:

```txt
L = { L_1, L_2, ..., L_K }
```

of plasticity rule templates, where:

- Each `L_k` specifies a simple parametric form for how synaptic weights change as a function of local pre, post, and modulatory variables.
- The number `K` and the functional forms of `L_k` are chosen once and then held fixed for all subsequent experiments within this encoding.
- Rule parameters inside each `L_k` may vary within bounded ranges to capture known biological diversity, but the template family is not expanded or redesigned to fit individual datasets.

RuleSignature is defined so that each state `m` is effectively associated with one or a small mixture of templates from `L` together with parameter ranges, and the tension quantities are computed relative to this fixed template library.

### 4.3 Q085 as a low tension principle

At the effective layer, Q085 is encoded as the claim that:

> There exists a nontrivial region of `M_reg` representing real biological circuits and tasks, in which the combined tension functional `Tension_plasticity(m)` remains within a low band when evaluated with respect to the fixed template library `L` and fixed weights `(w_local_global, w_generalization, w_bio)`.

More concretely, there should exist states `m_bio` in `M_reg` representing real circuits such that:

```txt
Tension_plasticity(m_bio) <= epsilon_plasticity
```

for a small threshold `epsilon_plasticity` that reflects the precision of the encoding. This low tension should remain attainable:

- across multiple brain regions and species,
- across multiple task families,
- without changing the finite library `L` or the weight triple.

### 4.4 Failure as persistent high plasticity tension

The opposite possibility is that, even after reasonable optimization of parameters within the fixed library `L`, we find that:

```txt
Tension_plasticity(m_bio) >= delta_plasticity
```

for all states `m_bio` representing real circuits in the sense of this encoding, where `delta_plasticity` is a strictly positive lower bound that cannot be reduced by better data or modest refinement of parameter estimates.

In that case, this specific TU encoding of "general rules of synaptic plasticity" would be falsified. This would not prove that no general rules exist in reality, but it would indicate that this particular template library and tension decomposition cannot capture them.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds at the effective layer:

- World T: general plasticity rules exist and are well captured by a small template family.
- World F: plasticity is fundamentally fragmented and resists such compression.

Both are described by patterns of observables and tensions, not by any deep generative mechanism.

### 5.1 World T: rule like plasticity world

In World T:

1. Template compression

   - A small subset of templates in `L` explains most observed RuleSignature patterns across many circuits and species.
   - Diversity exists but is structured around these main template families.

2. Local global alignment

   - For typical states `m_T` representing healthy circuits, `DeltaS_local_global(m_T)` is small.
   - Local synaptic updates implied by RuleSignature are consistent with high StabilityIndex values.

3. Task generalization

   - For a wide range of task families, `GeneralizationScore(m_T; task_family)` is high while RuleSignature remains within the fixed template family.
   - `DeltaS_generalization(m_T)` stays low for many tasks without large changes in templates.

4. Biophysical compatibility

   - BioFeasibility remains high for plasticity regimes that support learning, and `DeltaS_biophysical(m_T)` stays low over long timescales.

5. Overall tension

   - There exist states `m_T` with `Tension_plasticity(m_T)` in a narrow low tension band across many contexts.

### 5.2 World F: idiosyncratic plasticity world

In World F:

1. Template fragmentation

   - RuleSignature patterns vary so widely that no small subset of templates in the fixed library `L` can capture them without large residuals.
   - Attempts to compress plasticity into a compact rule family lead to high mismatch.

2. Local global mismatch

   - For typical states `m_F`, local RuleSignature patterns imply instability unless aggressive, ad hoc global corrections are deployed.
   - `DeltaS_local_global(m_F)` remains large for many realistic activity regimes.

3. Poor generalization

   - High GeneralizationScore can only be achieved with sharply different templates or parameter settings for each task, leading to high `DeltaS_generalization(m_F)` when using a shared rule family.

4. Biophysical stress

   - Many plausible rule configurations that yield learning would require sustained synaptic changes that are incompatible with known biophysical limits, leading to high `DeltaS_biophysical(m_F)`.

5. Overall tension

   - For all reasonable states `m_F` and parameter choices inside the fixed library, `Tension_plasticity(m_F)` stays above a significant lower bound, indicating persistent high tension.

### 5.3 Interpretive note

These worlds do not claim that we can fully simulate all biological detail. They only assert that if real circuits behave as in World T or World F, then, under this encoding:

- World T maps into a region of `M_reg` where low tension states exist and are common.
- World F maps into `M_reg` where high tension states are unavoidable, given the fixed library and weights.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

- test the coherence of the Q085 encoding,
- discriminate between rule like and idiosyncratic plasticity patterns at the effective layer,
- falsify specific choices of template library and weights.

They do not prove or disprove the existence of ultimate biological laws. They only accept or reject this particular encoding.

### Experiment 1: Cross region template compression

*Goal:*  
Test whether a fixed finite library of plasticity templates can account for observed synaptic changes across many brain regions with low local global tension.

*Setup:*

- Data:
  - Collect published or newly acquired plasticity measurements from multiple brain areas, species, and preparations.
  - Each dataset should include pre and post activity measures, neuromodulatory context, and observed synaptic changes.
- Fixed encoding choices:
  - Choose the finite template library `L` and the weight triple `(w_local_global, w_generalization, w_bio)` before analyzing the datasets.
  - Define RuleSignature, StabilityIndex, and DeltaS_local_global according to this encoding, without dataset specific modifications.

*Protocol:*

1. For each dataset and region, construct a state `m_data` in `M_reg` that summarizes:
   - RuleSignature based on fitting one or more templates in `L`,
   - StabilityIndex based on network level analyses or models guided by the data.
2. Compute `DeltaS_local_global(m_data)` for each state.
3. Aggregate results across regions and species into a distribution of local global tension values.
4. Optionally stratify by region type, cell class, or developmental stage.

*Metrics:*

- Distribution of `DeltaS_local_global(m_data)` across all states.
- Fraction of states with `DeltaS_local_global(m_data)` below a chosen tolerance band.
- Variation of these quantities across regions and species.

*Falsification conditions:*

- If, for the fixed `L` and weights, a large majority of states show high `DeltaS_local_global(m_data)` beyond a pre specified tolerance, and this cannot be reduced by parameter tuning within each template, then this encoding of general rules is rejected at the effective layer.
- If local global tension behaves erratically between very similar regions or species without a clear structural reason, the RuleSignature and StabilityIndex definitions are considered misaligned and must be revised or discarded.

*Semantics implementation note:*  
All variables are treated as hybrid signals: discrete spike events and trial markers are aggregated into continuous rate like and summary statistics, which then feed into the state space `M` and the observables defined in Block 3.

*Boundary note:*  
Falsifying TU encoding != solving canonical statement. This experiment can reject this particular encoding of general plasticity rules but does not prove that no general rules exist.

---

### Experiment 2: Stability under ongoing learning in model circuits

*Goal:*  
Evaluate whether synaptic plasticity templates from the fixed library `L` can support stable ongoing learning in realistic model circuits without producing high tension or collapse.

*Setup:*

- Construct or select several model circuits:
  - recurrent networks with biologically plausible connectivity and activity regimes,
  - parameter ranges for synaptic weights and firing thresholds.
- For each circuit:
  - Implement one or more templates from `L` as the synaptic update rule.
  - Define a family of tasks or input statistics for the circuit to learn.

*Protocol:*

1. For each circuit and template choice, run the model under ongoing learning for a long sequence of epochs with realistic activity statistics.
2. Periodically construct states `m_model` encoding:
   - RuleSignature (from the instantiated template and parameters),
   - StabilityIndex (based on activity boundedness and functional performance),
   - GeneralizationScore (on held out tasks),
   - BioFeasibility (based on constraints like average weight magnitude and update rates).
3. Compute `DeltaS_local_global(m_model)`, `DeltaS_generalization(m_model)`, and `DeltaS_biophysical(m_model)` at each checkpoint.
4. Track `Tension_plasticity(m_model)` over learning time.

*Metrics:*

- Time series of `Tension_plasticity(m_model)` for each circuit template pair.
- Proportion of learning runs that remain in a low tension band throughout training.
- Failure modes:
  - runaway activity or quiescence,
  - catastrophic forgetting,
  - violations of biophysical constraints.

*Falsification conditions:*

- If for most circuits and tasks, all templates in `L` lead to runs where `Tension_plasticity(m_model)` frequently or persistently exceeds a pre defined upper bound, then the encoding is considered inconsistent with stable ongoing learning.
- If small variations in template parameters cause extreme swings in tension or stability with no clear structural reason, the encoding is treated as poorly conditioned and rejected in its current form.

*Semantics implementation note:*  
Model circuits are simulated with discrete time steps and spikes, but observables and tension quantities are computed from continuous approximations (for example average firing rates, weight statistics) consistent with the hybrid field interpretation in Block 3.

*Boundary note:*  
Falsifying TU encoding != solving canonical statement. The experiment can reject particular template libraries or weight choices but does not establish a final answer to whether general biological rules exist.

---

## 7. AI and WFGY engineering spec

This block describes how Q085 can be used as an engineering module for AI systems inside the WFGY framework, at the effective layer.

### 7.1 Training signals

We define several training or regularization signals inspired by the observables of Q085.

1. `signal_plasticity_stability`

   - Definition: a penalty proportional to an AI analogue of `DeltaS_local_global`, computed from:
     - the relation between internal "weight update proposals",
     - and a stability measure for the system after applying them.
   - Purpose: discourage update rules that preserve task performance only by relying on fragile or unstable dynamics.

2. `signal_rule_sharing_across_tasks`

   - Definition: a measure of how similar the effective update rules are across related tasks, adjusted by a performance term.
   - Purpose: encourage reuse of a small family of update templates when generalization remains good, analogous to low `DeltaS_generalization`.

3. `signal_update_bio_analogue`

   - Definition: a soft constraint that penalizes sustained very large or very frequent internal parameter changes, in analogy to `DeltaS_biophysical`.
   - Purpose: encourage learning rules that achieve good performance without extreme per step changes.

4. `signal_plasticity_world_consistency`

   - Definition: a measure of how consistent the model's own explanations of its update behavior are with a fixed template family, when probed as a "plasticity world".
   - Purpose: provide a self consistency check on adaptive behavior.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q085 components without exposing any deep TU generative rules.

1. `TU_SynapticUpdateHead`

   - Role: maps internal representations and gradient like signals into:
     - update directions for parameters,
     - an estimated internal RuleSignature,
     - a stability proxy that approximates StabilityIndex.
   - Interface:
     - Inputs: latent state, task context, candidate gradients.
     - Outputs: proposed parameter update, rule signature vector, stability score.

2. `TU_HomeostaticController`

   - Role: maintains long term bounds on effective weights or activations based on analogues of BioFeasibility.
   - Interface:
     - Inputs: moving averages of parameter norms and activations.
     - Outputs: small corrective factors that nudge the system back into a safe regime.

3. `TU_PlasticityProbe`

   - Role: diagnostic module that constructs approximate RuleSignature, GeneralizationScore, and tension quantities given logs of updates and performance.
   - Interface:
     - Inputs: history of updates, tasks, and performance metrics.
     - Outputs: proxy values for Q085 observables and a scalar AI tension estimate.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models augmented with Q085 inspired modules.

1. Task selection

   - A suite of continual learning and multi task benchmarks where:
     - the model must adapt over time,
     - catastrophic forgetting and instability are common risks.

2. Conditions

   - Baseline:
     - conventional optimization and learning without explicit Q085 constraints.
   - TU augmented:
     - same base model, but with TU_SynapticUpdateHead and TU_HomeostaticController, plus Q085 derived signals included in the objective.

3. Metrics

   - Stability:
     - fraction of training runs that remain stable (no divergence, no collapse of performance).
   - Generalization:
     - performance on held out tasks or distribution shifts after long adaptation.
   - Plasticity tension:
     - tracked analogue of `Tension_plasticity` computed from logs via TU_PlasticityProbe.

4. Outcome

   - The goal is not to mimic biology exactly, but to test whether viewing updates through the Q085 lens gives more stable and interpretable adaptive behavior.

### 7.4 60 second reproduction protocol

A minimal protocol to let external users experience the effect of Q085 style constraints in an AI system.

- Baseline setup

  - Prompt an AI system to design an update rule for continual learning across several tasks without any reference to biological plasticity.
  - Ask it to comment on expected stability and generalization qualitatively.

- TU encoded setup

  - Prompt the same system, but now request:
    - an update rule described in terms of local vs global information,
    - explicit discussion of stability, generalization, and biophysical analogue constraints,
    - a simple scalar plasticity tension estimate for the proposed rule.

- Comparison metric

  - Human evaluators rate:
    - clarity of assumptions,
    - explicitness about stability and constraints,
    - degree to which the rule could be monitored over time.

- What to log

  - Both sets of prompts and responses,
  - any internal tension estimates,
  - post hoc success or failure of the proposed rules in toy implementations.

These logs can later be analyzed as "AI plasticity worlds" and scored using Q085 like observables.

---

## 8. Cross problem transfer template

This block describes the main reusable components produced by Q085 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `PlasticityRuleSignature`

   - Type: field
   - Minimal interface:
     - Inputs: summaries of synaptic changes, local activity statistics, and modulatory context.
     - Output: a finite dimensional vector indicating which plasticity template from a fixed library best describes the data.
   - Preconditions:
     - Inputs must be drawn from a context where synaptic changes and activity can be reliably summarized.

2. ComponentName: `SynapticStabilityIndex`

   - Type: functional
   - Minimal interface:
     - Inputs: summaries of network activity and connectivity over a learning period.
     - Output: a scalar in [0, 1] indicating the degree of stability under continued learning.
   - Preconditions:
     - The network must be sufficiently well characterized to estimate the impact of continued updates.

3. ComponentName: `PlasticityWorldTemplate`

   - Type: experiment_pattern
   - Minimal interface:
     - Inputs: a class of circuits or models and a family of candidate plasticity rules.
     - Output: a standardized experiment design for assessing tension quantities (local global, generalization, biophysical) over time.
   - Preconditions:
     - The circuits or models must expose enough observables to construct the Q085 observables at the effective layer.

### 8.2 Direct reuse targets

1. Q084 (Long term memory storage and retention)

   - Reuses: `PlasticityRuleSignature`, `SynapticStabilityIndex`.
   - Why it transfers: long term memory requires that plasticity both store information and preserve stability over long timescales, which these components help quantify.
   - What changes: observables are computed over longer time windows and with memory specific performance criteria.

2. Q087 (Neurodegenerative disease mechanisms)

   - Reuses: `SynapticStabilityIndex`, `PlasticityWorldTemplate`.
   - Why it transfers: many disease hypotheses involve maladaptive plasticity and breakdown of stability; these components quantify how far circuits move into high tension regimes.
   - What changes: additional observables for degeneration markers and structural loss are added.

3. Q089 (Predictive coding in the brain)

   - Reuses: `PlasticityRuleSignature`.
   - Why it transfers: predictive coding schemes require a match between error signals and synaptic updates; the signature field captures which rule templates are compatible with such schemes.
   - What changes: task families focus on prediction error reduction and inference quality.

4. Q121 (AI alignment under continual adaptation)

   - Reuses: `SynapticStabilityIndex`, `PlasticityWorldTemplate`.
   - Why it transfers: alignment can be seen as a constraint on how update rules move internal states; these components are used as analogues for safe adaptation.
   - What changes: observables operate on AI parameter updates and alignment metrics instead of biological synapses.

---

## 9. TU roadmap and verification levels

This block places Q085 along the TU verification ladder and outlines next steps.

### 9.1 Current levels

- E_level: E1

  - A coherent effective encoding of "general rules of synaptic plasticity" has been specified.
  - State space, observables, tension quantities, and a combined tension functional are defined on a regular domain `M_reg` with an explicit singular set.
  - At least one discriminating experiment with falsification conditions is provided.

- N_level: N1

  - The narrative clearly separates:
    - local synaptic dynamics,
    - global stability and performance,
    - biophysical constraints.
  - Rule like and idiosyncratic worlds are distinguished in terms of observable tension patterns.

### 9.2 Next measurable step toward E2

To reach E2, at least one of the following should be implemented:

1. An instantiated template library `L` with:
   - explicit functional forms for a small number of plasticity rules,
   - parameter ranges informed by empirical data,
   - open source code for mapping data summaries into RuleSignature and tension quantities.

2. A pilot study applying Experiment 1 to:
   - a curated meta dataset of plasticity experiments,
   - with published distributions of `DeltaS_local_global` and associated conclusions about compression into a small number of templates.

3. A set of model circuit experiments based on Experiment 2, demonstrating:
   - how different template choices affect stability and generalization,
   - how `Tension_plasticity(m_model)` behaves over long adaptation.

These steps remain within the effective layer, as they work only with observables and encoded summaries.

### 9.3 Long term role in the TU program

In the long term, Q085 is expected to serve as:

- The reference node for all problems in the cluster where:
  - local learning rules,
  - global behavior,
  - and long term safety must be jointly considered.
- A bridge between biological and artificial learning rule design, providing:
  - a language for discussing update rules as tension balancing mechanisms,
  - a set of reusable metrics for stability and generalization.
- A template for other domains where "local update rules under global constraints" are central, such as:
  - social learning systems,
  - institutional adaptation,
  - large scale AI training regimes.

---

## 10. Elementary but precise explanation

Synaptic plasticity is the process by which connections between neurons get stronger or weaker when they are used. Without it, brains could not learn or adapt.

Over many years, scientists have found many different kinds of plasticity:

- some depend on how often neurons fire,
- some depend on the exact timing of spikes,
- some depend on chemicals that signal reward or attention,
- some act slowly to keep overall activity in a safe range.

The big question in Q085 is:

> Are there a few general rules that really describe how all these changes work, or is every synapse doing something different?

In the Tension Universe view, we do not try to guess the hidden mechanisms in detail. Instead, we ask:

- For a given circuit, can we describe its plasticity by a simple rule template?
- Does that rule keep the circuit stable when learning goes on for a long time?
- Does it let the circuit handle many tasks without needing a new rule for each one?
- Does it stay within what biology can realistically support?

We turn these questions into numbers:

- a "signature" that says which rule template is being used,
- a stability score between 0 and 1,
- a generalization score between 0 and 1,
- a feasibility score between 0 and 1,
- and a combined tension value that is small when everything fits nicely and large when something is wrong.

Then we consider two kinds of worlds:

- In a rule like world, a small set of rule templates works well across many circuits and tasks, and the tension stays low.
- In an idiosyncratic world, any small set of templates fails, and the tension stays high no matter how you tune within that set.

This way of looking at synaptic plasticity does not prove what the true rules are. It gives us:

- a clear way to say what we mean by "general rules",
- a way to test whether a proposed family of rules is good enough,
- and a set of tools that can also be used to design and monitor learning rules in AI systems.

Q085 is therefore the place where "how connections change" is turned into a structured tension problem that links neuroscience and AI without exposing any deep hidden TU machinery.

