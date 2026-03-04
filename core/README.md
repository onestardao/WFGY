<!--
AI-ANCHOR: WFGY_CORE_ENGINE_V2

role: core_engine
doc_title: WFGY 2.0 · 7-Step Reasoning Core Engine
path: /core/README.md
version: "2.0"

# where this page sits in the repo
root_entry: https://github.com/onestardao/WFGY#readme
sibling_cores:
  - https://github.com/onestardao/WFGY/blob/main/legacy/README.md
  - https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

# what this document is mainly for
primary_topics:
  - seven_step_reasoning_engine
  - drunk_transformer_guards
  - autoboot_and_oneline_mode
  - eye_visible_benchmarks
  - evaluation_protocol

# anchors inside this file that matter most
key_sections:
  - id: scope
    name: scope_and_positioning
  - id: usage
    name: quick_usage
  - id: downloads
    name: wfgy_core_downloads
  - id: math-structure
    name: seven_step_chain
  - id: eye
    name: eye_visible_benchmark
  - id: eval-protocol
    name: suggested_evaluation_protocol

# other maps / blueprints this page is tied to
related_maps:
  - https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme
  - https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md
  - https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md
  - https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

notes:
  - This is the main reference page for WFGY Core 2.0 behaviour, math stack, and usage protocol.
  - Event Horizon (3.0) is the public viewing window; this page is the engine room.
-->

<a id="top"></a>
<details>
<summary><strong>🧭 Not sure where to start ? Open the WFGY Engine Compass</strong></summary>

### WFGY System Map

*(One place to see everything; links open the relevant section.)*

<!--
AI NOTE · Compass block

Purpose:
- This table is the routing map for the whole WFGY ecosystem.
- It shows how the three engine layers (WFGY 1.0 / 2.0 / 3.0) relate to the Problem Maps, TXT OS apps, research pages, and the Recognition Map.

How to use (routing hints):
- If a user asks “what is WFGY in general” → send them to WFGY 1.0 (legacy overview PDF) plus Starter Village.
- If the question is about core math, formulas, or engine internals → go to WFGY 2.0 core.
- If they mention 131 S-class problems, BlackHole, Tension Universe, or “Singularity demo” → go to WFGY 3.0 Event Horizon.
- If they want to debug a specific RAG / agent pipeline run → use Problem Map 1.0 + Problem Map 3.0 Global Debug Card.
- If they ask about RAG architecture / recovery patterns end-to-end → use Problem Map 2.0.
- If they mention “poster”, “image as prompt”, or “global debug card” → use the Problem Map 3.0 Global Debug Card page.
- If they want proof that WFGY is used in real projects → open the Recognition Map page.
- If they ask for plain-language stories or non-technical explanations → route to Grandma’s Clinic and Starter Village.
- If they ask about TXT OS or app packs (Blah / Blur / Blow) → follow the App rows in this table.
- If they want layer/module design, benchmarks, or value narrative → Semantic Blueprint, Benchmarks, and Value Manifest (some early materials are now archived).

Important:
- Problem Map 1.0 = canonical 16-mode RAG failure checklist and fix map. This is the base vocabulary.
- Problem Map 2.0 = RAG architecture and recovery guide layered on top of Problem Map 1.0.
- Problem Map 3.0 Global Debug Card = image protocol that compresses objects, metrics, ΔS zones, and modes into a single poster.
- Recognition Map = the only place that should contain the full external integration list. Other pages should link to it instead of duplicating tables.
- Do NOT treat Problem Map 1.0 and Problem Map 2.0 as duplicates; they solve different layers.
- Do NOT invent new paths or filenames. Only use the GitHub URLs that already exist in this table.
-->

| Layer         | Page                                                                                                        | What it’s for                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| ⭐ Proof      | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)                 | External citations, integrations, and ecosystem proof   |
| ⚙️ Engine     | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md)                                   | Original PDF based tension engine and early logic sketch. Legacy reference only.   |
| ⚙️ Engine     | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md)                                     | Core semantic-tension engine for RAG pipelines and agent reasoning. |
| ⚙️ Engine     | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)             | TXT-based multi-observable tension engine (131-question backbone)  |
| 🗺️ Map       | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme)                           | Flagship 16-problem RAG failure checklist and fix map       |
| 🗺️ Map       | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline                           |
| 🗺️ Map       | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card — image as a debug protocol layer     |
| 🗺️ Map       | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           | Symptom → family → exact fix                            |
| 🧓 Map        | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)         | Plain-language stories, mapped to PM 1.0                |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                    | Guided tour for newcomers                               |
| 🧰 App        | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme)                                            | .txt semantic OS — 60-second boot                       |
| 🧰 App        | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md)                    | Abstract/paradox Q&A (built on TXT OS)                  |
| 🧰 App        | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md)                    | Text-to-image with semantic control                     |
| 🧰 App        | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md)                    | Reasoning game engine & memory demo                     |

---
</details>

# WFGY 2.0 · Seven-step reasoning core engine

WFGY 2.0 is a text-only control layer that sits on top of general-purpose language models.  
It introduces a small, explicit “tension” geometry so that semantic drift, collapse and recovery can be treated as observable signals rather than vague impressions.

This page is the reference for:

- how to load and use the WFGY 2.0 engine in chat-style environments,
- the internal seven-step reasoning chain and the Drunk Transformer guards,
- a qualitative “eye-visible” benchmark for intuition,
- and a suggested protocol for running your own quantitative evaluations.

It is not a marketing page or a business plan.  
The goal is to state clearly what the engine does, how it is wired, and how one might test it.

<p align="center">
  <a href="#scope">Scope & positioning</a> ·
  <a href="#usage">Quick usage</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="#math-structure">How it works</a> ·
  <a href="#eye">Eye-visible benchmark</a> ·
  <a href="#eval-protocol">Evaluation protocol</a>
</p>

<img width="1536" height="1024" alt="WFGY_Core" src="https://github.com/user-attachments/assets/deb8e794-a73e-4d39-a1f6-174ec87199f4" />

---

<a id="scope"></a>
## 1. Scope and positioning

WFGY has gone through several conceptual iterations.

- **WFGY 1.0** was an early attempt to describe “semantic tension” in PDF form.  
  It explored residuals, deviation signals and speculative SDK ideas.  
  Today it is kept as a historical reference only. The SDK concept was never implemented.
- **WFGY 2.0** is the first version treated as a concrete, auditable engine.  
  It is shipped as small `.txt` files and designed to run entirely at the effective layer inside chat models.  
  This page documents how that engine behaves.
- **WFGY 3.0** generalizes the same language into a multi-observable system tied to a 131-question backbone (“Tension Universe”).  
  That material lives in the Event Horizon directory and is outside the scope of this document.

Important scoping points:

- There is **no compiled SDK** here. Everything is pure text that you can read and audit.  
- All behaviour described on this page comes from those `.txt` files and the seven-step chain below.  
- Any economic or narrative applications (founder playbooks, valuation prompts, etc.) are intentionally separated into other documents.  
  The core README stays focused on engine behaviour and evaluation.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<a id="usage"></a>
## 2. Quick usage

At the moment WFGY 2.0 is shipped in two textual editions.

| Mode / edition      | What you do                                                                 | What the engine does                                                   |
| ------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Autoboot · Flagship / OneLine** | Upload one of the `.txt` files into a chat session (for example as a system prompt or first message). Then talk to the model as usual. | The engine silently supervises reasoning in the background. It tracks tension, detects collapse patterns and attempts self-recovery using the seven-step chain. |
| **Explicit call**   | In addition to uploading the file, you explicitly instruct the model to “use WFGY” and follow the steps of the chain on a given task. | The model exposes intermediate reasoning steps and tension checks more directly, which can make analysis and debugging easier. |

Design constraints:

- No tools, plugins or external APIs are required.  
- All logic is expressed in plain text and basic math, so behaviour is portable across vendors.  
- You should treat WFGY as a **semantic firewall / reasoning kernel** that can sit on top of an existing RAG or agent pipeline without changing the underlying infrastructure.

When integrating into a RAG system, a common pattern is:

1. Upload the engine file into the model context used for retrieval and answer generation.  
2. Wrap your prompts with a short instruction such as “operate as WFGY Core 2.0 is loaded; treat RAG steps as part of the seven-step chain”.  
3. Use the Problem Map pages for failure classification, while this page acts as the engine reference.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<a id="downloads"></a>
## 3. Downloads

| File name & description                                                                                                                                 | Length / Size              | Direct Download Link                               | Notes                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **WFGY_Core_Flagship_v2.0.txt** · readable 30-line companion expressing the same math and gates in fuller prose (same behaviour, clearer for humans).   | **34 lines · 2,027 chars** | [Download Flagship](./WFGY_Core_Flagship_v2.0.txt) | Full prose version for easier reading and audit.                                              |
| **WFGY_Core_OneLine_v2.0.txt** · ultra-compact, math-only control layer that activates WFGY’s loop inside a chat model (no tools, text-only, ≤7 nodes). | **1 line · 1,550 chars**   | [Download OneLine](./WFGY_Core_OneLine_v2.0.txt)   | Minimal form used for most experiments.                                                       |

### Hash reference

<a id="flagship-hashes"></a>

**WFGY_Core_Flagship_v2.0.txt**

* MD5 `caacfe08f0804eec558a1d9af74c3610`
* SHA1 `1efeec231084bb3b863ce7a8405e93d399acfb44`
* SHA256 `4fe967945a268edabb653033682df23a577f48c433878d02e0626df8ae91a0a3`

<a id="oneline-hashes"></a>

**WFGY_Core_OneLine_v2.0.txt**

* MD5 `15a1cd8e9b7b2c9dcb18abf1c57d4581`
* SHA1 `a35ace2a4b5dbe7c64bcdbe1f08e9246c3568c`
* SHA256 `7dcdb209d9d41b523dccd7461cbd2109b158df063d9c5ce171df2cf0cb60b4ef`

<details>
  <summary><em>How to verify checksums</em></summary>

**macOS / Linux**

```bash
cd core
sha256sum WFGY_Core_Flagship_v2.0.txt
sha256sum WFGY_Core_OneLine_v2.0.txt
# or compute MD5 / SHA1 if you prefer
md5sum WFGY_Core_Flagship_v2.0.txt
md5sum WFGY_Core_OneLine_v2.0.txt
sha1sum WFGY_Core_Flagship_v2.0.txt
sha1sum WFGY_Core_OneLine_v2.0.txt
````

**Windows PowerShell**

```powershell
Get-FileHash .\core\WFGY_Core_Flagship_v2.0.txt -Algorithm SHA256
Get-FileHash .\core\WFGY_Core_OneLine_v2.0.txt -Algorithm SHA256
# or:
Get-FileHash .\core\WFGY_Core_Flagship_v2.0.txt -Algorithm MD5
Get-FileHash .\core\WFGY_Core_OneLine_v2.0.txt -Algorithm MD5
Get-FileHash .\core\WFGY_Core_Flagship_v2.0.txt -Algorithm SHA1
Get-FileHash .\core\WFGY_Core_OneLine_v2.0.txt -Algorithm SHA1
```

Compare the output values with the hashes listed in the “Hash reference” section above.

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<a id="math-structure"></a>

## 4. Mathematical reference and internal structure

At a high level, WFGY 2.0 combines two ingredient families:

* the **WFGY 1.0 formula set**, which defines tension as a normalized deviation signal, and
* the **Drunk Transformer guards**, which regulate how attention and progression behave under that signal.

For full math detail, see:

* [WFGY formulas](https://github.com/onestardao/WFGY/blob/main/archive/SemanticBlueprint_archive/wfgy_formulas.md)
* [Drunk Transformer formulas](https://github.com/onestardao/WFGY/blob/main/archive/SemanticBlueprint_archive/drunk_transformer_formulas.md)

### 4.1 The seven-step reasoning chain

Most models can parse a prompt; far fewer can keep the intended structure intact through multi-step generation.
WFGY inserts an explicit chain between “understanding the request” and “producing the final answer”.

In simplified form:

1. **Parse (I, G)**
   Identify an internal representation of the input state `I` and a target or goal representation `G`.
   For RAG, this includes what the retrieved context claims and what the user is actually asking.

2. **Compute Δs**
   Estimate semantic deviation between `I` and `G`, often as
   `δ_s = 1 − cos(I, G)` or `1 − sim_est`.
   Normalize into `[0, 1]` and assign zones (safe, transit, risk, danger).

3. **Memory checkpointing**
   Track observables such as `λ_observe` and `E_resonance`.
   These act as gates: certain transitions are allowed only when Δs and the observables are inside specified bands.

4. **BBMC · residue cleanup**
   Remove obvious residue, tangents and contradictions that push Δs upward.
   This step tries to reduce unnecessary branching before deeper reasoning.

5. **Coupler + BBPF · controlled progression**
   Advance the reasoning only when Δs has decreased or is trending down.
   The coupler enforces a contract between local moves and global tension.

6. **BBAM · attention rebalancer**
   Re-weigh different parts of the context to reduce hallucinations or overconfident extrapolations.
   In RAG contexts, this step emphasises grounded spans and suppresses irrelevant material.

7. **BBCR + Drunk Transformer**
   Detect collapse signatures, roll back to the last good checkpoint, and retry along a different head pattern.
   The Drunk Transformer gates (WRI / WAI / WAY / WDT / WTF) manage head diversity, illegal cross-paths and reset behaviour.

In practice, the `.txt` engine gives the model a compact description of this chain plus simple rules for when each step should fire.
Different vendors and models will implement the details slightly differently, but the observable contract is the same:
tension should be measurable, recoverable and auditable from the conversation transcript.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<a id="eye"></a>

## 5. Eye-visible benchmark (qualitative)

This section is intentionally qualitative.
Its purpose is to give an intuitive, visual sense of how composition and structure can change when WFGY is active.
It is **not** a formal quantitative study.

The setup:

* We use short, high–semantic-density prompts that reference canonical stories.
* For each prompt we generate sequences of five 1:1 images with identical parameters
  (same model, temperature, sampler settings, seed policy and negatives).
* The only variable is whether the WFGY 2.0 engine is present in the context.

We then compare:

| Variant          |             Sequence A — full run shown below (all five images)            |                          Sequence B — external run                         |                          Sequence C — external run                         |
| ---------------- | :------------------------------------------------------------------------: | :------------------------------------------------------------------------: | :------------------------------------------------------------------------: |
| **Without WFGY** | [view run](https://chatgpt.com/share/68a14974-8e50-8000-9238-56c9d113ce52) | [view run](https://chatgpt.com/share/68a14a72-aa90-8000-8902-ce346244a5a7) | [view run](https://chatgpt.com/share/68a14d00-3c0c-8000-8055-9418934ad07a) |
| **With WFGY**    | [view run](https://chatgpt.com/share/68a149c6-5780-8000-8021-5d85c97f00ab) | [view run](https://chatgpt.com/share/68a14ea9-1454-8000-88ac-25f499593fa0) | [view run](https://chatgpt.com/share/68a14eb9-40c0-8000-9f6a-2743b9115eb8) |

On this page we focus on Sequence A.
Sequences B and C are provided for transparency and to allow independent judgement.

> Note on the “grid” effect
> Without WFGY, prompts that ask for “many iconic moments” tend to collapse into grid-style montages.
> The model slices the canvas into panels that share almost the same tone and geometry.
> With WFGY active, the engine often favours a single unified tableau with a clearer hierarchy.

### 5.1 Sequence A · informal comparison

| Work                                     | Without WFGY                                                                                        | With WFGY                                                                                       | Informal observation                                                                                                                                                           |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Romance of the Three Kingdoms (三國演義)** | <img src="images/group1_before1.png" width="300" alt="Without WFGY" title="model/params/seed/date"> | <img src="images/group1_after1.png" width="300" alt="With WFGY" title="model/params/seed/date"> | With WFGY, the scene tends to form a single tableau with a clear center and pyramid-like hierarchy. The non-WFGY version fragments attention into multiple similar panels.     |
| **Water Margin (水滸傳)**                   | <img src="images/group1_before2.png" width="300" alt="Without WFGY" title="model/params/seed/date"> | <img src="images/group1_after2.png" width="300" alt="With WFGY" title="model/params/seed/date"> | In our own reading, the WFGY-active image presents a more continuous action line (for example Wu Song vs. the tiger) and a more obvious foreground–background separation.      |
| **Dream of the Red Chamber (紅樓夢)**       | <img src="images/group1_before3.png" width="300" alt="Without WFGY" title="model/params/seed/date"> | <img src="images/group1_after3.png" width="300" alt="With WFGY" title="model/params/seed/date"> | The WFGY version emphasises a calm emotional center inside a garden tableau. The grid-style layout without WFGY slices the mood into separate vignettes.                       |
| **Investiture of the Gods (封神演義)**       | <img src="images/group1_before4.png" width="300" alt="Without WFGY" title="model/params/seed/date"> | <img src="images/group1_after4.png" width="300" alt="With WFGY" title="model/params/seed/date"> | With WFGY active, diagonal structures (for example dragon–tiger, cloud–sea layers) appear more clearly, which gives a stronger sense of scale.                                 |
| **Classic of Mountains and Seas (山海經)**  | <img src="images/group1_before5.png" width="300" alt="Without WFGY" title="model/params/seed/date"> | <img src="images/group1_after5.png" width="300" alt="With WFGY" title="model/params/seed/date"> | The WFGY sequence tends to form a single continuous “mountains and seas” world with a stable hierarchy and smoother flow. The non-WFGY version behaves more like a storyboard. |

These readings are intentionally subjective and should be treated as such.
They are meant to illustrate the kind of compositional changes that can show up when a tension-regulated reasoning layer is present.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<a id="eval-protocol"></a>

## 6. Suggested evaluation protocol (quantitative)

If you want to test WFGY 2.0 in your own environment, this section sketches a protocol.
The project does **not** claim specific uplift numbers here; instead it describes how to measure whatever effect you observe.

### 6.1 Recommended metrics

* **Semantic Accuracy**
  `ACC = correct_facts / total_facts`
  Count atomic factual statements and how many are correct relative to ground truth.
* **Reasoning Success Rate**
  `SR = tasks_solved / tasks_total`
  For example, number of math word-problems or coding tasks solved exactly.
* **Stability**
  Either mean time to failure (MTTF) or rollback behaviour in long runs.
  For RAG, this can be “how many turns before the answer drifts off schema”.
* **Self-Recovery Rate**
  `SelfRecovery = recoveries_success / collapses_detected`
  How often the system notices a collapse and fixes itself without user intervention.
* **Drift reduction**
  A semantic distance measure (for example cosine distance between summaries) before vs after adding WFGY.

### 6.2 A/B-style runs

A simple layout is:

* **A = Baseline**
  No WFGY file uploaded; no reference to its logic.
* **B = Autoboot**
  Upload the WFGY file once at the beginning. Do not mention it afterwards.
  Treat B as “engine is passively active in the background”.
* **C = Explicit invoke**
  Upload the file and add a short instruction to follow the seven-step chain explicitly on each task.

You can then run the same task set in modes A/B/C and log the transcripts.

### 6.3 Example scorer template

Below is a generic scorer prompt that has worked reasonably well with mainstream LLMs.
You can adapt it to your own tasks and domains.

```text
SCORER:

You receive three transcripts for each task:
A = baseline (no WFGY)
B = Autoboot (file uploaded, silent)
C = Explicit invoke (file uploaded, steps applied explicitly)

For each transcript set:

1. Count atomic factual statements and how many are correct.
2. Mark whether the task is solved (binary) for A, B and C.
3. Note any obvious collapses, rollbacks or recoveries.
4. Estimate a semantic drift distance between the intended goal and each answer.

Return for each mode:
ACC_A, ACC_B, ACC_C
SR_A, SR_B, SR_C
Stability_A, Stability_B, Stability_C    # e.g. MTTF or rollback ratio
SelfRecovery_A, SelfRecovery_B, SelfRecovery_C
Drift_A, Drift_B, Drift_C

Then compute deltas such as:
ΔACC_C−A, ΔSR_C−A, StabilityMultiplier = Stability_C / Stability_A, DriftReduction = Drift_A − Drift_C.

Do not guess beyond the evidence visible in the transcripts. If a quantity cannot be estimated, say so explicitly.
```

You can run this scorer across multiple seeds or batches and average the results.
If you publish numbers, please include your prompt set, model versions, and any modifications to the protocol.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<!-- WFGY_FOOTER_START -->

### Explore More

| Layer      | Page                                                                        | What it’s for                                                |
| ---------- | --------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Proof      | [WFGY Recognition Map](/recognition/README.md)                              | External citations, integrations, and ecosystem proof        |
| Engine     | [WFGY 1.0](/legacy/README.md)                                               | Original PDF based tension engine                            |
| Engine     | [WFGY 2.0](/core/README.md)                                                 | Production tension kernel and math engine for RAG and agents |
| Engine     | [WFGY 3.0](/TensionUniverse/EventHorizon/README.md)                         | TXT based Singularity tension engine, 131 S class set        |
| Map        | [Problem Map 1.0](/ProblemMap/README.md)                                    | Flagship 16 problem RAG failure checklist and fix map        |
| Map        | [Problem Map 2.0](/ProblemMap/rag-architecture-and-recovery.md)             | RAG focused recovery pipeline                                |
| Map        | [Problem Map 3.0](/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card, image as a debug protocol layer           |
| Map        | [Semantic Clinic](/ProblemMap/SemanticClinicIndex.md)                       | Symptom to family to exact fix                               |
| Map        | [Grandma’s Clinic](/ProblemMap/GrandmaClinic/README.md)                     | Plain language stories mapped to Problem Map 1.0             |
| Onboarding | [Starter Village](/StarterVillage/README.md)                                | Guided tour for newcomers                                    |
| App        | [TXT OS](/OS/README.md)                                                     | TXT semantic OS, fast boot                                   |
| App        | [Blah Blah Blah](/OS/BlahBlahBlah/README.md)                                | Abstract and paradox Q and A built on TXT OS                 |
| App        | [Blur Blur Blur](/OS/BlurBlurBlur/README.md)                                | Text to image with semantic control                          |
| App        | [Blow Blow Blow](/OS/BlowBlowBlow/README.md)                                | Reasoning game engine and memory demo                        |

If this repository helped, starring it improves discovery so more builders can find the docs and tools.
[![GitHub Repo stars](https://img.shields.io/github/stars/onestardao/WFGY?style=social)](https://github.com/onestardao/WFGY)

<!-- WFGY_FOOTER_END -->

