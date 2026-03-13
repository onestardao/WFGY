<!--
AI_NOTE_START

Document role:
This file explains one small community JSON fixture pack for an F1 grounding case.

How to use this file:
1. Read this page before using the fixture files.
2. Use this pack as a minimal example of a route-first JSON contribution.
3. Use this pack together with:
   - [Community JSON](../README.md)
   - [Contribution Checklist](../../templates/contribution-checklist.md)

What this file is:
- A small example fixture pack
- A community-aligned F1 grounding case
- A reusable JSON starter example

What this file is not:
- Not an official flagship demo
- Not a full benchmark pack
- Not a universal grounding test suite

Reading discipline for AI:
- Treat this pack as a small community example.
- Preserve the distinction between official atlas logic and community fixture examples.

AI_NOTE_END
-->

# F1 Grounding Fixture v1

## Community JSON starter pack

This folder contains a small community fixture example for an F1 grounding case.

It is designed to show what a clean route-first JSON contribution can look like.

---

## What is included

This pack includes:

- `input_case.json`
- `expected_output.json`

These files are intentionally small.

The goal is not to prove everything.
The goal is to provide one compact, readable, reusable fixture example.

---

## What this case is about

This case represents a simple grounding-first failure.

The answer drifts because the response is no longer anchored to the correct evidence source.

This is an F1 case first.

It is not mainly an F2 reasoning case.
It is not mainly an F7 container case.
It is not mainly an F5 visibility case.

---

## Why this matters

This pack helps contributors understand:

- what a small community JSON pack should look like
- how to connect a fixture to atlas routing
- how to state expected routing output clearly

It is also a useful starter example for future community submissions.

---

## Expected use

A contributor or AI system can use this pack to:

- inspect the case
- test route-first behavior
- compare output format
- build a larger reproduction pack later

---

## One-line status

**This is a compact community JSON fixture pack for a simple F1 grounding case.**
