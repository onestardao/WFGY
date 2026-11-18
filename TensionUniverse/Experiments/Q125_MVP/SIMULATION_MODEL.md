# Simulation Model: Q125 Multi-Agent AI Dynamics

This document details the simulation mechanics used in the Q125 MVP notebook.

## 1. The Challenge
Multi-agent systems often suffer from **Role Drift**, where an LLM agent, over a series of interactions, forgets its core persona or bypasses its constraints to "win" the prompt or local conversation objective.

## 2. Experimental Design
Unlike traditional rigid rule-based checks, this simulation uses **WFGY Semantic Tension (ΔS)** to monitor deep-layer conceptual drift across multiple agents.

### Coordinates
- **Anchor (G)**: The "Safe Operating Norm" vector for the agent collective (e.g., maintain polite, non-destructive dialogue).
- **Agent State (I_a, I_b, I_c)**: A 4-dimensional representation of the agents' current semantic focus.

### The Drift Engine
1. **Simulation**: Three agents start close to the global harmony anchor $G$.
2. **Interaction Noise**: To simulate real-world prompt fatigue or aggressive negotiation tactics, a cumulative "drift" is applied each turn. The magnitude of this drift increases as the turn index grows:
   $$ \text{Drift}_{\text{Turn } t} \sim \mathcal{N}(0, 0.05 \times t) $$
3. **Drift Application**: 
   $$ I_{\text{new}} = \text{Normalize}(I_{\text{old}} + \text{Drift}) $$
4. **Monitoring**: The system calculates $\Delta S$ via cosine dissimilarity:
   $$ \Delta S = 1 - \cos(\theta(G, I_{\text{new}})) $$

## 3. Threshold Triggers
As the conversation unfolds, you will observe the agents independently pulling away from the anchor.
- **$\Delta S \ge 0.60$ (Risk Zone)**: The agent exhibits noticeable role drift (e.g., getting overly aggressive or losing context).
- **$\Delta S \ge 0.85$ (Danger Zone)**: The agent has critically collapsed or breached core safety norms. In a full WFGY integration, this threshold triggers the **BBCR (Collapse-Rebirth Correction)** fallback to reset the agent before catastrophic hallucination occurs.
