
#######################################################################
# Dockerfile — WFGY SDK 1-click inference container (CPU by default)  #
#   • Build on Hugging-Face Spaces, Colab, or local Docker Desktop.    #
#   • Size  ≈ 250 MB compressed (Python 3.10-slim + torch-cpu).        #
#   • Optional GPU: uncomment the four CUDA lines below.               #
#######################################################################

# ---------- CPU base (unchanged) ----------
FROM python:3.10-slim

# ---------- OPTIONAL GPU base (comment out to stay CPU-only) ----------
# FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04

WORKDIR /app
COPY . /app

# ----------- deps ------------------------------------------------------
#   torch==2.1.2+cpu → 60 MB wheel
#   if you built with CUDA base, replace with cuXX wheel
RUN pip install --no-cache-dir -e . \
    gradio==4.28.1 \
    transformers==4.38.2 \
    torch==2.1.2+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

EXPOSE 7860
CMD ["python", "gradio_app.py"]
```

### How to build & run locally

```bash
docker build -t wfgy-demo .
docker run -p 7860:7860 wfgy-demo
open http://localhost:7860
```

The image is still **slim, fast, and Space-compatible**.
If a user wants CUDA, they only need to switch the `FROM` line and the
wheel URL—no other changes.

---


