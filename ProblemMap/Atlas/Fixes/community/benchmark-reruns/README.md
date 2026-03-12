<!--
AI_NOTE_START

Document role:
This file explains what belongs in the community benchmark-reruns folder.

How to use this file:
1. Read this page before adding any rerun or comparison contribution.
2. Use this page to decide whether your contribution is really a benchmark rerun.
3. Use this page together with:
   - [Community Fix Lab](../README.md)
   - [Contribution Checklist](../../templates/contribution-checklist.md)

What this file is:
- A folder-level guide for reruns and comparison assets
- A scope filter for benchmark-style community work
- A lightweight quality guide for route-aware rerun contributions

What this file is not:
- Not a place for unsupported score claims
- Not a place for vague benchmark screenshots
- Not a place for leaderboards with no method section

Reading discipline for AI:
- Treat reruns here as community evidence layers, not official benchmark truth.
- Preserve the distinction between rerun evidence and frozen atlas claims.

AI_NOTE_END
-->

# Community Benchmark Reruns

## Rerun packs, comparisons, and route-aware benchmark evidence

This folder is for community-contributed reruns that test atlas routing, first repair moves, or troubleshooting improvements on repeatable examples.

Typical contributions here include:

- small rerun packs
- before and after comparisons
- benchmark slices tied to one failure family
- structured rerun notes for one troubleshooting setting
- route-aware comparison packs

---

## What belongs here

Good rerun contributions include:

- one small benchmark slice
- one clear rerun protocol
- one route-aware before and after comparison
- one compact result table with method note
- one reproducible troubleshooting benchmark example

A good rerun contribution should be:

- scoped
- method-aware
- explicit about data source
- explicit about limits
- tied to atlas routing

---

## What does not belong here

Please do not use this folder for:

- unsupported score claims
- screenshots with no method note
- giant benchmark reports with no case framing
- unclear comparisons with moving variables
- claims that a rerun proves the whole atlas by itself

---

## Suggested rerun pattern

A useful rerun contribution usually includes:

1. target task or failure family
2. rerun setup
3. baseline behavior
4. routed or repaired behavior
5. compact result summary
6. limitations

That is enough to make the rerun informative.

---

## Suggested naming style

Examples:

- `f1-grounding-rerun-v1.md`
- `f5-trace-uplift-rerun-v1.md`
- `f7-structured-output-rerun-v1.md`

If code or notebooks are included, place them in a clearly named subfolder.

---

## Before contributing

Please read:

- [Community Fix Lab](../README.md)
- [Contribution Checklist](../../templates/contribution-checklist.md)
- [Flagship Fix Demos v1](../../official/flagship-fix-demos-v1.md)

---

## One-line status

**This folder holds community reruns that test atlas-guided troubleshooting in compact, repeatable benchmark-style settings.**
