# Simulation Model: Q107 Large Scale Collective Action

This document outlines the theoretical logic and mathematical modeling behind the Q107 MVP notebook.

## 1. The Paradigm
In traditional game theory (e.g., Public Goods Games), tension is usually measured by utility or payoff deficits. **WFGY Tension Universe (TU Q107)** shifts this paradigm towards **Semantic Tension (ΔS)** — measuring the alignment between an agent's internal "belief state" and the collective "goal state".

## 2. Core Variables
- **G (Collective Goal Vector)**: Represented as a normalized vector (e.g., `[1.0, 0.0]`). This represents perfect alignment with the public good (e.g., full cooperation).
- **$I_i$ (Agent Belief Vector)**: The current internal state of Agent $i$. In this simulation, each agent starts with a belief closely aligned with $G$, but subject to variance.
- **Noise ($\epsilon$)**: A dynamic variable representing individual incentives, miscommunication, or "free-riding" temptations.

## 3. Simulation Loop
1. **Initialization**: $N$ agents (e.g., 100) are placed in the environment, forming a tightly clustered vector field around $G$.
2. **Turn Execution**: Each turn, agents experience a random noise $\epsilon$ added to their belief vector:
   $$ I_{i, t+1} = \text{Normalize}(I_{i, t} + \epsilon) $$
3. **Tension Calculation**: The system continually calculates the semantic tension between the group's average belief direction and the anchor $G$:
   $$ \Delta S_{i} = 1 - \cos(\theta(I_i, G)) $$
   Tension increases as the collective alignment "drifts" into a fragmented state.

## 4. Academic Alignment
This model strictly adheres to the WFGY 2.0 definition of ΔS. Instead of predicting individual actions, it monitors the **structural stability** of the group's narrative. Once average ΔS breaches $0.6$, the collective action is formally categorised as entering a "Risk Zone" of dissolution.
