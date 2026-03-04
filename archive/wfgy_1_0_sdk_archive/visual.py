# visual.py
# Optional histogram plot (CPU only)

import numpy as np, matplotlib.pyplot as plt

def plot_histogram(logits_before: np.ndarray, logits_after: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(logits_before, bins=60, alpha=0.4, label="before")
    ax.hist(logits_after,  bins=60, alpha=0.4, label="after")
    ax.set_title("Logit Distribution Before vs After WFGY")
    ax.legend()
    plt.show()
