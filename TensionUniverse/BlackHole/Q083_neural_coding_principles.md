# Q083 · Neural coding principles

## 0. Header metadata

```txt
ID: Q083
Code: BH_NEURO_CODE_L3_083
Domain: Neuroscience
Family: Neural coding and representation
Rank: S
Projection_dominance: I
Field_type: cognitive_field
Tension_type: computational_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-25
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem of neural coding asks:

How does the brain encode information in patterns of neural activity across time and populations, such that these patterns support perception, action, learning, and cognition?

More concretely, the questions include:

* What variables are represented by neurons and neural populations, for example sensory features, motor commands, internal states.
* What code families are used, for example firing rates, precise spike timing, synchrony, population patterns, low dimensional manifolds.
* How reliable and efficient these codes are, given biological noise, metabolic cost, and anatomical constraints.
* How codes are transformed across stages of processing and across brain areas.

Despite many partial answers in specific systems, there is no consensus unified set of neural coding principles that explains coding across modalities, species, and scales.

### 1.2 Status and difficulty

Current knowledge includes:

* Detailed case studies where specific neurons or populations encode particular sensory features or motor variables.
* Formal theories such as efficient coding, redundancy reduction, sparse coding, and predictive coding, which explain aspects of sensory representations under certain conditions.
* Information theoretic analyses that quantify the amount of information carried by spikes or population activity about defined stimuli or tasks.
* Experimental evidence that neural codes can be flexible and context dependent, changing with attention, learning, or behavioral state.

Difficulties include:

* High dimensionality and noise in neural activity.
* Limited sampling of neurons relative to the full population.
* Complex, nonstationary relationships between activity, stimuli, and internal variables.
* Multiple candidate code families that can explain the same data within error bars.

As a result, the existence and nature of a small set of general coding principles remains an open problem in neuroscience.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q083 plays several roles:

1. It is the primary node for questions where information is carried by biological activity patterns under strong resource and noise constraints, with **computational_tension** as the main tension type.
2. It provides a structured way to describe neural codes as effective fields and observables that can be compared across brain regions, tasks, and species.
3. It feeds downstream problems that depend on coding, such as memory storage (Q084), plasticity rules (Q085), and social cognition (Q090), and it provides biological templates for AI representation and interpretability questions (Q123).

### References

1. Rieke F, Warland D, de Ruyter van Steveninck R, Bialek W, “Spikes: Exploring the Neural Code”, MIT Press, 1997.
2. Dayan P, Abbott LF, “Theoretical Neuroscience: Computational and Mathematical Modeling of Neural Systems”, MIT Press, 2001.
3. Bialek W, “Biophysics: Searching for Principles”, Princeton University Press, 2012.
4. Simoncelli EP, Olshausen BA, “Natural image statistics and neural representation”, Annual Review of Neuroscience, 2001.
5. “Unsolved problems in neuroscience”, standard encyclopedia entry, section on coding and representation problems, accessed 2026.

---

## 2. Position in the BlackHole graph

This block places Q083 within the BlackHole graph as a node with upstream, downstream, parallel, and cross domain edges. Each edge has a single line reason tied to concrete components or tension types.

### 2.1 Upstream problems

These problems provide foundations and constraints that Q083 must respect.

* Q081 (BH_NEURO_CONSCIOUS_HARD_L3_081)
  Reason: Defines the broader space of conscious states that neural codes must at least be capable of supporting as effective representations.
* Q082 (BH_NEURO_BINDING_L3_082)
  Reason: Provides constraints on how distributed coded features must bind into unified percepts that any coding principle must allow.
* Q078 (BH_BIO_DEVELOPMENTAL_L3_078)
  Reason: Limits possible coding architectures by what biological development can reliably construct and maintain.
* Q088 (BH_NEURO_DEV_PATTERN_L3_088)
  Reason: Supplies effective constraints from cortical maps and developmental patterning on which population codes are biologically reachable.

### 2.2 Downstream problems

These problems reuse Q083 components or depend directly on its coding tension structures.

* Q084 (BH_NEURO_MEMORY_STORE_L3_084)
  Reason: Reuses the NeuralCodeField and CodeEfficiencyFunctional components to define what kinds of representations can be stably stored.
* Q085 (BH_NEURO_PLASTICITY_RULES_L3_085)
  Reason: Uses CodeEfficiencyFunctional as a target for plasticity, where synaptic changes seek to reduce coding tension.
* Q090 (BH_NEURO_SOC_BRAIN_L3_090)
  Reason: Builds high level social representations on top of lower level population codes described by NeuralCodeField.
* Q123 (BH_AI_INTERP_L3_123)
  Reason: Uses CrossContextCodeGraph and related components as blueprints for interpreting internal AI representations as codes.

### 2.3 Parallel problems

Parallel nodes share similar tension types but have no direct component reuse at this stage.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Both Q032 and Q083 involve physical systems that carry information under thermodynamic and noise constraints, with computational_tension patterns constrained by energy and entropy.
* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Both formulate tradeoffs between information processing, energy cost, and robustness as computational_tension problems.
* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Internal AI goal codes and their stability can be analyzed using code tension ideas parallel to those in biological neural coding.

### 2.4 Cross domain edges

Cross domain edges link Q083 to non neuroscience nodes that can reuse its components.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Can reuse CodeEfficiencyFunctional as a template for mapping between coding efficiency and energetic cost in physical substrates.
* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses the notion of Tension_code as a functional balancing accuracy, robustness, and cost in engineered information systems.
* Q101 (BH_ECON_EQUITY_PREMIUM_L3_101)
  Reason: Agent internal codes for risk and reward can conceptually reuse NeuralCodeField and CrossContextCodeGraph structures.
* Q125 (BH_AI_MULTI_AGENT_DYN_L3_125)
  Reason: Multi agent internal representations can reuse population code descriptors and cross context tension measures from Q083.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is strictly at the effective layer. It describes state spaces, observables, invariants, tension scores, and singular sets. It does not describe any deep TU generative rules or mappings from raw data to internal TU fields.

### 3.1 State space

We assume a semantic state space

`M`

with elements `m` that represent coherent “neural coding configurations” at the effective layer.

For each `m` in `M`, we assume:

* A finite set of neurons or neural populations `N(m)` is in focus.
* A finite time window `T(m)` is considered, with resolution fine enough to distinguish relevant temporal patterns.
* For each neuron or population in `N(m)` and each time bin in `T(m)`, there exists an effective activity descriptor.

We do not specify how these descriptors are computed from raw spike trains or continuous voltage traces. We only assume that such summarizing descriptors exist and can be treated as well defined quantities in the effective model.

### 3.2 Effective activity observables

We define activity observables that map each state `m` to summaries of neural activity.

1. Single unit activity

```txt
A_single(m; n, t)
```

* Input: state `m`, neuron index `n` in `N(m)`, time bin `t` in `T(m)`.
* Output: scalar that encodes effective activity at that neuron and time, for example spike count or normalized firing rate.

2. Population activity

```txt
A_pop(m; P, t)
```

* Input: state `m`, subset `P` of `N(m)`, time bin `t`.
* Output: vector or low dimensional descriptor summarizing collective activity of `P` at time `t`.

3. Context labels

```txt
Cxt(m; k)
```

* Input: state `m`, context index `k`.
* Output: descriptor specifying the stimulus condition, task variable, or internal state relevant for this configuration.

These observables are assumed to be well defined for all regular states in `M`, but we do not prescribe their construction from data.

### 3.3 Code field descriptors

We define effective code field descriptors that attempt to capture structured coding motifs.

1. Rate code descriptor

```txt
C_rate(m; n)
```

* Summarizes the dependence of average activity of neuron `n` on context labels across `T(m)`.
* For example, tuning curves or low order statistics of `A_single` over contexts and time.

2. Temporal code descriptor

```txt
C_temp(m; n, window)
```

* Captures temporal structure in the spike or activity pattern of neuron `n` within a time window.
* For example, inter spike interval patterns or phase relationships relative to an oscillatory reference.

3. Population code descriptor

```txt
C_pop(m; P)
```

* Summarizes joint activity in a subset `P` of neurons, for example low dimensional manifolds, principal components, or pattern dictionaries.
* It is treated as a structured object at the effective layer without specifying any particular algorithm.

These descriptors allow us to talk about code families such as rate codes, temporal codes, and population codes without committing to a particular implementation.

### 3.4 Information observables

We introduce coarse information theoretic observables at the effective layer.

1. Stimulus information

```txt
I_stim(m)
```

* Represents mutual information between defined stimulus variables and neural activity descriptors in the configuration `m`.
* Treated as a scalar that can be estimated in principle from stimuli and `A_single` or `A_pop`.

2. Task information

```txt
I_task(m)
```

* Represents mutual information between task relevant variables, for example decisions or rewards, and neural activity descriptors in `m`.

3. Code cost

```txt
C_cost(m)
```

* Represents an effective resource cost associated with maintaining and using the neural code in `m`, for example metabolic expenditure or wiring cost.

We do not specify estimators, only the existence of such effective quantities.

### 3.5 Mismatch observables and combined code tension

We define mismatch observables that compare actual codes to reference families.

1. Structural mismatch

```txt
DeltaS_struct(m)
```

* Nonnegative scalar that measures deviation of observed code descriptors `C_rate`, `C_temp`, `C_pop` from a chosen reference code family, for example sparse linear codes or smooth manifold codes.
* `DeltaS_struct(m) = 0` if the descriptors lie exactly within the reference family under the encoding.

2. Noise robustness mismatch

```txt
DeltaS_noise(m)
```

* Nonnegative scalar that measures how much performance or information degrades under noise injections relative to predicted robustness from the reference code family.

3. Resource mismatch

```txt
DeltaS_resource(m)
```

* Nonnegative scalar that measures deviation of observed code cost `C_cost(m)` from a target cost range predicted by efficient coding or related principles.

We fix an admissible encoding class `E_code` that specifies:

* Which reference code families are allowed.
* Which parameter ranges are allowed when fitting these families.
* How the mismatch quantities above are computed, at least at the level of which summaries they depend on.

For any encoding within `E_code`, we define fixed positive weights:

```txt
w_struct, w_noise, w_resource > 0
w_struct + w_noise + w_resource = 1
```

These weights must be chosen before running any experiment that uses this encoding and remain fixed for that encoding.

The combined coding tension is then defined by:

```txt
Tension_code(m) =
    w_struct   * DeltaS_struct(m) +
    w_noise    * DeltaS_noise(m) +
    w_resource * DeltaS_resource(m)
```

for all regular states `m` in `M`.

### 3.6 Singular set and domain restriction

Some states may be ill posed for coding analysis, for example if activity descriptors are missing or inconsistent so that mismatch quantities cannot be evaluated.

We define the singular set:

```txt
S_sing = { m in M :
           DeltaS_struct(m) is undefined
           or DeltaS_noise(m) is undefined
           or DeltaS_resource(m) is undefined }
```

We then define the regular domain:

```txt
M_reg = M \ S_sing
```

All code tension analysis at the effective layer is restricted to `M_reg`. Whenever a protocol would need `Tension_code(m)` for `m` in `S_sing`, the result is treated as out of domain and not as evidence about coding principles.

---

## 4. Tension principle for this problem

This block states how Q083 is characterized as a tension problem in TU.

### 4.1 Core coding tension functional

The core coding tension functional is the `Tension_code(m)` defined above. It captures a tradeoff between three aspects:

* How well structured the code is relative to some principled family.
* How robust the code is to noise and perturbations.
* How well the code respects resource constraints.

For regular states `m` in `M_reg`:

```txt
Tension_code(m) >= 0
```

Small values of `Tension_code(m)` indicate codes that are close to a chosen principled family, robust, and resource compatible. Large values indicate codes that deviate strongly in at least one of these respects.

### 4.2 Coding principles as low tension regimes

At the effective layer, candidate neural coding principles can be phrased as statements of the form:

For the actual brain and for appropriate context classes, there exist encoding choices in `E_code` and regular states `m_true` in `M_reg` such that:

```txt
Tension_code(m_true) <= epsilon_code
```

where `epsilon_code` is a small threshold that depends on the resolution of the analysis and the complexity of the task, but does not grow without bound as more data are included.

In words:

* Good coding principles are those for which plausible encodings exist that keep code tension uniformly low over a wide set of tasks and conditions.

### 4.3 Failure of coding principles as persistent high tension

If a proposed coding principle is fundamentally mismatched to how the brain actually encodes information, then for any encoding in `E_code` respecting that principle and remaining faithful to observational constraints, world representing states `m_world` would eventually exhibit persistent high tension:

```txt
Tension_code(m_world) >= delta_code
```

for some `delta_code > 0` that cannot be driven toward zero by refining the analysis, as long as the encoding stays in `E_code` and respects the data.

In words:

* Failed coding principles show up as families of encodings for which tension remains high or even grows when we look at more precise and diverse data.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds at the effective layer.

* World T: the brain uses coherent, relatively simple coding principles with low coding tension.
* World F: the brain uses heterogeneous, poorly organized codes with high coding tension.

These worlds are patterns of observables, not constructive rules.

### 5.1 World T: coherent coding principles

In World T:

1. Code structure

   * For a wide range of tasks and modalities, there exist encodings in `E_code` such that:

     ```txt
     DeltaS_struct(m_T) is small
     ```

     for states `m_T` that summarize recorded activity and context.

2. Noise robustness

   * When noise levels in inputs or internal processes are changed within a realistic range, `DeltaS_noise(m_T)` stays small or grows in ways predicted by efficient coding or similar theories.

3. Resource compatibility

   * The resource mismatch `DeltaS_resource(m_T)` remains within narrow bands compatible with metabolic and wiring constraints.

4. Global coding tension

   * For these states, the combined tension satisfies:

     ```txt
     Tension_code(m_T) <= epsilon_code
     ```

     across multiple tasks and modalities, with `epsilon_code` not exploding as data quality or diversity increases.

### 5.2 World F: ad hoc coding patterns

In World F:

1. Code structure

   * For many tasks and modalities, no encoding in `E_code` yields small `DeltaS_struct(m_F)` when fitting brain data without overfitting.
   * Codes appear heterogeneous and incompatible with any simple reference family across contexts.

2. Noise robustness

   * Measured robustness under noise manipulations does not match any set of predictions within `E_code`, leading to large `DeltaS_noise(m_F)`.

3. Resource mismatch

   * Code cost `C_cost(m_F)` is systematically higher or lower than expected from resource principles, leading to large `DeltaS_resource(m_F)`.

4. Global coding tension

   * For world states `m_F` representing realistic patterns, the combined tension satisfies:

     ```txt
     Tension_code(m_F) >= delta_code
     ```

     with `delta_code > 0` that does not vanish under refinements that respect both data and the encoding rules.

### 5.3 Interpretive note

These counterfactual descriptions do not claim that the brain explicitly optimizes `Tension_code`. They only state that:

* If the brain follows coherent coding principles, then there should exist encodings in `E_code` that keep observed tension low.
* If it does not, then any honest encoding in `E_code` will show persistent high tension.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments that can test TU encodings for Q083. They do not solve neural coding, but they can falsify particular choices of encoding class `E_code` and associated parameters.

### Experiment 1: Cross modality code reuse

*Goal:*
Test whether a single family of codes within `E_code` can achieve low tension across two sensory modalities within the same species.

*Setup:*

* Choose two sensory modalities, for example primary visual cortex and primary auditory cortex in a mammal.
* Collect neural population activity and context labels for both modalities under naturalistic stimulus conditions and defined tasks.
* Fix an encoding class `E_code_mod` contained in `E_code`, for example sparse population codes with simple temporal structure and a limited number of free parameters.

*Protocol:*

1. Fit an encoding from `E_code_mod` to visual data to obtain an encoding `E_vis`, including choices of reference code family and parameters.
2. With `E_vis` as a starting point, construct an encoding for auditory data `E_aud` that only allows adjustments within a predefined small parameter neighborhood.
3. For both `E_vis` and `E_aud`, compute `DeltaS_struct`, `DeltaS_noise`, `DeltaS_resource` and `Tension_code(m)` over a representative set of states for each modality.
4. Compare the distributions of `Tension_code(m)` for visual and auditory configurations under these encodings.

*Metrics:*

* Mean and variance of `Tension_code` for each modality.
* Maximum observed `Tension_code` for each modality.
* Difference between modality specific tension distributions.

*Falsification conditions:*

* Before seeing the data, choose thresholds `tau_vis` and `tau_aud` and a maximal allowed parameter adjustment radius in `E_code_mod`.
* If no encoding within that radius yields `Tension_code(m)` less than or equal to `tau_vis` for visual and `tau_aud` for auditory configurations simultaneously, then the combination of `E_code_mod` and the chosen code family is considered falsified at the effective layer.
* If arbitrarily small changes in parameters produce arbitrarily large changes in tension without any change in the underlying code family, the encoding is considered unstable and rejected.

*Semantics implementation note:*
All observables in this experiment are treated in a hybrid sense, where discrete spike times and continuous rate summaries are both represented by the activity and code descriptors defined in Block 3.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can reject specific coding encodings, but it does not by itself establish the true coding principles of the brain.

---

### Experiment 2: Noise manipulation and robustness

*Goal:*
Determine whether observed neural codes show robustness patterns consistent with low coding tension predictions from efficient coding like principles.

*Setup:*

* Choose a cortical area where sensory coding has been studied in detail.
* Construct experimental or simulation based conditions where input noise or internal noise can be systematically adjusted while recording neural activity and behavioral performance.
* Fix an encoding class `E_code_noise` within `E_code` that includes explicit expectations about robustness, for example how `DeltaS_noise` should change as a function of noise level.

*Protocol:*

1. For each noise level condition, construct states `m_noise` summarizing neural activity, context, and performance.
2. For a fixed encoding in `E_code_noise`, compute `DeltaS_noise(m_noise)` and overall `Tension_code(m_noise)` across noise levels.
3. Compare the observed relationship between noise level and `Tension_code` with the predicted relationship from the encoding.

*Metrics:*

* Curve of `Tension_code` versus noise level.
* Deviation of the observed curve from the predicted curve, for example by a mean squared deviation measure.
* Presence or absence of qualitative transitions such as sudden jumps in tension.

*Falsification conditions:*

* Specify a tolerance band for the difference between predicted and observed tension curves before analyzing the data.
* If, for any encoding in `E_code_noise` consistent with basic biological constraints, the observed curve lies outside this band for a substantial range of noise levels, then that encoding is considered falsified.
* If different encodings in `E_code_noise` that are supposed to be similar produce qualitatively different predictions that cannot be reconciled with the data, the encoding class is considered ill posed for Q083.

*Semantics implementation note:*
Discrete aspects of spike trains and continuous aspects of rates are both mapped into the same effective quantities, and all tension computations use these hybrid representations consistently.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can show that a particular coding principle or encoding class is incompatible with observed robustness, but it does not uniquely identify the correct coding scheme.

---

## 7. AI and WFGY engineering spec

This block specifies how Q083 structures can be used in AI systems within the WFGY framework.

### 7.1 Training signals

We define several training signals that can be computed from internal states of an AI model and used as auxiliary objectives.

1. `signal_code_efficiency`

   * Definition: scalar proportional to `Tension_code(m_AI)`, where `m_AI` is a state summarizing internal representations and task context for an AI model.
   * Purpose: encourage internal representations that achieve lower coding tension, balancing structure, robustness, and cost.

2. `signal_code_robustness`

   * Definition: difference in `Tension_code` between clean and perturbed inputs at matched difficulty.
   * Purpose: penalize representations that show large increases in tension under small perturbations.

3. `signal_cross_context_stability`

   * Definition: a signal based on differences in code descriptors for related tasks or domains, mapped into a cross context tension measure.
   * Purpose: encourage shared codes across tasks when appropriate, analogous to code reuse across brain areas.

4. `signal_alignment_with_bio_codes`

   * Definition: a similarity based signal that rewards internal representations whose code descriptors resemble those extracted from biological data for similar tasks.
   * Purpose: provide a bridge between biological and artificial coding where desired.

### 7.2 Architectural patterns

We outline module patterns that implement these signals without exposing deep TU rules.

1. `NeuralCodeObserver_Module`

   * Role: map internal activations of an AI model into effective code descriptors similar to `C_rate`, `C_temp`, and `C_pop`.
   * Interface: takes activations and context labels as input, outputs code descriptors and simple statistics needed for tension evaluation.

2. `CodeTensionHead_Module`

   * Role: estimate `Tension_code(m_AI)` from code descriptors, possibly decomposed into structural, noise, and resource components.
   * Interface: takes code descriptors as input, outputs a scalar tension estimate and optional component breakdown.

3. `CrossContextCodeConsistency_Module`

   * Role: compute cross context tension by comparing code descriptors across tasks or modalities.
   * Interface: takes pairs or sets of code descriptors from different contexts, outputs measures of code reuse and mismatch.

### 7.3 Evaluation harness

We propose an evaluation harness to test the impact of Q083 modules in AI models.

1. Tasks

   * Use multimodal tasks that require the model to process visual, auditory, and symbolic inputs and perform related outputs.

2. Conditions

   * Baseline models trained without explicit code tension modules.
   * TU augmented models with NeuralCodeObserver_Module and CodeTensionHead_Module active during training or fine tuning.

3. Metrics

   * Task performance across modalities.
   * Generalization to new combinations of modalities or tasks.
   * Robustness under input perturbations.
   * Stability of code descriptors across tasks that share underlying structure.

4. Analysis

   * Compare models with similar performance to see whether lower coding tension correlates with better robustness or interpretability.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience Q083 encoding in an AI system.

* Baseline setup

  * Prompt the AI with questions about how information is represented in the brain and in neural networks, without mentioning coding tension.
  * Observe whether explanations are fragmented, purely verbal, and lacking explicit description of codes and tradeoffs.

* TU encoded setup

  * Prompt the same AI, now with instructions to use notions of codes, mismatch, and coding tension as organizing concepts for its explanations.
  * Ask it to explain how neural codes trade off structure, robustness, and cost, and how similar patterns appear in deep networks.

* Comparison metric

  * Evaluate explanations along three axes: clarity about what is encoded, explicit discussion of noise and robustness, and explicit discussion of resource constraints.
  * Ask independent evaluators to rate which explanation better matches the structure of known neural coding literature.

* What to log

  * Prompts and responses in both conditions.
  * Any internal tension scores returned by Q083 style modules.
  * This enables later audit of how coding tension influenced the reasoning.

---

## 8. Cross problem transfer template

This block lists reusable components from Q083 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `NeuralCodeField`

   * Type: field
   * Minimal interface:

     * Inputs: identifiers for neurons or units, time window, and context labels.
     * Outputs: structured descriptors combining `A_single`, `A_pop`, `C_rate`, `C_temp`, and `C_pop`.
   * Preconditions:

     * There must exist well defined summaries of activity and context for the units and time window of interest.

2. ComponentName: `CodeEfficiencyFunctional`

   * Type: functional
   * Minimal interface:

     * Inputs: code descriptors, information observables `I_stim`, `I_task`, and cost observable `C_cost`.
     * Output: scalar efficiency or inefficiency score related to `Tension_code`.
   * Preconditions:

     * Lower bounds or reference values for information and cost must be specified for the domain.

3. ComponentName: `CrossContextCodeGraph`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: a set of contexts or tasks and corresponding NeuralCodeField descriptors.
     * Output: a graph whose nodes are contexts and whose edges carry similarity or tension values between codes.
   * Preconditions:

     * Code descriptors must be comparable across contexts at the chosen level of abstraction.

### 8.2 Direct reuse targets

1. Q084 (BH_NEURO_MEMORY_STORE_L3_084)

   * Reused component: `NeuralCodeField`.
   * Why it transfers: long term memory storage must act on existing neural codes; memory theories can be expressed in terms of transformations of NeuralCodeField configurations.
   * What changes: emphasis shifts from immediate coding efficiency to stability and recoverability of codes over long time scales.

2. Q085 (BH_NEURO_PLASTICITY_RULES_L3_085)

   * Reused component: `CodeEfficiencyFunctional`.
   * Why it transfers: plasticity rules can be constrained by requiring that they reduce coding tension or improve efficiency over time.
   * What changes: plasticity is described as a process on code descriptors and efficiency scores instead of raw synaptic strengths.

3. Q123 (BH_AI_INTERP_L3_123)

   * Reused components: `NeuralCodeField`, `CrossContextCodeGraph`.
   * Why it transfers: AI interpretability can treat internal activations as codes and use the same structures to map, compare, and visualize them.
   * What changes: neurons become artificial units or channels, and contexts are AI tasks or prompts rather than biological tasks.

4. Q121 (BH_AI_ALIGNMENT_L3_121)

   * Reused component: `CodeEfficiencyFunctional`.
   * Why it transfers: internal representations of goals and values can be evaluated as codes with tensions relative to alignment targets, for example conflicts between encoded goals and external specifications.
   * What changes: information observables relate to goal and constraint variables rather than sensory inputs and motor outputs.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

For Q083 after this Run 2 document:

* E_level: E1

  * The effective encoding of neural coding tension is specified.
  * State space, observables, mismatch quantities, and singular set are defined at a level suitable for conceptual experiments.

* N_level: N1

  * The narrative connecting neural coding questions and coding tension is coherent at a conceptual level.
  * Counterfactual coding worlds and discriminating experiments are described in a way that can be instantiated in simplified settings.

### 9.2 Next measurable step toward E2

To move from E1 to E2, the following measurable steps are proposed:

1. Implement a prototype that:

   * takes empirical or simulated neural data from at least one modality,
   * constructs approximate NeuralCodeField descriptors,
   * computes `DeltaS_struct`, `DeltaS_noise`, `DeltaS_resource`, and `Tension_code`,
   * publishes anonymized tension summaries and analysis code.

2. Run at least one instance of Experiment 1 or Experiment 2 in a simplified setting, for example:

   * comparing codes in two layers of a deep network trained on two modalities,
   * or in two simulated brain areas with controlled coding rules.

Both steps remain at the effective layer, because they operate on descriptors and tension functionals, not on any deep TU generative process.

### 9.3 Long term role in the TU program

In the long term, Q083 is expected to serve as:

* The central node for questions about biological neural representations and their tradeoffs.
* A bridge between neuroscience and AI representation learning, via shared code descriptors and tension functionals.
* A test bed for methods that let researchers probe internal codes of complex systems without requiring full mechanistic understanding.

---

## 10. Elementary but precise explanation

This block provides an explanation for non specialists while staying faithful to the effective layer description.

Neurons in the brain send electrical signals. When many neurons fire over time, they create patterns. The hard question is:

What do these patterns mean, and how are they organized?

People have proposed many answers. Sometimes they say the important thing is how fast a neuron fires on average. Sometimes they say the exact timing of spikes matters. Sometimes they say what matters is the joint activity of large groups of neurons.

In the Tension Universe picture, we do not assume we already know the correct answer. Instead, we treat each possible way of explaining the patterns as a kind of “code family”. For any given situation, we imagine:

* a snapshot that describes which neurons are active, over what time window, and under which conditions,
* a set of summaries that describe how these neurons respond on average, over time, and in groups,
* some numbers that describe how much information these patterns seem to carry and how much they cost the brain.

From this, we define a coding tension number:

* it is small when the patterns look like a clean, robust, and efficient code from the chosen family,
* it is large when the patterns look messy, fragile, or wasteful relative to that family.

We then ask two simple questions.

1. Can we find code families such that, across many brain areas and tasks, we can keep this coding tension small without cheating or overfitting?
2. Or do all reasonable code families end up with large tension somewhere, no matter how hard we try?

If the first situation holds, we live in a world where the brain uses relatively simple coding principles. If the second holds, the brain may use more ad hoc coding strategies, or we may need to rethink our assumptions.

This approach does not tell us which specific code is correct. It does not try to prove a theorem about the brain. It does something more modest but still sharp:

* it turns vague stories about “neural codes” into objects with clear observables and a single tension number,
* it proposes experiments that can falsify particular coding ideas,
* it produces reusable tools that can be applied to both brains and artificial networks.

Q083 is therefore the place in the Tension Universe where the problem of “how neural activity carries information” is written in a way that can be tested, compared, and reused, without claiming to reveal any ultimate generative rules of the brain.
