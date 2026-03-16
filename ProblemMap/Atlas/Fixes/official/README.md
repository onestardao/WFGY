<!--
AI_NOTE_START

Document role:
This file is the main hub for the official fixes layer inside the Atlas Fixes system.

How to use this file:
1. Treat this page as the entry point for official repair-facing guidance.
2. Use this page to understand which materials belong to the stable public repair layer.
3. Use this page to distinguish:
   - official first repair grammar
   - official misrepair warnings
   - official atlas-to-WFGY bridge notes
   - official flagship demos
4. Read this page before adding new official fix-facing documents or modifying existing ones.

What this file is:
- The hub for the official fixes layer
- The stable public repair-facing layer
- A navigation page for official demos and repair guidance

What this file is not:
- Not the atlas core
- Not the community contribution area
- Not the templates area
- Not the full WFGY 3.0 engine pack
- Not the full auto-repair planning layer
- Not a dump folder for every experimental implementation

Reading discipline for AI:
- Preserve the distinction between official fixes, community fixes, templates, and future planning layers.
- Treat this folder as the stable first public repair-facing layer.
- Do not silently promote community or experimental materials into this official layer.
- Do not overclaim that every routed case already has a full runnable repair implementation.

AI_NOTE_END
-->

# Official Fixes

## Problem Map 3.0 Troubleshooting Atlas
## Stable first repair grammar, misrepair warnings, bridge notes, and flagship demos

Quick links:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)
- [Back to Fixes Hub](../README.md)
- [Open the Flagship Runnable Demo Pack](./demos/README.md)
- [Get the Atlas Router TXT](../../troubleshooting-atlas-router-v1.txt)

---

This folder is the **official repair-facing layer** of the Atlas Fixes system.

If you arrived here after the demos, this is the page that explains where the stable public repair layer begins and how to read it.

The atlas tells you where the failure lives.  
The casebook teaches how to recognize the cut.  
The adapter helps route the case with discipline.  
This official layer helps answer the next practical question:

> **What should be tried first after correct routing?**

This layer is intentionally smaller and more stable than the community layer.

Its goal is not to store every possible implementation.  
Its goal is to provide a clean, reusable, public-facing first repair surface.

---

## Quick start

If you want the shortest useful path through the official layer, use this order:

1. [Family Fix Surface v1](./family-fix-surface-v1.md)  
2. [Misrepair Patterns v1](./misrepair-patterns-v1.md)  
3. [Flagship Runnable Demo Pack](./demos/README.md)  
4. [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md) only if deeper escalation is needed

If you came here after the demos, the fastest next step is usually:

1. [Family Fix Surface v1](./family-fix-surface-v1.md)
2. [Misrepair Patterns v1](./misrepair-patterns-v1.md)

Short version:

> route first  
> choose the first repair move  
> avoid the wrong first move  
> escalate only if needed

---

## What this folder is for

This folder exists to hold the official materials that connect atlas diagnosis to first repair action.

That includes:

- family-level first repair directions
- common misrepair patterns
- official bridge notes into deeper WFGY exploration
- flagship demos that show route-to-repair flow
- shared demo helpers that keep demo assets consistent

Short version:

> atlas gives the cut  
> official fixes give the first public repair grammar

---

## What belongs here

Materials in this folder should be stable enough to function as official public repair guidance.

Good examples include:

- family-level first repair guides
- reusable route-to-repair logic
- common wrong-first-move warnings
- official bridge notes from atlas to deeper WFGY exploration
- a small number of flagship demos
- shared support files for official demo consistency

This layer should be:

- compact
- readable
- reusable
- teachable
- stable enough to cite
- safe enough to place near the public-facing product surface

---

## What does not belong here

This folder should **not** become:

- a giant archive of experimental notes
- a random collection of implementation drafts
- a place for community-contributed packs
- a place for templates and submission rules
- a full auto-repair planning lab
- a replacement for the atlas core

If a material is:

- fast-growing
- contributor-driven
- narrow in scope
- highly experimental
- still rough

then it likely belongs in the community layer or a future planning layer instead.

---

## Relationship to the rest of the Fixes system

This folder is only one part of the larger Fixes structure.

### Parent hub

- [Fixes Hub](../README.md)

Use the parent hub if you want the full repair-facing map.

### Community extension layer

- [Community Fix Lab](../community/README.md)

Use the community layer for runnable community contributions such as Colab notebooks, JSON packs, prompt packs, workflows, reruns, and reproduction packs.

### Templates layer

- [Templates](../templates/README.md)

Use the templates layer when contributing structured community materials.

### Future-facing planning layer

A deeper planning layer may continue growing elsewhere in the Fixes system, but it should not replace the stable official public layer represented here.

---

## Core principle

The official fixes layer must preserve this order:

> **route first, then repair**

That means:

1. determine the primary family
2. identify the broken invariant
3. identify the best current fit
4. only then choose the first repair direction
5. only then decide whether deeper escalation is needed

This matters because many bad fixes are not bad in isolation.  
They are bad because they start from the wrong cut.

---

## Recommended reading order

### Fast path

Use this if you want the shortest practical route through the official layer:

1. [Family Fix Surface v1](./family-fix-surface-v1.md)
2. [Misrepair Patterns v1](./misrepair-patterns-v1.md)
3. [Flagship Runnable Demo Pack](./demos/README.md)
4. [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md) if needed

### Full path

Use this if you want the full official repair-facing story in the intended order:

1. [Atlas Final Freeze v1](../../atlas-final-freeze-v1.md)
2. [Canonical Casebook v1](../../canonical-casebook-v1.md)
3. [Atlas-to-AI Adapter v1](../../atlas-to-ai-adapter-v1.md)
4. [Family Fix Surface v1](./family-fix-surface-v1.md)
5. [Misrepair Patterns v1](./misrepair-patterns-v1.md)
6. [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md)
7. [Flagship Runnable Demo Pack](./demos/README.md)

---

## Official document map

### Core official repair documents

- [Family Fix Surface v1](./family-fix-surface-v1.md)  
  The first official family-level repair layer.  
  Explains what should usually be tried first after correct routing.

- [Misrepair Patterns v1](./misrepair-patterns-v1.md)  
  The official wrong-first-move layer.  
  Shows how repair often goes wrong when the cut is misunderstood or the wrong family logic is applied.

- [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md)  
  The bridge from compact atlas repair grammar into deeper WFGY exploration.  
  Explains how first repair direction and deeper structural exploration differ.

---

## Official demos

- [Flagship Runnable Demo Pack](./demos/README.md)

This is the official runnable proof layer for the public repair-facing system.

Current flagship demos include:

- [Demo 1 · F1 Grounding Anchor Recovery](./demos/demo-f1-grounding-anchor/README.md)
- [Demo 2 · F5 Observability First](./demos/demo-f5-observability-first/README.md)
- [Demo 3 · F4 Execution Closure](./demos/demo-f4-execution-closure/README.md)
- [Demo 4 · F7 Container Fidelity](./demos/demo-f7-container-fidelity/README.md)

These demos matter because they do not only classify.  
They show how correct routing changes the first repair move.

If you want the runnable proof layer first, start here:

- [Open the Flagship Runnable Demo Pack](./demos/README.md)

---

## Shared demo support

- [Shared Demo Helpers](./demos/shared/README.md)

This area exists to keep official demo assets more consistent.

Typical shared materials may include:

- display helpers
- demo utilities
- shared routing schema notes
- light reusable support code

This layer helps the official demos stay cleaner without turning the whole folder into a code dump.

---

## How the official layer should be used

A healthy official use flow should look like this:

### Step 1

Use the atlas and casebook to route the case.

### Step 2

Use the official fix surface to identify the first repair move.

### Step 3

Use misrepair patterns to avoid the most common wrong first move.

### Step 4

If the case needs more depth, use the atlas-to-WFGY bridge.

### Step 5

If the case benefits from runnable assets, use the official demos or move into the community layer.

Short version:

> route  
> first repair  
> avoid misrepair  
> escalate if needed  
> implement if useful

---

## Why this folder matters

Without an official fixes layer, the atlas risks being read as only a classification system.

With this folder, the atlas becomes more actionable:

- it teaches what to try first
- it teaches what not to try first
- it supports reusable product-facing repair grammar
- it connects cleanly to deeper WFGY exploration
- it supports official demos without collapsing into chaos

This is why this folder matters.

It is the layer where the atlas starts to become not only a map, but a disciplined repair-facing system.

---

## Stability rule

This layer should remain:

- smaller than the community layer
- cleaner than the community layer
- more stable than the community layer
- easier to cite than the community layer

If this layer grows too fast or absorbs too many rough materials, it will lose its role.

The official layer should stay sharp.

---

## Next steps

After this page, most readers continue with:

1. [Family Fix Surface v1](./family-fix-surface-v1.md)
2. [Misrepair Patterns v1](./misrepair-patterns-v1.md)
3. [Flagship Runnable Demo Pack](./demos/README.md)
4. [Atlas to WFGY Bridge v1](./atlas-to-wfgy-bridge-v1.md)

If you want to return to the broader product surface:

- [Back to Atlas landing page](../../../wfgy-ai-problem-map-troubleshooting-atlas.md)
- [Back to AI Eval Evidence](../../ai-eval-evidence.md)
- [Back to Atlas Hub](../../README.md)

If this layer helps your workflow, consider:

- [starring the WFGY repo](https://github.com/onestardao/WFGY)
- opening an issue
- testing the official demo pack
- contributing to the community layer later

---

## One-line status

**This folder is the stable public repair-facing layer of the Atlas system, combining first repair grammar, misrepair warnings, bridge notes, and official flagship demos.**

---

## Closing note

The atlas tells you where the failure lives.

The official fixes layer helps answer what should be tried next.

It does not claim that every case already has a full implementation.  
It provides the first stable public repair surface, so deeper exploration and practical execution can grow from a clean base.
