# Q119 · Meaning of probability

## 0. Header metadata

```txt
ID: Q119
Code: BH_PHIL_PROB_MEANING_L3_119
Domain: Philosophy
Family: Probability and foundations
Rank: S
Projection_dominance: C
Field_type: cognitive_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-30
```

## 0. Effective layer disclaimer

### 0.1 Scope of claims

* This page works entirely at the Tension Universe (TU) effective layer.
* Its goal is to specify an effective-layer encoding of the problem “meaning of probability” and to define observable tension quantities and experiments.
* It does not claim to solve or refute the canonical statements about probability in philosophy, mathematics, or physics.
* It does not introduce new theorems beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### 0.2 Effective-layer boundary

* All objects introduced in this document live at the effective layer as defined in the TU Effective Layer Charter.
* This includes state spaces `M`, interpretation libraries, context and constraint libraries, observables, tension scores, invariants, counterfactual worlds, and experiment patterns.
* No deep TU generative rules are specified. No claim is made about the fundamental ontology of probability, logic, or physical reality.
* We do not give any mapping from raw texts, physical systems, or mental states to TU fields. We only assume that such mappings can be implemented by encodings that respect the TU Encoding and Fairness Charter.

### 0.3 Encoding classes and fairness

* All encodings used in this page are required to belong to the admissible encoding classes of the TU Encoding and Fairness Charter.
* The specific class for this problem is called `E_probMeaning`. It is a subfamily of the global TU admissible encoding classes and is defined in Section 3.2.
* Once an encoding is chosen inside `E_probMeaning`, its libraries, weights, and mapping rules must be fixed at design time and remain fixed for all experiments and worlds that use that encoding.
* Encodings are not allowed to be retrofitted in response to observed tension scores. In particular, they may not:

  * change the interpretation of labels on a case-by-case basis,
  * adjust weights per scenario,
  * add special-purpose tags or constraints only to improve tension for a specific dataset or domain.

### 0.4 Tension scale and bands

* All scalar tension quantities in this document, including `DeltaS_norm(m)`, `DeltaS_sem(m)`, `DeltaS_ctx(m)`, and `Tension_prob(m)`, are dimensionless TU tension scores.
* They are normalized to lie in the interval `[0, 1]` according to the normalization rules in the TU Tension Scale Charter.
* Thresholds such as `epsilon_prob`, `delta_prob`, `epsilon_core`, and `delta_mix` are band markers on this normalized scale. They distinguish low-tension, medium-tension, and high-tension regimes as defined in the TU Tension Scale Charter.
* These thresholds do not carry any physical units. They are part of the effective-layer description only.

### 0.5 Semantics regime

* The metadata flag `Semantics: hybrid` means that:

  * probability discourse is represented using discrete symbolic labels and context features,
  * these labels are combined with numerical tension scores on the `[0, 1]` scale,
  * no additional semantic regime is assumed beyond what is explicitly defined in Section 3.
* Hybrid semantics here is an effective representation choice. It does not commit to any view about whether probability is ultimately objective, subjective, or something else.

### 0.6 Relation to TU charters

* This page should be read together with the following charters, which specify the global rules that constrain all effective-layer encodings and tension scales in TU:

  * TU Effective Layer Charter
  * TU Encoding and Fairness Charter
  * TU Tension Scale Charter

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q119 can be stated as follows:

When we say that something has a certain probability, what exactly are we talking about, and can there be a single coherent notion of probability that unifies the main uses across science, statistics, decision theory, and everyday reasoning?

More concretely, Q119 asks:

1. What is the correct interpretation, or family of interpretations, of probability statements such as:

   * “The probability that this radioactive atom decays in the next hour is 0.5.”
   * “The probability that a fair coin lands heads is 0.5.”
   * “My degree of belief that the theory is correct is 0.7.”

2. Can a single hybrid account simultaneously:

   * respect objective-seeming uses (for example physical chance),
   * respect frequency-based uses (for example long-run relative frequencies),
   * respect subjective or epistemic uses (for example rational credence and betting behavior),

   without either collapsing them into one narrow notion or fragmenting them into unrelated meanings?

3. Is there a principled way to decide, in concrete cases, which reading of probability is in play and which coherence constraints must hold between them?

### 1.2 Status and difficulty

The interpretation of probability is an open foundational problem. Several major traditions exist:

* Objective chance views, which treat probability as a real feature of the world or its laws.
* Frequency views, which identify probability with actual or limiting frequencies in sequences of trials.
* Subjective or Bayesian views, which interpret probability as rational degrees of belief subject to coherence constraints.
* Logical or evidential views, which see probability as a measure of support provided by evidence to hypotheses.

Each of these traditions has well-known strengths and well-known difficulties. Attempts to give a unified account, such as hybrid or pluralist views, face systematic challenges:

* Connecting single-case and long-run uses without contradiction.
* Handling cases where chance, frequency, and rational credence pull in different directions.
* Explaining how probability connects to decision, causality, and the value of information.

There is no widely accepted solution that simultaneously satisfies the main mathematical, scientific, and philosophical constraints. Q119 collects these tensions into a single S-level problem for the BlackHole program.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q119 plays a central role in the cognitive and philosophical sector:

1. It is the prototype **consistency_tension** problem for probability talk across domains.
2. It links logical and epistemic structure (for example Q114, Q105) to risk and tail behavior (Q117) and to information value (Q120).
3. It provides a test bed for Tension Universe encodings where:

   * formal probability calculus,
   * human conceptual usage,
   * and AI model behavior

   must be held to a common consistency standard without assuming that any single pre-existing interpretation is correct.

### References

1. A. N. Kolmogorov, “Foundations of the Theory of Probability”, 1933, English translation by N. Morrison, Chelsea Publishing, 1950.
2. B. de Finetti, “Theory of Probability”, Volumes 1 and 2, Wiley, 1974 and 1975.
3. D. Lewis, “A Subjectivist’s Guide to Objective Chance”, in “Philosophical Papers, Volume 2”, Oxford University Press, 1986.
4. A. Hajek, “Interpretations of Probability”, Stanford Encyclopedia of Philosophy, first published 2002, substantive revision 2012.

---

## 2. Position in the BlackHole graph

This block records how Q119 sits inside the BlackHole graph among Q001–Q125. Each edge includes a one-line reason pointing to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q119 relies on at the effective layer.

* Q114 (BH_PHIL_INDUCTION_L3_114)
  Reason: Supplies the core inductive and confirmation structures that constrain how probability can connect evidence to hypotheses.

* Q105 (BH_PHIL_DECISION_CAUSALITY_L3_105)
  Reason: Provides the decision-theoretic and causal background that constrains how probabilistic beliefs guide action and counterfactuals.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Contributes the information-theoretic side of probability, including entropy and thermodynamic cost, which Q119 must treat consistently.

### 2.2 Downstream problems

These problems directly reuse Q119 components or depend on its consistency_tension structure.

* Q117 (BH_PHIL_RISK_AND_RUIN_L3_117)
  Reason: Reuses probability meaning profiles and tail-tension scores to analyze ruin scenarios and risk management.

* Q120 (BH_PHIL_VALUE_OF_INFORMATION_L3_120)
  Reason: Builds on Q119’s probability meaning encoding to define how information changes expected value and rational choice.

* Q098 (BH_AI_LONG_TERM_CALIBRATION_L3_098)
  Reason: Uses Q119’s tension functionals as part of long-term calibration criteria for AI probabilities under distribution shift.

* Q121 (BH_AI_ALIGNMENT_L3_121)
  Reason: Depends on Q119’s consistency_tension structure to evaluate whether probability assignments used in AI alignment pipelines remain meaningful and norm-coherent under safety constraints.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q091 (BH_NEURO_BAYES_BRAIN_L3_091)
  Reason: Both Q119 and Q091 concern probabilistic reasoning in cognitive systems, but Q091 focuses on neural implementation rather than conceptual meaning.

* Q001 (BH_MATH_NUM_L3_001)
  Reason: Both Q119 and Q001 treat probability-like or measure-like structures as constrained by consistency_tension between formal models and observable patterns, but in different domains.

### 2.4 Cross-domain edges

Cross-domain edges connect Q119 to problems in other domains that can reuse its components.

* Q091 (BH_NEURO_BAYES_BRAIN_L3_091)
  Reason: Reuses probability meaning profiles to interpret how neural systems may implement Bayesian-like computations.

* Q098 (BH_AI_LONG_TERM_CALIBRATION_L3_098)
  Reason: Applies Q119’s tension scores to evaluate whether AI predictive probabilities remain meaningful under long-term drift.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Connects probability meaning to physical information measures and thermodynamic constraints on computation.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* interpretation and context libraries,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions,
* admissible encoding classes.

We do not describe any hidden TU generative rules or any mapping from raw linguistic data or mental states to internal TU fields.

### 3.1 State space

We assume a semantic state space:

```txt
M
```

with the following effective interpretation:

* Each element `m` in `M` represents a coherent “probability discourse configuration” in a bounded context. This includes:

  * a finite collection of probability claims (for example about chances, frequencies, credences),
  * a finite library of background constraints that are taken as operative in this context (for example Kolmogorov-style rules, decision-theoretic norms),
  * a finite set of interpretation tags assigned to these claims (for example chance_like, frequency_like, credence_like).

We do not specify how such configurations are constructed from texts, experiments, or cognitive states. At the effective layer we only assume:

* For any bounded discourse context of interest, there exist states `m` in `M` that encode a finite summary of:

  * which probability claims are made,
  * how they are classified by interpretation tags,
  * which coherence constraints are supposed to hold.

### 3.2 Interpretation, context, constraint libraries and admissible encoding class

To avoid free-choice pathologies, we fix:

1. A finite interpretation library:

   ```txt
   L_int = { chance_like, frequency_like, credence_like,
             logical_support_like, pragmatic_heuristic_like }
   ```

   Each label is a coarse type, not a detailed theory.

2. A finite context feature library:

   ```txt
   L_ctx = { single_case, repeatable_process, symmetry_cue_present,
             causal_model_available, high_stakes, low_stakes }
   ```

3. A finite constraint library:

   ```txt
   L_con = { kolmogorov_axioms, dutch_book_coherence,
             principal_principle_style_link,
             law_of_large_numbers_style_link,
             reflection_principle_style_link }
   ```

We define an admissible encoding class for Q119:

```txt
E_probMeaning
```

with the following properties.

* `E_probMeaning` is a subfamily of the global TU admissible encoding classes defined in the TU Encoding and Fairness Charter.
* Any encoding in `E_probMeaning`:

  * maps a concrete discourse context into some `m` in `M` using only labels from `L_int`, `L_ctx`, and `L_con`,
  * pre-declares how each label contributes to the observables below,
  * does not adjust the interpretation of these labels on a case-by-case basis in response to observed tension scores.

Weight selection is constrained as follows.

* We predefine a finite set of candidate weight triples:

  ```txt
  W_candidates = {
    (1.0, 0.0, 0.0),
    (0.6, 0.2, 0.2),
    (0.5, 0.25, 0.25),
    (0.4, 0.3, 0.3),
    (0.33, 0.33, 0.34)
  }
  ```

* Each encoding in `E_probMeaning` must choose one triple `(w_norm, w_sem, w_ctx)` from `W_candidates` at design time.

* Once chosen, the triple is fixed for all contexts, states, and worlds that use that encoding. It cannot be tuned per scenario or per domain.

In addition, the following fairness constraints hold.

* Library contents and classification rules for `L_int`, `L_ctx`, and `L_con` must be specified once per encoding.
* New labels cannot be introduced solely to decrease tension for a specific domain without being applicable across the encoding’s whole intended scope.
* No encoding may condition its label assignments or weight choice on tension scores observed on the same dataset.

All statements about high or low tension in this document are implicitly restricted to encodings in `E_probMeaning`.

### 3.3 Effective observables

We introduce three nonnegative observables on `M`. Each is a dimensionless TU tension score normalized to lie in `[0, 1]` according to the TU Tension Scale Charter.

1. Normative mismatch observable:

   ```txt
   DeltaS_norm(m) in [0, 1]
   ```

   * Input: a state `m` with a finite set of claims and constraints from `L_con`.
   * Output: a scalar summarizing violations of basic probability-style norms, including:

     * additivity and normalization,
     * simple Dutch-book coherence patterns,
     * obvious clashes between claimed probabilities and declared constraints.
   * Requirements:

     * `DeltaS_norm(m) = 0` when all recorded claims respect the operative constraints.
     * `DeltaS_norm(m)` increases toward `1` when more or stronger violations are present, with monotonicity and normalization rules specified by the encoding.

2. Cross-interpretation mismatch observable:

   ```txt
   DeltaS_sem(m) in [0, 1]
   ```

   * Input: a state `m` with interpretation tags in `L_int`.
   * Output: a scalar summarizing mismatches between:

     * how a probability claim is tagged,
     * how it is used in reasoning or linked to other claims.
   * Examples at the effective layer include:

     * using a chance_like claim as if it were a personal credence with no link to any chance principle,
     * treating a frequency_like claim as if it applied to a single, non-repeatable case without any bridge rule.
   * Requirements:

     * `DeltaS_sem(m) = 0` when the use of each claim is consistent with its tag and with the constraint library.
     * `DeltaS_sem(m)` increases toward `1` as cross-interpretation misuse accumulates.

3. Contextual mismatch observable:

   ```txt
   DeltaS_ctx(m) in [0, 1]
   ```

   * Input: a state `m` with context features from `L_ctx`.
   * Output: a scalar summarizing mismatches between:

     * the context features (for example single_case with no repeatable process),
     * the chosen interpretation tags and their intended domains of application.
   * Requirements:

     * `DeltaS_ctx(m) = 0` when interpretation choices and reasoning uses are context-appropriate.
     * `DeltaS_ctx(m)` increases toward `1` as context-inappropriate uses accumulate.

### 3.4 Combined probability meaning tension

We combine the three observables into a single effective tension score:

```txt
Tension_prob(m) = w_norm * DeltaS_norm(m)
                  + w_sem * DeltaS_sem(m)
                  + w_ctx * DeltaS_ctx(m)
```

where:

* `(w_norm, w_sem, w_ctx)` is a triple chosen from `W_candidates` as specified in Section 3.2,
* all three weights are nonnegative and sum to `1`.

Since each component observable lies in `[0, 1]` and the weights sum to `1`, we have:

```txt
Tension_prob(m) in [0, 1]
```

for all `m` where the observables are defined.

Fairness constraints for the combined tension:

* The triple `(w_norm, w_sem, w_ctx)` is chosen once per encoding in `E_probMeaning` and then held fixed for all contexts and experiments.
* The triple cannot be tuned retrospectively on a per-case basis in response to observed data in order to artificially lower `Tension_prob(m)`.

### 3.5 Invariants and effective constraints

We define three simple invariants over finite collections of states. They are computed from normalized tension scores and therefore also lie in `[0, 1]`.

1. Single-case coherence invariant:

   For a finite collection `C_single` of states representing single-case probability uses, define:

   ```txt
   I_single = average over m in C_single of Tension_prob(m)
   ```

   This invariant measures how well the encoding handles single-case statements across different contexts.

2. Ensemble linkage invariant:

   For states grouped into matched ensembles where both frequency_like and credence_like tags appear, define:

   ```txt
   I_ensemble = average over ensembles of
                |DeltaS_norm(m_freq) - DeltaS_norm(m_cred)|
   ```

   where `m_freq` and `m_cred` are the frequency-focused and credence-focused sides of the same ensemble.

   This invariant measures how well the encoding keeps long-run and single-case reasoning in sync. High values indicate persistent tension between frequency and credence sides.

3. Cross-domain uniformity invariant:

   For states drawn from different domains (for example physics, statistics, everyday reasoning), define:

   ```txt
   I_mix = max over m in C_domains of Tension_prob(m)
   ```

   with `C_domains` a finite sample. This invariant tests whether any domain forces systematically higher tension. If `I_mix` sits in medium or high bands on the TU tension scale, the encoding struggles to unify the domains.

### 3.6 Singular set and domain restrictions

Some states may be ill-posed for our observables, for example:

* missing crucial information to determine violations,
* incompatible combinations of tags and constraints that make observables undefined,
* scenarios where any finite representation of the mismatch is impossible.

We define the singular set:

```txt
S_sing = { m in M :
           DeltaS_norm(m) is undefined or not finite,
           or DeltaS_sem(m) is undefined or not finite,
           or DeltaS_ctx(m) is undefined or not finite }
```

We then restrict all Q119 analysis to the regular domain:

```txt
M_reg = M \ S_sing
```

Any attempt to evaluate `Tension_prob(m)` for `m` in `S_sing` is treated as “out of domain” and does not count as evidence for or against any interpretation of probability or any encoding in `E_probMeaning`.

All experiments and protocols in this document are implicitly restricted to states in `M_reg`.

---

## 4. Tension principle for this problem

This block states how Q119 is characterized as a tension problem within TU at the effective layer.

### 4.1 Core tension functional

The core functional for Q119 is:

```txt
Tension_prob(m) = w_norm * DeltaS_norm(m)
                  + w_sem * DeltaS_sem(m)
                  + w_ctx * DeltaS_ctx(m)
```

with the properties:

* `Tension_prob(m) in [0, 1]` for all `m` in `M_reg`,
* `Tension_prob(m) = 0` if and only if:

  * all basic probability norms are respected,
  * interpretation tags and uses are mutually consistent,
  * context features and interpretations are well matched.

We do not assume that any real discourse context realizes zero tension. Instead, we treat zero tension as an ideal target in the TU tension scale.

### 4.2 Unified meaning as low-tension principle

At the effective layer, a strong unification claim for the meaning of probability can be phrased as:

> There exists at least one encoding in `E_probMeaning` and at least one way of assigning states to real-world probability practices such that:
>
> 1. Single-case, frequency, and credence uses of probability can all be interpreted in a unified hybrid scheme using the finite libraries `L_int`, `L_ctx`, and `L_con`.
> 2. For typical or core scientific and everyday contexts, states `m` in `M_reg` that represent those contexts satisfy
>
>    ```txt
>    Tension_prob(m) ≤ epsilon_prob
>    ```
>
>    for a threshold `epsilon_prob` that lies in the low-tension bands defined by the TU Tension Scale Charter and remains bounded as we refine the encoding or add more contexts.

Informally: a unified meaning of probability exists at the effective layer if we can find a stable hybrid encoding in `E_probMeaning` where typical uses do not generate persistent medium or high tension under fair and fixed weights.

### 4.3 Fragmentation or pluralism as persistent high tension

Competing views claim that no single unified meaning is possible and that different notions of probability are fundamentally independent or even in conflict. At the effective layer, such failure of unification can be expressed as:

> For every encoding in `E_probMeaning` and every way of assigning states to a sufficiently rich set of real-world probability practices, there exists a subset of contexts such that:
>
> ```txt
> Tension_prob(m) ≥ delta_prob
> ```
>
> for some strictly positive `delta_prob` that sits in the medium or high bands of the TU tension scale and that cannot be reduced below that band without:
>
> * discarding some core contexts, or
> * changing weights in violation of the fairness constraints, or
> * redefining labels in ways that no longer match their intended meaning.

Informally: if every coherent attempt to unify the meanings runs into inescapable pockets of medium or high tension, then probability meaning is fundamentally fragmented at the effective layer under the constraints of `E_probMeaning`.

---

## 5. Counterfactual tension worlds

We now describe two counterfactual worlds, both strictly at the effective layer and restricted to encodings in `E_probMeaning`.

* World T: unified hybrid meaning of probability (low-tension world).
* World F: irreducible pluralism or fragmentation (high-tension world).

### 5.1 World T (unified hybrid meaning, low tension)

In World T:

1. Core scientific discourse

   * For states `m_T` encoding core scientific uses of probability (for example statistical mechanics, quantum chance, large-scale empirical studies), we have:

     ```txt
     Tension_prob(m_T) ≤ epsilon_core
     ```

     with `epsilon_core` in low-tension bands and stable under reasonable refinements of the encoding and the corpus.

2. Everyday and decision contexts

   * For states encoding everyday decision making and risk assessment using credences and betting behavior, `DeltaS_norm` and `DeltaS_sem` remain low:

     ```txt
     DeltaS_norm(m_T) ≤ epsilon_decision
     DeltaS_sem(m_T)  ≤ epsilon_decision
     ```

     for a threshold `epsilon_decision` comparable to `epsilon_core` on the TU tension scale.

3. Cross-link constraints

   * In contexts where frequencies, chances, and credences interact (for example calibration tasks), the ensemble invariant `I_ensemble` is small:

     ```txt
     I_ensemble ≤ epsilon_link
     ```

     with `epsilon_link` in low-tension bands.

   * No domain (physics, statistics, everyday reasoning) forces systematically higher tension. The cross-domain invariant `I_mix` stays in low or lower-medium bands.

### 5.2 World F (irreducible pluralism, persistent high tension)

In World F:

1. Domain clashes

   * There exist domain-specific samples such that the cross-domain invariant `I_mix` is bounded away from low-tension bands:

     ```txt
     I_mix ≥ delta_mix
     ```

     with `delta_mix` in medium or high bands that cannot be reduced while keeping all domains in scope.

2. Interpretation deadlocks

   * Some contexts require probability talk that can only be interpreted as chance_like, others only as credence_like, and in overlap regions any assignment of tags produces medium or high `DeltaS_sem` or `DeltaS_ctx`.
   * Attempts to repair this by redefining tags either violate the intended meaning of the labels or move important contexts into `S_sing`.

3. Broken ensemble links

   * For ensembles that link frequencies and credences, the invariant `I_ensemble` is bounded below:

     ```txt
     I_ensemble ≥ delta_ensemble
     ```

     with `delta_ensemble` in at least medium-tension bands that remain even as encodings become more precise.

In this world, no encoding in `E_probMeaning` can keep `Tension_prob(m)` in low bands across the full range of practices without sacrificing some core domain or violating fairness constraints.

### 5.3 Interpretive note

These counterfactual worlds are not claims about actual metaphysical truth. They describe patterns of observables and invariants that would characterize success or failure of unification at the effective layer under the finite libraries and encoding class defined above.

They also do not exhaust all possibilities. Real-world practice may sit between World T and World F. The purpose of these worlds is to give clear targets for experiments and audits.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols at the effective layer that can:

* test the coherence of the Q119 encoding,
* distinguish between different probability meaning models within `E_probMeaning`,
* falsify specific choices of observables and weights for Q119.

They do not settle the metaphysical question of what probability really is.

All experiments are conducted only on states `m` in `M_reg`. States in `S_sing` are recorded as out of domain.

### Experiment 1: Corpus-based probability meaning audit

**Goal:**
Test whether the chosen observables and weights produce stable, interpretable tension profiles across diverse probability discourse for encodings in `E_probMeaning`.

**Setup:**

* Build a finite corpus of probability statements drawn from:

  * physics and engineering textbooks,
  * statistics and machine learning papers,
  * decision theory and economics texts,
  * everyday language corpora.
* For each passage, using a fixed encoding in `E_probMeaning`, create a state `m` in `M_reg` by:

  * tagging probability claims with labels from `L_int`,
  * marking context features from `L_ctx`,
  * selecting operative constraints from `L_con`.

**Protocol:**

1. For each `m` in the corpus, compute `DeltaS_norm(m)`, `DeltaS_sem(m)`, `DeltaS_ctx(m)`, and `Tension_prob(m)` in `[0, 1]`.
2. Group states by domain (for example physics, statistics, everyday).
3. Compute invariants `I_single`, `I_ensemble` where applicable, and `I_mix` for each encoding.
4. Repeat the analysis for several encodings within `E_probMeaning` that:

   * differ only in fixed weights `(w_norm, w_sem, w_ctx)` chosen from `W_candidates`,
   * and in explicit, predeclared rules for mapping texts to labels in `L_int`, `L_ctx`, and `L_con`.

**Metrics:**

* Distribution of `Tension_prob(m)` by domain and context type, with reference to TU tension bands.
* Values of `I_single`, `I_ensemble`, and `I_mix` for each encoding.
* Sensitivity of tension profiles to small, predeclared changes in the encoding.

**Falsification conditions:**

* The target of falsification is the Q119 encoding family for `E_probMeaning`, not the TU framework as a whole and not the canonical problem itself.

* If reasonable encodings in `E_probMeaning` produce tension profiles that are:

  * highly unstable under small, predeclared encoding changes, or
  * dominated by artifacts of weight choice rather than by genuine mismatches, or
  * assign medium or high tension to core, paradigmatic uses of probability that are widely regarded as clear,

  then the specific definitions of `DeltaS_norm`, `DeltaS_sem`, `DeltaS_ctx`, or the combination rule for `Tension_prob` are considered falsified for Q119.

* If no encoding in `E_probMeaning` can keep typical core uses in low-tension bands without violating fairness constraints, this provides evidence against strong unification claims as formulated in Section 4.2 at the effective layer.

**Semantics implementation note:**
All observables are treated in the hybrid semantics regime described in Section 0.5. They combine structured symbolic tags with normalized numerical scores. No additional semantic regime is introduced in this experiment.

**Boundary note:**
Falsifying a particular Q119 encoding in `E_probMeaning` does not solve the canonical problem about probability and does not falsify TU. It only rules out one concrete way of embedding the problem into TU under the given libraries and normalization.

---

### Experiment 2: Human concept and calibration probe

**Goal:**
Assess whether the Q119 tension scores track human judgments about good and bad uses of probability across contexts when encodings respect `E_probMeaning`.

**Setup:**

* Design a set of short scenarios in which:

  * agents make probability claims,
  * agents act on those claims in decisions or bets,
  * background contextual information is made explicit.
* Recruit human participants with varied backgrounds, for example:

  * laypersons,
  * scientists,
  * statisticians,
  * philosophers.

**Protocol:**

1. For each scenario, using a fixed encoding in `E_probMeaning`, create a state `m` in `M_reg` with labels from `L_int`, `L_ctx`, and constraints from `L_con`.
2. Ask participants to rate, on simple scales:

   * how coherent or incoherent the probability talk appears,
   * whether they see category errors (for example treating belief as chance),
   * whether they judge the decisions as rational given the expressed probabilities.
3. Compute `DeltaS_norm(m)`, `DeltaS_sem(m)`, `DeltaS_ctx(m)`, and `Tension_prob(m)` for each scenario.
4. Correlate human ratings with tension scores, both at the level of individual components and at the level of the combined `Tension_prob(m)`.

**Metrics:**

* Rank correlations between human coherence judgments and `Tension_prob(m)`.
* Proportion of scenarios that humans rate as clearly coherent while tension scores lie in medium or high bands.
* Proportion of scenarios that humans rate as clearly incoherent while tension scores lie in low bands.

**Falsification conditions:**

* The target of falsification is again the Q119 effective-layer encoding within `E_probMeaning`.
* If tension scores systematically fail to distinguish scenarios that humans judge as clearly coherent from those judged as clearly incoherent, the current observable definitions are considered inadequate.
* If tuning within the fairness constraints cannot repair this mismatch across multiple encodings in `E_probMeaning`, the present Q119 encoding family is rejected as a plausible model of probability meaning in practice.

**Semantics implementation note:**
Human ratings are used as external calibration signals. They are not themselves part of the state representation in `M`. The hybrid representation remains within the fixed label libraries and numerical scores.

**Boundary note:**
Agreement or disagreement with human judgments tests the usefulness of the encoding at the effective layer. It does not settle the metaphysical status of probability or prove that any interpretation is true or false.

---

## 7. AI and WFGY engineering spec

This block describes how Q119 can be used as an engineering module for AI systems within the WFGY framework at the effective layer.

### 7.1 Training signals

We define several training signals that can be attached to AI models that handle probabilistic language and reasoning. Each signal is derived from normalized scores in `[0, 1]`.

1. `signal_prob_norm_violation`

   * Definition: a nonnegative signal proportional to `DeltaS_norm(m)` for states extracted from the model’s own probability claims.
   * Purpose: penalize outputs that violate basic probability-style norms in simple, detectable ways.

2. `signal_prob_semantic_mismatch`

   * Definition: a signal proportional to `DeltaS_sem(m)`, measured on how the model mixes chance_like, frequency_like, and credence_like talk within the same context.
   * Purpose: discourage category errors such as treating personal beliefs as physical chances without any bridge rule.

3. `signal_prob_context_mismatch`

   * Definition: a signal proportional to `DeltaS_ctx(m)`, based on mismatches between context features and chosen interpretation (for example using frequency language in non-repeatable cases without explanation).
   * Purpose: nudge the model toward context-appropriate uses of probability language.

4. `signal_prob_tension_score`

   * Definition: directly equal to `Tension_prob(m)` for selected states.
   * Purpose: provide a general-purpose probability-tension indicator that can be minimized in tasks requiring clean probabilistic reasoning.

### 7.2 Architectural patterns

We outline several module patterns reusing Q119 structures.

1. `ProbMeaningHead`

   * Role: a head attached to internal representations that predicts interpretation tags in `L_int` and context features in `L_ctx`, along with tension scores.
   * Interface:

     * Inputs: internal embeddings for a segment of text or a reasoning trace.
     * Outputs: predicted tag distributions, context feature flags, and estimated `Tension_prob(m)` and its components.

2. `ProbConsistencyFirewall`

   * Role: a filter that checks candidate probability outputs against basic norms and flags or edits high-tension cases.
   * Interface:

     * Inputs: candidate probability claims and their local context.
     * Outputs: adjusted claims or warnings, plus diagnostic contributions from `DeltaS_norm`, `DeltaS_sem`, `DeltaS_ctx`.

3. `ProbWorldSwitcher`

   * Role: a module that allows the system to reason in different counterfactual probability meaning regimes, analogous to World T and World F, while tracking how `Tension_prob(m)` changes.
   * Interface:

     * Inputs: internal state plus a mode flag indicating which regime or interpretation emphasis is assumed.
     * Outputs: revised interpretations and tension summaries under that regime.

### 7.3 Evaluation harness

We propose an evaluation harness for AI models extended with Q119 modules.

1. Task suite:

   * Natural language tasks involving probability statements, for example textbook problems, forecasts, calibration questions, arguments about chance and risk.
   * Logic puzzles where misuse of probability is common.

2. Conditions:

   * Baseline: model without Q119 modules.
   * TU-enhanced: model with `ProbMeaningHead` and `ProbConsistencyFirewall` active and used in generation or post-processing.

3. Metrics:

   * Rate of basic norm violations, for example probability sums outside `[0, 1]` or incoherent conditionalization patterns.
   * Frequency of clear category errors in expert annotation, for example switching without warning between objective chance and subjective credence in the same context.
   * Human-rated coherence of probability reasoning.
   * Average `Tension_prob(m)` across tasks, and its distribution across TU tension bands.

### 7.4 60 second reproduction protocol

A minimal protocol for external users to experience the effect of Q119-style encoding.

* Baseline setup:

  * Prompt: ask a model to explain whether “the probability that a single coin toss yields heads is the same kind of probability as the frequency of heads in a long series of tosses” and to give arguments.
  * Observation: check for conflation of interpretations, missing links, or abrupt shifts between chance, frequency, and credence.

* TU encoded setup:

  * Prompt: repeat the question but instruct the model to:

    * explicitly classify each probability claim as chance_like, frequency_like, or credence_like,
    * point out when interpretation shifts occur,
    * mention possible tension if the interpretations are mixed without explanation.
  * Observation: assess whether the explanation becomes more structured and whether interpretation shifts are clearly marked.

* Comparison metric:

  * Expert or informed ratings of:

    * interpretation clarity,
    * explicit handling of context,
    * internal consistency.
  * Simple aggregate of `Tension_prob(m)` assigned to the two outputs.

* What to log:

  * Prompts, outputs, predicted tags, and tension scores, plus any firewall interventions, so that experiments can be inspected and replicated.

---

## 8. Cross problem transfer template

This block describes reusable components from Q119 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `ProbMeaningProfile`

   * Type: field.
   * Minimal interface:

     * Inputs: a bounded probability discourse context, for example a passage or reasoning trace.
     * Output: a structured profile including tags from `L_int`, context features from `L_ctx`, and operative constraints from `L_con`.
   * Preconditions:

     * The context must contain at least one probability claim and enough information to assign basic tags and context features.
     * The resulting profile must correspond to a state in `M_reg` for tension to be defined.

2. ComponentName: `ProbTensionScore`

   * Type: functional.
   * Minimal interface:

     * Inputs: a `ProbMeaningProfile` instance.
     * Output: a scalar `tension_value = Tension_prob(m)` in `[0, 1]`.
   * Preconditions:

     * The profile must correspond to a state in `M_reg` so that all component observables are defined and finite.

3. ComponentName: `ProbWorldTemplate`

   * Type: experiment_pattern.
   * Minimal interface:

     * Inputs: a description of a domain-specific probability practice, for example scientific forecasting, risk assessment.
     * Output: a pair of effective scenarios analogous to World T and World F, plus a specification of which invariants and tension measures to monitor.
   * Preconditions:

     * The domain practice can be sampled to produce finite sets of discourse contexts that can be encoded into `M_reg`.

### 8.2 Direct reuse targets

1. Q120 (Value of information and knowledge)

   * Reused component: `ProbMeaningProfile` and `ProbTensionScore`.
   * Why it transfers: Q120 needs to evaluate how information changes rational probabilities and decisions. These components provide a consistent way to check whether those probability updates are meaningfully interpreted and norm-consistent.
   * What changes: Q120 adds value and utility observables, while keeping the underlying probability tension structure intact.

2. Q117 (Risk, ruin, and tail events)

   * Reused component: `ProbWorldTemplate`.
   * Why it transfers: Q117 analyzes scenarios where probability meaning interacts with extreme outcomes. World templates allow systematic exploration of different probability interpretations and their impact on risk assessment.
   * What changes: emphasis shifts toward high-stakes and tail-heavy contexts in `L_ctx`, and additional risk-specific observables are added.

3. Q098 (Long-term calibration of AI models under distribution shift)

   * Reused component: `ProbTensionScore`.
   * Why it transfers: Q098 evaluates whether AI probabilities remain meaningful over time. Probability tension scores become part of the calibration and monitoring signals.
   * What changes: `ProbMeaningProfile` is instantiated from AI model outputs rather than human discourse, and additional metrics for temporal drift are included.

4. Q121 (AI alignment problem)

   * Reused component: `ProbMeaningProfile`.
   * Why it transfers: alignment requires that AI systems use probability in ways that are coherent, interpretable, and safe under human norms. Probability meaning profiles make explicit how chances, frequencies, and credences are mixed in alignment-relevant reasoning.
   * What changes: context features are extended to encode safety-critical status and alignment-specific constraints, while the underlying Q119 structures remain in place.

---

## 9. TU roadmap and verification levels

This block explains Q119’s position on the TU verification ladder and the next measurable steps.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of probability meaning has been specified with finite libraries, observables, and a combined tension functional.
  * Basic invariants, normalization to `[0, 1]`, and singular set restrictions are defined for Q119.
* N_level: N2

  * The narrative linking formal norms, interpretation tags, contexts, and tension scores is explicit and internally coherent.
  * Counterfactual worlds (World T and World F) are described in terms of observable patterns rather than metaphysical claims.

### 9.2 Next measurable steps toward E2 and E3

To progress from E1 to E2 and E3 under the TU verification ladder, at least the following steps are needed.

1. E2 step:

   * Implement a working prototype that:

     * takes annotated discourse samples from multiple domains,
     * constructs `ProbMeaningProfile` instances using an encoding in `E_probMeaning`,
     * computes `Tension_prob(m)` and related invariants,
     * publishes the resulting tension profiles and calibration plots as open data with sufficient metadata for independent audit.

2. E3 step:

   * Run the corpus-based audit and human concept probe experiments described in Section 6 with at least two independent encodings in `E_probMeaning`, demonstrating:

     * robustness of key tension patterns under small encoding variations allowed by fairness constraints,
     * clear falsification of at least one naive or ill-designed encoding family for Q119.

These steps maintain the effective-layer boundary while producing concrete, reproducible artifacts that other groups can test.

### 9.3 Long-term role in the TU program

Over the long term, Q119 is expected to:

* Serve as the main anchor for probability-related consistency_tension across the entire BlackHole collection.
* Provide a reference framework for evaluating AI systems that manipulate probabilities in scientific, economic, and everyday contexts.
* Connect philosophical debates about chance, belief, and frequency to concrete metrics and experiments that can be shared across disciplines and laboratories.

---

## 10. Elementary but precise explanation

This block gives a non-technical explanation that remains aligned with the effective-layer description.

People talk about probability all the time. A physicist might say that a particle has a certain probability of decaying in the next second. A statistician might say that a treatment has a certain probability of working. Someone making a decision might say they are seventy percent sure that something will happen.

The central question of Q119 is:

> Are all of these “probabilities” really the same kind of thing, or are we mixing different ideas under one word?

Some uses of probability sound like statements about the world itself, for example how random a process is. Some sound like statements about long-run frequencies, for example “in the long run this happens thirty percent of the time”. Others sound like statements about what we believe or how we should bet.

In the Tension Universe view, we do not start by choosing one interpretation and declaring it the winner. Instead, we:

1. Treat each probability context as a finite configuration that lists:

   * which probability claims are made,
   * which type of interpretation they are using, for example chance-like, frequency-like, credence-like,
   * which basic rules of probability are supposed to apply,
   * what the surrounding context looks like, for example single case versus repeatable process.
2. Define numbers between `0` and `1` that measure:

   * how much the claims violate basic probability rules,
   * how much they mix interpretations in confusing ways,
   * how much they ignore their own context.
3. Combine these numbers into a single tension score called `Tension_prob(m)`.

If `Tension_prob(m)` stays in low bands for a wide range of real-life cases, using a single hybrid scheme, then it looks like we have a unified meaning of probability at the effective layer. If `Tension_prob(m)` keeps jumping into medium or high bands in some domains no matter how carefully we encode things, that suggests probability meaning is fragmented and we need more than one basic picture.

This approach does not answer what probability really is. It gives us:

* a clean way to describe when different uses of probability fit together smoothly,
* a way to detect when we are secretly mixing incompatible ideas,
* tools for testing how humans and AI systems handle probability language in practice.

Q119 is the node that gathers all these questions into one place, so that other problems about risk, information, calibration, and alignment can build on a common structure instead of fighting over the word “probability” without a shared framework.

---

## Tension Universe effective-layer footer

This page is part of the **WFGY / Tension Universe** BlackHole S-problem collection.

### Scope of claims

* This document specifies an effective-layer encoding of the named S-problem, together with observables, tension scores, counterfactual worlds, and experiment patterns.
* It does not claim to prove or disprove the canonical statement in Section 1.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here (state spaces `M`, libraries, observables, tension scores, invariants, counterfactual worlds, and engineering modules) live entirely at the TU effective layer as defined in the TU Effective Layer Charter.
* No assumption is made about the deep generative structure of reality or about any fundamental logic, probability, or ontology beyond what is needed to interpret the observables defined in this page.
* Any mapping from raw data, texts, or systems into the state space `M` must respect the TU Effective Layer Charter and is subject to separate audit.

### Encoding and fairness

* All encodings referenced in this page are required to belong to the admissible encoding classes defined in the TU Encoding and Fairness Charter.
* Differences in tension between worlds, models, or systems must not be attributed to hidden parameter tuning, retrofitting, or case-by-case modifications of the encoding.
* Any concrete implementation derived from this page must document its encoding choices, including weight selection and library definitions, and publish enough metadata for independent verification.

### Tension scale

* All scalar tension quantities on this page are dimensionless scores in the interval `[0, 1]`, interpreted according to the TU Tension Scale Charter.
* Thresholds such as `epsilon_...` and `delta_...` are band markers on this normalized scale. They indicate low, medium, or high tension regimes and do not carry any physical units.
* Comparisons of tension across problems, systems, or worlds are meaningful only when all scores have been computed under encodings that respect the TU Tension Scale normalization.

### Reproducibility and falsifiability

* Suggested experiments and protocols are intended to be implementable by independent groups using the same or compatible encodings.
* Falsifying a particular encoding or tension functional derived from this page does not falsify the TU framework as a whole and does not settle the canonical problem. It only rules out one concrete way of embedding the problem into TU under the stated assumptions.
* Implementations that claim low-tension behavior relative to this page are expected to provide logs, datasets, and configuration details sufficient for re-run and audit.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
