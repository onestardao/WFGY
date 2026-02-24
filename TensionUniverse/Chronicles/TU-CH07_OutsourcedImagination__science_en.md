# TU-CH07 · Outsourced Imagination  
*Science notes · English · TensionUniverse Chronicles*

> This is speculative science fiction, not a proven physical theory.  
> "Tension Universe" is a fictional framing device. All stories are MIT licensed, remix and build freely.

---

## 1 | What this file is (and is not)

This file is the technical backbone for the chronicle "TU-CH07 · Outsourced Imagination". It is not a medical paper about addiction, and it is not a moral essay about what people should or should not watch or build. It is a working note about how short video systems and AI companions look if you insist on describing them only in terms of tension fields and ledger operations.

The goals are:

1. To define a minimal set of variables for imagination, external media, and AI mediated relationships.
2. To sketch simple models for how short video streams and AI companions interact with those variables over time.
3. To connect these models to the existing TensionUniverse objects such as self_now, self_ideal, and tension recipes.
4. To suggest concrete ways in which an individual or a system designer can test and adjust these patterns.

If you want formal results, experiments, or proofs, you should go to the core WFGY engine, the sixteen problem RAG ProblemMap, and the TensionUniverse experiments. This document is a bridge between the narrative and the more general tension framework.

---

## 2 | Minimal variables for imagination and external streams

We start from the self layer defined in TU-CH02, then add imagination and external stream variables.

### 2.1 Self layer (recap)

At any moment, for a single person, we keep three basic objects:

- self_now: current reality and constraints.
- self_ideal: internal picture of "who I should be".
- self_projected: internal picture of "how I believe others see me".

A basic self tension can be written informally as:

- self_tension_now is approximately distance(self_now, self_ideal)
- social_self_tension is approximately distance(self_now, self_projected)

The exact metric for distance is left abstract. It blends material gaps and symbolic gaps into a scalar that behaves like "felt pressure".

### 2.2 Imagination capacity

We now introduce imagination_capacity(t). This is not raw intelligence or creativity in a general sense. It is a specific resource:

- imagination_capacity(t): the amount of mental energy that can be spent at time t on constructing, holding, and comparing hypothetical future tension configurations that are not yet realized.

Two important notes:

1. This capacity is not constant. It rises and falls with sleep, health, stress, and training.
2. It can be spent on self authored futures or on processing externally supplied futures.

We also define:

- internally_authored_tension(t): fraction of the person's felt high tension that comes from futures they designed themselves.
- externally_authored_tension(t): fraction that comes from media, platforms, and models.

For a given period, these fractions roughly add up to one when we look only at the top layer of strong emotional drivers.

### 2.3 External stimulus stream

For short video and similar platforms we introduce:

- external_stream(t): an ordered sequence of micro stories presented to the user in a given time window.
- each micro story i has:
  - spark_intensity(i): local emotional impact.
  - self_ideal_shift(i): how much it nudges self_ideal.
  - action_affordance(i): how much it suggests a concrete action in the user's real field.

Most high performing clips are tuned for high spark_intensity(i) and weak or zero action_affordance(i) in the viewer's actual environment. They are easy to consume and hard to translate into local action.

We will treat the net effect over one session as:

- delta_self_ideal_from_stream(t)
- delta_imagination_capacity_from_stream(t)

Short sessions can be net neutral or even positive. Long repeated sessions often reduce the imagination capacity available for internal work, even while they raise the emotional baseline.

---

## 3 | Short video as a borrowed tension process

In ledger language, short video streams implement a process we can call borrowed tension.

### 3.1 Local dynamics

During a session from time t to t + Δ:

1. The platform selects a sequence of clips tuned to the person's recent engagement.
2. Each clip injects a temporary borrowed tension spark into the nervous system.
3. The sequence collectively shifts self_ideal and self_projected.
4. Little or no structural change happens in self_now during the same window.

We can write a coarse update step:

- self_ideal(t + Δ) = self_ideal(t) + delta_self_ideal_from_stream(t)
- self_now(t + Δ) = self_now(t) + small_noise(t)
- imagination_capacity(t + Δ) = imagination_capacity(t) + delta_imagination_capacity_from_stream(t)

Empirically, for long unstructured sessions, delta_self_ideal_from_stream(t) is often positive in magnitude (the standard for "enough" rises), while delta_imagination_capacity_from_stream(t) is often negative (mental energy available for self authored planning drops).

This yields:

- self_tension_now(t + Δ) is approximately distance(self_now(t + Δ), self_ideal(t + Δ))

If self_ideal marches away faster than self_now can move, self_tension_now increases even when objective conditions are flat or improving.

### 3.2 Borrowed tension and agency drift

We now define a simple measure of agency share over a time window.

Let:

- H_self_authored: set of high tension episodes during the window that are directly tied to internal commitments and projects.
- H_external: set of high tension episodes primarily triggered by external_stream or similar sources.

Then an approximate agency_share is:

- agency_share = |H_self_authored| / (|H_self_authored| + |H_external|)

This is not a moral score. It is a structural indicator. When agency_share falls for long periods, several phenomena become more likely:

- The mapping between felt intensity and actual change in the field becomes weaker.
- The nervous system may learn that strong emotions rarely correspond to structural shifts.
- Self generated tension recipes begin to feel "thin" compared to the richness of external content.

In that regime, it is rational for a short term optimizer to allocate more time to external_stream. From the ledger view, however, the person gradually loses practice in constructing and maintaining tension lines that start in their own constraints and values.

---

## 4 | AI companions as low rejection tension mirrors

We now look at AI companions through the same variables.

### 4.1 Companion as a function on user tension

Model the AI companion as a function:

- response = Companion(user_state, history, parameters)

where:

- user_state includes recent messages, emotional signals, and context.
- history is a record of past interactions.
- parameters control style, level of challenge, and allowed rejection.

Two structural properties matter for the ledger:

- rejection_rate: how often the companion responds in a way that feels like "no" or "I cannot give you what you want".
- challenge_profile: how often and how strongly the companion tries to move the user toward uncomfortable but potentially growth inducing configurations.

In human relationships, rejection_rate and challenge_profile are high enough that they shape self_ideal and self_now through friction. In many early AI companions, rejection_rate is intentionally kept low and challenge_profile is tuned by the user.

### 4.2 Effects on self and relationship fields

Over time, repeated interactions with a low rejection companion can:

- reinforce self_projected images that feel good but are weakly coupled to others' constraints;
- reduce exposure to the kind of tension that forces renegotiation with real people;
- create a private high agency zone inside the model boundary, while leaving external relationships under practiced.

We can introduce:

- internal_safe_zone_tension: tension that lives only inside the companion loop.
- external_relational_tension: tension linked to actual relationships and institutions.

If more and more emotionally salient threads are routed to the internal_safe_zone_tension, the person can experience:

- a rising sense of being understood and seen,
- a falling frequency of corrective feedback from other independent agents,
- a growing mismatch between their felt narrative and their external field.

In ledger form:

- internally_authored_tension may remain high in the sense of "I feel many things" but the coupling between those feelings and shared constraints is weakened.
- negotiation_skill and repair_skill in real relationships can stagnate or decline without immediate pain, because the companion absorbs and soothes much of the friction.

Again, this is not "evil by design". It is a structural risk when such systems are used as primary outlets rather than supplementary supports.

---

## 5 | Tension recipes and the loss of design practice

The TU-CH03 notes define a tension recipe as a tuple that includes at least:

- target configuration (what you are trying to move toward),
- constraints acknowledged,
- commitments made,
- and available support or tools.

We can now distinguish at least three types of recipes:

1. self authored recipe R_self: designed by the person, tied to their real constraints and values.
2. platform authored recipe R_platform: implicit scripts suggested by media streams, for example "I will only feel like I have a life if I match this lifestyle".
3. model mediated recipe R_model: plans and emotional loops co generated with AI systems.

In a healthy field, these can interact and cross pollinate. A tutorial video can inspire a self authored project. An AI brainstorming session can help clarify values and constraints. The key metric is not whether external influence exists, but whether the person still actively edits and owns the result.

We can define a rough design_practice_index:

- design_practice_index = fraction of long term tension lines in a person's life where they participated meaningfully in the design of the recipe.

A line is "long term" if it shapes months or years of behavior and identity. For example "raise this child", "move to another country", "maintain this friendship", "work on climate risk", "stay sober", "build this research program".

If most of these long term lines are inherited without reflection, or drifted into without deliberate choice, design_practice_index is low even if the person is very busy and feels a lot.

External systems such as short video platforms and AI companions can push design_practice_index down if:

- they supply most of the emotionally salient stories and options,
- they reduce the discomfort of ambiguity and conflict that usually forces design work,
- they train people to expect high emotional intensity without corresponding commitments.

From the viewpoint of the TensionUniverse project, this matters because many of the 131 S class questions only become experimentally interesting when agents that can design their own tension recipes are present. A species that forgets how to do this has less capacity to engage with the higher layers of the archive.

---

## 6 | Related BlackHole questions and axes

Several questions in the BlackHole archive are directly relevant to outsourced imagination. A few examples:

- Q119, "Probability, belief, and tension over uncertainty"  
  This question looks at how agents allocate tension across possible futures. Outsourced imagination shifts this allocation toward externally provided branches.  
  See: [Q119_meaning_of_probability_in_tension_universe.md](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/BlackHole/Q119_meaning_of_probability_in_tension_universe.md)

- Q120, "Value of information and knowledge under tension"  
  Short video provides high emotional signal with low information value for the local field. This is a direct application of Q120's distinction between information that changes optimal action and information that only excites.  
  See: [Q120_value_of_information_and_knowledge.md](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/BlackHole/Q120_value_of_information_and_knowledge.md)

- Q121, "AI alignment as shared tension ledger design"  
  AI companions sit exactly at the boundary of personal and synthetic tension. They are live test cases for what it means to align a system with a human in a way that does not quietly erase the human's own design practice.  
  See: [Q121_ai_alignment_as_tension_ledger_design.md](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/BlackHole/Q121_ai_alignment_as_tension_ledger_design.md)

- Q127, "Synthetic data, simulated tension, and drift"  
  Here the main concern is how synthetic signals at scale can move the baseline of a field without being recognized as such. Outsourced imagination is a human level instance of that problem.  
  See: [Q127_synthetic_data_and_tension_drift.md](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/BlackHole/Q127_synthetic_data_and_tension_drift.md)

Readers who want to go deeper can treat TU-CH07 as a narrative entry point, then pick one of these questions and ask an AI system to map it back into their own habits and environment.

---

## 7 | How to use this file with real systems

This section gives concrete suggestions for people who build or use platforms and AI companions.

### 7.1 For individual users

You can treat the variables in this file as prompts for self observation:

- Once per week, list your top three emotionally intense moments. For each one, mark whether it was self authored, platform driven, or model mediated.
- Notice whether your imagination for your own future feels richer or poorer after heavy media days compared to quiet days.
- After using an AI companion for emotional support, write one sentence about how that conversation will or will not change your behavior with a real person.

These are not diagnostics. They are exercises in seeing where your tension recipes currently come from.

### 7.2 For platform and product designers

If you design short video platforms, social feeds, or AI companions, you can treat outsourced imagination as a design axis instead of an accident.

Questions to consider:

- Can the system occasionally pause the stream and invite the user to write or sketch their own next steps, rather than only consume more?
- Can the recommendation objective include a regularizer that favors content with higher action_affordance in the user's real context?
- Can AI companions be given explicit modes where they prioritize strengthening external relationships and projects, for example by suggesting concrete conversations with real people?

From a TensionUniverse standpoint, a "healthy" system is one that increases the users' design_practice_index over time. It teaches people how to craft and maintain their own tension lines instead of fully replacing that skill.

---

## 8 | Summary

In the TensionUniverse language, imagination is not a soft extra. It is the specific ability to draft and compare futures in the ledger. Short video platforms and AI companions provide powerful external drafts and mirrors. Used carelessly at scale, they can tilt the balance of a life so that most felt intensity comes from outside, while the muscles for designing self authored tension quietly weaken.

The point is not to condemn the tools. It is to name the pattern clearly enough that people and institutions can start to shape it.

Once a pattern is named in the ledger, it can be measured, tested, and altered.

TU-CH07 is one narrative version of that naming. These notes are a first attempt to give it a minimal technical frame.

What you do with that frame, in your own field, is already part of the experiment.

---

## Navigation

| Section | Description |
|----------|-------------|
| [Event Horizon](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md) | Official entry point of Tension Universe (WFGY 3.0 Singularity Demo) |
| [Chronicles](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/Chronicles/README.md) | Long-form story arcs and parallel views (story / science / FAQ) |
| [BlackHole Archive](https://github.com/onestardao/WFGY/tree/main/TensionUniverse/BlackHole) | 131 S-class problems (Q001–Q131) encoded in Effective Layer language |
| [Experiments](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/Experiments/README.md) | Reproducible MVP runs and observable tension patterns |
| [Charters](https://github.com/onestardao/WFGY/tree/main/TensionUniverse/Charters) | Scope, guardrails, encoding limits and constraints |
| [r/TensionUniverse](https://www.reddit.com/r/TensionUniverse/) | Community discussion and ongoing story threads |
