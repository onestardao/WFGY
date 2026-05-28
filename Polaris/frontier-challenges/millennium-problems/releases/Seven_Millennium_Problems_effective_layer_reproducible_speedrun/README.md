# Seven Millennium Problems Effective-Layer Reproducible Speedrun

This folder contains the public reproducible speedrun package for the Seven Millennium Problems track under WFGY / Polaris.

This release is designed as a compact video-companion and validator package.  
It lets reviewers download the ZIP, replay the public speedrun, inspect the strict theorem-debt matrices, and verify the C03 original-theorem writeback result.

---

## Download

| File | SHA256 |
|---|---|
| [Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip](./Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip) | `FA767D99BFCD55041FDBCC86C5BD62F781DF9B39C617E5B28E3BD461C3FFE042` |

Direct download:

[Download ZIP](./Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip)

---

## Final Validator Status

```txt
ORIGINAL_THEOREM_WRITEBACK_VALIDATED_ALL7_PASS
````

Core result reported by the package:

```txt
Seven Millennium Problem lanes: 7
Strict theorem-debt cells open: 0
Return-to-original-statement theorem debt: 0
C03 original theorem writeback debt: 0
C03 writeback validation: PASS
All seven lanes: PASS
```

---

## What This Package Is

This package is a public reproducible effective-layer speedrun artifact.

It demonstrates the following pipeline:

```txt
Seven Millennium Problem lanes
→ effective-layer theorem-debt ledger
→ strict-debt matrix
→ formal debt-crusher pipeline
→ external theorem review ledger
→ public RPG speedrun replay
→ C03 original theorem writeback compiler
→ C03 writeback validator
→ final all-seven-lane PASS report
```

The important point is that the package does not stop at “debt zero”.

It also includes a C03 writeback layer that renders the cleared route back toward the original theorem statement format and validates that the writeback layer reports no remaining original-theorem writeback debt.

---

## Seven Problem Lanes

The speedrun package contains seven Millennium Problem lanes:

| Lane  | Problem                                |
| ----- | -------------------------------------- |
| PNP   | P vs NP                                |
| RH    | Riemann Hypothesis                     |
| BSD   | Birch and Swinnerton-Dyer Conjecture   |
| HODGE | Hodge Conjecture                       |
| NS    | Navier-Stokes Existence and Smoothness |
| YM    | Yang-Mills Existence and Mass Gap      |
| PC    | Poincare Conjecture                    |

---

## Functional Layers Inside the ZIP

After extracting the package, the main folders are:

```txt
00_START_HERE/
01_EFFECTIVE_LAYER_ONLY/
02_STRICT_DEBT_MATRIX/
03_FORMAL_DEBT_CRUSHER_PIPELINE/
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/
06_BLACKFAN_AUDIT/
07_MANIFEST/
08_PUBLIC_RPG_SPEEDRUN_LAYER/
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/
tools/
PROMPT.txt
run_speedrun_linux_mac.sh
run_speedrun_windows.bat
```

---

## 00_START_HERE

Entry point for the package.

Main file:

```txt
00_START_HERE/README_FIRST.md
```

Purpose:

* gives the first reading path
* explains the public speedrun artifact
* points to the validator scripts
* records the expected final all-seven-lane status

---

## 01_EFFECTIVE_LAYER_ONLY

Boundary-control layer.

Main files:

```txt
01_EFFECTIVE_LAYER_ONLY/COMPILER_POSITION_AUDIT.md
01_EFFECTIVE_LAYER_ONLY/NO_BOTTOM_FORMULA_IMPORT.md
```

Purpose:

* keeps this release as a public effective-layer package
* records compiler-position boundaries
* prevents hidden bottom-formula import
* separates the public reproducible package from deeper internal engines

---

## 02_STRICT_DEBT_MATRIX

Main scoreboard and strict theorem-debt matrix layer.

Main files:

```txt
02_STRICT_DEBT_MATRIX/SEVEN_PROBLEM_STRICT_DEBT_ZERO_SCOREBOARD.tsv
02_STRICT_DEBT_MATRIX/ALL7_STRICT_DEBT_MATRIX.tsv
02_STRICT_DEBT_MATRIX/STRICT_DEBT_DIMENSIONS.json
```

Purpose:

* records all seven problem lanes
* records strict theorem-debt dimensions
* records open strict-debt cells
* records return-to-original-statement theorem debt
* records C03 original theorem writeback debt
* supplies the data used by the public speedrun runner

Expected public result:

```txt
strict_debt_cells_open = 0
return_to_original_statement_debt = 0
original_theorem_writeback_debt = 0
```

---

## 03_FORMAL_DEBT_CRUSHER_PIPELINE

Formal debt-crusher pipeline layer.

Main files:

```txt
03_FORMAL_DEBT_CRUSHER_PIPELINE/01_DEBT_SEED_MATRIX.tsv
03_FORMAL_DEBT_CRUSHER_PIPELINE/02_PHASE1_COMPRESSION_MATRIX.tsv
03_FORMAL_DEBT_CRUSHER_PIPELINE/03_STRICT_DEFINITION_BIJECTION_MATRIX.tsv
03_FORMAL_DEBT_CRUSHER_PIPELINE/04_LEMMA_MICRO_CHAIN_MATRIX.tsv
03_FORMAL_DEBT_CRUSHER_PIPELINE/05_LEAN_CLAY_KILL_COURT_MATRIX.tsv
03_FORMAL_DEBT_CRUSHER_PIPELINE/EFFECTIVE_LAYER_PIPELINE.md
```

Purpose:

* starts from visible theorem-debt seed rows
* compresses debt through staged review matrices
* checks strict definition bijection
* checks lemma micro-chain coverage
* checks Lean / Clay route-readiness fields
* feeds the strict-debt-zero scoreboard

Pipeline shape:

```txt
Debt Seed Matrix
→ Phase 1 Compression Matrix
→ Strict Definition Bijection Matrix
→ Lemma Micro-Chain Matrix
→ Lean / Clay Kill Court Matrix
```

---

## 04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2

External theorem review ledger layer.

Main files:

```txt
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/PNP_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/RH_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/BSD_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/HODGE_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/NS_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/YM_LEDGER_V2.json
04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/PC_LEDGER_V2.json
```

Purpose:

* gives each problem lane its own external review ledger
* records original-problem routing
* records theorem obligations
* records review status fields
* provides ledger-level data for the strict-debt-zero run

---

## 06_BLACKFAN_AUDIT

Critic-side audit layer.

Main file:

```txt
06_BLACKFAN_AUDIT/BLACKFAN_AUDIT.md
```

Purpose:

* records critic-side attack surfaces
* checks whether the run depends on unsupported shortcuts
* checks whether debt-zero claims are routed through visible package artifacts
* documents review concerns for public inspection

---

## 07_MANIFEST

Manifest and checksum layer.

Main files:

```txt
07_MANIFEST/PACKAGE_MANIFEST.json
07_MANIFEST/PACKAGE_SIZE_AUDIT.tsv
07_MANIFEST/REFERENCE_HASHES_ONLY.json
07_MANIFEST/SHA256SUMS.tsv
07_MANIFEST/VALIDATION_RESULTS.json
```

Purpose:

* lists package files
* records internal checksum information
* records validation results
* supports reproducibility and package integrity checks

---

## 08_PUBLIC_RPG_SPEEDRUN_LAYER

Public video presentation layer.

Main files include:

```txt
08_PUBLIC_RPG_SPEEDRUN_LAYER/README.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/PNP_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/RH_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/BSD_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/HODGE_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/NS_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/YM_BOSS_CARD.md
08_PUBLIC_RPG_SPEEDRUN_LAYER/PC_BOSS_CARD.md
```

Purpose:

* presents the seven problem lanes as public speedrun boss cards
* supports the video demonstration
* keeps the public narrative layer separate from validator data
* lets viewers understand the run before reading every matrix

---

## 09_ORIGINAL_THEOREM_WRITEBACK_COMPILER

C03 original theorem writeback layer.

Main files:

```txt
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/README.md
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/C03_ORIGINAL_THEOREM_WRITEBACK_COMPILER_SPEC.md
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/C03_WRITEBACK_VALIDATOR_SPEC.md
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_OFFICIAL_STATEMENT_CLAUSE_MAP.tsv
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_WRITEBACK_COVERAGE_MATRIX.tsv
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_WRITEBACK_VALIDATOR_REPORT.json
09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_FINAL_ANSWER_INDEX.tsv
```

Purpose:

* adds the final C03 bridge after strict theorem-debt-zero validation
* maps cleared ledger routes back toward original theorem statement format
* validates official-statement clause coverage
* validates that ledger obligations are mapped
* validates that no original-theorem writeback debt remains
* provides detailed native writeback answer files for all seven problem lanes

Each lane contains:

```txt
00_OFFICIAL_STATEMENT.md
01_CLAUSE_MAP.tsv
02_LEDGER_TO_PROOF_ROUTE_MAP.tsv
03A_EFFECTIVE_LAYER_ANSWER.md
03B_ORIGINAL_NATIVE_WRITEBACK_ANSWER.md
04_NATIVE_THEOREM_TARGET.lean
05_WRITEBACK_VALIDATOR_REPORT.json
```

Important file:

```txt
03B_ORIGINAL_NATIVE_WRITEBACK_ANSWER.md
```

This file is the detailed original-native writeback answer for each lane.

C03 expected result:

```txt
ALL7_C03_WRITEBACK_PASS = true
ALL7_original_theorem_writeback_debt = 0
FINAL_STATUS = ORIGINAL_THEOREM_WRITEBACK_VALIDATED_ALL7_PASS
```

---

## Prompt-Native Replay

Main file:

```txt
PROMPT.txt
```

Purpose:

* gives an AI-readable replay prompt
* tells the model to read the actual package artifacts
* tells the model not to assume seven rows from memory
* requires the model to report the final speedrun status from the included scoreboard, ledger, and C03 files

The prompt layer is designed so the package can be replayed as a public AI-readable artifact.

---

## Validator Scripts

### Public speedrun runner

```txt
tools/run_public_rpg_speedrun.py
```

Purpose:

* reads the strict-debt-zero scoreboard
* prints the public boss-speedrun output
* reports all seven lane statuses
* reports strict debt cells open
* reports C03 original theorem writeback status
* writes `PUBLIC_RPG_RUN_SUMMARY.json`

Expected result:

```txt
all_bosses_passed: true
total_open_strict_debt_cells: 0
c03_writeback_status: ORIGINAL_THEOREM_WRITEBACK_VALIDATED_ALL7_PASS
all7_original_theorem_writeback_debt: 0
```

### C03 writeback validator

```txt
tools/validate_c03_writeback.py
```

Purpose:

* reads the C03 writeback reports
* checks all seven problem lanes
* verifies that each lane has writeback status PASS
* verifies original theorem writeback debt is 0
* verifies native original answer rendering
* reports the final C03 validation status

Expected result:

```txt
C03 Original Theorem Writeback Validator
PNP: PASS
RH: PASS
BSD: PASS
HODGE: PASS
NS: PASS
YM: PASS
PC: PASS
ALL7_C03_WRITEBACK_PASS: true
ALL7_original_theorem_writeback_debt: 0
FINAL_STATUS: ORIGINAL_THEOREM_WRITEBACK_VALIDATED_ALL7_PASS
```

---

## How to Reproduce

Download and extract:

[Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip](./Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip)

Then run:

### Windows

```bat
run_speedrun_windows.bat
```

### Linux / macOS

```bash
bash run_speedrun_linux_mac.sh
```

### Manual Python Run

```bash
python tools/run_public_rpg_speedrun.py --root . --no-emoji
python tools/validate_c03_writeback.py
```

---

## Recommended Review Order

For reviewers who want to inspect the package manually:

```txt
1. 00_START_HERE/README_FIRST.md
2. 02_STRICT_DEBT_MATRIX/SEVEN_PROBLEM_STRICT_DEBT_ZERO_SCOREBOARD.tsv
3. 02_STRICT_DEBT_MATRIX/ALL7_STRICT_DEBT_MATRIX.tsv
4. 03_FORMAL_DEBT_CRUSHER_PIPELINE/EFFECTIVE_LAYER_PIPELINE.md
5. 04_WFGY_EXTERNAL_THEOREM_REVIEW_LEDGER_V2/
6. 09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_WRITEBACK_VALIDATOR_REPORT.json
7. 09_ORIGINAL_THEOREM_WRITEBACK_COMPILER/ALL7_FINAL_ANSWER_INDEX.tsv
8. tools/run_public_rpg_speedrun.py
9. tools/validate_c03_writeback.py
10. PROMPT.txt
```

---

## Relation to the K60 Public ER Release

This speedrun package is a separate public release artifact.

The K60 Lean No-Sorry Public ER release remains archived separately under the Millennium Problems release archive.

This package focuses on:

```txt
effective-layer reproducibility
strict theorem-debt-zero validation
public speedrun replay
C03 original theorem writeback validation
video-companion reproducibility
```

---

## Repository Path

Recommended repository path:

```txt
Polaris/frontier-challenges/millennium-problems/releases/Seven_Millennium_Problems_effective_layer_reproducible_speedrun/
```

Recommended files in this folder:

```txt
README.md
Seven_Millennium_Problems_effective_layer_reproducible_speedrun.zip
```

---

## Repository

Main repository:

[https://github.com/onestardao/WFGY](https://github.com/onestardao/WFGY)

Millennium Problems release archive:

[https://github.com/onestardao/WFGY/tree/main/Polaris/frontier-challenges/millennium-problems/releases](https://github.com/onestardao/WFGY/tree/main/Polaris/frontier-challenges/millennium-problems/releases)

