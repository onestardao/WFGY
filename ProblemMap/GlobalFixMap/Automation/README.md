<!--
Search Anchor:
automation platform bugs
workflow automation failures
zapier zap not working
zapier duplicate triggers
zapier runs twice
zapier retry storm
zapier webhook timeout
n8n workflow stuck
n8n execution retry loop
n8n idempotency dedupe
make integromat scenario duplicated
make scenario retries
power automate flow failed
power automate runs twice
power automate trigger duplicates
retool workflow cron drift
retool job retries
ifttt applet not firing
pipedream webhook handler timeout
github actions workflow stuck
github actions rerun duplicates
airflow dag stuck
airflow scheduler time drift
airflow retry overload
airtable automation runs twice
asana rules duplicated
crm automation duplicate leads
gohighlevel ghl workflow duplication

Failure classes / Fix intent:
at least once delivery
exactly once semantics
idempotency key
dedupe key
retries with backoff and jitter
rate limit storm
webhook acknowledged before persist
store then process pattern
cron timezone drift
utc scheduling
time drift and clock skew
bootstrap ordering
cold start ordering
deployment deadlock
predeploy collapse
traceability breaks
citation mismatch
data contract missing offsets tokens
embedding semantic drift
high similarity wrong meaning
vector index not ready
VECTOR_READY INDEX_HASH

Routing to vendor pages:
Zapier -> Automation/zapier.md
n8n -> Automation/n8n.md
Make Integromat -> Automation/make.md
Retool -> Automation/retool.md
IFTTT -> Automation/ifttt.md
Pipedream -> Automation/pipedream.md
Power Automate -> Automation/power-automate.md
GitHub Actions -> Automation/github-actions.md
Airflow -> Automation/airflow.md
Airtable Automations -> Automation/airtable.md
Asana Rules -> Automation/asana.md
GoHighLevel GHL -> Automation/ghl.md
Parabola -> Automation/parabola.md
LangChain automation -> Automation/langchain.md
LlamaIndex automation -> Automation/llamaindex.md
-->


# Automation Platforms — Global Fix Map

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

Stabilize automations across Zapier, n8n, Make, Retool, Power Automate, and more.  
Most “platform bugs” are not bugs at all — they are ordering, retries, dedupe, or time drift. This hub routes you to exact structural fixes with measurable acceptance targets.

---

## Orientation: pick your tool

| Platform | What it is | Typical use | Link |
|---|---|---|---|
| Zapier | Mainstream no-code automation | Broad connectors, fast start | [zapier.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/zapier.md) |
| n8n | Open-source workflow engine | Self-hosted, extensible | [n8n.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/n8n.md) |
| Make (Integromat) | Visual workflow builder | SMB and RAG pipelines | [make.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/make.md) |
| Retool | Internal-tool builder + workflows | Backoffice jobs, cron | [retool.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/retool.md) |
| IFTTT | Consumer-grade triggers | Personal automations | [ifttt.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/ifttt.md) |
| Pipedream | Event platform + code steps | Webhooks, SaaS APIs | [pipedream.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/pipedream.md) |
| Power Automate | Microsoft ecosystem automation | O365, SharePoint, Dynamics | [power-automate.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/power-automate.md) |
| GitHub Actions | CI/CD + repo event runner | Build, test, deploy | [github-actions.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/github-actions.md) |
| Airflow | Code-first workflow scheduler | Data/ETL DAGs | [airflow.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/airflow.md) |
| Airtable Automations | Table-driven automations | CRUD triggers | [airtable.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/airtable.md) |
| Asana Rules | Project management rules | PM events to actions | [asana.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/asana.md) |
| GoHighLevel (GHL) | CRM automation platform | Marketing + sales flows | [ghl.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/ghl.md) |
| Parabola | Dataflow-based automation | Transform + schedule | [parabola.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/parabola.md) |
| LangChain (automation mode) | Agent orchestration | LLM-based workflows | [langchain.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/langchain.md) |
| LlamaIndex (automation mode) | Knowledge orchestration | RAG pipelines | [llamaindex.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/Automation/llamaindex.md) |

---

## Common failure classes

- **Bootstrap race conditions**  
  Trigger fires before vector/index is ready.  
  → [bootstrap-ordering.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/bootstrap-ordering.md)

- **Deployment deadlocks**  
  Infinite waits between worker, retriever, or webhook callbacks.  
  → [deployment-deadlock.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/deployment-deadlock.md)

- **Pre-deploy collapse**  
  Wrong version triggered on first call after shipping.  
  → [predeploy-collapse.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/predeploy-collapse.md)

- **Embedding vs semantic drift**  
  High similarity but wrong meaning.  
  → [embedding-vs-semantic.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/embedding-vs-semantic.md)

- **Traceability breaks**  
  Citations do not match the source.  
  → [retrieval-traceability.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/retrieval-traceability.md), [data-contracts.md](https://github.com/onestardao/WFGY/blob/main/ProblemMap/data-contracts.md)

---

## Minimal contract for any workflow

1. **Check readiness**  
   Verify `VECTOR_READY` and `INDEX_HASH` before RAG/LLM calls.  
2. **Idempotency**  
   Always compute a dedupe key and block duplicates.  
3. **Boundary contract**  
   Require `{snippet_id, section_id, source_url, offsets, tokens}`.  
4. **Observability**  
   Log ΔS and λ across steps, alert if ΔS ≥ 0.60.

---

## FAQ for newcomers

**Why does my Zap/Flow run twice?**  
Because triggers are at-least-once. Add idempotency keys to dedupe.

**Why did my webhook return 200 but no data was processed?**  
You acknowledged before persisting. Always store → then process.

**Why do my cron jobs drift?**  
Local timezone drift. Always store schedules in UTC.

**Why do retries overload my API?**  
You used immediate retries. Add exponential backoff with jitter.

**Why does everything work in dev but break in prod?**  
Because of boot order. Index not warmed, wrong analyzer, or cache empty.

---

### 🔗 Quick-Start Downloads

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1) Download · 2) Upload to LLM · 3) Ask “Use WFGY to fix my automation bug” |
| **TXT OS** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1) Download · 2) Paste into LLM · 3) Type “hello world” |

---

### 🧭 Explore More

| Module                | Description                                              | Link     |
|-----------------------|----------------------------------------------------------|----------|
| WFGY Core             | WFGY 2.0 engine is live: full symbolic reasoning architecture and math stack | [View →](https://github.com/onestardao/WFGY/tree/main/core/README.md) |
| Problem Map 1.0       | Initial 16-mode diagnostic and symbolic fix framework    | [View →](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md) |
| Problem Map 2.0       | RAG-focused failure tree, modular fixes, and pipelines   | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Semantic Clinic Index | Expanded failure catalog: prompt injection, memory bugs, logic drift | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md) |
| Semantic Blueprint    | Layer-based symbolic reasoning & semantic modulations   | [View →](https://github.com/onestardao/WFGY/tree/main/SemanticBlueprint/README.md) |
| Benchmark vs GPT-5    | Stress test GPT-5 with full WFGY reasoning suite         | [View →](https://github.com/onestardao/WFGY/tree/main/benchmarks/benchmark-vs-gpt5/README.md) |
| 🧙‍♂️ Starter Village 🏡 | New here? Lost in symbols? Click here and let the wizard guide you through | [Start →](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md) |

---

> 👑 **Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)** —  
> <img src="https://img.shields.io/github/stars/onestardao/WFGY?style=social" alt="GitHub stars"> ⭐ [WFGY Engine 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md) is already unlocked. ⭐ Star the repo to help others discover it and unlock more on the [Unlock Board](https://github.com/onestardao/WFGY/blob/main/STAR_UNLOCKS.md).

<div align="center">

[![WFGY Main](https://img.shields.io/badge/WFGY-Main-red?style=flat-square)](https://github.com/onestardao/WFGY)
&nbsp;
[![TXT OS](https://img.shields.io/badge/TXT%20OS-Reasoning%20OS-orange?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS)
&nbsp;
[![Blah](https://img.shields.io/badge/Blah-Semantic%20Embed-yellow?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlahBlahBlah)
&nbsp;
[![Blot](https://img.shields.io/badge/Blot-Persona%20Core-green?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlotBlotBlot)
&nbsp;
[![Bloc](https://img.shields.io/badge/Bloc-Reasoning%20Compiler-blue?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlocBlocBloc)
&nbsp;
[![Blur](https://img.shields.io/badge/Blur-Text2Image%20Engine-navy?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlurBlurBlur)
&nbsp;
[![Blow](https://img.shields.io/badge/Blow-Game%20Logic-purple?style=flat-square)](https://github.com/onestardao/WFGY/tree/main/OS/BlowBlowBlow)
&nbsp;
</div>

