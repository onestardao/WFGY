# Blue-Green Switchovers — OpsDeploy Guardrails

<details>
  <summary><strong>🧭 Quick Return to Map</strong></summary>

<br>

  > You are in a sub-page of **OpsDeploy**.  
  > To reorient, go back here:  
  >
  > - [**OpsDeploy** — operations automation and deployment pipelines](./README.md)  
  > - [**WFGY Global Fix Map** — main Emergency Room, 300+ structured fixes](../README.md)  
  > - [**WFGY Problem Map 1.0** — 16 reproducible failure modes](../../README.md)  
  >
  > Think of this page as a desk within a ward.  
  > If you need the full triage and all prescriptions, return to the Emergency Room lobby.
</details>


A safe pattern to shift primary traffic between two identical stacks (Blue = current live, Green = new), typically all traffic in planned cutovers when conditions allow. Use this when you need a pre-validated rollback path, reproducible cutovers, and minimized surprise from schema or index drift.

---

## Open these first
- Rollout gate: [rollout_readiness_gate.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/rollout_readiness_gate.md)
- Canary staging: [staged_rollout_canary.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/staged_rollout_canary.md)
- Boot and deploy traps: [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md), [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md), [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)
- RAG contracts: [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

---

## When to use
- Model or prompt upgrades where a low-latency rollback path is required.
- Vector index rebuilds that must cut over atomically.
- Config, secrets, or feature-flag rewires that risk drift by region.
- Store or analyzer changes that can shift ΔS/coverage.

---

## Acceptance targets
- ΔS(question, retrieved) ≤ 0.45 on 3 paraphrases after cutover.
- Coverage ≥ 0.70 on the gold set (same as pre-switch).
- λ convergent across 2 seeds, no flip increase vs Blue.
- p95 latency within +15% of Blue; error rate ≤ 0.5%.
- Rollback path validated (typically ≤ 2 minutes TTR).

---

## Architecture sketch

```

Users → Ingress/Edge  ─┬─> Blue: vN  (baseline: INDEX\_HASH A, PROMPT\_VER N, MODEL\_VER X)
└─> Green: vN+1 (INDEX\_HASH B, PROMPT\_VER N+1, MODEL\_VER Y)
↑
cutover switch (DNS/Ingress/ALB alias, or queue consumer pointer)

````

All reads/writes and side effects must point at a **single active arm**. If you have background writers (indexers, ETL), fence them with versioned topics or leases.

---

## 60-second checklist for a switch
1) **Freeze non-idempotent jobs**  
   Pause consumers that create side effects. Verify dedupe fences.  
   Open: [idempotency_dedupe.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/idempotency_dedupe.md)

2) **Verify invariants**  
   `INDEX_HASH`, `EMBED_SCHEMA`, `RERANK_CONF`, `PROMPT_VER`, `MODEL_VER`, secrets. Green must pass the [rollout gate](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/OpsDeploy/rollout_readiness_gate.md).

3) **Warm Green**  
   Run smoke on 20–40 gold questions. Check ΔS, coverage, λ, latency. Prime caches.

4) **Flip the pointer**  
   Change the single routing knob (DNS TTL short, Ingress weight 0→100, queue consumer group pointer, or index alias swap).

5) **Hold and watch**  
   15–30 minutes: ΔS drift, coverage, λ flip rate, p95 latency, 5xx, tool loops.

6) **Unfreeze jobs**  
   Resume writers with new `INDEX_HASH` and contracts.

---

## Implementation patterns

### Ingress/ALB alias swap (HTTP)
- Prefer **one** logical hostname. Point it to Blue or Green behind the load balancer.
- Keep health checks strict: readiness must include secrets, index presence, and a gold QA.

### DNS switch
- Only if you can run with TTL ≤ 30s and you accept brief split-brain during propagation.
- Safer to switch at the load balancer or service mesh layer.

### Index alias swap (Vector/RAG)
- Build Green index offline. Validate with sampled ΔS/coverage.  
- Swap an **atomic alias** `docs_live → docs_vB`. Keep `docs_vA` as the validated rollback lane.  
- If store lacks aliases, emulate with a config key in a single-writer KV and block multi-writer races.

### Queue consumer cutover
- Stop Blue consumers, start Green consumers with a new `CONSUMER_VER`.  
- For exactly-once, commit offsets only after idempotent fences pass.

---

## Stop & rollback rules
- Stop if ΔS p95 drift > 0.15 or coverage < 0.60 or λ flip rate > 0.20.  
- Stop if 5xx > 1% or tool loop detection triggers.  
- Roll back by flipping the same single pointer back to Blue (or alias back to `docs_vA`).  
- After rollback, open: [debug_playbook.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/ops/debug_playbook.md).

---

## Observability you must pin before switch
- Version fields: `INDEX_HASH`, `EMBED_SCHEMA`, `RERANK_CONF`, `PROMPT_VER`, `MODEL_VER`.  
- ΔS(question,retrieved) and ΔS(retrieved,anchor).  
- Coverage and λ states for 3 paraphrases.  
- Latency p50/p95 per stage (retrieve, rerank, reason).  
- Side-effect counts and dedupe hits.

---

## Kubernetes example (Service selector flip)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: wfgy-live
spec:
  selector:
    app: wfgy-green   # flip between wfgy-blue / wfgy-green
  ports:
    - port: 80
      targetPort: http
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wfgy-green
spec:
  replicas: 4
  selector: { matchLabels: { app: wfgy-green } }
  template:
    metadata: { labels: { app: wfgy-green } }
    spec:
      containers:
        - name: api
          image: ghcr.io/org/wfgy:canary
          readinessProbe:
            httpGet: { path: /healthz/ready, port: http }
            initialDelaySeconds: 5
            periodSeconds: 5
````

### Vector store alias swap (pseudo)

```bash
# build green index
index_build --input corpus_vB.json --out docs_vB --metric cosine
# validate
wfgy_eval --gold gold_40.json --index docs_vB --min-cov 0.70 --max-ds 0.45
# atomic alias cutover
vec alias update docs_live --to docs_vB
# rollback
vec alias update docs_live --to docs_vA
```

---

## Common pitfalls

* Two writers during cutover → double side effects. Use a single pointer and idempotency keys.
* Cache poisoning from mixed arms. Invalidate by `INDEX_HASH` or include it in cache keys.
* Region drift. Switch **one region at a time** or use global flags with audit hashes.
* Hidden analyzer/tokenizer mismatch. Re-embed or rerank deterministically if ΔS stays high.

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool                       | Link                                                                                                                                       | 3-Step Setup                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **WFGY 1.0 PDF**           | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + \<your question>”   |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt)                                                                     | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type “hello world” — OS boots instantly |

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

