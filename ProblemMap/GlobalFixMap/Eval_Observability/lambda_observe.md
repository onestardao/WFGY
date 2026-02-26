# Eval Observability — λ_observe

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

> **Evaluation disclaimer (λ_observe)**  
> λ_observe is a heuristic stability signal defined inside the WFGY framework.  
> It helps you notice drift and volatility but is not a formal guarantee of long term robustness.

---

A core probe for evaluating **semantic convergence** across multiple seeds, paraphrases, and retrieval variations.  
While ΔS measures semantic distance, **λ_observe** captures **stability vs divergence of reasoning paths**.

---

## Why λ_observe matters

- **Detect fragile reasoning**: Even when ΔS looks safe, λ divergence indicates unstable chains.  
- **Identify paraphrase sensitivity**: If λ flips across harmless rewordings, the system is brittle.  
- **Audit retrieval randomness**: Different seeds producing opposite λ signals reveal weak schema.  
- **Ensure eval reproducibility**: Stable λ means tests repeat reliably under small perturbations.

---

## λ state encoding

| Symbol | Meaning | Example failure |
|--------|---------|-----------------|
| **→**  | Forward convergence, stable path | Same citations and reasoning across paraphrases |
| **←**  | Backward collapse, early abort | Tool call retries, empty citations |
| **<>** | Split state, partial divergence | One paraphrase cites correct snippet, others miss |
| **×**  | Total collapse | Random answers, no citation alignment |

---

## Acceptance targets

- **Convergence rate ≥ 0.80** across 3 paraphrases × 2 seeds.  
- **No × states** tolerated in gold-set eval.  
- **Split states (<>): ≤ 10%** of test cases acceptable.  
- **Forward (→)** must dominate stable runs.

---

## Evaluation workflow

1. **Run triple paraphrase probe**  
   Ask the same question three ways. Collect λ states.  
2. **Repeat with two seeds**  
   Track variance.  
3. **Roll-up stats**  
   Compute convergence ratio, collapse frequency, divergence rate.  
4. **Escalation**  
   If λ <0.80 or × >0%, run root-cause: schema audit, retriever split, prompt ordering.

---

## Example probe schema

```json
{
  "query_id": "Q42",
  "runs": [
    {"paraphrase": 1, "seed": 123, "λ": "→"},
    {"paraphrase": 2, "seed": 123, "λ": "→"},
    {"paraphrase": 3, "seed": 123, "λ": "<>"},
    {"paraphrase": 1, "seed": 456, "λ": "→"},
    {"paraphrase": 2, "seed": 456, "λ": "×"},
    {"paraphrase": 3, "seed": 456, "λ": "→"}
  ]
}
````

---

## Common pitfalls

* **Only measuring ΔS** → misses hidden divergence.
* **Seed-fixed eval** → looks stable but fragile in production.
* **Ignoring split states** → small divergence often grows into collapse.
* **No per-query logs** → averages hide catastrophic single failures.

---

## Reporting recommendations

* **λ distribution table**: % of →, ←, <>, ×.
* **Convergence trend**: chart over time by eval batch.
* **Drift alerts**: trigger if convergence <0.80 or × appears.
* **Correlation**: track ΔS vs λ to spot mixed failures.

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
