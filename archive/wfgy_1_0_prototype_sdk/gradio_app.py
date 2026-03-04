# Evaluation disclaimer (Gradio demo):
# Scores and labels shown in this app come from specific prompts, models and datasets.
# They are debugging aids, not scientific proof or product level guarantees.

import wfgy_sdk as w, numpy as np, gradio as gr
from wfgy_sdk.evaluator import compare_logits, pretty_print

def run_wfgy(prompt):
    logits = w.call_remote_model(prompt, model_id="gpt2")
    G = np.random.randn(128); G /= np.linalg.norm(G)
    I = G + np.random.normal(scale=0.05, size=128)
    out = w.get_engine().run(input_vec=I, ground_vec=G, logits=logits)
    m = compare_logits(logits, out)
    delta = (1 - m["std_ratio"]) * 100
    return f"variance drop {delta:.0f}% • KL {m['kl_divergence']:.2f}"

demo = gr.Interface(fn=run_wfgy,
                    inputs=gr.Textbox(),
                    outputs="textbox",
                    title="WFGY Quick Test",
                    description="Type any prompt. GPT-2 baseline, variance/KL will appear.")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
