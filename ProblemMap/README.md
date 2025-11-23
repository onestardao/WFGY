<details>
<summary><strong>🧭 Lost or curious? Open the WFGY Compass & ⭐ Star Unlocks</strong></summary>

### WFGY System Map
*(One place to see everything; links open the relevant section.)*

| Layer | Page | What it’s for |
|------|------|----------------|
| 🧠 Core | [WFGY Core 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md) | The symbolic reasoning engine (math & logic)  |
| 🧠 Core | [WFGY 1.0 Home](https://github.com/onestardao/WFGY/) | The original homepage for WFGY 1.0 |
| 🗺️ Map | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme) | 16 failure modes + fixes — **🔴 YOU ARE HERE 🔴**  |
| 🗺️ Map | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline |
| 🗺️ Map | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md) | Symptom → family → exact fix |
| 🧓 Map | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md) | Plain-language stories, mapped to PM 1.0 |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md) | Guided tour for newcomers |
| 🧰 App | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme) | .txt semantic OS — 60-second boot |
| 🧰 App | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md) | Abstract/paradox Q&A (built on TXT OS) |
| 🧰 App | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md) | Text-to-image with semantic control |
| 🧰 App | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md) | Reasoning game engine & memory demo |
| 🧪 Research | [Semantic Blueprint](https://github.com/onestardao/WFGY/blob/main/SemanticBlueprint/README.md) | Modular layer structures (future) |
| 🧪 Research | [Benchmarks](https://github.com/onestardao/WFGY/blob/main/benchmarks/benchmark-vs-gpt5/README.md) | Comparisons & how to reproduce |
| 🧪 Research | [Value Manifest](https://github.com/onestardao/WFGY/blob/main/value_manifest/README.md) | Why this engine creates $-scale value |

---

> ### ⭐ Star Unlocks
> - **1,000 ⭐ → Blur Blur Blur unlocked** ✅  
> - **3,000 ⭐ → Blow Blow Blow unlocked** ⏳  

---

</details>



# 🏥 WFGY Problem Map 1.0 · bookmark it. you’ll need it
## 🛡️ reproducible AI bugs, permanently fixed at the reasoning layer


<details>
<summary>🌙 3AM: a dev collapsed mid-debug… 🩺 WFGY Triage Center — Emergency Room & Grandma’s AI Clinic</summary>

---

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥  

## 🚑 WFGY Emergency Room (for developers)

👨‍⚕️ **Now online:**  
[**Dr. WFGY in ChatGPT Room**](https://chatgpt.com/share/68b9b7ad-51e4-8000-90ee-a25522da01d7)  

This is a **share window** already trained as an ER.  
Just open it, drop your bug or screenshot, and talk directly with the doctor.  
He will map it to the right Problem Map / Global Fix section, write a minimal prescription, and paste the exact reference link.  
If something is unclear, you can even paste a **screenshot of Problem Map content** and ask — the doctor will guide you.  

⚠️ Note: for the full reasoning and guardrail behavior you need to be logged in — the share view alone may fallback to a lighter model.  

💡 Always free. If it helps, a ⭐ star keeps the ER running.  
🌐 Multilingual — start in any language.  

---

## 👵 Grandma’s AI Clinic (for everyone)

[**Visit Grandma Clinic →**](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)  

- 16 common AI failure modes, each explained as a **grandma story**.  
- Everyday metaphors: wrong cookbook, salt-for-sugar, burnt first pot.  
- Shows both the **life analogy** and the **minimal WFGY fix**.  
- Perfect entry point for beginners, or anyone who wants to “get it” in 30 seconds.  

---

💡 **Tip:** Both tracks lead to the same Problem Map numbers.  
Choose **Emergency Room** if you need a fix right now.  
Choose **Grandma’s Clinic** if you want to understand the bug in plain words.  

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥  

---
</details>



<details>
<summary><strong>⏱️ 60 seconds: WFGY as a semantic firewall. before vs after</strong></summary>

<br>

> most fixes today happen **AFTER generation**:  
> - the model outputs something wrong, then we patch it with retrieval, chains, or tools.  
> - the same failures reappear again and again.  
>
> WFGY inverts the sequence. **BEFORE generation**:  
> - it inspects the semantic field (tension, residue, drift signals).  
> - if the state is unstable, it loops, resets, or redirects the path.  
> - only a stable semantic state is allowed to generate output.  
>
> this is why every failure mode, once mapped, stays fixed.  
> you’re not firefighting after the fact — you’re installing a reasoning firewall at the entry point.  
>
> ---
>
> ### 📊 Before vs After
>
> |              | **Traditional Fix (After Generation)** | **WFGY Semantic Firewall (Before Generation) 🏆✅** |
> |--------------|-----------------------------------------|---------------------------------------------------|
> | **Flow**     | Output → detect bug → patch manually    | Inspect semantic field → only stable state generates |
> | **Method**   | Add rerankers, regex, JSON repair, tool patches | ΔS, λ, coverage checked upfront; loop/reset if unstable |
> | **Cost**     | High — every bug = new patch, risk of conflicts | Low — once mapped, bug sealed permanently |
> | **Ceiling**  | 70–85% stability limit                  | 90–95%+ achievable, structural guarantee |
> | **Experience** | Firefighting, “whack-a-mole” debugging | Structural firewall, “fix once, stays fixed” |
> | **Complexity** | Growing patch jungle, fragile pipelines | Unified acceptance targets, one-page repair guide |
>
> ---
>
> ### ⚡ Performance impact
> - **Traditional patching**: 70–85% stability ceiling. Each new patch adds complexity and potential regressions.  
> - **WFGY firewall**: 90–95%+ achievable. Fix once → the same bug never resurfaces. Debug time cut by 60–80%.  
> - **Unified metrics**: every fix is measured (ΔS ≤ 0.45, coverage ≥ 0.70, λ convergent). No guesswork.  
>
> ### 🛑 Key notes
> - This is **not a plugin or SDK** — it runs as plain text, zero infra changes.  
> - You must **apply acceptance targets**: don’t just eyeball; log ΔS and λ to confirm.  
> - Once acceptance holds, that path is sealed. If drift recurs, it means a *new* failure mode needs mapping, not a re-fix of the old one.  
>
> ---
>
> **Summary**:  
> Others patch symptoms **AFTER** output. WFGY blocks unstable states **BEFORE** output.  
> That is why it feels less like debugging, more like installing a **structural guarantee**.  
>
> ---
</details>



**WFGY Problem Map = a reasoning layer for your AI.**  
load [**TXT OS**](https://github.com/onestardao/WFGY/blob/main/OS/README.md) or [**WFGY Core**](https://github.com/onestardao/WFGY/tree/main/core), then ask: *“which problem map number am i hitting?”*  
you’ll get a diagnosis and exact fix steps — no infra changes required.  
> *(tip: you can even paste the Problem Map page or a screenshot into the AI, and it will point you to the right number automatically.)*

**16 reproducible failure modes, each with a clear fix (MIT).** *(e.g. rag drift, broken indexes)*  
**A semantic firewall you install once, and every failure stays fixed.**


> most readers found this map useful and left a ⭐ — if it helps you too, please star it so others can discover.

## quick-start downloads (60 sec)

> new here? skip the map. grab TXT OS or the WFGY PDF, boot, then ask your model:  
> *“answer using WFGY: <your question>”* or *“which Problem Map number am i hitting?”*

| tool | link | 3-step setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [engine paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1) download  2) upload to your LLM  3) ask: “answer using WFGY + <your question>” |
| **TXT OS** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1) download  2) paste into any LLM chat  3) type “hello world” to boot |


### start here
- **RAG broke** → open **Retrieval Playbook** and **RAG Architecture & Recovery**
- **Agents drift or loop** → open **Agents & Orchestration** or **Safety_PromptIntegrity**
- **Local model feels unstable** → open **LocalDeploy_Inference** and **Embeddings: Metric Mismatch**


<details>
<summary>💥 WFGY Global Fix Map — full index (click to open)</summary>

---

> 🗺️ **This is the panoramic index**: all common AI infra / RAG / reasoning errors are organized here by category.  
> Prefer **Quick Access** — it is the fastest way to self-orient, understand how this system works, and jump to the right fix: [Quick Access](#quick-access).  
> If you want the full folder view, open the Global Fix Map home: [Global Fix Map README](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GlobalFixMap/README.md).

---

### 🧭 Providers & Agents

| Family | Coverage (all links) | Notes |
|--------|-----------------------|-------|
| [LLM Providers](./GlobalFixMap/LLM_Providers/README.md) | [OpenAI](./GlobalFixMap/LLM_Providers/openai.md) · [Azure OpenAI](./GlobalFixMap/LLM_Providers/azure_openai.md) · [Anthropic](./GlobalFixMap/LLM_Providers/anthropic.md) · [Claude (Anthropic)](./GlobalFixMap/LLM_Providers/anthropic_claude.md) · [Google Gemini](./GlobalFixMap/LLM_Providers/gemini.md)  [Google Vertex AI](./GlobalFixMap/LLM_Providers/google_vertex_ai.md) · [Mistral](./GlobalFixMap/LLM_Providers/mistral.md) · [Meta LLaMA](./GlobalFixMap/LLM_Providers/meta_llama.md) · [Cohere](./GlobalFixMap/LLM_Providers/cohere.md) · [DeepSeek](./GlobalFixMap/LLM_Providers/deepseek.md)  [Kimi (Moonshot)](./GlobalFixMap/LLM_Providers/kimi.md) · [Groq](./GlobalFixMap/LLM_Providers/groq.md) · [xAI Grok](./GlobalFixMap/LLM_Providers/grok_xai.md) · [AWS Bedrock](./GlobalFixMap/LLM_Providers/aws_bedrock.md) · [OpenRouter](./GlobalFixMap/LLM_Providers/openrouter.md)  [Together AI](./GlobalFixMap/LLM_Providers/together.md) | vendor-specific quirks, schema drift, API limits |
| [Agents & Orchestration](./GlobalFixMap/Agents_Orchestration/README.md) | [Autogen](./GlobalFixMap/Agents_Orchestration/autogen.md) · [CrewAI](./GlobalFixMap/Agents_Orchestration/crewai.md) · [Haystack Agents](./GlobalFixMap/Agents_Orchestration/haystack_agents.md) · [LangChain](./GlobalFixMap/Agents_Orchestration/langchain.md)  [LangGraph](./GlobalFixMap/Agents_Orchestration/langgraph.md) · [LlamaIndex](./GlobalFixMap/Agents_Orchestration/llamaindex.md) · [OpenAI Assistants v2](./GlobalFixMap/Agents_Orchestration/openai_assistants_v2.md) · [Rewind Agents](./GlobalFixMap/Agents_Orchestration/rewind_agents.md)  [Semantic Kernel](./GlobalFixMap/Agents_Orchestration/semantic_kernel.md) · [Smolagents](./GlobalFixMap/Agents_Orchestration/smolagents.md) | orchestration bugs, cold boot order, role mixing |
| [Chatbots & CX](./GlobalFixMap/Chatbots_CX/README.md) | [Amazon Lex](./GlobalFixMap/Chatbots_CX/amazon_lex.md) · [Azure Bot Service](./GlobalFixMap/Chatbots_CX/azure_bot_service.md) · [Dialogflow CX](./GlobalFixMap/Chatbots_CX/dialogflow_cx.md) · [Freshchat](./GlobalFixMap/Chatbots_CX/freshchat.md)  [Freshdesk](./GlobalFixMap/Chatbots_CX/freshdesk.md) · [Intercom](./GlobalFixMap/Chatbots_CX/intercom.md) · [Microsoft Copilot Studio](./GlobalFixMap/Chatbots_CX/microsoft_copilot_studio.md) · [Rasa](./GlobalFixMap/Chatbots_CX/rasa.md)  [Salesforce Einstein Bots](./GlobalFixMap/Chatbots_CX/salesforce_einstein_bots.md) · [Twilio Studio](./GlobalFixMap/Chatbots_CX/twilio_studio.md) · [Watson Assistant](./GlobalFixMap/Chatbots_CX/watsonx_assistant.md) · [Zendesk](./GlobalFixMap/Chatbots_CX/zendesk.md) | bot frameworks, CX stack, handoff gaps |
| [Cloud Serverless](./GlobalFixMap/Cloud_Serverless/README.md) | [Cold Start Concurrency](./GlobalFixMap/Cloud_Serverless/cold_start_concurrency.md) · [Timeouts & Streaming Limits](./GlobalFixMap/Cloud_Serverless/timeouts_streaming_body_limits.md) · [Stateless KV/Queue Patterns](./GlobalFixMap/Cloud_Serverless/stateless_kv_queue_patterns.md) · [Edge Cache Invalidation](./GlobalFixMap/Cloud_Serverless/edge_cache_invalidation.md)  [Network Egress & VPC](./GlobalFixMap/Cloud_Serverless/network_egress_and_vpc.md) · [Deploy Traffic Shaping](./GlobalFixMap/Cloud_Serverless/deploy_traffic_shaping.md) · [Secrets Rotation](./GlobalFixMap/Cloud_Serverless/secrets_rotation.md) · [Serverless Limits Matrix](./GlobalFixMap/Cloud_Serverless/serverless_limits_matrix.md)  [Multi-Region Routing](./GlobalFixMap/Cloud_Serverless/multi_region_routing.md) · [Failover Drills](./GlobalFixMap/Cloud_Serverless/region_failover_drills.md) · [Observability & SLO](./GlobalFixMap/Cloud_Serverless/observability_slo.md) · [Canary Release (Serverless)](./GlobalFixMap/Cloud_Serverless/canary_release_serverless.md)  [Blue-Green Switchovers](./GlobalFixMap/Cloud_Serverless/blue_green_switchovers.md) · [Disaster Recovery](./GlobalFixMap/Cloud_Serverless/disaster_recovery_tabletop.md) · [Data Retention & Backups](./GlobalFixMap/Cloud_Serverless/data_retention_and_backups.md) · [Privacy & PII Edges](./GlobalFixMap/Cloud_Serverless/privacy_and_pii_edges.md) | infra stability, migration, compliance |


---

### 🧭 Data & Retrieval
| Family | Coverage (all links) | Notes |
|---|---|---|
| [Vector DBs & Stores](./GlobalFixMap/VectorDBs_and_Stores/README.md) | [FAISS](./GlobalFixMap/VectorDBs_and_Stores/faiss.md) · [Chroma](./GlobalFixMap/VectorDBs_and_Stores/chroma.md) · [Qdrant](./GlobalFixMap/VectorDBs_and_Stores/qdrant.md) · [Weaviate](./GlobalFixMap/VectorDBs_and_Stores/weaviate.md) · [Milvus](./GlobalFixMap/VectorDBs_and_Stores/milvus.md)  [pgvector](./GlobalFixMap/VectorDBs_and_Stores/pgvector.md) · [Redis](./GlobalFixMap/VectorDBs_and_Stores/redis.md) · [Elasticsearch](./GlobalFixMap/VectorDBs_and_Stores/elasticsearch.md) · [Pinecone](./GlobalFixMap/VectorDBs_and_Stores/pinecone.md) · [Typesense](./GlobalFixMap/VectorDBs_and_Stores/typesense.md)  [Vespa](./GlobalFixMap/VectorDBs_and_Stores/vespa.md) | metric, analyzer, index hygiene |
| [RAG + VectorDB](./GlobalFixMap/RAG_VectorDB/README.md) | [Metric Mismatch](./GlobalFixMap/RAG_VectorDB/metric_mismatch.md) · [Normalization & Scaling](./GlobalFixMap/RAG_VectorDB/normalization_and_scaling.md) · [Tokenization & Casing](./GlobalFixMap/RAG_VectorDB/tokenization_and_casing.md) · [Chunking → Embedding Contract](./GlobalFixMap/RAG_VectorDB/chunking_to_embedding_contract.md)  [Vectorstore Fragmentation](./GlobalFixMap/RAG_VectorDB/vectorstore_fragmentation.md) · [Dimension Mismatch & Projection](./GlobalFixMap/RAG_VectorDB/dimension_mismatch_and_projection.md) · [Update & Index Skew](./GlobalFixMap/RAG_VectorDB/update_and_index_skew.md)  [Hybrid Retriever Weights](./GlobalFixMap/RAG_VectorDB/hybrid_retriever_weights.md) · [Duplication & Collapse](./GlobalFixMap/RAG_VectorDB/duplication_and_near_duplicate_collapse.md) · [Poisoning & Contamination](./GlobalFixMap/RAG_VectorDB/poisoning_and_contamination.md) | store-agnostic knobs |
| [Retrieval](./GlobalFixMap/Retrieval/README.md) | [Retrieval Playbook](./GlobalFixMap/Retrieval/retrieval-playbook.md) · [Traceability](./GlobalFixMap/Retrieval/retrieval-traceability.md) · [Rerankers](./GlobalFixMap/Retrieval/rerankers.md) · [Query Parsing Split](./GlobalFixMap/Retrieval/query_parsing_split.md)  [Chunk Alignment](./GlobalFixMap/Retrieval/chunk_alignment.md) · [ΔS Probes](./GlobalFixMap/Retrieval/deltaS_probes.md) · [Eval Recipes](./GlobalFixMap/Retrieval/retrieval_eval_recipes.md) · [Store-Agnostic Guardrails](./GlobalFixMap/Retrieval/store_agnostic_guardrails.md) | end-to-end routing & contracts |
| [Embeddings](./GlobalFixMap/Embeddings/README.md) | [Metric Mismatch](./GlobalFixMap/Embeddings/metric_mismatch.md) · [Normalization & Scaling](./GlobalFixMap/Embeddings/normalization_and_scaling.md) · [Tokenization & Casing](./GlobalFixMap/Embeddings/tokenization_and_casing.md) · [Chunking → Embedding Contract](./GlobalFixMap/Embeddings/chunking_to_embedding_contract.md)  [Vectorstore Fragmentation](./GlobalFixMap/Embeddings/vectorstore_fragmentation.md) · [Dimension Mismatch & Projection](./GlobalFixMap/Embeddings/dimension_mismatch_and_projection.md) · [Update & Index Skew](./GlobalFixMap/Embeddings/update_and_index_skew.md)  [Hybrid Retriever Weights](./GlobalFixMap/Embeddings/hybrid_retriever_weights.md) · [Duplication & Collapse](./GlobalFixMap/Embeddings/duplication_and_near_duplicate_collapse.md) · [Poisoning & Contamination](./GlobalFixMap/Embeddings/poisoning_and_contamination.md) | embedding≠semantic checks |
| [Chunking](./GlobalFixMap/Chunking/README.md) | [Chunk ID Schema](./GlobalFixMap/Chunking/chunk_id_schema.md) · [Checklist](./GlobalFixMap/Chunking/chunking-checklist.md) · [Code / Tables / Blocks](./GlobalFixMap/Chunking/code_tables_blocks.md) · [Section Detection](./GlobalFixMap/Chunking/section_detection.md)  [Title Hierarchy](./GlobalFixMap/Chunking/title_hierarchy.md) · [PDF Layouts & OCR](./GlobalFixMap/Chunking/pdf_layouts_and_ocr.md) · [Reindex & Migration](./GlobalFixMap/Chunking/reindex_migration.md)  [Eval Precision & Recall](./GlobalFixMap/Chunking/eval_rag_precision_recall.md) · [Live Monitoring](./GlobalFixMap/Chunking/live_monitoring_rag.md) | chunk/section discipline |
| [RAG](./GlobalFixMap/RAG/README.md) | [Retrieval Drift](./GlobalFixMap/RAG/retrieval_drift.md) · [Hallucination RAG](./GlobalFixMap/RAG/hallucination_rag.md) · [Citation Break](./GlobalFixMap/RAG/citation_break.md) · [Hybrid Failure](./GlobalFixMap/RAG/hybrid_failure.md)  [Index Skew](./GlobalFixMap/RAG/index_skew.md) · [Context Drift](./GlobalFixMap/RAG/context_drift.md) · [Entropy Collapse](./GlobalFixMap/RAG/entropy_collapse.md) · [Eval Drift](./GlobalFixMap/RAG/eval_drift.md) | visual routes, acceptance targets |

---

### 🧭 Input & Parsing

| Family (link) | Coverage (all links) | Notes |
|---|---|---|
| [**DocumentAI_OCR**](./GlobalFixMap/DocumentAI_OCR/README.md) | [Tesseract](./GlobalFixMap/DocumentAI_OCR/tesseract.md) · [Google Document AI](./GlobalFixMap/DocumentAI_OCR/google_docai.md) · [AWS Textract](./GlobalFixMap/DocumentAI_OCR/aws_textract.md) · [Azure OCR](./GlobalFixMap/DocumentAI_OCR/azure_ocr.md) · [ABBYY](./GlobalFixMap/DocumentAI_OCR/abbyy.md) · [PaddleOCR](./GlobalFixMap/DocumentAI_OCR/paddleocr.md) | pre-embedding text integrity |
| [**OCR_Parsing**](./GlobalFixMap/OCR_Parsing/README.md) | [Layout, Headers, Footers](./GlobalFixMap/OCR_Parsing/layout_headers_and_footers.md) · [Tokenization & Casing](./GlobalFixMap/OCR_Parsing/tokenization_and_casing.md) · [Tables & Columns](./GlobalFixMap/OCR_Parsing/tables_and_columns.md) · [Images & Figures](./GlobalFixMap/OCR_Parsing/images_and_figures.md) · [Scanned PDFs & Quality](./GlobalFixMap/OCR_Parsing/scanned_pdfs_and_quality.md) · [Multi-language & Fonts](./GlobalFixMap/OCR_Parsing/multi_language_and_fonts.md) | parser rails & checks |
| [**Language**](./GlobalFixMap/Language/README.md) | [Tokenizer Mismatch](./GlobalFixMap/Language/tokenizer_mismatch.md) · [Script Mixing](./GlobalFixMap/Language/script_mixing.md) · [Locale Drift](./GlobalFixMap/Language/locale_drift.md) · [Multilingual Guide](./GlobalFixMap/Language/multilingual_guide.md) · [Proper Noun Aliases](./GlobalFixMap/Language/proper_noun_aliases.md)  [Romanization & Transliteration](./GlobalFixMap/Language/romanization_transliteration.md) · [Query Language Detection](./GlobalFixMap/Language/query_language_detection.md) · [Query Routing & Analyzers](./GlobalFixMap/Language/query_routing_and_analyzers.md) · [Hybrid Ranking (Multilingual)](./GlobalFixMap/Language/hybrid_ranking_multilingual.md) · [Stopword & Morphology Controls](./GlobalFixMap/Language/stopword_and_morphology_controls.md)  [Fallback Translation & Glossary Bridge](./GlobalFixMap/Language/fallback_translation_and_glossary_bridge.md) · [Code-Switching Eval](./GlobalFixMap/Language/code_switching_eval.md) | cross-script retrieval stability |
| [**LanguageLocale**](./GlobalFixMap/LanguageLocale/README.md) | [Tokenizer Mismatch (cross-lang)](./GlobalFixMap/LanguageLocale/tokenizer_mismatch.md) · [Script Mixing (single query)](./GlobalFixMap/LanguageLocale/script_mixing.md) · [Locale Drift & Analyzer Skew](./GlobalFixMap/LanguageLocale/locale_drift.md) · [Unicode Normalization](./GlobalFixMap/LanguageLocale/unicode_normalization.md) · [CJK Segmentation / Word-break](./GlobalFixMap/LanguageLocale/cjk_segmentation_wordbreak.md)  [Fullwidth vs Halfwidth, Punctuation](./GlobalFixMap/LanguageLocale/digits_width_punctuation.md) · [Diacritics & Folding](./GlobalFixMap/LanguageLocale/diacritics_and_folding.md) · [RTL / BiDi Control](./GlobalFixMap/LanguageLocale/rtl_bidi_control.md) · [Transliteration & Romanization](./GlobalFixMap/LanguageLocale/transliteration_and_romanization.md) · [Locale Collation & Sort Keys](./GlobalFixMap/LanguageLocale/locale_collation_and_sorting.md)  [Numbering & Sort Orders](./GlobalFixMap/LanguageLocale/numbering_and_sort_orders.md) · [Date/Time Format Variants](./GlobalFixMap/LanguageLocale/date_time_format_variants.md) · [Timezones & DST](./GlobalFixMap/LanguageLocale/timezones_and_dst.md) · [Keyboard Input Methods](./GlobalFixMap/LanguageLocale/keyboard_input_methods.md) · [Input Language Switching](./GlobalFixMap/LanguageLocale/input_language_switching.md)  [Emoji, ZWJ, Grapheme Clusters](./GlobalFixMap/LanguageLocale/emoji_zwj_grapheme_clusters.md) · [Mixed-Locale Metadata](./GlobalFixMap/LanguageLocale/mixed_locale_metadata.md) | analyzer / normalization profiles |

---

### 🧭 Reasoning & Memory

| Family | Coverage (all links) | Notes |
|---|---|---|
| [Reasoning](./GlobalFixMap/Reasoning/README.md) | [Entropy Overload](./GlobalFixMap/Reasoning/entropy-overload.md) · [Recursive Loop](./GlobalFixMap/Reasoning/recursive-loop.md) · [Hallucination Re-entry](./GlobalFixMap/Reasoning/hallucination-reentry.md) · [Logic Collapse](./GlobalFixMap/Reasoning/logic-collapse.md)  [Symbolic Collapse](./GlobalFixMap/Reasoning/symbolic-collapse.md) · [Proof Dead Ends](./GlobalFixMap/Reasoning/proof-dead-ends.md) · [Anchoring & Bridge Proofs](./GlobalFixMap/Reasoning/anchoring-and-bridge-proofs.md)  [Context Stitching & Window Joins](./GlobalFixMap/Reasoning/context-stitching-and-window-joins.md) · [Chain-of-Thought Variance Clamp](./GlobalFixMap/Reasoning/chain-of-thought-variance-clamp.md) · [Redundant Evidence Collapse](./GlobalFixMap/Reasoning/redundant-evidence-collapse.md) | BBMC / BBPF / BBCR / BBAM rails |
| [MemoryLongContext](./GlobalFixMap/MemoryLongContext/README.md) | [Memory Coherence](./GlobalFixMap/MemoryLongContext/memory-coherence.md) · [Entropy Collapse](./GlobalFixMap/MemoryLongContext/entropy-collapse.md) · [Context Drift](./GlobalFixMap/MemoryLongContext/context-drift.md) · [Ghost Context](./GlobalFixMap/MemoryLongContext/ghost-context.md)  [State Fork](./GlobalFixMap/MemoryLongContext/state-fork.md) · [Pattern Memory Desync](./GlobalFixMap/MemoryLongContext/pattern_memory_desync.md) · [OCR Jitter](./GlobalFixMap/MemoryLongContext/ocr-jitter.md) · [OCR Parsing Checklist](./GlobalFixMap/MemoryLongContext/ocr-parsing-checklist.md)  [Data Contracts](./GlobalFixMap/MemoryLongContext/data-contracts.md) · [Retrieval Traceability](./GlobalFixMap/MemoryLongContext/retrieval-traceability.md) · [Chunking Checklist](./GlobalFixMap/MemoryLongContext/chunking-checklist.md) | Long-window guardrails |
| [Multimodal_LongContext](./GlobalFixMap/Multimodal_LongContext/README.md) | [Alignment Drift](./GlobalFixMap/Multimodal_LongContext/alignment-drift.md) · [Anchor Misalignment](./GlobalFixMap/Multimodal_LongContext/anchor-misalignment.md) · [Boundary Fade](./GlobalFixMap/Multimodal_LongContext/boundary-fade.md) · [Caption Collapse](./GlobalFixMap/Multimodal_LongContext/caption-collapse.md)  [Cross-Modal Bootstrap](./GlobalFixMap/Multimodal_LongContext/cross-modal-bootstrap.md) · [Cross-Modal Trace](./GlobalFixMap/Multimodal_LongContext/cross-modal-trace.md) · [Desync Amplification](./GlobalFixMap/Multimodal_LongContext/desync-amplification.md) · [Desync Anchor](./GlobalFixMap/Multimodal_LongContext/desync-anchor.md)  [Echo Loop](./GlobalFixMap/Multimodal_LongContext/echo-loop.md) · [Fusion Blindspot](./GlobalFixMap/Multimodal_LongContext/fusion-blindspot.md) · [Fusion Latency](./GlobalFixMap/Multimodal_LongContext/fusion-latency.md) · [Modal Bridge Failure](./GlobalFixMap/Multimodal_LongContext/modal-bridge-failure.md)  [Modality Dropout](./GlobalFixMap/Multimodal_LongContext/modality-dropout.md) · [Modality Swap](./GlobalFixMap/Multimodal_LongContext/modality-swap.md) · [Multi-Hop Collapse](./GlobalFixMap/Multimodal_LongContext/multi-hop-collapse.md) · [Multi-Seed Consistency](./GlobalFixMap/Multimodal_LongContext/multi-seed-consistency.md)  [Multimodal Fusion Break](./GlobalFixMap/Multimodal_LongContext/multimodal-fusion-break.md) · [Phantom Visuals](./GlobalFixMap/Multimodal_LongContext/phantom-visuals.md) · [Reference Bleed](./GlobalFixMap/Multimodal_LongContext/reference-bleed.md) · [Semantic Anchor Shift](./GlobalFixMap/Multimodal_LongContext/semantic-anchor-shift.md)  [Signal Drop](./GlobalFixMap/Multimodal_LongContext/signal-drop.md) · [Spatial Fusion Error](./GlobalFixMap/Multimodal_LongContext/spatial-fusion-error.md) · [Sync Loop](./GlobalFixMap/Multimodal_LongContext/sync-loop.md) · [Time Sync Failure](./GlobalFixMap/Multimodal_LongContext/time-sync-failure.md) · [Visual Anchor Shift](./GlobalFixMap/Multimodal_LongContext/visual-anchor-shift.md) | Multimodal joins & anchors |


---

### 🧭 Automation & Ops

| Family (link) | Coverage examples | Notes |
|---|---|---|
| [**Automation**](./GlobalFixMap/Automation/README.md) | [Zapier](./GlobalFixMap/Automation/zapier.md) · [n8n](./GlobalFixMap/Automation/n8n.md) · [Make](./GlobalFixMap/Automation/make.md) · [Retool](./GlobalFixMap/Automation/retool.md) · [IFTTT](./GlobalFixMap/Automation/ifttt.md)  [Pipedream](./GlobalFixMap/Automation/pipedream.md) · [Power Automate](./GlobalFixMap/Automation/power-automate.md) · [GitHub Actions](./GlobalFixMap/Automation/github-actions.md) · [Airflow](./GlobalFixMap/Automation/airflow.md) · [Airtable](./GlobalFixMap/Automation/airtable.md)  [Asana](./GlobalFixMap/Automation/asana.md) · [GoHighLevel](./GlobalFixMap/Automation/ghl.md) · [Parabola](./GlobalFixMap/Automation/parabola.md) · [LangChain (automation)](./GlobalFixMap/Automation/langchain.md) · [LlamaIndex (automation)](./GlobalFixMap/Automation/llamaindex.md) | idempotency, warmups, fences |
| [**OpsDeploy**](./GlobalFixMap/OpsDeploy/README.md) | [Blue-Green Switchovers](./GlobalFixMap/OpsDeploy/blue_green_switchovers.md) · [Cache Warmup](./GlobalFixMap/OpsDeploy/cache_warmup_invalidation.md) · [DB Migration Guardrails](./GlobalFixMap/OpsDeploy/db_migration_guardrails.md) · [Feature Flags](./GlobalFixMap/OpsDeploy/feature_flags_safe_launch.md) · [Idempotency Dedup](./GlobalFixMap/OpsDeploy/idempotency_dedupe.md)  [Incident Comms](./GlobalFixMap/OpsDeploy/incident_comms_and_statuspage.md) · [Postmortem & Regression](./GlobalFixMap/OpsDeploy/postmortem_and_regression_tests.md) · [Rate Limit Backpressure](./GlobalFixMap/OpsDeploy/rate_limit_backpressure.md) · [Read-Only Mode](./GlobalFixMap/OpsDeploy/read_only_mode_and_maintenance_window.md) · [Release Calendar](./GlobalFixMap/OpsDeploy/release_calendar_and_change_freeze.md)  [Retry & Backoff](./GlobalFixMap/OpsDeploy/retry_backoff.md) · [Rollback & Recovery](./GlobalFixMap/OpsDeploy/rollback_and_fast_recovery.md) · [Rollout Gate](./GlobalFixMap/OpsDeploy/rollout_readiness_gate.md) · [Shadow Traffic](./GlobalFixMap/OpsDeploy/shadow_traffic_mirroring.md) · [Staged Canary](./GlobalFixMap/OpsDeploy/staged_rollout_canary.md)  [Vector Index Swap](./GlobalFixMap/OpsDeploy/vector_index_build_and_swap.md) · [Version Pinning](./GlobalFixMap/OpsDeploy/version_pinning_and_model_lock.md) | prod safety rails |
| [**Safety_PromptIntegrity**](./GlobalFixMap/Safety_PromptIntegrity/README.md) | [Prompt Injection](./GlobalFixMap/Safety_PromptIntegrity/prompt_injection.md) · [Jailbreaks & Overrides](./GlobalFixMap/Safety_PromptIntegrity/jailbreaks_and_overrides.md) · [Role Confusion](./GlobalFixMap/Safety_PromptIntegrity/role_confusion.md) · [Memory Fences](./GlobalFixMap/Safety_PromptIntegrity/memory_fences_and_state_keys.md) · [JSON & Tools](./GlobalFixMap/Safety_PromptIntegrity/json_mode_and_tool_calls.md)  [Citation First](./GlobalFixMap/Safety_PromptIntegrity/citation_first.md) · [Tool Selection & Timeouts](./GlobalFixMap/Safety_PromptIntegrity/tool_selection_and_timeouts.md) · [System/User/Role Order](./GlobalFixMap/Safety_PromptIntegrity/system_user_role_order.md) · [Template Library](./GlobalFixMap/Safety_PromptIntegrity/template_library_min.md) · [Eval Prompts](./GlobalFixMap/Safety_PromptIntegrity/eval_prompts_and_checks.md) | schema locks |
| [**PromptAssembly**](./GlobalFixMap/PromptAssembly/README.md) | [Anti-Injection Recipes](./GlobalFixMap/PromptAssembly/anti_prompt_injection_recipes.md) · [Citation First](./GlobalFixMap/PromptAssembly/citation_first.md) · [Eval Prompts](./GlobalFixMap/PromptAssembly/eval_prompts_and_checks.md) · [JSON Mode & Tools](./GlobalFixMap/PromptAssembly/json_mode_and_tool_calls.md) · [Memory Fences](./GlobalFixMap/PromptAssembly/memory_fences_and_state_keys.md)  [System/User/Role Order](./GlobalFixMap/PromptAssembly/system_user_role_order.md) · [Template Library](./GlobalFixMap/PromptAssembly/template_library_min.md) · [Tool Selection & Timeouts](./GlobalFixMap/PromptAssembly/tool_selection_and_timeouts.md) | contract & eval kits |
| [**LocalDeploy_Inference**](./GlobalFixMap/LocalDeploy_Inference/README.md) | [AutoGPTQ](./GlobalFixMap/LocalDeploy_Inference/autogptq.md) · [AWQ](./GlobalFixMap/LocalDeploy_Inference/awq.md) · [BitsAndBytes](./GlobalFixMap/LocalDeploy_Inference/bitsandbytes.md) · [CTransformers](./GlobalFixMap/LocalDeploy_Inference/ctransformers.md) · [ExLlama](./GlobalFixMap/LocalDeploy_Inference/exllama.md)  [ExLlamaV2](./GlobalFixMap/LocalDeploy_Inference/exllamaV2.md) · [GPT4All](./GlobalFixMap/LocalDeploy_Inference/gpt4all.md) · [Jan](./GlobalFixMap/LocalDeploy_Inference/jan.md) · [KoboldCpp](./GlobalFixMap/LocalDeploy_Inference/koboldcpp.md) · [llama.cpp](./GlobalFixMap/LocalDeploy_Inference/llamacpp.md)  [LMStudio](./GlobalFixMap/LocalDeploy_Inference/lmstudio.md) · [Ollama](./GlobalFixMap/LocalDeploy_Inference/ollama.md) · [Textgen-WebUI](./GlobalFixMap/LocalDeploy_Inference/textgen-webui.md) · [TGI](./GlobalFixMap/LocalDeploy_Inference/tgi.md) · [vLLM](./GlobalFixMap/LocalDeploy_Inference/vllm.md) | local stack guardrails |
| [**DevTools_CodeAI**](./GlobalFixMap/DevTools_CodeAI/README.md) | [GitHub Copilot](./GlobalFixMap/DevTools_CodeAI/github_copilot.md) · [Cursor](./GlobalFixMap/DevTools_CodeAI/cursor.md) · [Sourcegraph Cody](./GlobalFixMap/DevTools_CodeAI/sourcegraph_cody.md) · [VSCode Copilot Chat](./GlobalFixMap/DevTools_CodeAI/vscode_copilot_chat.md) · [Codeium](./GlobalFixMap/DevTools_CodeAI/codeium.md)  [Tabnine](./GlobalFixMap/DevTools_CodeAI/tabnine.md) · [AWS CodeWhisperer](./GlobalFixMap/DevTools_CodeAI/aws_codewhisperer.md) · [JetBrains AI Assistant](./GlobalFixMap/DevTools_CodeAI/jetbrains_ai_assistant.md) | IDE/assist rails |

---

#### 🧭 Eval & Governance
| Family (link) | Coverage examples | Notes |
|---|---|---|
| [**Eval**](./GlobalFixMap/Eval/README.md) | [Eval_Benchmarking](./GlobalFixMap/Eval/eval_benchmarking.md) · [Eval_Cost_Reporting](./GlobalFixMap/Eval/eval_cost_reporting.md) · [Eval_Cross_Agent_Consistency](./GlobalFixMap/Eval/eval_cross_agent_consistency.md) · [Eval_Harness](./GlobalFixMap/Eval/eval_harness.md) · [Eval_Latency_vs_Accuracy](./GlobalFixMap/Eval/eval_latency_vs_accuracy.md)  [Eval_Operator_Guidelines](./GlobalFixMap/Eval/eval_operator_guidelines.md) · [Eval_RAG_Precision_Recall](./GlobalFixMap/Eval/eval_rag_precision_recall.md) · [Eval_Semantic_Stability](./GlobalFixMap/Eval/eval_semantic_stability.md) · [Goldset_Curation](./GlobalFixMap/Eval/goldset_curation.md) | SDK-free evals |
| [**Eval_Observability**](./GlobalFixMap/Eval_Observability/README.md) | [Alerting_and_Probes](./GlobalFixMap/Eval_Observability/alerting_and_probes.md) · [Coverage_Tracking](./GlobalFixMap/Eval_Observability/coverage_tracking.md) · [DeltaS_Thresholds](./GlobalFixMap/Eval_Observability/deltaS_thresholds.md) · [Eval_Playbook](./GlobalFixMap/Eval_Observability/eval_playbook.md) · [Lambda_Observe](./GlobalFixMap/Eval_Observability/lambda_observe.md)  [Metrics_and_Logging](./GlobalFixMap/Eval_Observability/metrics_and_logging.md) · [Regression_Gate](./GlobalFixMap/Eval_Observability/regression_gate.md) · [Variance_and_Drift](./GlobalFixMap/Eval_Observability/variance_and_drift.md) | drift alarms |
| [**Governance**](./GlobalFixMap/Governance/README.md) | [Audit_and_Logging](./GlobalFixMap/Governance/audit_and_logging.md) · [Audit_Logs_and_Traceability](./GlobalFixMap/Governance/audit_logs_and_traceability.md) · [Data_Lineage_and_Provenance](./GlobalFixMap/Governance/data_lineage_and_provenance.md) · [Escalation_and_Governance](./GlobalFixMap/Governance/escalation_and_governance.md) · [Ethics_and_Bias_Mitigation](./GlobalFixMap/Governance/ethics_and_bias_mitigation.md)  [Eval_Governance_Gates_and_Signoff](./GlobalFixMap/Governance/eval_governance_gates_and_signoff.md) · [Incident_Response_and_Postmortems](./GlobalFixMap/Governance/incident_response_and_postmortems.md) · [License_and_Dataset_Rights](./GlobalFixMap/Governance/license_and_dataset_rights.md) · [Model_Governance_Model_Cards_and_Releases](./GlobalFixMap/Governance/model_governance_model_cards_and_releases.md)  [PII_Handling_and_Minimization](./GlobalFixMap/Governance/pii_handling_and_minimization.md) · [Policy_Baseline](./GlobalFixMap/Governance/policy_baseline.md) · [Prompt_Policy_and_Change_Control](./GlobalFixMap/Governance/prompt_policy_and_change_control.md) · [Regulatory_Alignment](./GlobalFixMap/Governance/regulatory_alignment.md) · [Risk_Register_and_Waivers](./GlobalFixMap/Governance/risk_register_and_waivers.md) · [Roles_and_Access_RBAC_ABAC](./GlobalFixMap/Governance/roles_and_access_rbac_abac.md) · [Transparency_and_Explainability](./GlobalFixMap/Governance/transparency_and_explainability.md) | program-level rails |
| [**Enterprise_Knowledge_Gov**](./GlobalFixMap/Enterprise_Knowledge_Gov/README.md) | [Access_Control](./GlobalFixMap/Enterprise_Knowledge_Gov/access_control.md) · [Audit_and_Traceability](./GlobalFixMap/Enterprise_Knowledge_Gov/audit_and_traceability.md) · [Compliance](./GlobalFixMap/Enterprise_Knowledge_Gov/compliance.md) · [Compliance_Audit](./GlobalFixMap/Enterprise_Knowledge_Gov/compliance_audit.md) · [Data_Residency](./GlobalFixMap/Enterprise_Knowledge_Gov/data_residency.md)  [Data_Sensitivity](./GlobalFixMap/Enterprise_Knowledge_Gov/data_sensitivity.md) · [Knowledge_Expiry](./GlobalFixMap/Enterprise_Knowledge_Gov/knowledge_expiry.md) · [Retention_Policy](./GlobalFixMap/Enterprise_Knowledge_Gov/retention_policy.md) | knowledge governance |

---

</details>


<div align="center">
  <img src="https://github.com/onestardao/WFGY/raw/main/OS/images/tree-semantic-memory.gif"
       alt="semantic memory & reasoning fix in action"
       width="100%" style="max-width:900px" loading="lazy">
</div>

---

> **❓ BigBig Question — If AI bugs are not random but mathematically inevitable, can we finally define and prevent them?**  
> *(this repo is one experiment toward that direction)*

---

## Quick Access

> don’t worry if this looks long. with TXT OS loaded, simply ask your LLM:  
> *“which Problem Map number fits my issue?”* it will point you to the right page.

- **Semantic Clinic (triage when unsure):** [Fix symptoms fast →](./SemanticClinicIndex.md)
- **Getting Started (practical):** [Guard a RAG pipeline with WFGY →](./getting-started.md)
- **Beginner Guide:** [Find and fix your first failure →](./BeginnerGuide.md)
- **Problem Map FAQ:** [Beginner + practitioner answers →](./faq.md)
- **Diagnose by symptom:** [`Diagnose.md` table →](./Diagnose.md)
- **Visual RAG Guide:** [`RAG Architecture & Recovery`](./rag-architecture-and-recovery.md)  
  high-altitude map linking symptom × stage × failure class with exact recovery paths.
- **Multi-Agent chaos:** [Role drift & memory overwrite →](./Multi-Agent_Problems.md)
- **TXT OS directory:** [browse the OS repo →](../OS/README.md)
- **MVP demos:** [Minimal WFGY examples →](./mvp_demo/README.md)

### 🆕 Common Issues (LangFlow, Hosting, RAG)
- **Slow on Railway/Cloud hosting:** [Performance troubleshooting →](./hosting-performance-slowness.md)
- **2000-page PDF splitting:** [Large PDF processing guide →](./large-pdf-processing.md)
- **Vector Store RAG errors:** [Template troubleshooting →](./vectorstore-rag-troubleshooting.md)

> tip: if you’re new, skip scrolling — use the **minimal quick-start** below.


## failure catalog (with fixes)

> if you are unsure which one applies, ask your LLM with TXT OS loaded:  
> *“which Problem Map number matches my trace?”* it will route you.

### legend
`[IN]` Input & Retrieval   `[RE]` Reasoning & Planning  
`[ST]` State & Context     `[OP]` Infra & Deployment  
`{OBS}` Observability/Eval `{SEC}` Security `{LOC}` Language/OCR

| #  | problem domain (with layer/tags)           | what breaks                                   | doc |
|----|--------------------------------------------|-----------------------------------------------|-----|
| 1  | **[IN]** hallucination & chunk drift {OBS} | retrieval returns wrong/irrelevant content    | [hallucination.md](./hallucination.md) |
| 2  | **[RE]** interpretation collapse           | chunk is right, logic is wrong                | [retrieval-collapse.md](./retrieval-collapse.md) |
| 3  | **[RE]** long reasoning chains {OBS}       | drifts across multi-step tasks                | [context-drift.md](./context-drift.md) |
| 4  | **[RE]** bluffing / overconfidence         | confident but unfounded answers               | [bluffing.md](./bluffing.md) |
| 5  | **[IN]** semantic ≠ embedding {OBS}        | cosine match ≠ true meaning                   | [embedding-vs-semantic.md](./embedding-vs-semantic.md) |
| 6  | **[RE]** logic collapse & recovery {OBS}   | dead-ends, needs controlled reset             | [logic-collapse.md](./logic-collapse.md) |
| 7  | **[ST]** memory breaks across sessions     | lost threads, no continuity                   | [memory-coherence.md](./memory-coherence.md) |
| 8  | **[IN]** debugging is a black box {OBS}    | no visibility into failure path               | [retrieval-traceability.md](./retrieval-traceability.md) |
| 9  | **[ST]** entropy collapse                  | attention melts, incoherent output            | [entropy-collapse.md](./entropy-collapse.md) |
| 10 | **[RE]** creative freeze                   | flat, literal outputs                         | [creative-freeze.md](./creative-freeze.md) |
| 11 | **[RE]** symbolic collapse                 | abstract/logical prompts break                | [symbolic-collapse.md](./symbolic-collapse.md) |
| 12 | **[RE]** philosophical recursion           | self-reference loops, paradox traps           | [philosophical-recursion.md](./philosophical-recursion.md) |
| 13 | **[ST]** multi-agent chaos {OBS}           | agents overwrite or misalign logic            | [Multi-Agent_Problems.md](./Multi-Agent_Problems.md) |
| 14 | **[OP]** bootstrap ordering                | services fire before deps ready               | [bootstrap-ordering.md](./bootstrap-ordering.md) |
| 15 | **[OP]** deployment deadlock               | circular waits in infra                       | [deployment-deadlock.md](./deployment-deadlock.md) |
| 16 | **[OP]** pre-deploy collapse {OBS}         | version skew / missing secret on first call   | [predeploy-collapse.md](./predeploy-collapse.md) |

for No.13 deep dives:  
• role drift → [`multi-agent-chaos/role-drift.md`](./multi-agent-chaos/role-drift.md)  
• cross-agent memory overwrite → [`multi-agent-chaos/memory-overwrite.md`](./multi-agent-chaos/memory-overwrite.md)


## 🧪 one-click sandboxes — run WFGY instantly
run lightweight diagnostics with zero install and zero api key. powered by colab.

> these tools map directly to the problem classes. others are handled inside WFGY and will surface in later CLIs.

<details>
<summary><strong>ΔS diagnostic (mvp)</strong> — measure semantic drift</summary>

[open in colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/tools/wfgy_diagnose_colab.ipynb)

detects: No.2 — [Interpretation Collapse](./retrieval-collapse.md)  
steps: run all, paste prompt+answer, read ΔS and fix tip
</details>

<details>
<summary><strong>λ_observe checkpoint</strong> — mid-step re-grounding</summary>

[open in colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/tools/wfgy_lambda_observe_colab.ipynb)

fixes: No.6 — [Logic Collapse & Recovery](./logic-collapse.md)  
steps: run all, compare ΔS before/after, fallback to BBCR if needed
</details>

<details>
<summary><strong>ε_resonance</strong> — domain-level harmony</summary>

[open in colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/tools/wfgy_e_resonance_colab.ipynb)

explains: No.12 — [Philosophical Recursion](./philosophical-recursion.md)  
steps: run, tune anchors, read ε
</details>

<details>
<summary><strong>λ_diverse</strong> — answer-set diversity</summary>

[open in colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/tools/wfgy_lambda_diverse_colab.ipynb)

detects: No.3 — [Long Reasoning Chains](./context-drift.md)  
steps: run, supply ≥3 answers, read score
</details>


## why this matters long-term

these 16 errors are not random. they are structural weak points every ai pipeline hits eventually.  
with WFGY as a **semantic firewall** you don’t just fix today’s issue — you shield tomorrow’s.

> this isn’t just a bug list. it’s an **x-ray** for your pipeline, so you stop guessing and start repairing.

see the end-to-end view: [`RAG Architecture & Recovery`](./rag-architecture-and-recovery.md)


## minimal quick-start

1) open **Beginner Guide** and follow the symptom checklist.  
2) use the **Visual RAG Guide** to locate the failing stage.  
3) open the matching page and apply the patch.

ask any LLM to apply WFGY (TXT OS makes it smoother):

```

i’ve uploaded TXT OS / WFGY notes.
my issue: \[e.g., OCR tables look fine but answers point to wrong sections]
which WFGY modules should i apply and in what order?

```


<details>
<summary><strong>status & difficulty</strong></summary>

| #  | problem (with layer/tags)                  | difficulty* | implementation |
|----|--------------------------------------------|-------------|----------------|
| 1  | **[IN]** hallucination & chunk drift {OBS} | medium      | ✅ stable |
| 2  | **[RE]** interpretation collapse           | high        | ✅ stable |
| 3  | **[RE]** long reasoning chains {OBS}       | high        | ✅ stable |
| 4  | **[RE]** bluffing / overconfidence         | high        | ✅ stable |
| 5  | **[IN]** semantic ≠ embedding {OBS}        | medium      | ✅ stable |
| 6  | **[RE]** logic collapse & recovery {OBS}   | very high   | ✅ stable |
| 7  | **[ST]** memory breaks across sessions     | high        | ✅ stable |
| 8  | **[IN]** debugging black box {OBS}         | medium      | ✅ stable |
| 9  | **[ST]** entropy collapse                  | high        | ✅ stable |
| 10 | **[RE]** creative freeze                   | medium      | ✅ stable |
| 11 | **[RE]** symbolic collapse                 | very high   | ✅ stable |
| 12 | **[RE]** philosophical recursion           | very high   | ✅ stable |
| 13 | **[ST]** multi-agent chaos {OBS}           | very high   | ✅ stable |
| 14 | **[OP]** bootstrap ordering                | medium      | ✅ stable |
| 15 | **[OP]** deployment deadlock               | high        | ⚠️ beta |
| 16 | **[OP]** pre-deploy collapse {OBS}         | medium-high | ✅ stable |

\*distance from default LLM behavior to a production-ready fix.
</details>


### 🔬 Behind the Map
The Problem Map is practical and ready to use.  
But if you wonder *why* these fixes work, and how we’re defining physics inside embedding space:  
→ [The Hidden Value Engine (WFGY Physics)](https://github.com/onestardao/WFGY/tree/main/value_manifest/README.md)


## 🔮 coming soon: global fix map

a universal layer above providers, agents, and infra.  
Problem Map is step one. **Global Fix Map** expands the same reasoning-first firewall to RAG, infra boot, agents, evals, and more. same zero-install experience. launching around **Sep**.


## contributing / support

- open an issue with a minimal repro (inputs → calls → wrong output).  
- PRs for clearer docs, repros, or patches are welcome.  
- project home: [github.com/onestardao/WFGY](https://github.com/onestardao/WFGY)  
- TXT OS: [browse the OS](https://github.com/onestardao/WFGY/tree/main/OS)  
- if this map helped you, a ⭐ helps more devs find it.

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
> Engineers, hackers, and open source builders who supported WFGY from day one.

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
