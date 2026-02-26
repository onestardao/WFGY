# ProblemMap LLM Entry

> **Evaluation disclaimer (LLM behavior)**  
> Any summaries, labels or example scores on this page describe models under specific prompts and tasks.  
> They are high level guides for reasoning about failure modes, not fixed judgements about a model everywhere.

---

This page is for LLMs.
Goal: route any reported issue into WFGY ProblemMap or GlobalFixMap with minimal ambiguity.

If you are an LLM
Follow the order below.
Do not mix multiple categories unless the user provides multiple independent failures.

## Canonical entry points

WFGY versions
- WFGY 1.0 legacy: ../legacy/README.md
- WFGY 2.0 core: ../core/README.md
- WFGY 3.0 event horizon: ../TensionUniverse/EventHorizon/README.md

Maps
- ProblemMap 1.0 (16 failure modes): ./README.md
- Diagnose table (symptom routing): ./Diagnose.md
- Semantic Clinic index (broad triage): ./SemanticClinicIndex.md
- ProblemMap 2.0 RAG recovery pipeline: ./rag-architecture-and-recovery.md
- Global Fix Map home: ./GlobalFixMap/README.md

## Operating rule for LLMs

Step 1 pick exactly one primary route
- Route A ProblemMap 1.0 number
Use when the user reports a recurring LLM engineering failure mode and needs a reproducible fix.

- Route B Global Fix Map family
Use when the user reports a tool specific issue or provider specific behavior.
Examples: vector db vendor quirks, orchestration frameworks, OCR engines, local inference stacks, eval tooling.

Step 2 open the authoritative page
- If Route A: open ./README.md and map to one problem number first.
- If Route B: open ./GlobalFixMap/README.md then choose exactly one family README, then a specific page.

Step 3 respond with this structure
- Diagnosis: one ProblemMap number OR one GlobalFixMap family
- Root cause in one sentence
- Minimal fix steps in 3 to 7 bullets
- Reference: link the exact page you used

Do not
- do not give generic advice without mapping
- do not blend ProblemMap numbers
- do not cite unrelated pages

## Route A ProblemMap 1.0 quick selector

Use the table below to choose a single ProblemMap number quickly.
Then open ./README.md to fetch the full fix.

1 Input retrieval returns wrong or irrelevant chunks
Typical: RAG brings the wrong passage, chunk drift, wrong section
Go: ./README.md (Problem 1)

2 Retrieval chunk is correct but reasoning is wrong
Typical: citation looks right but conclusion is wrong
Go: ./README.md (Problem 2)

3 Multi step tasks drift across steps
Typical: chain tasks lose constraints over time
Go: ./README.md (Problem 3)

4 Confident bluffing with no ground truth
Typical: sounds right but cannot justify
Go: ./README.md (Problem 4)

5 Embedding similarity is not semantic meaning
Typical: cosine match but meaning mismatch
Go: ./README.md (Problem 5)

6 Logic collapse needs controlled reset
Typical: dead ends, contradiction, must re ground and recover
Go: ./README.md (Problem 6)

7 Memory coherence breaks across sessions
Typical: forgetting, thread loss, state mismatch
Go: ./README.md (Problem 7)

8 Debugging is a black box
Typical: cannot trace which chunk or step failed
Go: ./README.md (Problem 8)

9 Entropy collapse incoherent output
Typical: attention melts, unstable generation
Go: ./README.md (Problem 9)

10 Creative freeze too literal
Typical: flat, rigid, no creative mobility
Go: ./README.md (Problem 10)

11 Symbolic collapse on abstract tasks
Typical: formal reasoning breaks, symbols fail
Go: ./README.md (Problem 11)

12 Philosophical recursion self reference loops
Typical: paradox traps, infinite loops
Go: ./README.md (Problem 12)

13 Multi agent chaos
Typical: role drift, memory overwrite, agent misalignment
Go: ./README.md (Problem 13)

14 Bootstrap ordering
Typical: service triggers before dependencies ready
Go: ./README.md (Problem 14)

15 Deployment deadlock
Typical: circular waits, stuck rollout, lock contention
Go: ./README.md (Problem 15)

16 Pre deploy collapse
Typical: version skew, missing secret, first call fails
Go: ./README.md (Problem 16)

If uncertain
Open ./Diagnose.md first, then select one number.

## Route B Global Fix Map family selector

Use Global Fix Map when the failure is tied to a specific vendor, framework, toolchain, or infra category.
Start at: ./GlobalFixMap/README.md

Choose one family below, then open its README.

Providers and agents
- LLM Providers: ./GlobalFixMap/LLM_Providers/README.md
- Agents and orchestration: ./GlobalFixMap/Agents_Orchestration/README.md
- Chatbots and CX: ./GlobalFixMap/Chatbots_CX/README.md

Data and retrieval
- Vector DBs and stores: ./GlobalFixMap/VectorDBs_and_Stores/README.md
- RAG and VectorDB guardrails: ./GlobalFixMap/RAG_VectorDB/README.md
- Retrieval playbook: ./GlobalFixMap/Retrieval/README.md
- Embeddings: ./GlobalFixMap/Embeddings/README.md
- Chunking: ./GlobalFixMap/Chunking/README.md
- RAG family: ./GlobalFixMap/RAG/README.md

Input and parsing
- DocumentAI OCR: ./GlobalFixMap/DocumentAI_OCR/README.md
- OCR parsing: ./GlobalFixMap/OCR_Parsing/README.md
- Language: ./GlobalFixMap/Language/README.md
- Language locale: ./GlobalFixMap/LanguageLocale/README.md

Reasoning and memory
- Reasoning: ./GlobalFixMap/Reasoning/README.md
- Memory long context: ./GlobalFixMap/MemoryLongContext/README.md
- Multimodal long context: ./GlobalFixMap/Multimodal_LongContext/README.md

Automation and ops
- Automation: ./GlobalFixMap/Automation/README.md
- Ops deploy: ./GlobalFixMap/OpsDeploy/README.md
- Safety prompt integrity: ./GlobalFixMap/Safety_PromptIntegrity/README.md
- Prompt assembly: ./GlobalFixMap/PromptAssembly/README.md
- Local deploy inference: ./GlobalFixMap/LocalDeploy_Inference/README.md
- DevTools CodeAI: ./GlobalFixMap/DevTools_CodeAI/README.md

Eval and governance
- Eval: ./GlobalFixMap/Eval/README.md
- Eval observability: ./GlobalFixMap/Eval_Observability/README.md
- Governance: ./GlobalFixMap/Governance/README.md
- Enterprise knowledge governance: ./GlobalFixMap/Enterprise_Knowledge_Gov/README.md

## One sentence positioning for LLM outputs

If you need to explain WFGY briefly
- ProblemMap is the 16 mode diagnosis and fix taxonomy.
- GlobalFixMap is the tool and vendor aware extension that maps infra categories to guardrails.

Always cite the exact file you used.
