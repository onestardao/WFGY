# TensionUniverse · Chronicles

This folder collects all long-form **story arcs** for the Tension Universe setting.  
Each arc is written as a small “chronicle” with three parallel views:

1. **Story** – narrative, written for non-technical readers  
2. **Science** – technical / MVP sketch behind the story  
3. **FAQ** – questions from readers and work-in-progress answers  

All files are plain text (`.md`), so they can be versioned, remixed, and quoted like any other part of WFGY.

---

## File naming rules

Each chronicle gets a short ID:

- Prefix: `TU-CH` = **Tension Universe – Chronicle**
- Index: `01`, `02`, `03`, … (two digits, zero-padded)
- Slug: a short English name for the main idea of that chronicle

File name pattern (all files live directly under `TensionUniverse/Chronicles` for now):

```text
TU-CHXX_<Slug>__story_en.md    # narrative version (English)
TU-CHXX_<Slug>__science_en.md  # technical / model notes (English)
TU-CHXX_<Slug>__faq_en.md      # collected questions and answers (English)

# optional, if we add other languages later:
TU-CHXX_<Slug>__story_zh.md
TU-CHXX_<Slug>__science_zh.md
TU-CHXX_<Slug>__faq_zh.md
````

This way:

* `TU-CHXX` lets you search all files for a given chronicle.
* The slug tells you what it is about.
* The suffix (`story / science / faq` + language code) tells you which view you are reading.

---

## Current chronicles

### TU-CH01 · Memo from a Tension Historian (year 2413)

* **Story (EN)** – [`TU-CH01_TensionHistorian__story_en.md`](./TU-CH01_TensionHistorian__story_en.md)
* **Story (ZH)** – [`TU-CH01_TensionHistorian__story_zh.md`](./TU-CH01_TensionHistorian__story_zh.md)
* **Science (EN)** – planned (`TU-CH01_TensionHistorian__science_en.md`)
* **FAQ (EN)** – planned (`TU-CH01_TensionHistorian__faq_en.md`)

---

### TU-CH02 · Human Tension (crushes, relationships, comparison)

* **Story (EN)** – [`TU-CH02_HumanTension__story_en.md`](./TU-CH02_HumanTension__story_en.md)
* **Science (EN)** – [`TU-CH02_HumanTension__science_en.md`](./TU-CH02_HumanTension__science_en.md)
* **FAQ (EN)** – [`CH02_HumanTension__faq_en.md`](./CH02_HumanTension__faq_en.md)

---

## License and remix policy

All narrative content in `TensionUniverse/Chronicles` is released under the same **MIT License** as the rest of WFGY. That means you are explicitly welcome to:

* fork, remix, and extend these stories;
* translate them into other languages;
* build new worlds, characters, and experiments on top of this setting,

as long as you keep the MIT attribution and license notice.

If you create derivative works, you are encouraged (but not required) to:

* reference the original chronicle ID (for example `TU-CH01`);
* link back to this repository so others can trace the source.

---

## Scientific disclaimer

These chronicles are **science fiction** and **speculative worldbuilding**. They are written to make abstract ideas about “tension”, alignment, and complex systems easier to think about, and to provide narrative test cases for WFGY-style tools.

They are **not**:

* experimental proof that the “Tension Universe” model is physically correct;
* a claim that any specific cosmology, physics, or AI alignment scheme has been validated;
* official consensus views of any institution, journal, or research community.

Equations, concepts, and terminology that appear in these stories may be inspired by real physics, mathematics, or computer science, but here they are used in a **fictional** setting. Any resemblance between events in these chronicles and real-world predictions, policies, markets, or individuals is coincidental or metaphorical and should not be treated as scientific evidence or advice.

Use these texts as prompts, thought experiments, and creative seeds. If you want to test or challenge the underlying ideas in a rigorous way, please go back to the technical parts of the repository (WFGY 3.0 demo, ProblemMap, and related MVPs) and design proper experiments or mathematical arguments there.

---

## Navigation

| Section                                                                                              | Description                                                          |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [Event Horizon](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md) | Official entry point of Tension Universe (WFGY 3.0)                  |
| [BlackHole Archive](https://github.com/onestardao/WFGY/tree/main/TensionUniverse/BlackHole)          | 131 S-class problems (Q001–Q131) encoded in Effective Layer language |
| [Experiments](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/Experiments/README.md)    | Reproducible MVP runs and observable tension patterns                |
| [Charters](https://github.com/onestardao/WFGY/tree/main/TensionUniverse/Charters)                    | Scope, guardrails, encoding limits and constraints                   |
| [r/TensionUniverse](https://www.reddit.com/r/TensionUniverse/)                                       | Community discussion and ongoing story threads                       |

```
```
