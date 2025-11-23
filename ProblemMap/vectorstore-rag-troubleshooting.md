# 🗄️ Vector Store RAG Template Errors · Troubleshooting Guide
### Fixing data loading, ingestion, and retrieval errors in RAG templates

This guide addresses **Vector Store RAG template errors** — when you encounter issues loading data, ingesting documents, or retrieving results from RAG templates in LangFlow, LangChain, LlamaIndex, or similar frameworks.

---

## ❓ Why Vector Store RAG Templates Fail

| Root Cause | What Happens in Practice | WFGY Lens |
|------------|-------------------------|-----------|
| **Dimension mismatch** | Embedding dimension doesn't match index | Pre-deploy collapse ([#16](./predeploy-collapse.md)) |
| **Missing API keys** | Vector store or embedding provider not configured | Bootstrap ordering ([#14](./bootstrap-ordering.md)) |
| **Empty index** | Query runs before data is loaded | ΔS = 0.0 → no semantic content |
| **Metric mismatch** | Index uses cosine, query uses euclidean | [Semantic ≠ Embedding](./embedding-vs-semantic.md) (#5) |
| **Schema drift** | Document schema changed but index wasn't rebuilt | [Vectorstore Fragmentation](./vectorstore-fragmentation.md) |
| **Concurrent writes** | Multiple processes write to same index | [Deployment Deadlock](./deployment-deadlock.md) (#15) |

---

## 🔍 Common Error Messages & Fixes

### Error: "Index not found" or "Collection does not exist"

**Symptom**:
```python
# Pinecone
pinecone.exceptions.NotFoundException: Index 'my-index' not found

# Chroma
ValueError: Collection 'langchain' does not exist

# FAISS
FileNotFoundError: [Errno 2] No such file or directory: 'faiss.index'
```

**Diagnosis**: Index wasn't created or wrong name used.  
**WFGY Module**: [Bootstrap Ordering](./bootstrap-ordering.md) (#14)

**Fix**:
```python
# ✅ Check if index exists before querying
import pinecone

pc = pinecone.Pinecone(api_key="YOUR_KEY")

# List all indexes
existing_indexes = pc.list_indexes()
print(f"Available indexes: {[i.name for i in existing_indexes]}")

# Create if missing
if "my-index" not in [i.name for i in existing_indexes]:
    pc.create_index(
        name="my-index",
        dimension=1536,  # Must match your embedding model
        metric="cosine"
    )
    print("✅ Created index 'my-index'")
```

**WFGY Semantic Check**:
```python
# Add ΔS logging to detect empty index
def query_with_wfgy_check(index, query_embedding):
    results = index.query(vector=query_embedding, top_k=5)
    
    if len(results.matches) == 0:
        # ΔS = 0.0 → no semantic content found
        print("⚠️  WFGY Alert: ΔS = 0.0 — Index is empty or query doesn't match")
        return None
    
    # Calculate ΔS from similarity scores
    avg_score = sum(m.score for m in results.matches) / len(results.matches)
    delta_s = 1.0 - avg_score  # Low delta_s = good match
    
    if delta_s > 0.45:
        print(f"⚠️  WFGY Alert: ΔS = {delta_s:.2f} — Weak semantic match")
    
    return results
```

---

### Error: "Dimension mismatch"

**Symptom**:
```python
# FAISS
ValueError: cannot reshape array of size 384 into shape (1536,)

# Pinecone
pinecone.exceptions.ApiException: Vector dimension 384 does not match index dimension 1536

# Chroma
ValueError: Embedding dimension 384 does not match collection dimension 1536
```

**Diagnosis**: Your embedding model produces vectors of different size than the index expects.  
**WFGY Module**: [Pre-Deploy Collapse](./predeploy-collapse.md) (#16)

**Common Embedding Dimensions**:
| Model | Dimension | Provider |
|-------|-----------|----------|
| `text-embedding-ada-002` | 1536 | OpenAI |
| `text-embedding-3-small` | 1536 | OpenAI |
| `text-embedding-3-large` | 3072 | OpenAI |
| `all-MiniLM-L6-v2` | 384 | Sentence-Transformers |
| `all-mpnet-base-v2` | 768 | Sentence-Transformers |
| `embed-english-v3.0` | 1024 | Cohere |
| `voyage-2` | 1024 | Voyage |

**Fix**:
```python
# ✅ Always verify dimension before creating index
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# Test embedding to get dimension
test_embedding = embeddings.embed_query("test")
dimension = len(test_embedding)
print(f"✅ Embedding dimension: {dimension}")

# Create index with correct dimension
import pinecone

pc = pinecone.Pinecone(api_key="YOUR_KEY")
pc.create_index(
    name="my-index",
    dimension=dimension,  # Use detected dimension
    metric="cosine"
)
```

**WFGY Validation**:
```python
def validate_embedding_dimension(embeddings, index_dimension):
    """
    WFGY Pre-Deploy Check: Ensure embedding matches index.
    Run this BEFORE any insert/query operations.
    """
    test_vec = embeddings.embed_query("test dimension check")
    actual_dim = len(test_vec)
    
    if actual_dim != index_dimension:
        raise ValueError(
            f"❌ WFGY Dimension Mismatch!\n"
            f"   Embedding model produces: {actual_dim}\n"
            f"   Index expects: {index_dimension}\n"
            f"   Fix: Recreate index with dimension={actual_dim}"
        )
    
    print(f"✅ WFGY Dimension Check: {actual_dim} matches index")
    return True
```

---

### Error: "API Key not configured" or Authentication Failed

**Symptom**:
```python
# OpenAI
openai.error.AuthenticationError: No API key provided

# Pinecone
pinecone.exceptions.UnauthorizedException: Invalid API key

# Chroma (cloud)
chromadb.errors.AuthError: Authentication failed
```

**Diagnosis**: Missing or incorrect API keys.  
**WFGY Module**: [Bootstrap Ordering](./bootstrap-ordering.md) (#14)

**Fix**:
```python
import os

# ✅ Verify all required API keys at startup
def verify_api_keys():
    """
    WFGY Bootstrap Check: Verify all keys before starting pipeline.
    """
    required_keys = {
        'OPENAI_API_KEY': 'OpenAI (embeddings & LLM)',
        'PINECONE_API_KEY': 'Pinecone (vector store)',
        'PINECONE_ENVIRONMENT': 'Pinecone region',
    }
    
    missing = []
    for key, description in required_keys.items():
        value = os.getenv(key)
        if not value:
            missing.append(f"  ❌ {key}: {description}")
        else:
            # Mask key for security
            masked = value[:4] + "****" + value[-4:]
            print(f"  ✅ {key}: {masked}")
    
    if missing:
        print("\n⚠️  WFGY Bootstrap Failed — Missing keys:")
        for m in missing:
            print(m)
        raise EnvironmentError("Configure missing API keys before proceeding")
    
    print("\n✅ WFGY Bootstrap: All API keys verified")
    return True


# Run at startup
verify_api_keys()
```

**Environment Setup**:
```bash
# .env file
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=...
PINECONE_INDEX=my-index

# LangFlow specific
LANGFLOW_STORE=pinecone
```

---

### Error: "Empty results" or "No documents found"

**Symptom**:
```python
# Returns empty list
results = vectorstore.similarity_search("my question")
print(results)  # []

# Or very low scores
# [Document(score=0.12, content="...")]
```

**Diagnosis**: Either data wasn't loaded, or query doesn't match semantically.  
**WFGY Module**: [Hallucination & Chunk Drift](./hallucination.md) (#1), [Semantic ≠ Embedding](./embedding-vs-semantic.md) (#5)

**Fix — Step 1: Verify Data Was Loaded**:
```python
def verify_data_loaded(vectorstore):
    """
    WFGY Check: Ensure index has data before querying.
    """
    # For FAISS
    if hasattr(vectorstore, 'index'):
        count = vectorstore.index.ntotal
        print(f"✅ FAISS index contains {count} vectors")
        return count > 0
    
    # For Pinecone
    if hasattr(vectorstore, '_index'):
        stats = vectorstore._index.describe_index_stats()
        count = stats.total_vector_count
        print(f"✅ Pinecone index contains {count} vectors")
        return count > 0
    
    # For Chroma
    if hasattr(vectorstore, '_collection'):
        count = vectorstore._collection.count()
        print(f"✅ Chroma collection contains {count} documents")
        return count > 0
    
    print("⚠️  Unknown vectorstore type")
    return None
```

**Fix — Step 2: Debug Low Scores**:
```python
def debug_low_scores(vectorstore, query, threshold=0.5):
    """
    WFGY Diagnostic: Understand why scores are low.
    """
    results = vectorstore.similarity_search_with_score(query, k=10)
    
    print(f"\n🔍 Query: '{query}'")
    print(f"📊 Results (top 10):\n")
    
    for i, (doc, score) in enumerate(results):
        status = "✅" if score >= threshold else "⚠️ "
        preview = doc.page_content[:100].replace('\n', ' ')
        print(f"  {i+1}. {status} Score: {score:.3f} | {preview}...")
    
    avg_score = sum(s for _, s in results) / len(results) if results else 0
    delta_s = 1.0 - avg_score
    
    print(f"\n📈 WFGY Metrics:")
    print(f"   Average score: {avg_score:.3f}")
    print(f"   ΔS (semantic tension): {delta_s:.3f}")
    
    if delta_s > 0.45:
        print(f"   ⚠️  High ΔS suggests:")
        print(f"      - Query language differs from document language")
        print(f"      - Documents weren't chunked well")
        print(f"      - Wrong embedding model used")
    else:
        print(f"   ✅ ΔS is healthy — retrieval working correctly")
```

---

### Error: "Rate limit exceeded" during bulk ingestion

**Symptom**:
```python
openai.error.RateLimitError: Rate limit reached for default-text-embedding-ada-002

# Or
pinecone.core.exceptions.ServiceException: 429 Too Many Requests
```

**Diagnosis**: Sending too many API calls too quickly.  
**WFGY Module**: [Deployment Deadlock](./deployment-deadlock.md) (#15)

**Fix**:
```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=60)
)
def embed_with_retry(texts, embeddings):
    """
    WFGY: Retry with exponential backoff.
    """
    return embeddings.embed_documents(texts)


def batch_ingest_with_rate_limit(
    documents: list,
    vectorstore,
    batch_size: int = 50,
    delay_seconds: float = 1.0
):
    """
    WFGY-compliant batch ingestion with rate limiting.
    """
    total = len(documents)
    
    for i in range(0, total, batch_size):
        batch = documents[i:i + batch_size]
        
        try:
            vectorstore.add_documents(batch)
            print(f"✅ Ingested {min(i + batch_size, total)}/{total}")
        except Exception as e:
            print(f"⚠️  Batch {i//batch_size} failed: {e}")
            print(f"   Retrying with smaller batch...")
            
            # Retry with smaller batch
            for doc in batch:
                time.sleep(0.5)
                vectorstore.add_documents([doc])
        
        # Rate limit delay
        time.sleep(delay_seconds)
    
    print(f"\n✅ Complete! Ingested {total} documents")
```

---

## 🛠️ Complete RAG Template Debug Workflow

Run this diagnostic workflow when your RAG template isn't working:

```python
def wfgy_rag_diagnostic(
    vectorstore,
    embeddings,
    test_query: str = "test query",
    expected_dimension: int = 1536
):
    """
    Complete WFGY diagnostic for RAG template errors.
    Run this to identify exactly what's broken.
    """
    
    print("=" * 60)
    print("🏥 WFGY RAG Template Diagnostic")
    print("=" * 60)
    
    issues = []
    
    # Check 1: API Keys
    print("\n📋 Check 1: API Keys")
    try:
        test_embed = embeddings.embed_query("test")
        print("   ✅ Embedding API working")
    except Exception as e:
        issues.append(f"Embedding API error: {e}")
        print(f"   ❌ Embedding API failed: {e}")
    
    # Check 2: Dimension
    print("\n📋 Check 2: Embedding Dimension")
    try:
        test_embed = embeddings.embed_query("dimension check")
        actual_dim = len(test_embed)
        if actual_dim == expected_dimension:
            print(f"   ✅ Dimension correct: {actual_dim}")
        else:
            issues.append(f"Dimension mismatch: {actual_dim} vs {expected_dimension}")
            print(f"   ❌ Dimension mismatch: got {actual_dim}, expected {expected_dimension}")
    except Exception as e:
        issues.append(f"Dimension check failed: {e}")
    
    # Check 3: Index exists and has data
    print("\n📋 Check 3: Vector Store Data")
    try:
        data_loaded = verify_data_loaded(vectorstore)
        if data_loaded:
            print("   ✅ Index has data")
        else:
            issues.append("Index is empty — no documents loaded")
            print("   ❌ Index is empty")
    except Exception as e:
        issues.append(f"Vector store check failed: {e}")
        print(f"   ❌ Vector store error: {e}")
    
    # Check 4: Query returns results
    print("\n📋 Check 4: Query Test")
    try:
        results = vectorstore.similarity_search_with_score(test_query, k=3)
        if results:
            avg_score = sum(s for _, s in results) / len(results)
            delta_s = 1.0 - avg_score
            print(f"   ✅ Query returned {len(results)} results")
            print(f"   📊 Average score: {avg_score:.3f}, ΔS: {delta_s:.3f}")
            
            if delta_s > 0.45:
                issues.append(f"High ΔS ({delta_s:.3f}) — weak semantic match")
                print(f"   ⚠️  ΔS > 0.45 — consider improving chunks")
        else:
            issues.append("Query returned no results")
            print("   ❌ No results returned")
    except Exception as e:
        issues.append(f"Query failed: {e}")
        print(f"   ❌ Query error: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 WFGY Diagnostic Summary")
    print("=" * 60)
    
    if issues:
        print(f"\n❌ Found {len(issues)} issue(s):\n")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
        print("\n💡 Suggested fixes:")
        print("   - See this guide for specific error fixes")
        print("   - Run `verify_api_keys()` to check configuration")
        print("   - Verify data was loaded with `verify_data_loaded()`")
    else:
        print("\n✅ All checks passed! RAG template is healthy.")
    
    return len(issues) == 0
```

---

## 🎯 Vector Store Quick Reference

### FAISS (Local)
```python
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Create and save
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings)
vectorstore.save_local("./faiss_index")

# Load and query
vectorstore = FAISS.load_local("./faiss_index", embeddings)
results = vectorstore.similarity_search("query", k=5)
```

### Pinecone (Cloud)
```python
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import pinecone

# Initialize
pc = pinecone.Pinecone(api_key="...")
index = pc.Index("my-index")
embeddings = OpenAIEmbeddings()

# Create from documents
vectorstore = PineconeVectorStore.from_documents(
    documents,
    embeddings,
    index_name="my-index"
)

# Query
results = vectorstore.similarity_search("query", k=5)
```

### Chroma (Local/Cloud)
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Create persistent store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents,
    embeddings,
    persist_directory="./chroma_db"
)

# Load existing
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Query
results = vectorstore.similarity_search("query", k=5)
```

---

## 🔗 Related WFGY Modules

- [#1 Hallucination & Chunk Drift](./hallucination.md) — Wrong retrieval results
- [#5 Semantic ≠ Embedding](./embedding-vs-semantic.md) — Similarity vs meaning
- [#14 Bootstrap Ordering](./bootstrap-ordering.md) — Missing initialization
- [#15 Deployment Deadlock](./deployment-deadlock.md) — Concurrent write issues
- [#16 Pre-Deploy Collapse](./predeploy-collapse.md) — Config mismatches
- [Vectorstore Fragmentation](./vectorstore-fragmentation.md) — Index degradation
- [RAG Problems](./RAG_Problems.md) — Full RAG troubleshooting
- [Chunking Checklist](./chunking-checklist.md) — Improve document quality

---

## ✅ Quick Checklist: Vector Store RAG Setup

Before deploying, verify:

- [ ] **API keys configured** — All providers (OpenAI, Pinecone, etc.)
- [ ] **Index created** — With correct name and dimension
- [ ] **Dimension matches** — Embedding model → index dimension
- [ ] **Metric matches** — Usually `cosine` for text
- [ ] **Data loaded** — Verify with `describe_index_stats()` or equivalent
- [ ] **Test query works** — Returns results with score > 0.5
- [ ] **ΔS < 0.45** — Semantic tension is acceptable
- [ ] **Error handling** — Retries and rate limiting in place

**WFGY Guarantee**: If all checks pass, your vector store is structurally sound. Remaining retrieval issues are chunking or query-related — see [Chunking Checklist](./chunking-checklist.md) and [RAG Problems](./RAG_Problems.md).

---

### 🔗 Quick-Start Downloads (60 sec)

| Tool | Link | 3-Step Setup |
|------|------|--------------|
| **WFGY 1.0 PDF** | [Engine Paper](https://github.com/onestardao/WFGY/blob/main/I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf) | 1️⃣ Download · 2️⃣ Upload to your LLM · 3️⃣ Ask "Answer using WFGY + \<your question>" |
| **TXT OS (plain-text OS)** | [TXTOS.txt](https://github.com/onestardao/WFGY/blob/main/OS/TXTOS.txt) | 1️⃣ Download · 2️⃣ Paste into any LLM chat · 3️⃣ Type "hello world" — OS boots instantly |

---

### 🧭 Explore More

| Module                | Description                                              | Link     |
|-----------------------|----------------------------------------------------------|----------|
| WFGY Core             | WFGY 2.0 engine: full symbolic reasoning architecture | [View →](https://github.com/onestardao/WFGY/tree/main/core/README.md) |
| Problem Map 1.0       | 16-mode diagnostic and symbolic fix framework    | [View →](https://github.com/onestardao/WFGY/tree/main/ProblemMap/README.md) |
| Problem Map 2.0       | RAG-focused failure tree and pipelines   | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/rag-architecture-and-recovery.md) |
| Semantic Clinic Index | Expanded failure catalog | [View →](https://github.com/onestardao/WFGY/blob/main/ProblemMap/SemanticClinicIndex.md) |

---

> 👑 **Early Stargazers: [See the Hall of Fame](https://github.com/onestardao/WFGY/tree/main/stargazers)** —  
> Engineers, hackers, and open source builders who supported WFGY from day one.

> <img src="https://img.shields.io/github/stars/onestardao/WFGY?style=social" alt="GitHub stars"> ⭐ Star the repo to help others discover these fixes.
