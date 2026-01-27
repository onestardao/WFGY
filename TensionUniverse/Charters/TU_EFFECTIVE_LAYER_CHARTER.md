# Tension Universe Effective Layer Charter (TU-ELC v1.0)

**File**: `TU_EFFECTIVE_LAYER_CHARTER.md`  
**Scope**: All Tension Universe (TU) documents in this repository that describe "effective-layer" encodings, including the BlackHole S-problem collection `Q001–Q125`.  
**Status**: Working charter, version 1.0  

This charter defines what is meant by the **effective layer** in the Tension Universe program and what kinds of objects are allowed or forbidden at that layer.

---

## 1. Purpose and scope

1.1  
The effective layer is the level at which TU documents describe:

- abstract state spaces,
- observables and invariants,
- tension functionals,
- counterfactual worlds,
- experiment patterns and falsifiability conditions,

without exposing any deep TU generative rules, axiom systems, or constructive mappings from raw data to internal TU fields.

1.2  
This charter applies to:

- all `TensionUniverse/BlackHole/Qxxx_*.md` files,
- all future TU subprojects that explicitly declare themselves as effective-layer encodings and link to this charter.

1.3  
Whenever there is a conflict between this charter and a problem specific file, this charter takes precedence. The problem file must be revised or annotated accordingly.

---

## 2. Allowed objects at the effective layer

2.1  
Each effective-layer document may introduce:

- a **state space** `M` whose elements represent coarse grained configurations relevant to the problem,
- auxiliary parameter spaces (for example parameter sets for experiments, environments, or models),
- **observables** that map states in `M` to real valued or categorical quantities,
- **invariants** and **indices** built from observables,
- **tension functionals** that combine mismatch or cost terms into nonnegative scalars,
- **singular sets** and **regular domains** that delimit where observables are well defined,
- **counterfactual worlds** described as patterns or regimes of observables and tension,
- **experiment patterns** and **falsification criteria** phrased entirely in terms of observables and tension.

2.2  
Problem files may assume the existence of external procedures that:

- construct approximate states in `M` from data,
- estimate observables and invariants,

as long as these procedures are treated as black boxes at the effective layer and are not specified as TU generative rules.

2.3  
Effective-layer documents may refer to:

- existing theorems, models, or empirical regularities from the literature,
- known physical, mathematical, or computational constraints,

but they may not redefine or override them.

---

## 3. Forbidden content at the effective layer

3.1  
The following are not allowed in effective-layer documents:

- Full axiom systems for TU or any claimed "ultimate" theory.
- Constructive algorithms that map raw data or microscopic states directly into internal TU fields, including any fully specified pipeline from experimental data to TU internal representations.
- Hidden encodings of canonical answers in the definition of state spaces, observables, or tension functionals, such as fields that are defined as "1 if the hypothesis is true and 0 otherwise".
- Any direct claim that an open problem in mathematics, physics, or another domain has been solved at the level of full proof.

3.2  
Effective-layer documents must not:

- introduce new axioms for standard mathematical objects beyond what is accepted in mainstream practice,
- contradict known theorems or rigorous impossibility results,
- treat TU constructs as shortcuts to bypass established proof obligations.

3.3  
Whenever a description would require explicit TU generative rules or deep axiomatics, the effective-layer document must instead:

- refer to such rules abstractly (for example "there exists a family of mappings with properties A, B, C"),
- or declare the corresponding step as "out of scope for the effective layer".

---

## 4. World-representing states and counterfactual worlds

4.1  
A **world-representing state** at the effective layer is an element `m` in a defined state space `M` that is intended to summarize one coherent configuration of a system, experiment, or scenario, strictly in terms of observables and invariants.

4.2  
Effective-layer documents may define named sets such as:

- `World T` (for example "low tension regime consistent with a compact theory"),
- `World F` (for example "persistent high tension regime with no compact theory"),

under the following constraints:

- These worlds are defined only as patterns of observables and tension values over subsets of `M`.
- They do not assert which world the actual universe occupies.
- They do not encode the real truth value of any canonical statement.

4.3  
Statements of the form:

> "If the universe behaves like World T, then the following observable relationships must hold."

are allowed at the effective layer.  
Statements of the form:

> "The universe is in World T."

are not allowed as normative claims in effective-layer documents.

---

## 5. Singular sets and domain restrictions

5.1  
Each problem file must specify a **singular set** `S_sing` of states in `M` for which:

- some required observables are undefined,
- or numerical estimates are unstable,
- or the effective description fails in a way that cannot be repaired without leaving the effective layer.

5.2  
The **regular domain** `M_reg` is defined as:

```txt
M_reg = M \ S_sing
````

All tension functionals and invariants are required to be well defined and finite on `M_reg`.

5.3
Experiment patterns and falsification criteria must explicitly state that they operate only on states in `M_reg`.
When a procedure encounters `m` in `S_sing`, the outcome must be recorded as:

* "out of domain", or
* "inconclusive",

rather than as evidence for or against a hypothesis.

---

## 6. Experiments and falsifiability at the effective layer

6.1
Whenever an effective-layer document states that an experiment "falsifies" or "confirms" something, this must be understood as:

* falsifying or supporting a **TU encoding** or a choice of parameter class at the effective layer,
* not as proving or disproving the underlying canonical problem in the absolute sense.

6.2
Each experiment pattern must define:

* which observables and invariants are needed,
* what parameter choices or encoding classes are held fixed,
* what thresholds or tolerance bands are used,
* what outcomes count as falsification, support, or "inconclusive".

6.3
Experiment patterns may be instantiated in practice by:

* physical experiments,
* simulations,
* or AI model evaluations,

as long as the mapping from real procedures to effective-layer observables is clearly documented outside the TU core and treated as an implementation detail, not as part of the effective-layer definition.

---

## 7. Interaction with external theory and data

7.1
Effective-layer documents must respect:

* established mathematical theorems,
* standard physical laws at the relevant scales,
* basic constraints from information theory and computation.

7.2
If any effective-layer construction is later shown to conflict with established results, the proper response is:

* to revise or retire the construction under this charter,
* not to reinterpret external results in ad hoc ways.

7.3
All claims about "open problems", "difficulty", or "status" in problem files are descriptive, based on the scientific literature at the time of writing. They do not carry any authority beyond that.

---

## 8. Updates and versions

8.1
This charter is versioned. Each version must include:

* a version number,
* a date,
* a brief change log.

8.2
Problem files that rely on this charter may reference a specific version or a minimal required version.

8.3
When the charter is updated:

* problem files do not need to be rewritten immediately,
* but any explicit conflicts between a problem file and the new charter must be resolved in favor of the charter, either by editing the problem file or by marking the conflicting section as deprecated.

---

## 9. Program note

9.1
The Tension Universe program and the BlackHole S-problem collection are research artifacts.
This charter is an internal consistency and fairness specification, not a claim about the fundamental laws of nature.

9.2
Nothing in this charter should be interpreted as an argument that TU is uniquely correct or complete. The charter only constrains what TU effective-layer documents are allowed to say and how they must say it.
