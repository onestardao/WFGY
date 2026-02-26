# Eval: Latency vs Accuracy Trade-off

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **Eval**.  
  > To reorient, go back here:  
  >
  > - [**Eval** — model evaluation and benchmarking](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>

> **Evaluation disclaimer (latency vs accuracy)**  
> The trade off curves and numbers here depend on your stack, load and datasets.  
> Treat them as shapes to look for, not fixed targets that prove one model or setting is always better.

---

This page defines how to measure, report, and optimize the trade-off between model latency and retrieval/answer accuracy. It is not enough to chase precision; stable systems must also meet latency SLOs while holding ΔS and λ within guardrails.

## Open these first

* Core eval protocols: [Eval Benchmarking](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_benchmarking.md)
* Precision/recall metrics: [Eval RAG Precision/Recall](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_rag_precision_recall.md)
* Observability instruments: [deltaS\_thresholds.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/deltaS_thresholds.md), [lambda\_observe.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/lambda_observe.md)
* Drift and variance: [variance\_and\_drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/variance_and_drift.md)

---

## Acceptance targets

* **Latency**:

  * Median ≤ 1.2× baseline
  * P90 ≤ 1.5× baseline

* **Accuracy**:

  * Precision ≥ 0.80
  * Recall ≥ 0.70
  * ΔS(question, cited) ≤ 0.45 for ≥ 80 percent of runs
  * λ convergent across paraphrases

* **Cost stability**:

  * Tokens or API cost per correct answer ≤ 1.3× baseline

If accuracy improves but latency inflates beyond thresholds, classify as *not production-ready*. Only ship when both dimensions pass.

---

## Measurement protocol

1. **Dual track runs**

   * Run with and without extra retrieval steps (rerank, multi-hop, HyDE, etc).
   * Record latency per stage (retrieve, rerank, reason).

2. **Buckets**

   * Short queries: <50 tokens
   * Medium queries: 50–200 tokens
   * Long queries: >200 tokens
     Latency vs accuracy must be reported per bucket.

3. **Seeds and paraphrases**

   * Use 2 random seeds, 3 paraphrases each.
   * Average and variance required for both latency and accuracy metrics.

4. **Normalization**

   * Report cost per correct answer, not raw tokens.
   * Normalize across providers for fair comparison.

---

## Reporting schema

Append to the JSONL logs from [Eval Benchmarking](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval/eval_benchmarking.md):

```json
{
  "suite": "v1_latency",
  "arm": "with_rerank",
  "provider": "openai",
  "model": "gpt-4o-mini-2025-07",
  "bucket": "medium",
  "precision": 0.82,
  "recall": 0.71,
  "ΔS_avg": 0.39,
  "λ_flip_rate": 0.02,
  "latency_ms": { "retrieve": 120, "rerank": 85, "reason": 910 },
  "latency_total_ms": 1115,
  "latency_vs_baseline": 1.35,
  "tokens": { "in": 1980, "out": 510 },
  "cost_per_correct": 1.25,
  "notes": "acceptable trade-off"
}
```

---

## Diagnostic questions

When latency grows faster than accuracy:

* Is reranking adding value or just delay? → check ΔS histograms pre/post rerank.
* Are paraphrases redundant? → drop to 2 if λ stability holds.
* Is retrieval k too large? → compare 5, 10, 20.
* Are you re-embedding too often? → reuse cached vectors.
* Is model size the bottleneck? → test smaller model + WFGY vs large model baseline.

---

## Escalation and fixes

* **Latency regressions without accuracy gain** → cut rerank or hybrid steps. See [Rerankers](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rerankers.md).
* **High ΔS despite more steps** → rebuild index and re-chunk. See [Embedding ≠ Semantic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md).
* **Unstable λ across seeds** → clamp variance with BBAM, see [variance\_and\_drift.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Eval_Observability/variance_and_drift.md).

---

## Minimal 60-second run

1. Pick 5 medium-length questions.
2. Run baseline and WFGY rerank arm.
3. Record latency\_total\_ms and accuracy metrics.
4. Accept only if ΔS ≤ 0.45 and latency inflation ≤ 1.5× baseline.

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
