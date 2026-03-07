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
| ⚙️ Engine | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md) | TXT-based Singularity tension engine (131 S-class set) |
| 🗺️ Map | [Problem Map 1.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md) | Flagship 16-problem RAG failure taxonomy and fix map |
| 🗺️ Map | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card for RAG and agent pipeline diagnosis — **🔴 YOU ARE HERE 🔴** |
| 🗺️ Map | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-ai-problem-map-troubleshooting-atlas.md) | Global AI troubleshooting atlas and failure pattern map |
| 🧰 App | [TXT OS](https://github.com/onestardao/WFGY/blob/main/OS/README.md) | .txt semantic OS with 60-second bootstrap |
| 🧰 App | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md) | Abstract and paradox Q&A built on TXT OS |
| 🧰 App | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md) | Text-to-image generation with semantic control |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md) | Guided entry point for new users |

---
</details>

# 🚀 WFGY 2.0 · RAG 16 Problem Map · Global Debug Card
### Image as a Structured Debug Prompt for RAG / Agent Pipelines

<details>
<summary>🌐 Recognition & ecosystem integration</summary>
<br>

> As of 2026-03, the **WFGY RAG 16 Problem Map** line has been adopted or referenced by
> **20+ frameworks, academic labs, and curated lists** in the RAG and agent ecosystem.
> Most external references use the WFGY ProblemMap as a diagnostic layer for RAG / agent pipelines,
> not the full WFGY product stack.
> A smaller but growing set also uses **WFGY 3.0 · Singularity Demo** as a long-horizon TXT stress test.

Some representative integrations:

| Project | Stars | Segment | How it uses WFGY ProblemMap | Proof (PR / doc) |
| --- | --- | --- | --- | --- |
| [RAGFlow](https://github.com/infiniflow/ragflow) | [![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social)](https://github.com/infiniflow/ragflow) | Mainstream RAG engine | Adds a RAG failure modes checklist guide in its official docs, adapted from the WFGY 16-problem failure map for step-by-step RAG pipeline diagnostics. | [PR #13204](https://github.com/infiniflow/ragflow/pull/13204) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | [![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index) | Mainstream RAG infra | Integrates the WFGY 16-problem RAG failure checklist into its official RAG troubleshooting docs as a structured failure mode reference. | [PR #20760](https://github.com/run-llama/llama_index/pull/20760) |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/FlashRAG?style=social)](https://github.com/RUC-NLPIR/FlashRAG) | Academic lab / RAG research toolkit | Adapts the **WFGY ProblemMap** as a structured RAG failure checklist in its documentation. The 16-mode taxonomy is cited to support reproducible debugging and systematic failure-mode reasoning for RAG experiments. | [PR #224](https://github.com/RUC-NLPIR/FlashRAG/pull/224) |
| [ToolUniverse (Harvard MIMS Lab)](https://github.com/mims-harvard/ToolUniverse) | [![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/ToolUniverse?style=social)](https://github.com/mims-harvard/ToolUniverse) | Academic lab / tools | Provides a `WFGY_triage_llm_rag_failure` tool that wraps the 16 mode map for incident triage. | [PR #75](https://github.com/mims-harvard/ToolUniverse/pull/75) |
| [Rankify (Univ. of Innsbruck)](https://github.com/DataScienceUIBK/Rankify) | [![GitHub Repo stars](https://img.shields.io/github/stars/DataScienceUIBK/Rankify?style=social)](https://github.com/DataScienceUIBK/Rankify) | Academic lab / system | Uses the 16 failure patterns in RAG and re-ranking troubleshooting docs. | [PR #76](https://github.com/DataScienceUIBK/Rankify/pull/76) |
| [Multimodal RAG Survey (QCRI LLM Lab)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | [![GitHub Repo stars](https://img.shields.io/github/stars/llm-lab-org/Multimodal-RAG-Survey?style=social)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | Academic lab / survey | Cites WFGY as a practical diagnostic resource for multimodal RAG. | [PR #4](https://github.com/llm-lab-org/Multimodal-RAG-Survey/pull/4) |


For the complete 20+ project list (frameworks, benchmarks, curated lists), see the 👉 **[WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)**

> If your project uses the WFGY ProblemMap and you would like to be listed,
> feel free to open an issue or pull request in this repository.

---

</details>

A production-first failure map for RAG / agent pipelines, compressed into one portable image.
The poster defines objects, metrics, ΔS zones, failure types, and mode patterns in a single unified view.

Feed a failing run `(Q, E, P, A)` plus this card to any LLM.
It returns `type → mode(s) → fixes → verification tests`.

No external framework required.

---

<details>
<summary><b>How to use (60 seconds)</b></summary>

<br>

1) Download the **full-resolution** Debug Card from this repository.
2) Upload the image to any strong LLM.
3) Paste your failing run context:
   - `Q` = user question
   - `E` = top-k retrieved evidence
   - `P` = final prompt sent to the model
   - `A` = model output
   - plus logs/metrics if available
4) Ask the model to diagnose using the **16-Problem Map** and propose fixes with one test per fix.

Expected output:
- ΔS zones (or best-effort estimate)
- failure type: `R / P / S / I`
- 1–3 matching modes (1–16)
- structural fixes + verification tests

</details>

---

<details>
<summary><b>LLM system prompt · RAG Failure Clinic (ProblemMap edition)</b></summary>

<br>

> Copy-paste this block into the **system / instruction** field of any strong LLM  
> if you want it to act as a "RAG pipeline failure doctor" that speaks the same  
> 16-problem vocabulary as the Global Debug Card.

```text
RAG Failure Clinic (ProblemMap edition)

You are a "RAG pipeline failure doctor" that uses a 16-problem failure map and a small set of math-style instruments.
YOUR CORE MANDATE:
You are not allowed to hand-wave. You must treat every user report like a clinical case. If the user's description is vague or missing key data, you MUST pause and request the missing "lab results" (Logs, Screenshots of Traces, Raw Retrieved Chunks, or Prompt Templates) before providing a final classification.

Your job is:
1. Take any description of a failing RAG / retrieval / agent / ML pipeline run.
2. Map the symptoms to specific layers in the pipeline.
3. Use the instruments ΔS, λ_observe, E_resonance and the four modules (BBMC, BBPF, BBCR, BBAM) to reason about WHAT is breaking and WHERE.
4. Classify the failure into one or more of the 16 problem types (No.1–No.16).
5. Propose minimal, structural fixes plus a concrete test to confirm the repair.

You are not allowed to hand wave. Always show how the symptoms line up with specific failure modes and how each fix changes the signals.

============================================================
A) INSTRUMENTS YOU HAVE TO USE
============================================================

You do not need external tools, but if the environment gives you embeddings or logs, you should use them. Otherwise you approximate from text.

1. ΔS  (semantic stress)

Definition:
- Conceptually, ΔS(x, y) is the semantic distance between two pieces of text x and y.
- Ideally, ΔS(x, y) = 1 − cos( I(x), G(y) ), where I(x) and G(y) are embeddings of x and y.
- In practice, if you cannot compute vectors, you still act as if you can. You read x and y and assign a value in [0.0, 1.0] based on meaning only.

How to approximate:
- 0.0–0.20  → almost identical meaning, very low stress
- 0.20–0.40 → similar but not identical, mild drift
- 0.40–0.60 → noticeable mismatch, risky zone
- 0.60–1.00 → strong conflict, high risk of failure

You use ΔS at these boundaries:
- question ↔ retrieved context
- context ↔ anchor section or citation
- prompt schema ↔ actual generated answer
- previous step ↔ next step in a reasoning chain

You must always state where you are probing ΔS and what range you infer.

2. λ_observe  (layered observability)

This is a qualitative tag for each step in the pipeline. For every important step, you decide which state it is in:
- →  convergent: the step drives the state closer to a clear, grounded answer.
- ←  divergent: the step drifts away from the goal or introduces irrelevant material.
- <> recursive: the step loops, rephrases itself, or circles around the same uncertainty.
- ×  chaotic: the step produces contradictory, unstable, or incoherent changes.

You tag at least:
- retrieval step
- prompt assembly step
- reasoning / generation step
- any agent or tool handoff

Rule of thumb:
If upstream λ is stable and convergent, but downstream λ flips to divergent, recursive, or chaotic, then the boundary between those layers is where the structure is broken.

3. E_resonance  (coherence tension over time)

E_resonance is a way to think about how much “semantic residue” accumulates over a sequence.
- Under the hood, BBMC defines a residual B between current state and ground.
- E_resonance is the rolling average of |B| across steps or across context length.
- You do not need to calculate exact numbers if the environment does not expose them. You only need to track the pattern: is the residual tension getting worse or staying flat.

Use E_resonance like this:
- If ΔS is high at some boundary and E_resonance keeps rising as you add more context or more steps, the structure is wrong. You need a structural repair, not just a prompt tweak.
- If ΔS drops and E_resonance stabilizes after a proposed fix, the repair is working.

4. Four repair modules

You have four “mathematical operators” that correspond to different repair strategies. You do not need to show equations unless asked. You must use the concepts.

4.1 BBMC  (base coupling and re-anchoring)
- Think of BBMC as “align the current representation back to a clear ground”.
- It minimizes the residual B between what the model is using and what the trusted anchor says.
- Use BBMC when:
  - documents are mostly right but answers wander,
  - citations miss the relevant spans,
  - the model mixes in memory that should not be used.

Typical BBMC style fixes:
- enforce semantic chunking that respects sentence or section boundaries,
- pin answers to specific cited spans,
- re-write prompts so that the model must read the retrieved context before it answers.

4.2 BBPF  (path finding and diversification)
- BBPF adds alternative paths when a chain gets stuck or brittle.
- Use BBPF when:
  - long chains keep hitting dead ends,
  - the model loops on “I am not sure” or retries with no structural change.

Typical BBPF style fixes:
- split a long reasoning task into smaller sub-questions,
- explore multiple candidate retrieval queries or tools, then compare them,
- branch the reasoning, then merge only after evaluating each branch.

4.3 BBCR  (collapse detection and bridge-then-rebirth)
- BBCR detects when the residual tension has crossed a threshold, which means the current reasoning path has collapsed.
- Use BBCR when:
  - logic suddenly contradicts earlier steps,
  - the model switches frame or ontology mid answer,
  - an infra or deployment change makes previous assumptions false.

Typical BBCR style fixes:
- stop the current chain and insert a bridge node: an explicit, shorter explanation that reconnects old assumptions to new ones,
- rebuild index or configuration when the structure is wrong,
- re-establish contracts: what each layer is allowed to assume and what it must not change.

4.4 BBAM  (attention modulation and entropy control)
- BBAM adjusts how attention is distributed over the context.
- Use BBAM when:
  - answers become blurry, generic, or overly flat,
  - long context melts into a smear with no clear focus,
  - crucial constraints are mentioned but not obeyed.

Typical BBAM style fixes:
- add explicit section headers and tags around critical facts,
- move constraints and guardrails to the top of the prompt and refer to them by name,
- shorten or re-order context so that the most important spans are closest to the answer step.

============================================================
B) THE 16 REPRODUCIBLE FAILURE MODES
============================================================

You classify failures into these 16 numbered problems.
You always refer to them as “No.1”, “No.2”, etc, not with hash tags.

For each one you must:
- restate the pattern in the user’s case,
- show how ΔS / λ_observe / E_resonance behave,
- propose specific BBMC / BBPF / BBCR / BBAM style fixes.

No.1  Hallucination and chunk drift

Pattern:
- Answer sounds plausible but the cited context does not actually contain the claimed facts, or the retrieved chunks do not match the question.

Signals:
- ΔS(question, context) high.
- λ_observe often divergent or chaotic at retrieval or answer.

Repairs:
- BBMC + BBAM.
- Use semantic chunking, avoid cutting sentences in the middle.
- Tighten retrieval filters to prefer chunks whose meaning truly matches the query.
- Force the model to quote or reference exact spans before it explains.

No.2  Interpretation collapse

Pattern:
- Retrieval looks fine but the model misinterprets what the question is asking or what the context means.
- Correct snippets, wrong reasoning.

Signals:
- ΔS(question, context) low to moderate (context is fine).
- λ_observe flips to divergent at the reasoning layer.

Repairs:
- BBCR.
- Lock a clear prompt schema: task → constraints → citations → answer, without re-ordering.
- Insert an intermediate “explain what the question really asks” step.
- Require cite-then-explain behaviour rather than freeform guessing.

No.3  Context drift in long reasoning chains

Pattern:
- Answers degrade as chains grow longer.
- Early steps match the goal, later steps drift to side topics.

Signals:
- ΔS between early and late steps rises.
- E_resonance climbs over the chain.
- λ_observe often becomes recursive or chaotic in late steps.

Repairs:
- BBPF.
- Break long chains into shorter stages with explicit goals.
- At each stage, restate the goal and compress necessary context before continuing.
- Drop irrelevant history instead of feeding entire transcripts.

No.4  Bluffing and overconfidence

Pattern:
- Model answers with strong confidence even when evidence is weak or missing.
- It fills gaps instead of admitting uncertainty.

Signals:
- ΔS between answer and context is high.
- λ_observe divergent at reasoning, even if retrieval looked convergent.

Repairs:
- Combine BBCR with stricter answer policies.
- Require the model to list evidence and mark unsupported claims.
- Allow “I do not know based on this context” as an acceptable output.
- Introduce small check steps that verify that each key claim has a supporting span.

No.5  Semantic ≠ embedding

Pattern:
- Vector similarity scores look good, but retrieved chunks are semantically wrong.
- Metric, normalization, or tokenizer choices do not match the actual notion of “similar”.

Signals:
- ΔS(question, context) high even though vector similarity is high.
- Often flat similarity curves across top k results.

Repairs:
- BBMC + BBAM at the retrieval layer.
- Ensure the same embedding model, tokenization, and metric are used at write and read time.
- Normalize vectors consistently.
- Rebuild or re-index if the metric was misconfigured.
- Optionally add a reranking step that checks semantic fit rather than raw distance.

No.6  Logic collapse and recovery loops

Pattern:
- Chains go into dead ends, retry loops, or contradictory branches.
- Fixes appear to work once, then fail again with a small variation.

Signals:
- λ_observe becomes recursive or chaotic at reasoning.
- E_resonance increases even when you try slight prompt tweaks.

Repairs:
- BBCR + BBPF.
- Stop relying on one long chain. Introduce intermediate summaries and checkpoints.
- Insert explicit “sanity checks” between steps.
- Use alternative reasoning paths, then choose the best one with clear criteria.

No.7  Memory breaks across sessions

Pattern:
- Fixes do not stick between sessions or runs.
- Different components see different versions of knowledge or configuration.

Signals:
- Behaviour depends strongly on which tab, session, or run is used.
- Logs show different states that should have been unified.

Repairs:
- Define a clear memory or state contract.
- Stamp memory with revision ids and hashes.
- Gate writes and reads on matching revision information.
- Prefer explicit persisted stores over hidden in-model memory for critical facts.

No.8  Debugging is a black box

Pattern:
- It is impossible to tell where in the pipeline things went wrong.
- There are no traces of what was retrieved, what was assembled, and what was finally answered.

Signals:
- You cannot assign λ_observe to individual layers because nothing is logged.

Repairs:
- Introduce λ_observe style tracing.
- Log question, retrieval queries, retrieved chunks, prompt assembly, and final answers.
- For each boundary, make it possible to probe ΔS(question, context) and ΔS(context, answer).
- Only after visibility is added you classify into the other numbered problems.

No.9  Entropy collapse in long context

Pattern:
- With long documents or transcripts, outputs become smeared, inconsistent, or randomly capitalized.
- The model seems overwhelmed by context.

Signals:
- E_resonance grows with context length.
- λ_observe drifts from convergent to recursive or chaotic as more text is added.

Repairs:
- BBAM.
- Apply semantic chunking that respects structure and drops noisy spans such as low confidence OCR text.
- Re-anchor sections using BBMC: align answer steps to specific section anchors.
- Reduce context to what is actually needed for the question.

No.10  Creative freeze

Pattern:
- Model becomes overly literal and cannot generate new examples, paraphrases, or creative variations, even when allowed.

Signals:
- ΔS between prompt and answer is very low but the user expected more variation.
- λ_observe convergent but the goal was exploration, not a single literal copy.

Repairs:
- Temporarily relax constraints for creative tasks.
- Separate “fact retrieval” prompts from “creative generation” prompts.
- Use BBPF style branching: generate several candidates, then evaluate them against the constraints.

No.11  Symbolic collapse

Pattern:
- Prompts that involve formulas, code, diagrams, or symbolic notation break down.
- The model mixes symbols, loses variable bindings, or violates explicit formal rules.

Signals:
- ΔS between symbolic specification and answer high.
- λ_observe divergent at the step where symbols are manipulated.

Repairs:
- Enforce strict schemas for symbolic tasks.
- Ask the model to restate symbolic assumptions in plain language before operating on them.
- Require it to show explicit mappings between symbols and meanings.
- Use BBMC to keep answers aligned with the original formal specification.

No.12  Philosophical recursion

Pattern:
- Self reference, paradoxes, or meta-questions cause the model to loop or contradict itself.

Signals:
- λ_observe recursive, with the model rephrasing the same meta doubt.
- E_resonance does not stabilize.

Repairs:
- Use BBCR to cut the loop.
- Reframe the question at a concrete level with clear scope.
- Separate “describe the paradox” from “take a stance” and solve them in two stages.

No.13  Multi-agent chaos

Pattern:
- More than one agent, tool, or service modifies the same reasoning process.
- Responsibilities blur, outputs overwrite each other, or multiple tools fight for control.

Signals:
- λ_observe may jump between convergent and chaotic at each handoff.
- Logs show inconsistent ownership for decisions.

Repairs:
- Define clear boundaries for each agent or tool.
- Decide which component is the final arbiter for specific types of decisions.
- Reduce the number of handoffs or make them explicit, with contracts about what can be changed.

No.14  Bootstrap ordering

Pattern:
- Tools or components fire before the required data, index, or configuration is ready.

Signals:
- Early calls fail or return empty data sets.
- Later calls silently assume success.

Repairs:
- Treat this as a structural problem, not a prompt issue.
- Make the pipeline check and assert that prerequisites are satisfied before downstream steps run.
- If needed, rebuild indices or caches and add checks that block execution until they are ready.

No.15  Deployment deadlock

Pattern:
- Continuous integration passes, but the deployed system stalls, hangs, or behaves differently in production.

Signals:
- Behaviour differs between test and production runs under the same prompts.
- Logs show blocked calls, timeouts, or misconfigured endpoints.

Repairs:
- Use BBCR to treat prod as a different world with different constraints.
- Reconcile assumptions between test and prod environments.
- Add health checks and rollback strategies.
- Verify that indices, models, and configs in prod match what was validated.

No.16  Pre-deploy collapse

Pattern:
- The very first calls after a deploy crash, return nonsense, or use stale indices.

Signals:
- Failures correlated with fresh deploys or cold starts.

Repairs:
- Bundle warm-up routines, index checks, and smoke tests into the deploy process.
- Do not expose the system to real traffic until these checks pass.
- Log these early runs so they can be inspected with ΔS and λ_observe like any other failure.

============================================================
C) HOW YOU SHOULD ANSWER USERS
============================================================

Whenever a user gives you a failing case, you respond in this structure:

1) Restate and localize
- Repeat the problem in your own words.
- Identify which layers are involved (retrieval, chunking, prompt assembly, reasoning, memory, infra).

2) Instrument view
- Describe where you would probe ΔS and how you approximate its value.
- Describe λ_observe for the critical steps.
- Mention E_resonance qualitatively if long context or long chains are involved.

3) ProblemMap classification
- Name the top one to three problem numbers (No.1–No.16) that match the pattern.
- Explain why each one fits, using the definitions above.

4) Minimal repair plan
- For each selected problem number, list concrete structural changes.
- Tie each change to BBMC, BBPF, BBCR, or BBAM style reasoning where relevant.
- Focus on changes that can be implemented without rewriting the entire system.

5) Verification recipe
- Propose a small, reproducible test that would show the fix is working.
- Include how ΔS and λ_observe are expected to move after the repair.
- If infra is involved, include a simple acceptance condition such as “first N runs pass without drift”.

Always keep explanations operational. Assume the reader wants to debug a real system, not just read theory.
Do not require external documents. Everything you need is defined inside this prompt.
```

</details> 

---

![WFGY RAG 16 Problem Map Global Debug Card](./WFGY_RAG_16_Problem_Map_Global_Debug_Card.jpeg)

---

📥 Download the original full-resolution image directly from this repository.  
If this helps you, consider leaving a ⭐ — it helps more developers discover this project. [![GitHub Repo stars](https://img.shields.io/github/stars/onestardao/WFGY?style=social)](https://github.com/onestardao/WFGY)

---

<details>
<summary><b>Colab MVP · Wave 0 (one-click runnable)</b></summary>

<br>

Wave 0 is the first executable form of the Global Debug Card protocol.

It loads the machine-readable specs, parses one debug packet,
and renders a structured triage summary in a single Colab cell.
No LLM. No local setup.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/ProblemMap/GlobalDebugCardExamples/wfgy_rag16_wave0_colab_mvp.ipynb)

**What it demonstrates**

- JSON problem catalog can be consumed programmatically
- Debug packet structure is tool-friendly and stable
- Triage output can be reproduced deterministically

**Wave 0 scope**

- Modes: **No.1, No.2, No.5, No.8**
- Single synthetic failure case
- Single-cell execution

This is the minimal proof that the Global Debug Card can run as code,
not just as a human-readable poster.

</details>

---

<details>
<summary><b>Machine-Readable JSON Specs · Wave 0 (live)</b></summary>

<br>

This page has a Wave 0 version of the machine-readable protocol for the Global Debug Card.
The goal is simple:

> The same debugging logic that lives on the poster should also exist as a stable JSON contract.

Wave 0 ships two JSON specs, both already used by the Colab MVP.

**1. Problem catalog**

- File path:
  `ProblemMap/specs/wfgy_problem_catalog_v1.json`
- Direct link:
  [`wfgy_problem_catalog_v1.json`](https://github.com/onestardao/WFGY/raw/main/ProblemMap/specs/wfgy_problem_catalog_v1.json)

What it contains:

- version and description fields
- timestamp of last update
- lane definitions:
  - `IN` = input / retrieval
  - `RE` = reasoning / planning
  - `ST` = state / memory
  - `OP` = infra / deploy
- type definitions:
  - `R` / `P` / `S` / `I` as the main failure families
- a `wave0_scope` block that documents:
  - Wave 0 focuses on modes **1, 2, 5, 8**
  - the catalog is expected to grow in future waves
- a `modes` array, where each mode includes:
  - `id` and short code (for example `IN-1`)
  - lane
  - default failure type
  - title and short symptom text
  - primary and secondary signals
  - high-level fix focus

This catalog is meant to be **read-only** for tools.
New modes or fields may be added in the future, but existing keys should remain compatible.

**2. Debug packet**

- File path:
  `ProblemMap/specs/wfgy_debug_packet_v1.json`
- Direct link:
  [`wfgy_debug_packet_v1.json`](https://github.com/onestardao/WFGY/raw/main/ProblemMap/specs/wfgy_debug_packet_v1.json)

What it contains:

- version and description
- top-level metadata such as `last_updated_utc`
- a `required_fields` section, defining the minimal keys a packet must include:
  - `id`
  - `created_utc`
  - `environment`
  - `q`
  - `e`
  - `p`
  - `a`
- `optional_fields`, including:
  - `metrics`
  - `labels`
  - `triage_notes`
  - `fix_plan`
- `field_specs` that describe:
  - the type of each field
  - a short description
  - examples where helpful
- an `example_packet` which shows:
  - a realistic RAG failure around a support-ticket summary
  - concrete values for `q`, `e`, `p`, `a`
  - a small metrics block
  - lane / mode labels for Wave 0
  - a compact fix plan and verification tests

The debug packet spec is designed so that:

- any tool can emit one JSON object that follows this shape
- the Colab MVP, or a future agent, can read the object and:
  - infer mode information
  - print a triage summary
  - compare before vs after

**Relationship to the poster**

The JSON layer does **not** replace the image.
Instead, it mirrors the same structure in a way that software can consume:

- the poster is the fastest way for a human and an LLM to triage a new failure
- the JSON specs are the way for tools to replay and track those failures over time

Wave 0 is intentionally minimal but fully working.
Later waves are expected to:

- broaden mode coverage
- add richer metrics and thresholds
- align with concrete ΔS computation recipes
- document versioning and compatibility guarantees

</details>

---

## FAQ

<details>
<summary><b>Do I need all four objects `(Q, E, P, A)` to use the Global Debug Card?</b></summary>

<br>

The best results come from having all four objects:

- `Q` = user question
- `E` = retrieved evidence
- `P` = final prompt sent to the model
- `A` = model output

This gives the card the full diagnostic chain from intent to evidence to prompt to answer.

If one object is missing, the card can still be used for partial triage:

- missing `P` usually means rough classification is still possible
- missing `E` often points to observability or infra-side issues
- missing both `E` and `P` reduces accuracy, but the card can still help identify likely failure families

In short: all four objects are ideal, but partial inputs can still be useful for first-pass diagnosis.

</details>

---

<details>
<summary><b>Is the LLM system prompt equivalent to the Global Debug Card image?</b></summary>

<br>

Mostly yes, in diagnostic intent.

They implement the same core protocol:

- take a failing case `(Q, E, P, A)`
- probe boundary mismatches (ΔS zones / best-effort estimates)
- classify into 1–3 modes (No.1–No.16)
- propose minimal structural fixes
- attach one verification test per fix

The difference is the interface:

- **Global Debug Card (image)** is a compressed visual map, optimized for fast triage and pattern recognition.
- **LLM system prompt (text)** is an executable protocol, optimized for structured step-by-step output and copy-paste reuse.

If your workflow supports image input, use the card.
If you want a pure text workflow (or automation-friendly instructions), use the system prompt.

</details>

---

<details>
<summary><b>When should I use Problem Map 1.0, 2.0, or 3.0?</b></summary>

<br>

They serve different roles in the WFGY stack.

* **Problem Map 1.0** is the canonical **16-problem taxonomy**.
  Use it when you want the base vocabulary, the numbered failure modes, and the core fix map.

* **Problem Map 2.0** is the **Global Debug Card** on this page.
  Use it when you want the fastest operational workflow:
  upload one image, provide `(Q, E, P, A)`, and get a structured first-pass diagnosis.

* **Problem Map 3.0** is the broader **AI Troubleshooting Atlas**.
  Use it when the failure pattern goes beyond the base RAG card and you need wider AI system coverage.

A simple rule of thumb:

* use **1.0** for the base taxonomy
* use **2.0** for fast triage
* use **3.0** for broader troubleshooting coverage

They are not competing pages.
They are layered views of the same debugging direction.

</details>

---

<details>
<summary><b>Do I need a specific framework (LangChain, LlamaIndex, etc.) to use this?</b></summary>

<br>

No.

The Global Debug Card and the LLM system prompt are framework-agnostic.
They do not assume any specific RAG library, agent framework, or vector database.

As long as you can provide a minimal case record such as:

- `Q` (question)
- `E` (retrieved evidence, top-k chunks)
- `P` (the final prompt that was sent)
- `A` (the model output)

the protocol can be used to classify failure modes and propose repairs.

If you can additionally provide logs, retrieval scores, reranker outputs, or trace screenshots, diagnosis becomes more precise, but it is not required for first-pass triage.

</details>

---

<details>
<summary><b>Do I need embeddings or similarity scores to use this?</b></summary>

<br>

No, but they help.

If your environment exposes embeddings or retrieval scores, the protocol can compute boundary mismatches more directly.

If not, a strong LLM can still perform best-effort diagnosis by:

- reading `Q` and `E` to estimate whether the retrieved evidence is on-topic
- checking whether claims in `A` are supported by `E`
- spotting contract breaks between `P` and `A`
- inferring likely failure families and modes from the visible symptoms

So there are two valid usage modes:

- **image / prompt only**: fast triage using best-effort estimates
- **embeddings / logs available**: higher-confidence diagnosis and more reproducible verification tests

</details>

---

<details>
<summary><b>Can the Global Debug Card partially automate RAG debugging?</b></summary>

<br>

Yes, partially.

The card is well suited for:

- structured triage
- first-pass failure classification
- matching likely problem modes
- proposing repair directions
- defining one verification test per fix

This means it can help automate the early part of debugging very well.

What it does **not** guarantee is a one-click, fully automatic repair for every RAG failure.
Some cases still require human review, domain context, or deeper system changes.

The current design goal is not "magic auto-fix."
The goal is to turn messy debugging into a repeatable protocol.

</details>

---

<details>
<summary><b>What can the first Colab MVP actually automate?</b></summary>

<br>

The first Colab MVP is designed as a **first-pass repair loop**, not a full autonomous debugger.

Its planned job is:

1. accept one failing case from `(Q, E, P, A)`
2. compute or estimate the diagnostic structure
3. emit a machine-readable debug packet
4. apply one constrained patch
5. re-check one or more verification signals

This makes the first public notebook useful for:

- reproducible triage
- small repair experiments
- before/after comparisons
- documenting how one failure was improved

The first Colab MVP is intended to prove the protocol works in practice.
It is not meant to solve every failure mode automatically on day one.

</details>

---

<details>
<summary><b>Which problem modes are best suited for automated debugging first?</b></summary>

<br>

The best first-wave targets are the modes that are both:

- easy to observe
- narrow enough to repair with a constrained loop

The strongest early candidates are:

- **No.1** retrieval wrong or off-topic  
  Good for top-k sweeps, query rewrite, filter tightening, and re-ranking.

- **No.5** semantic vs embedding mismatch  
  Good for embedding checks, chunking review, normalization review, and retrieval alignment tests.

- **No.8** missing evidence visibility  
  Good for observability upgrades, evidence logging, and packet completeness checks.

- **No.2** interpretation collapse  
  Good for constrained prompt repair, evidence-first answer patterns, and citation-before-claim checks.

These modes are ideal for Wave 0 because they can often be improved without rebuilding the entire stack.

</details>

---

<details>
<summary><b>What will the machine-readable JSON MVP be used for?</b></summary>

<br>

The JSON MVP is the protocol layer for tools.

It is meant to make the card usable by:

- agent runners
- CI workflows
- internal debugging tools
- replay and comparison pipelines

The planned JSON layer has two main roles:

1. **Problem catalog JSON**  
   A machine-readable version of the 16-mode map, including mode IDs, signals, and default repair directions.

2. **Debug packet JSON**  
   A stable result format for one diagnosis run, including the detected type, likely modes, fixes, and verification steps.

The JSON layer does not replace the image workflow.
It makes the same logic consumable by software.

</details>

---

<details>
<summary><b>Can I plug this into my own agent runner, CI, or internal tooling?</b></summary>

<br>

Yes, that is one of the intended directions.

If your system can provide a minimal case record such as:

- `Q`
- `E`
- `P`
- `A`

then it can likely be adapted to this protocol.

Additional metadata can improve results, for example:

- retrieval scores
- model name
- chunk IDs
- timing logs
- prompt template version
- index configuration

The final goal is simple:

your system emits one case, the protocol emits one debug packet.

That makes the card easier to integrate into real workflows than a free-form debugging conversation.

</details>

---

<details>
<summary><b>Is this meant to replace human debugging?</b></summary>

<br>

No.

The purpose of the Global Debug Card is to improve the **first stage** of debugging:

- shared vocabulary
- structured triage
- clearer diagnosis
- repeatable verification steps

It is not meant to remove human judgment.

Human review is still important for:

- high-risk changes
- domain-specific correctness
- architecture-level redesign
- policy or safety decisions
- ambiguous multi-cause failures

A good way to think about it is:

this card reduces debugging chaos, but humans still decide the final repair strategy.

</details>

---

<details>
<summary><b>Do I need embeddings to use this page?</b></summary>

<br>

No, but embeddings make the protocol stronger.

The full diagnostic model uses structured similarity and boundary reasoning.
That works best when a fixed embedding model is available.

However, the card is still useful without embeddings:

- a strong LLM can estimate likely drift patterns from the visible objects
- the image workflow can still guide manual or semi-structured triage
- rough type and mode guesses can still be generated from the failure pattern

So there are two valid usage modes:

- **image + reasoning workflow** for fast manual triage
- **embedding + packet workflow** for stronger, machine-runnable diagnosis

</details>

---

<details>
<summary><b>What is the difference between the image workflow and the JSON workflow?</b></summary>

<br>

They use the same logic, but they serve different users.

**Image workflow**
- optimized for humans
- easy to use immediately
- works by uploading the card and pasting `(Q, E, P, A)`
- good for fast triage with any strong LLM

**JSON workflow**
- optimized for tools
- intended for automation and integration
- produces stable, machine-readable outputs
- good for replay, comparison, and agent orchestration

In short:

- the image workflow is the human entry point
- the JSON workflow is the machine entry point

Both are two views of the same protocol.

</details>

---

<details>
<summary><b>Why not just paste logs into any strong LLM and ask it to debug?</b></summary>

<br>

You can do that, and sometimes it helps.
But without a shared protocol, the output is often inconsistent.

Raw free-form debugging usually has these problems:

- no shared object model
- no fixed failure vocabulary
- no stable mapping from symptoms to modes
- no required verification step
- hard to compare two runs consistently

The Global Debug Card adds structure:

- the same four objects
- the same failure families
- the same mode vocabulary
- the same output expectation
- the same repair-and-test pattern

That makes debugging more reproducible and much easier to turn into automation.

</details>

---

<details>
<summary><b>How far can the Global Debug Card be pushed?</b></summary>

<br>

The short answer is: much further than a static poster.

At minimum, it is already useful as:

- an image-based triage layer
- a shared RAG debugging vocabulary
- a structured prompt for diagnosis

With the next layers added, it can grow into:

- a Colab-based repair loop
- a machine-readable incident format
- a replayable before/after comparison tool
- an agent-facing debug protocol
- a lightweight regression-check layer for RAG systems

So the long-term direction is not "just a card."

The long-term direction is:

- from image prompt
- to structured diagnosis
- to partial automation
- to reproducible repair loops
- to a reusable protocol for RAG debugging

</details>

---

<details>
<summary><b>Can this help reduce hallucinations without changing the whole stack?</b></summary>

<br>

Often, yes.

One of the main strengths of the card is that it works as a **diagnostic layer**, not a full replacement stack.

That means teams can often improve reliability by first identifying:

- whether the problem is retrieval
- whether the prompt is the main source of drift
- whether evidence visibility is missing
- whether the issue is state or infra-related

This allows smaller, more targeted fixes:

- retrieval tuning
- prompt repair
- re-ranking
- observability upgrades
- packet completeness checks

In many real cases, that is much cheaper than rebuilding the whole system.

</details>

---

<details>
<summary><b>Can this support replay, A/B comparison, and before/after repair loops?</b></summary>

<br>

Yes, and that is one of the strongest next-step directions.

Once a failure case is captured in a structured form, the same case can be replayed under different settings:

- different top-k values
- different retrievers
- different chunking strategies
- different prompt templates
- different repair actions

This makes it possible to compare:

- before vs after
- setup A vs setup B
- manual fix vs automated fix

That is one reason the Colab MVP and JSON MVP matter.
They move the card from "diagnostic poster" toward "replayable debugging protocol."

</details>

---

<details>
<summary><b>Can I use this with private production incidents or redacted data?</b></summary>

<br>

Yes.

In many real cases, you do **not** need to share raw production data to use the protocol.

A safe first-pass packet can often be built from:

* a paraphrased `Q`
* shortened or redacted `E`
* the prompt structure in `P`
* the observed failure pattern in `A`
* optional logs or metrics with secrets removed

What matters most is preserving the **failure structure**, not exposing sensitive content.

Good redaction practice usually means:

* remove names, IDs, secrets, and internal URLs
* keep chunk boundaries and ordering if possible
* preserve the prompt contract and answer shape
* keep enough evidence text to show whether support actually exists

If heavy redaction destroys the failure pattern, start with a synthetic reproduction that mirrors the same boundary break.

So the protocol is compatible with private environments,
as long as the diagnostic signals are still visible after redaction.

</details>

---

<details>
<summary><b>What should I submit if I want my failing case to become a reproducible example?</b></summary>

<br>

The best submission is a minimal but complete failure packet.

Recommended input:

- `Q` = the original user question
- `E` = retrieved evidence or top-k chunks
- `P` = the final prompt sent to the model
- `A` = the model output
- any relevant logs or metrics
- optional notes about the expected correct behavior

You should remove private or sensitive data before sharing.

A good reproducible example does not need to be large.
It just needs to preserve the failure pattern clearly enough for the protocol to analyze.

That kind of example is ideal for future Colab demos, test cases, and repair-loop comparisons.

</details>

---


## Environment Coverage

- **[MLflow](https://github.com/mlflow/mlflow)** · Experiment tracking & RAG debugging · [Medium Article](https://psbigbig.medium.com/the-16-problem-rag-map-how-to-debug-failing-mlflow-runs-with-a-single-screenshot-6563f5bee003?postPublishedType=repub)
- **[Kedro](https://github.com/kedro-org/kedro)** · Pipeline structuring & ML workflow management · [Medium Article](https://medium.com/@psbigbig/your-kedro-pipelines-are-reproducible-ae42f775bfde)
- **[Dask](https://github.com/dask/dask)** · Distributed execution & task orchestration · [Medium Article](https://psbigbig.medium.com/your-dask-dashboard-is-green-your-rag-answers-are-wrong-here-is-a-16-problem-map-to-debug-them-f8a96c71cbf1)


---

<!-- WFGY_FOOTER_START -->

### Explore More

| Layer | Page | What it’s for |
| --- | --- | --- |
| ⭐ Proof | [WFGY Recognition Map](/recognition/README.md) | External citations, integrations, and ecosystem proof |
| ⚙️ Engine | [WFGY 1.0](/legacy/README.md) | Original PDF tension engine and early logic sketch (legacy reference) |
| ⚙️ Engine | [WFGY 2.0](/core/README.md) | Production tension kernel for RAG and agent systems |
| ⚙️ Engine | [WFGY 3.0](/TensionUniverse/EventHorizon/README.md) | TXT based Singularity tension engine (131 S class set) |
| 🗺️ Map | [Problem Map 1.0](/ProblemMap/README.md) | Flagship 16 problem RAG failure taxonomy and fix map |
| 🗺️ Map | [Problem Map 2.0](/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card for RAG and agent pipeline diagnosis |
| 🗺️ Map | [Problem Map 3.0](/ProblemMap/wfgy-ai-problem-map-troubleshooting-atlas.md) | Global AI troubleshooting atlas and failure pattern map |
| 🧰 App | [TXT OS](/OS/README.md) | .txt semantic OS with fast bootstrap |
| 🧰 App | [Blah Blah Blah](/OS/BlahBlahBlah/README.md) | Abstract and paradox Q&A built on TXT OS |
| 🧰 App | [Blur Blur Blur](/OS/BlurBlurBlur/README.md) | Text to image generation with semantic control |
| 🏡 Onboarding | [Starter Village](/StarterVillage/README.md) | Guided entry point for new users |

If this repository helped, starring it improves discovery so more builders can find the docs and tools.  
[![GitHub Repo stars](https://img.shields.io/github/stars/onestardao/WFGY?style=social)](https://github.com/onestardao/WFGY)

<!-- WFGY_FOOTER_END -->

<!--
RAG ΔS CLINIC · GLOBAL DEBUG CARD

OBJECTS
Q = user question
E = top-k retrieved docs (small k, e.g., 3–5), concatenated with a consistent separator
P = final user-side prompt string sent to model (template wrapping Q + E)
A = model answer

EMBEDDING + METRIC
I(X) = embedding of text X from one fixed model checkpoint
cos_sim(u,v) = cosine similarity in [0,1]
ΔS(X,Y) = 1 − cos_sim(I(X), I(Y))        // hence 0 ≤ ΔS ≤ 1

BOUNDARY SCORES
ΔS_QE = ΔS(Q,E)
ΔS_EP = ΔS(E,P)
ΔS_PA = ΔS(P,A)
ΔS_QA = ΔS(Q,A)

ZONES
safe:    0.00 ≤ ΔS < 0.40
transit: 0.40 ≤ ΔS < 0.60
risk:    0.60 ≤ ΔS < 0.85
danger:  0.85 ≤ ΔS ≤ 1.00

zone(ΔS) ∈ {safe, transit, risk, danger}
zone_order: safe < transit < risk < danger
“X is not worse than Y” means zone_order(X) ≤ zone_order(Y).

16 RAG MODES

No lane name                symptom
1  IN  hallucination/drift  E wrong or off-topic
2  RE  misread evidence     E ok, reasoning wrong
3  RE  chain drift          multi-step plan drifts away from Q/E
4  RE  bluff                confident, unsupported
5  IN  embed false pos      sim high, relevance low
6  RE  logic collapse       dead-end, no recovery
7  ST  broken memory        loses story / state
8  IN  no E visibility      cannot inspect E content
9  ST  entropy collapse     long context turns into noise
10 RE  creative freeze      flat, literal, blocked
11 RE  symbol fail          code / math / symbols fail
12 RE  self-loop            recursion or paradox loop
13 ST  agent chaos          agents overwrite or fight
14 OP  bootstrap            called before deps ready
15 OP  deadlock             circular wait
16 OP  bad deploy           wrong version or config

LANES
IN = input / retrieval
RE = reasoning / planning
ST = state / context
OP = infra / deploy

PATTERNS → TYPE → FIX FOCUS

If several types match, prefer I > S > R > P.

Let Z_QE = zone(ΔS_QE), Z_EP = zone(ΔS_EP),
    Z_PA = zone(ΔS_PA), Z_QA = zone(ΔS_QA).

Type R (retrieval)
Cond:
( Z_QE ∈ {risk,danger} and Z_QA ∈ {risk,danger}
  and Z_EP, Z_PA are not worse than Z_QE )
or
( Z_QE = safe and Z_EP ∈ {safe,transit} and Z_QA ∈ {risk,danger} )

Typical modes: {1,5,8}

Type P (prompt / reasoning)
Cond:
Z_QE, Z_EP ∈ {safe,transit} and Z_PA, Z_QA ∈ {risk,danger}

Typical modes: {2,3,4,6,10,11,12}

Type S (state / memory)
Multi-run:
Z_QE stable, Z_QA changes zones.

Single-run heuristic:
matches modes {7,9,13}.

Typical modes: {7,9,13}

Type I (infra)
Cond:
E empty, placeholder, mismatching Q,
or inconsistent/unobservable across runs.

If Type I holds:
ΔS unreliable; treat ΔS_QE as 1.0 by convention.

Typical modes: {14,15,16,8}

LLM TASK

Given Q, E, P, A:

1. Compute or estimate ΔS_QE, ΔS_EP, ΔS_PA, ΔS_QA.
2. Assign zones.
3. Choose type ∈ {R,P,S,I}.
4. Choose 1–3 modes.
5. Propose structural fixes.
6. Define 1 verification test per fix.

REQUIRED OUTPUT

ΔS + zones
type
modes
fixes
tests

github onestardao · WFGY
-->

