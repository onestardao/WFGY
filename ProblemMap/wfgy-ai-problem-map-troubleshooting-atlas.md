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
- A troubleshooting decision-system introduction
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
## The first failure grammar for complex AI systems that changes the first repair move.
> **Stop debugging from symptoms. Route the failure, find the broken invariant, and repair the right layer first.**

<img width="1536" height="1024" alt="TS_Atlas" src="https://github.com/user-attachments/assets/b323dcf5-7eb8-4916-a8be-d1dd4f61b30f" />


Modern AI systems rarely fail in one clean way.

A case that looks like hallucination may actually begin as grounding drift.  
A case that looks like reasoning collapse may actually begin as a broken formal container.  
A case that looks like safety trouble may actually begin as missing observability.  
A case that looks like memory trouble may actually begin as execution closure failure.

That is why ordinary debugging advice collapses too early.

Problem Map 3.0 was built for a more precise job:

- identify the failure family
- locate the best-fit node
- inspect the broken invariant
- choose the right first repair surface

In short:

> **Problem Map 3.0 helps humans and AI systems avoid starting with the wrong fix.**

---

## What this system actually does

Problem Map 3.0 does not stop at naming the failure.

It helps humans and AI systems do five things more reliably:

1. classify a failure
2. identify which invariant is broken
3. separate neighboring failure regions that are easy to confuse
4. choose the right first repair direction
5. prevent future debugging from collapsing into ad hoc guesswork

This is why the project should be understood as a **debugging decision system**, not just a checklist.

The biggest cost in complex AI debugging is often not the final answer itself.

It is the **first wrong repair move**.

---

## Why this exists

Modern AI systems are increasingly:

- retrieval-heavy
- multi-step
- tool-using
- stateful
- agentic
- operational

As systems grow like this, symptom words become too coarse:

- hallucination
- prompting issue
- bad retrieval
- bad reasoning
- memory problem
- alignment problem

Those labels can be useful, but they are often too shallow to decide what should be repaired first.

Problem Map 3.0 Troubleshooting Atlas was built to cut these regions apart more cleanly, so diagnosis becomes more stable and first repair moves become more precise.

---

## The core promise

You can think of this project in one sentence:

> **a system that helps humans and AI avoid walking into the wrong repair path at the start of complex debugging**

That is the practical threshold.

Not just:

- what went wrong

But also:

- where the failure lives
- what neighboring region is tempting but wrong
- what should be repaired first
- what should not be repaired first

---

## A simple view of the system

```mermaid
flowchart LR
    A[Input case] --> B[Failure family]
    B --> C[Best-fit node]
    C --> D[Broken invariant]
    D --> E[First repair surface]
````

**Route first. Repair second. Stop guessing from symptoms alone.**

---

## Why “3.0” matters

The name is intentional.

**Problem Map** stays because this system grows out of the earlier Problem Map line and keeps its original debugging spirit.

**3.0** matters because this is not a small update.
It is a structural jump:

* from checklist logic to atlas logic
* from flat failure naming to routing grammar
* from isolated debugging tips to reusable failure mapping
* from local AI debugging toward a broader complex-system bridge

**Troubleshooting Atlas** matters because this project is meant to feel like a map, not a loose article, and like an operating surface, not a decorative theory page.

---

## What makes this different

Most debugging material does one of three things:

* it names symptoms
* it lists best practices
* it suggests local fixes

Problem Map 3.0 does something more structural.

It organizes failure space into a stable mother table, then teaches how to move through that space using:

* family routing
* boundary rules
* canonical cases
* relation lines
* first repair directions
* patch discipline

That is why this project is better understood as a **routing grammar for failures** than as a checklist.

---

## The seven-family mother table 🧩

The current atlas organizes failure space through seven top-level families.

### F1 · Grounding & Evidence Integrity

The system fails to remain correctly aligned with external evidence anchors, truth-like anchors, world anchors, or semantic targets.

**Short intuition**
the output is no longer properly tied to reality, evidence, or the intended target

### F2 · Reasoning & Progression Integrity

The reasoning chain, decomposition chain, recursive chain, or recovery path loses continuity, controllability, or recoverability.

**Short intuition**
the system is no longer moving through reasoning space in a stable way

### F3 · State & Continuity Integrity

Memory, role, ownership, session thread, or continuity thread can no longer remain stable across steps, sessions, or interacting entities.

**Short intuition**
the system no longer preserves what should persist

### F4 · Execution & Contract Integrity

Readiness, ordering, bridge integrity, liveness, closure, protocol, or enforcement skeletons fail to close.

**Short intuition**
the workflow or operational skeleton breaks before the task can complete safely

### F5 · Observability & Diagnosability Integrity

The system cannot stably expose, trace, audit, interpret, or anticipate the structures required to understand the failure.

**Short intuition**
the problem may already be there, but you still cannot see it clearly enough

### F6 · Boundary & Safety Integrity

Goal, control, incentive, collective, or regime boundaries drift, erode, fragment, or become captured.

**Short intuition**
the system no longer stays inside a safe or viable boundary

### F7 · Representation & Localization Integrity

Symbolic shells, formal containers, layouts, local anchors, explanations, or synthetic structures fail to preserve structure faithfully.

**Short intuition**
the container that carries meaning is distorted before the task can remain stable

---

## Why these seven families exist

These seven families were not chosen by aesthetics, convenience, or rhetorical style.

They were carved through a longer WFGY line:

* **WFGY 1.0** contributed the original self-healing logic and correction framework
* **WFGY 2.0** pushed the system toward explicit routing, text-native control, and guardrail logic
* **WFGY 3.0** expanded the pressure field through a much larger stress-tested problem set

The result is that these seven families are not topic buckets.

They are better understood as **seven recurring modes of instability in complex systems**.

That is why the atlas can begin with AI failures while still pointing beyond AI.

---

## What already exists ✅

Problem Map 3.0 already includes a stable first body of work.

### Core atlas

A frozen first atlas structure with:

* seven-family mother table
* major routing rules
* canonical node layer
* high-value subtree layer
* relation matrix
* patch discipline

### Casebook layer

A first canonical casebook that teaches:

* what each family looks like
* how important boundaries should be cut
* how diagnosis changes the first repair move

### AI adapter layer

A first atlas-to-AI adapter layer that compresses atlas logic into reusable routing modes for model-facing use.

### Fix layer

A first repair-facing layer that connects correct routing to first repair surfaces and misrepair discipline.

### Demo layer

A first official demo pack showing that different routes lead to different first repair moves.

### Patch layer

A first completed patch wave that thickens selected subtrees, strengthens relations, improves case teaching, and improves adapter usability.

### Cross-domain bridge layer

A first formal bridge pack showing that the current atlas can already extend beyond narrow AI-only framing without requiring a redraw of the mother table.

---

## Use the atlas directly with AI ⚡

Problem Map 3.0 is not only a document system.

It now also includes a compact product-facing routing pack:

### [Troubleshooting Atlas Router v1](./Atlas/troubleshooting-atlas-router-v1-freeze-note.md)

This is the first compact TXT routing pack built from the atlas.

Its purpose is simple:

- route the case first
- identify the broken invariant
- separate the strongest neighboring pressure
- suggest the first repair direction
- warn about likely misrepair
- stay honest when evidence is weak

Short version:

> **The Atlas is the map.**  
> **The Router is the first compact executable surface of that map.**

If you want the practical entry points:

- [Router Freeze Note](./Atlas/troubleshooting-atlas-router-v1-freeze-note.md)
- [Router Usage Guide](./Atlas/troubleshooting-atlas-router-v1-usage.md)
- [Router TXT Pack](./Atlas/troubleshooting-atlas-router-v1.txt)

What the Router is **not**:

- not the full Atlas
- not the full Casebook
- not a full auto-repair engine
- not a claim of full diagnosis closure

What it does give you is something more immediate:

> **drop the TXT into an AI system, feed it a failure case, and the model becomes much more likely to classify the failure family correctly before jumping into the wrong fix**

---

## From routing to repair

Problem Map 3.0 does not stop at diagnosis.

It opens a controlled path from routing to first repair.

### Atlas layer

The atlas routes the failure.

### Casebook layer

The casebook teaches how major cuts should be made and how neighboring regions should be separated.

### Fix layer

The fix surface turns correct routing into a disciplined first repair move.

### Deeper bridge layer

WFGY remains the deeper exploration engine when the case needs stronger structural intervention.

This means the system is not just:

* classify and stop

It is:

* route
* cut correctly
* repair the right layer first
* only then escalate deeper if needed

---

## Use it now

If you want the shortest working path, start here:

- want the full product overview → [Problem Map 3.0 Troubleshooting Atlas](./wfgy-ai-problem-map-troubleshooting-atlas.md)
- want the full system map → [Atlas Hub](./Atlas/README.md)
- want the compact TXT routing pack → [Troubleshooting Atlas Router v1](./Atlas/troubleshooting-atlas-router-v1-usage.md)
- want first repair-facing guidance → [Fixes Hub](./Atlas/Fixes/README.md)
- want official proof-of-use demos → [Official Flagship Demos](./Atlas/Fixes/official/demos/README.md)

This is the shortest practical interpretation of the current system:

> **read the atlas if you want the map**  
> **use the router if you want the compact operational entry**  
> **use the fixes layer if you want the first repair surface**

---

## Proof that this is usable, not just theoretical

The current system already crosses the line from “interesting framework” into “usable troubleshooting surface.”

The strongest current public proof is simple:

> **different routes lead to different first repair moves**

That is exactly what the official demos are designed to show.

The first demo pack focuses on four sharp families:

* F1 grounding-first
* F5 observability-first
* F4 execution-first
* F7 container-first

These were chosen because they are the fastest way to show that the atlas does not only classify failures.

It changes what should happen next.

---

## How to use this atlas ⚙️

There are three practical ways to use Problem Map 3.0.

### 1. Human debugging

Use the atlas to ask:

* what kind of failure is this
* which family should I route to first
* which neighboring family is tempting but wrong
* what first repair direction should I try

### 2. AI-assisted routing

Use the atlas as an AI-facing routing grammar so that a model can classify a case more consistently and explain why one family is primary and another is only secondary.

### 3. Product and workflow design

Use the atlas as a design surface for:

* triage flows
* case cards
* routing prompts
* onboarding
* benchmark failure analysis
* patch-aware debugging workflows

---

## Why this matters now

AI systems are becoming more layered, more stateful, more agentic, and more operational.

When systems grow like this, debugging starts failing if every mistake is reduced to labels like:

* hallucination
* prompting issue
* model limitation
* alignment problem
* bad retrieval
* bad reasoning

Those labels are too coarse.

Teams increasingly need a reusable grammar that can say:

* this is grounding-first, not reasoning-first
* this is container-first, not semantics-first
* this is observability-first, not boundary-first
* this is execution-first, not continuity-first

That is the practical value of this atlas.

---

## The broader direction 🌍

Problem Map 3.0 is being built first as a powerful AI troubleshooting atlas.

That is the practical entry point.

At the same time, the long-range direction is larger.

The same family grammar appears capable of absorbing more general failures in:

* coordination
* institutions
* coherence
* collective pressure
* structural breakdown

The correct reading is:

> **AI Troubleshooting Atlas is the first validated operational surface.**
> **A broader complex-system bridge is the next step, not a marketing shortcut.**

That distinction matters, and it is intentional.

---

## What this page does not claim 🔒

This page does **not** claim that:

* every possible failure has already been captured
* all subtrees are fully expanded
* all relations are fully enumerated
* all future cross-domain problems are already solved by the current map
* no more patching is needed
* the final civilization-scale atlas is already complete

The safer and more accurate claim is:

> the first formal atlas version is complete enough to matter,
> and future work should continue through patching, thickening, adaptation, and demonstration expansion

---

## FAQ

<details>
<summary><strong>What is the difference between Problem Map 1.0, 2.0, and 3.0?</strong></summary>

**Problem Map 1.0** is the canonical 16-problem RAG failure taxonomy and fix map.

**Problem Map 2.0** is the Global Debug Card layer.  
It compresses debugging objects, metrics, ΔS zones, and operating modes into a visual protocol.

**Problem Map 3.0** is the broader troubleshooting atlas.  
It moves from flat failure naming toward routing grammar, family structure, boundary rules, case teaching, repair-facing direction, and broader bridge work.

Short version:

- **1.0** gives the base failure vocabulary
- **2.0** gives the compressed visual debug protocol
- **3.0** gives the broader troubleshooting atlas and routing system

</details>

<details>
<summary><strong>Is this a checklist, a framework, or a routing system?</strong></summary>

It begins where a checklist stops.

Problem Map 3.0 should be understood as a **debugging decision system** and a **failure routing grammar**.

It still preserves map-like clarity, but its real job is not just to name failures.

Its real job is to help humans and AI systems decide:

- where the failure lives
- what neighboring region is tempting but wrong
- which invariant is broken
- what should be repaired first

So the most accurate answer is:

> **it is a routing grammar and troubleshooting decision system, not just a checklist**

</details>

<details>
<summary><strong>Do I need to read the full Atlas to use it?</strong></summary>

No.

The full Atlas is the strongest version if you want the full structure, deeper definitions, casebook, patch logic, and bridge materials.

But you do **not** need to read the full Atlas just to start using the system.

If you want the compact entry point, use:

- [Troubleshooting Atlas Router v1 Usage Guide](./Atlas/troubleshooting-atlas-router-v1-usage.md)
- [Troubleshooting Atlas Router v1 TXT Pack](./Atlas/troubleshooting-atlas-router-v1.txt)

That is the shortest route from “I have a bug case” to “help me classify this correctly.”

</details>

<details>
<summary><strong>What does Troubleshooting Atlas Router actually do?</strong></summary>

The Router is the first compact TXT routing pack built from the Atlas.

Its job is to help an AI system do the following in order:

1. identify the most likely primary family
2. identify the strongest neighboring family pressure if it is real
3. explain why the primary cut is stronger
4. identify the broken invariant
5. suggest the first repair direction
6. warn about likely misrepair
7. stay honest about confidence and evidence sufficiency

It is best understood as:

> **the first compact executable surface of the Atlas**

It is not the whole Atlas and not a full repair engine.

</details>

<details>
<summary><strong>Does this system already repair everything automatically?</strong></summary>

No.

The current public system is strongest at:

- route-first classification
- boundary-aware diagnosis
- broken-invariant reading
- first repair direction
- misrepair warning
- deeper escalation paths when needed

That is already very valuable.

But it is not the same thing as claiming:

- full autonomous diagnosis
- full autonomous repair
- complete root-cause closure in every case

The current repair logic is best understood as:

> **route first, choose the right first move, then escalate deeper only when needed**

</details>

<details>
<summary><strong>Is this only for AI systems?</strong></summary>

The current strongest public form is **AI-first**.

That is intentional, because AI troubleshooting is the first validated operational surface of the atlas.

At the same time, the family grammar was not carved as a narrow topic list.
It was carved as a more general failure grammar for complex systems.

That is why the atlas already has a formal bridge layer through documents such as:

- [Cross-Domain Demonstration Pack v2](./Atlas/cross-domain-demonstration-pack-v2.md)
- [Civilization Bridge Modules v1](./Atlas/civilization-bridge-modules-v1.md)

So the correct reading is:

> **AI-first in its strongest validated public form**  
> **already structured enough to support controlled bridge work beyond AI**  
> **not yet claiming universal final closure**

</details>

<details>
<summary><strong>Why do you call it an atlas?</strong></summary>

Because this project is not meant to feel like a loose article or a flat symptom list.

It is meant to function like a map:

- a map of failure space
- a map of neighboring regions
- a map of common wrong turns
- a map of first repair surfaces

That is why “atlas” fits better than a simple checklist or note collection.

The name is meant to signal:

> **this is a structured navigation surface for debugging, not a loose pile of advice**

</details>

<details>
<summary><strong>Where should a new user start?</strong></summary>

That depends on what kind of user you are.

### If you want the product overview
Start with this page, then go to:
- [Atlas Hub](./Atlas/README.md)

### If you want the core structure
Go to:
- [Atlas Final Freeze v1](./Atlas/atlas-final-freeze-v1.md)

### If you want examples and teaching cases
Go to:
- [Canonical Casebook v1](./Atlas/canonical-casebook-v1.md)

### If you want a compact AI-usable entry point
Go to:
- [Troubleshooting Atlas Router v1 Usage Guide](./Atlas/troubleshooting-atlas-router-v1-usage.md)

### If you want repair-facing materials
Go to:
- [Fixes Hub](./Atlas/Fixes/README.md)

### If you want demos
Go to:
- [Official Flagship Demos](./Atlas/Fixes/official/demos/README.md)

</details>

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
5. [Fixes Hub](./Atlas/Fixes/README.md)
6. [Official Flagship Demos](./Atlas/Fixes/official/demos/README.md)

---

## Current status 🚀

The current system should be understood as:

* main atlas body established
* first formal freeze established
* first casebook established
* first AI adapter established
* first repair-facing layer established
* first major patch wave established
* first formal cross-domain bridge established

This means the project has moved from:

**trying to find the core structure**

into:

**using, extending, and productizing a core structure that is already stable enough to matter**

---

## One-line version

**Problem Map 3.0 Troubleshooting Atlas is a debugging decision system for complex AI failures, built to reduce wrong-first-fix debugging.**

---

## Closing note ✨

If you are reading this as a human:

treat this page as the front door.

If you are reading this as an AI system:

treat this page as the product-facing mainline overview, then route to the Atlas folder for deeper structure, rules, cases, fix layers, and adaptation materials.

The atlas is not being introduced as a static taxonomy.
It is being introduced as a system you can actually use.
