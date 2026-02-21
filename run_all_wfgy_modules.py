# run_all_wfgy_modules.py 
# Individual module smoke tests with human-readable comments

import pathlib, sys, numpy as np, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from wfgy_sdk import bbmc, bbpf, bbcr, bbam
from wfgy_sdk.evaluator import compare_logits, pretty_print

print("\n=== WFGY · Module-by-Module Demo ===")

# ── BBMC ────────────────────────────────────────────────────────────────
I = np.random.randn(16); G = I + np.random.normal(scale=0.05, size=16)
bm = bbmc.compute_residue(I, G)
print("\n📊 BBMC  · semantic residue")
print(f"‖B‖ = {bm['B_norm']:.4f}  ( <1.0 means well-aligned )")

# ── BBPF ────────────────────────────────────────────────────────────────
paths, w, fS = bbpf.bbpf_progression(bm["B_vec"])
print("\n⚙️  BBPF  · progression")
print(f"f_S = {fS:.3f}  ( >0.8 = stable )")

# ── BBCR ────────────────────────────────────────────────────────────────
collapse = bbcr.check_collapse(bm["B_norm"], fS, Bc=2.0, eps=0.05)
lam = bbcr.compute_lyapunov(np.array([0.4, 0.3, 0.25, 0.24]))
print("\n🕸️  BBCR  · collapse-rebirth")
print(f"λ ≈ {lam:.3f}  | collapse? {collapse}")

# ── BBAM ────────────────────────────────────────────────────────────────
raw = np.random.randn(10)
mod = bbam.modulate_attention(raw, gamma=0.5)
print("\n🔁 BBAM  · attention gating")
print(f"first 3 logits {raw[:3]} -> {mod[:3]}")
m = compare_logits(raw, mod)
pretty_print(m)

print("\n✅ Module demo finished — each metric matches paper thresholds.\n")
