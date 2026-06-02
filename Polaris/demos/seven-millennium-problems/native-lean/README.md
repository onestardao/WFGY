# Native Lean no-sorry Materials

This page collects the Native Lean no-sorry materials for the Seven Millennium Problems package.

The standard is simple:

**No sorry.**  
**No admit.**  
**No fake proof stubs.**  
**No status label pretending to be proof.**

[Back to Seven Millennium Problems](../README.md)  
[Verification and Review](../verification/)  
[Packages](../packages/)

---

## What To Inspect

| Item | Purpose |
|---|---|
| Lean source files | Inspect theorem statements and proof terms. |
| Build notes | Check whether the files build under the expected environment. |
| no-sorry status | Confirm no `sorry` / `admit` placeholders. |
| Theorem linkage | Check that formal files connect back to the Seven Millennium Problems route. |
| Review notes | Track objections, weak spots, and repair history. |

---

## File Index

| Material | Link |
|---|---|
| Lean source tree | [Open Lean files](./files/) |
| Build log | [Open build log](./build-log/) |
| no-sorry report | [Open no-sorry report](./no-sorry-report/) |
| Formal review notes | [Open formal review](./formal-review/) |

---

## AI Inspection Command

Copy this into AI:

```text
inspect Native Lean no-sorry materials
```

For the flagship package:

```text
inspect Native Lean no-sorry materials for Seven Millennium Problems
```

---

## Reviewer Checklist

| Check | Question |
|---|---|
| no-sorry | Are there any `sorry`, `admit`, or placeholder proof terms? |
| theorem target | Are theorem statements meaningful and connected to the target? |
| proof terms | Are final claims supported by actual proof terms? |
| hidden shortcuts | Are definitions or metadata doing hidden proof work? |
| route connection | Do Lean files connect back to the Seven Millennium Problems route? |

---

## Final Line

Native Lean no-sorry is not decoration.

It is the formal edge of the flagship claim.
