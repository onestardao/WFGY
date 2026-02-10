<!--
Search Anchor:
reasoning global fix map
reasoning failure modes
long chain stability
chain of thought stability
cot variance clamp
reasoning collapse map
hallucination reentry
recursive reasoning loop
logic collapse invariants
symbolic collapse abstraction
proof dead ends unprovable steps
anchoring bridge proofs
context stitching window joins
redundant evidence collapse
entropy overload long plans
llm planning never converge
multi step answer drift
rerun same question different answer
window roll loses anchor
long chat loses earlier facts
plan keeps growing never lands
model rewrites reality in long plans
drift across seeds and paraphrases
auditable reasoning steps
deterministic step count

Typical reasoning bugs:
steps keep growing and answer never lands
model goes in circles and repeats itself
model re asserts false claim after correction
reasoning jumps without citing source step
invariants vanish during abstraction jump
proof chain stalls at unprovable step
model changes interpretation mid chain
long context window drops earlier anchor
window joins flip the claim
different runs choose different evidence
reruns disagree on the same question
minority facts drowned by many similar snippets
model cherry picks evidence to support wrong answer
different seeds give different final conclusion
answer depends on irrelevant snippet ordering
model conflates hypothetical with real data

When to use this folder:
rag already fixed but answers still drift
retrieval stable yet explanation changes every run
you see hallucination only in long plans
cot used but not reproducible
agent loop does many steps without progress
mathematical proof suddenly switches frame
safety or governance chain needs audit trail
researcher wants to compare seeds and paraphrases
benchmark requires stable long chain behavior
legal or medical reasoning must be traceable

Key metrics and targets:
delta s question selected evidence <= 0.45 on all runs
coverage of target section >= 0.70 with cite then explain
lambda observe convergent across three paraphrases and two seeds
e_resonance flat across long windows and window joins
deterministic step count per stage after clamps applied
no hallucination reentry after correction
same conclusion across seeds given same evidence
proof chain explicit about each jump and its source
no hidden frame jumps or abstraction collapse
reasons and evidence stay aligned across windows

Core pages in this folder:
ProblemMap/GlobalFixMap/Reasoning/entropy-overload.md
ProblemMap/GlobalFixMap/Reasoning/recursive-loop.md
ProblemMap/GlobalFixMap/Reasoning/hallucination-reentry.md
ProblemMap/GlobalFixMap/Reasoning/logic-collapse.md
ProblemMap/GlobalFixMap/Reasoning/symbolic-collapse.md
ProblemMap/GlobalFixMap/Reasoning/proof-dead-ends.md
ProblemMap/GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md
ProblemMap/GlobalFixMap/Reasoning/context-stitching-and-window-joins.md
ProblemMap/GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md
ProblemMap/GlobalFixMap/Reasoning/redundant-evidence-collapse.md

Related structural fixes:
ProblemMap/rag-architecture-and-recovery.md
ProblemMap/retrieval-playbook.md
ProblemMap/retrieval-traceability.md
ProblemMap/data-contracts.md
ProblemMap/context-drift.md
ProblemMap/entropy-collapse.md
ProblemMap/rerankers.md
ProblemMap/embedding-vs-semantic.md
ProblemMap/Embeddings/metric_mismatch.md
ProblemMap/Embeddings/normalization_and_scaling.md

Reasoning scenarios:
multi step financial plan changes answer across runs
safety policy chain contradicts itself later
math proof switches definition mid argument
system design review flips conclusion with same docs
governance decision tree loops on same node
research summary hallucinate extra papers
cot explanation disagrees with final answer
agent rewrites the task mid execution
long back and forth chat forgets original constraint
model keeps expanding plan without committing

Signals to check:
coverage good but lambda unstable
delta s low on evidence but conclusion different
citations stable but reasoning text drifts
proof steps not numbered or auditable
no explicit reference to step that caused jump
branching factor keeps increasing per step
model keeps asking for more context
seed one and seed two disagree on final verdict
paraphrase question changes the reasoning path
-->

<!--
Cross folder jumps:
ProblemMap/GlobalFixMap/Reasoning/README.md
ProblemMap/rag-architecture-and-recovery.md
ProblemMap/retrieval-playbook.md
ProblemMap/retrieval-traceability.md
ProblemMap/context-drift.md
ProblemMap/entropy-collapse.md
ProblemMap/rerankers.md
ProblemMap/GlobalFixMap/Retrieval/README.md
ProblemMap/GlobalFixMap/Embeddings/README.md
ProblemMap/GlobalFixMap/Chunking/README.md
ProblemMap/SemanticClinicIndex.md
-->


# Reasoning — Global Fix Map

<details>
  <summary><strong>🏥 Quick Return to Emergency Room</strong></summary>

<br>

  > You are in a specialist desk.  
  > For full triage and doctors on duty, return here:  a
  > 
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
  > 
  > Think of this page as a sub-room.  
  > If you want full consultation and prescriptions, go back to the Emergency Room lobby.
</details>

A compact hub to keep long chains stable, prevent collapse, and make decisions auditable.  
Use this folder when answers drift across runs, chains dead end, or the model rewrites reality during long plans.  
Every page maps symptoms to exact WFGY fixes with measurable targets. No infra change required.

---

<!--
Anchor Menu:
open: entropy overload guide ProblemMap/GlobalFixMap/Reasoning/entropy-overload.md
open: recursive loop guide ProblemMap/GlobalFixMap/Reasoning/recursive-loop.md
open: hallucination reentry guide ProblemMap/GlobalFixMap/Reasoning/hallucination-reentry.md
open: logic collapse guide ProblemMap/GlobalFixMap/Reasoning/logic-collapse.md
open: symbolic collapse guide ProblemMap/GlobalFixMap/Reasoning/symbolic-collapse.md
open: proof dead ends guide ProblemMap/GlobalFixMap/Reasoning/proof-dead-ends.md
open: anchoring and bridge proofs guide ProblemMap/GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md
open: context stitching and window joins guide ProblemMap/GlobalFixMap/Reasoning/context-stitching-and-window-joins.md
open: chain of thought variance clamp guide ProblemMap/GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md
open: redundant evidence collapse guide ProblemMap/GlobalFixMap/Reasoning/redundant-evidence-collapse.md

jump: rag architecture and recovery visual map ProblemMap/rag-architecture-and-recovery.md
jump: retrieval playbook knobs and metrics ProblemMap/retrieval-playbook.md
jump: retrieval traceability and data contracts ProblemMap/retrieval-traceability.md ProblemMap/data-contracts.md
jump: long context drift and entropy collapse ProblemMap/context-drift.md ProblemMap/entropy-collapse.md
jump: rerankers for ordering evidence ProblemMap/rerankers.md
-->


## Orientation: what each page solves

| Page | What it fixes | Typical symptom |
|---|---|---|
| [Entropy Overload](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/entropy-overload.md) | Caps branching and token wander | Steps keep growing, plan never lands |
| [Recursive Loop](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/recursive-loop.md) | Breaks self reference loops | Chain circles back to the same step |
| [Hallucination Re entry](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/hallucination-reentry.md) | Prevents re asserting wrong claims | Model repeats a false claim after correction |
| [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/logic-collapse.md) | Rebuilds structure and legal jumps | Jumps without citing the step that caused it |
| [Symbolic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/symbolic-collapse.md) | Guards abstraction changes | Frame jump breaks meaning, invariants vanish |
| [Proof Dead Ends](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/proof-dead-ends.md) | Adds pivots and escape hatches | Chain stalls at an unprovable step |
| [Anchoring and Bridge Proofs](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md) | Builds safe bridges across frames | Need to cross domains without losing semantics |
| [Context Stitching and Window Joins](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/context-stitching-and-window-joins.md) | Stabilizes long windows and joins | Window roll drops the anchor or flips the claim |
| [Chain of Thought Variance Clamp](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md) | Makes reruns agree | Reruns disagree because thoughts wander |
| [Redundant Evidence Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/redundant-evidence-collapse.md) | Balances majority and minority facts | Too many similar snippets drown the truth |

---

## When to use this folder

- Multi step answers change when you rerun the same prompt  
- Chains go in circles or re assert a claim after correction  
- Logic jumps without citing the source that drove the jump  
- Long chats lose earlier anchors when the window rolls  
- Plans grow without bound and never converge

---

## Acceptance targets

- ΔS(question, selected_evidence) ≤ 0.45 on all runs  
- Coverage of the target section ≥ 0.70 with cite then explain  
- λ_observe convergent across three paraphrases and two seeds  
- E_resonance flat across long windows and at window joins  
- Deterministic step count for plan stages after clamps

---

## Fast triage by symptom

| Symptom | Open this |
|---|---|
| Steps keep growing, answer never lands | [Entropy Overload](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/entropy-overload.md) |
| Chain circles back to earlier step | [Recursive Loop](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/recursive-loop.md) |
| Model re asserts the wrong claim after you fix it | [Hallucination Re entry](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/hallucination-reentry.md) |
| Reasoning jumps without structure, loses invariants | [Logic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/logic-collapse.md) |
| Abstract move breaks semantics across frames | [Symbolic Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/symbolic-collapse.md) |
| Proof chain stalls at an unprovable step | [Proof Dead Ends](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/proof-dead-ends.md) |
| Window roll drops the anchor or flips the claim | [Context Stitching and Window Joins](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/context-stitching-and-window-joins.md) |
| Reruns disagree because thoughts wander | [Chain of Thought Variance Clamp](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md) |
| Too many similar snippets overpower minority facts | [Redundant Evidence Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/redundant-evidence-collapse.md) |
| Need a stable bridge between two frames | [Anchoring and Bridge Proofs](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md) |

---

## Fix in 60 seconds

1) **Measure ΔS and observe λ**  
   Probe ΔS(question, selected_evidence). Sample λ across two seeds and three paraphrases.  
   If ΔS ≥ 0.60 or λ flips, you have structural drift.

2) **Apply the right clamp**  
   - Wandering thoughts → variance clamp  
     Open [Chain of Thought Variance Clamp](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md)  
   - Lost anchor at joins → micro bridges  
     Open [Context Stitching and Window Joins](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/context-stitching-and-window-joins.md)  
   - Abstract jumps → bridge proofs  
     Open [Anchoring and Bridge Proofs](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md)

3) **Contract the payload and cite first**  
   Enforce snippet schema and cite then explain.  
   Open [Retrieval Traceability](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md) and [Data Contracts](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

4) **Verify**  
   Coverage ≥ 0.70, ΔS ≤ 0.45, λ convergent on two seeds.  
   If flat high ΔS remains, fix retrieval first with the playbook.  
   Open [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

---

## Copy paste diagnostic prompt

```txt
Context: TXT OS and WFGY pages are loaded.

Task:
- For question Q, log ΔS(Q, selected_evidence) on 3 paraphrases and 2 seeds.
- Report λ states across steps, and the first point where drift starts.
- Recommend the smallest page from this folder that will clamp variance
  and recover anchors. Name the page and the exact subsection.
- Return a reproducible check that proves ΔS ≤ 0.45 and coverage ≥ 0.70.

Return JSON only:
{ "ΔS": 0.xx, "λ": "<>|→|←|×", "failing_step": "...",
  "page": "anchoring-and-bridge-proofs", "subsection": "...",
  "verify": "run X, expect Y" }
````

---

## Cross links you will likely need

* Visual map and recovery
  [RAG Architecture & Recovery](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md)

* End to end retrieval knobs
  [Retrieval Playbook](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-playbook.md)

* Long context stability
  [Context Drift](https://github.com/onestardao/WFGY/blob/main/ProblemMap/context-drift.md) ·
  [Entropy Collapse](https://github.com/onestardao/WFGY/blob/main/ProblemMap/entropy-collapse.md)

* Reranking and ordering
  [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md)

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1) Download  2) Upload to your LLM  3) Ask “Answer using WFGY + <your question>” |
| **TXT OS (plain text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt)                                                                     | 1) Download  2) Paste into any LLM chat  3) Type “hello world”                   |

---

### 🧭 Explore More

| Module                | Description                                             | Link                                                                                               |
| --------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| WFGY Core             | Full symbolic reasoning architecture and math stack     | [View →](https://github.com/onestardao/WFGY/tree/main/core/README.md)                              |
| Problem Map 1.0       | Initial 16 mode diagnostic and symbolic fix framework   | [View →](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md)                        |
| Problem Map 2.0       | RAG focused failure tree, modular fixes, and pipelines  | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Semantic Clinic Index | Prompt injection, memory bugs, logic drift              | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           |
| Semantic Blueprint    | Layer based symbolic reasoning and semantic modulations | [View →](https://github.com/onestardao/WFGY/tree/main/SemanticBlueprint/README.md)                 |
| Benchmark vs GPT 5    | Stress test GPT 5 with full WFGY reasoning suite        | [View →](https://github.com/onestardao/WFGY/tree/main/benchmarks/benchmark-vs-gpt5/README.md)      |
| Starter Village       | New here, want a guided path                            | [Start →](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                   |

---

> Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)
> ⭐ [WFGY Engine 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md) is unlocked. Star the repo to help others discover it and unlock more on the [Unlock Board](https://github.com/onestardao/WFGY/blob/main/STAR_UNLOCKS.md).

<div align="center">

[![WFGY Main](https://img.shields.io/badge/WFGY-Main-red?style=flat-square)](https://github.com/onestardao/WFGY)
 
[![TXT OS](https://img.shields.io/badge/TXT%20OS-Reasoning%20OS-orange?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS)
 
[![Blah](https://img.shields.io/badge/Blah-Semantic%20Embed-yellow?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlahBlahBlah)
 
[![Blot](https://img.shields.io/badge/Blot-Persona%20Core-green?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlotBlotBlot)
 
[![Bloc](https://img.shields.io/badge/Bloc-Reasoning%20Compiler-blue?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlocBlocBloc)
 
[![Blur](https://img.shields.io/badge/Blur-Text2Image%20Engine-navy?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlurBlurBlur)
 
[![Blow](https://img.shields.io/badge/Blow-Game%20Logic-purple?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlowBlowBlow)

</div>
