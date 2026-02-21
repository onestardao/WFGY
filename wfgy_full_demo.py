import io, numpy as np, matplotlib.pyplot as plt
from wfgy_sdk import get_engine
from wfgy_sdk.evaluator import compare_logits, pretty_print, plot_histogram
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "sshleifer/tiny-gpt2"
tok   = AutoTokenizer.from_pretrained(MODEL)
mdl   = AutoModelForCausalLM.from_pretrained(MODEL)
eng   = get_engine()

def one_pass(prompt: str):
    toks = tok(prompt, return_tensors="pt")
    rawL = mdl(**toks).logits[0, -1].detach().cpu().numpy()

    # demo-only vectors
    G = np.random.randn(256).astype(np.float32)
    I = G + np.random.normal(scale=0.05, size=256).astype(np.float32)

    modL = eng.run(I, G, rawL)
    m    = compare_logits(rawL, modL)

    print("\n## Metrics\n")
    print(pretty_print(m))

    # Save histogram
    fig = plot_histogram(rawL, modL)
    fig.savefig("hist.png")
    print("\n![hist](hist.png)")

if __name__ == "__main__":
    one_pass("Summarise Gödel's Incompleteness in one sentence!")
