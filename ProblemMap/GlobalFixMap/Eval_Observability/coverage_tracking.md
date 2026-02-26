# Eval Observability — Coverage Tracking

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Eval_Observability**.  
  > To reorient, go back here:  
  >
  > - [**Eval_Observability** — evaluation metrics and system observability](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

> **Evaluation disclaimer (coverage tracking)**  
> Coverage numbers here measure how much of a designed space you have touched under chosen tests.  
> High coverage does not guarantee absence of bugs or failures outside those tests.

---

A focused module to monitor **retrieval coverage** during eval and live runs.  
Coverage answers the key question: *“Did we retrieve enough of the right section to support the answer?”*

---

## Why coverage tracking matters

- **False negatives**: The right fact exists, but snippets cover too little of the section.  
- **Over-fragmentation**: Documents chunked too aggressively result in coverage <0.50 despite correct snippets.  
- **Hallucinations**: When coverage is low, LLMs often fill gaps with fabrications.  
- **Eval blind spots**: Benchmarks without coverage probes miss systematic recall failures.

---

## Core definition

Coverage is defined as:

```text
coverage = retrieved_tokens_in_target_section / total_tokens_in_target_section
````

* **Target section** = gold label or expected answer span.
* **Threshold** = minimum 0.70 in most RAG tasks.
* **Tolerance** = allow 5–10% batch queries below threshold before raising alert.

---

## Probe design

1. **Annotate gold sets**
   For each eval question, mark the expected source section IDs and token spans.

2. **Measure per-query coverage**
   Count how many tokens from expected span were retrieved.
   Normalize by total tokens in span.

3. **Batch aggregation**
   Track percentage of queries below threshold.
   Report average coverage ± variance.

4. **Drift detection**
   Compare against historical baseline (previous model or retriever version).
   If drop >0.05, escalate to retriever/infrastructure team.

---

## Alert thresholds

| Metric             | Warning    | Critical   |
| ------------------ | ---------- | ---------- |
| Per-query coverage | <0.70      | <0.60      |
| Batch pass rate    | <0.90      | <0.80      |
| Drift vs baseline  | drop >0.05 | drop >0.10 |

---

## Example probe code (pseudo)

```python
def track_coverage(retrieved, target_span):
    overlap = count_tokens(retrieved, target_span)
    coverage = overlap / len(target_span)
    return coverage

for q in eval_batch:
    cov = track_coverage(q.retrieved_tokens, q.gold_span)
    if cov < 0.70:
        alerts.append({"qid": q.id, "coverage": cov})
```

---

## Common pitfalls

* **Ignoring multi-section answers** → coverage must sum across all required sections.
* **Only measuring top-1 snippet** → always include top-k, otherwise underestimation occurs.
* **Static thresholds** → thresholds should adapt to doc size and retrieval depth.
* **No historical baseline** → without drift tracking, regressions pass unnoticed.

---

## Reporting dashboards

* **Histograms** of per-query coverage distribution.
* **Trend lines** for batch averages across eval sets.
* **Drift deltas** vs baseline runs.
* **Heatmaps** showing coverage by document or domain.

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + \<your question>”   |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt)                                                                     | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type “hello world” — OS boots instantly |

---

### 🧭 Explore More

| Module                   | Description                                                                  | Link                                                                                               |
| ------------------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| WFGY Core                | WFGY 2.0 engine is live: full symbolic reasoning architecture and math stack | [View →](https://github.com/onestardao/WFGY/tree/main/core/README.md)                              |
| Problem Map 1.0          | Initial 16-mode diagnostic and symbolic fix framework                        | [View →](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md)                        |
| Problem Map 2.0          | RAG-focused failure tree, modular fixes, and pipelines                       | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Semantic Clinic Index    | Expanded failure catalog: prompt injection, memory bugs, logic drift         | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           |
| Semantic Blueprint       | Layer-based symbolic reasoning & semantic modulations                        | [View →](https://github.com/onestardao/WFGY/tree/main/SemanticBlueprint/README.md)                 |
| Benchmark vs GPT-5       | Stress test GPT-5 with full WFGY reasoning suite                             | [View →](https://github.com/onestardao/WFGY/tree/main/benchmarks/benchmark-vs-gpt5/README.md)      |
| 🧙‍♂️ Starter Village 🏡 | New here? Lost in symbols? Click here and let the wizard guide you through   | [Start →](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                   |

---

> 👑 **Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)** —
> Engineers, hackers, and open source builders who supported WFGY from day one.

> <img src="https://img.shields.io/github/stars/onestardao/WFGY?style=social" alt="GitHub stars"> ⭐ [WFGY Engine 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md) is already unlocked. ⭐ Star the repo to help others discover it and unlock more on the [Unlock Board](https://github.com/onestardao/WFGY/blob/main/STAR_UNLOCKS.md).

<div align="center">

[![WFGY Main](https://img.shields.io/badge/WFGY-Main-red?style=flat-square)](https://github.com/onestardao/WFGY)
 
[![TXT OS](https://img.shields.io/badge/TXT%20OS-Reasoning%20OS-orange?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS)
 
[![Blah](https://img.shields.io/badge/Blah-Semantic%20Embed-yellow?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlahBlahBlah)
 
[![Blot](https://img.shields.io/badge/Blot-Persona%20Core-green?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlotBlotBlot)
 
[![Bloc](https://img.shields.io/badge/Bloc-Reasoning%20Compiler-blue?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlocBlocBloc)
 
[![Blur](https://img.shields.io/badge/Blur-Text2Image%20Engine-navy?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlurBlurBlur)
 
[![Blow](https://img.shields.io/badge/Blow-Game%20Logic-purple?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlowBlowBlow)
 

</div>
