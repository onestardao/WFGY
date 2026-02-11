<!--
AI NOTE (WFGY 3.0 TU Experiment Anchor)

This file is part of the WFGY 3.0 "Tension Universe" experiment collection.
Main hub for context and navigation:
https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md

Problem ID: TU Q127 (Synthetic Worlds and Data Entropy).
Role: MVP experiment log for Q127 at the effective layer. Focus on synthetic worlds,
      label entropy and entropy–aware tension observables.
Use: When a user asks about TU Q127 synthetic world or data entropy experiments, or wants
      runnable examples, load this page first, then follow its notebook links.
-->

# TU Q127 MVP: synthetic worlds and data entropy

_Status: first MVP experiment completed. This page will expand as the TU Q127 program evolves._

> This page documents the first effective-layer MVP experiment for TU Q127.  
> It does **not** claim that Q127 is solved as a mathematical problem or as a full benchmark.  
> The script is short and fully inspectable. You can re-run it line by line or use the
> Colab one-click notebook to reproduce the qualitative pattern.

**Navigation**

- [← Back to Experiments index](../README.md)  
- [← Back to Event Horizon (WFGY 3.0)](../../EventHorizon/README.md)

---

## 0. What this page is about

TU Q127 studies how truth, data entropy and synthetic worlds interact.  
In the Tension Universe picture we do not start from a fixed “real dataset”.  
Instead we explicitly design small worlds with known generative rules and then ask

- how a model trained on these worlds encodes “truth”,  
- how much of that truth is visible from simple observables at the effective layer,  
- how tension grows when the same model is moved between worlds with different entropy.

This page currently ships one concrete MVP experiment:

- **Experiment A · three synthetic worlds and an entropy gap.**

Additional Q127 variants (for example more world families or LLM-based probes) are reserved
for future iterations and will be linked from the Experiments index when they come online.

The canonical S-problem statement and the full TU Q127 formalism live in the BlackHole Q127
entry. This page is only a practical notebook-style companion that records how the first
experiment was actually run.

---

## 1. Experiment A: three synthetic worlds and an entropy gap

### 1.1 Research question

If we construct three very small synthetic worlds, each with

- a different class balance, and  
- a different pattern of label noise,

can we define a one-dimensional observable `T_entropy` that

- separates the worlds in a stable way, and  
- exposes when a trained classifier is carrying the *wrong* world in its internal beliefs?

The question is intentionally small. We are not trying to model any real domain.  
We only want to see whether a scalar effective-layer observable can track a simple entropy gap.

---

### 1.2 Setup

At a high level the script does the following.

- Generates three tiny synthetic worlds called `W1`, `W2` and `W3`.  

  Each world is a simple binary classification problem in a two-dimensional real space (R²)
  with Gaussian blobs.

  - `W1_balanced_clean`  
    - balanced classes, prior₁ ≈ 0.50  
    - no label noise  
    - empirical label entropy `H_label ≈ 1.000 bits`, noise entropy `H_noise ≈ 0.000 bits`.  

  - `W2_imbalanced_clean`  
    - imbalanced classes, prior₁ ≈ 0.90, prior₀ ≈ 0.10  
    - no label noise  
    - empirical label entropy `H_label ≈ 0.505 bits`, noise entropy `H_noise ≈ 0.000 bits`.  

  - `W3_balanced_noisy`  
    - balanced prior, but labels are flipped with probability 0.20  
    - empirical label entropy `H_label ≈ 1.000 bits`, noise entropy `H_noise ≈ 0.722 bits`.

- Trains a small classifier on **one world at a time**.  

  The default version in the code uses a compact two-layer MLP implemented in PyTorch.  
  There is a single training loop per world with fixed hyper-parameters.  
  We do not tune the model for each run.

- Evaluates each trained classifier on **all three** worlds.  

  For each pair `(train_world, test_world)` the script records

  - the predicted probability `p̂(y = 1 | x)` for each sample,  
  - the empirical label distribution under the model,  
  - the empirical cross-entropy between model predictions and the true labels,  
  - the KL divergence between the model label distribution and the world label distribution.

- Defines a simple effective-layer observable `T_entropy(train_world → test_world)`.

  In plain language:

  - `T_entropy` increases when the average test cross-entropy is high  
    (`ce_bits` in the code),  
  - `T_entropy` increases when the KL divergence between model labels and world labels is high  
    (`kl_bits`),  
  - `T_entropy` also increases when the absolute difference in label entropies  
    `|H_label(train_world) − H_label(test_world)|` is large (`deltaH`).  

  The relative strength of these three pieces is controlled by fixed positive weights  
  `b_ce`, `b_kl` and `b_deltaH` inside the script.  
  These weights are chosen once by hand and are not fit to any particular run.

- Treats effective-layer “correctness” in a lightweight way.  

  An evaluation is counted as correct if both

  - the classification accuracy on the test world is at least `0.8`, and  
  - the KL divergence between model labels and world labels is below a small threshold.

For every pair of worlds we therefore get a bundle

- accuracy, cross-entropy and KL divergence,  
- the scalar `T_entropy`,  
- a Boolean correctness flag.

That is enough to see whether the observable respects the world structure.

---

### 1.3 Representative results

A representative run with one TinyMLP per world and 500 samples per world produced the
following pattern. The console log and cross-world table look like this:

![Console log and cross-world table for Q127-A](./Q127A.png)

The main numbers (one row per train → test pair) follow the expected structure:

- **train and test on the same world** (diagonal pairs)  
  - accuracy above `0.90` on the clean worlds,  
  - KL divergence close to `0.0`,  
  - `T_entropy(W_i → W_i)` between roughly `0.02` and `0.06` for `W1` and `W2`,  
  - higher but still moderate tension for the noisy world `W3`.

- **mismatched worlds** show noticeably higher tension.  

  Examples from the same run:

  - `W1_balanced_clean → W2_imbalanced_clean`  
    - accuracy still acceptable,  
    - but the model keeps a roughly `0.5 / 0.5` internal label balance,  
    - KL to the true `0.1 / 0.9` world increases,  
    - `T_entropy` rises into the `0.20+` band.  

  - `W2_imbalanced_clean → W3_balanced_noisy`  
    - both class balance and noise structure are mismatched,  
    - `T_entropy` is among the highest entries in the table.

The same run can be visualised as a 3×3 heatmap of `T_entropy(train_world → test_world)`:

![Heatmap of T_entropy(train_world → test_world) for Q127-A](./Q127A2.png)

- The diagonal entries (train and test on the same world) are the darkest,  
  indicating low tension.  
- Off-diagonal entries become progressively brighter as the worlds diverge in class balance
  and noise, with the largest mismatch appearing as the brightest cell.

If we treat `T_entropy` as a crude world detector and simply pick

> the training world `W_i` that minimises `T_entropy(W_i → W_test)`,

this rule correctly recovers the origin world of a held-out batch in most trials of this
toy setup.

Plain-language interpretation:

- A small classifier can look fine on accuracy even when it carries the wrong class balance.  
- An entropy-aware observable makes the mismatch visible.  
- In this toy case the scalar `T_entropy` behaves like a “which world am I in?” probe:
  it is small when beliefs and world structure match, and larger when they do not.

None of these numbers are a benchmark.  
They will shift if you change the model, sample size or world definitions.  
The object of interest is the *pattern* and the fact that it is stable under small changes.

---

### 1.4 How to reproduce (single-cell Colab)

Experiment A is implemented as a single-cell notebook. You can either read the code directly
or run it end-to-end in Colab.

1. Open the notebook for the synthetic-worlds entropy experiment:

   - GitHub notebook: [`Q127_A.ipynb`](./Q127_A.ipynb)  
   - Run in Colab (one-click):  
     [![Open Q127-A in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q127_MVP/Q127_A.ipynb)

   The header inside the cell starts with  
   `WFGY 3.0 Singularity demo, Q127 Synthetic Worlds Entropy Gauge`.

2. Press **“Run all”** in Colab.  

   - The single code cell will install the required Python packages  
     (`numpy`, `pandas`, `matplotlib`, `torch`) in the current runtime,  
     generate the three synthetic worlds,  
     train one TinyMLP per world and evaluate all train → test pairs.  
   - On a standard free Colab CPU, a fresh run typically finishes within a couple of minutes.

3. Inspect the outputs.

   - The notebook prints the world definitions, cross-world table and scalar `T_entropy`
     for each train → test pair, similar to the screenshot above.  
   - At the end it draws the 3×3 heatmap of `T_entropy(train_world → test_world)`.

If you prefer not to run any code, the screenshots and numbers on this page already show the
qualitative behaviour of the observable.

---

## 2. How this MVP fits into Tension Universe

The TU Q127 S-problem defines a broader language for talking about synthetic worlds,  
truthful signals and entropy at the effective layer. That definition lives in the BlackHole
collection and does not depend on any particular model or Colab notebook.

This page is the first practical companion for that definition.

- It provides one effective-layer experiment showing how a small set of synthetic worlds  
  and a scalar observable `T_entropy` can already expose meaningful structure.  
- The code is intentionally short so that readers can audit every line and change the model,
  world definitions or observables as needed.  
- Future experiments for Q127 and for other S-problems will be added under
  `TensionUniverse/Experiments/` and linked from the Experiments index.

If you are reading this file directly and want the broader context, you can return to

- [Experiments index](../README.md) for the full list of TU experiments, and  
- [Event Horizon (WFGY 3.0)](../../EventHorizon/README.md) for the main entry point and
  narrative overview of the Tension Universe project.

---

### Charters and formal context

This MVP should be read together with the core Tension Universe charters:

- [TU Effective Layer Charter](../../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)  
- [TU Encoding and Fairness Charter](../../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)  
- [TU Tension Scale Charter](../../Charters/TU_TENSION_SCALE_CHARTER.md)

These charters define how effective-layer claims, encodings and tension scales are expected
to behave across the whole project. The experiment on this page is written to stay inside
those boundaries.
