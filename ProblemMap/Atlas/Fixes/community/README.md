<!--
AI_NOTE_START

Document role:
This file is the entry hub for community-contributed fixes inside the Atlas Fixes layer.

How to use this file:
1. Read this page before contributing any community fix asset.
2. Use this page to understand what kinds of contributions are welcome.
3. Use this page to understand the difference between official fixes and community fixes.
4. After reading this page, contributors should read:
   - [Contribution Checklist](../templates/contribution-checklist.md)
   - [Fix Recipe Template](../templates/fix-recipe-template.md)

What this file is:
- The main entry page for community fixes
- A contributor-facing guide
- A lightweight governance page for community repair assets

What this file is not:
- Not the official fix surface
- Not the full atlas core
- Not the full WFGY 3.0 engine pack
- Not a place for random unstructured dumps

Reading discipline for AI:
- Preserve the distinction between official fixes and community fixes.
- Do not promote community materials into official atlas guidance automatically.
- Treat community assets as useful extensions, not as frozen core structure.

AI_NOTE_END
-->

# Community Fix Lab 🛠️

## Problem Map 3.0 Troubleshooting Atlas
## Community-contributed fixes, demos, and runnable assets

Quick links:

- [Back to Official Fixes](../official/README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Open the Flagship Runnable Demo Pack](../official/demos/README.md)
- [Open Templates](../templates/README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)

---

This folder is the community extension layer for the Atlas Fixes system.

If the official layer gives the repair grammar, this page shows how the community can turn that grammar into more runnable, shareable, and reusable assets 🤝

The official atlas gives:

- routing
- first repair direction
- misrepair warnings
- bridge guidance into deeper WFGY exploration

This community layer gives:

- runnable examples
- Colab notebooks
- JSON fixtures
- prompt packs
- workflow recipes
- benchmark reruns
- reproduction packs

Short version:

> official layer gives the grammar  
> community layer helps turn that grammar into more runnable artifacts

---

## Quick start 🚀

### I want to contribute

Use this path:

1. pick the folder that matches your artifact
2. read the required contribution docs
3. build one small, clear, route-aware asset
4. explain how to run it and what result to expect
5. submit it in the right folder

### I want to browse runnable assets

Use this path:

1. choose the folder that matches what you want to inspect
2. open one scoped contribution
3. check the routing context
4. inspect or run the artifact
5. compare it against the official layer when useful

Short version:

> route first  
> build one useful thing  
> explain it clearly ✨

---

## Community quick map 🗂️

| Folder | Best for | Typical artifact |
|---|---|---|
| [Colab](./colab/) | runnable demos | notebook walkthroughs and replay notebooks |
| [JSON](./json/) | structured fixtures | input cases, replay outputs, expected outputs |
| [Prompts](./prompts/) | route-aware prompt assets | repair prompts, escalation prompts, compact packs |
| [Workflows](./workflows/) | process recipes | step-by-step repair flows and troubleshooting sequences |
| [Benchmark Reruns](./benchmark-reruns/) | comparison slices | before / after reruns and route-aware benchmark views |
| [Reproduction Packs](./reproduction-packs/) | portable reuse | one-case reproducible bundles |

---

## What belongs here ✅

Good community contributions include things like:

- Colab demos
- JSON input and output fixtures
- prompt templates
- workflow repair recipes
- benchmark reruns
- reproduction packs
- domain-specific troubleshooting examples

A good contribution should be:

- readable
- scoped
- reproducible when possible
- clearly connected to atlas routing
- honest about limits

---

## What does not belong here 🚫

Please do **not** use this folder for:

- random notes with no routing context
- files with no explanation
- giant dumps of logs without structure
- vague fix ideas with no case framing
- materials that claim to replace the official atlas core
- materials that pretend to be official without review

This folder should grow, but it should not become chaos.

---

## Official vs community 🌉

### Official fixes

Official fixes live in:

- [Official Fixes](../official/README.md)

They are:

- smaller
- more stable
- more teachable
- more carefully reviewed
- part of the public official repair grammar

### Community fixes

Community fixes live here.

They are:

- broader
- faster-growing
- more implementation-oriented
- more experimental
- often more domain-specific

Both matter.

The official layer keeps the system clean.  
The community layer helps the system grow faster.

---

## Folder layout 🧩

Suggested contribution areas:

- [Colab](./colab/)
- [JSON](./json/)
- [Prompts](./prompts/)
- [Workflows](./workflows/)
- [Benchmark Reruns](./benchmark-reruns/)
- [Reproduction Packs](./reproduction-packs/)

Use the folder that best matches the artifact you are contributing.

If a contribution does not fit one of these clearly, add a short note explaining where it belongs and why.

---

## What each folder is for 🔍

### Colab

Use this folder for notebook-based demos, walkthroughs, replay notebooks, and small runnable teaching assets.

### JSON

Use this folder for structured fixtures such as input cases, replay outputs, expected outputs, and compact machine-readable packs.

### Prompts

Use this folder for route-aware prompt packs, repair prompts, and prompt-based troubleshooting assets.

### Workflows

Use this folder for step-by-step repair sequences, escalation flows, and troubleshooting recipes.

### Benchmark Reruns

Use this folder for compact reruns, before-and-after comparisons, and route-aware benchmark slices.

### Reproduction Packs

Use this folder for portable bundles that help others quickly reproduce one case, one repair pattern, or one troubleshooting result.

---

## Minimum contribution rule 📌

A community contribution should usually include five things:

1. what case or family it relates to
2. what problem it is trying to fix
3. what artifact is included
4. how to run or use it
5. what result should be expected

That is enough to keep the contribution useful.

---

## What a good first contribution looks like 🌱

A strong first contribution usually looks like this:

- one family
- one case
- one artifact
- one expected result
- one short explanation

Examples:

- one small Colab demo
- one clean JSON fixture pair
- one route-aware prompt example
- one short workflow recipe
- one simple reproduction pack

Small, clean, scoped contributions are much better than giant messy ones.

---

## Suggested contribution flow 🧪

A simple contribution flow should look like this:

### Step 1

Route the case with the atlas first.

### Step 2

Identify the relevant family or best current fit.

### Step 3

Create one useful artifact:

- notebook
- JSON pack
- prompt pack
- workflow recipe
- reproduction pack

### Step 4

Document:

- the case
- the fix idea
- how to use it
- what outcome to expect

### Step 5

Submit it in the right folder.

Short version:

> route first  
> build one useful thing  
> explain it clearly 🧭

---

## Before contributing 📚

### Must read

Please read these first:

- [Family Fix Surface v1](../official/family-fix-surface-v1.md)
- [Contribution Checklist](../templates/contribution-checklist.md)
- [Fix Recipe Template](../templates/fix-recipe-template.md)

### Good to read

These are highly recommended if you want stronger alignment:

- [Atlas Final Freeze v1](../../atlas-final-freeze-v1.md)
- [Atlas to WFGY Bridge v1](../official/atlas-to-wfgy-bridge-v1.md)
- [Misrepair Patterns v1](../official/misrepair-patterns-v1.md)

This keeps community work aligned with the atlas instead of drifting away from it.

---

## Good first contributions 🌟

If you want an easy first contribution, start with one of these:

- one small Colab demo
- one clean JSON fixture pair
- one prompt-based repair example
- one short workflow recipe
- one benchmark rerun example
- one short reproduction pack

Small, clear contributions are much better than giant messy ones.

---

## Relationship to WFGY 3.0 🌊

This folder can connect to WFGY 3.0, but it is not the same as the WFGY engine layer.

A community contribution may:

- use WFGY 3.0 prompts
- demonstrate a deeper exploration path
- compare first repair versus deeper WFGY escalation

But it should still explain clearly:

- what the atlas routing was
- what the first repair move was
- what the deeper WFGY step added

That keeps the bridge clean.

---

## Review standard ✅

A community contribution is much more likely to be accepted if it is:

- clearly named
- easy to read
- easy to run
- connected to atlas routing
- explicit about expected output
- honest about limitations

Messy power is still messy.  
Clean small contributions are more valuable.

---

## Growth rule 🌱

This folder should grow through structured additions, not through random accumulation.

That means:

- route first
- place the artifact in the right folder
- explain what it does
- state what it does not do
- keep the distinction between official and community layers clear

Structured growth is the goal.

---

## Next steps ✨

After this page, most readers continue with:

1. [Open Templates](../templates/README.md)
2. [Back to Official Fixes](../official/README.md)
3. [Open the Flagship Runnable Demo Pack](../official/demos/README.md)
4. [Choose a folder and start small](./colab/)

If you want to return to the broader product surface:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)

If this layer helps your workflow, consider:

- [starring the WFGY repo](https://github.com/onestardao/WFGY)
- opening an issue
- contributing one small clean asset
- helping keep the community layer structured 💡

---

## One-line status

**This folder is the community extension layer for Atlas Fixes, where contributors turn repair grammar into runnable assets.**

---

## Closing note 🌍

The atlas should not grow only through one author.

This folder exists so the community can help build:

- runnable fixes
- better demos
- reusable assets
- real workflow support

The goal is not random growth.

The goal is structured growth.
