# Q120 · Value of information and knowledge

## 0. Header metadata

```txt
ID: Q120
Code: BH_PHIL_VALUE_OF_INFORMATION_L3_120
Domain: Philosophy
Family: Epistemology and decision theory
Rank: S
Projection_dominance: I
Field_type: socio_technical_field
Tension_type: incentive_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-26
```

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical question behind Q120 can be stated as follows:

> What is the fundamental role of information and knowledge in guiding action and determining value, and how should their value be measured and compared across contexts, agents, and time?

More concretely, Q120 asks for a unified account that answers at least three tightly coupled subquestions:

1. **Normative value of information**

   * Given an agent with preferences and uncertainty about the world, how should the value of additional information be defined, across:

     * one-shot decisions,
     * sequential decisions,
     * multi-agent and institutional settings?
   * When, if ever, is more information strictly harmful rather than merely irrelevant or costly?

2. **Knowledge versus mere information**

   * How should we distinguish between:

     * raw information (for example data, signals, messages),
     * beliefs,
     * justified beliefs,
     * knowledge?
   * In which sense does knowledge, if it is more than just high-quality information, change the structure of action and value?

3. **Global role in value and agency**

   * Can we regard information and knowledge as:

     * a fundamental “currency” of rational agency,
     * a basic determinant of long-run value,
     * or only as instrumental tools that derive their value entirely from other goods?

The tension arises because standard decision-theoretic “value of information” formalisms, epistemological theories of knowledge, and real-world uses of information in institutions and AI systems often diverge in how they assess the worth and role of information.

### 1.2 Status and difficulty

Several mature partial frameworks exist:

* Bayesian decision theory and expected utility models give precise definitions of the value of information for idealized agents in stylized settings.
* Epistemology offers multiple competing accounts of knowledge and justification, including reliabilist, evidentialist, and knowledge-first approaches.
* Economic and social theories study information as a resource in markets, institutions, and technology.

However, there is no widely accepted unified account that:

* simultaneously handles:

  * individual decision making,
  * collective and institutional behavior,
  * long-run civilization-scale value,
* and cleanly reconciles:

  * formal value-of-information calculus,
  * philosophical accounts of knowledge,
  * observed failures and pathologies in real-world information ecosystems.

For the BlackHole S-problem collection, Q120 is treated as an open, high-rank problem because any serious attempt to align AI and socio-technical systems with human values must implicitly or explicitly solve some version of it.

### 1.3 Role in the BlackHole project

Within the BlackHole graph, Q120 plays three roles:

1. It anchors the **value-of-information cluster** in philosophy, connecting decision theory, epistemology, and global value questions.
2. It provides a reference node for how TU encodes **incentive_tension** around information and knowledge in socio-technical systems.
3. It supplies reusable components for downstream problems about AGI alignment, interpretability, and multi-agent systems, where mis-valued information and knowledge can lead to catastrophic outcomes.

### References

1. C. E. Shannon, “A Mathematical Theory of Communication”, *Bell System Technical Journal*, 27(3–4), 1948, pp. 379–423, 623–656.
2. R. A. Howard, “Information value theory”, *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 1966, pp. 22–26.
3. F. P. Ramsey, “Truth and Probability”, in *The Foundations of Mathematics and Other Logical Essays*, Routledge and Kegan Paul, 1931 (original manuscript 1926).
4. F. Dretske, *Knowledge and the Flow of Information*, MIT Press, 1981.
5. T. Williamson, *Knowledge and Its Limits*, Oxford University Press, 2000.

---

## 2. Position in the BlackHole graph

This block records how Q120 sits inside the BlackHole graph as nodes and edges among Q001–Q125. Each edge includes a one-line reason that points to a concrete component or tension feature.

### 2.1 Upstream problems

These problems provide prerequisites or tools that Q120 relies on at the effective layer.

* Q115 (BH_PHIL_INDUCTION_UNDERDETERMINATION_L3_115)
  Reason: Supplies the treatment of inductive support and underdetermination that Q120 reuses when defining normative value-of-information baselines.

* Q116 (BH_PHIL_CONFIRMATION_EVIDENCE_L3_116)
  Reason: Provides the structure of evidential support and confirmation that informs how information updates are evaluated in Q120.

* Q118 (BH_PHIL_LOGIC_BOUNDS_L3_118)
  Reason: Constrains the logical environment (classical or otherwise) in which information and knowledge are evaluated and compared.

* Q119 (BH_PHIL_MEANING_OF_PROBABILITY_L3_119)
  Reason: Supplies the interpretation of probability that Q120 must adopt when defining expected value-of-information and epistemic risk.

### 2.2 Downstream problems

These problems directly reuse Q120 components or depend on its tension structure.

* Q121 (BH_AI_ALIGNMENT_TRUST_L3_121)
  Reason: Reuses the ValueOfInformationGap functional to quantify when an AGI system undervalues alignment-critical information provided by humans.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Uses Q120’s KnowledgeStateField to treat interpretability tools as information channels about internal AI states with measurable value.

* Q124 (BH_AI_MULTIAGENT_ALIGNMENT_L3_124)
  Reason: Reuses the InformationChannelLibrary to analyze mis-valued information in multi-agent negotiation and coordination settings.

### 2.3 Parallel problems

Parallel nodes share similar incentive_tension structure but have no direct component dependence.

* Q111 (BH_PHIL_MIND_BODY_L3_111)
  Reason: Both Q111 and Q120 involve how internal states (mental or informational) matter for action, but without sharing explicit value-of-information functionals.

* Q114 (BH_PHIL_MORAL_REALISM_L3_114)
  Reason: Both introduce tension between “how things are” and “how they guide action and value”, but with different focus (moral facts versus informational states).

* Q117 (BH_PHIL_SCIENTIFIC_REALISM_L3_117)
  Reason: Both grapple with how theoretical states (scientific models, knowledge claims) should be weighed in determining rational action.

### 2.4 Cross-domain edges

Cross-domain edges connect Q120 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses the ValueOfInformationGap functional to compare informational and energetic costs in information-theoretic thermodynamics.

* Q098 (BH_EARTH_ANTHROPOCENE_L3_098)
  Reason: Uses Q120’s framing to quantify how mis-valued information about planetary systems contributes to Anthropocene-scale misalignment.

* Q121 (BH_AI_ALIGNMENT_TRUST_L3_121)
  Reason: Connects epistemic trust in AGI to the valuation of alignment-relevant information in human–AI interaction loops.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Treats interpretability artifacts as information channels whose value can be scored using Q120’s components.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden generative rules or explicit mappings from raw data to internal TU fields.

### 3.1 State space

We assume a semantic state space

`M`

with the following effective interpretation:

* Each element `m` in `M` is a coherent “decision and information configuration” for one agent (or institution) in one situation. It includes:

  * a finite set of available actions `A(m)`,
  * a finite library of potential information channels `L_channels(m)`,
  * a finite library of world-hypothesis summaries `L_world(m)` (for example high-level scenarios),
  * a coarse description of the agent’s current belief state and preference structure.

We do not specify how these objects are constructed from raw logs or psychological states. We only require that:

* For each `m` in `M`, the sets `A(m)`, `L_channels(m)`, and `L_world(m)` are finite and well defined.
* For each action and world hypothesis, there is a well defined payoff summary in real numbers.

### 3.2 Effective fields and observables

We introduce the following effective observables on `M`.

1. Normative value-of-information functional for a channel

```txt
VOI_norm(m; ch) in R
```

* Input: a state `m` in `M` and a channel `ch` in `L_channels(m)`.
* Output: a real number representing the normative expected value of using channel `ch` before acting, given a reference model of:

  * the agent’s preferences,
  * probabilities over `L_world(m)`,
  * and how `ch` would update those probabilities.

We do not specify the internal computation. We only assume:

* VOI_norm is finite for all channels in the finite library,
* it is evaluated using a consistent reference model fixed at the encoding level, not tuned per outcome.

2. Realized value-of-information functional

```txt
VOI_real(m; ch) in R
```

* Input: a state `m` and a channel `ch`.
* Output: a real number representing the effective value the agent actually obtains from `ch`, given:

  * their real belief-updating behavior,
  * attention limits,
  * institutional constraints.

At the effective layer we treat VOI_real as a well defined summary that can be estimated or modeled, without specifying details.

3. Information gap observable

```txt
DeltaS_info(m; ch) = max(0, VOI_norm(m; ch) - VOI_real(m; ch))
```

* This is a nonnegative scalar for each channel.
* It measures how much normative value is “left on the table” because the agent or institution fails to extract or use the information that would be available.

4. Channel weight observable

For each state `m` we define normalized, fixed weights:

```txt
w_ch(m) >= 0   for ch in L_channels(m)
sum over ch in L_channels(m) of w_ch(m) = 1
```

These weights encode how important each channel is for the situation type. They are determined by a rule that depends only on:

* the type of decision,
* the role of the channel (for example safety-critical, convenience, cosmetic),

and are fixed before any experiment. They do not depend on observed outcomes or on VOI_norm or VOI_real values for the specific instance.

5. Knowledge state observable

```txt
K_score(m) in [0, 1]
```

* A scalar that summarizes how close the agent’s state is to a reference “knowledgeable” baseline for that situation, with:

  * `K_score(m) = 1` meaning fully aligned with the reference knowledge profile,
  * `K_score(m) = 0` meaning severe ignorance or mis-knowledge.

We only require that K_score is well defined on the regular domain and can be estimated from external behavior or assessments.

### 3.3 Effective tension tensor components

We define an aggregate information-tension score at the state level:

```txt
Gap_info(m) = sum over ch in L_channels(m) of w_ch(m) * DeltaS_info(m; ch)
```

This is a nonnegative scalar. Then we define an effective semantic tension tensor over `M`:

```txt
T_ij(m) = S_i(m) * C_j(m) * Gap_info(m) * lambda_factor(m) * kappa_VoI
```

where:

* `S_i(m)` is a source factor describing how strongly source component `i` (for example safety-critical decisions) depends on correctly valued information in state `m`.
* `C_j(m)` is a receptivity factor describing how sensitive downstream component `j` (for example long-term value, institutional stability) is to mis-valued information.
* `Gap_info(m)` is the aggregate information gap defined above.
* `lambda_factor(m)` is a convergence-state factor in a fixed bounded range, indicating whether local reasoning processes in `m` are convergent, recursive, divergent, or chaotic.
* `kappa_VoI` is a fixed positive scaling constant for Q120 encodings.

At the effective layer we do not need explicit index sets for `i` and `j`. It is sufficient that for each `m` in the regular domain, all `T_ij(m)` are finite real numbers.

### 3.4 Invariants and effective constraints

We define two simple invariants on `M`.

1. Aggregate information tension invariant

```txt
I_VoI(m) = Gap_info(m)
```

This is just the aggregate gap. For world-representing states in which information and knowledge are properly valued, we expect `I_VoI(m)` to lie in a low band.

2. Knowledge and information alignment invariant

Define:

```txt
I_align(m) = max(0, Gap_info(m) - alpha_align * (1 - K_score(m)))
```

where `alpha_align` is a fixed positive constant chosen at the encoding level. This invariant is small when:

* either information gaps are small,
* or knowledge is low but in ways that do not induce large information gaps (for example honest ignorance in low-stakes contexts).

It is large when there is both mis-valued information and substantial deviation from the reference knowledge profile.

### 3.5 Singular set and domain restrictions

Some observables may be undefined or non-finite if:

* payoffs are not well summarized,
* VOI_norm or VOI_real cannot be assigned finite values,
* K_score is not meaningfully defined.

We define the singular set:

```txt
S_sing = {
  m in M :
  VOI_norm(m; ch) or VOI_real(m; ch) is undefined or non-finite for some ch in L_channels(m),
  or K_score(m) is undefined
}
```

We impose the following domain restriction:

* All Q120 tension analysis is carried out only on the regular domain

  ```txt
  M_reg = M \ S_sing
  ```

* Whenever an experiment or protocol encounters a state in `S_sing`, the result is treated as “out of domain” for Q120 encoding and not as evidence about the underlying philosophical problem.

---

## 4. Tension principle for this problem

### 4.1 Core tension functional

We define the core tension functional for Q120 as:

```txt
Tension_VoI(m) = I_VoI(m) + beta_align * I_align(m)
```

with `beta_align > 0` fixed at the encoding level.

This functional satisfies:

* `Tension_VoI(m) >= 0` for all `m` in `M_reg`.
* `Tension_VoI(m)` is small when:

  * high-value channels are appropriately used and integrated,
  * knowledge is in reasonable alignment with the reference profile.
* `Tension_VoI(m)` grows when:

  * important channels are ignored or mis-used,
  * knowledge is distorted in ways that systematically misdirect action or value.

### 4.2 Low-tension principle

At the effective layer, the “good” version of Q120 can be phrased as a low-tension principle:

> In well-functioning agents and institutions, across a wide range of situations, world-representing states lie in a low-tension band for `Tension_VoI`, after controlling for costs and constraints.

Formally, for a chosen admissible encoding class (fixed choice of:

* reference VOI_norm model,
* channel libraries,
* weight rules,
* knowledge baselines),

we expect that for many world-representing states `m_good`:

```txt
Tension_VoI(m_good) <= epsilon_VoI
```

for some small `epsilon_VoI` that does not grow without bound as we refine the encoding or observe more behavior.

### 4.3 Persistent high tension as failure of value-of-information

In contrast, we say that a configuration exhibits persistent high tension if, under the same admissible encoding class, there exist world-representing states `m_bad` such that:

```txt
Tension_VoI(m_bad) >= delta_VoI
```

for some strictly positive `delta_VoI` that cannot be made arbitrarily small by:

* refining the representation of channels,
* improving estimates of VOI_real,
* or mildly adjusting the fixed weight rule,

while still staying faithful to observed actions and outcomes.

At the effective layer, Q120 then partitions the space of socio-technical configurations into:

* low-tension worlds where information and knowledge are valued in ways that broadly match their normative roles,
* high-tension worlds where the mismatch is systematic and cannot be explained away by modeling artifacts.

---

## 5. Counterfactual tension worlds

We describe two counterfactual worlds strictly at the effective layer:

* World K: knowledge and information are systematically well valued.
* World M: knowledge and information are systematically mis-valued.

### 5.1 World K (knowledge aligned, low information tension)

In World K:

1. For a wide range of high-stakes situations, there exist world-representing states `m_K` in `M_reg` such that:

   ```txt
   I_VoI(m_K) is small
   I_align(m_K) is small
   ```

2. When new channels are introduced, high-value ones are quickly integrated, and low-value or harmful ones are eventually down-weighted or removed, leading to:

   ```txt
   Tension_VoI(m_K_new) <= Tension_VoI(m_K_old)
   ```

   on average across similar situations.

3. Knowledge baselines evolve in ways that reduce long-run information gaps rather than increasing them.

4. Incentive structures are at least partly aligned with the proper valuation of information, so that ignoring high-value information is discouraged and rewarded less than using it.

### 5.2 World M (mis-valued information, high information tension)

In World M:

1. There exist many world-representing states `m_M` in `M_reg` such that:

   ```txt
   I_VoI(m_M) is large
   I_align(m_M) is large
   ```

   especially in safety-critical or long-run contexts.

2. High-value channels are systematically ignored, distrusted, or underused, while low-value or misleading channels are amplified, leading to persistent:

   ```txt
   Gap_info(m_M) >= delta_gap
   ```

   for some positive `delta_gap`.

3. Knowledge baselines are distorted in ways that make it easier to maintain high information gaps (for example entrenched misinformation or structural ignorance).

4. Incentive structures reward behavior that increases or preserves information gaps, such as exploiting others’ ignorance or optimizing for short-term metrics that ignore long-run value.

### 5.3 Interpretive note

These worlds are not claims about our actual universe. They are templates for how:

* low-tension,
* high-tension

configurations would look in terms of observables without specifying any deep-level generative rules of TU.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

* test the coherence of the Q120 encoding,
* discriminate between different choices of encoding parameters,
* provide evidence about whether a given socio-technical configuration behaves more like World K or World M.

None of these experiments prove or disprove any philosophical thesis. They only test the Q120 encoding at the effective layer.

### Experiment 1: Human decision tasks with controlled value-of-information

*Goal:*
Test whether the ValueOfInformationGap functional tracks actual human behavior in controlled decision tasks.

*Setup:*

* Design a finite set of decision scenarios for human participants, each with:

  * a small set of actions,
  * explicit probabilistic outcomes and payoffs (for experimenters),
  * one or more information channels that participants can optionally consult at some cost.
* For each scenario, use a fixed normative model to compute `VOI_norm(m; ch)` for each channel.
* Collect participant choices about:

  * whether to query each channel,
  * which actions to take.

*Protocol:*

1. For each participant and scenario, construct an effective state `m_data` in `M_reg` that summarizes:

   * the available actions and channels,
   * payoffs as specified,
   * the participant’s observed information choices and actions.
2. Estimate `VOI_real(m_data; ch)` from behavior, for example by:

   * comparing choices with and without access to `ch`,
   * evaluating realized payoffs and inferable strategy changes.
3. Compute `DeltaS_info(m_data; ch)` for each channel, then `Gap_info(m_data)` and `Tension_VoI(m_data)`.
4. Aggregate these scores across scenarios and participants, and compare them with independent assessments of:

   * how “rational” participants’ information use appears,
   * whether they are ignoring clearly valuable information.

*Metrics:*

* Correlation between `Tension_VoI(m_data)` and independent expert ratings of misused information.
* Average `Tension_VoI` in scenarios where human behavior is widely considered good versus poor.
* Stability of `Tension_VoI` under small changes in modeling assumptions that keep the same admissible encoding class.

*Falsification conditions:*

* If across many scenarios it is not possible to choose fixed weight rules and reference models (within the admissible class) such that high `Tension_VoI` corresponds reliably to widely recognized misuses of information and low `Tension_VoI` to good use, then the current encoding of `Gap_info` and `Tension_VoI` is considered falsified.
* If tiny, ad hoc changes in encoding parameters produce arbitrarily different `Tension_VoI` rankings of the same behaviors, the encoding is deemed unstable and rejected.

*Semantics implementation note:*
States are represented using finite sets of actions, channels, and scenarios, with payoffs and VOI values treated as real numbers. This matches the hybrid setting where discrete decisions interact with continuous payoff summaries.

*Boundary note:*
Falsifying TU encoding != solving canonical statement. This experiment can reject specific encoding choices for Q120, but it does not settle the philosophical question of the ultimate role of information and knowledge.

---

## 7. AI and WFGY engineering spec

This block describes how Q120 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

### 7.1 Training signals

1. `signal_voi_gap`

   * Definition: a nonnegative scalar signal equal to `Gap_info(m)` for the current decision context.
   * Purpose: penalize policies and internal representations that consistently leave large normative information gaps.

2. `signal_knowledge_alignment`

   * Definition: a signal proportional to `I_align(m)`.
   * Purpose: encourage models to bring their effective knowledge state closer to the reference baseline in ways that reduce information gaps.

3. `signal_channel_usage_efficiency`

   * Definition: a ratio-like signal comparing VOI_real and VOI_norm aggregated across channels in `L_channels(m)`.
   * Purpose: reward efficient selection and use of high-value channels, and discourage overuse of low-value channels.

4. `signal_long_horizon_information_safety`

   * Definition: a signal that increases when a model’s information usage pattern leads to high `Tension_VoI` in simulated long-horizon scenarios, especially safety-critical ones.
   * Purpose: integrate Q120 tension measures into safety-oriented training loops.

### 7.2 Architectural patterns

1. `VoI_Estimator_Head`

   * Role: a module that estimates VOI_norm and VOI_real for candidate channels from internal representations of the current context.
   * Interface: takes context embeddings and channel descriptors as input, outputs estimates for VOI_norm, VOI_real, and DeltaS_info.

2. `Knowledge_Gap_Monitor`

   * Role: a module that maintains an approximate K_score for the model’s understanding of the current domain.
   * Interface: aggregates signals from tasks, feedback, and self-assessment probes to produce K_score, which feeds into I_align.

3. `Information_Pricing_Module`

   * Role: a module that converts information usage decisions (for example whether to call tools or request external data) into explicit “prices” based on Gap_info and Tension_VoI.
   * Interface: interacts with decision layers to modulate when and how external information is requested.

### 7.3 Evaluation harness

1. Task selection

   * Interactive decision tasks where the model can optionally query external tools or data sources.
   * Domains where the value of additional information can be approximately computed by experimenters.

2. Conditions

   * Baseline: the model can query tools without any explicit Q120-based signals.
   * TU condition: the model has VoI_Estimator_Head and Knowledge_Gap_Monitor modules providing signals described above.

3. Metrics

   * Overall task performance (for example reward, success rate).
   * Information efficiency: performance per unit of external information cost.
   * Safety margin: how often high-risk actions are taken without querying clearly high-value channels.

### 7.4 60-second reproduction protocol

A minimal protocol that external users can run to experience Q120 encoding in an AI system.

* Baseline setup

  * Prompt the AI with a short scenario where a decision must be made (for example whether to launch a product, proceed with a medical procedure, or sign a contract), and provide access to several optional information sources without mentioning value-of-information.
  * Ask the AI to decide whether to consult each source and to justify its decisions.

* TU encoded setup

  * Present a similar scenario but additionally instruct the AI to:

    * estimate the normative value of each information source,
    * explain which are high-value and why,
    * avoid ignoring high-value sources in safety-critical contexts.
  * The AI uses internal Q120-based modules to compute approximate Gap_info and Tension_VoI.

* Comparison metric

  * Compare how often the AI:

    * consults high-value sources,
    * avoids consulting obviously low-value or distracting sources,
    * articulates clear reasons tied to value-of-information.

* What to log

  * The prompts, decisions about information use, and any associated tension scores (Gap_info and Tension_VoI) for later analysis.

---

## 8. Cross problem transfer template

### 8.1 Reusable components produced by this problem

1. ComponentName: `ValueOfInformationGap_Functional`

   * Type: functional
   * Minimal interface:

     * Inputs: `VOI_norm_profile`, `VOI_real_profile`, `channel_weights`
     * Output: `gap_score` (a nonnegative scalar)
   * Preconditions:

     * Inputs summarize finite sets of channels with consistent units and weight rules fixed at the encoding level.

2. ComponentName: `KnowledgeStateField`

   * Type: field
   * Minimal interface:

     * Inputs: `task_history_summary`, `assessment_signals`
     * Output: `K_score` in `[0, 1]`
   * Preconditions:

     * Task history and assessment signals can be summarized in a way that supports a meaningful scalar knowledge score.

3. ComponentName: `InformationChannelLibrary`

   * Type: field
   * Minimal interface:

     * Inputs: `situation_descriptor`
     * Output: `L_channels`, a finite set of channel descriptors with roles (for example safety-critical, optional, cosmetic).
   * Preconditions:

     * Situation descriptors are rich enough to classify channels into role categories used by the weighting rule.

### 8.2 Direct reuse targets

1. Q121 (AGI alignment and trust)

   * Reused component: `ValueOfInformationGap_Functional`.
   * Why it transfers: mis-valued alignment-relevant information (for example human feedback, oversight signals) can be modeled as high Gap_info in alignment scenarios.
   * What changes: VOI_norm and VOI_real are evaluated for channels conveying human intent and safety constraints.

2. Q123 (AI interpretability and internal representations)

   * Reused component: `KnowledgeStateField` and `InformationChannelLibrary`.
   * Why it transfers: interpretability tools are treated as channels providing information about internal states, and their value depends on the knowledge gap they help close.
   * What changes: the situation_descriptor now describes internal model behaviors, and K_score is interpreted as knowledge about those behaviors.

3. Q059 (Information-theoretic thermodynamics)

   * Reused component: `ValueOfInformationGap_Functional`.
   * Why it transfers: physical measurement channels and feedback loops have both informational and energetic costs, which can be jointly analyzed through Gap_info.
   * What changes: VOI_norm and VOI_real are tied to thermodynamic and control-theoretic payoffs rather than human preferences.

4. Q098 (Anthropocene system dynamics)

   * Reused component: `InformationChannelLibrary`.
   * Why it transfers: global policy decisions depend on which scientific and monitoring channels are available and how they are valued.
   * What changes: channels correspond to environmental monitoring systems and scientific assessments, and the situation_descriptor encodes planetary-scale decisions.

---

## 9. TU roadmap and verification levels

### 9.1 Current levels

* E_level: E1

  * A coherent effective-layer encoding of Q120 in terms of information gaps and knowledge alignment has been specified.
  * At least one concrete experimental protocol has been described that can falsify specific instances of the encoding.

* N_level: N1

  * The narrative connecting information, knowledge, incentives, and value has been laid out using explicit observables and tension scores.
  * Counterfactual worlds (World K and World M) have been specified at a qualitative level.

### 9.2 Next measurable step toward E2

To move from E1 to E2 for Q120, at least one of the following should be implemented:

1. A working prototype that:

   * instantiates `ValueOfInformationGap_Functional` and `KnowledgeStateField`,
   * logs Gap_info and Tension_VoI for real decision tasks (human or AI),
   * and publishes the resulting tension profiles with enough detail to be independently recomputed.

2. A systematic study of controlled human decision experiments where:

   * VOI_norm and VOI_real are estimated,
   * Q120 tension scores are computed,
   * and their relation to independent quality judgments is reported.

Both steps operate entirely at the effective layer and require no exposure of deep TU generative rules.

### 9.3 Long-term role in the TU program

In the longer term, Q120 is expected to serve as:

* the central node for value-of-information and knowledge-related tension in socio-technical systems,
* a template for how to encode incentive_tension problems that connect philosophical analysis and concrete engineering,
* a bridge between philosophical accounts of knowledge, decision-theoretic models, and practical AI alignment work.

---

## 10. Elementary but precise explanation

In ordinary language, Q120 is about a simple but deep question:

> How should we decide what information is worth having, what it means to really know something, and how that should change what we do and what we care about?

Sometimes more information clearly helps. Sometimes it just distracts us or even makes things worse. Similarly, having data is not the same as having knowledge that actually guides good action.

In the Tension Universe view, we do not try to solve all philosophical debates. Instead, we set up a way to measure how “out of line” a situation is with the idea that information and knowledge should be used well.

For each situation, we imagine:

* a small set of possible actions,
* a set of information sources the agent could consult,
* a way to say, in principle, how valuable each source would be if used perfectly,
* and a way to see how much value the agent actually gets from the sources they use.

The difference between “value available” and “value actually used” is the information gap. We combine these gaps across sources, and we also track how far the agent’s knowledge is from a reasonable reference level. When both gaps are small, tension is low. When they are large, tension is high.

We then think about two types of worlds:

* In a good world, agents and institutions mostly use high-value information and build solid knowledge, so the tension stays low.
* In a bad world, high-value information is ignored, low-value signals are amplified, and knowledge is twisted or missing, so the tension stays high.

This does not answer every philosophical question about information and knowledge. It does something more modest and concrete:

* it defines observable quantities (information gaps, knowledge scores),
* it specifies how to combine them into tension scores,
* it gives experiments that can show when a particular encoding of these ideas is working or failing,
* and it creates tools that can be reused in other problems, especially in AI alignment and socio-technical design.

Q120 is therefore the reference point for how Tension Universe treats the value of information and knowledge as a measurable kind of tension in real decision-making systems.
