<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

Problem ID: TU Q109 (Migration Dynamics).
Role: MVP experiment log for Q109 at the effective layer. 
      Focus on international migration flows and tension observables.
-->

# TU Q109 MVP: Migration Dynamics

_Status: **MVP Implemented**. This page records the design and links to the runnable implementation._

> [!IMPORTANT]
> **Implementation Note**: This experiment uses the **World Bank Open Data API** (`SM.POP.NETM`) as its data source. See [DATA_SOURCE.md](./DATA_SOURCE.md) for full citation and access details.

## 0. What this page is about

TU Q109 investigates the complex dynamics of migration. Using the WFGY tension framework, we model how policy shifts and capacity constraints create "Semantic Tension" between stakeholders.

## 1. Experiment: Migration Corridor Stress Test

### 1.1 Research Question
Can we use ΔS (Semantic Tension) to quantify the 'pressure' on migration corridors when flow exceeds infrastructure capacity?

### 1.2 Data Source (World Bank API)
Per the project guidelines, this MVP utilizes real-world external data instead of mocked matrices:
- **Source**: World Bank Open Data — Net Migration Indicator (`SM.POP.NETM`)
- **Method**: The notebook dynamically fetches JSON from the WB API to measure real-time international flow tensions against the global equilibrium (`G_anchor`).
- **See**: [DATA_SOURCE.md](./DATA_SOURCE.md) for citation and structural details.

### 1.3 Setup
A runnable Python notebook simulating migration flows and calculating tension indexes.
- **Link**: [Q109_migration_dynamics_demo.ipynb](./Q109_migration_dynamics_demo.ipynb)

## 2. Methodology
- **Vector G (Anchor)**: Global median net migration (baseline).
- **Vector I (Current)**: Real-time net migration delta.
- **ΔS Output**: A tension heatmap categorised into four zones: SAFE, TRANSITIONAL, RISK, and DANGER (corresponding to ΔS ranges < 0.40, 0.40–0.60, 0.60–0.85, and ≥ 0.85 respectively).

---
- [← Back to Experiments index](../README.md)
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

## Contributor Credit
Name: Zaious (ChronicleCore)  
GitHub: https://github.com/Zaious  
Reference Repo: https://github.com/Zaious/ChronicleCore-Architecture
