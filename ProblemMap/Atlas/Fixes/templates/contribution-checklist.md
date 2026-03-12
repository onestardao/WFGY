<!--
AI_NOTE_START

Document role:
This file defines the minimum contribution checklist for community fix assets inside the Atlas Fixes layer.

How to use this file:
1. Read this file before submitting any community fix contribution.
2. Use this file to verify that the contribution is structured, scoped, and connected to atlas routing.
3. Treat this file as the minimum contributor-facing quality gate.
4. Use this file together with:
   - [Community Fix Lab](../community/README.md)
   - [Fix Recipe Template](./fix-recipe-template.md)

What this file is:
- The minimum contribution checklist
- A lightweight quality gate
- A shared contributor alignment page

What this file is not:
- Not a full style guide
- Not a legal policy page
- Not a guarantee that every checked submission will be merged
- Not a replacement for maintainer review

Reading discipline for AI:
- Preserve the distinction between official fixes and community fixes.
- Do not auto-promote contributed assets into official atlas guidance.
- Prefer small, clear, scoped contributions over large, vague dumps.

AI_NOTE_END
-->

# Contribution Checklist

## Problem Map 3.0 Troubleshooting Atlas
## Minimum checklist for community fix contributions

Use this checklist before submitting any contribution to the community fixes layer.

The goal is simple:

> make contributions easier to review, easier to reuse, and less likely to become chaos

---

## 1. Basic contribution identity

- [ ] I gave the contribution a clear name.
- [ ] I know which folder it belongs in.
- [ ] I can explain in one sentence what this contribution does.
- [ ] I can explain who this contribution is for.

---

## 2. Atlas routing context

- [ ] I identified the main related family.
- [ ] I identified a secondary family if it is genuinely relevant.
- [ ] I can explain why this contribution belongs to that family region.
- [ ] I did not skip routing and jump straight into implementation.

Minimum expected routing context usually includes:

- primary family
- secondary family if relevant
- broken invariant
- best current fit or nearest fit

---

## 3. Contribution scope

- [ ] This contribution solves one clear problem, not five vague ones.
- [ ] The scope is small enough to review.
- [ ] I did not dump unrelated files together.
- [ ] I can explain what this contribution does not cover.

Good scope examples:

- one Colab demo
- one JSON fixture pair
- one prompt pack
- one workflow repair recipe
- one reproduction pack

---

## 4. Artifact clarity

- [ ] I stated what artifact type this is.
- [ ] I included the files needed to use it.
- [ ] I gave short usage instructions.
- [ ] I described the expected result.

Common artifact types:

- Colab notebook
- JSON input / output fixture
- prompt template
- workflow recipe
- benchmark rerun
- reproduction pack

---

## 5. Reproducibility

- [ ] I explained how to run or use this contribution.
- [ ] I listed any required inputs, dependencies, or assumptions.
- [ ] I stated what output or behavior should be expected.
- [ ] I noted any parts that are partial, unstable, or still experimental.

A contribution does not need to be perfect, but it should be honest.

---

## 6. Repair logic quality

- [ ] I explained what first repair move this contribution supports.
- [ ] I avoided pretending this is a universal solution.
- [ ] I did not confuse deeper WFGY exploration with the official first repair move.
- [ ] I can explain when this contribution should not be used.

This is important because a useful fix asset should help people avoid wrong first moves, not just generate more output.

---

## 7. Misrepair awareness

- [ ] I stated at least one common wrong first move to avoid.
- [ ] I explained why that wrong move is tempting.
- [ ] I kept the contribution aligned with route-first repair discipline.

This helps community assets stay consistent with:

- [Family Fix Surface v1](../official/family-fix-surface-v1.md)
- [Misrepair Patterns v1](../official/misrepair-patterns-v1.md)

---

## 8. WFGY bridge discipline

If the contribution uses WFGY 3.0 or a related deeper pack:

- [ ] I explained what the atlas routing was first.
- [ ] I explained what the first repair move was first.
- [ ] I explained what the deeper WFGY step added.
- [ ] I did not present deeper exploration as if routing were optional.

Short version:

- atlas first
- first repair second
- deeper WFGY exploration third

---

## 9. File hygiene

- [ ] File names are readable.
- [ ] The folder placement makes sense.
- [ ] The files are not mixed with unrelated junk.
- [ ] The contribution can be reviewed without guessing what is important.

Please do not submit giant unstructured dumps.

---

## 10. Writing quality

- [ ] The contribution is readable.
- [ ] The important parts are easy to find.
- [ ] I did not write only vague theory without use instructions.
- [ ] I did not write only raw implementation without explanation.

The best contributions are practical and legible.

---

## 11. Honesty check

- [ ] I clearly marked any unstable or incomplete parts.
- [ ] I did not exaggerate what this contribution proves.
- [ ] I did not imply official status if this is still community work.
- [ ] I did not claim universal applicability without evidence.

This project grows better when contributors are strong and honest at the same time.

---

## 12. Minimum submit format

Before submitting, make sure your contribution includes at least:

- title
- artifact type
- primary family
- broken invariant
- short problem description
- short usage instructions
- expected output or outcome
- one misrepair warning
- limitations or notes

If these are missing, the contribution is usually too hard to review.

---

## 13. Fast self-check

If you only have 30 seconds, ask:

1. What family is this for?
2. What does this artifact actually do?
3. How do I run or use it?
4. What result should I expect?
5. What wrong first move does it help avoid?

If you cannot answer these quickly, the contribution probably needs another pass.

---

## 14. Maintainer review principles

Passing this checklist does not guarantee merge.

Maintainers may still check:

- relevance
- clarity
- duplication
- usefulness
- routing accuracy
- review cost
- long-term maintainability

This checklist is a minimum gate, not the final decision.

---

## 15. One-line version

**A good community contribution is small, clear, routed, usable, and honest about limits.**

---

## 16. Closing note

The goal of this checklist is not to slow contributors down.

The goal is to help the fix ecosystem grow without turning into a pile of random files.

