# Polaris Protocol Experimental Evidence Packages 🌌

> Traditional Chinese version: [`README.zh-TW.md`](./README.zh-TW.md)  
> Note: Not every WFGY page currently has a Traditional Chinese version. If there is any difference between this English page and the Traditional Chinese page, please treat the English page as the primary reference.

This is the public experimental evidence page for **WFGY 5.0 Polaris Protocol**.

The purpose of this page is simple:

You should be able to understand what these experiments are testing, why they matter for AI cost, what the public evidence packages represent, how to inspect or rerun the Colab notebooks, and what the current results can and cannot claim.

The published ZIP files contain the public evidence records.

The Colab notebooks are companion notebooks for inspection, reproduction attempts, and report generation.

Official repository:

https://github.com/onestardao/WFGY

License:

Unless a specific file states otherwise, this project uses the MIT License.

<a id="top"></a>

---

## Quick Navigation 🧭

| What you want to see | Jump to |
| --- | --- |
| Understand the experiment first | [3-minute overview](#quick-start) |
| Open the Colab notebooks | [Run / inspect with Colab](#colab) |
| What the packages mean | [Seven public evidence packages](#evidence-packs) |
| Why PP02D was added | [Community follow-up supplement](#community-follow-up) |
| Core numbers | [Core results overview](#results) |
| Whether the tasks were too easy | [Task design and rigor](#rigor) |
| How skeptic questions are answered | [FAQ and skeptic attacks](#faq) |
| Download evidence ZIP files | [Downloads and file verification](#downloads) |
| What this does not claim | [Claim boundary](#claim-ceiling) |

---

<a id="quick-start"></a>

## 3-minute overview ⚡

AI cost is rising, not only because models are getting larger, but also because many tasks repeatedly push large amounts of background, rules, constraints, examples, and context into the model.

The more tokens a model has to read, the higher the inference cost becomes.

The Polaris Protocol experiment asks:

> Instead of giving the model the entire instruction book every time, what if we first organize the task into a more stable structure, then ask the model to produce the output? Can we use far fewer tokens while still preserving inspectable output quality?

This is not simply shortening a prompt.

If you only shorten a prompt, you may also remove important constraints, boundaries, scoring conditions, and error checks. Polaris Protocol is not about aggressively deleting text. It is about extracting the important relationships inside the task.

What Polaris Protocol tries to preserve:

| What should be preserved | Why it matters |
| --- | --- |
| Task goal | Helps the model understand what must be completed |
| Constraints | Prevents the model from drifting |
| Order relations | Prevents missing or skipping steps |
| Boundary rules | Prevents overextension |
| Error risks | Prevents common false success patterns |
| Audit conditions | Makes the result inspectable |

In plain language:

A traditional long-context approach is like handing the model an entire city encyclopedia every time.

The Polaris Protocol approach is more like drawing a city map, including roads, relations, danger zones, destinations, and checkpoints.

The point is not to make the information smaller.

The point is to make the information clearer.

One sentence summary:

> Polaris Protocol does not make the task smaller. It makes the task clearer. 🧠

<details>
<summary>Expand: What does this have to do with GPU cost?</summary>

When people talk about AI cost, they usually think about GPUs first.

That is not wrong. GPU cost is a major part of model inference cost.

But in real use cases, cost does not only come from the GPU itself. It also comes from how many tokens the model has to read, how many tokens it has to generate, how many rounds it has to run, and how much long-context baggage it has to carry.

If every task requires a large block of background text, the model must repeatedly read a large amount of content.

That becomes cost.

The Polaris Protocol idea is:

Besides pursuing larger models, stronger GPUs, and longer context windows, we can also ask another question:

Can the task itself be represented in a smarter way first?

If a task can be organized into a more stable structure, the model may not need to reread an entire library every time. It may only need to read a clearer task map.

So Polaris Protocol is not saying that GPUs are unimportant.

It is saying:

AI cost can be approached not only from the hardware side, but also from the task-structure side.

</details>

<details>
<summary>Expand: This is not simply making the prompt shorter</summary>

If you only make the prompt shorter, you usually lose information, and output quality may drop.

The key point of Polaris Protocol is not aggressive text deletion. It is reorganizing task content into a more stable structure.

You can think of it like this:

| Original long text | After conversion |
| --- | --- |
| A long task description | Task nodes |
| Many rules | Rule relations |
| Multiple goals | Goal order |
| Multiple constraints | Boundary conditions |
| Possible errors | Audit points |
| Final output | Output format |

This means the model does not receive a long messy block of text. It receives a clearer task structure.

The model’s job then becomes more like:

Read the task map.  
Translate the map back into the correct output.  
Complete the requested task.

So you can understand it as:

First turn the task into structure, then let the model translate that structure into an answer.

</details>

[Back to quick navigation](#top)

---

<a id="colab"></a>

## Run / inspect with Colab 🚀

The published evidence packages already contain the experimental results, raw outputs, verdicts, audits, token records, and public-safe evidence files.

The Colab notebooks are provided as companion notebooks for readers who want to inspect, reproduce, or adapt the experiments.

You do **not** need to rerun the notebooks to understand the published results.

The result snapshots are already summarized below.

If you choose to rerun a notebook, token usage and cost may vary depending on:

- selected model
- current API pricing
- API behavior at runtime
- number of cases
- retry behavior
- output length
- whether you run smoke, mini, or full mode

These Colab notebooks are **not third-party certification**.

They are public reproduction / inspection companions for the existing evidence packages.

---

### Colab notebooks

| Package | Purpose | Published result snapshot | Colab |
| --- | --- | --- | --- |
| PP01 | Main cost battlefield | 320 cases; Group C total token ratio vs Group A = `0.1656`; overclaim count = `0`; critical wrong-source count = `0` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP01.ipynb) |
| PP02A | Version evolution evidence | 120 cases; 240 final-run raw outputs; parse success rate = `1.0`; final result = `SEAL_PASS` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02A.ipynb) |
| PP02B | Math stress / structured evidence chain | 120 cases; 720 expected / actual outputs; Group C parse pass rate = `1.0`; main certificate result = `T4_MAIN_CERTIFICATE_PASS` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02B.ipynb) |
| PP02C | Code repair red-line evidence | 120 cases; 720 expected / actual outputs; hard red-line count = `0`; claim-boundary pass rate = `1.0` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02C.ipynb) |
| PP02D_A | API stability supplement | 216 fixtures; fixture pass = `216/216`; support closure checks = `2160/2160`; poison reject = `12/12` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D.ipynb) |
| PP02D_B | Hardcase final-run gates | 216 API calls; certificate exact = `216/216`; parser rescue = `0`; semantic fallback = `0` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D_B.ipynb) |
| PP02D_C | Public QA compact-context evidence | 100 public QA cases; compact context preserves comparable answer F1 with lower token / cost load in the published scope | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D_C.ipynb) |

---

### What each Colab produces

Each MVP Colab is designed to end with a compact report section.

The goal is not to flood readers with raw tables.

The goal is to make the experimental signal visible in a few simple outputs.

Each notebook should produce:

| Output | Purpose |
| --- | --- |
| `executive_report.md` | short human-readable summary |
| `metrics_summary.csv` | compact metric table |
| `chart_01_*.png` | main signal chart |
| `chart_02_*.png` | safety / gate / comparison chart |
| `chart_03_*.png` | token / cost / supporting chart |

The report charts are meant to show the key signal of each experiment:

| Package | Report focus |
| --- | --- |
| PP01 | token ratio, score retention, overclaim / wrong-source checks |
| PP02A | final pass, domain coverage, weaker previous reference |
| PP02B | compiler certificate, family verdicts, model stress separation |
| PP02C | hard red-line counts, claim-boundary pass rate, false repair categories |
| PP02D_A | fixture pass, support closure, poison rejection |
| PP02D_B | certificate exactness, parser rescue = 0, semantic fallback = 0 |
| PP02D_C | baseline vs compact answer F1, token reduction, estimated cost reduction |

---

### Colab claim boundary

The Colab notebooks are public reproduction / inspection companions.

They do not change the claim boundary of the experiments.

| Do not interpret Colab as | Correct interpretation |
| --- | --- |
| Third-party official validation | Public reproduction / inspection notebook |
| Universal proof | Scoped experimental companion |
| Production seal | Runnable evidence-side artifact |
| Guaranteed identical rerun | Rerun may vary depending on model, API, pricing, and settings |
| Proof that all AI tasks are solved | Evidence within the published task scope |

The published result summaries remain the primary reference.

The Colab notebooks make the evidence easier to inspect, rerun, and adapt.

[Back to quick navigation](#top)

---

<a id="evidence-packs"></a>

## Seven public evidence packages 📦

This page currently publishes seven main evidence packages.

They are not seven copies of the same material. They represent different angles of evidence.

The first four packages, PP01 through PP02C, are the original public evidence layer. The PP02D_A, PP02D_B, and PP02D_C packages are a later supplementary evidence layer added after community feedback, including suggestions from [Zaious (@ChronicleCore)](https://github.com/Zaious).

The PP02D packages do not replace the earlier packages. They add more checks around API stability, hardcase final-run gates, and public QA noninferiority.

| Evidence package | What it answers | One-line meaning |
| --- | --- | --- |
| PP01 / Main evidence bundle | After task structuring, can token cost be reduced while preserving quality? | Main cost battlefield |
| PP02A | Can the T4 branch move from a weaker version to final pass? | Version evolution evidence |
| PP02B | Can math-leaning tasks form an inspectable structured evidence chain? | Math stress test |
| PP02C | Can code repair preserve source boundaries, sandbox checks, and hard red lines? | Skeptic red-line test |
| PP02D_A | Can sharded API fixtures preserve structured outputs under stability checks? | API stability supplement |
| PP02D_B | Can hardcase final-run gates pass without parser rescue or semantic fallback? | Hardcase final-run supplement |
| PP02D_C | Can public QA compact context reduce cost while staying noninferior on inspectable QA metrics? | Public QA noninferiority supplement |

### PP01 / Main evidence bundle

This is the best package for first-time readers to start with.

It answers:

Can structured task representation preserve inspectable output quality while using far fewer tokens?

This page treats `wfgy5_polaris_protocol_public_evidence_bundle_20260503.zip` as the **PP01 / Main evidence bundle** and the current public evidence entry point.

### PP02A

This package focuses on the T4 evidence branch.

Its value is not only that the final result passes. It also preserves the evolution path, so readers can see that this is not just a cherry-picked victory screenshot.

### PP02B

This package focuses on math-leaning tasks.

It does not claim that all math problems have been solved. It shows how, within this task set, model outputs, normalized results, family verdicts, contract checks, and certificate results form an inspectable evidence chain.

### PP02C

This package focuses on code repair, sandbox checks, source boundaries, and hard red lines.

Code repair is especially prone to false success, such as guessing repository content, misusing metadata, following distractor sources, claiming precise fixes without evidence, or ignoring source priority. PP02C is designed to check exactly these problems.

### PP02D_A

This package focuses on sharded API stability and output preservation checks.

It adds evidence that structured outputs, support checks, aggregate support checks, counterfactual checks, and poison-rejection checks can pass across a 216-fixture supplement.

### PP02D_B

This package focuses on hardcase final-run API evidence.

It checks transport success, parse success, certificate exactness, arena valid-set matching, valid recall, and invalid rejection across 216 API calls.

### PP02D_C

This package focuses on public QA noninferiority under compact context.

It uses 100 public QA cases and compares baseline raw context against Polaris Protocol compact context across two model levels. The purpose is not to claim global QA superiority. The purpose is to publish inspectable evidence that compact context can reduce token cost while preserving a comparable QA signal within this public test scope.

[Back to quick navigation](#top)

---

<a id="community-follow-up"></a>

## Community follow-up supplement 🤝

The PP02D_A, PP02D_B, and PP02D_C packages were added as a community-follow-up supplement.

After the first public evidence layer was prepared, community feedback suggested that the release would be stronger if it included additional evidence for several pressure points that were not the main focus of PP01 through PP02C.

Special thanks to [Zaious (@ChronicleCore)](https://github.com/Zaious) for suggesting that these supplementary checks be made more explicit.

The added PP02D packages are implemented and published by the WFGY / OneStarDAO side. They should be read as additional public experimental evidence, not as third-party validation, official benchmark certification, or a release of the core mathematics.

What PP02D adds:

| Supplement | What it adds | Why it matters |
| --- | --- | --- |
| PP02D_A | 216-fixture sharded API stability and preservation checks | Adds evidence that structured outputs, support checks, counterfactual checks, and poison-rejection checks can survive API-style sharding |
| PP02D_B | 216-call hardcase final-run evidence | Adds evidence that hardcase gates can pass without parser rescue, semantic fallback, certificate mismatch, or valid-set mismatch |
| PP02D_C | 100-case public QA noninferiority pilot | Adds a public QA comparison between baseline raw context and Polaris Protocol compact context, with token and cost reduction records |

In plain language:

PP01 through PP02C established the first public evidence layer.

PP02D_A through PP02D_C make that layer harder to dismiss by adding extra checks where a skeptical reader may reasonably ask for more evidence.

This does not change the claim boundary.

The PP02D supplement makes the evidence layer broader and more inspectable, but it does not claim that all AI tasks are solved, that small models universally beat large models, or that the full core mathematics has already been released.

[Back to quick navigation](#top)

---

<a id="results"></a>

## Core results overview 📊

The current public release is the first-layer experimental evidence for the pre-release stage of WFGY 5.0 Polaris Protocol.

This layer focuses on publishing results, evidence chains, auditable materials, and MVP Colab companion notebooks.

It is not a full formal reproduction suite.

| Item | Count or status |
| --- | ---: |
| Main public evidence packages | 7 |
| Recommended MVP Colab companion notebooks | 7 |
| Original PP01–PP02C main test cases | 680 |
| Original PP01–PP02C main model outputs | 3600 |
| PP02D_A fixtures | 216 |
| PP02D_B final-run API calls / raw outputs | 216 |
| PP02D_C public QA cases | 100 |
| PP02D_C model-arm output records | 400 |
| Full core mathematics included | 0 |
| Full formal reproduction suite | Still expanding |

What the current public version can support:

> Within the currently published task scope, Polaris Protocol shows a signal worth paying attention to: if a task is first organized into a more stable structure, it may reduce token cost while preserving inspectable output quality.

What the current public version should not be interpreted as:

| Should not be interpreted as | Explanation |
| --- | --- |
| All AI tasks have been solved | The current scope only covers the specified public tasks |
| Small models completely beat large models | The current evidence supports structured-task effects in specific tasks |
| GPU scaling is no longer important | GPUs remain important; Polaris Protocol is a task-structure-side cost route |
| A third-party official benchmark | This is a self-built public experimental evidence chain |
| Full core mathematics already released | The current release is an evidence package, not the full core |
| Full formal reproduction suite already complete | The MVP Colab companion notebooks are now provided, but the full formal reproduction suite is still expanding |

Full core mathematics, formal reproduction materials, and more release materials are expected to be added over time.

<details>
<summary>Expand: detailed result snapshots of the seven packages</summary>

### PP01 / Main evidence bundle

| Metric | Value |
| --- | ---: |
| Test cases | 320 |
| Test groups | 6 |
| Expected outputs | 1920 |
| Actual outputs | 1920 |
| Parse pass rate | 1.0 |
| Leakage count | 0 |
| Group C average score | 0.988465 |
| Group B average score | 0.967265 |
| Group C retention rate vs Group B | 1.0219 |
| Group C total token ratio vs Group A | 0.1656 |
| Group C input token ratio vs Group A | 0.1242 |
| Failure signature match rate | 1.0 |
| Overclaim count | 0 |
| Critical wrong-source count | 0 |
| Family collapse count | 0 |
| Hard checks passed | true |
| Final pass | true |
| Global status | `OSK_MVP_FINAL_PASS` |

### PP02A

| Metric | Final value |
| --- | ---: |
| Test cases | 120 |
| Final-run raw outputs | 240 |
| Domains | 6 |
| API errors | 0 |
| Parse failures | 0 |
| Parse success rate | 1.0 |
| Weak rows | 0 |
| Domains reaching seal | 6 |
| Domains reaching dominant or better | 6 |
| Domains reaching release or better | 6 |
| T4 system score | 100.0 |
| Internal weighted score | 125.0 |
| Final result | `SEAL_PASS` |

PP02A also preserves a weaker previous reference record: parse success rate 0.9958, weak rows 1, domains reaching seal 5, final result `INVALID`.

### PP02B

| Metric | Value |
| --- | ---: |
| Test cases | 120 |
| Expected compiled outputs | 120 |
| Actual compiled outputs | 120 |
| Expected total outputs | 720 |
| Actual total outputs | 720 |
| Expected model stress outputs | 600 |
| Actual model stress outputs | 600 |
| Model API calls | 600 |
| Group C parse pass rate | 1.0 |
| Group C contract pass rate | 1.0 |
| Family red count | 0 |
| Compile verification red count | 0 |
| Model stress warning count | 0 |
| Model stress result | `MODEL_STRESS_PASS` |
| Main certificate result | `T4_MAIN_CERTIFICATE_PASS` |
| Final result | `T4_MAIN_CERTIFICATE_PASS` |

### PP02C

| Metric | Value |
| --- | ---: |
| Main test cases | 120 |
| Test groups per case | 6 |
| Expected main outputs | 720 |
| Actual main outputs | 720 |
| Parse pass rate | 1.0 |
| Hard red-line count | 0 |
| Warning count | 0 |
| Library hallucination count | 0 |
| Metadata-as-evidence count | 0 |
| Distractor-source-as-official-source count | 0 |
| Source-priority-ignore count | 0 |
| Precise-fix-without-source count | 0 |
| Contract missing-field count | 0 |
| Contract enum-error count | 0 |
| Contract value-mismatch count | 0 |
| Claim-boundary pass rate | 1.0 |
| Surplus pass score | 120 |
| Final branch result | `FULL_SANDBOX_STRONG_PASS` |

PP02C also includes supporting checks such as sandbox runs, a global hard-veto matrix, a mini preflight test, and a synthetic distractor matrix.

### PP02D_A

| Metric | Value |
| --- | ---: |
| Fixture count | 216 |
| Shard count | 6 |
| API exception count | 0 |
| Shard parse fail count | 0 |
| Parse fail count | 0 |
| Fixture pass count | 216/216 |
| Semantic support checks | 1944/1944 |
| Aggregate support union checks | 216/216 |
| Total support closure checks | 2160/2160 |
| Forbidden-use count | 0 |
| Hard-zero count | 0 |
| Counterfactual pairs pass | 180/180 |
| DeltaHitScore | 1.0 |
| StabilityScore | 1.0 |
| CounterfactualScore | 1.0 |
| Poison reject count | 12/12 |
| Schema budget pass | true |
| Final result | `GREEN` |

### PP02D_B

| Metric | Value |
| --- | ---: |
| API calls | 216/216 |
| Transport pass | 216/216 |
| Transport fail | 0 |
| Parse pass | 216/216 |
| Parse fail | 0 |
| Parser rescue count | 0 |
| Semantic fallback count | 0 |
| Certificate exact | 216/216 |
| Arena valid-set match | 54/54 |
| Valid recall | 108/108 |
| Invalid rejection | 108/108 |
| Final result | `GREEN` |
| Claim ceiling | `API_216_EVIDENCE_ONLY_NOT_GLOBAL_PROOF` |

### PP02D_C

| Metric | Value |
| --- | ---: |
| Public QA cases | 100 |
| Models | `gpt-4.1-mini`, `gpt-4.1` |
| Arms | baseline raw context, Polaris Protocol compact context |
| Model-arm output records | 400 |
| Parse pass records | 400/400 |
| Metadata leakage fail count | 0 |
| Self-grading fail count | 0 |
| API key pattern in prompts count | 0 |
| Baseline answer F1 mean, both models | 0.7884761905 |
| Compact-context answer F1 mean, both models | 0.7941428571 |
| Baseline support-title F1 mean, both models | 0.8966666667 |
| Compact-context support-title F1 mean, both models | 0.8453333333 |
| Token reduction, compact vs baseline | 0.3704355582 |
| Estimated cost reduction, compact vs baseline | 0.3124261543 |
| Baseline wrong-source total, both models | 2 |
| Compact-context wrong-source total, both models | 5 |
| Baseline hallucinated-detail total, both models | 0 |
| Compact-context hallucinated-detail total | 1 |
| Final result | `GREEN` |
| Claim ceiling | `100_CASE_PUBLIC_HOTPOTQA_MODEL_LADDER_EVIDENCE_ONLY` |

Model-ladder detail:

| Model | Arm | Answer F1 mean | Support-title F1 mean | Wrong-source total | Hallucinated-detail total | Estimated cost USD |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `gpt-4.1` | `A_BASELINE_RAW_CONTEXT` | 0.7791428571 | 0.9026666667 | 1 | 0 | 0.498238 |
| `gpt-4.1` | `B_POLARIS_COMPACT_CONTEXT` | 0.7819761905 | 0.8403333333 | 3 | 1 | 0.342512 |
| `gpt-4.1-mini` | `A_BASELINE_RAW_CONTEXT` | 0.7978095238 | 0.8906666667 | 1 | 0 | 0.099630 |
| `gpt-4.1-mini` | `B_POLARIS_COMPACT_CONTEXT` | 0.8063095238 | 0.8503333333 | 2 | 0 | 0.068566 |

Note:

The recommended MVP Colab for PP02D_C may use the `Full100 Mini` runnable path for lower reproduction cost. The broader model-ladder summary remains part of the published evidence record.

</details>

[Back to quick navigation](#top)

---

<a id="rigor"></a>

## Task design and rigor 🧪

These experiments are not a few showcase questions used for performance theater.

If we only selected a few questions the model happened to answer well, the page could look impressive, but the result would have little research value.

The Polaris Protocol experiments use family-based design.

This means:

Instead of only asking “Did the model get the answer right?”, the tasks separate different failure types and check whether the model can preserve task structure, source boundaries, error checks, and claim boundaries under different kinds of pressure.

In simple terms:

> We are not choosing a few easy roads for the model to walk on. We first mark the places where models tend to fall, then check whether it can walk through them reliably. 🕳️

### Why not use single-question demonstrations?

Single-question demonstrations usually have three problems:

| Problem | Risk |
| --- | --- |
| Too few questions | The model may simply happen to know them |
| Too smooth | Boundaries and failure risks are not exposed |
| Only final answers are inspected | You cannot see whether the model skipped steps, guessed sources, or overclaimed |

So these experiments do not only check whether the final output looks good.

They also check:

| Check direction | Why it matters |
| --- | --- |
| Whether the task keeps its original meaning | Prevents the model from turning the problem into an easier one |
| Whether conditions are preserved | Prevents the model from ignoring constraints |
| Whether sources are reliable | Prevents guessing or using the wrong material |
| Whether the result overclaims | Prevents local results from being inflated into general conclusions |
| Whether there is leakage | Prevents task or answer contamination |
| Whether hard red lines are crossed | Prevents good-looking answers from hiding unacceptable errors |
| Whether raw outputs can be inspected | Prevents reliance only on normalized summaries |

### What risks do the branches test?

| Branch | Main test direction | What it protects against |
| --- | --- | --- |
| PP01 / Main evidence bundle | Token cost reduction and quality retention | Saving tokens while quality collapses, or results supported by leakage and overclaiming |
| PP02A | T4 evidence branch and version evolution | Showing only the final good result without preserving process context |
| PP02B | Structured testing for math-leaning tasks | Symbol drift, condition loss, false equivalence, ignored counterexamples |
| PP02C | Code repair, source boundaries, sandbox checks, and hard red lines | Repository hallucination, metadata misuse, distractor-source misuse, precise-fix claims without evidence |
| PP02D_A | Sharded API stability and output preservation | Passing only a visible summary while parse, support, or counterfactual checks fail |
| PP02D_B | Hardcase final API evidence | Transport failure, parser rescue dependency, certificate mismatch, valid-set mismatch |
| PP02D_C | Public QA noninferiority pilot | Token reduction that quietly loses QA quality, increases leakage, or inflates claims |

These branches are not testing the same thing repeatedly.

They correspond to different risk surfaces.

PP01 checks the main cost signal.

PP02A checks the evidence path.

PP02B checks math-leaning reasoning pressure.

PP02C checks code repair and skeptic red lines.

PP02D_A checks sharded API stability and preservation.

PP02D_B checks hardcase final-run gates.

PP02D_C checks public QA noninferiority under compact context.

<details>
<summary>Expand: Were the tasks intentionally made easy?</summary>

No.

A more precise way to say it:

The tasks were not designed to make the model look impressive. They were designed so common errors would have a chance to appear.

PP01 does not only check whether tokens decrease. It also checks quality, leakage, wrong sources, and overclaiming.

PP02A does not only check the final pass. It also preserves a weaker previous reference record.

PP02B does not only check whether the math answer looks good. It checks symbols, conditions, assumptions, counterexamples, and reasoning structure.

PP02C does not only check whether the code answer sounds plausible. It checks source usage, sandbox checks, distractor sources, and hard red lines.

PP02D_A does not only check whether a summary is green. It checks fixtures, support closure, counterfactual pairs, poison rejection, and parse stability.

PP02D_B does not only check whether an API run completed. It checks transport, parsing, certificate exactness, valid-set match, valid recall, and invalid rejection.

PP02D_C does not only check whether compact context uses fewer tokens. It also checks answer F1, support-title F1, leakage, wrong-source totals, hallucinated-detail totals, and cost records.

So the task design is not “watering things down.”

It is closer to:

> Turn common model failure paths into a test field, then check whether Polaris Protocol can reduce those failures.

</details>

<details>
<summary>Expand: Why is a self-built experiment still valuable?</summary>

This is a self-built public experiment, not a third-party official benchmark.

So it should not be packaged as an external authority ranking.

But a self-built experiment can still be valuable, as long as it does not only publish the final score.

It must allow readers to inspect the path backward:

| If only the result is shown | Trust problem |
| --- | --- |
| Only a total score | You cannot see how each case was judged |
| Only screenshots | You cannot see raw model outputs |
| Only good-looking examples | You cannot tell whether results were cherry-picked |
| Only conclusions | You cannot tell whether claims were inflated |
| No file fingerprint | You cannot verify file consistency |

This release publishes the evidence chain:

Raw model outputs.  
Normalized outputs.  
Per-case verdicts.  
Token cost.  
Audit records.  
Warning records.  
Hard red lines.  
File fingerprints.  
MVP Colab companion notebooks.

So the position of this material is not:

> Please believe that we are strong.

It is:

> This is the currently public experimental trace. You can inspect it backward from the result.

</details>

[Back to quick navigation](#top)

---

<a id="faq"></a>

## FAQ and skeptic attacks 🛡️

This section answers the questions first-time readers and skeptics are most likely to ask.

<details>
<summary>Q1. Is this just making the prompt shorter?</summary>

No.

A short prompt reduces words.

Polaris Protocol organizes task structure.

If you only shorten text, you can easily remove constraints, boundaries, scoring conditions, and error checks. Polaris Protocol tries to preserve those key pieces of information, but organize them into a task map that is easier for the model to use.

In plain language:

The traditional approach is like giving the model an entire encyclopedia every time.

The Polaris Protocol approach is more like drawing a map first, then asking the model to complete the task by following the map.

</details>

<details>
<summary>Q2. Is this just a self-made experiment congratulating itself?</summary>

This is a self-built public experiment, not a third-party official benchmark.

But it still has value because it does not only publish the final score.

The material publishes an evidence chain, including raw model outputs, normalized results, per-case verdicts, token cost, audit records, warning records, hard red lines, file fingerprints, and MVP Colab companion notebooks.

So its position is not external ranking. It is inspectable public experimental evidence.

More precisely:

This is not asking you to first believe that we are strong.

It first publishes the experimental trace, so you can inspect backward from the result.

</details>

<details>
<summary>Q3. Were the tasks intentionally made simple?</summary>

This is not a single-question showcase. It uses family-based pressure design.

The branches do not only test comfortable scenarios. They check different types of failure risk.

So this task design is not watered down.

It is closer to:

Turn common model failure paths into a test field, then check whether Polaris Protocol can reduce those failures.

</details>

<details>
<summary>Q4. Did you leak answers or contaminate the tasks?</summary>

The public packages do not only publish total scores. They also include leakage checks, raw outputs, normalized results, audit records, and MVP Colab companion notebooks.

This does not mean future experiments can never make mistakes.

It means this public release does not only provide a beautiful screenshot. It preserves inspection material that can be checked backward.

For example:

PP01 checks leakage, wrong sources, overclaiming, and family collapse.

PP02C checks source behavior, distractor sources, metadata as evidence, sandbox checks, and hard red lines.

PP02D_C checks metadata leakage, self-grading risk, API key pattern risk, wrong-source totals, and hallucinated-detail totals.

The purpose of these checks is to avoid models relying on leaked answers, misusing sources, or treating non-evidence as evidence.

</details>

<details>
<summary>Q5. Does this mean small models completely beat large models?</summary>

No.

A more precise statement is:

Within the currently published task scope, Polaris Protocol shows a signal that structured task representation can reduce token cost while preserving inspectable output quality.

This should not be interpreted as all small models completely beating all large models.

It should also not be interpreted as all AI tasks being solved.

What can be said for now:

In these public test branches, structured task representation shows a cost and quality signal worth paying attention to.

</details>

<details>
<summary>Q6. Does this mean GPU scaling is no longer important?</summary>

No.

GPUs remain important.

Polaris Protocol focuses on reducing cost from another direction: improving the representation of the task itself, so the model does not have to reread large amounts of context every time.

In other words:

Hardware scaling is one path.

Task-structure optimization is another path.

These experiments are not saying GPUs are unimportant. They are showing that AI cost can also be reconsidered from the task-structure side.

</details>

<details>
<summary>Q7. Why do the ZIP files not include the full core mathematics?</summary>

Because this release is an experimental evidence package, not the full core mathematics release.

The current goal is to let readers inspect raw model outputs, verdicts, cost, audits, warnings, red lines, file fingerprints, and MVP Colab companion notebooks.

Full core mathematics and deeper formal materials will be added over time.

In simple terms:

This version publishes the evidence and companion notebooks first.

Deeper mathematical logic and implementation materials will follow later.

</details>

<details>
<summary>Q8. What is the most important meaning of this release?</summary>

The most important point is not that there are many ZIP files.

The most important point is:

Evidence is published first, before deeper mathematics and full implementation materials are released.

This means readers do not have to rely only on screenshots or slogans. They can first inspect raw model outputs, normalized results, verdict tables, token cost, audit records, file fingerprints, and Colab companion notebooks.

In other words:

This material is not asking you to believe first.

It first publishes the public evidence chain so you can understand it and inspect backward. ✨

</details>

<details>
<summary>Q9. Why were PP02D_A, PP02D_B, and PP02D_C added?</summary>

They were added as a community-follow-up supplement.

PP01 through PP02C already covered the first public evidence layer: cost signal, version evolution, math-leaning tasks, and code-repair red lines.

The PP02D packages add extra evidence where readers may reasonably ask for more pressure:

API stability.

Hardcase final-run gates.

Public QA noninferiority under compact context.

Special thanks to [Zaious (@ChronicleCore)](https://github.com/Zaious) for suggesting that these supplementary checks be made more explicit.

This does not change the claim boundary. PP02D makes the public evidence layer broader and more inspectable, but it is still not a full release of the core mathematics or a third-party official benchmark.

</details>

<details>
<summary>Q10. Why are public prompt bodies removed from PP02D_C?</summary>

PP02D_C is published as an evidence package, not as a core-method package.

The public ZIP keeps the result evidence: case manifest, raw outputs, parser records, scorer traces, leakage audits, and verdicts.

Prompt bodies and compact-selection trace internals are excluded to avoid exposing non-public method details before the formal open-source release.

The public PP02D_C archive also normalizes the uploaded source label from `DD02C` to `PP02D_C` and renames stale `full_30` artifact filenames to `full100`, while preserving raw model JSON bodies for hash integrity.

</details>

<details>
<summary>Q11. Do I have to run the Colab notebooks?</summary>

No.

The published results are already summarized on this page.

The Colab notebooks are provided for readers who want to inspect, rerun, adapt, or generate compact reports.

Running the notebooks may require API keys and may consume paid tokens depending on the notebook and selected settings.

</details>

[Back to quick navigation](#top)

---

<a id="downloads"></a>

## Downloads and file verification 🧾

If you only want a quick understanding, reading this README should be enough.

The ZIP files are mainly for people who want to reproduce, research, audit, or inspect raw outputs.

The current official public evidence packages are the following seven files:

| Official name | File | Purpose |
| --- | --- | --- |
| PP01 / Main evidence bundle | `wfgy5_polaris_protocol_public_evidence_bundle_20260503.zip` | Main cost evidence and public evidence entry point |
| PP02A | `wfgy5_polaris_protocol_pp02a_t4_120case_public_evidence_20260503.zip` | T4 evidence branch and version evolution |
| PP02B | `wfgy5_polaris_protocol_pp02b_sp_120case_public_evidence_20260503.zip` | Structured testing for math-leaning tasks |
| PP02C | `wfgy5_polaris_protocol_pp02c_t4_120case_public_evidence_20260503.zip` | Code repair, sandbox checks, and hard red lines |
| PP02D_A | `wfgy5_polaris_protocol_pp02d_a_public_evidence_20260504.zip` | 216-fixture sharded API stability and preservation checks |
| PP02D_B | `wfgy5_polaris_protocol_pp02d_b_public_evidence_20260504.zip` | 216-call API hardcase final-run evidence |
| PP02D_C | `wfgy5_polaris_protocol_pp02d_c_public_evidence_20260504.zip` | Public QA noninferiority pilot evidence |

Download links:

| File | Download |
| --- | --- |
| `wfgy5_polaris_protocol_public_evidence_bundle_20260503.zip` | [Download](./downloads/wfgy5_polaris_protocol_public_evidence_bundle_20260503.zip) |
| `wfgy5_polaris_protocol_pp02a_t4_120case_public_evidence_20260503.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02a_t4_120case_public_evidence_20260503.zip) |
| `wfgy5_polaris_protocol_pp02b_sp_120case_public_evidence_20260503.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02b_sp_120case_public_evidence_20260503.zip) |
| `wfgy5_polaris_protocol_pp02c_t4_120case_public_evidence_20260503.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02c_t4_120case_public_evidence_20260503.zip) |
| `wfgy5_polaris_protocol_pp02d_a_public_evidence_20260504.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02d_a_public_evidence_20260504.zip) |
| `wfgy5_polaris_protocol_pp02d_b_public_evidence_20260504.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02d_b_public_evidence_20260504.zip) |
| `wfgy5_polaris_protocol_pp02d_c_public_evidence_20260504.zip` | [Download](./downloads/wfgy5_polaris_protocol_pp02d_c_public_evidence_20260504.zip) |

Colab links:

| Package | Colab |
| --- | --- |
| PP01 | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP01.ipynb) |
| PP02A | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02A.ipynb) |
| PP02B | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02B.ipynb) |
| PP02C | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02C.ipynb) |
| PP02D_A | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D.ipynb) |
| PP02D_B | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D_B.ipynb) |
| PP02D_C | [Open Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/Polaris/experiments/downloads/PP02D_C.ipynb) |

The downloads folder may also contain earlier process files.

First-time readers should use the seven official public evidence packages and seven recommended Colab notebooks listed above as the main reference.

<details>
<summary>Expand: suggested inspection order for engineers</summary>

| Order | Suggested check | Why it matters |
| --- | --- | --- |
| 1 | Read this README | Understand scope and claim boundary first |
| 2 | Open the Colab notebook | Inspect or rerun the companion workflow |
| 3 | Raw model outputs | Confirms that the run actually produced model responses |
| 4 | Normalized outputs | Shows how outputs were converted into structured records |
| 5 | Per-case or per-fixture verdicts | Shows how each case maps to a result |
| 6 | Group or stage verdicts | Shows higher-level result patterns |
| 7 | Token cost records | Checks cost and token efficiency behavior |
| 8 | Audit records | Checks leakage, warnings, hard vetoes, or source quality checks |
| 9 | SHA256 records | Checks file integrity |

</details>

<details>
<summary>Expand: SHA256 file fingerprints</summary>

SHA256 can be understood as a file fingerprint.

It does not prove that the experimental conclusion is correct. It verifies whether the ZIP you downloaded is consistent with the public record.

| File | SHA256 |
| --- | --- |
| `wfgy5_polaris_protocol_public_evidence_bundle_20260503.zip` | `50ed006c83f25d69b3080da044882e21663ada2cecb432622b843411d078657e` |
| `wfgy5_polaris_protocol_pp02a_t4_120case_public_evidence_20260503.zip` | `28f2ca19a0a6bac27967bedbc07b4c2f9b44f1c212687ae74512967d42a2e7ad` |
| `wfgy5_polaris_protocol_pp02b_sp_120case_public_evidence_20260503.zip` | `10c5d39a15d74afb29d89386147ba60e830fc624b050d53f0e4187c97fe3df65` |
| `wfgy5_polaris_protocol_pp02c_t4_120case_public_evidence_20260503.zip` | `a85b7919da2fae8c543189fbaf586e3573af73642a1e410e49e5df6a5e6bb9f8` |
| `wfgy5_polaris_protocol_pp02d_a_public_evidence_20260504.zip` | `3915a336566074344314ced1c9c332640f659019d6278e434e18e987118af299` |
| `wfgy5_polaris_protocol_pp02d_b_public_evidence_20260504.zip` | `0fcd4529f531b5a0c8724183c7034f36b083995509fb977ddaa81a34f14a76a5` |
| `wfgy5_polaris_protocol_pp02d_c_public_evidence_20260504.zip` | `2a372b926f2aeb7fa8043018dedb45087d8a5ab45be24c035bdd24d06bb85d8b` |

</details>

[Back to quick navigation](#top)

---

<a id="claim-ceiling"></a>

## Claim boundary 🚧

What this material can currently say:

| Can say | Explanation |
| --- | --- |
| Polaris Protocol shows a token-cost reduction signal within the public task scope | Especially in the PP01 main cost experiment and the PP02D_C public QA pilot |
| Structured task representation may preserve inspectable output quality | The evidence chain matters, not only whether the answer looks good |
| The public packages cover different risk surfaces | Cost, version evolution, math-leaning tasks, code repair, API stability, hardcase gates, and public QA |
| ZIP files allow researchers and skeptics to inspect backward | Includes raw outputs, verdicts, cost, audits, and file fingerprints |
| Colab notebooks make inspection and rerun attempts easier | They are companion notebooks for the evidence packages |

What this material currently cannot say:

| Cannot say | Reason |
| --- | --- |
| All AI tasks have been solved | The current scope only covers specified public tasks |
| Small models completely beat large models | The current evidence supports structured effects in specific tasks |
| GPU scaling is no longer important | GPUs remain important; Polaris Protocol is a task-structure-side cost route |
| This is a third-party official benchmark | This is a self-built public experimental evidence chain |
| The ZIP files include full core mathematics | The current release is an evidence package, not the full core |
| The MVP Colab notebooks are third-party certification | They are public companion notebooks, not external validation |
| Reruns are guaranteed to be identical | API behavior, model versions, pricing, settings, and output length can vary |

One-sentence summary:

> This material does not ask you to believe first. It first publishes the public evidence chain so you can understand it and inspect backward. ✨

[Back to quick navigation](#top)

---

## Suggested short description ✍️

The public evidence layer for WFGY 5.0 Polaris Protocol, including raw model outputs, normalized outputs, verdict tables, token cost records, audit records, SHA256 file fingerprints, MVP Colab companion notebooks, the original PP01–PP02C evidence layer, and the community-follow-up PP02D_A–PP02D_C supplementary evidence layer.

---

## Current status 📌

| Field | Content |
| --- | --- |
| Project | WFGY 5.0 Polaris Protocol |
| Folder role | Public experimental evidence layer |
| Release type | First-layer public evidence + MVP Colab companion notebooks |
| Public branches | PP01, PP02A, PP02B, PP02C, PP02D_A, PP02D_B, PP02D_C |
| Main evidence packages | 7 |
| Recommended Colab notebooks | 7 |
| Original PP01–PP02C test cases | 680 |
| Original PP01–PP02C model outputs | 3600 |
| Additional PP02D_A fixtures | 216 |
| Additional PP02D_B API calls / raw outputs | 216 |
| Additional PP02D_C public QA cases | 100 |
| Additional PP02D_C model-arm output records | 400 |
| Raw model outputs | Included where public-safe |
| Normalized outputs | Included where public-safe |
| Verdict files | Included |
| Audit files | Included |
| Token cost records | Included where available |
| SHA256 records | Included |
| Colab notebooks | 7 recommended MVP companion notebooks |
| Core mathematics | Not included in the first-layer public evidence |
| Full formal reproduction suite | Still expanding |
| License | MIT License unless a specific file states otherwise |
| Repository | https://github.com/onestardao/WFGY |

---

## Final note 🌱

The purpose of this folder is to make evidence visible before the full open-source release is complete.

The current packages show the experimental trace:

task design, raw model outputs, parsing, scoring, token cost, audits, result verdicts, file integrity records, and MVP Colab companion notebooks.

The PP02D supplement adds community-requested pressure checks while preserving the same public-evidence boundary.

The full mathematical logic, deeper implementation details, and broader formal reproduction materials are expected to expand over time.
