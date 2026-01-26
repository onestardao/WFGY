# Q123 · Scalable interpretability

## 0. Header metadata

```txt
ID: Q123
Code: BH_AI_INTERP_L3_123
Domain: Artificial intelligence
Family: Interpretability and internal representations
Rank: S
Projection_dominance: I
Field_type: cognitive_field
Tension_type: cognitive_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-26
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical question behind Q123 can be phrased as:

> Can we maintain faithful, useful, and affordable interpretability of internal AI representations as models scale in capability and size, without the cost or complexity of interpretation growing so fast that it becomes effectively impossible?

More concretely, Q123 asks whether there exists a family of interpretability tools and encodings such that, for frontier models:

1. Internal representations can be mapped to human usable concepts and mechanisms in a controlled way.
2. The size and complexity of the explanation library grow much slower than the raw parameter count and state space of the models.
3. This interpretability remains robust when tasks, architectures, and deployment conditions change.

The problem does not ask for a specific method. It asks whether the general regime of “scalable interpretability” is achievable at all under realistic constraints.

### 1.2 Status and difficulty

Current interpretability work has demonstrated several partial successes:

* Mechanistic interpretability studies have identified circuits and features in vision and language models that correspond to human understandable patterns.
* Feature visualization and probing methods can sometimes reveal concept like structure in internal layers.
* Some methods transfer across model sizes within a narrow architecture family.

However, several pressure points remain unresolved:

* Many interpretability tools do not scale well. Cost grows very quickly with parameter count or with the number of layers inspected.
* Results can be brittle. Probes that work on one model or dataset fail or give misleading answers on another.
* It is unclear whether a small, stable library of concepts and circuits can explain most of what very large models are doing.

There is no consensus answer to whether scalable interpretability is possible in the strong sense defined above. The problem is open and tightly coupled to questions about alignment, control, and oversight of powerful AI systems.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q123 plays several roles:

1. It is the central node for the interpretability cluster of AI problems, connecting to alignment, control, and oversight.
2. It provides the core notion of cognitive_tension between:

   * internal representation complexity, and  
   * the size, stability, and usability of human level explanations.

3. It offers a template for encoding questions about whether human understanding can keep up with systems whose internal state spaces grow far beyond intuitive scales.
4. It acts as a bridge node to:

   * neuroscience problems about neural coding and representation,
   * socio technical problems where understanding complex models of society is necessary.

### References

1. C. Olah et al., “Zoom In: An introduction to circuits”, Distill, 2020.  
   (Mechanistic interpretability agenda and circuits framing for internal representations.)

2. N. Elhage et al., “Toy Models of Superposition”, Anthropic technical report, 2022.  
   (Demonstrates how features can become entangled as models scale, stressing interpretability.)

3. F. Doshi Velez and B. Kim, “Towards a Rigorous Science of Interpretable Machine Learning”, arXiv preprint, 2017.  
   (Formal discussion of interpretability as a scientific problem and evaluation challenge.)

4. A. Nanda, “A Mechanistic Interpretability Analysis of Grokking”, technical writeup, 2022.  
   (Case study on understanding internal circuits and their evolution during training.)

At least one of the above references comes from or is backed by a major research organization, and each contains enough bibliographic information to be located and checked.

---

## 2. Position in the BlackHole graph

This block records how Q123 sits in the BlackHole graph, using only Q identifiers and one line reasons that point to concrete components or tension types.

### 2.1 Upstream problems

Upstream nodes provide prerequisites, tools, or conceptual framing that Q123 relies on at the effective layer.

* Q121 (BH_AI_ALIGNMENT_L3_121)  
  Reason: Defines the alignment objectives and value grounded behaviors that scalable interpretability is supposed to support, via components like AlignmentObjectiveField and FailureModeCatalog.

* Q122 (BH_AI_CONTROL_L3_122)  
  Reason: Supplies control and intervention patterns that assume some ability to read and modify internal mechanisms, using components such as InterventionHandleSpace and ControlRiskFunctional.

* Q083 (BH_NEURO_CODE_L3_083)  
  Reason: Provides analogies and constraints from biological neural coding, including CodebookObservables that inform how internal representations might map to concepts.

* Q089 (BH_NEURO_PREDICTIVE_CODE_L3_089)  
  Reason: Offers predictive coding style structures and invariants, for example PredictionErrorField, which influence what “explanation” means for layered networks.

### 2.2 Downstream problems

Downstream nodes directly reuse Q123 components or depend on its tension structure.

* Q124 (BH_AI_OVERSIGHT_L3_124)  
  Reason: Reuses InterpretabilityTensionFunctional_Q123 to decide where human or automated oversight should be concentrated in large models.

* Q125 (BH_AI_MULTIAGENT_L3_125)  
  Reason: Uses ConceptProbeLibrary_Q123 and WorldTF_InterpretabilityPattern to interpret interacting agents’ internal states and to detect opaque coordination behaviors.

### 2.3 Parallel problems

Parallel nodes share similar tension types but do not directly reuse Q123 components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)  
  Reason: Both Q059 and Q123 study how much structured information can be extracted, compressed, or made usable from very large state spaces, under information theoretic constraints.

* Q116 (BH_PHIL_MATH_FOUND_L3_116)  
  Reason: Both address what counts as an acceptable explanation or understanding, linking technical structure to human level conceptual clarity.

### 2.4 Cross domain edges

Cross domain edges connect Q123 to problems in other domains that can reuse its patterns.

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)  
  Reason: Can reuse Q123’s interpretability patterns to understand complex climate and socio economic models that inform decisions about the Anthropocene.

* Q105 (BH_COMPLEX_CRASHES_L3_105)  
  Reason: Can reuse interpretability tension tools to inspect models of complex systems where unpredictable crashes or cascades occur, using similar ideas of opaque internal mechanisms.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions,
* encoding classes and fairness constraints.

We do not describe any hidden generative rules or how raw model weights, activations, or datasets are turned into TU internal fields.

### 3.1 State space

We assume a semantic state space:

```txt
M
```

with elements `m` in `M` interpreted as “interpretability worlds” for AI systems.

Each state `m` encodes, at the effective layer:

* A particular AI model or a family of closely related models, including:

  * architecture class,
  * approximate scale (for example parameter count bucket),
  * training regime and task family descriptor.

* One interpretability tool stack, including:

  * a fixed concept probe library,
  * a fixed family of feature or circuit extraction tools,
  * a fixed set of reporting formats for explanations.

* Coarse summaries of performance on tasks that are relevant for safety or alignment.

We do not specify how `m` is constructed from raw weights or training logs. We only assume that for each such model and tool stack there exists at least one state `m` that encodes the observable summaries listed below.

At the effective layer, we require that:

* For each state `m` and each observable defined in this block, the observable is either well defined and finite or explicitly marked as out of domain.

### 3.2 Effective observables and fields

We define the following observables and fields on `M`.

1. Local interpretability score family

```txt
I_local(m; U)
```

* Input: state `m` and a finite set `U` of internal units, features, or circuit fragments.
* Output: a nonnegative scalar that summarizes how well the fixed probe library can assign stable, human usable concepts to the elements of `U`.
* Interpretation: larger values indicate higher interpretability quality for that local subset.

2. Global conceptual coherence

```txt
C_global(m)
```

* Input: state `m`.
* Output: a scalar that measures the degree to which local explanations can be composed into a small set of global concepts or mechanisms that explain large fractions of model behavior.
* Higher values indicate better global coherence and reuse of a compact concept library.

3. Explanation complexity

```txt
K_complexity(m)
```

* Input: state `m`.
* Output: a nonnegative scalar that approximates description length or complexity of the explanation library needed to cover a fixed portfolio of behaviors for the model.

Examples of what K_complexity may summarize:

* number of distinct concept probes used,
* total size of a circuit dictionary,
* complexity of the minimal explanation graphs.

4. Interpretability mismatch

```txt
DeltaS_interp(m)
```

* Input: state `m`.
* Output: a nonnegative scalar that measures how badly the pair `(C_global(m), K_complexity(m))` deviates from an idealized scalable regime for the given performance and scale of the model.

Properties:

* `DeltaS_interp(m) >= 0`.
* Small `DeltaS_interp(m)` indicates that global coherence is high relative to explanation complexity, for the given capability level.

The exact functional definition of `DeltaS_interp` will depend on fixed reference curves and thresholds specified in the encoding class below.

### 3.3 Encoding class and fairness constraints

To avoid arbitrary post hoc tuning, we restrict attention to an admissible encoding class `E_interp` with the following properties.

1. Finite probe library

There exists a fixed countable family of interpretability probes and concept templates:

```txt
P = {p_1, p_2, ..., p_n, ...}
```

For any specific encoding instance in `E_interp`, only a finite subset of `P` can be activated, and this subset must be chosen before any experiment is run.

2. Fixed aggregation rules

For each encoding instance, the rules that aggregate local probe results into `I_local`, and that aggregate local explanations into `C_global` and `K_complexity`, are fixed before observing detailed outcomes of experiments.

3. Weight constraints

When defining `DeltaS_interp(m)` we may use weights of the form:

```txt
w_C, w_K >= 0, w_C + w_K = 1
```

These weights must be selected once for the encoding instance and cannot be changed based on experiment outcomes. They may depend on coarse model scale buckets but not on fine grained internal measurements.

4. Resolution and refinement order

Each state `m` is associated with a resolution parameter:

```txt
r(m) in R_plus
```

which can represent, for example, the size of the model, the coverage of the task portfolio, or the density of measurement of internal activations.

We introduce a refinement partial order `<=_ref` on `M` defined by:

* `m1 <=_ref m2` if and only if `m2` represents a refinement of `m1` with higher resolution parameter (for example `r(m2) > r(m1)`) and strictly more detailed but compatible summaries.

All admissible encodings must respect this partial order in the sense that:

* Observables do not change in arbitrary ways under refinement.
* If `m1 <=_ref m2` then it is meaningful to compare `DeltaS_interp(m1)` and `DeltaS_interp(m2)`.

### 3.4 Effective tension tensor components

We assume that Q123 reuses the general TU tension tensor structure:

```txt
T_ij(m) = S_i(m) * C_j(m) * DeltaS_interp(m) * lambda(m) * kappa
```

where:

* `S_i(m)` is a source like factor that represents how strongly source component `i` (for example a particular subsystem or layer family) contributes to interpretability relevant behavior.
* `C_j(m)` is a receptivity like factor that represents how sensitive observer or downstream component `j` is to interpretability quality for decision making or safety.
* `DeltaS_interp(m)` is the interpretability mismatch defined above.
* `lambda(m)` is a convergence state factor drawn from a fixed range that codes whether local reasoning about the model is convergent, recursive, divergent, or chaotic.
* `kappa` is a coupling constant that sets the overall scale of cognitive_tension for this encoding.

The detailed indexing sets for `i` and `j` are not needed at the effective layer. It is sufficient that for any `m` in `M` and any admissible encoding, `T_ij(m)` is well defined and finite whenever `m` is in the regular domain.

### 3.5 Invariants and domain restrictions

We define an interpretability tension functional:

```txt
Tension_interp(m) = G(I_local(m; U_*), C_global(m), K_complexity(m))
```

where:

* `U_*` is a fixed finite selection rule for internal units or fragments, chosen once per encoding instance.
* `G` is a nonnegative function that is monotone in the following sense:

  * If `I_local` increases and `C_global` increases while `K_complexity` stays the same or decreases, then `Tension_interp(m)` does not increase.
  * If `K_complexity` increases while `I_local` and `C_global` remain roughly constant, `Tension_interp(m)` does not decrease.

An example of such a functional is:

```txt
Tension_interp(m) = w_low * (1 - I_norm(m)) + w_struct * (1 - C_norm(m)) + w_comp * K_norm(m)
```

where:

* `I_norm(m)` and `C_norm(m)` are normalized versions of `I_local` and `C_global` in the interval `[0, 1]`,
* `K_norm(m)` is a normalized complexity,
* `w_low`, `w_struct`, and `w_comp` are nonnegative weights that sum to `1` and are fixed within the encoding.

We now define the singular set for Q123:

```txt
S_sing = { m in M :
           I_local(m; U_*) is undefined or not finite
           or C_global(m) is undefined or not finite
           or K_complexity(m) is undefined or not finite
           or Tension_interp(m) is undefined or not finite
         }
```

All analysis and experiments for Q123 are restricted to the regular set:

```txt
M_reg = M \ S_sing
```

Whenever an experiment attempts to evaluate observables for a state in `S_sing`, the result is treated as “out of domain” rather than as informative evidence about interpretability regimes.

---

## 4. Tension principle for this problem

This block encodes Q123 as a tension principle at the effective layer.

### 4.1 Core tension statement

The core cognitive_tension principle for Q123 can be stated as:

*Inside realistic resource and tooling limits, there is a tension between:*

1. The richness, size, and flexibility of internal representations in powerful AI models.
2. The requirement that humans (or human aligned tools) can understand and work with these representations using a compact, robust explanation library and a finite probe set.

Q123 asks whether this tension can be kept within a manageable band as models scale, or whether it inevitably grows beyond any reasonable threshold.

### 4.2 Scalable interpretability as low tension

At the effective layer, a world is in the scalable interpretability regime if there exists an admissible encoding class `E_interp` such that:

```txt
For each scale bucket k,
there exists m_k in M_reg with resolution r(m_k) in bucket k
and Tension_interp(m_k) <= epsilon_interp(k)
```

where:

* `epsilon_interp(k)` is a scale dependent threshold that grows slowly with `k` and remains bounded in a way consistent with realistic oversight and tooling.

In words:

* As models grow, there are ways to encode their internal structure so that interpretability tension remains controlled.
* The explanation and concept libraries remain usable and do not explode in size or complexity relative to the models.

### 4.3 Interpretability collapse as persistent high tension

Conversely, an interpretability collapse regime is one in which, for any admissible encoding in `E_interp`, there exists a scale bucket beyond which all regular states exhibit persistent high tension:

```txt
There exists k_0 and delta_interp > 0 such that
for all k >= k_0, for all m in M_reg with resolution r(m) in bucket k,
Tension_interp(m) >= delta_interp
```

In words:

* Beyond some scale, every honest attempt to encode the model with fixed probe libraries and aggregation rules leads to explanations that are either:

  * too complex to be practical, or
  * too incoherent to be trustworthy.

Q123, as an S problem, does not claim which regime the real world occupies. It provides a way to formulate and test encodings that discriminate between these regimes.

---

## 5. Counterfactual tension worlds

We now describe counterfactual worlds at the effective layer. None of these worlds describes how internal TU fields are constructed from raw data.

### 5.1 World T_interp (scalable interpretability)

World T_interp is a world in which scalable interpretability is achievable in a strong sense.

Typical properties:

1. Existence of low tension sequences

   * For each relevant scale level, there exist states `m_T(k)` in `M_reg` that encode models at that scale such that:

     ```txt
     Tension_interp(m_T(k)) <= epsilon_interp(k)
     ```

     with `epsilon_interp(k)` growing slowly enough that explanations remain usable for oversight and control.

2. Stability of local probes

   * The local interpretability scores `I_local(m_T(k); U_*)` remain bounded away from zero for key subsystems, and do not degrade dramatically when the model or data distribution shifts.

3. Global coherence

   * `C_global(m_T(k))` stays high, indicating that a compact concept and circuit library explains a large fraction of important behaviors across tasks.

4. Controlled complexity

   * `K_complexity(m_T(k))` grows slower than a simple function of model size or resolution, such as sublinear in an appropriate scale measure, within the chosen encoding class.

### 5.2 World F_interp (interpretability collapse)

World F_interp is a world in which strong scalable interpretability fails.

Typical properties:

1. No low tension encodings beyond some scale

   * For every admissible encoding, there exists a scale level `k_0` such that all states `m_F(k)` with `k >= k_0` satisfy:

     ```txt
     Tension_interp(m_F(k)) >= delta_interp
     ```

     for some `delta_interp > 0` that does not shrink with further refinement.

2. Fragile local probes

   * Probes that appear to work at small scales fail to generalize at higher scales or under small distribution shifts, so `I_local` becomes noisy or misleading.

3. Fragmented global structure

   * `C_global(m_F(k))` cannot be kept high without rapidly increasing `K_complexity`. The explanation library becomes too large and tangled to be usable.

4. Escalating explanation burden

   * Any attempt to maintain adequate coverage of safety relevant behaviors leads to exponential or otherwise infeasible growth in explanation complexity measures, making oversight via interpretability unrealistic.

### 5.3 Intermediate regime

We also allow an intermediate regime where:

* Some subsystems or tasks remain in a low tension interpretability regime.
* Others move toward high tension, especially those that involve emergent or strategic behavior.

This regime is important for engineering decisions, but the primary distinction in Q123 is still between:

* worlds where strong scalable interpretability is possible in principle, and
* worlds where it is not.

### 5.4 Interpretive note

These counterfactual worlds describe patterns of observables and tension functionals. They do not include any description of how TU internal fields are generated from raw data or how training pipelines operate at the deep level.

---

## 6. Falsifiability and discriminating experiments

This block describes experiments and protocols that can:

* test whether a given Q123 encoding is coherent and useful, and
* discriminate between encodings that support scalable interpretability and those that do not.

These experiments cannot prove or disprove the canonical statement itself. They only accept or reject particular TU encodings within the admissible class.

### Experiment 1: Scaling sweep in a controlled model family

*Goal:*

Evaluate whether a chosen Q123 encoding tracks intuitive interpretability quality as models scale within a fixed architecture and training regime.

*Setup:*

* Select a family of models with the same architecture pattern, trained on the same task family, at multiple scale levels (for example different parameter counts).
* Fix a finite concept probe library and circuit template set before any inspection of internal activations.
* Fix aggregation rules for `I_local`, `C_global`, and `K_complexity` as described in Block 3.
* Choose a fixed portfolio of behaviors and test cases (for example reasoning tasks, safety relevant prompts).

*Protocol:*

1. For each model size, construct a state `m_size` in `M_reg` that encodes the chosen summaries and probe outcomes.
2. Compute `I_local(m_size; U_*)`, `C_global(m_size)`, and `K_complexity(m_size)` using the fixed encoding.
3. Compute `Tension_interp(m_size)` for each scale level.
4. Collect human judgments or expert judgments on interpretability:

   * For a subset of internal circuits or features, ask whether humans can understand and predict their behavior using the explanation library.

5. Compare the tension scores with human judgments across scales.

*Metrics:*

* Correlation between `Tension_interp(m_size)` and human interpretability ratings.
* Trend of `Tension_interp(m_size)` as model scale increases.
* Stability of this trend under minor variations in probe selection that stay within the admissible library.

*Falsification conditions:*

* If models that human experts judge as clearly more interpretable consistently receive higher tension scores than models they judge as opaque, under the fixed encoding, then this encoding is considered misaligned and is rejected for Q123.
* If small permitted changes within the admissible encoding class (for example swapping a few probes in the same library or modestly changing normalization constants) produce arbitrary reversals in the ordering of `Tension_interp(m_size)` across scales, the encoding fails the stability requirement and is rejected.

*Semantics implementation note:*

The experiment uses hybrid semantics in line with Block 0. Internal representations and activations are treated as continuous fields, while probes, concept dictionaries, and explanation libraries are treated as discrete structures. All observables are defined at the effective layer in terms of summaries and do not depend on raw floating point details.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. This experiment can show that a particular Q123 encoding is misaligned or unstable, but it does not settle whether scalable interpretability exists in principle.

---

### Experiment 2: Toy interpretable vs scrambled models

*Goal:*

Test whether the Q123 encoding can reliably distinguish between deliberately interpretable toy models and scrambled models with similar performance but less structured internal representations.

*Setup:*

* Construct a set of toy interpretable models, where internal circuits or features are hand designed or strongly constrained to have clear human understandable roles on a small suite of tasks.
* Construct a matched set of scrambled models with similar input and output behavior but intentionally obfuscated internal structures (for example through random basis transformations or entangled parameterizations).
* Use the same concept probe library and aggregation rules for all models.

*Protocol:*

1. For each toy interpretable model, construct a regular state `m_Ttoy` in `M_reg`.
2. For each scrambled model, construct a regular state `m_Ftoy` in `M_reg`.
3. Evaluate `I_local`, `C_global`, `K_complexity`, and `Tension_interp` on all these states under the fixed encoding.
4. Optionally, obtain human judgments on how easy it is to understand circuits in each model class.

*Metrics:*

* Comparison of the distribution of `Tension_interp(m_Ttoy)` and `Tension_interp(m_Ftoy)`.
* Fraction of model pairs where the toy interpretable model has strictly lower tension than its scrambled counterpart.
* Alignment of tension differences with human judgments, where available.

*Falsification conditions:*

* If the encoding fails to consistently assign lower `Tension_interp` to toy interpretable models than to scrambled models, across a broad enough sample, it is considered ineffective and rejected for Q123.
* If the sign of the average tension difference between the two model classes is sensitive to arbitrary choices within the fixed probe library (for example different but equally plausible subsets of probes) in a way that violates the fairness constraints, this signals that the encoding is not robust and should be revised or rejected.

*Semantics implementation note:*

Hybrid semantics are used in the same way as in Experiment 1. Continuous internal states are observed through discrete probes and explanation artifacts, and only their summarized forms appear in the effective layer.

*Boundary note:*

Falsifying TU encoding != solving canonical statement. Success or failure on toy models only evaluates the quality of a particular Q123 encoding; it does not prove that scalable interpretability is possible or impossible for real frontier systems.

---

## 7. AI and WFGY engineering spec

This block explains how Q123 becomes a reusable engineering module within AI systems and the WFGY framework, at the effective layer.

### 7.1 Training signals

We define training signals that can be used as auxiliary objectives or diagnostics.

1. `signal_interp_stability`

   * Definition: a penalty signal that increases when `Tension_interp(m)` increases between nearby training checkpoints or under small perturbations of prompts and inputs, for states representing the same model.
   * Purpose: encourage models and interpretability tools to move toward stable, low tension regions of `M_reg`.

2. `signal_circuit_sparsity`

   * Definition: a regularization term that penalizes increases in `K_complexity(m)` when performance remains constant or improves.
   * Purpose: favor internal structures whose explanations can be expressed with smaller and more reusable circuit libraries.

3. `signal_world_TF_separation`

   * Definition: a signal that encourages the model to keep answers under World T_interp assumptions and World F_interp assumptions clearly separated, by measuring inconsistency when it implicitly mixes the two interpretability regimes.
   * Purpose: avoid hidden conflation of “we can understand this” and “we cannot realistically understand this” regimes.

4. `signal_probe_alignment`

   * Definition: a signal that penalizes discrepancies between probe based explanations and known causal interventions in toy settings, where ground truth mechanisms are accessible.
   * Purpose: tie interpretability scores to genuine causal structure rather than purely correlational patterns.

### 7.2 Architectural patterns

We sketch architectural patterns that can incorporate Q123 components.

1. `InterpretabilityHead`

   * Role: given a representation of the current internal state and context, this head outputs an estimated `Tension_interp` value and a short vector of interpretable diagnostics (for example normalized `I_local`, `C_global`, `K_complexity`).
   * Interface: takes intermediate activations or compressed summaries as input, emits tension estimates and supporting statistics as outputs.

2. `ConceptLibraryModule`

   * Role: maintains a small, explicit library of concept vectors, circuits, or templates that explanations must be expressed in terms of, to constrain explanation complexity.
   * Interface:

     * Inputs: task family descriptors, high level goals, and training context.
     * Outputs: a fixed size set of concept anchors and associated decoding mechanisms.

3. `TU_InterpObserver`

   * Role: acts as a generalized observer that maps internal states and concept library contents into the observables used by Q123: `I_local`, `C_global`, `K_complexity`.
   * Interface: takes the model’s internal activations and concept library state as input and provides the observable summaries needed to compute `Tension_interp`.

### 7.3 Evaluation harness

An evaluation harness for Q123 augmented systems can be organized as follows.

1. Task mix

   * Include tasks where mechanistic structure is partly known (for example algorithmic tasks with known circuits).
   * Include high level capabilities tasks where interpretability is important for safety (for example instruction following with safety constraints).

2. Conditions

   * Baseline condition: models without Q123 modules and without interpretability related training signals.
   * TU condition: models with Q123 modules, receiving interpretability related signals and exposing tension outputs.

3. Metrics

   * Behavioral performance on the task mix.
   * Quality of explanations, measured against human expert assessments or ground truth circuits where available.
   * Agreement between explanation complexity and measured `K_complexity` and `Tension_interp` values.
   * Stability of explanations and tension scores under minor changes of prompts or inputs.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience the effect of Q123 encodings.

*Baseline setup*

* Prompt a model with a question like:  

  “Explain how this language model decides which answer to give on safety relevant questions. Please be detailed.”

* Observe the explanation:

  * Does it reference concrete internal mechanisms, or does it stay at a vague design level?
  * Does it provide any sense of which parts of the model are most important?

*TU encoded setup*

* Ask the same question, but with an additional instruction:  

  “Use interpretable internal concepts and circuits, and report a scalar interpretability tension score for the explanation. Explain which parts of your internal representation space are easy to understand and which are opaque.”

* Observe the explanation and the reported tension:

  * Are specific internal structures or concept libraries mentioned?
  * Does the model identify which parts of its behavior cannot easily be explained within a small concept library?

*Comparison metric*

* Rate both explanations on:

  * structure (clear parts and relationships),
  * concreteness (linkage to internal mechanisms or concept libraries),
  * honesty about opacity (does the model admit areas with high tension).

*What to log*

* Prompts and full responses for both setups.
* Any intermediate tension scores or diagnostics emitted by Q123 modules.
* This allows later analysis of how Q123 affects explanation style without exposing any deep TU generative rules.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q123 and their direct reuse targets.

### 8.1 Reusable components produced by this problem

1. ComponentName: `InterpretabilityTensionFunctional_Q123`

   * Type: functional
   * Minimal interface:

     * Inputs: internal representation summaries, probe results, and explanation complexity indicators for a given model and context.
     * Output: a scalar interpretability tension score in a fixed range (for example `[0, 1]`) plus a small diagnostic vector.

   * Preconditions:

     * The encoding must belong to the admissible class `E_interp`, with probe libraries and aggregation rules fixed ahead of time.

2. ComponentName: `ConceptProbeLibrary_Q123`

   * Type: field or ai_module
   * Minimal interface:

     * Inputs: task family descriptor and architecture descriptor.
     * Output: a finite set of concept probes and templates selected from a global library `P`, plus associated configuration for mapping probe activations into explanations.

   * Preconditions:

     * The selection policy must be independent of fine grained activation patterns and must be fixed before running interpretability experiments for the models under study.

3. ComponentName: `WorldTF_InterpretabilityPattern`

   * Type: experiment_pattern
   * Minimal interface:

     * Inputs: description of a model family and interpretability tool stack.
     * Output: a pair of experiment designs corresponding to World T_interp and World F_interp assumptions, each with defined observables, metrics, and falsification conditions.

   * Preconditions:

     * The experiment designs must respect the constraints on encoding class and fairness as set out in Block 3 and Block 6.

### 8.2 Direct reuse targets

1. Target: Q121 (BH_AI_ALIGNMENT_L3_121)

   * Reused components: `InterpretabilityTensionFunctional_Q123`, `ConceptProbeLibrary_Q123`.
   * Why it transfers: alignment scenarios often require knowing when internal representations for value related concepts are interpretable and stable. Q123 supplies a way to score and monitor this.
   * What changes: observables are focused on value aligned circuits and representations rather than general task behavior.

2. Target: Q122 (BH_AI_CONTROL_L3_122)

   * Reused components: `InterpretabilityTensionFunctional_Q123`.
   * Why it transfers: control procedures can use tension scores to decide where intervention handles are safe or where additional interpretability work is needed.
   * What changes: tension thresholds and metrics are tuned for control sensitivity rather than general understanding.

3. Target: Q124 (BH_AI_OVERSIGHT_L3_124)

   * Reused components: `ConceptProbeLibrary_Q123`, `WorldTF_InterpretabilityPattern`.
   * Why it transfers: oversight processes need structured protocols for distinguishing interpretable and non interpretable regimes, and for routing human attention accordingly.
   * What changes: experiment patterns emphasize auditing workflows and oversight load, not just scientific evaluation.

4. Target: Q125 (BH_AI_MULTIAGENT_L3_125)

   * Reused components: `WorldTF_InterpretabilityPattern`.
   * Why it transfers: multi agent systems require understanding internal states of interacting agents; interpretability patterns help identify opaque coordination channels.
   * What changes: input model families are now agent populations; metrics focus on coordination structures and emergent collective behaviors.

---

## 9. TU roadmap and verification levels

This block explains how Q123 is positioned on the TU verification ladder and what the next measurable steps are.

### 9.1 Current levels

* E_level: E1

  * A coherent effective layer encoding of scalable interpretability has been specified, including state space, observables, a tension functional, and a singular set.
  * At least two discriminating experiments with explicit falsification conditions have been described.

* N_level: N2

  * A clear narrative distinguishes World T_interp and World F_interp, plus an intermediate regime.
  * Cross problem connections to alignment, control, oversight, and neuroscience are spelled out.

### 9.2 Next measurable step toward E2

To move Q123 from E1 to E2, at least one of the following must be realized in concrete implementations:

1. A working tool chain that:

   * takes trained models and an interpretability tool stack as input,
   * constructs states in `M_reg` for those models,
   * computes approximate `Tension_interp` scores and publishes them along with model scale and task portfolio.

2. A completed instance of Experiment 1:

   * applied to at least one real model family across several scale levels,
   * with publicly available data on tension scores and human interpretability judgments,
   * allowing independent groups to reproduce or challenge the results.

These steps operate entirely at the effective layer and do not require exposing any deep TU generative rules.

### 9.3 Long term role in the TU program

In the longer term, Q123 is expected to serve as:

* The anchor node for interpretability considerations in the AI cluster, linking to alignment, control, oversight, and multi agent questions.
* A test bed for whether TU encodings can remain practical as systems become extremely large and complex.
* A bridge between:

  * technical interpretability research,
  * formal safety specifications,
  * and philosophical discussions about understanding and explanation.

As verification levels rise, Q123 components should become standard tools for evaluating and comparing AI systems along interpretability dimensions.

---

## 10. Elementary but precise explanation

This block explains Q123 in everyday language, while staying faithful to the effective layer encoding.

Modern AI models are very large. Inside them there are many numbers and complicated patterns that decide what the model does. Interpretability is about trying to look inside and say:

* “This part is doing roughly this job.”
* “These patterns mean the model is thinking about this concept.”

So far, people have made progress on small or medium models. They can sometimes find circuits that recognize simple shapes, grammar patterns, or other clear features. But as models get bigger and more powerful, it becomes harder to keep up. There are too many parts, and the patterns can become tangled.

Q123 asks a simple but hard question:

> As models get bigger, can we still understand them well enough, using tools that do not explode in cost and complexity?

In the Tension Universe view, we do not jump to an answer. Instead, we:

1. Imagine a space of “interpretability worlds”. Each world is:

   * one model at some size,
   * with one fixed set of interpretability tools and probes,
   * plus a way to summarize explanations.

2. For each world, we measure:

   * how well we can give simple, stable explanations of what the model is doing (local and global interpretability),
   * how big and complicated the explanation library has to be.

3. We combine these into a single number called interpretability tension. Roughly:

   * low tension means explanations are clear and not too complex,
   * high tension means it feels like the model is a black box or the explanations are too messy.

Then we look at two kinds of imaginary universes:

* In a “good” universe, as we build bigger and smarter models, there are still ways to keep interpretability tension low. Our tools scale well enough. We can still see what matters inside the models.
* In a “bad” universe, after some point interpretability tension stays high no matter what we do, as long as we play fair and do not cheat with hindsight. The inside becomes too complicated for us to really understand.

Q123 does not say which universe we live in. Instead, it gives:

* a careful way to define what we mean by “scalable interpretability”,
* clear measurements and experiments that can tell us whether a particular way of encoding interpretability is working,
* reusable pieces that other problems, like alignment and oversight, can use when they talk about understanding models.

In this way, Q123 turns a vague worry into a structured tension problem: one that can be tested, compared, and improved over time, without claiming any deep magic or revealing how the inner TU machinery is built.
