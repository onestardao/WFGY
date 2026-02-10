<!--
Search Anchor:
eval observability global fix map
rag eval observability signals
delta s lambda e_resonance monitoring
rag evaluation drift detection
variance and drift between seeds
regression gate for llm pipelines
alerting and probes for rag eval
coverage tracking vs real coverage
lambda observe thresholds and flips
eval playbook for stable metrics
metrics and logging for rag systems
evaluation contract seeds paraphrases
eval_contract yaml deltaS coverage lambda variance drift

When to use this folder:
metrics look unstable between runs
coverage looks high but answers still drift
delta s changes across paraphrases or seeds
lambda flips divergent after small edits
benchmarks regress without any code change
long run eval shows gradual decline in quality
alerts missing when metrics cross thresholds
local eval passes but ci fails inconsistently
variance across seeds is higher than expected
no clear target for delta s thresholds
no agreement on acceptable coverage levels
no guardrail on drift across eval windows

Key metrics and targets:
delta s question retrieved <= 0.45
coverage to target section >= 0.70
lambda observe convergent across 3 paraphrases and 2 seeds
variance ratio across seeds <= 0.15
no downward drift beyond 3 eval windows
e_resonance flat or within tolerance on long evals
alerts configured for delta s >= 0.60
alerts configured when lambda diverges or drift slope > 0.02

Core pages in this folder:
ProblemMap/GlobalFixMap/EvalObservability/regression_gate.md
ProblemMap/GlobalFixMap/EvalObservability/alerting_and_probes.md
ProblemMap/GlobalFixMap/EvalObservability/coverage_tracking.md
ProblemMap/GlobalFixMap/EvalObservability/deltaS_thresholds.md
ProblemMap/GlobalFixMap/EvalObservability/lambda_observe.md
ProblemMap/GlobalFixMap/EvalObservability/variance_and_drift.md
ProblemMap/GlobalFixMap/EvalObservability/eval_playbook.md
ProblemMap/GlobalFixMap/EvalObservability/metrics_and_logging.md

Related structural fixes:
ProblemMap/GlobalFixMap/EvaluationGuardrails/README.md
ProblemMap/retrieval-traceability.md
ProblemMap/data-contracts.md
ProblemMap/rag-architecture-and-recovery.md
ProblemMap/retrieval-playbook.md
ProblemMap/embedding-vs-semantic.md
ProblemMap/context-drift.md
ProblemMap/entropy-collapse.md
ProblemMap/rerankers.md
ProblemMap/hallucination.md

Evaluation scenarios:
benchmarks regress with no code change
metrics fluctuate but there are no alerts
coverage high on paper but not semantic
delta s thresholds chosen without evidence
lambda flips on harmless prompt edits
variance high between seeds or runs
no eval_contract yaml or versioned config
no trace of which eval suite was used
cannot replay a failing eval case from logs
no drift window or history across runs

Signals to check:
delta s per item across windows and seeds
coverage against gold snippet or section
lambda observe state across paraphrases
variance ratio across seeds and models
drift slope across eval windows
e_resonance across long context runs
alert counts vs threshold crossings
missing or incomplete metrics in logs
correlation between latency changes and quality shifts
-->


# Eval Observability — Global Fix Map

<details>
  <summary><strong>🏥 Quick Return to Emergency Room</strong></summary>

<br>

  > You are in a specialist desk.  
  > For full triage and doctors on duty, return here:  
  > 
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
  > 
  > Think of this page as a sub-room.  
  > If you want full consultation and prescriptions, go back to the Emergency Room lobby.
</details>

This folder provides **guardrails for evaluation and observability** in RAG and agent pipelines.  
It shows how to catch silent drift, regressions, and unstable metrics before they break your system.

---

## What this folder is
- A starter kit to make evals predictable and repeatable.
- Guardrails for metrics, variance, and drift detection.
- Copy-paste probes and configs you can add to your pipeline.
- Acceptance targets you can actually measure and enforce.

---

## When to use
- Metrics look **unstable** between runs.  
- Coverage seems high but answers still drift.  
- ΔS changes across paraphrases or seeds.  
- λ flips divergent after harmless edits.  
- Benchmarks regress without any code change.  
- Long-run evals show a slow decline.

---

## Acceptance targets
- **ΔS(question, retrieved) ≤ 0.45**  
- **Coverage ≥ 0.70** to target section  
- **λ remains convergent** across 3 paraphrases and 2 seeds  
- **Variance ratio ≤ 0.15** across seeds  
- **No downward drift** beyond 3 eval windows  
- **E_resonance stays flat** on long evals  

---

<!--
Anchor Menu:
open: eval observability readme ProblemMap/GlobalFixMap/EvalObservability/README.md
open: regression gate page ProblemMap/GlobalFixMap/EvalObservability/regression_gate.md
open: alerting and probes page ProblemMap/GlobalFixMap/EvalObservability/alerting_and_probes.md
open: coverage tracking page ProblemMap/GlobalFixMap/EvalObservability/coverage_tracking.md
open: delta s thresholds page ProblemMap/GlobalFixMap/EvalObservability/deltaS_thresholds.md
open: lambda observe page ProblemMap/GlobalFixMap/EvalObservability/lambda_observe.md
open: variance and drift page ProblemMap/GlobalFixMap/EvalObservability/variance_and_drift.md
open: eval playbook page ProblemMap/GlobalFixMap/EvalObservability/eval_playbook.md
open: metrics and logging page ProblemMap/GlobalFixMap/EvalObservability/metrics_and_logging.md

jump: evaluation and guardrails readme ProblemMap/GlobalFixMap/EvaluationGuardrails/README.md
jump: rag precision recall eval page ProblemMap/GlobalFixMap/EvaluationGuardrails/eval_rag_precision_recall.md
jump: latency vs accuracy eval page ProblemMap/GlobalFixMap/EvaluationGuardrails/eval_latency_vs_accuracy.md
jump: cross agent consistency eval page ProblemMap/GlobalFixMap/EvaluationGuardrails/eval_cross_agent_consistency.md
jump: semantic stability eval page ProblemMap/GlobalFixMap/EvaluationGuardrails/eval_semantic_stability.md

jump: retrieval traceability schema ProblemMap/retrieval-traceability.md
jump: data contracts snippet schema ProblemMap/data-contracts.md
jump: rag architecture and recovery ProblemMap/rag-architecture-and-recovery.md
jump: retrieval playbook ProblemMap/retrieval-playbook.md
jump: embedding vs semantic mismatch page ProblemMap/embedding-vs-semantic.md
jump: context drift page ProblemMap/context-drift.md
jump: entropy collapse page ProblemMap/entropy-collapse.md
jump: rerankers page ProblemMap/rerankers.md
jump: hallucination page ProblemMap/hallucination.md
-->


## Quick routes — open these first

| Symptom | Open this page |
|---------|----------------|
| Benchmarks regress with no code change | [regression_gate.md](./regression_gate.md) |
| Metrics fluctuate or alerts missing | [alerting_and_probes.md](./alerting_and_probes.md) |
| Coverage looks high but not real | [coverage_tracking.md](./coverage_tracking.md) |
| ΔS thresholds unclear | [deltaS_thresholds.md](./deltaS_thresholds.md) |
| λ flips or diverges | [lambda_observe.md](./lambda_observe.md) |
| Variance high between seeds | [variance_and_drift.md](./variance_and_drift.md) |
| Need a full setup | [eval_playbook.md](./eval_playbook.md) |
| Logging + monitoring integration | [metrics_and_logging.md](./metrics_and_logging.md) |

---

## Copy-paste eval contract

```yaml
eval_contract:
  seeds: 3
  paraphrases: 3
  targets:
    deltaS: <=0.45
    coverage: >=0.70
    lambda: convergent
    variance: <=0.15
    drift: <=0.02
alerts:
  - deltaS >=0.60
  - lambda divergent
  - drift slope >0.02
````

---

## FAQ

**Q: What if my metrics vary a lot each run?**
A: Check [variance\_and\_drift.md](./variance_and_drift.md). Add more seeds and enforce variance ≤0.15.

**Q: My eval passes locally but fails in CI — why?**
A: See [metrics\_and\_logging.md](./metrics_and_logging.md). Local runs often miss logging detail. CI must enforce the same eval contract.

**Q: What if coverage is high but the answer is still wrong?**
A: Open [coverage\_tracking.md](./coverage_tracking.md). You might be measuring snippet recall, not semantic coverage. Switch to ΔS-based coverage.

**Q: ΔS is always drifting, even on simple questions.**
A: Look at [deltaS\_thresholds.md](./deltaS_thresholds.md). Adjust thresholds and clamp variance with λ probes.

**Q: How do I stop regressions before release?**
A: Use [regression\_gate.md](./regression_gate.md). It defines pass/fail rules so bad models never ship.

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
