# Platform Ban Log: Zenodo & Reddit Incident (Aug 2025)

**TL;DR**
On the same day, my **Zenodo account was auto-flagged and removed** (reason shown: “Spam”; user blocked) and my **Reddit account `u/wfgy_engine` was disabled** shortly after I edited several posts to replace broken Zenodo DOIs with GitHub links. Appeals have been submitted to both platforms. In the meantime, **all files have been migrated to GitHub** and are downloadable **in-repo** without external mirrors. This makes forks reproducible out of the box.

---

## 1) What happened

* **Date:** mid-August 2025
* **Event A — Zenodo:** My primary record for WFGY Core 2.0 was removed with a tombstone page stating:
  *Reason: Spam · Removed by: System (automatic) · Note: User was blocked*.
  This effectively blocked my account and made previous DOIs unreachable.
* **Event B — Reddit:** Within hours of replacing \~7–8 of my earlier Reddit posts’ links (DOI → GitHub) to keep content accessible, my account `u/wfgy_engine` became inaccessible/disabled.

**Impact:**

* DOIs went dead; discussions and guides that referenced them broke.
* Community members could no longer fetch the files from Zenodo.
* I temporarily lost a public discussion channel on Reddit.

---

## 2) Why this may have occurred (hypotheses)

These are **hypotheses**, not accusations:

1. **Automated false positive (Zenodo):**

   * Minimal/text-only math artifacts (no executables) + rapid early interest can match “spammy” patterns for automated filters.
   * Multiple versions/uploads around the same family of files may look like “duplication” to risk systems.

2. **Coordinated or clustered reports (cross-platform):**

   * WFGY grew quickly (GitHub \~600 stars in \~60 days; one paper >4,000 downloads in \~60 days).
   * Sudden visibility sometimes attracts mass reports or misunderstandings (“promotion” vs. research mirrors).

3. **Link-update burst (Reddit):**

   * Editing several posts in a short window (to replace dead DOIs with GitHub links) can trip an automated anti-spam rule.

> Note: None of my artifacts were commercial or executable. They are **MIT-licensed, text-only mathematical protocols** used for reproducible LLM reasoning evaluations.

---

## 3) Current status

* **Zenodo:** Formal appeal submitted from **[hello@onestardao.com](mailto:hello@onestardao.com)** requesting manual review and account reinstatement.
* **Reddit:** Appeal submitted (contact and appeals channels) requesting clarification and restoration of `u/wfgy_engine`.
* **Expectation:** I’m prepared for the possibility that reinstatement may not happen quickly (or at all), so I have fully de-risked distribution.

---

## 4) What changed for users (the fix)

I moved **all public files** into the GitHub repository so **every asset is downloadable in-repo**:

* **Repo:** `https://github.com/onestardao/WFGY`
* **Core engine files:**

  * `core/WFGY_Core_OneLine_v2.0.txt`
  * `core/WFGY_Core_Flagship_v2.0.txt`
* **Primary book/PDF:**

  * `I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf`
* **Papers (PDFs):**

  * `I_am_not_lizardman/papers/…` (all individual papers live here)

**Why this helps:**

* Forks now contain everything needed; **no external mirrors required**.
* CI, notebooks, and demos can reference **stable, in-repo paths**.
* Community packaging or downstream mirrors can be built from a single source of truth.

---

## 5) Migration map (DOI → GitHub)

All DOIs that previously pointed to Zenodo have been replaced by **direct GitHub links** to the exact PDFs.
Examples (non-exhaustive):

* WFGY book/PDF →
  `I_am_not_lizardman/WFGY_All_Principles_Return_to_One_v1.0_PSBigBig_Public.pdf`
* Papers →
  `I_am_not_lizardman/papers/Semantic_Relativity_Theory_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/Semantic_BioEnergy_Plants_vs_Einstein_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/Semantic_Field_Induced_Objective_Collapse_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/Semantic_Field_Fifth_Force_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/BERT-Based_Semantic_Entropy_under_Landauer's_Principle_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/Semantic_Holography_CausalFields_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/TrinityOfLight_Hypothesis_v1.0_PSBigBig_Public.pdf`
  `I_am_not_lizardman/papers/Asymmetric_SelfConsistency_AI_Verification_v1.0_PSBigBig_Public.pdf`

(Where needed, README tables now link to these in-repo files.)

---

## 6) How to download (developers)

**Direct browser download:** click any file in the repo; GitHub shows a preview and a “Download raw file” option.
**Scripted:**

```bash
# Example: fetch OneLine and Flagship
curl -L -o WFGY_Core_OneLine_v2.0.txt \
  https://raw.githubusercontent.com/onestardao/WFGY/main/core/WFGY_Core_OneLine_v2.0.txt

curl -L -o WFGY_Core_Flagship_v2.0.txt \
  https://raw.githubusercontent.com/onestardao/WFGY/main/core/WFGY_Core_Flagship_v2.0.txt
```

(Adjust paths similarly for PDFs under `I_am_not_lizardman/`.)

---

## 7) Verification & provenance

* **Open-source repo history:** commit logs and PRs document the evolution of WFGY.
* **Community signals:** \~600+ GitHub stars in \~60 days (publicly visible).
* **Usage evidence:** one public paper surpassed **4,000+ downloads** in \~60 days prior to the Zenodo takedown.
* **License & content type:** **MIT**; files are **text/PDF**, no executables, no installers.
* **Reproducibility:** A/B/C evaluation protocol and prompts are public; users can reproduce deltas.

---

## 8) Risk assessment & next steps

* **If Zenodo returns:** It will be treated as a **mirror only** (for DOI/citation). GitHub remains the primary distribution.
* **If Zenodo does not return:**

  * We’ll publish DOIs via alternate scholarly channels when appropriate (e.g., arXiv overlays, institutional or HF datasets).
  * The repo will keep stable, versioned releases so downstream users have a reliable anchor.
* **Reddit:** If `u/wfgy_engine` is restored, I’ll continue participating under the same community-first rules (no cold promotion; respond only when asked). If not, communication will continue via GitHub Discussions and other forums.

---

## 9) What this means for the community

* **Nothing disappears.** Math and protocols remain open and forkable.
* **Reproducibility improves.** One repo = one source of truth.
* **Fewer dead links.** No external mirrors required for the basics.
* **Invite audits.** If you detect any issue with links or files, open an Issue or PR.

---

## 10) Contact

* **GitHub:** [https://github.com/onestardao/WFGY](https://github.com/onestardao/WFGY)
* **Email (appeals & support):** **[hello@onestardao.com](mailto:hello@onestardao.com)**
* **Reddit (under appeal):** `u/wfgy_engine`

> If you mirrored any of the old DOIs, please update to the GitHub paths above.
> Thank you for helping keep the knowledge accessible and verifiable.

---

**Postscript (ethos):**
This log is not an apology; it is a **transparent changelog of distribution**. Growth can trigger blunt automated defenses. I will keep shipping, documenting, and inviting verification. If a platform gate closes, we route around it—**the work continues.**
