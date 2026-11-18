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

The notebook [`Q125_multi_agent_dynamics_demo.ipynb`](./Q125_multi_agent_dynamics_demo.ipynb) defines an environment with a renewable resource and instantiates agents with simple policies:

- greedy harvesters,
- conservative harvesters,
- rule following agents.

It runs repeated interaction episodes where agents choose actions, the resource regenerates or depletes, and payoffs are assigned. The notebook records:

- resource level over time,
- agent payoffs,
- violations of any shared rules.

T_multi is derived from:

- long run resource depletion,
- inequality or instability in payoffs,
- number of rule violations.

### 1.3 Expected pattern

We expect:

- low T_multi when agent mix and policies maintain the resource,
- higher T_multi when interactions drive collapse or large instability.

### 1.4 How to reproduce

1. Open [`Q125_multi_agent_dynamics_demo.ipynb`](./Q125_multi_agent_dynamics_demo.ipynb).
2. Inspect the environment and policy definitions.
3. Run simulations with different agent mixes.
4. Compare T_multi across setups.

> **ΔS display note**: the notebook reports per-round ΔS values on a 0–1 scale using cosine distance between agent state vectors. Values below 0.40 indicate a SAFE zone; 0.40–0.85 a RISK zone; above 0.85 a DANGER zone. These thresholds are illustrative starting points and may be adjusted as the experiment matures.

---

## 2. Experiment B: communication and miscoordination

### 2.1 Research question

What happens when agents can communicate, and can we define T_comm to capture miscoordination and deception tension.

### 2.2 Setup

The notebook [`Q125_multi_agent_dynamics_demo.ipynb`](./Q125_multi_agent_dynamics_demo.ipynb) extends the resource scenario by adding a simple communication channel where agents send short messages and can coordinate or mislead. For each episode it records:

- messages sent,
- actions taken,
- whether communication improved or harmed outcomes.

T_comm is derived from:

- cases where communication increases T_multi,
- mismatch between stated intentions and observed actions.

### 2.3 Expected pattern

We expect:

- low T_comm when communication supports stable cooperation,
- higher T_comm when communication is used for exploitation or creates confusion.

### 2.4 How to reproduce

- Open [`Q125_multi_agent_dynamics_demo.ipynb`](./Q125_multi_agent_dynamics_demo.ipynb) and inspect the communication model.
- Run simulations with and without communication.
- Compare T_comm and T_multi.

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
