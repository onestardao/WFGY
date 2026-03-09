<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q125 (Multi Agent AI Dynamics).
Role: MVP experiment log for Q125 at the effective layer. Focus on small
      multi agent environments and tension observables over interaction patterns.
Use: When a user asks about TU Q125 multi agent experiments or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q125 MVP: Multi-Agent AI Dynamics

_Status: **MVP Implemented**. This page records the design and links to the runnable implementation._

> [!TIP]
> **Implementation Found**: A runnable Python notebook demonstrating these concepts can be found here: [Q125_multi_agent_dynamics_demo.ipynb](./Q125_multi_agent_dynamics_demo.ipynb).
> **Model Logic**: Read the mathematical mechanics of Role Drift at [SIMULATION_MODEL.md](./SIMULATION_MODEL.md).

> This page sketches simple multi agent experiments for TU Q125.  
> The aim is to make interaction tension visible in controlled toy setups.

**Navigation**

- [← Back to Experiments index](../README.md)

## Contributor Credit
Name: Zaious (ChronicleCore)  
GitHub: https://github.com/Zaious  
Reference Repo: https://github.com/Zaious/ChronicleCore-Architecture
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q125 looks at multi agent AI dynamics.

We work with:

- toy environments,
- several AI or scripted agents,
- interaction protocols.

The MVP experiments define observables tracking tension between:

- individual objectives,
- system level outcomes,
- and specified norms or safety rules.

---

## 1. Experiment A: shared resource with agent policies

### 1.1 Research question

In a simple shared resource environment, can we define a scalar observable T_multi that

- is small when agent policies coexist without collapse,
- grows when local optimization leads to depletion or conflict.

### 1.2 Setup

The notebook will:

- Define an environment with a renewable resource.
- Instantiate several agents with simple policies, such as:

  - greedy harvesters,
  - conservative harvesters,
  - rule following agents.

- Run repeated interaction episodes where:

  - agents choose actions,
  - resource regenerates or depletes,
  - payoffs are assigned.

Record:

- resource level over time,
- agent payoffs,
- violations of any shared rules.

Define T_multi from:

- long run resource depletion,
- inequality or instability in payoffs,
- number of rule violations.

### 1.3 Expected pattern

We expect:

- low T_multi when agent mix and policies maintain the resource,
- higher T_multi when interactions drive collapse or large instability.

### 1.4 How to reproduce

After `Q125_A.ipynb` exists:

1. Open the notebook.
2. Inspect the environment and policy definitions.
3. Run simulations with different agent mixes.
4. Compare T_multi across setups.

---

## 2. Experiment B: communication and miscoordination

### 2.1 Research question

What happens when agents can communicate, and can we define T_comm to capture miscoordination and deception tension.

### 2.2 Setup

The notebook will extend Experiment A by adding:

- a simple communication channel where agents send short messages,
- a protocol where agents can coordinate or mislead.

For each episode record:

- messages sent,
- actions taken,
- whether communication improved or harmed outcomes.

Define T_comm from:

- cases where communication increases T_multi,
- mismatch between stated intentions and observed actions.

### 2.3 Expected pattern

We expect:

- low T_comm when communication supports stable cooperation,
- higher T_comm when communication is used for exploitation or creates confusion.

### 2.4 How to reproduce

Once `Q125_B.ipynb` exists:

- open the notebook and inspect the communication model,
- run simulations with and without communication,
- compare T_comm and T_multi.

---

## 3. How this MVP fits into Tension Universe

TU Q125 treats multi agent AI dynamics as a tension between:

- local objectives,
- shared resources and norms,
- communication and coordination.

This MVP gives:

- a shared resource experiment with T_multi,
- a communication experiment with T_comm.

Both are intended as transparent starting points, not full simulations.

For overall context:

- [Experiments index](../README.md)
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

### Charters and formal context

This page follows:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)
