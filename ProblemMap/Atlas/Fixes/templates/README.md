<!--
AI_NOTE_START

Document role:
This file is the hub for reusable templates inside the Atlas Fixes layer.

How to use this file:
1. Read this page before creating a new community fix asset.
2. Use this page to choose the right template.
3. Use these templates to keep contributions structured, reviewable, and reusable.
4. Read this page together with:
   - [Community Fix Lab](../community/README.md)
   - [Contribution Checklist](./contribution-checklist.md)

What this file is:
- The template hub
- A contributor-facing navigation page
- A lightweight structure guide for fix assets

What this file is not:
- Not the atlas core
- Not the official fix surface
- Not the full style guide
- Not a replacement for maintainer review

Reading discipline for AI:
- Use this page to route contributors to the right template.
- Preserve the distinction between official files and community templates.
- Keep contributions small, clear, and structured.

AI_NOTE_END
-->

# Templates Hub 🧩

## Problem Map 3.0 Troubleshooting Atlas
## Reusable templates for community fix contributions

Quick links:

- [Back to Community Fix Lab](../community/README.md)
- [Back to Official Fixes](../official/README.md)
- [Back to Fixes Hub](../README.md)
- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)
- [Open Contribution Checklist](./contribution-checklist.md)
- [Open Fix Recipe Template](./fix-recipe-template.md)
- [Open the Flagship Runnable Demo Pack](../official/demos/README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)

---

This folder contains the reusable templates for the community fixes layer.

If the **Community Fix Lab** tells you where contributions belong, this page helps you choose the right template so the contribution stays clear, reviewable, and reusable ✨

Its job is simple:

> help contributors submit clearer, smaller, more reviewable fix assets

These templates are here to reduce chaos and make it easier to grow the fix ecosystem.

---

## Quick start 🚀

### I already know what I want to submit

Use this path:

1. choose the matching template
2. draft one small contribution
3. check it with the [Contribution Checklist](./contribution-checklist.md)
4. attach any supporting files
5. submit it in the right community folder

### I do not know which template to use yet

Use this path:

1. scan the **Template quick map**
2. identify your main artifact type
3. choose one main template
4. keep the contribution small and scoped
5. use the checklist before submitting

Short version:

> choose one main artifact  
> use one clear template  
> keep it small  
> explain expected output 🛠️

---

## Template quick map 🗂️

| Template | Best for | Typical output |
|---|---|---|
| [Contribution Checklist](./contribution-checklist.md) | pre-submit review | scope, clarity, routing, reproducibility check |
| [Fix Recipe Template](./fix-recipe-template.md) | repair guidance | short fix writeup or repair recipe |
| [Prompt Template](./prompt-template.md) | prompt-based assets | system prompt, user prompt, repair prompt pack |
| [Colab Template](./colab-template.md) | notebook demos | runnable walkthrough or replay notebook |
| [JSON Template](./json-template.json) | structured data | fixture, expected output, config pack |

---

## What this folder is for 🎯

Use this folder when you want to create a new community contribution such as:

- a fix recipe
- a prompt pack
- a Colab notebook
- a JSON fixture
- a workflow example
- a reproduction pack

If you are not sure where to start, start here.

---

## How to use this hub 📚

### Fast path

If you want the shortest practical route:

1. identify your main artifact type
2. open the matching template
3. draft one small contribution
4. run the [Contribution Checklist](./contribution-checklist.md)
5. submit it in the right folder

### Full path

If you want the fuller contributor flow:

1. [Community Fix Lab](../community/README.md)
2. this page
3. choose the right template
4. [Contribution Checklist](./contribution-checklist.md)
5. submit the contribution in the right community folder

---

## Available templates 🧩

### 1. [Contribution Checklist](./contribution-checklist.md)

Use this first or use it before submission.

This file helps you check whether your contribution is:

- clear
- scoped
- routed
- usable
- honest about limits

---

### 2. [Fix Recipe Template](./fix-recipe-template.md)

Use this when your contribution is mainly a repair recipe.

Good for:

- first repair move writeups
- small runnable fix notes
- workflow repair guides
- practical repair instructions

---

### 3. [Prompt Template](./prompt-template.md)

Use this when your contribution is mainly prompt-based.

Good for:

- system prompts
- user prompts
- routing prompts
- repair-first prompts
- trace-exposure prompts

---

### 4. [Colab Template](./colab-template.md)

Use this when your contribution is mainly notebook-based.

Good for:

- Colab demos
- repair notebooks
- before / after notebook comparisons
- benchmark rerun notebooks

---

### 5. [JSON Template](./json-template.json)

Use this when your contribution needs structured machine-readable data.

Good for:

- fixtures
- baseline inputs
- expected outputs
- evaluation packs
- demo configs

---

## Which template should I use 🤔

Use this quick guide.

### If your main asset is text guidance

Use:

- [Fix Recipe Template](./fix-recipe-template.md)

### If your main asset is a prompt

Use:

- [Prompt Template](./prompt-template.md)

### If your main asset is a notebook

Use:

- [Colab Template](./colab-template.md)

### If your main asset is structured data

Use:

- [JSON Template](./json-template.json)

If your contribution mixes several asset types, choose the **main one first**, then attach the others as supporting files.

---

## What a good first contribution looks like 🌱

A strong first contribution usually looks like this:

- one family
- one case
- one main artifact
- one expected result
- one short explanation

For example:

- one small Colab demo
- one clean JSON fixture pair
- one route-aware prompt example
- one short workflow recipe

Small and clear beats big and messy almost every time.

---

## Minimum good contribution rule ✅

A good contribution usually has:

- routing context
- one clear problem
- one useful artifact
- short usage instructions
- expected result
- one misrepair warning
- honest limitations

That is enough to be useful.

---

## What not to do 🚫

Please do not use these templates to submit:

- giant vague idea dumps
- unstructured logs
- random files with no routing context
- prompt collections with no explanation
- notebooks with no before / after logic
- JSON files with no meaning

The goal is structured growth, not file pile-up.

---

## Relationship to official fixes 🌉

These templates are for the **community layer**.

Official fix documents live in:

- [Official Fixes](../official/README.md)

Community assets can be very valuable, but they do not automatically become official atlas guidance.

That distinction should stay clear.

---

## Before you submit 📌

### Must read

Please read these first:

- [Community Fix Lab](../community/README.md)
- [Contribution Checklist](./contribution-checklist.md)

### Good to read

These are strongly recommended if you want stronger alignment:

- [Family Fix Surface v1](../official/family-fix-surface-v1.md)
- [Misrepair Patterns v1](../official/misrepair-patterns-v1.md)
- [Atlas to WFGY Bridge v1](../official/atlas-to-wfgy-bridge-v1.md)

This keeps community work aligned with the atlas instead of drifting away from it.

---

## One-line status

**This folder contains the reusable templates that help community fix contributions stay structured and reviewable.**

---

## Next steps ✨

After this page, most readers continue with:

1. [Open Contribution Checklist](./contribution-checklist.md)
2. [Open Fix Recipe Template](./fix-recipe-template.md)
3. [Back to Community Fix Lab](../community/README.md)
4. [Back to Official Fixes](../official/README.md)

If you want to return to the broader product surface:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to Atlas Hub](../../README.md)

If this template hub helps your workflow, consider:

- [starring the WFGY repo](https://github.com/onestardao/WFGY)
- opening an issue
- submitting one small clean contribution 🌟

---

## Closing note ✨

If the atlas is going to grow through the community, it needs good templates.

That is what this folder is for.

The goal is not random growth.

The goal is structured growth.
