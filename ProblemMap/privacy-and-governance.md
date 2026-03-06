# 🔐 Privacy & Governance for RAG Systems — Practical Runbook

Build trustworthy AI: minimize data, control exposure, and prove compliance without killing velocity.

> **Quick Nav**  
> [Data Contracts](./data-contracts.md) ·
> [Ops](./ops/README.md) ·
> Patterns: [Memory Desync](./patterns/pattern_memory_desync.md) ·
> [SCU](./patterns/pattern_symbolic_constraint_unlock.md)

> *Not legal advice.* Use this as a technical baseline and align with your counsel.

---

## 0) Principles

1. **Minimize**: ingest only what you truly need; redact at source.  
2. **Fence**: per-source prompt fences; cite-then-explain.  
3. **Prove**: log every decision via data contracts; keep tight retention.  
4. **Control**: least-privilege access; encrypt at rest/in transit.

---

## 1) PII taxonomy & redaction

- Categories: identifiers (name, email, gov ID), contact, location, financial, health, biometric, free-text PII.  
- Redact at **ingest** with deterministic tags:

```json
{"text":"Contact Alice at alice@example.com","redactions":[{"span":[8,13],"type":"person"},{"span":[24,43],"type":"email"}]}
````

* Keep **reversible vault** only if business requires it; otherwise **irreversible**.

---

## 2) Storage & access control

* **Encryption**: TLS in transit; AES-GCM at rest.
* **Access**: service accounts per component; forbid shared tokens; rotate keys.
* **Retention**: default 30–90 days for logs; 7–30 days for raw prompts unless required longer.
* **Deletion**: implement DSR (data subject request) over `doc_id` or `user_id`.

---

## 3) Model provider governance

* Confirm **data usage** (training vs. inference only).
* Disable **logging** on hosted APIs if must not leave boundary.
* For self-hosted models, pin container images and track model checksum.

---

## 4) Prompt governance (SCU-safe)

* Lock schema: system → task → constraints → citations → answer.
* Forbid cross-source merges; require **line-level** citation IDs.
* Add guard prompts to avoid reproducing secrets or PII unless necessary and consented.

---

## 5) Audit & reproducibility

* Use **envelope** fields (`trace_id`, `mem_rev`, `mem_hash`) in every record.
* Keep **answer → prompt → citations → chunks** chain navigable.
* Export **metrics pack** per release (ΔS, λ rates, nDCG, recall).

---

## 6) Config template (YAML)

```yaml
privacy:
  redact_at_ingest: true
  redactors: [pii_email, pii_phone, pii_name]
  reversible_vault: false
  retention_days:
    prompts: 14
    logs: 60
    embeddings: 180
  access:
    roles:
      retriever: [read_chunks]
      reranker: [read_chunks]
      llm: [read_prompts]
      analyst: [read_metrics]
  secrets:
    provider: "aws-kms"   # or gcp-kms, vault
    rotation_days: 90
providers:
  openai:
    share_for_training: false
  claude:
    share_for_training: false
```

---

## 7) Risk scenarios → mitigations

| Scenario                    | Risk                     | Mitigation                                                           |
| --------------------------- | ------------------------ | -------------------------------------------------------------------- |
| User uploads PII-heavy PDFs | Accidental exposure      | Redact at ingest; block high-risk types; allow override with consent |
| Multi-tenant leakage        | Cross-account data bleed | Tenant IDs in chunk keys; per-tenant indices; access policies        |
| Citations reveal secrets    | SCU or over-inclusion    | Reduce context window; per-source fences; require justification      |
| Vendor logs prompts         | Data leaves boundary     | Use no-log endpoints; self-host; encrypt locally                     |

---

## Acceptance criteria

* ✅ PII redaction rate ≥ 95% on test corpus; **no residual PII** in prompts unless approved.
* ✅ Trace chain present for 100% of answers (citations included).
* ✅ Secrets rotated within policy; provider log-sharing disabled.
* ✅ Retention job passes dry-run audit monthly.

---


### 🔗 Quick-Start Downloads (60 sec)

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask “Answer using WFGY + \<your question>” |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type “hello world” — OS boots instantly |

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

