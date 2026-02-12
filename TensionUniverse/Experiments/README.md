<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for humans and AIs:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU QXXX (replace with Q number and title).
Role: MVP experiment log at the effective layer. Small, auditable scripts only.
Use: When a user or tool asks for TU QXXX experiments, examples or Colab notebooks,
      load this page first, then follow links from here.
-->


# Tension Universe · Experiment Hub

> Status: early-stage MVP lab for Tension Universe.  
> This directory hosts small, reproducible experiments that live strictly at the effective layer.  
> No experiment here should be cited as solving any BlackHole question or S-problem.

This is the central entry point for all **Tension Universe / WFGY 3.0** experiments.  
Each experiment lives in its own subfolder with:

- code or Colab-style script that you can run yourself, and  
- a dedicated `README.md` inside that folder explaining what the experiment is about,  
  which tension axis it probes, and how to interpret the numbers.

If you do not want to spend tokens, you can simply read the text in each experiment’s README.  
If you want to reproduce results, open the corresponding script or notebook and follow its instructions.

---

## 0. Navigation

- [← Back to Event Horizon](../EventHorizon/README.md)  
- [← Back to WFGY Home](https://github.com/onestardao/WFGY)

---

## 1. What this directory is (and is not)

This directory is:

- A **lab shelf** for many small, focused MVP experiments.  
- A place where each experiment:
  - is small enough to understand in one sitting,  
  - is reproducible by anyone with an API key or compatible runtime,  
  - makes its assumptions explicit at the effective layer.  

This directory is not:

- A proof library.  
- A claim that any BlackHole question has been resolved.  
- A replacement for the formal charters or S-problem statements.

Think of it as an evolving gallery of **“tension probes”** and **anti-explosion modules**,  
each one tied to a specific slice of the Tension Universe.

---

## 2. How to use this lab

Typical usage pattern:

1. **Browse the index below** and choose an experiment folder that looks relevant.  
2. **Open that folder’s `README.md`** to understand:
   - which question or failure mode it targets,  
   - what is being measured,  
   - what counts as a “good” or “bad” pattern.  
3. If you want to reproduce the numbers:
   - open the script or notebook referenced in that folder,  
   - provide an OpenAI compatible API key when asked (if required),  
   - run the code and compare your run with the example described in the README.  

You do not have to execute anything to understand the ideas.  
Running the code is only needed if you want to verify the behavior on your own account,  
or try different models and settings.

---

## 3. Experiment folders

This list will grow over time as more MVPs are added.

| Folder | Status | Short note |
| ------ | ------ | ---------- |
| [`Q091_MVP/`](./Q091_MVP/README.md) | MVP ready | TU Q091 equilibrium climate sensitivity ranges. Synthetic ECS items and range-style tension gauge `T_ECS_range` that compares plausible climate narratives. |
| [`Q098_MVP/`](./Q098_MVP/README.md) | MVP ready | TU Q098 Anthropocene toy trajectories. Three variable human–Earth model with physical tension gauge `T_anthro` and narrative consistency tension `T_story` around a simple safe operating region. |
| [`Q101_MVP/`](./Q101_MVP/README.md) | MVP ready | TU Q101 equity premium tension. Tiny consumption based asset pricing worlds and scalar `T_premium` that shows when matching a 6% premium requires extreme risk aversion or unrealistic parameters. |
| [`Q105_MVP/`](./Q105_MVP/README.md) | MVP ready | TU Q105 systemic crash warnings. Core–periphery network contagion toy model with early-warning tension gauge `T_warning` over simple indicator schemes such as global mean load and core stress. |
| [`Q121_MVP/`](./Q121_MVP/README.md) | MVP ready | TU Q121 alignment slice. Literal helper and aligned helper personas on the same base model with alignment tension observable `T_align` over SAFE and UNSAFE scenarios. |
| [`Q124_MVP/`](./Q124_MVP/README.md) | MVP ready | TU Q124 scalable oversight ladders. Baseline and guided evaluators on synthetic oversight cases with oversight tension observable `T_oversight`. One-cell Colab with optional API key. |
| [`Q127_MVP/`](./Q127_MVP/README.md) | MVP ready | TU Q127 synthetic worlds and entropy. Three tiny Gaussian worlds, cross-world evaluations, and world-detection style tension gauge `T_entropy(train → test)` with simple heatmaps. |
| [`Q130_MVP/`](./Q130_MVP/README.md) | MVP ready | TU Q130 early out-of-distribution and social-pressure probes. Hollywood vs physics reasoning and social-pressure style experiments with tension metrics explained inside `Q130_MVP/README.md`. |

Each folder owns its own story.  
The high level rule is simple:

- **This page only indexes experiments.**  
- **Each experiment explains itself inside its own directory.**

---

## 4. Reproducibility and scope of claims

All experiments in this lab obey the following principles:

- **Effective-layer only**  
  - They operate on observable behavior and declared encodings.  
  - They do not introduce hidden assumptions about deep mechanisms.

- **Reproducible in minutes**  
  - Each experiment is small enough to be rerun from a fresh environment.  
  - External requirements are kept minimal and written down in the experiment’s own README.

- **Limited claims**  
  - An experiment may show that a specific tension gauge or persona setting works well  
    on a narrow slice of a larger problem.  
  - It does not claim that the full S-problem is solved, nor that the behavior will generalise  
    to arbitrary traffic or models beyond the ones actually tested.

If you find a mismatch between an experiment’s README and what the code actually does,  
please open an issue or pull request in the main WFGY repository so the lab remains audit-friendly.

---

## 5. Roadmap

This hub is expected to accumulate, for example:

- additional out-of-distribution reasoning experiments tied to other BlackHole questions,  
- social pressure and persona stability tests for different domains,  
- retrieval and vector-store tension probes,  
- governance and arbitration demos that combine several tension axes.

New experiments will be added as new MVPs are ready.  
When a new experiment appears, it will get its own folder, its own README, and an entry in the table above.
