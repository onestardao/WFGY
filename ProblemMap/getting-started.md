# Getting Started — Apply the WFGY Problem Map in real projects (no SDK)

This page shows how to turn the Problem Map into a working pipeline.
No framework lock-in. No custom SDK. Everything is minimal, testable, and easy to remove if you do not like it.

**You will build**

1. A stable retrieval chain that resists chunk drift and reduces hallucinations.
2. A thin guard that forces answers to stay inside evidence.
3. A trace log so you can locate failure points and map them to Problem Map items.
4. A small evaluation harness so you can prove improvements.

**Hardware**
A laptop with 16 to 32 GB RAM is enough for a 300 to 800 page corpus using CPU embeddings and FAISS or SQLite VSS.

**References**

* Problem Map index: `ProblemMap/README.md`
* RAG Architecture and Recovery: `ProblemMap/rag-architecture-and-recovery.md`
* Math layer and rules (PDF): [Download Now](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf
)

---

## 0. Principles you will enforce

These map directly to common failures in the Problem Map.

* Retrieval is constrained to avoid returning context that crosses entity or constraint boundaries by default. Boundary leakage can still occur if constraints are incomplete, in which case we tighten extraction rules.
* Generation must quote only the provided evidence. If not provable, it must say `not in context`.
* Every answer writes a machine readable trace with query, chunk ids, and scores. This turns debugging from guesswork into data.
* Optional rerank step promotes passages that match constraints, not only keywords.
* When storage or write fails, do not advance offsets or cursors. This prevents No.11 Symbolic Collapse type off by one bugs in pipelines.

---

## 1. Corpus preparation and chunking (Python)

Install minimal tools.

```bash
pip install pypdf rank-bm25 sentence-transformers faiss-cpu rapidfuzz
```

Extract text per page. Save page spans to preserve boundaries.

```python
# tools/extract_pdf.py
from pypdf import PdfReader
import json, sys

def extract(pdf_path, out_json):
    reader = PdfReader(pdf_path)
    docs = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        docs.append({"id": f"p{i+1}", "page": i+1, "text": text})
    with open(out_json, "w", encoding="utf8") as f:
        json.dump(docs, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])
```

Chunk with a constraint aware strategy.
Keep headings or definition lines attached to their paragraphs. Merge small lines, but avoid crossing section boundaries like References or Footnotes unless section-level intent explicitly allows it.

```python
# tools/chunk.py
import re, json, sys
MAX_TOKENS = 350  # target size per chunk

def split_into_sentences(txt):
    # light sentence split. replace with a better splitter if you have one.
    return re.split(r'(?<=[.!?])\s+', txt.strip())

def is_boundary(line):
    head = line.lower().strip()
    return bool(re.match(r'^(abstract|introduction|conclusion|references?)\b', head))

def chunk_page(doc):
    lines = [l for l in doc["text"].splitlines() if l.strip()]
    chunks, buf, tokens, mark_boundary = [], [], 0, False
    for ln in lines:
        if is_boundary(ln):
            mark_boundary = True
        sents = split_into_sentences(ln)
        for s in sents:
            t = max(1, len(s.split()))
            if tokens + t > MAX_TOKENS or mark_boundary:
                if buf:
                    chunks.append(" ".join(buf))
                buf, tokens, mark_boundary = [s], t, False
            else:
                buf.append(s); tokens += t
    if buf:
        chunks.append(" ".join(buf))
    out = []
    for j, c in enumerate(chunks):
        out.append({
            "id": f'{doc["id"]}#{j+1}',
            "page": doc["page"],
            "text": c
        })
    return out

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    docs = json.load(open(src, encoding="utf8"))
    out = []
    for d in docs:
        out.extend(chunk_page(d))
    json.dump(out, open(dst, "w", encoding="utf8"), ensure_ascii=False, indent=2)
```

---

## 2. Build a hybrid index: BM25 + embeddings + optional rerank (Python)

```bash
pip install numpy
```

```python
# index/build.py
import json, numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import faiss, os, sys

def build(corpus_json, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    chunks = json.load(open(corpus_json, encoding="utf8"))
    texts = [c["text"] for c in chunks]
    ids = [c["id"] for c in chunks]

    # lexical
    tokenized = [t.lower().split() for t in texts]
    bm25 = BM25Okapi(tokenized)

    # semantic
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embs = model.encode(texts, show_progress_bar=True, convert_to_numpy=True, normalize_embeddings=True)
    index = faiss.IndexFlatIP(embs.shape[1])
    index.add(embs.astype(np.float32))

    np.save(os.path.join(out_dir, "embs.npy"), embs)
    json.dump(chunks, open(os.path.join(out_dir, "chunks.json"), "w", encoding="utf8"), ensure_ascii=False)
    json.dump(ids, open(os.path.join(out_dir, "ids.json"), "w", encoding="utf8"))
    bm25_dump = {
        "ids": ids,
        "tokenized": tokenized
    }
    json.dump(bm25_dump, open(os.path.join(out_dir, "bm25.json"), "w", encoding="utf8"))
    faiss.write_index(index, os.path.join(out_dir, "faiss.index"))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
```

Retriever with hybrid scoring and simple rerank.
You can replace the rerank with your favorite cross encoder later.

```python
# index/retrieve.py
import json, numpy as np, faiss
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

class HybridRetriever:
    def __init__(self, idx_dir):
        self.chunks = json.load(open(f"{idx_dir}/chunks.json", encoding="utf8"))
        ids = json.load(open(f"{idx_dir}/ids.json"))
        bm = json.load(open(f"{idx_dir}/bm25.json", encoding="utf8"))
        self.ids = ids
        self.bm25 = BM25Okapi(bm["tokenized"])
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index = faiss.read_index(f"{idx_dir}/faiss.index")
        self.embs = np.load(f"{idx_dir}/embs.npy")

    def retrieve(self, q, topk=12):
        toks = q.lower().split()
        bm_scores = self.bm25.get_scores(toks)
        bm_top = np.argsort(bm_scores)[::-1][:topk*4]

        qv = self.model.encode([q], normalize_embeddings=True)
        sims, idxs = self.index.search(qv.astype(np.float32), topk*4)
        sem_top = idxs[0]

        # intersect then union
        cand = list(set(bm_top).intersection(set(sem_top)))
        if len(cand) < topk:
            cand = list(set(list(bm_top) + list(sem_top)))
        # simple rerank by cosine against query vector
        cand = np.array(cand)
        scores = (self.embs[cand] @ qv[0])
        order = np.argsort(scores)[::-1][:topk]
        picks = cand[order]

        out = []
        for i, ix in enumerate(picks):
            c = self.chunks[ix]
            out.append({
                "id": c["id"], "text": c["text"],
                "score": float(scores[order][i])
            })
        return out
```

---

## 3. Guard the answer and write a trace (Python)

You can use any LLM. The guard is model agnostic.

```bash
pip install openai  # or any client you prefer
```

```python
# pipeline/answer_py.py
import json, time, os
from index.retrieve import HybridRetriever
from typing import List, Dict
from openai import OpenAI

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")  # example. replace as needed
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    out = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )
    return out.choices[0].message.content.strip()

def build_prompt(question: str, chunks: List[Dict]) -> str:
    ctx = "\n\n".join(f"[{c['id']}] {c['text']}" for c in chunks)
    return (
        "Use only the evidence. If not provable, reply exactly: not in context.\n"
        "Answer format:\n"
        "- claim\n- citations: [id,...]\n\n"
        f"Question: {question}\n\nEvidence:\n{ctx}\n"
    )

def answer(question: str, retriever: HybridRetriever, topk=8) -> Dict:
    chunks = retriever.retrieve(question, topk=topk)
    prompt = build_prompt(question, chunks)
    txt = call_llm(prompt)

    ok = "not in context" in txt.lower() or "citations:" in txt.lower()
    record = {
        "ts": int(time.time()),
        "q": question,
        "chunks": [{"id": c["id"], "score": c["score"]} for c in chunks],
        "answer": txt,
        "ok": ok
    }
    os.makedirs("runs", exist_ok=True)
    with open("runs/trace.jsonl", "a", encoding="utf8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record

if __name__ == "__main__":
    import sys
    retriever = HybridRetriever(sys.argv[1])
    print(answer(sys.argv[2], retriever))
```

Run end to end.

```bash
python tools/extract_pdf.py your.pdf data/pages.json
python tools/chunk.py data/pages.json data/chunks.json
python index/build.py data/chunks.json index_out
OPENAI_API_KEY=sk-... python pipeline/answer_py.py index_out "What is the author’s definition of X and on which page?"
```

---

## 4. Node.js variant

Install minimal tools.

```bash
npm install node-fetch @xenova/transformers faiss-node bm25
```

Simple hybrid retriever.
`@xenova/transformers` runs CPU embeddings in process. For large corpora, precompute and store embeddings offline.

```js
// index/retrieve.js
import { pipeline } from "@xenova/transformers";
import faiss from "faiss-node";
import fs from "node:fs";

export class HybridRetriever {
  constructor(dir) {
    this.chunks = JSON.parse(fs.readFileSync(`${dir}/chunks.json`, "utf8"));
    this.ids = JSON.parse(fs.readFileSync(`${dir}/ids.json`, "utf8"));
    this.embs = Float32Array.from(
      Object.values(JSON.parse(fs.readFileSync(`${dir}/embs.json`, "utf8")))
    );
    this.d = this.embs.length / this.ids.length;
    this.index = new faiss.IndexFlatIP(this.d);
    this.index.add(this.embs);
  }
  async init() {
    this.embed = await pipeline("feature-extraction", "Xenova/all-MiniLM-L6-v2");
  }
  async retrieve(q, topk = 12) {
    const out = await this.embed(q, { pooling: "mean", normalize: true });
    const qv = Float32Array.from(out.data);
    const { distances, labels } = this.index.search(qv, topk * 2);
    const picks = labels.slice(0, topk);
    return picks.map((ix, i) => ({
      id: this.chunks[ix].id,
      text: this.chunks[ix].text,
      score: distances[i]
    }));
  }
}
```

Guarded answer with your LLM client.

```js
// pipeline/answer_node.js
import fs from "node:fs";
import fetch from "node-fetch";
import { HybridRetriever } from "../index/retrieve.js";

async function callLLM(prompt) {
  const r = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: process.env.OPENAI_MODEL || "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }],
      temperature: 0
    })
  });
  const j = await r.json();
  return j.choices[0].message.content.trim();
}

function buildPrompt(question, chunks) {
  const ctx = chunks.map(c => `[${c.id}] ${c.text}`).join("\n\n");
  return `Use only the evidence. If not provable, reply exactly: not in context.
Answer format:
- claim
- citations: [id,...]

Question: ${question}

Evidence:
${ctx}
`;
}

export async function answer(indexDir, question) {
  const retr = new HybridRetriever(indexDir);
  await retr.init();
  const chunks = await retr.retrieve(question, 8);
  const prompt = buildPrompt(question, chunks);
  const txt = await callLLM(prompt);
  const ok = txt.toLowerCase().includes("not in context") || txt.includes("citations");

  const rec = {
    ts: Date.now(),
    q: question,
    chunks: chunks.map(c => ({ id: c.id, score: c.score })),
    answer: txt,
    ok
  };
  fs.mkdirSync("runs", { recursive: true });
  fs.appendFileSync("runs/trace.jsonl", JSON.stringify(rec) + "\n");
  return rec;
}

// run: node pipeline/answer_node.js index_out "your question"
if (import.meta.url === `file://${process.argv[1]}`) {
  answer(process.argv[2], process.argv.slice(3).join(" ")).then(x => console.log(x));
}
```

---

## 5. Evaluation harness

Create ten questions with ground truth spans. Keep the spans inside your chunks to avoid ambiguity.

```json
// eval/qaset.json
[
  {
    "qid": "q1",
    "q": "State the definition of X and cite the page.",
    "gold_ids": ["p12#2", "p12#3"],
    "gold_answer_contains": ["X is ..."]
  }
]
```

Scorer.

```python
# eval/score.py
import json, re, sys

def norm(s):
    return re.sub(r'\W+', ' ', s.lower()).strip()

def score(run_file, qaset):
    preds = [json.loads(l) for l in open(run_file, encoding="utf8")]
    gold = {q["qid"]: q for q in json.load(open(qaset, encoding="utf8"))}
    ok, refuse, cite_hit, n = 0, 0, 0, 0
    for p in preds:
        n += 1
        if "not in context" in p["answer"].lower():
            refuse += 1
        # citation overlap
        qid = p.get("qid", f"q{n}")
        g = gold.get(qid)
        if g:
            cites = {c["id"] for c in p["chunks"]}
            if set(g["gold_ids"]) & cites:
                cite_hit += 1
            if all(norm(x) in norm(p["answer"]) for x in g["gold_answer_contains"]):
                ok += 1
    return {"n": n, "exact_like": ok, "refusal": refuse, "cite_hit": cite_hit}

if __name__ == "__main__":
    print(score(sys.argv[1], sys.argv[2]))
```

Run a baseline then the guarded pipeline. Compare `exact_like`, `refusal`, and `cite_hit`.
Expect the guarded version to increase refusal when information is missing. That is good. It means fewer fabricated answers.

---

## 6. Recipes for common failures and how to fix them

These map directly to Problem Map items.

**No.1 Hallucination and Chunk Drift**
Symptoms

* Answers include facts that are near the topic but not in your chunks.
  Fix
* Reduce chunk size to keep entity and constraint within the same chunk.
* Use intersection of BM25 and embeddings then rerank by cosine.
* Keep a strict answer template and allow refusal.

**No.2 Query Parsing and Intent Split**
Symptoms

* Multi part questions pull only one sub topic.
  Fix
* Split questions on explicit markers. Run retrieval per subquestion. Merge results.
* Rerank with a feature that rewards coverage across sub parts.

**No.3 Index Schema Drift**
Symptoms

* Chunks produced with a different preprocessor than the one used at query time.
  Fix
* Store chunker version and tokenization rule with the index. Refuse to answer if version mismatch.

**No.4 Over Retrieval and Tail Noise**
Symptoms

* Too many low score chunks enter the prompt and drown the relevant ones.
  Fix
* Hard cut after the score knee. Never include tail beyond top 20 before rerank and top 8 after rerank.

**No.11 Symbolic Collapse**
Symptoms

* Pipeline marks success while storage or catalog updates failed. Users later see missing answers or duplicates.
  Fix
* Make commit of offsets or cursors contingent on durable writes.
* Example in Python

```python
def flush_and_commit(batch):
    try:
        write(batch)
        update_catalog()
        return next_offset()      # expose N+1 only after both steps succeed
    except Exception:
        return None               # block commit so batch replays
```

**No.14 Bootstrap Ordering**
Symptoms

* Components start in the wrong order and initial calls see empty resources.
  Fix
* Warm the retriever and embedding model before serving the first query.
* Cache the model and index in memory with a readiness flag.

```python
class Service:
    def __init__(self):
        self.ready = False
    def warm(self):
        self.retr = HybridRetriever("index_out")
        _ = self.retr.retrieve("warmup", 1)
        self.ready = True
```

---

## 7. Operational guidance

* Store `runs/trace.jsonl` in your logs. Add query id and user id if appropriate.

* Sample one in ten queries for manual inspection.

* Track these metrics

  * refusal rate
  * citation overlap rate
  * first token latency
  * rerank time
  * chunk size distribution

* Capacity

  * FAISS flat inner product on CPU handles tens of thousands of chunks easily.
  * For millions of chunks, move to IVF or HNSW and precompute embeddings offline.

---

## 8. Minimal quick start summary

```bash
# one time
pip install pypdf rank-bm25 sentence-transformers faiss-cpu rapidfuzz openai
python tools/extract_pdf.py your.pdf data/pages.json
python tools/chunk.py data/pages.json data/chunks.json
python index/build.py data/chunks.json index_out

# answering
OPENAI_API_KEY=sk-... python pipeline/answer_py.py index_out "Your question here"
# traces at runs/trace.jsonl
```

---

## 9. What to do if results are still unstable

Open an issue with three things. This makes triage fast and maps to the Problem Map.

1. The query and your expected answer.
2. The top 10 retrieved chunk ids and scores.
3. The generated answer.

We will tell you which Problem Map item it matches and give exact steps that apply to your repo.

---

## 10. Roadmap for practice oriented docs

We will add

* A small corpus with prebuilt index for quick experiments.
* Node scripts that mirror the Python chunker and builder.
* Optional cross encoder rerankers that still run on CPU.

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

