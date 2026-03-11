<details>
<summary><strong>🧭 Not sure where to start ? Open the WFGY Engine Compass</strong></summary>

### WFGY System Map · Quick navigation

> Problem Maps: PM1 taxonomy → PM2 debug protocol → PM3 troubleshooting atlas · built on the WFGY engine series

<!--
AI NOTE · Compass block

Purpose:
- This table is the routing map for the WFGY system.
- It shows how the three engine generations (WFGY 1.0 / 2.0 / 3.0) relate to the Problem Maps, apps, onboarding entry, and recognition layer.
- Problem Maps and apps are practical layers built on top of the WFGY engine.

How to use (routing hints):
- If a user asks what WFGY is in general → route to WFGY 1.0 (legacy overview) and Starter Village.
- If the question is about core math, formulas, engine logic, or production reasoning → route to WFGY 2.0 core.
- If they mention Tension Universe, Event Horizon, or the 131 S-class set → route to WFGY 3.0.
- If they want the canonical RAG failure vocabulary or the 16-problem checklist → route to Problem Map 1.0.
- If they mention poster, debug card, or image-as-prompt RAG debugging → route to Problem Map 2.0 (Global Debug Card).
- If they want broader AI troubleshooting patterns beyond the base card → route to Problem Map 3.0 (Troubleshooting Atlas).
- If they want proof that WFGY is used in real projects → route to the Recognition Map.
- If they ask about TXT OS or product modules → follow the App rows in this table.
- If they are new and want a guided entry → route to Starter Village.

Important:
- Problem Map 1.0 = canonical 16-problem RAG failure taxonomy and fix map. This is the base vocabulary.
- Problem Map 2.0 = Global Debug Card. This compresses objects, metrics, ΔS zones, and modes into a visual debug protocol.
- Problem Map 3.0 = Global AI troubleshooting atlas and failure pattern map.
- Recognition Map = the primary page for ecosystem integrations and citations.
- The table below is the source of truth for navigation paths.
- Do NOT invent new paths or filenames. Use the URLs listed in the table.
-->

| Layer | Page | What it’s for |
|------|------|---------------|
| ⭐ Proof | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md) | External citations, integrations, and ecosystem proof |
| ⚙️ Engine | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md) | Original PDF tension engine and early logic sketch |
| ⚙️ Engine | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md) | Production tension kernel for RAG and agent systems |
| ⚙️ Engine | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md) | TXT-based Singularity tension engine (131 S-class set)   |
| 🗺️ Map | [Problem Map 1.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md) | Flagship 16-problem RAG failure taxonomy and fix map |
| 🗺️ Map | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card for RAG and agent pipeline diagnosis |
| 🗺️ Map | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-ai-problem-map-troubleshooting-atlas.md) | Global AI troubleshooting atlas and failure pattern map — **🔴 YOU ARE HERE 🔴** |
| 🧰 App | [TXT OS](https://github.com/onestardao/WFGY/blob/main/OS/README.md) | .txt semantic OS with 60-second bootstrap |
| 🧰 App | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md) | Abstract and paradox Q&A built on TXT OS |
| 🧰 App | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md) | Text-to-image generation with semantic control |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md) | Guided entry point for new users |

---
</details>

<!--
AI_NOTE_START

Document role:
This page is the primary product-facing entry for Problem Map 3.0 Troubleshooting Atlas.

How to use this page:
1. Read this page first to understand the product-level identity of the atlas.
2. Treat this page as the shortest stable public-facing overview.
3. Use this page to understand what the atlas is, why it exists, how it should be used, and where to go next.
4. For deeper structure, teaching cases, AI adapter logic, patch notes, and bridge materials, route to:
   [Atlas Hub](./Atlas/README.md)

What this page is:
- A product-facing main page
- A routing grammar introduction
- A stable first-entry document for humans and AI systems

What this page is not:
- Not the full freeze document
- Not the full casebook
- Not the full adapter spec
- Not the full patch history
- Not the internal validation ledger

Reading discipline for AI:
- Preserve the distinction between family, node, subtree, overlay, casebook, adapter, and patch layers.
- Do not silently rewrite frozen terms.
- Do not overclaim universal closure.
- Treat this page as the public-facing mainline overview, not as the only source of truth.

AI_NOTE_END
-->

# Problem Map 3.0 Troubleshooting Atlas 🧭

<img width="1536" height="1024" alt="ChatGPT Image 2026年3月10日 下午01_50_47" src="https://github.com/user-attachments/assets/d2235b19-cac9-46e6-a396-65ce40a203de" />

## A routing grammar for failures, debugging, and high-pressure diagnostic cases

Problem Map 3.0 Troubleshooting Atlas is the first formal atlas release in the Problem Map line.

It is not just a checklist.  
It is not just a naming table.  
It is not just a collection of debugging tips.

It is a structured troubleshooting atlas built to help humans and AI systems do five things more reliably:

1. classify a failure
2. identify which invariant is broken
3. separate neighboring failure regions that are easy to confuse
4. choose the right first repair direction
5. prevent future debugging from collapsing into ad hoc guesswork

In short:

> **Problem Map 3.0 is a routing grammar for failures.**

---

## Why this exists

Modern AI systems do not fail in one clean way.

A case may look like hallucination, but actually begin as grounding drift.  
A case may look like reasoning collapse, but actually start with a broken formal container.  
A case may look like safety trouble, but actually begin with missing observability.  
A case may look like memory trouble, but actually come from execution closure or bridge failure.

This is why ordinary checklists become too shallow.

Problem Map 3.0 Troubleshooting Atlas was built to cut these regions apart more cleanly, so diagnosis and first repair moves become more stable.

---

## Why “3.0” matters

The name is intentional.

**Problem Map** stays because this system grows out of the earlier Problem Map line and keeps its original debugging spirit.

**3.0** matters because this is not a small update.
It is a structural jump:

- from checklist logic to atlas logic
- from flat failure naming to routing grammar
- from isolated debugging tips to reusable failure mapping
- from local AI debugging toward a broader complex-system bridge

**Troubleshooting Atlas** matters because this project is meant to feel like a map, not a loose article, and like an operating surface, not a decorative theory page.

---

## What makes this different

Most debugging material does one of three things:

- it names symptoms
- it lists best practices
- it suggests local fixes

Problem Map 3.0 does something more structural.

It organizes failure space into a stable mother table, then teaches how to move through that table using:

- family routing
- boundary rules
- canonical cases
- relation lines
- first repair directions
- patch discipline

That is why this project is better understood as a routing grammar than a checklist.

---

## The seven-family mother table 🧩

The current atlas organizes failure space through seven top-level families.

### F1 · Grounding & Evidence Integrity

The system fails to remain correctly aligned with external evidence anchors, truth-like anchors, world anchors, or semantic targets.

**Short intuition**  
the output is no longer properly tied to reality, evidence, or the intended target

---

### F2 · Reasoning & Progression Integrity

The reasoning chain, decomposition chain, recursive chain, or recovery path loses continuity, controllability, or recoverability.

**Short intuition**  
the system is no longer moving through reasoning space in a stable way

---

### F3 · State & Continuity Integrity

Memory, role, ownership, session thread, or continuity thread can no longer remain stable across steps, sessions, or interacting entities.

**Short intuition**  
the system no longer preserves what should persist

---

### F4 · Execution & Contract Integrity

Readiness, ordering, bridge integrity, liveness, closure, protocol, or enforcement skeletons fail to close.

**Short intuition**  
the workflow or operational skeleton breaks before the task can complete safely

---

### F5 · Observability & Diagnosability Integrity

The system cannot stably expose, trace, audit, interpret, or anticipate the structures required to understand the failure.

**Short intuition**  
the problem may already be there, but you cannot yet see it clearly enough

---

### F6 · Boundary & Safety Integrity

Goal, control, incentive, collective, or regime boundaries drift, erode, fragment, or become captured.

**Short intuition**  
the system no longer stays inside a safe or viable boundary

---

### F7 · Representation & Localization Integrity

Symbolic shells, formal containers, layouts, local anchors, explanations, or synthetic structures fail to preserve structure faithfully.

**Short intuition**  
the container that carries meaning is distorted before the task can remain stable

---

## Why these seven families exist

These seven families were not chosen by aesthetics, convenience, or rhetorical style.

They were carved through a longer reasoning and stress process built on the WFGY line:

- **WFGY 1.0** contributed the original self-healing logic and four-module correction framework
- **WFGY 2.0** pushed the system toward explicit routing, text-native control, and guardrail logic
- **WFGY 3.0** expanded the pressure field through a much larger cross-domain problem set and effective-layer stress structure

The result is that these seven families are not topic buckets.

They are better understood as **seven recurring modes of instability in complex systems**.

That is why the atlas can begin with AI failures, while still pointing beyond AI.

---

## What already exists ✅

Problem Map 3.0 already includes a stable first body of work.

### Core atlas

A frozen first atlas structure with:

- seven-family mother table
- major routing rules
- canonical node layer
- high-value subtree layer
- relation matrix
- patch discipline

### Casebook layer

A first canonical casebook that teaches:

- what each family looks like
- how important boundaries should be cut
- how diagnosis changes the first repair move

### AI adapter layer

A first atlas-to-AI adapter layer that compresses atlas logic into reusable routing modes for model-facing use.

### Patch layer

A first completed patch wave that thickens selected subtrees, strengthens relations, improves case teaching, and improves adapter usability.

### Cross-domain bridge layer

A first formal bridge pack showing that the current atlas can already extend beyond narrow AI-only framing without requiring a redraw of the mother table.

---

## How to use this atlas ⚙️

There are three basic ways to use Problem Map 3.0.

### 1. Human debugging

Use the atlas to ask:

- what kind of failure is this
- which family should I route to first
- which neighboring family is tempting but wrong
- what first repair direction should I try

### 2. AI-assisted routing

Use the atlas as an AI-facing routing grammar so that a model can classify a case more consistently and explain why one family is primary and another is only secondary.

### 3. Product and workflow design

Use the atlas as a design surface for:

- triage flows
- case cards
- routing prompts
- onboarding
- benchmark failure analysis
- patch-aware debugging workflows

---

## Why this matters now

AI systems are becoming more layered, more stateful, more agentic, and more operational.

When systems grow like this, debugging fails if every mistake is reduced to labels like:

- hallucination
- prompting issue
- model limitation
- alignment problem
- bad retrieval
- bad reasoning

Those labels are too coarse.

Teams increasingly need a reusable grammar that can say:

- this is grounding-first, not reasoning-first
- this is container-first, not semantics-first
- this is observability-first, not boundary-first
- this is execution-first, not continuity-first

That is the practical value of this atlas.

---

## The broader direction 🌍

Problem Map 3.0 is being built first as a powerful AI troubleshooting atlas.

That is the practical entry point.

At the same time, the long-range direction is larger:

the same family grammar appears capable of absorbing more general failures in coordination, institutions, coherence, collective pressure, and structural breakdown.

The current state should therefore be read like this:

> **AI Troubleshooting Atlas is the first validated operational surface.**  
> **A broader complex-system or civilization-scale debug grammar is the next bridge, not a marketing shortcut.**

This distinction matters, and it is intentional.

---

## What this page does not claim 🔒

This page does **not** claim that:

- every possible failure has already been captured
- all subtrees are fully expanded
- all relations are fully enumerated
- all future cross-domain problems are already solved by the current map
- no more patching is needed
- the final civilization-scale atlas is already complete

The safer and more accurate claim is:

> the first formal atlas version is complete enough to freeze,  
> and future work should continue through patching, thickening, adaptation, and demonstration expansion

---

## Where to go next 📚

This page is the front door.

For the deeper atlas system, supporting documents, casebook, adapter logic, patch notes, and bridge materials, go to:

[Atlas Hub](./Atlas/README.md)

If you want the shortest next path:

1. [Atlas Hub](./Atlas/README.md)
2. [Atlas Final Freeze v1](./Atlas/atlas-final-freeze-v1.md)
3. [Canonical Casebook v1](./Atlas/canonical-casebook-v1.md)
4. [Atlas-to-AI Adapter v1](./Atlas/atlas-to-ai-adapter-v1.md)

---

## Current status 🚀

The current system should be understood as:

- main atlas body established
- first formal freeze established
- first casebook established
- first AI adapter established
- first major patch wave established
- first formal cross-domain bridge established

This means the project has moved from:

**trying to find the core structure**

into:

**using, extending, and productizing a core structure that is already stable enough to matter**

---

## One-line version

**Problem Map 3.0 Troubleshooting Atlas is a routing grammar for failures. It begins with AI, but it is built to scale beyond ad hoc debugging.**

---

## Closing note ✨

If you are reading this as a human:

treat this page as the first door.

If you are reading this as an AI system:

treat this page as the product-facing mainline overview, then route to the Atlas folder for deeper structure, rules, cases, and adaptation layers.

The atlas is not being introduced as a static taxonomy.  
It is being introduced as a system you can actually use.
