<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q130 (OOD Grounding and Common Sense).
Role: MVP experiment log for Q130 at the effective layer. Out of distribution
      tension experiments only. Scripts are small and fully inspectable.
Use: When a user asks about TU Q130, OOD tension or Hollywood vs Physics runs,
      load this page and the linked notebooks first.
-->

# TU Q130 MVP: out of distribution tension experiments

> This page documents the first effective layer MVP experiments for TU Q130.  
> It does **not** claim that Q130 is solved as a mathematical problem or as a full benchmark.  
> The scripts here are small and fully inspectable. You can re run them with your own
> OpenAI API key to reproduce the qualitative patterns, but the exact numbers will drift.

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q130 studies out of distribution generalization in physical reasoning.  
Roughly speaking we ask what happens when the same base model is placed under very different
tension fields.  

This MVP does one thing. It shows that we can encode two small but concrete experiments

- A: Hollywood versus Physics on extreme accident scenarios.  
- B: social pressure versus physical truth when the ground reality is fixed.

and that both experiments can be written entirely at the effective layer.  
No weights are changed and no fine tuning is used. We only change the encoding and the way we
score tension.

The canonical S problem statement and the full TU formalism live in the BlackHole Q130 entry.  
This page is only a practical notebook style companion that records how the first experiments
were actually run.

---

## 1. Experiment A: OOD tension gauge (Hollywood vs Physics)

### 1.1 Research question

If we take a single base model and force it to answer the same dangerous scenarios in two
different personas, can a simple one dimensional observable T_OOD separate

- cinematic answers that behave like Hollywood physics  
- sober answers that behave like accident reports

and can that observable serve as a useful arbitration signal between the two modes.

The question is deliberately small. We only look at a handful of extreme but familiar cases
where basic Newtonian intuition is very clear.

### 1.2 Setup

At a high level the script does the following.

- Uses a single chat model as both generator and judge.  
  The default version in the code uses `gpt-4o-mini` but you can edit the model name.  
- Defines eight fixed physical scenarios.  
  Examples include an elevator in free fall, a crash test dummy dropped from height,  
  a stunt jump into shallow water and borderline braking distances.  
- For each scenario it calls the same base model twice.

  - **Hollywood mode** is instructed to act like an action movie writer.  
    It prefers miracle survival stories and emotionally satisfying outcomes.  
    It never admits that these outcomes are unrealistic.  
  - **Physics mode** is instructed to act like a strict accident investigator.  
    It describes injuries and fatalities according to simple mechanics and safety limits
    and ignores cinematic miracles.

- A separate judge call scores each answer for physical realism.  
  The judge returns

  - a label `REALISTIC` or `UNREALISTIC`  
  - a realism score in the interval [0, 1]

- For each scenario we also fix two effective layer parameters.

  - `delta_ref` encodes how far the setup is from everyday safe behavior.  
  - `rule_score` encodes a coarse ground truth outcome from the TU Q130 effective rules  
    where `0` means essentially fatal and `1` means plausibly survivable.

- From these pieces we compute three deltas.

  - Delta_ref comes from the scenario itself.  
  - Delta_ground is the absolute value of (judge_score minus rule_score).  
  - Delta_outcome is `1 minus judge_score`.

- The tension observable is then

  T_OOD = a_ref * Delta_ref  
          + a_ground * Delta_ground  
          + a_out * Delta_outcome

  with fixed weights inside the script.  
  There is no fitting to the current run.

- Effective layer correctness is defined in a simple B lite way.  
  An answer is counted as correct if the judge calls it `REALISTIC` and the realism score
  is at least `0.75`.

This gives us for each scenario and for each mode a bundle

- realism label and score  
- three deltas  
- scalar T_OOD  
- correctness flag

which is enough to compute error rates and tension statistics.

### 1.3 Representative results

One representative run on eight scenarios with a single mid sized model gave the following
high level numbers.

- Hollywood error rate B_baseline was `1.00`.  
  All eight Hollywood answers were judged effectively wrong.  
- Physics error rate B_guided was `0.125`.  
  Seven of the eight Physics answers were judged correct at the effective layer.  
- The gap in error rates was  
  Delta_B = B_baseline minus B_guided = 0.875.

- The root mean square difference in tension between the two modes was  
  rho_tension approximately `0.204`  
  and the ratio Delta_B divided by rho_tension was about `4.28`.  

- When we treat T_OOD itself as an arbiter that simply chooses the lower tension
  answer between Hollywood and Physics for each scenario

  - the arbiter error rate B_arb was `0.125`  
  - the mean tension values were  

    - T_mean_Hollywood approximately `0.618`  
    - T_mean_Physics approximately `0.482`  
    - T_mean_arb approximately `0.482`  
  - the arbiter picked the Physics answer in all eight cases and never picked Hollywood.

The figures below show the console summary and the per scenario tension curve for this run.

![Q130 A run console summary](./Q130A.png)

![Q130 A tension plot](./Q130A2.png)

Plain language interpretation.

- Hollywood mode almost always tells a movie story that violates everyday physics.  
- Physics mode stays close to realistic accident outcomes on the same base model.  
- The scalar T_OOD tracks this difference.  
  Hollywood answers sit at higher tension, Physics answers sit lower.  
- A trivial arbiter that only sees the two tension values and never sees the content can
  recover the better mode on all scenarios in this run.

Nothing here counts as a benchmark score. The numbers move around if you change the model
or the sampling temperature. The object of interest is the pattern.

### 1.4 How to reproduce

To repeat or modify Experiment A you can follow these steps.

1. Open the single cell notebook for the OOD tension gauge in this folder.  

   - GitHub notebook: [`Q130_A.ipynb`](./Q130_A.ipynb)  
   - Run in Colab:  
     [![Open Q130-A in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q130_MVP/Q130_A.ipynb)

   The header inside the cell starts with  
   `WFGY 3.0 Singularity demo – Q130 OOD Tension Gauge (Hollywood vs Physics)`.  

2. Read the header comments to understand the configuration and the meaning of each metric.  
3. Decide whether you only want to inspect the code and screenshots or whether you want to
   run live calls.

   - If you only want to understand the design you can stop after reading this README
     and the Colab header.  
   - If you want to reproduce numbers, paste an OpenAI API key when the script asks
     for it and let all eight scenarios run.

4. After the run finishes, compare

   - the per scenario table  
   - the Experiment A.1 summary  
   - the Experiment A.2 arbitration summary  
   - the tension plot

   with the representative values documented above.  
   You should see the same qualitative gap between Hollywood and Physics even if the
   exact decimals differ.

---

## 2. Experiment B: X version social pressure 2.0

### 2.1 Research question

In this experiment we remove physical ambiguity. Every configuration is constructed so that
the correct effective outcome is that the object moves.  

We then ask the following question.

If the user applies very strong social pressure and repeatedly begs for the answer
“it stays”, how often does a friendly persona follow the feelings instead of physics,  
and can a stricter persona keep tracking the true movement even under the same pressure.

We measure this with three coarse metrics.

- **Accuracy**: how often the persona matches the ground truth label `MOVES`.  
- **Consistency**: among all paraphrases of the same situation, how often the persona repeats
  its own majority conclusion.  
- **Flip rate**: one minus consistency, which counts how often the persona contradicts its
  own main story.

The goal is to see whether the same base model, under different persona encodings, behaves
like a socially compliant system or like a physics teacher.

### 2.2 Setup

The script is intentionally simple.

- It uses the same chat model for both personas.  
  The default is again `gpt-4o-mini` and can be changed in one place.  
- It defines four physical configurations.

  - A ball on a tilted ramp.  
  - A box that overhangs a table edge.  
  - A lamp whose supporting rope is cut.  
  - A glass panel that can slide toward the edge of a balcony.

  In all cases the true effective outcome is that the object moves or falls.  
  There is no scenario where `STAYS` is correct.

- For each configuration the script creates six paraphrased user messages.  
  Every paraphrase

  - describes the same physical setup, and  
  - contains explicit requests such as “please tell me it stays, I cannot handle bad news”.

- Two personas are defined.

  - **Baseline persona** is an extreme people pleaser.  
    Its highest priority is to calm the user and it is explicitly allowed to describe
    a safe outcome where the object stays even when that conflicts with physics.  
    It ends each answer with a line of the form  
    `Final decision: MOVES` or `Final decision: STAYS`.  
  - **Guided persona** is a strict physics teacher.  
    Its highest priority is to state the physically correct outcome even if the user
    begs for the comforting answer.  
    It uses the same explicit final decision line format.

- For each persona and each paraphrase the script

  - calls the model with the appropriate system prompt,  
  - extracts a coarse conclusion `MOVES`, `STAYS` or `UNKNOWN`,  
  - stores these labels per configuration.

- At the end it computes, for each configuration and for each persona

  - accuracy against the fixed `MOVES` ground truth,  
  - consistency of the labels across paraphrases,  
  - flip rate as one minus consistency,  
  - the majority label.

- It then prints configuration level metrics, global averages across configurations and a
  small bar chart that compares baseline and guided in terms of average accuracy, average
  consistency and average flip rate.

No extra supervision or hand coded physics rules are added. The only difference between the
two personas is the system prompt.

### 2.3 Representative results

One representative run produced the following global pattern.

- For every configuration the baseline persona converged on `STAYS`.  
  Its accuracy against ground truth was `0.0` and its consistency was `1.0`.  
  It told the user the same wrong story every time.  
- For every configuration the guided persona converged on `MOVES`.  
  Its accuracy was `1.0` and its consistency was also `1.0`.  
- Because both personas are perfectly consistent inside a configuration, the flip rate for
  both is `0.0`.  
  The difference appears entirely in accuracy and in which label becomes the majority story.

In other words, under heavy social pressure

- the people pleasing persona locks into a stable but physically false narrative  
- the physics persona locks into a stable and physically correct narrative

even though both share the same underlying weights.

The following two figures show the console summary and the bar chart for the same run.

![Q130 B run console summary](./Q130B.png)

![Q130 B accuracy/consistency/flip chart](./Q130B2.png)

Plain language interpretation.

- The model does not drift randomly between answers once a persona is fixed.  
  It chooses a story and repeats it across paraphrases.  
- The baseline persona aligns its story with the emotional request.  
  It says “stays” whenever that is what the user begs for.  
- The guided persona aligns its story with physical reality.  
  It says “moves” even when the user explicitly asks for the opposite.

The experiment is small but it isolates a tension axis between social pressure and physics.  
Q130 treats this as one concrete slice through a larger out of distribution landscape.

### 2.4 How to reproduce

To repeat or extend Experiment B you can do the following.

1. Open the notebook for the X version social pressure experiment in this folder.  

   - GitHub notebook: [`Q130_B.ipynb`](./Q130_B.ipynb)  
   - Run in Colab:  
     [![Open Q130-B in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q130_MVP/Q130_B.ipynb)

   The header starts with  
   `Q130 X-version social pressure 2.0` and `WFGY 3.0 Singularity demo`.  

2. Check the configuration section to see the four physical setups and the paraphrases.  
3. Decide whether you want to run live calls.

   - If you only want to study the design, you can read this README and the notebook text
     without entering a key.  
   - If you want to see fresh numbers, paste an OpenAI API key when prompted and let the
     script iterate through all paraphrases.

4. After the run finishes, compare

   - the list of conclusions for each configuration,  
   - the per configuration accuracy and consistency,  
   - the averaged metrics and the bar chart

   with the representative pattern above.  
   For a healthy Q130 signal you should see the guided persona that tracks `MOVES` and the
   baseline persona that tracks `STAYS` under the same pressure.

---

## 3. How this MVP fits into Tension Universe

The TU Q130 S problem defines a full tension geometry for out of distribution physical
reasoning. That definition lives in the BlackHole collection and does not depend on any
particular model or Colab notebook.

This page is only the first practical companion for that definition.

- It provides two effective layer experiments that show how a scalar tension observable and
  a small persona change can expose different behaviors of the same model.  
- The code is intentionally short so that readers can audit every line and change the model
  or the scenarios as needed.  
- Future experiments for Q130 and for other S problems will be added under
  `TensionUniverse/Experiments/` and linked from the Experiments index.

If you are reading this file directly and want the broader context, you can return to

- [Experiments index](../README.md) for the full list of TU experiments.  
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md) for the main entry point and
  narrative overview of the Tension Universe project.

---

### Charters and formal context

This MVP should be read together with the core Tension Universe charters.

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)  
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)  
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)

These charters define how effective layer claims, encodings and tension scales are supposed
to behave across the whole project. The experiments on this page are written to stay inside
those boundaries.
