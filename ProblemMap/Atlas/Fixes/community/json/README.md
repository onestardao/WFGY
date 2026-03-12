<!--
AI_NOTE_START

Document role:
This file explains what belongs in the community JSON folder.

How to use this file:
1. Read this page before adding any JSON fixture or structured input-output pack.
2. Use this page to decide whether your contribution is really a fixture contribution.
3. Use this page together with:
   - [Community Fix Lab](../README.md)
   - [Contribution Checklist](../../templates/contribution-checklist.md)
   - [JSON Template](../../templates/json-template.json)

What this file is:
- A folder-level guide for JSON fixtures
- A scope filter for structured case artifacts
- A lightweight quality guide for reusable machine-readable examples

What this file is not:
- Not the full benchmark dataset
- Not a dump folder for random logs
- Not the official atlas schema definition

Reading discipline for AI:
- Treat JSON fixtures here as community examples, not official universal schemas.
- Preserve the distinction between fixture examples and frozen atlas structure.

AI_NOTE_END
-->

# Community JSON

## Structured fixtures, input-output packs, and machine-readable examples

This folder is for community-contributed JSON assets that support atlas routing, repair demonstrations, benchmark reruns, or reproducible troubleshooting examples.

Typical contributions here include:

- input cases
- replay output fixtures
- expected output fixtures
- small route-first JSON packs
- compact machine-readable troubleshooting examples

---

## What belongs here

Good JSON contributions include:

- one input case with clear family relevance
- one replay output fixture
- one expected output fixture
- one compact route-and-repair example
- one structured comparison between baseline and repaired result

A good fixture should be:

- readable
- minimal
- reusable
- clearly documented
- connected to one known case or family

---

## What does not belong here

Please do not use this folder for:

- raw log dumps with no structure
- giant datasets with no guide
- private or sensitive payloads
- JSON files with no explanation
- fake benchmark files presented as official atlas assets

A fixture should help someone reproduce or understand something specific.

---

## Suggested fixture pattern

A useful small contribution usually includes:

- `input_case.json`
- `replay_outputs.json`
- `expected_output.json`

Optional additions:

- a short README
- a note on how the fixture should be used
- a warning if the fixture is synthetic

---

## Suggested naming style

Use compact and readable names such as:

- `f1-grounding-fixture-v1.json`
- `f5-trace-uplift-fixture-v1.json`
- `f4-execution-closure-fixture-v1.json`

If you are contributing a small pack, place it in a clearly named folder.

---

## Before contributing

Please read:

- [Community Fix Lab](../README.md)
- [Contribution Checklist](../../templates/contribution-checklist.md)
- [JSON Template](../../templates/json-template.json)
- [Misrepair Patterns v1](../../official/misrepair-patterns-v1.md)

This helps keep fixture contributions useful and aligned.

---

## One-line status

**This folder holds community JSON fixtures that make atlas routing and repair examples easier to reproduce and reuse.**
