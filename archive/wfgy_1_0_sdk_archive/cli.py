# cli.py

# Evaluation disclaimer (WFGY CLI):
# Any evaluation commands in this CLI produce heuristic diagnostics for your local stack.
# They should not be treated as formal benchmarks or guarantees of model safety or quality.

import argparse, wfgy_sdk as w
from wfgy_sdk.evaluator import compare_logits, pretty_print
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="text prompt to test")
    parser.add_argument("--model", default="gpt2",
                        help="huggingface model id (public)")
    args = parser.parse_args()

    logits = w.call_remote_model(args.prompt, model_id=args.model)
    G = np.random.randn(128); G /= np.linalg.norm(G)
    I = G + np.random.normal(scale=0.05, size=128)

    logits_mod = w.get_engine().run(input_vec=I, ground_vec=G, logits=logits)
    pretty_print(compare_logits(logits, logits_mod))

if __name__ == "__main__":
    main()


