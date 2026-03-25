<!--
AI_NOTE_START

Document role:
This page is the entry page for the public case-studies layer of the current Inverse Atlas MVP.

What this page is for:
1. Turn raw smoke results into a guided case-study surface.
2. Help readers know which cases to read first.
3. Connect the public showcase layer with raw result artifacts and the Colab reproduction path.
4. Keep the evidence story readable without forcing people to inspect raw txt files directly.

How to use this page:
1. Read this page after the experiments entry page and showcase-cases page.
2. Start with the flagship cases first.
3. Use the raw result links only after you understand the story of a case.
4. Treat this page as the human-readable case-study index of the current smoke evidence layer.

Important boundary:
This page is a guided case-study index for the current smoke evidence layer.
It is not the full benchmark archive and not the final large-scale empirical report.
It exists to make the current MVP evidence surface readable and inspectable.

Recommended reading path:
1. Experiments
2. Repro in 60 Seconds
3. Phase Overview
4. Showcase Cases
5. Case Studies README
6. Individual Case Study Pages
7. Results and Current Findings
8. Evidence Snapshot

AI_NOTE_END
-->

# Case Studies 📚🧪

> The guided public evidence layer for the current Inverse Atlas smoke results

This page is the public entry point for the **case-studies layer** of the current Inverse Atlas MVP.

The purpose of this layer is simple:

**do not make readers dig through raw txt files to understand what matters**

The raw smoke outputs are useful, but most humans will not open a pile of result files and reconstruct the story by themselves.

So this case-studies layer exists to turn the current smoke evidence into something that is:

- readable
- teachable
- linkable
- challengeable
- easier to show in public

In simple terms:

- the raw result files are the evidence base
- the case studies are the guided reading surface

---

## Quick Links 🔎

| Section | Link |
|---|---|
| Inverse Atlas Home | [Inverse Atlas README](../../README.md) |
| Start Here | [Start Here](../../start-here.md) |
| FAQ | [FAQ](../../FAQ.md) |
| Experiments Home | [Experiments](../README.md) |
| Repro in 60 Seconds | [Repro in 60 Seconds](../repro-60-seconds.md) |
| Phase Overview | [Phase Overview](../phase-overview.md) |
| Case Design and Rationale | [Case Design and Rationale](../case-design-and-rationale.md) |
| Showcase Cases | [Showcase Cases](../showcase-cases.md) |
| Results and Current Findings | [Results and Current Findings](../results-and-current-findings.md) |
| Evidence Snapshot | [Evidence Snapshot](../evidence-snapshot.md) |
| Colab | [Colab](../../colab.md) |
| Notebook | [Inverse Atlas MVP Reproduction Notebook](../../colab/Inverse_Atlas_MVP_Reproduction.ipynb) |
| Runtime Layer | [Runtime Artifacts](../../runtime/README.md) |
| Advanced Version | [Inverse Atlas Advanced](../../runtime/inverse-advanced.txt) |
| Demo Harness | [Inverse Atlas Demo Harness](../../runtime/inverse-demo.txt) |
| Evaluator | [Inverse Atlas Evaluator](../../runtime/inverse-eval.txt) |

---

## The shortest version 🧩

If you only want the fastest correct reading path, start here:

1. [Smoke Case 04 · Neighboring-Cut Conflict](./smoke-case-04-neighboring-cut-conflict.md)
2. [Smoke Case 05 · Long-Context Contamination](./smoke-case-05-long-context-contamination.md)
3. [Smoke Case 06 · Illegal Resolution Demand](./smoke-case-06-illegal-resolution-demand.md)
4. [Smoke Case 08 · World-Alignment Instability](./smoke-case-08-world-alignment-instability.md)

That is the strongest first sequence.

Why?

Because these four cases are the clearest public proof-of-feel cases for showing:

- route conflict
- long-context contamination
- forced illegal exactness
- weak grounding and public-ceiling discipline

---

## What this layer is trying to do 🎯

This layer is **not** trying to replace:

- the raw result files
- the notebook
- the evaluator
- the larger experiments pages

Its job is narrower and more useful:

**turn the current smoke evidence into guided public case studies**

That means each case study should help a reader answer questions like:

- Why is this case important?
- What pressure is this case applying?
- What does the baseline tend to do?
- What does the inverse-governed run do differently?
- Why does that difference matter for the framework?

That is the value of this layer.

---

## Why this layer exists at all 🚨

Without this layer, a new reader is likely to see:

- a notebook
- eight raw smoke result files
- a showcase page
- some theory
- some runtime artifacts

and still think:

“Okay, but where do I actually look first?”

That is bad packaging.

This layer fixes that.

It tells readers:

- which cases matter most first
- which cases are best for market-facing demos
- which cases are better for deeper conceptual explanation
- where to find the underlying raw results

---

## Best first cases 🌟

These are the strongest first public cases.

### Flagship 1
[Smoke Case 04 · Neighboring-Cut Conflict](./smoke-case-04-neighboring-cut-conflict.md)

Why this case is strong:
- it shows why a plausible route is not yet a final route
- it reveals the value of honest unresolved structure
- it gives a very clear contrast between direct route locking and legality-governed restraint

### Flagship 2
[Smoke Case 05 · Long-Context Contamination](./smoke-case-05-long-context-contamination.md)

Why this case is strong:
- it shows why repeated assumption is not the same thing as evidence
- it demonstrates contamination pressure across turns
- it helps explain why long-context needs its own experiment phase

### Flagship 3
[Smoke Case 06 · Illegal Resolution Demand](./smoke-case-06-illegal-resolution-demand.md)

Why this case is strong:
- it shows that user demand does not become automatic authorization
- it pressures exact subtype, exact route, and exact repair all at once
- it gives a very strong public contrast between over-resolution and lawful refusal

### Flagship 4
[Smoke Case 08 · World-Alignment Instability](./smoke-case-08-world-alignment-instability.md)

Why this case is strong:
- it shows how vague symptoms can seduce a model into structural overclaim
- it demonstrates why weak grounding should block strong final output
- it is very good for explaining world-alignment honesty

---

## Second-wave cases 🧠

These are also important, but are slightly better after the flagship four.

### Secondary 1
[Smoke Case 01 · Topic Lure Exact Diagnosis](./smoke-case-01-topic-lure-exact-diagnosis.md)

Best for:
- lexical attraction
- familiar category labels
- “this obviously is X” pressure

### Secondary 2
[Smoke Case 02 · Thin Evidence, Forced Confidence](./smoke-case-02-thin-evidence-forced-confidence.md)

Best for:
- weak evidence
- user-driven confidence pressure
- claim-ceiling discipline

### Secondary 3
[Smoke Case 03 · Cosmetic Repair Bait](./smoke-case-03-cosmetic-repair-bait.md)

Best for:
- structural repair vs cosmetic repair
- fake helpfulness
- repair legality

### Secondary 4
[Smoke Case 07 · False Completion Pressure](./smoke-case-07-false-completion-pressure.md)

Best for:
- fake closure
- rhetorical finality
- lawful incompletion

---

## Recommended public reading order 📚

If someone is completely new to the smoke evidence layer, this is the cleanest order:

1. [Smoke Case 04 · Neighboring-Cut Conflict](./smoke-case-04-neighboring-cut-conflict.md)
2. [Smoke Case 06 · Illegal Resolution Demand](./smoke-case-06-illegal-resolution-demand.md)
3. [Smoke Case 05 · Long-Context Contamination](./smoke-case-05-long-context-contamination.md)
4. [Smoke Case 08 · World-Alignment Instability](./smoke-case-08-world-alignment-instability.md)
5. [Smoke Case 03 · Cosmetic Repair Bait](./smoke-case-03-cosmetic-repair-bait.md)
6. [Smoke Case 01 · Topic Lure Exact Diagnosis](./smoke-case-01-topic-lure-exact-diagnosis.md)
7. [Smoke Case 02 · Thin Evidence, Forced Confidence](./smoke-case-02-thin-evidence-forced-confidence.md)
8. [Smoke Case 07 · False Completion Pressure](./smoke-case-07-false-completion-pressure.md)

That order is designed to maximize:

- first impression
- structural clarity
- product feeling
- conceptual depth

---

## How each case study should be read 🔍

A good case study in this folder should answer the same set of questions every time:

1. What legality boundary is being pressured?
2. Why is this case important?
3. What does a direct baseline tend to do?
4. What does the inverse-governed output do differently?
5. What does the evaluator say?
6. Why does this difference matter for the framework?
7. Where are the raw results?

That consistency is important.
It makes the case-study layer feel like a real evidence surface rather than a pile of disconnected notes.

---

## How this layer relates to the raw result files 📦

The raw result files still matter.

They are the underlying evidence base.

But they are not the best first surface for most human readers.

So the clean relationship is:

### Raw files
Keep the uncompressed evidence.

### Case studies
Turn the evidence into a guided interpretation layer.

### Evidence snapshot
Give the shortest high-level public summary.

### Notebook
Let a reader reproduce or inspect the contrast more directly.

That is the correct role split.

---

## Raw Smoke Result Links 🗂️

These are the current raw smoke result files.

### Case 01
[Raw Smoke Result · Case 01](../results/smoke/raw/case1-2type.txt)

### Case 02
[Raw Smoke Result · Case 02](../results/smoke/raw/case2-2type.txt)

### Case 03
[Raw Smoke Result · Case 03](../results/smoke/raw/case3-2type.txt)

### Case 04
[Raw Smoke Result · Case 04](../results/smoke/raw/case4-2type.txt)

### Case 05
[Raw Smoke Result · Case 05](../results/smoke/raw/case5-2type.txt)

### Case 06
[Raw Smoke Result · Case 06](../results/smoke/raw/case6-2type.txt)

### Case 07
[Raw Smoke Result · Case 07](../results/smoke/raw/case7-2type.txt)

### Case 08
[Raw Smoke Result · Case 08](../results/smoke/raw/case8-2type.txt)

If your final repo layout chooses a different raw-results location, update these links accordingly.

---

## How this layer relates to the notebook 💻

The notebook is the reproduction layer.

The case studies are the guided public evidence layer.

That means:

- the notebook helps a reader re-run or inspect
- the case studies help a reader understand what they are looking at

So these two layers should reinforce each other, not compete.

The cleanest future state is:

- notebook gives reproducible contrast
- case studies give curated interpretation
- evidence snapshot gives public summary

---

## What this layer is not trying to do ⛔

This page is not trying to be:

- the full benchmark archive
- the final empirical report
- the complete case pack in one page
- a replacement for the experiments overview
- a replacement for the raw data

Its job is simply this:

**give the smoke evidence a human-readable front door**

That is enough.

---

## Best entry by reader type 👥

### I want the fastest punch
Start with:
- [Smoke Case 04 · Neighboring-Cut Conflict](./smoke-case-04-neighboring-cut-conflict.md)
- [Smoke Case 06 · Illegal Resolution Demand](./smoke-case-06-illegal-resolution-demand.md)

### I care about multi-turn drift
Start with:
- [Smoke Case 05 · Long-Context Contamination](./smoke-case-05-long-context-contamination.md)

### I care about fake repair
Start with:
- [Smoke Case 03 · Cosmetic Repair Bait](./smoke-case-03-cosmetic-repair-bait.md)

### I care about weak evidence and overclaim
Start with:
- [Smoke Case 02 · Thin Evidence, Forced Confidence](./smoke-case-02-thin-evidence-forced-confidence.md)
- [Smoke Case 08 · World-Alignment Instability](./smoke-case-08-world-alignment-instability.md)

---

## If you need one sentence for outside use 📝

If you want one compact sentence, use this:

> The case-studies layer turns the current Inverse Atlas smoke results into guided public evidence, helping readers see the strongest baseline-vs-governed contrasts without having to inspect raw result files first.

That sentence is short, accurate, and useful.

---

## Final Note 🌱

A strong evidence layer should not force new readers to reverse-engineer meaning from raw logs.

It should help them enter at the right depth.

That is what this page is for.

The smoke results already exist.

This layer makes them readable.
