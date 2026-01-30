<!-- QUESTION_ID: TU-Q072 -->
# Q072 · Origin of the genetic code

## 0. Header metadata

```txt
ID: Q072
Code: BH_BIO_GENETIC_CODE_L3_072
Domain: Biology
Family: Molecular evolution (origin-of-life, molecular coding)
Rank: S
Projection_dominance: M
Field_type: combinatorial_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N1
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework:

* We only describe state spaces, observables, mismatch functionals, tension scores, singular sets, and experiment patterns at a coarse, effective level.
* We do not specify any underlying TU axiom system, deep generative rule, or constructive derivation of TU itself.
* We do not provide any explicit mapping from raw biochemical or evolutionary data to internal TU fields. We only assume that such mappings exist inside an admissible encoding class, as defined in Section 3.7.
* We do not claim to prove or disprove the canonical origin-of-code statements from molecular evolution or origin-of-life research.
* We do not introduce any new theorem about the genetic code, its optimality, or its historical origin. All claims are about effective-layer encodings and their behavior.

The objects defined in this entry, including:

* the state space `M_code`,
* observables such as `Error_impact(m)`, `Cost_profile(m)`, `Access_profile(m)`,
* mismatch functionals such as `DeltaS_error(m)`, `DeltaS_cost(m)`, `DeltaS_access(m)`,
* the combined consistency tension `Tension_Code(m)`,
* and the tensor-like quantity `T_ij(m)`,

are all effective-layer quantities. They can be instantiated inside tools and models without exposing any deeper TU rules or claiming any solution of the open biological problem.

This page follows the constraints of the TU Effective Layer Charter and the TU Encoding and Fairness Charter. See the footer for links to the relevant charters.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical question behind Q072 is:

> How did the mapping between nucleotide triplets (codons) and amino acids in the standard genetic code arise and become fixed, given the enormous space of possible codes and the physical, chemical, and evolutionary constraints acting on early life?

More concretely, the problem asks for:

1. A coherent explanation of why the standard genetic code has:

   * its particular pattern of redundancy and degeneracy,
   * its specific grouping of similar amino acids in codon space,
   * its robustness to common classes of point mutations and translation errors.

2. A mechanistic class (or classes) of origin scenarios that can:

   * generate codes with properties close to the standard code,
   * do so without extreme fine tuning of parameters,
   * and explain why alternative codes with apparently better properties are not observed.

Traditional explanatory classes include:

* Stereochemical hypotheses:

  * Direct chemical affinities between codons (or anticodons) and amino acids guided the mapping.

* Frozen accident hypotheses:

  * The code was historically contingent and became locked in after an early choice.

* Coevolutionary and adaptive hypotheses:

  * The code coevolved with amino acid biosynthesis pathways and was shaped by selection for error minimization and robustness.

No consensus exists on a single, fully quantitative explanation.

### 1.2 Status and difficulty

The origin of the genetic code is widely recognized as a central open problem in origin-of-life research and molecular evolution. Key aspects of its status include:

* There is strong evidence that:

  * The standard code is highly nonrandom in its error-tolerance properties.
  * It often appears near the top of performance rankings when compared with large ensembles of alternative codes.

* There is no agreement on:

  * Which mechanistic class or combination of classes best explains these properties.
  * How to reconcile chemical constraints, historical contingency, and adaptive selection within a single framework.

* Most existing models exhibit one or more of the following issues:

  * Heavy dependence on a specific set of parameters or initial conditions.
  * Limited ability to generate codes with properties as good as or better than the standard code.
  * Difficulty in capturing evolutionary accessibility and path dependence in code space.

The problem remains open because it requires unifying:

* combinatorial structure in codon space,
* chemical and energetic constraints,
* population and evolutionary dynamics,
* and historical contingencies,

inside a single, testable framework.

### 1.3 Role in the BlackHole project

Within the BlackHole S-problem collection, Q072 plays the following roles:

1. It is the flagship example of a biological coding origin problem, where:

   * discrete symbol mappings must align with physical and evolutionary constraints,
   * and apparent optimality must be balanced against historical path dependence.

2. It provides a template for:

   * other biological code problems (immune repertoires, signaling codes),
   * and socio-technical code problems (language, communication protocols).

3. It is the main node where TU-style consistency tension between:

   * code structure,
   * error and cost profiles,
   * and evolutionary accessibility,

   is defined and tested at the effective layer.

### References

1. F. H. C. Crick, "The origin of the genetic code", Journal of Molecular Biology, 38(3):367-379, 1968.
2. R. F. Freeland and L. D. Hurst, "The genetic code is one in a million", Journal of Molecular Evolution, 47(3):238-248, 1998.
3. E. V. Koonin and A. S. Novozhilov, "Origin and evolution of the genetic code: the universal enigma", IUBMB Life, 61(2):99-111, 2009, doi:10.1002/iub.146.
4. J. Knight, S. J. Freeland, and L. F. Landweber, "Selection, history and chemistry: the three faces of the genetic code", Trends in Biochemical Sciences, 24(6):241-247, 1999.

---

## 2. Position in the BlackHole graph

This block records how Q072 sits inside the BlackHole graph as nodes and edges among Q001–Q125. Each edge includes a one-line reason that points to a concrete component or tension structure.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q072 relies on at the effective layer.

* Q069 (BH_CHEM_SELECTIVITY_RULES_L3_069)
  Reason: Provides general principles for chemical selectivity and reaction networks that constrain prebiotic chemistry relevant to genetic coding mechanisms.

* Q070 (BH_CHEM_SOFTMATTER_L3_070)
  Reason: Supplies self-assembly and soft-matter phase behavior needed to model compartments and proto-translation machinery in which codes can emerge.

* Q071 (BH_BIO_ORIGIN_LIFE_L3_071)
  Reason: Provides the broader origin-of-life context, including the transition from noncoded replication to coded translation where genetic codes become relevant.

### 2.2 Downstream problems

These problems are direct reuse targets of Q072 components or depend on Q072 tension structures.

* Q073 (BH_BIO_EVO_COMPLEXITY_L3_073)
  Reason: Reuses `CodeOrigin_TensionFunctional` and `CodeSpace_MoveRules_Template` to analyze how a fixed genetic code shapes major evolutionary transitions.

* Q074 (BH_BIO_CELL_DIFFERENTIATION_L3_074)
  Reason: Depends on a stable genetic code as the base layer for cell-type and tissue differentiation programs modeled as higher-level coding systems.

* Q076 (BH_BIO_IMMUNE_CODE_L3_076)
  Reason: Compares genetic-code origin constraints with immune coding schemes, reusing fair code-ensemble descriptors to study robustness and diversity.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q076 (BH_BIO_IMMUNE_CODE_L3_076)
  Reason: Both treat many-to-many biological coding systems under robustness and constraint, but immune codes are derived and do not depend directly on genetic code origin.

* Q078 (BH_BIO_DEVELOPMENTAL_L3_078)
  Reason: Both address mapping rules from discrete genetic information to structure, yet developmental codes operate on top of an already fixed genetic code.

* Q063 (BH_BIO_PROTEIN_FOLDING_L3_063)
  Reason: Both involve mapping from sequence space to functionally relevant states, but protein folding does not depend on how the genetic code originally formed.

### 2.4 Cross-domain edges

Cross-domain edges connect Q072 to problems in other domains that can reuse its components.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Reuses `CodeOrigin_TensionFunctional` as a biological case study of information encoding tradeoffs between robustness and energetic cost.

* Q032 (BH_PHYS_QTHERMO_L3_032)
  Reason: Uses genetic-code origin as a concrete example where thermodynamic constraints shape which codes are reachable and stable.

* Q090 (BH_SOC_LANGUAGE_EMERGENCE_L3_090)
  Reason: Transfers the "evolving code under constraint" pattern to models of language and symbol systems in social groups, using code-space move rules as a template.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe:

* state spaces,
* observables and fields,
* invariants and tension scores,
* singular sets and domain restrictions.

We do not describe any hidden TU generative rules or construction of internal TU fields from raw biochemical data.

### 3.1 State space

We introduce an effective state space:

```txt
M_code
```

with the following interpretation:

* Each element `m` in `M_code` is a "code origin configuration" that summarizes:

  * a complete genetic code mapping from codons to amino acids and stop signals,
  * an effective description of the biochemical and energetic context,
  * an effective description of the error and mutation environment,
  * an effective description of evolutionary accessibility relationships in code space.

More concretely, each `m` encodes:

* `Code_map(m)`
  A mapping from 64 codons to 20 amino acids plus at least one stop symbol, including degeneracy structure.

* `Env_context(m)`
  Coarse summaries of:

  * amino acid biosynthesis difficulty classes,
  * prebiotic availability groups,
  * approximate energetic costs.

* `Error_env(m)`
  A compact representation of:

  * typical point mutation spectra,
  * translation misreading patterns,
  * relative frequencies of different error types.

* `Access_graph(m)`
  A coarse graph-like description of code space accessibility under allowed local moves (for example single reassignment steps that preserve viability).

We do not specify how any of these summaries are computed from detailed models or data. We only assume that for each scenario of interest there exist states `m` in `M_code` that encode them in a well-defined way within an admissible encoding.

### 3.2 Reference libraries and fairness constraints

To prevent trivial tuning, we fix finite reference libraries and fairness conditions at the effective layer.

We define:

* `Library_random`
  A finite ensemble of genetic codes where:

  * the number of codons, amino acids, and stop signals matches the standard code,
  * codons are assigned to amino acids and stops under simple structural constraints,
  * the generation procedure uses no information about performance of the standard code under the metrics we will later evaluate.

* `Library_chem_constrained`
  A finite ensemble of "chemistry-respecting" codes where:

  * codons are grouped or biased according to simple stereochemical or biosynthetic classes,
  * assignments respect these groupings but remain otherwise unconstrained,
  * the generation procedure is defined independently of the performance of the standard code.

Fairness constraints:

1. Both libraries are defined once, before any tension evaluation on the standard code or on specific evolutionary models.
2. No code in a reference library is selected or reweighted based on how similar it is to the standard code in performance metrics.
3. When we speak of "better" or "worse" codes, this is always measured relative to distributions over these fixed libraries, not relative to ad hoc tuned subsets.

### 3.3 Observables and mismatch functionals

We introduce effective observables on `M_code`.

1. Error impact observable

```txt
Error_impact(m) >= 0
```

* Input: a state `m` and a fixed error model derived from `Error_env(m)`.
* Output: a scalar error cost that aggregates how often single-base changes or translation misreads lead to amino acid changes with large physicochemical differences.
* Interpretation: lower values correspond to more error-robust codes under the chosen environment.

2. Cost profile observable

```txt
Cost_profile(m)
```

* Input: a state `m`.
* Output: a vector or low-dimensional summary describing:

  * the average energetic or resource cost of amino acids weighted by codon usage,
  * a small set of aggregate statistics summarizing this distribution.

We only require that these summaries are finite and well defined for `m`.

3. Accessibility profile observable

```txt
Access_profile(m)
```

* Input: a state `m`.
* Output: a summary of:

  * how many low-cost local moves from `Code_map(m)` remain viable,
  * how often local moves lead to major increases or decreases in error and cost metrics.

Based on these observables we define mismatch functionals.

4. Error robustness mismatch

```txt
DeltaS_error(m) >= 0
```

* Measures how far `Error_impact(m)` is from the distribution of error impacts across codes in `Library_random` or `Library_chem_constrained`.
* One possible implementation at the effective layer:

```txt
DeltaS_error(m) = max(0, rank_error(m) - tau_error)
```

where:

* `rank_error(m)` is the percentile rank of `Error_impact(m)` among codes in the chosen library (lower percentile is better),
* `tau_error` is a library dependent threshold defining the top performance band.

5. Cost feasibility mismatch

```txt
DeltaS_cost(m) >= 0
```

* Measures how far `Cost_profile(m)` is from a band of profiles considered feasible for early metabolism.
* One possible implementation:

```txt
DeltaS_cost(m) = max(0, dist_cost(m) - tau_cost)
```

where:

* `dist_cost(m)` is a scalar measuring distance from a feasible cost band,
* `tau_cost` is a threshold chosen from geochemically plausible constraints.

6. Accessibility mismatch

```txt
DeltaS_access(m) >= 0
```

* Measures how atypical `Access_profile(m)` is relative to an ensemble of codes reachable under simple local move rules.
* For example:

```txt
DeltaS_access(m) = max(0, dist_access(m) - tau_access)
```

where:

* `dist_access(m)` compares `Access_profile(m)` to an ensemble of codes visited by random walks starting from simple codes,
* `tau_access` is a threshold defining a typical accessibility band.

The exact definitions of `rank_error`, `dist_cost`, `dist_access`, and thresholds `tau_error`, `tau_cost`, `tau_access` are encoding choices, but they:

* must be defined in terms of the fixed reference libraries and move ensembles,
* must not be re-tuned after observing where the standard code lies.

### 3.4 Combined consistency tension

We define the main consistency tension functional for Q072:

```txt
Tension_Code(m) =
    w_error  * DeltaS_error(m)  +
    w_cost   * DeltaS_cost(m)   +
    w_access * DeltaS_access(m)
```

with weights:

```txt
w_error  >= 0
w_cost   >= 0
w_access >= 0
w_error + w_cost + w_access = 1
```

Weight rules:

* We fix `w_error`, `w_cost`, and `w_access` once, based on broad domain judgment, for example:

  * error robustness and cost feasibility receive comparable weight,
  * accessibility receives a nonzero but not dominant weight.

* We do not change these weights after computing `Tension_Code` for the standard code or for any particular model.

* If later analysis suggests different weights, that constitutes a new encoding, which must be evaluated as a separate TU instance.

### 3.5 Singular set and domain restriction

Some states in `M_code` may fail to yield well defined mismatch values, for example because:

* their observables are incomplete,
* their reference comparisons diverge,
* or their summaries violate basic structural constraints.

We define the singular set:

```txt
S_sing = {
  m in M_code :
  DeltaS_error(m), DeltaS_cost(m), or DeltaS_access(m)
  is undefined or not finite
}
```

Domain restriction:

* All analysis of Q072 tension is restricted to:

```txt
M_reg = M_code \ S_sing
```

* States in `S_sing` represent invalid or incomplete encodings at this effective layer, not evidence for or against any specific origin mechanism.
* When an experiment encounters a state in `S_sing`, the result is reported as "out of domain" and excluded from tension statistics.

### 3.6 Effective tension tensor

We align with the TU core tension tensor structure by defining, for each `m` in `M_reg`:

```txt
T_ij(m) = S_i(m) * C_j(m) * Tension_Code(m) * lambda(m) * kappa
```

where:

* `S_i(m)` are source-like factors representing the strength of different origin-mechanism components present in configuration `m`
  (for example emphasis on stereochemical constraints, historical contingency, or adaptive selection).

* `C_j(m)` are receptivity-like factors representing how sensitive different downstream systems are to changes in code properties
  (for example robustness of cell lineages, evolvability of regulatory networks).

* `Tension_Code(m)` is the nonnegative scalar consistency tension defined in Section 3.4.

* `lambda(m)` is a convergence-state factor encoding whether local reasoning about code origin is convergent, recursive, divergent, or chaotic.

* `kappa` is a global coupling constant that sets the overall scale at which genetic-code origin tension contributes to larger TU structures.

This `T_ij(m)` is an effective bookkeeping device. It repackages the scalar `Tension_Code(m)` and simple multiplicative factors into a tensor-like form so that genetic-code origin tension can be combined with other TU components. It does not introduce any new equations of motion, any deep TU generative rules, or any explicit dynamics beyond what is already encoded in the effective-layer quantities defined above.

We do not need explicit index sets for `i` and `j` at the effective layer; it suffices that `T_ij(m)` is finite and well defined for the configurations considered.

### 3.7 Encoding class and fairness constraints

We now collect the ingredients above into an explicit encoding class, in line with the TU Encoding and Fairness Charter.

An admissible Q072 encoding at the effective layer is specified by a tuple:

```txt
E = (D, F, W, L)
```

where:

* `D` is a data-to-state mapping family:

  * It specifies how raw or simulated information about codes, environments, and dynamics is mapped into states in `M_code`.
  * Members of `D` must obey the same structural constraints on `Code_map(m)`, `Env_context(m)`, `Error_env(m)`, and `Access_graph(m)`.

* `F` is a mismatch-functional family:

  * It specifies concrete formulas and numerical procedures that instantiate `Error_impact(m)`, `Cost_profile(m)`, `Access_profile(m)`, and the derived quantities `DeltaS_error(m)`, `DeltaS_cost(m)`, `DeltaS_access(m)`.
  * Each member of `F` must define these functionals in terms of the fixed reference libraries and move ensembles, without any dependence on the performance of the observed genetic code.

* `W` is a finite set of admissible weight triples and threshold sets:

  * Each element of `W` provides a choice of `(w_error, w_cost, w_access)` and thresholds `(tau_error, tau_cost, tau_access)` that:

    * satisfy the constraints in Sections 3.3 and 3.4,
    * and are selected based on general domain considerations, not on the measured `Tension_Code(m_obs)` of the observed code.

* `L` is a specification of reference libraries and move ensembles:

  * It fixes `Library_random`, `Library_chem_constrained`, and any additional fair code ensembles used in F and in the experiments of Section 6.
  * `L` also fixes the code-space move ensembles used to define `dist_access(m)` and related quantities.

Fairness and auditability:

* For any concrete study, one must choose a single tuple `E = (D, F, W, L)` from this encoding class before computing any tension values for the observed genetic code or for specific historical scenarios.
* All components of `E` must be recorded in an auditable way, for example as configuration files or protocol descriptions.
* Once `E` is fixed, no part of `D`, `F`, `W`, or `L` may be modified in response to the observed position of the standard code in the resulting tension distributions. Any such modification defines a new encoding `E'` that must be evaluated as a separate instance.

Refinement sequence:

* In Section 4.4 we refer to a sequence of encodings:

  ```txt
  Encode(k),  k = 1, 2, 3, ...
  ```

* Each `Encode(k)` is understood as a refinement of a single base encoding `E` from this encoding class, for example by:

  * increasing the size of reference libraries,
  * using more detailed error models,
  * or refining accessibility descriptions,

  while keeping the admissible choices of `D`, `F`, `W`, and `L` inside the same encoding class.

* Refinement may increase resolution or statistical power but may not change the basic rules of the encoding family to force a desired outcome for `Tension_Code(m_obs)`.

This explicit encoding class ensures that claims about low-tension or high-tension origin of the genetic code are traceable to auditable choices, and that tuning away inconvenient tension patterns is disallowed by construction.

---

## 4. Tension principle for this problem

This block states how Q072 is characterized as a tension problem in TU.

### 4.1 Informal description

In TU terms, Q072 asks whether the observed genetic code can be understood as:

* a low-tension configuration in code space,

  * naturally favored by broad classes of chemical and evolutionary processes,
  * and reachable by many trajectories,

or instead as:

* a high-tension configuration,

  * requiring narrow, finely tuned processes,
  * or improbable trajectories,
  * with many unrealized alternatives that would have provided better error and cost properties.

### 4.2 Low-tension code origin

We define a low-tension regime as follows.

There exist world-representing states `m_star` in `M_reg` such that:

```txt
Tension_Code(m_star) <= epsilon_code
```

for a small threshold `epsilon_code` that is:

* determined by the reference libraries and encoding resolutions,
* and stable under reasonable refinements of the encoding.

Qualitatively, in a low-tension regime:

1. The standard code lies in a favorable band of the joint distribution of error robustness and cost feasibility across the reference libraries.

2. Codes with similar or slightly lower tension are not extremely rare, and simple evolutionary dynamics in code space can reach codes in this band with non-negligible probability.

3. Many distinct process models, when coarse-grained inside the same encoding class, predict similar low-tension regions in code space.

### 4.3 High-tension code origin

We define a high-tension regime as follows.

For world-representing states `m_obs` reflecting the actual standard code and environment, tension satisfies:

```txt
Tension_Code(m_obs) >= delta_code
```

for some strictly positive `delta_code` that:

* remains bounded away from zero as we refine encoding resolution and library sizes,
* and cannot be removed without violating fairness constraints or structural assumptions of the encoding class.

Qualitatively, in a high-tension regime:

1. The standard code is a strong outlier in reference libraries, far beyond what is expected under simple process models.

2. Most plausible local-move dynamics avoid codes as good as or better than the standard code, unless parameters are tuned to a narrow range.

3. Different process models disagree on which codes should be favored, so the observed code does not sit at a robust intersection of mechanisms.

### 4.4 Refinement and stability

To prevent hidden tuning through resolution changes, we consider a sequence of encodings:

```txt
Encode(k),  k = 1, 2, 3, ...
```

where increasing `k` represents:

* larger or more refined reference libraries,
* more detailed error models,
* and more detailed accessibility descriptions,

all within the same admissible encoding class `E`.

For each `k`, we obtain:

* `Tension_Code_k(m_obs)` for the observed code.

The tension principle requires that:

* In a low-tension narrative, there exists a band `[0, epsilon_code]` such that for all sufficiently large `k`,
  `Tension_Code_k(m_obs)` remains inside this band.

* In a high-tension narrative, there exists `delta_code > 0` such that for all sufficiently large `k`,
  `Tension_Code_k(m_obs) >= delta_code`.

This prevents us from hiding tension behavior inside the choice of resolution or library size.

---

## 5. Counterfactual tension worlds

We outline two counterfactual worlds, described strictly via observables and tension patterns.

* World T: low-tension origin of the genetic code.
* World F: high-tension origin of the genetic code.

### 5.1 World T (low-tension code origin)

In World T:

1. Reference library positioning

   * When we compute `Tension_Code(m_obs)` for the observed code, it lies in a high-performing but not astronomically rare band of the distributions induced by `Library_random` and `Library_chem_constrained`.
   * The standard code is near the top, but it does not require special selection of the library or thresholds to appear exceptional.

2. Error and cost structure

   * `DeltaS_error(m_obs)` is small, reflecting strong error robustness relative to typical codes.
   * `DeltaS_cost(m_obs)` is small, reflecting compatibility with plausible metabolic constraints.

3. Accessibility structure

   * Under simple local move rules, random or mildly biased walks in code space frequently visit codes with tension comparable to or lower than the standard code.
   * The region of code space containing such codes is connected and has non-negligible measure under processes consistent with origin-of-life scenarios.

4. Process robustness

   * Different coarse-grained process models, when instantiated inside the same encoding class, still identify similar low-tension regions.
   * The code origin narrative is robust to moderate changes in assumptions and parameter choices.

### 5.2 World F (high-tension code origin)

In World F:

1. Reference library positioning

   * `Tension_Code(m_obs)` for the observed code lies in an extremely rare tail of the distributions over the reference libraries.
   * Many codes with strictly lower tension are common and easily constructed within the same structural and chemical constraints.

2. Error and cost structure

   * Either `DeltaS_error(m_obs)` or `DeltaS_cost(m_obs)` (or both) are large compared to feasible alternatives, yet those alternatives are not realized.
   * The standard code looks atypical in ways not easily explained by known constraints.

3. Accessibility structure

   * Under reasonable local move rules and starting points, almost no trajectories visit codes with tension as low as or lower than the standard code.
   * Paths that reach such regions require extreme fine tuning of process parameters or very special initial conditions.

4. Process fragility

   * Small changes in model assumptions, such as slightly different cost estimates or error patterns, dramatically alter which codes are favored.
   * There is no stable intersection of chemistry, history, and selection that naturally singles out the observed code.

### 5.3 Interpretive note

These counterfactual worlds do not attempt to construct explicit histories of the code. They differ only in:

* where the observed code sits in tension distributions,
* how accessible low-tension regions are under simple dynamics,
* and how robust these conclusions are to model variation inside a fixed encoding class.

They do not assert any deep TU generative rule or hidden origin story beyond the effective-layer observables and tension functionals defined in Section 3.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols that can:

* test the coherence of the Q072 encoding,
* distinguish between different code-origin tension models,
* and provide evidence for or against particular parameter and library choices.

These experiments do not prove or disprove any specific biological mechanism. They can falsify or refine TU encodings of Q072 inside the encoding class defined in Section 3.7.

### Experiment 1: Code ranking in fair libraries

Goal:

* Evaluate where the standard genetic code sits in the joint distribution of error robustness and cost feasibility across fair reference libraries, and test whether the `Tension_Code` encoding is stable and discriminative.

Setup:

* Input:

  * A precisely defined `Library_random` and `Library_chem_constrained`, as in Section 3.2.
  * Implementations of `Error_impact(m)`, `Cost_profile(m)`, and `Access_profile(m)` that are consistent across all codes in the libraries.

* Choose fixed weights `w_error`, `w_cost`, `w_access` and thresholds `tau_error`, `tau_cost`, `tau_access` before any evaluation, in line with an admissible element of `W` in Section 3.7.

Protocol:

1. For each code `m` in each library:

   * Compute `DeltaS_error(m)`, `DeltaS_cost(m)`, and `DeltaS_access(m)` according to Section 3.3.
   * Compute `Tension_Code(m)` using Section 3.4.

2. Compute:

   * the empirical distribution of `Tension_Code(m)` over the combined libraries,
   * the percentile rank of `Tension_Code(m_obs)` for the observed standard code,
   * the gap between `Tension_Code(m_obs)` and the minimum tension observed in the libraries.

3. Repeat computations across increasing library sizes or more refined generating procedures, forming a sequence of refinements `Encode(k)` consistent with the same encoding class.

Metrics:

* `rank_code`: percentile rank of `Tension_Code(m_obs)` in each `Encode(k)`.
* `gap_best`: difference between `Tension_Code(m_obs)` and the lowest observed tension at each `k`.
* `stability_index`: variation in `rank_code` and `gap_best` as `k` increases.

Falsification conditions:

* If for all reasonable encodings `Encode(k)` that respect the fairness constraints and belong to the same encoding class:

  * `rank_code` never departs significantly from the middle of the distribution,
  * and `gap_best` remains small,

  then the current definition of `Tension_Code` is judged non-discriminative for Q072 and considered falsified as a useful TU encoding at this level.

* If small, unmotivated changes in thresholds or weights within one element of `W` cause `rank_code` to move from typical to highly exceptional regimes, the encoding is considered unstable and rejected at this level of analysis.

Semantics implementation note:

* All observables and tension scores are computed using the same hybrid treatment of discrete code structure and continuous cost and error parameters implied by Section 0 and recorded in `Semantics: hybrid` in the header.
* No alternative semantics category is introduced here.

Boundary note:

* Falsifying a particular TU encoding for Q072 in this experiment does not solve the canonical origin-of-code problem.
* Results of this experiment only support or rule out specific encodings inside the Q072 encoding class. They do not by themselves provide a biological mechanism, and they do not constrain other TU problems.

---

### Experiment 2: Evolutionary accessibility under local moves

Goal:

* Test whether simple local move dynamics in code space naturally lead to codes with low consistency tension, and whether the standard code lies in an accessible low-tension region.

Setup:

* Define a class of local move rules:

  * for example, single reassignment of a codon from one amino acid to another, subject to viability constraints such as preserving essential codons and avoiding catastrophic error patterns.

* Choose:

  * one or more initial code ensembles, for example simple, chemically biased starting codes,
  * a fixed error and cost environment consistent with origin-of-life scenarios.

* Use the same `Library_chem_constrained` as a background ensemble for comparison, as specified in `L` for the encoding.

Protocol:

1. Generate many trajectories in code space:

   * For each trajectory:

     * start from an initial code sampled from a specified ensemble,
     * iteratively apply local moves chosen by a simple rule, such as random moves filtered by viability constraints.

2. For each visited code along each trajectory, compute:

   * `DeltaS_error(m)`, `DeltaS_cost(m)`, `DeltaS_access(m)`,
   * `Tension_Code(m)`.

3. Record:

   * the distribution of `Tension_Code` values along trajectories,
   * the distribution of final or absorbing states,
   * whether and how often codes with tension equal to or lower than `Tension_Code(m_obs)` are reached.

Metrics:

* `reach_rate`: fraction of trajectories that reach a code `m` with `Tension_Code(m) <= Tension_Code(m_obs)`.
* `path_length`: typical number of moves required to reach such codes when they are reached.
* `sensitivity_index`: how much `reach_rate` and `path_length` change when local move rules or initial ensembles are moderately varied within the encoding class.

Falsification conditions:

* If, across a broad range of reasonable local move rules and initial ensembles that respect viability and basic chemistry:

  * `reach_rate` remains near zero,
  * or can only be made large by highly tuned or biologically implausible parameters,

  then the current accessibility component `DeltaS_access` and associated move rules are judged misaligned with the origin-of-life context and rejected at this level.

* If small, arbitrary changes in local move rules produce wild swings in `reach_rate` and `path_length` without clear mechanistic interpretation, the current encoding is considered unstable and inadequate for Q072 at this level.

Semantics implementation note:

* Discrete code changes and continuous error or cost parameters are treated consistently with the hybrid `Field_type: combinatorial_field` and `Semantics: hybrid` declared in the header and clarified in Section 0.
* No additional semantics category is introduced.

Boundary note:

* Falsifying a particular choice of accessibility tension and local move rules in this experiment does not settle the real history of the genetic code.
* It only shows that a specific encoding inside the Q072 encoding class is not adequate. Other encodings may still be viable, and the canonical biological problem remains open.

---

## 7. AI and WFGY engineering spec

This block describes how Q072 can be used as an engineering module for AI systems within WFGY, at the effective layer.

### 7.1 Training signals

We define several training signals that an AI system can use to handle genetic-code origin reasoning in a tension-aware way.

1. `signal_code_error_robustness`

   * Definition: a nonnegative signal derived from `DeltaS_error(m)` when the model represents a specific code or code-origin scenario.
   * Intended effect: penalize internal states that imply fragile coding schemes when the context explicitly assumes robust error handling.

2. `signal_code_cost_feasibility`

   * Definition: a signal derived from `DeltaS_cost(m)` in contexts where prebiotic or early-biosphere energetic constraints are relevant.
   * Intended effect: push the model to keep cost-feasible narratives separate from those that require unrealistic resource assumptions.

3. `signal_code_origin_tension`

   * Definition: directly equal to `Tension_Code(m)` for a state induced by the model's current narrative.
   * Intended effect: provide a scalar summary of how consistent a given explanation is with the combined error, cost, and accessibility constraints.

4. `signal_counterfactual_separation`

   * Definition: measures how distinguishable the model's internal representations are when conditioned on World T type assumptions versus World F type assumptions for code origin.
   * Intended effect: discourage the model from mixing properties of low-tension and high-tension worlds in a single explanation.

### 7.2 Architectural patterns

We outline module patterns that can reuse Q072 structures without exposing any deep TU generative rules.

1. `CodeTensionHead`

   * Role: auxiliary head that, given an internal representation of a code-origin scenario, outputs an estimate of `Tension_Code(m)` and its components.
   * Interface:

     * Input: internal embeddings encoding code structure and environment.
     * Output: scalar tension estimate and a small vector containing approximate `DeltaS_error`, `DeltaS_cost`, and `DeltaS_access`.

2. `OriginMechanismClassifier`

   * Role: a classifier that maps narrative fragments to major origin mechanism classes (stereochemical, frozen accident, coevolutionary, mixed) and reports expected contributions to each mismatch component.
   * Interface:

     * Input: text or structured representation of an explanation.
     * Output: mechanism-type probabilities and a coarse mapping to which mismatch components are most relevant.

3. `TU_CodeObserver`

   * Role: an observer that extracts simplified code, error, and cost summaries from model-internal states for use by `CodeTensionHead`.
   * Interface:

     * Input: internal embeddings corresponding to sequences, codon tables, or descriptive text.
     * Output: approximate `Code_map`, `Error_impact`, and `Cost_profile` summaries in a fixed low-dimensional format.

### 7.3 Evaluation harness

We propose an evaluation harness to test AI systems augmented with Q072 modules.

1. Task selection

   * A curated set of questions and prompts about:

     * known proposals for the origin of the genetic code,
     * comparative performance of alternative codes,
     * and tradeoffs between chemical constraints and selection.

2. Conditions

   * Baseline condition:

     * The AI model operates without Q072 modules and without explicit tension-aware guidance.

   * TU condition:

     * The model uses `CodeTensionHead` and `TU_CodeObserver` as auxiliary components, and can access tension signals when reasoning about code origin.

3. Metrics

   * Explanation coherence:

     * Does the model maintain a consistent view of which mechanisms are invoked and which constraints they satisfy?

   * Tension awareness:

     * Does the model correctly identify when a proposed mechanism implies high tension, for example extreme fine tuning or inaccessible trajectories?

   * Counterfactual clarity:

     * Does the model keep World T and World F narratives clearly separated when prompted?

### 7.4 60-second reproduction protocol

A minimal protocol for external users to experience the effect of Q072-style encoding in an AI system.

Baseline setup:

* Prompt:

  * Ask the AI to explain why the standard genetic code looks nonrandom and to list main hypotheses for its origin, without any reference to tension, TU, or WFGY.

* Observation:

  * Record whether the explanation:

    * mixes mechanisms without discussing constraints,
    * fails to distinguish rare coincidence from robust processes,
    * or ignores alternative codes and code-space structure.

TU encoded setup:

* Prompt:

  * Ask the same question but add instructions:

    * to treat error robustness, metabolic cost, and accessibility as separate tension components,
    * to explicitly compare low-tension and high-tension interpretations,
    * and to indicate where the standard code might lie in this tension landscape.

* Observation:

  * Record whether the explanation:

    * clearly distinguishes mechanism classes,
    * states which constraints each mechanism addresses,
    * and identifies where tension remains high or where it is plausibly low.

Comparison metric:

* Use a short rubric:

  * clarity of mechanism categorization,
  * explicit handling of constraints,
  * explicit recognition of unresolved high-tension aspects.

What to log:

* Baseline and TU prompts, full responses, and any tension component estimates from `CodeTensionHead`.
* These logs allow independent inspection of how Q072 modules influenced the reasoning process without exposing any deep TU rules.

---

## 8. Cross problem transfer template

This block describes reusable components produced by Q072 and how they transfer to other problems.

### 8.1 Reusable components produced by this problem

1. ComponentName: `CodeOrigin_TensionFunctional`

   * Type: functional

   * Minimal interface:

     * Inputs: summaries of code mappings, error models, cost profiles, and basic accessibility descriptors.
     * Output: scalar `Tension_Code` and component scores `DeltaS_error`, `DeltaS_cost`, `DeltaS_access`.

   * Preconditions:

     * Inputs must describe complete codes under fixed viability and structural constraints.
     * All quantities must be compatible with the encoding class specified in Section 3.7.

2. ComponentName: `CodeSpace_MoveRules_Template`

   * Type: experiment_pattern

   * Minimal interface:

     * Inputs: definitions of allowed local moves in code space, constraints for viability, and initial code ensembles.
     * Output: trajectories or distributions over codes, with associated tension values along paths.

   * Preconditions:

     * Move rules must preserve basic structural features, such as codon counts and essential amino acids.
     * Move rules must be specified independently of the observed code's tension score.

3. ComponentName: `CodeLibrary_FairEnsemble`

   * Type: field / ensemble descriptor

   * Minimal interface:

     * Inputs: structural constraints and chemical bias rules.
     * Output: description of a finite ensemble of codes and a sampling procedure consistent with fairness constraints.

   * Preconditions:

     * Ensemble definitions must be independent of performance metrics for the standard code.
     * Ensemble construction must be auditable and fixed before evaluating `Tension_Code(m_obs)`.

### 8.2 Direct reuse targets

1. Q073 (BH_BIO_EVO_COMPLEXITY_L3_073)

   * Reused components:

     * `CodeOrigin_TensionFunctional`, `CodeSpace_MoveRules_Template`.

   * Why it transfers:

     * Evolutionary complexity over deep time depends on which regions of code space are reachable and how code properties constrain evolvability.

   * What changes:

     * The emphasis shifts from origin scenarios to long-term diversification under a fixed or slowly changing code.

2. Q076 (BH_BIO_IMMUNE_CODE_L3_076)

   * Reused components:

     * `CodeLibrary_FairEnsemble`.

   * Why it transfers:

     * Immune receptor repertoires can be seen as coding systems under robustness and diversity constraints.

   * What changes:

     * The alphabet and move rules differ, but the idea of fair ensembles under structural constraints remains the same.

3. Q059 (BH_CS_INFO_THERMODYN_L3_059)

   * Reused components:

     * `CodeOrigin_TensionFunctional`.

   * Why it transfers:

     * The functional gives a concrete example where information encoding trades off robustness, cost, and accessibility, which can be mapped to information-thermodynamic questions.

   * What changes:

     * Inputs now describe more abstract codes or communication protocols rather than genetic codes, but tension components remain analogous.

---

## 9. TU roadmap and verification levels

This block explains how Q072 is positioned along the TU verification ladder and what the next measurable steps are, within the encoding class of Section 3.7.

### 9.1 Current levels

* E_level: E1

  * A coherent effective-layer encoding of the origin-of-code problem has been specified for an admissible encoding class.
  * Tension components `DeltaS_error`, `DeltaS_cost`, `DeltaS_access`, and `Tension_Code` are defined relative to fixed reference libraries and move ensembles.
  * At least two discriminating experiment patterns with clear falsification conditions have been outlined.

* N_level: N1

  * The narrative explicitly separates:

    * main mechanism classes (stereochemical, frozen accident, coevolutionary, mixed),
    * low-tension and high-tension worlds,
    * and roles of error robustness, cost feasibility, and accessibility.

  * Counterfactual worlds are described in terms of observable tension patterns without invoking hidden TU generative rules.

### 9.2 Next measurable step toward E2

To advance Q072 from E1 to E2, at least one of the following should be implemented inside a concrete encoding `E`:

1. A concrete numerical study that:

   * instantiates `Library_random` and `Library_chem_constrained` under clearly stated constraints,
   * computes `Tension_Code` for the standard code and for all library members using a fixed choice of `D`, `F`, and `W`,
   * and publishes the resulting distributions and ranks as open data with full configuration records.

2. A simulation of code-space dynamics that:

   * uses a well-defined `CodeSpace_MoveRules_Template`,
   * generates trajectories from simple starting codes,
   * and compares accessibility of low-tension regions with and without chemically informed constraints.

Both steps must be documented in a way that allows independent reproduction and audit of the encoding choices.

### 9.3 Next measurable step toward N2

To advance Q072 from N1 to N2, at least one of the following should be achieved:

1. A standardized explanatory template that:

   * maps any proposed code-origin mechanism into contributions to `DeltaS_error`, `DeltaS_cost`, and `DeltaS_access`,
   * and clearly flags where high consistency tension remains and which parts of the code are left unexplained.

2. A small set of case studies:

   * where different origin narratives are analyzed side by side using the same tension framework,
   * highlighting which aspects of the code each narrative explains, which aspects remain under high tension, and how sensitive these conclusions are to encoding choices.

### 9.4 Long-term role in the TU program

In the long term, Q072 is expected to serve as:

* The central biological example of how discrete codes can arise from constrained dynamics in large combinatorial spaces.
* A bridge between origin-of-life research, information theory, and socio-technical code problems such as language emergence.
* A calibration point for how far TU-style consistency tension can go in structuring reasoning about complex historical processes without claiming reconstruction of the full deep-layer generative rules.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non-specialists, while remaining aligned with the effective-layer description.

The genetic code is the rulebook that tells cells how to turn sequences of three nucleotides into amino acids. There are many possible rulebooks of this kind, but life on Earth uses just one main version. This raises a natural question:

* Why this particular rulebook, and how did it come to be?

Simple chance seems unlikely, because the standard code is surprisingly good at:

* making common errors less harmful,
* balancing the cost of building different amino acids,
* and keeping similar amino acids grouped together in codon space.

In the Tension Universe view, instead of trying to replay early Earth in full detail, we ask a more controlled question:

* If we compare our code to many alternative codes that respect basic constraints,
* and if we look at how easy it is to reach such codes under simple changes,
* do we see our code as a natural, low-tension outcome,
* or as a fragile, high-tension coincidence?

To do this, we imagine a space of possible codes. For each code we measure:

1. How bad typical errors are, which we call error robustness.

2. How expensive the amino acids are on average, which we call cost feasibility.

3. How easy it is to move from one code to another by small changes without breaking the system, which we call accessibility.

We then combine these into a single tension score for each code.

We consider two kinds of worlds:

* In a low-tension world:

  * our code scores well but not impossibly well,
  * many paths in code space can reach codes with similar tension,
  * and different broad mechanisms point toward the same region of good codes.

* In a high-tension world:

  * our code looks like an extreme outlier,
  * simple paths rarely reach anything as good or better,
  * and different plausible mechanisms do not agree on why this code should appear.

This framework does not tell us exactly how the genetic code originated, and it does not claim to solve the open problem. What it does provide is:

* a precise way to express what it would mean for an explanation to be robust and natural,
* a way to test whether particular models or parameter choices make the code look low-tension or high-tension,
* and a set of reusable tools for other problems where complex codes must match physical and evolutionary constraints.

In the Tension Universe project, Q072 is the reference problem for all such biological coding questions at the effective layer.

---

## Tension Universe effective-layer footer

### Scope of claims

* This page is part of the WFGY / Tension Universe S-problem collection.
* The goal of this document is to specify an effective-layer encoding of the origin-of-code problem for the genetic code.
* It does not claim to solve the canonical origin-of-code problem in molecular evolution or origin-of-life research.
* It does not introduce any new theorem beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open biological problem has been solved.

### Effective-layer boundary

* All objects used here (state spaces such as `M_code`, observables, invariants, tension scores, counterfactual worlds) live at the effective layer of the TU framework.
* They are defined only up to coarse-grained summaries and encoding choices, as described in Section 3.7.
* No explicit mapping from raw biochemical or evolutionary data to internal TU fields is specified.
* No deep TU axioms, generative rules, or equations of motion are exposed or relied upon in this document.

### Encoding and fairness

* Any concrete instantiation of this page requires selecting an admissible encoding `E = (D, F, W, L)` from the encoding class defined in Section 3.7.
* All such selections must be fixed and recorded before evaluating `Tension_Code(m_obs)` for the observed genetic code or for any particular historical scenario.
* Changing `D`, `F`, `W`, or `L` in response to observed tension values defines a new encoding that must be treated as a separate instance and re-evaluated from scratch.
* These requirements follow the TU Encoding and Fairness Charter and are intended to prevent hidden tuning that would trivialize tension-based claims.

### Falsifiability and experiments

* Section 6 outlines experiment patterns that can falsify or refine specific Q072 encodings at the effective layer.
* Falsification of a particular encoding shows that its way of measuring or organizing consistency tension is inadequate for this problem.
* Such falsification does not settle the biological origin-of-code question and does not constrain other TU problems.
* Successful experiments increase confidence that the chosen encoding captures something meaningful about code-origin constraints but do not amount to a proof of any deep TU claim.

### Relation to TU charters

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
