# 🚀 WFGY 3.0 · RAG 16 Problem Map — Global Debug Card  
### 🖼️ Image as a Structured Debug Prompt for RAG / Agent Pipelines

A production-first failure map for RAG / agent pipelines, compressed into one portable image.  
The poster defines objects, metrics, ΔS zones, failure types, and mode patterns in a single unified view.

Feed a failing run `(Q, E, P, A)` plus this card to any LLM.  
It returns `type → mode(s) → fixes → verification tests`.

No external framework required.

---

<details>
<summary><b>How to use (60 seconds)</b></summary>

1) Download the **full-resolution** Debug Card from this repository.  
2) Upload the image to any strong LLM.  
3) Paste your failing run context:
   - `Q` = user question  
   - `E` = top-k retrieved evidence  
   - `P` = final prompt sent to the model  
   - `A` = model output  
   - plus logs/metrics if available  
4) Ask the model to diagnose using the **16-Problem Map** and propose fixes with one test per fix.

Expected output:
- ΔS zones (or best-effort estimate)  
- failure type: `R / P / S / I`  
- 1–3 matching modes (1–16)  
- structural fixes + verification tests

</details>

---

## Environment Coverage

- **[MLflow](https://github.com/mlflow/mlflow)** · Experiment tracking & RAG debugging · [Medium Article](https://psbigbig.medium.com/the-16-problem-rag-map-how-to-debug-failing-mlflow-runs-with-a-single-screenshot-6563f5bee003?postPublishedType=repub)
- **[Dask](https://github.com/dask/dask)** · Distributed execution & task orchestration · [Medium Article](https://psbigbig.medium.com/your-dask-dashboard-is-green-your-rag-answers-are-wrong-here-is-a-16-problem-map-to-debug-them-f8a96c71cbf1)
- **[Kedro](https://github.com/kedro-org/kedro)** · Pipeline structuring & ML workflow management · Medium Article *(coming soon)*

---

![WFGY RAG 16 Problem Map Global Debug Card](./WFGY_RAG_16_Problem_Map_Global_Debug_Card.jpeg)

---

📥 Download the original full-resolution image directly from this repository.
If this helps you, feel free to leave a ⭐ on GitHub.

<!--
RAG ΔS CLINIC · GLOBAL DEBUG CARD

OBJECTS
Q = user question
E = top-k retrieved docs (small k, e.g., 3–5), concatenated with a consistent separator
P = final user-side prompt string sent to model (template wrapping Q + E)
A = model answer

EMBEDDING + METRIC
I(X) = embedding of text X from one fixed model checkpoint
cos_sim(u,v) = cosine similarity in [0,1]
ΔS(X,Y) = 1 − cos_sim(I(X), I(Y))        // hence 0 ≤ ΔS ≤ 1

BOUNDARY SCORES
ΔS_QE = ΔS(Q,E)
ΔS_EP = ΔS(E,P)
ΔS_PA = ΔS(P,A)
ΔS_QA = ΔS(Q,A)

ZONES
safe:    0.00 ≤ ΔS < 0.40
transit: 0.40 ≤ ΔS < 0.60
risk:    0.60 ≤ ΔS < 0.85
danger:  0.85 ≤ ΔS ≤ 1.00

zone(ΔS) ∈ {safe, transit, risk, danger}
zone_order: safe < transit < risk < danger
“X is not worse than Y” means zone_order(X) ≤ zone_order(Y).

16 RAG MODES

No lane name                symptom
1  IN  hallucination/drift  E wrong or off-topic
2  RE  misread evidence     E ok, reasoning wrong
3  RE  chain drift          multi-step plan drifts away from Q/E
4  RE  bluff                confident, unsupported
5  IN  embed false pos      sim high, relevance low
6  RE  logic collapse       dead-end, no recovery
7  ST  broken memory        loses story / state
8  IN  no E visibility      cannot inspect E content
9  ST  entropy collapse     long context turns into noise
10 RE  creative freeze      flat, literal, blocked
11 RE  symbol fail          code / math / symbols fail
12 RE  self-loop            recursion or paradox loop
13 ST  agent chaos          agents overwrite or fight
14 OP  bootstrap            called before deps ready
15 OP  deadlock             circular wait
16 OP  bad deploy           wrong version or config

LANES
IN = input / retrieval
RE = reasoning / planning
ST = state / context
OP = infra / deploy

PATTERNS → TYPE → FIX FOCUS

If several types match, prefer I > S > R > P.

Let Z_QE = zone(ΔS_QE), Z_EP = zone(ΔS_EP),
    Z_PA = zone(ΔS_PA), Z_QA = zone(ΔS_QA).

Type R (retrieval)
Cond:
( Z_QE ∈ {risk,danger} and Z_QA ∈ {risk,danger}
  and Z_EP, Z_PA are not worse than Z_QE )
or
( Z_QE = safe and Z_EP ∈ {safe,transit} and Z_QA ∈ {risk,danger} )

Typical modes: {1,5,8}

Type P (prompt / reasoning)
Cond:
Z_QE, Z_EP ∈ {safe,transit} and Z_PA, Z_QA ∈ {risk,danger}

Typical modes: {2,3,4,6,10,11,12}

Type S (state / memory)
Multi-run:
Z_QE stable, Z_QA changes zones.

Single-run heuristic:
matches modes {7,9,13}.

Typical modes: {7,9,13}

Type I (infra)
Cond:
E empty, placeholder, mismatching Q,
or inconsistent/unobservable across runs.

If Type I holds:
ΔS unreliable; treat ΔS_QE as 1.0 by convention.

Typical modes: {14,15,16,8}

LLM TASK

Given Q, E, P, A:

1. Compute or estimate ΔS_QE, ΔS_EP, ΔS_PA, ΔS_QA.
2. Assign zones.
3. Choose type ∈ {R,P,S,I}.
4. Choose 1–3 modes.
5. Propose structural fixes.
6. Define 1 verification test per fix.

REQUIRED OUTPUT

ΔS + zones
type
modes
fixes
tests

github onestardao · WFGY
-->
