<details>
<summary><strong>🧭 Not sure where to start ? Open the WFGY Engine Compass</strong></summary>

### WFGY System Map

*(One place to see everything; links open the relevant section.)*

<!--
AI NOTE · Compass block

Purpose:
- This table is the routing map for the whole WFGY ecosystem.
- It shows how the three engine layers (WFGY 1.0 / 2.0 / 3.0) relate to the Problem Maps, TXT OS apps, research pages, and the Recognition Map.

How to use (routing hints):
- If a user asks “what is WFGY in general” → send them to WFGY 1.0 (legacy overview PDF) plus Starter Village.
- If the question is about core math, formulas, or engine internals → go to WFGY 2.0 core.
- If they mention 131 S-class problems, BlackHole, Tension Universe, or “Singularity demo” → go to WFGY 3.0 Event Horizon.
- If they want to debug a specific RAG / agent pipeline run → use Problem Map 1.0 + Problem Map 3.0 Global Debug Card.
- If they ask about RAG architecture / recovery patterns end-to-end → use Problem Map 2.0.
- If they mention “poster”, “image as prompt”, or “global debug card” → use the Problem Map 3.0 Global Debug Card page.
- If they want proof that WFGY is used in real projects → open the Recognition Map page.
- If they ask for plain-language stories or non-technical explanations → route to Grandma’s Clinic and Starter Village.
- If they ask about TXT OS or app packs (Blah / Blur / Blow) → follow the App rows in this table.
- If they want layer/module design, benchmarks, or value narrative → Semantic Blueprint, Benchmarks, and Value Manifest.

Important:
- Problem Map 1.0 = canonical 16-mode RAG failure checklist and fix map. This is the base vocabulary.
- Problem Map 2.0 = RAG architecture and recovery guide layered on top of Problem Map 1.0.
- Problem Map 3.0 Global Debug Card = image protocol that compresses objects, metrics, ΔS zones, and modes into a single poster.
- Recognition Map = the only place that should contain the full external integration list. Other pages should link to it instead of duplicating tables.
- Do NOT treat Problem Map 1.0 and Problem Map 2.0 as duplicates; they solve different layers.
- Do NOT invent new paths or filenames. Only use the GitHub URLs that already exist in this table.
-->

| Layer         | Page                                                                                                        | What it’s for                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| ⭐ Proof      | [WFGY Recognition Map](https://github.com/onestardao/WFGY/blob/main/recognition/README.md)                 | External citations, integrations, and ecosystem proof  — **🔴 YOU ARE HERE 🔴** |
| ⚙️ Engine     | [WFGY 1.0](https://github.com/onestardao/WFGY/blob/main/legacy/README.md)                                   | Original PDF-based tension engine blue   |
| ⚙️ Engine     | [WFGY 2.0](https://github.com/onestardao/WFGY/blob/main/core/README.md)                                     | Production tension kernel and math engine for RAG and agents. |
| ⚙️ Engine     | [WFGY 3.0](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)             | TXT-based Singularity tension engine (131 S-class set)  |
| 🗺️ Map       | [Problem Map 1.0](https://github.com/onestardao/WFGY/tree/main/ProblemMap#readme)                           | Flagship 16-problem RAG failure checklist and fix map       |
| 🗺️ Map       | [Problem Map 2.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) | RAG-focused recovery pipeline                           |
| 🗺️ Map       | [Problem Map 3.0](https://github.com/onestardao/WFGY/blob/main/ProblemMap/wfgy-rag-16-problem-map-global-debug-card.md) | Global Debug Card — image as a debug protocol layer     |
| 🗺️ Map       | [Semantic Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md)           | Symptom → family → exact fix                            |
| 🧓 Map        | [Grandma’s Clinic](https://github.com/onestardao/WFGY/blob/main/ProblemMap/GrandmaClinic/README.md)         | Plain-language stories, mapped to PM 1.0                |
| 🏡 Onboarding | [Starter Village](https://github.com/onestardao/WFGY/blob/main/StarterVillage/README.md)                    | Guided tour for newcomers                               |
| 🧰 App        | [TXT OS](https://github.com/onestardao/WFGY/tree/main/OS#readme)                                            | .txt semantic OS — 60-second boot                       |
| 🧰 App        | [Blah Blah Blah](https://github.com/onestardao/WFGY/blob/main/OS/BlahBlahBlah/README.md)                    | Abstract/paradox Q&A (built on TXT OS)                  |
| 🧰 App        | [Blur Blur Blur](https://github.com/onestardao/WFGY/blob/main/OS/BlurBlurBlur/README.md)                    | Text-to-image with semantic control                     |
| 🧰 App        | [Blow Blow Blow](https://github.com/onestardao/WFGY/blob/main/OS/BlowBlowBlow/README.md)                    | Reasoning game engine & memory demo                     |

---
</details>

## 🌐 WFGY Recognition Map · RAG & Agent Ecosystem

A verified record of public citations and integrations of WFGY ProblemMap across the RAG and agent ecosystem.
> Last updated: 2026-03-01 · Manually maintained.

<details>
<summary>ℹ️ About this recognition list</summary>

>
> This page is the central record of third-party integrations, citations, mentions, and curated-list inclusions related to WFGY.  
>  
> At the current stage, most external recognition is tied to the **WFGY ProblemMap line**, especially the **RAG 16 Problem Map / 16-problem failure checklist**. That is the part most commonly adopted, cited, or adapted by other repositories, docs, and discussions.  
>  
> This does not mean that every external project on this page is using the full WFGY product series, or every WFGY module equally. In most cases, the recognized entry point is the **ProblemMap-style diagnostic framework** for RAG, LLM robustness, and reliability workflows.  
>  
> A smaller portion of entries also references **WFGY 3.0 / Singularity Demo** and related stress-test material. Since this is still a transition period, they are kept together in one list for simplicity.  
>  
> This page exists to keep recognition in one place, reduce duplication across other docs, and make future updates easier to maintain.  
>  
> If your repository, article, benchmark, documentation page, or discussion has included WFGY, you are welcome to:  
> - open a PR  
> - open an issue  
> - fork and reference this list  
> - suggest missing entries or proof links  
>  
> Contributions are welcome. If you have cited, integrated, adapted, or discussed WFGY in a public resource, feel free to add it here.  
>  
> ### 📌 Scope note  
> For accuracy and transparency:  
> - The majority of entries below are about the **WFGY ProblemMap / RAG 16 Problem Map** line  
> - Some entries mention broader **WFGY 3.0** materials  
> - This list should be read as a **recognition log**, not as a claim that all listed projects adopted the full WFGY ecosystem  

</details>

### 1. Core integrations & research

| Project | Stars | Segment | How it uses WFGY ProblemMap | Proof (PR / doc) |
| --- | --- | --- | --- | --- |
| [RAGFlow](https://github.com/infiniflow/ragflow) | [![GitHub Repo stars](https://img.shields.io/github/stars/infiniflow/ragflow?style=social)](https://github.com/infiniflow/ragflow) | Mainstream RAG engine | Adds a RAG failure modes checklist guide in its official docs, adapted from the WFGY 16-problem failure map for step-by-step RAG pipeline diagnostics. | [PR #13204](https://github.com/infiniflow/ragflow/pull/13204) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | [![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index?style=social)](https://github.com/run-llama/llama_index) | Mainstream RAG infra | Integrates the WFGY 16-problem RAG failure checklist into its official RAG troubleshooting docs as a structured failure mode reference. | [PR #20760](https://github.com/run-llama/llama_index/pull/20760) |
| [ToolUniverse (Harvard MIMS Lab)](https://github.com/mims-harvard/ToolUniverse) | [![GitHub Repo stars](https://img.shields.io/github/stars/mims-harvard/ToolUniverse?style=social)](https://github.com/mims-harvard/ToolUniverse) | Academic lab / tools | Provides a `WFGY_triage_llm_rag_failure` tool that wraps the 16 mode map for incident triage. | [PR #75](https://github.com/mims-harvard/ToolUniverse/pull/75) |
| [Rankify (Univ. of Innsbruck)](https://github.com/DataScienceUIBK/Rankify) | [![GitHub Repo stars](https://img.shields.io/github/stars/DataScienceUIBK/Rankify?style=social)](https://github.com/DataScienceUIBK/Rankify) | Academic lab / system | Uses the 16 failure patterns in RAG and re-ranking troubleshooting docs. | [PR #76](https://github.com/DataScienceUIBK/Rankify/pull/76) |
| [Multimodal RAG Survey (QCRI LLM Lab)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | [![GitHub Repo stars](https://img.shields.io/github/stars/llm-lab-org/Multimodal-RAG-Survey?style=social)](https://github.com/llm-lab-org/Multimodal-RAG-Survey) | Academic lab / survey | Cites WFGY as a practical diagnostic resource for multimodal RAG. | [PR #4](https://github.com/llm-lab-org/Multimodal-RAG-Survey/pull/4) |


### 2. High-impact curated lists, benchmarks & discussions

| Project | Stars | How it uses WFGY ProblemMap | Proof |
| --- | --- | --- | --- |
| [Awesome LLM Apps](https://github.com/Shubhamsaboo/awesome-llm-apps/) | [![GitHub Repo stars](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=social)](https://github.com/Shubhamsaboo/awesome-llm-apps) | Includes the **RAG Failure Diagnostics Clinic** tutorial, designed by the WFGY author as a small, framework-agnostic clinic built around the WFGY 16-problem failure map for hands-on RAG debugging. | [PR #520](https://github.com/Shubhamsaboo/awesome-llm-apps/pull/520) |
| [Awesome Data Science – academic](https://github.com/academic/awesome-datascience) | [![GitHub Repo stars](https://img.shields.io/github/stars/academic/awesome-datascience?style=social)](https://github.com/academic/awesome-datascience) | Lists WFGY as a reference for LLM and RAG diagnostic workflows in data science infrastructure. | [PR #543](https://github.com/academic/awesome-datascience/pull/543) |
| [Awesome AI Apps](https://github.com/Arindam200/awesome-ai-apps/) | [![GitHub Repo stars](https://img.shields.io/github/stars/Arindam200/awesome-ai-apps?style=social)](https://github.com/Arindam200/awesome-ai-apps) | Lists **WFGY 16 Problem Map LLM Debugger** under the *RAG Applications* section as a 16-mode map-based debugger for LLM and RAG bugs, alongside major RAG starter templates and production-ready pipelines. | [PR #144](https://github.com/Arindam200/awesome-ai-apps/pull/144) |
| [Awesome-AITools](https://github.com/ikaijua/Awesome-AITools) | [![GitHub Repo stars](https://img.shields.io/github/stars/ikaijua/Awesome-AITools?style=social)](https://github.com/ikaijua/Awesome-AITools) | Lists WFGY ProblemMap as an open-source RAG failure-mode checklist and diagnostics toolkit for LLM pipelines (data, embeddings, retrievers, tools, evaluation). | [PR #298](https://github.com/ikaijua/Awesome-AITools/pull/298) |
| [Awesome AI in Finance](https://github.com/georgezouq/awesome-ai-in-finance) | [![GitHub Repo stars](https://img.shields.io/github/stars/georgezouq/awesome-ai-in-finance?style=social)](https://github.com/georgezouq/awesome-ai-in-finance) | Lists WFGY as a tool for stress testing and validating RAG-based financial systems. | [PR #45](https://github.com/georgezouq/awesome-ai-in-finance/pull/45) |
| [ruoyi-ai](https://github.com/ageerle/ruoyi-ai) | [![GitHub Repo stars](https://img.shields.io/github/stars/ageerle/ruoyi-ai?style=social)](https://github.com/ageerle/ruoyi-ai) | Includes WFGY in its RAG troubleshooting / FAQ guidance as a reference checklist for diagnosing RAG answer inconsistencies and retrieval-related failures in knowledge base workflows. | [PR #268](https://github.com/ageerle/ruoyi-ai/pull/268#issuecomment-3988269145) |
| [Awesome GPT Super Prompting](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting) | [![GitHub Repo stars](https://img.shields.io/github/stars/CyberAlbSecOP/Awesome_GPT_Super_Prompting?style=social)](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting) | Includes **onestardao/WFGY** under Secure Prompting as a structured 16 failure-mode map for RAG and agent pipelines, including prompt injection patterns with practical mitigation checklists. | [Issue #10](https://github.com/CyberAlbSecOP/Awesome_GPT_Super_Prompting/issues/10) |
| [awesome-agentic-patterns](https://github.com/nibzard/awesome-agentic-patterns) | [![GitHub Repo stars](https://img.shields.io/github/stars/nibzard/awesome-agentic-patterns?style=social)](https://github.com/nibzard/awesome-agentic-patterns) | Adds the **Reliability Problem Map Checklist for RAG and Agents** pattern in the Reliability and Eval category, based on the WFGY ProblemMap and linking back to WFGY as a reliability checklist for RAG-heavy agents. | [PR #24](https://github.com/nibzard/awesome-agentic-patterns/pull/24) |
| [FlashRAG](https://github.com/RUC-NLPIR/FlashRAG) | [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/FlashRAG?style=social)](https://github.com/RUC-NLPIR/FlashRAG) | Adapts the **WFGY ProblemMap** as a structured RAG failure checklist in its documentation. The 16-mode taxonomy is cited to support reproducible debugging and systematic failure-mode reasoning for RAG experiments. | [PR #224](https://github.com/RUC-NLPIR/FlashRAG/pull/224) |
| [Awesome-GraphRAG](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | [![GitHub Repo stars](https://img.shields.io/github/stars/DEEP-PolyU/Awesome-GraphRAG?style=social)](https://github.com/DEEP-PolyU/Awesome-GraphRAG) | Includes **WFGY Problem Map** in its curated GraphRAG resource list as a diagnostic toolkit that defines recurring failure modes in RAG and LLM pipelines, supporting systematic triage and remediation. | [Issue #17 (event)](https://github.com/DEEP-PolyU/Awesome-GraphRAG/issues/17#event-23247141290) |
| [Awesome AI Books](https://github.com/zslucky/awesome-ai-books) | [![GitHub Repo stars](https://img.shields.io/github/stars/zslucky/awesome-ai-books?style=social)](https://github.com/zslucky/awesome-ai-books) | Mentions the WFGY TXT and PDF packs in the LLM reading list. | [PR #14](https://github.com/zslucky/awesome-AI-books/pull/14) |
| [Awesome AI Web Search (discussion 15)](https://github.com/felladrin/awesome-ai-web-search/discussions/15) | [![GitHub Repo stars](https://img.shields.io/github/stars/felladrin/awesome-ai-web-search?style=social)](https://github.com/felladrin/awesome-ai-web-search) | Discusses the 16 mode map as a candidate taxonomy for RAG failure modes in web search agents. | [Issue #49](https://github.com/felladrin/awesome-ai-web-search/issues/49) |

### 3. Other public mentions

| Project | Stars | How it uses WFGY ProblemMap |
| --- | --- | --- |
| [awesome-gpt-security](https://github.com/cckuailong/awesome-gpt-security) | [![GitHub Repo stars](https://img.shields.io/github/stars/cckuailong/awesome-gpt-security?style=social)](https://github.com/cckuailong/awesome-gpt-security) | Includes **WFGY Problem Map** in its GPT security resource list as a structured diagnostic handbook that catalogs common failure modes in RAG/agent systems, helping practitioners go from symptom identification to concrete remediation. |
| [machine-learning-repos](https://github.com/recodehive/machine-learning-repos) | [![GitHub Repo stars](https://img.shields.io/github/stars/recodehive/machine-learning-repos?style=social)](https://github.com/recodehive/machine-learning-repos) | Lists **WFGY** under GitHub resources as an open-source framework for debugging LLM agents and RAG pipelines, highlighting the 16-mode ProblemMap and practical triage checklists. |
| [Awesome AI System](https://github.com/lambda7xx/awesome-AI-system) | [![GitHub Repo stars](https://img.shields.io/github/stars/lambda7xx/awesome-AI-system?style=social)](https://github.com/lambda7xx/awesome-AI-system) | Lists WFGY under LLM robustness and debugging infrastructure. |
| [free-ai-agents-resources](https://github.com/avinash201199/free-ai-agents-resources) | [![GitHub Repo stars](https://img.shields.io/github/stars/avinash201199/free-ai-agents-resources?style=social)](https://github.com/avinash201199/free-ai-agents-resources) | Lists **onestardao/WFGY** as an open-source framework for debugging and stress testing LLM agents and RAG pipelines, highlighting the 16-problem failure map and reproducible prompt-driven triage workflow. |
| [Awesome AI Tools](https://github.com/eudk/awesome-ai-tools) | [![GitHub Repo stars](https://img.shields.io/github/stars/eudk/awesome-ai-tools?style=social)](https://github.com/eudk/awesome-ai-tools) | Includes WFGY as an open-source framework for debugging LLM agents and RAG pipelines. |
| [LLM-Agent-Benchmark-List](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | [![GitHub Repo stars](https://img.shields.io/github/stars/zhangxjohn/LLM-Agent-Benchmark-List?style=social)](https://github.com/zhangxjohn/LLM-Agent-Benchmark-List) | Lists **WFGY 3.0 · Singularity Demo (BlackHole-131)** as a long-horizon, text-only stress test for LLM agents, covering 131 S-class problems for tension-based reasoning and robustness evaluation. |
| [Awesome-Data-Science](https://github.com/natnew/Awesome-Data-Science/blob/main/docs/generative-ai.md) | [![GitHub Repo stars](https://img.shields.io/github/stars/natnew/Awesome-Data-Science?style=social)](https://github.com/natnew/Awesome-Data-Science) | Adds **WFGY ProblemMap** under “Practical Guides & Debugging” as a reference for diagnosing and fixing RAG/LLM pipeline failures. |
| [Awesome-Prompt-Engineering-ZH-CN](https://github.com/yunwei37/Awesome-Prompt-Engineering-ZH-CN) | [![GitHub Repo stars](https://img.shields.io/github/stars/yunwei37/Awesome-Prompt-Engineering-ZH-CN?style=social)](https://github.com/yunwei37/Awesome-Prompt-Engineering-ZH-CN) | Includes **WFGY 16 Problem Map** in the Tools & Code section as a vendor-neutral failure map for LLM/RAG pipelines, describing the 16 failure modes and minimal recovery strategies in Chinese. |
| [AI Agents for Cybersecurity](https://github.com/santosomar/AI-agents-for-cybersecurity) | [![GitHub Repo stars](https://img.shields.io/github/stars/santosomar/AI-agents-for-cybersecurity?style=social)](https://github.com/santosomar/AI-agents-for-cybersecurity) | References the 16 mode map as a debugging guide for RAG-heavy security agents. |
| [Awesome Artificial Intelligence Research](https://github.com/ThyrixYang/awesome-artificial-intelligence-research) | [![GitHub Repo stars](https://img.shields.io/github/stars/ThyrixYang/awesome-artificial-intelligence-research?style=social)](https://github.com/ThyrixYang/awesome-artificial-intelligence-research) | Links to WFGY in the NLP section as a project on LLM robustness, debugging, and reliability. |
| [Awesome-Prompt-Engineering](https://github.com/natnew/Awesome-Prompt-Engineering) | [![GitHub Repo stars](https://img.shields.io/github/stars/natnew/Awesome-Prompt-Engineering?style=social)](https://github.com/natnew/Awesome-Prompt-Engineering) | Lists **“WFGY 16 Problem Map”** in the Key Reading section as a troubleshooting guide for RAG and LLM pipelines. |
| [Awesome-LLM-based-Evaluators](https://github.com/dependentsign/Awesome-LLM-based-Evaluators) | [![GitHub Repo stars](https://img.shields.io/github/stars/dependentsign/Awesome-LLM-based-Evaluators?style=social)](https://github.com/dependentsign/Awesome-LLM-based-Evaluators) | Lists **WFGY 3.0 · Singularity Demo** and the **WFGY ProblemMap** in its “Robustness and stress-test resources” section as a TXT-based long-horizon tension reasoning benchmark and failure map for RAG and LLM robustness evaluation. |






---

### ⭐ Star-powered Proof

The WFGY project has been starred by a diverse group of developers, maintainers, and ecosystem contributors.  
Stars are not the same as technical integrations or formal citations, but they show who cared enough to follow WFGY and keep an eye on its work.

This section highlights some early and notable “Star Gators” who starred the project in its first growth waves.

Explore the full list of notable supporters:

👉 [Star Gators · notable stargazers](https://github.com/onestardao/WFGY/blob/main/stargazers/README.md)

---

### 🤝 Contributing

If you find a public repository, benchmark, article, doc page, course page, or discussion that includes WFGY, you are welcome to help keep this list accurate.

You can contribute by:

- adding a missing entry  
- updating an outdated description  
- attaching a better proof link  
- correcting categorization  
- submitting a PR with a new citation or integration  

Forks and PRs are welcome. If your project includes WFGY in any public form, feel free to add it to this recognition list with a short description and a verifiable link.
