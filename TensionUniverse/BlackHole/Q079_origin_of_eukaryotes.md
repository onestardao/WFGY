<!-- QUESTION_ID: TU-Q079 -->
# Q079 · Origin of eukaryotes

## 0. Header metadata

```txt
ID: Q079
Code: BH_BIO_ORIGIN_EUKARYOTES_L3_079
Domain: Biology
Family: Evolutionary and cell biology
Rank: S
Projection_dominance: P
Field_type: dynamical_field
Tension_type: consistency_tension
Status: Open
Semantics: hybrid
E_level: E1
N_level: N2
Last_updated: 2026-01-30
```

---

## 0. Effective layer disclaimer

All statements in this entry are made strictly at the effective layer of the Tension Universe (TU) framework.

This page only specifies:

* state spaces and effective encodings,
* observables, invariants and tension functionals,
* experiment templates and falsification conditions,
* and reusable components for AI or engineering use.

This page does not:

* propose or endorse any particular bottom layer axiom system for TU,
* describe any hidden generative rule that produces TU fields from raw physical or biological data,
* or provide any constructive mapping from empirical datasets to TU bottom layer objects.

For the biological problem itself:

* this entry does not claim to solve the canonical origin of eukaryotes,
* it does not introduce any new theorem about the historical sequence or mechanisms of eukaryogenesis,
* and it should not be cited as evidence that the canonical question has been answered.

The only claims made here are:

* that a specific effective layer encoding of Q079 has been defined,
* that this encoding can be tested and possibly falsified by experiments and model studies,
* and that its components can be reused in other problems while remaining inside the effective layer boundary.

---

## 1. Canonical problem and status

### 1.1 Canonical statement

The canonical problem behind Q079 can be phrased as follows:

> Explain how the first eukaryotic cells arose from prokaryote like ancestors, in a way that is consistent with:
>
> * genomic and phylogenetic evidence,
> * cell biological and structural evidence,
> * bioenergetic and ecological constraints,
> * and the observed diversity of modern eukaryotes.

In standard biological terms, the question asks:

1. What were the identities and properties of the partner lineages that gave rise to the first eukaryotic cells
   for example host archaeal lineage, bacterial endosymbiont lineages such as proto mitochondria and proto plastids?

2. By what sequence of events did these partners establish a stable endosymbiotic relationship, including:

   * entry of the symbiont into the host,
   * stabilization of residence inside the host,
   * gene transfer and genome reduction,
   * evolution of organelles and compartmentalization?

3. How did this process produce the characteristic features of eukaryotes:

   * nuclei and internal membrane systems,
   * mitochondria and later plastids,
   * cytoskeletal complexity,
   * greatly increased cell size and genome complexity?

The problem is not only to describe a plausible narrative. The deeper question is whether there exists a relatively simple and reusable integration pattern that can account for:

* the emergence of eukaryotic complexity,
* the repeated appearance of organelles through primary and secondary endosymbiosis,
* and the tight link between bioenergetic capacity and genomic complexity.

### 1.2 Status and difficulty

Several major components of the problem are widely accepted:

* Mitochondria and plastids are of bacterial origin and are descendants of once free living bacteria.
* Eukaryotes likely arose from a partnership between an archaeal host and a bacterial endosymbiont.
* Modern eukaryotes show extensive chimerism in their genomes, with both archaeal and bacterial contributions.
* Bioenergetic arguments suggest that mitochondria provided a qualitative jump in energy per gene that enabled large complex genomes.

However, many details remain open or strongly debated:

* The exact nature of the host lineage, for example which group within Asgard archaea and what its cell biology looked like.

* The sequence and timing of key transitions:

  * endosymbiont entry,
  * establishment of stable endosymbiosis,
  * evolution of internal membranes and cytoskeleton,
  * origin of the nucleus.

* The degree to which eukaryogenesis was:

  * a rare accident with many hard to repeat steps,
  * versus a generic outcome of certain ecological and bioenergetic conditions.

From a scientific standpoint, the problem is considered extremely hard because it combines:

* incomplete and biased fossil and molecular records,
* many potential historical contingencies,
* limited ability to perform experiments that directly replay deep time events.

There is also a structural difficulty. It is nontrivial to write down a compact and testable description of how genomes, energy flows, compartment structure and ecology can be jointly consistent with the origin and stability of eukaryotic cells.

### 1.3 Role in the BlackHole project

Within the BlackHole S problem collection, Q079 plays three roles.

1. It is a flagship example of a consistency_tension problem in evolutionary and cell biology, where:

   * multiple levels of description genomes, organelles, cells, ecosystems must be mutually consistent,
   * and the existence of complex cells depends on resolving tensions between these levels.

2. It provides a test ground for hybrid field encodings, where:

   * discrete structures genes, operons, organelles, compartments, lineages,
   * and continuous quantities energetic fluxes, population parameters, rate constants
     are combined into a single effective state space.

3. It anchors a family of biological problems that reuse its components:

   * biosphere level limits on complexity and energy Q080,
   * host microbe consortia and microbiomes Q077,
   * organellar conflict and aging Q075,
   * symbiosis inspired architectures in AI Q123.

### References

1. Lynn Margulis. Symbiosis in Cell Evolution: Life and its Environment on the Early Earth. W. H. Freeman, 1981.
2. Nick Lane, William Martin. The energetics of genome complexity. Nature 467, 929–934, 2010.
3. Bruce Alberts et al. Molecular Biology of the Cell. Garland Science, latest edition, chapters on mitochondria, chloroplasts, and the origin and evolution of eukaryotes.
4. A. J. Roger, S. A. Muñoz Gómez, R. Kamikawa. The origin and diversification of mitochondria. Current Biology 27(21): R1177–R1192, 2017.
5. Hiroyuki Imachi et al. Isolation of an archaeon at the prokaryote eukaryote interface. Nature 577, 519–525, 2020.
6. William Martin, Miklós Müller. The hydrogen hypothesis for the first eukaryote. Nature 392, 37–41, 1998.
7. Douglas Futuyma et al. Evolution. Sinauer Associates or equivalent, chapters on eukaryote origins and complex cells.

---

## 2. Position in the BlackHole graph

This block records how Q079 sits inside the BlackHole graph as nodes and edges among Q001 to Q125. Each edge is listed with a one line reason that points to a concrete component or tension type.

### 2.1 Upstream problems

These problems provide prerequisites, tools, or general foundations that Q079 relies on at the effective layer.

* Q071 (BH_BIO_ORIGIN_L3_071)
  Reason: Provides origin of minimal cells and replicators and defines the pre eukaryotic state space `M_pre` from which `M_euk` is extended.

* Q072 (BH_BIO_GENETIC_CODE_L3_072)
  Reason: Fixes the shared genetic code and translational machinery that both host and symbiont inherit and that appear inside `G_host(m)` and `G_sym(m)`.

* Q074 (BH_BIO_CELL_DIFFER_L3_074)
  Reason: Supplies general mechanisms of compartment formation and cell differentiation that are reused in the component `C_comp(m)`.

* Q078 (BH_BIO_DEVELOPMENTAL_L3_078)
  Reason: Provides `DevMap_field` and genotype to phenotype consistency_tension, which are reused in `P_euk(m)` to describe early developmental like patterns in emerging eukaryotes.

### 2.2 Downstream problems

These problems are direct reuse targets of Q079 components or depend on Q079 tension structure.

* Q080 (BH_BIO_BIOSPHERE_LIMITS_L3_080)
  Reason: Reuses `EukCompartment_field` and `Euk_energy_profile` to relate eukaryotic complexity to biosphere level energy and adaptability limits.

* Q077 (BH_BIO_MICROBIOME_L3_077)
  Reason: Uses the `Host_symbiont_partnership_profile` observable as a template for describing host microbiome consortia stability and conflict.

* Q075 (BH_BIO_AGING_L3_075)
  Reason: Reuses `Organellar_conflict_tension` derived from Q079 to model long term breakdown of host organelle integration in aging cells.

### 2.3 Parallel problems

Parallel nodes share similar tension types but no direct component dependence.

* Q063 (BH_CHEM_PROTEIN_FOLDING_L3_063)
  Reason: Both Q079 and Q063 involve mapping from many small building blocks into complex, stable configurations under strong energetic and structural constraints.

* Q059 (BH_CS_INFO_THERMODYN_L3_059)
  Reason: Both treat consistency_tension between information structures, physical capacity and energy costs as a key organizing principle.

### 2.4 Cross domain edges

Cross domain edges connect Q079 to problems in other domains that can reuse its components.

* Q031 (BH_PHYS_QINFO_L3_031)
  Reason: Reuses `Compartment_channel_capacity` style observables to compare biological compartmentalization with constrained information channels in quantum and classical systems.

* Q123 (BH_AI_INTERP_L3_123)
  Reason: Uses the `Symbiosis_to_architecture_template` derived from Q079 to interpret layered AI systems as integrated host symbiont style architectures under consistency_tension.

---

## 3. Tension Universe encoding (effective layer)

All content in this block is at the effective layer. We only describe state spaces, effective mappings, observables, invariants, tension functionals and band structures. We do not describe any hidden bottom layer rules or any mapping from raw data to TU bottom layer objects.

### 3.0 Encoding summary

We define an encoding class for Q079 in the form:

```txt
E_euk = (D, F, W, L)
```

with the following components.

* `D` is a class of data maps that:

  * take external biological or model data about early cells, host symbiont partnerships and environments,
  * produce effective states `m` in `M_euk`,
  * and assign indices into finite libraries of modules and reference patterns.

* `F` is a family of observables and functionals that act on `M_euk`, including:

  * fields such as `Euk_energy_profile(m; r)`, `Complexity_load(m; r)`,
    `Host_symbiont_conflict(m; r)`, `Integration_modularity(m; r)`,
  * mismatch and tension constructs such as `DeltaS_euk(m; r)`,
    invariants such as `I_energy(m)` and `I_integration(m)`,
  * and the global tension functional `Tension_euk(m)`.

* `W` is a parameter and library collection that includes:

  * finite libraries of modules for host, symbiont, couplings, compartments, phenotypes and environments,
  * a refinement index set `R_res_euk` and evaluation subsets `R_eval` and its task specific subfamilies,
  * reference classes such as `Ref_euk` and reference relationships such as `Ref_energy_complexity`,
  * weight vectors such as `(w_energy, w_complexity, w_conflict, w_modularity)`,
  * and a finite band library `L_ref_euk` of tension intervals.

* `L` is a list of system and dataset classes for which this encoding is declared applicable, for example:

  * comparative datasets of real prokaryotes and eukaryotes,
  * synthetic model worlds of eukaryogenesis,
  * and AI models that carry an internal eukaryogenesis representation.

An encoding instance is written as:

```txt
E*_euk = (D*, F*, W*, L*)
```

where the star indicates a concrete choice of data maps, observables, parameters, libraries and applicability domain, fixed in advance before any evaluation in experiments.

The functional family `{Gamma_r}` that appears below is treated as part of `F` and `W`. It is not the whole encoding by itself.

### 3.1 State space

We assume an effective state space

```txt
M_euk
```

Each state `m` in `M_euk` represents a coherent configuration for early eukaryogenesis, encoded as an effective tuple:

```txt
m = (G_host(m), G_sym(m), R_coupling(m), C_comp(m), E_env(m), P_euk(m))
```

where:

* `G_host(m)` is an effective descriptor of host genomic and metabolic modules.
* `G_sym(m)` is an effective descriptor of symbiont genomic and metabolic modules.
* `R_coupling(m)` is an effective descriptor of regulatory and signaling couplings between host and symbiont.
* `C_comp(m)` is an effective descriptor of compartmental structure, including membranes, organelles and trafficking routes.
* `E_env(m)` is an effective descriptor of environmental and ecological context, including available energy sources.
* `P_euk(m)` is an effective descriptor of eukaryotic phenotypes such as cell size, genome complexity, organelle complement and basic life history traits.

We only assume that for relevant historical or model scenarios there exist states in `M_euk` that encode:

* host and symbiont configurations,
* their couplings,
* compartmental structures,
* environmental context,
* and resulting eukaryotic phenotypes.

No details are given here on how these effective descriptors are constructed from empirical data. That is delegated to the data maps in `D` and instantiated in `D*` when an encoding instance `E*_euk` is fixed.

### 3.2 Finite libraries and admissible encodings

We introduce finite or countable libraries of modules:

```txt
Lib_G_host = {gh_1, ..., gh_Nh}
Lib_G_sym  = {gs_1, ..., gs_Ns}
Lib_R_cpl  = {rc_1, ..., rc_Nc}
Lib_C_comp = {cc_1, ..., cc_Ncc}
Lib_P_euk  = {pe_1, ..., pe_Np}
Lib_E_env  = {ee_1, ..., ee_Ne}
```

Each element is an effective building block. For example:

* `gh_k` may represent an archetypal host metabolic and regulatory package.
* `gs_l` may represent proto mitochondrial traits relevant to energy transduction.
* `cc_j` may represent a particular organelle or transport architecture.
* `pe_u` may represent a coarse phenotypic pattern, such as a class of eukaryotic cell types.

We also introduce an index set of resolutions:

```txt
R_res_euk = {r_1, r_2, ..., r_K, ...}
```

with a refinement order `<=` such that:

* `r_1 <= r_2 <= ...`,
* and moving from `r` to `r'` with `r' >= r` corresponds to adding more detail or finer resolution, never reducing information.

An admissible encoding map in the E_euk class is any map of the form:

```txt
Gamma_r : (G_host, G_sym, R_coupling, C_comp, E_env) -> P_euk
```

for some `r` in `R_res_euk`, satisfying:

1. For each `r`, the functional form of `Gamma_r` and any hyperparameters are fixed in advance and do not depend on the particular world or dataset to be evaluated.
2. `Gamma_r` can only use modules selected from the libraries above.
3. The family `{Gamma_r}` is fixed before evaluating tension or invariants and is not tuned in response to those evaluations.
4. Refinement means moving from `Gamma_r` to `Gamma_r'` with `r' >= r` in the fixed order, not redefining the library or the functional family.

We denote the set of all such admissible encoding maps as:

```txt
E_euk_maps = {Gamma_r | r in R_res_euk and Gamma_r satisfies conditions (1) to (4)}
```

The pair `(R_res_euk, E_euk_maps)` is part of `W`. A concrete choice for an encoding instance `E*_euk` appears inside `W*`.

This definition acts as a fairness constraint at the map level. Encodings cannot be chosen after seeing outcomes in order to artificially minimize tension.

### 3.3 Effective fields and observables

On `M_euk` and for a chosen `Gamma_r` in `E_euk_maps`, we define the following effective observables.

1. Bioenergetic profile observable

```txt
Euk_energy_profile(m; r)
```

* Input: a state `m` in `M_euk` and a resolution index `r` in `R_res_euk`.
* Output: an effective vector of nonnegative real valued quantities summarizing, for example:

  * ATP flux per cell,
  * ATP flux per gene,
  * energy cost of maintaining compartments and organelles,
  * surplus energy available for regulation and complexity.

2. Complexity load observable

```txt
Complexity_load(m; r)
```

* Input: `m` and `r`.
* Output: an effective vector capturing aspects of genomic and regulatory complexity:

  * genome size,
  * number of expressed genes,
  * degree of regulatory network complexity,
  * number and diversity of organelles.

3. Host symbiont conflict observable

```txt
Host_symbiont_conflict(m; r)
```

* Input: `m` and `r`.
* Output: a nonnegative scalar measuring unresolved conflict between host and symbiont modules, for example:

  * conflicting replication schedules,
  * incompatible expression patterns,
  * selfish symbiont behaviors that reduce host fitness.

4. Integration modularity observable

```txt
Integration_modularity(m; r)
```

* Input: `m` and `r`.
* Output: a nonnegative scalar, with larger values indicating clearer decomposition into stable modules. Examples are distinct organelles with coherent function and regulation.

5. Reference profiles and mismatch observable

We fix in advance a finite reference class of eukaryogenesis scenarios:

```txt
Ref_euk = {Ref_1, ..., Ref_Nref}
```

Each `Ref_k` is an effective tuple of target values for:

* energy profiles,
* complexity loads,
* conflict levels,
* modularity levels,

for a particular resolution `r` or small set of resolutions. The reference class `Ref_euk` is selected before evaluating any particular world or model and remains fixed. It cannot be tuned after observing tension outcomes. `Ref_euk` is part of `W`, and a concrete choice is part of `W*`.

Given `Ref_euk`, we define a mismatch observable:

```txt
DeltaS_euk(m; r) >= 0
```

that measures the deviation of

```txt
(Euk_energy_profile(m; r),
 Complexity_load(m; r),
 Host_symbiont_conflict(m; r),
 Integration_modularity(m; r))
```

from the closest reference pattern in `Ref_euk` at resolution `r`.

We also define fixed nonnegative weights:

```txt
w_energy > 0
w_complexity > 0
w_conflict > 0
w_modularity > 0
w_energy + w_complexity + w_conflict + w_modularity = 1
```

These weights are chosen once, before any evaluation, and are shared across all states and all worlds. They are stored in `W` and instantiated as `W*` in a concrete encoding instance.

The mismatch `DeltaS_euk(m; r)` is constructed using the weights above. The exact aggregation rule is an encoding choice inside `F` and `W`, but in all cases:

* `DeltaS_euk(m; r) = 0` if and only if the encoded observables match a reference pattern exactly,
* `DeltaS_euk(m; r)` increases as deviations from the reference patterns increase.

### 3.4 Tension tensor and global tension functional

We assume an effective semantic tension tensor over `M_euk` in the form:

```txt
T_ij_euk(m; r) = S_i_euk(m; r) * C_j_euk(m; r) * DeltaS_euk(m; r) * lambda_euk(m; r) * kappa_euk
```

where:

* `S_i_euk(m; r)` is a source like factor measuring how strongly the `i`th component of the configuration contributes to tension, for example host genome misalignment.
* `C_j_euk(m; r)` is a receptivity like factor measuring how sensitive the `j`th downstream structure is to that tension, for example fitness consequences in different environments.
* `DeltaS_euk(m; r)` is the mismatch defined above.
* `lambda_euk(m; r)` is a convergence state factor in a bounded interval, indicating whether local reasoning about this configuration is convergent, recursive, divergent or chaotic.
* `kappa_euk` is a constant in `W` that sets the overall scale of eukaryogenesis related consistency_tension.

All quantities are finite for `m` in the regular domain defined below.

We also define a finite evaluation set of resolutions:

```txt
R_eval subset of R_res_euk
R_eval = {r_1, ..., r_M}
```

The set `R_eval` is fixed at design time and stored in `W`. A concrete choice is part of `W*` in an encoding instance `E*_euk`.

The global tension functional is:

```txt
Tension_euk(m) = max over r in R_eval of DeltaS_euk(m; r)
```

Using a maximum over a fixed set of indices avoids unbounded suprema over unconstrained families. `Tension_euk` is part of `F`.

### 3.5 Singular set and domain restrictions

Some observables may fail to be defined or may become non finite if the encoding is incomplete or inconsistent. To ensure that tension summaries remain meaningful, we define a singular set:

```txt
S_sing_euk = {
  m in M_euk :
    for some r in R_eval,
    Euk_energy_profile(m; r),
    Complexity_load(m; r),
    Host_symbiont_conflict(m; r),
    Integration_modularity(m; r),
    or DeltaS_euk(m; r)
    is undefined or not finite
}
```

We then restrict all invariants and experiments to the regular domain:

```txt
M_euk_reg = M_euk \ S_sing_euk
```

Whenever a proposed state for analysis lies in `S_sing_euk`, evaluations of `Tension_euk` and related invariants are treated as out of domain. They are not used as evidence for or against any hypothesis about eukaryote origins.

This domain restriction is part of `F` and `W`. Any encoding instance `E*_euk` must respect it.

### 3.6 Band library and invariants

We define a band library for eukaryogenesis tension:

```txt
L_ref_euk = {B_1, ..., B_K}
B_j = [T_min_j, T_max_j]
0 <= T_min_j <= T_max_j < +infinity
```

Each `B_j` is a closed interval of nonnegative real numbers. The collection `L_ref_euk` is part of `W`. A concrete choice of intervals is part of `W*` in an encoding instance.

Typical intended roles include:

* one or more low tension bands that capture reusable integration patterns,
* one or more high tension bands that signal unstructured or idiosyncratic scenarios.

We also define two effective invariants on `M_euk_reg` using the observables above.

1. Energy complexity consistency invariant

We fix in advance a reference function:

```txt
Ref_energy_complexity(r)
```

that encodes the expected relationship between bioenergetic capacity and complexity load, inspired by but not identical to arguments in the literature. `Ref_energy_complexity` is part of `W`.

For each `m` in `M_euk_reg` we define:

```txt
I_energy(m) =
  max over r in R_eval of
    Energy_mismatch(m; r)
```

where `Energy_mismatch(m; r)` is a nonnegative scalar derived from the difference between:

* the observed relationship between `Euk_energy_profile(m; r)` and `Complexity_load(m; r)`,
* the reference relationship given by `Ref_energy_complexity(r)`.

`Energy_mismatch` and `I_energy` are part of `F`.

2. Integration stability invariant

We define:

```txt
I_integration(m) =
  max over r in R_eval of
    DeltaS_euk(m; r)
```

This invariant summarizes the worst case mismatch between the encoded integration pattern and the reference class across the chosen resolutions. By construction `I_integration(m)` is equal to `Tension_euk(m)` when both use the same `R_eval`.

Both invariants are well defined and finite on `M_euk_reg`. They are built using fixed reference objects in `W`, fixed evaluation resolutions, and weight vectors in `W`. They are not tuned in response to particular worlds.

### 3.7 Fair encoding and pre commitment

The encoding class `E_euk` is constrained by fairness and pre commitment rules that implement the TU Encoding and Fairness Charter at the effective layer. In particular:

1. All libraries, resolutions, reference classes, weight vectors and band libraries in `W` must be specified before any tension based evaluation is performed.

2. A concrete encoding instance `E*_euk = (D*, F*, W*, L*)` must be fixed before running an experiment or evaluation. This includes explicit choices of `{Gamma_r}`, `R_eval`, `Ref_euk`, `Ref_energy_complexity`, weight vectors and band intervals.

3. Thresholds such as `epsilon_euk`, `delta_euk`, `epsilon_energy`, `delta_energy`, and upper bounds such as `T_max` must be components of `W*`. They cannot be adjusted after observing tension values.

4. Changes to `W*` after an experiment that are motivated by the results invalidate that experiment as evidence for or against the corresponding encoding.

5. Any claim that a world is in a low tension or high tension regime must be made relative to a fixed encoding instance `E*_euk` and fixed bands in `L_ref_euk`. It is not meaningful to search over different encodings until a desired regime is obtained.

These rules ensure that Q079 encodings cannot be silently tuned to fit a preferred narrative. They only test whether a fixed encoding instance is aligned with data and model worlds.

---

## 4. Tension principle for this problem

This block states how Q079 is characterized as a tension problem within TU, at the effective layer, using the objects defined above.

### 4.1 Core tension functional and bands

We use the global tension functional:

```txt
Tension_euk(m) = max over r in R_eval of DeltaS_euk(m; r)
```

and interpret it as a scalar measure of how well a particular configuration `m` in `M_euk_reg` embodies a coherent, reusable pattern of eukaryogenesis.

By construction:

* `Tension_euk(m) >= 0` for all `m` in `M_euk_reg`.
* `Tension_euk(m)` is small if all evaluated resolutions show good agreement with the reference class `Ref_euk`.
* `Tension_euk(m)` is large if any evaluated resolution exhibits strong mismatch.

The band library `L_ref_euk` partitions the nonnegative axis into meaningful regions. For example:

* a low tension band `B_low` in `L_ref_euk` may be chosen as `[0, T_low_max]`,
* a high tension band `B_high` may be chosen as `[T_high_min, +infinity)`.

These choices are part of `W*`. Once fixed, they cannot be adjusted during analysis of particular worlds.

Different admissible encoding instances `E*_euk` may change the numerical value of `Tension_euk`, but they all respect the same fairness constraints:

* fixed libraries and reference classes,
* fixed weight vectors,
* fixed evaluation resolutions,
* and fixed tension bands in `L_ref_euk`.

### 4.2 Low tension eukaryogenesis principle

At the effective layer, the low tension principle for Q079 can be stated as follows.

> There exists at least one admissible encoding instance `E*_euk = (D*, F*, W*, L*)` and a low tension band `B_low` in `L_ref_euk` such that in the actual universe there are world representing states `m_T` in `M_euk_reg` with
>
> `Tension_euk(m_T)` in `B_low`
>
> and with the following properties:
>
> * bioenergetic capacity and complexity load are jointly consistent with a simple reference relationship across scales,
> * host symbiont conflicts are resolved by a relatively small set of reusable patterns,
> * integration modularity is high and stable across lineages.

Intuitively, under a low tension encoding instance:

* the origin of eukaryotes can be described by a compact set of integration rules,
* those rules are reused across multiple lineages and endosymbiotic events,
* and bioenergetic constraints are satisfied in a systematic way rather than by a sequence of unrelated accidents.

This principle does not assert that the universe is guaranteed to be low tension. It only asserts that it is meaningful, under an encoding instance `E*_euk`, to test whether the universe lies in a low tension band.

### 4.3 High tension eukaryogenesis principle

The contrasting high tension principle is stated in terms of the same encoding class.

> For an encoding instance `E*_euk = (D*, F*, W*, L*)` and any low tension band `B_low` in `L_ref_euk`, a world is in a high tension regime if every world representing state `m_F` in `M_euk_reg` that correctly encodes that world satisfies
>
> `Tension_euk(m_F)` in a band `B_high` in `L_ref_euk`
>
> where `B_high` is disjoint from `B_low` and has strictly positive lower bound.

In such worlds:

* there is no stable relationship between energy supply and complexity that fits the chosen `Ref_energy_complexity`,
* host symbiont conflicts are not resolved by any small reusable set of patterns,
* compartment structures and integration patterns differ so much between lineages that a single reference class `Ref_euk` cannot capture them without high mismatch.

Q079, at the effective layer, does not claim that the actual universe is known to lie in `B_low` or `B_high`. It only formalizes what these regimes would mean for a fixed encoding instance and band library, and sets up experiments that can falsify specific encodings.

---

## 5. Counterfactual tension worlds

We now outline two counterfactual worlds, both described strictly at the effective layer and relative to a fixed encoding instance `E*_euk = (D*, F*, W*, L*)`.

* World T: eukaryogenesis is governed by a structured, reusable integration pattern that produces low tension states in `B_low`.
* World F: eukaryogenesis is essentially unstructured and idiosyncratic, and only high tension states in `B_high` exist.

Each world is described through patterns of observables and invariants, not through any hidden construction rules.

### 5.1 World T (structured low tension eukaryogenesis)

In World T, under a fixed encoding instance `E*_euk` and chosen bands:

1. Energy complexity alignment

* For world representing states `m_T` in `M_euk_reg`, the invariant `I_energy(m_T)` remains within a controlled band:

  ```txt
  I_energy(m_T) <= epsilon_energy
  ```

  where `epsilon_energy` is a constant in `W*`. As resolution increases within `R_eval`, the relationship between energy supply and complexity load stays close to the reference `Ref_energy_complexity(r)`.

2. Host symbiont conflict resolution

* For most relevant states `m_T`, the observable `Host_symbiont_conflict(m_T; r)` is low across resolutions in `R_eval`, and the integration modularity is high:

  ```txt
  Host_symbiont_conflict(m_T; r) is small
  Integration_modularity(m_T; r) is large
  ```

  indicating that conflicts are resolved by a small set of reusable mechanisms such as gene transfer, genome reduction and compartment formation.

3. Cross lineage reuse

* The same libraries `Lib_G_host`, `Lib_G_sym`, `Lib_C_comp` and `Lib_R_cpl` can be used to describe:

  * mitochondria based origins,
  * plastid acquisition,
  * and secondary or tertiary endosymbioses,

  with only moderate increases in `DeltaS_euk(m_T; r)`. The reference class `Ref_euk` remains adequate without a lineage specific explosion in mismatch.

4. Global tension band

* The global tension functional satisfies:

  ```txt
  Tension_euk(m_T) in B_low subset of L_ref_euk
  ```

  for most world representing states and for a wide range of lineages. This indicates that Q079 sits in a low tension regime for this encoding instance.

### 5.2 World F (unstructured high tension eukaryogenesis)

In World F, for the same encoding instance and band library:

1. Energy complexity misalignment

* For world representing states `m_F`, the invariant `I_energy(m_F)` is large:

  ```txt
  I_energy(m_F) >= delta_energy
  ```

  for some positive `delta_energy` in `W*`. Attempts to encode a coherent relationship between energy supply and complexity across lineages fail, with different lineages requiring incompatible relationships.

2. Host symbiont conflict persistence

* The observable `Host_symbiont_conflict(m_F; r)` remains high for some resolutions in `R_eval`, and integration modularity is low:

  ```txt
  Host_symbiont_conflict(m_F; r) is large
  Integration_modularity(m_F; r) is small or unstable
  ```

  Conflicts are resolved, if at all, by lineage specific, non reusable mechanisms that do not compress into a small set of patterns.

3. Cross lineage failure

* Any attempt to use the fixed reference class `Ref_euk` and fixed libraries to describe all lineages leads to large mismatch:

  ```txt
  DeltaS_euk(m_F; r) is large for some r in R_eval
  ```

* To reduce mismatch for one lineage, one must introduce special modules that increase mismatch for others, or violate the finite library assumption. This prevents a unified low tension encoding for the whole world.

4. Global tension band

* For world representing states in World F:

  ```txt
  Tension_euk(m_F) in B_high subset of L_ref_euk
  ```

  where `B_high` is a band with strictly positive lower bound. This signifies a high tension regime for the given encoding instance.

### 5.3 Interpretive note

These counterfactual worlds do not assert any specific historical narrative or mechanistic sequence. They only state that:

* if there exist effective encodings that faithfully represent a eukaryote bearing universe,
* then low tension and high tension regimes would manifest as different patterns in the observables and invariants defined above.

The question of which regime the actual universe belongs to is empirical and model dependent. It is not settled within this block and depends on both the chosen encoding instance `E*_euk` and the available data.

---

## 6. Falsifiability and discriminating experiments

This block specifies experiments and protocols, at the effective layer, that can:

* test the coherence of the Q079 encoding,
* discriminate between different families of tension encodings,
* and provide evidence about whether eukaryogenesis behaves more like a low tension or high tension process under this framework.

These experiments cannot prove or disprove any specific biological hypothesis by themselves. They can only falsify specific TU encoding instances related to Q079.

In all experiments below, we assume that an encoding instance

```txt
E*_euk = (D*, F*, W*, L*)
```

has been fixed in advance. All libraries, reference objects, evaluation sets, thresholds and bands that appear are components of `W*`.

### Experiment 1: Comparative bioenergetic scaling

*Goal*
Test whether there exists an encoding instance in `E_euk` such that real prokaryote and eukaryote data produce a stable low band of `I_energy(m)` values for eukaryotes, while preserving a meaningful distinction from prokaryotes.

*Setup*

* Input data external to TU:

  * comparative datasets of cell volume, genome size, gene count,
  * estimates of ATP flux per cell and per gene for representative bacteria, archaea and eukaryotes.

* Choose once, as part of `W*`:

  * a finite subset `R_eval_energy` of `R_eval` for energy and complexity,
  * a family of maps `{Gamma_r}` in `E_euk_maps`,
  * a reference function `Ref_energy_complexity(r)` and mismatch function `Energy_mismatch(m; r)`,
  * a low band `[0, epsilon_energy]` for `I_energy` and possibly additional bands in `L_ref_euk`.

* All these choices are fixed before looking at any tension results.

*Protocol*

1. For each taxon in the dataset, use the data maps `D*` to construct an effective state `m_data` in `M_euk_reg` by:

   * encoding host and symbiont modules if applicable,
   * encoding environment summary,
   * assigning an effective phenotype summary.

   Construction details are external to TU and belong to `D*`. They are fixed before evaluation.

2. For each `m_data` and each `r` in `R_eval_energy`, evaluate:

   * `Euk_energy_profile(m_data; r)`,
   * `Complexity_load(m_data; r)`,
   * `Energy_mismatch(m_data; r)`.

3. Compute `I_energy(m_data)` for each state using:

   ```txt
   I_energy(m_data) =
     max over r in R_eval_energy of Energy_mismatch(m_data; r)
   ```

4. Separate states into:

   * prokaryote like states bacteria and archaea,
   * eukaryote states including proto eukaryotes if data exist.

*Metrics*

* Distribution of `I_energy(m_data)` for prokaryote and eukaryote states.
* Separation between distributions, for example differences in medians or quantiles.
* Stability of these distributions when `R_eval_energy` is expanded within `R_eval` or when additional taxa are added, as long as expansions are pre specified in `W*`.

*Falsification conditions*

*Condition A: no robust separation*
If, for this fixed encoding instance `E*_euk`, every reasonable choice of `R_eval_energy` in `W*` produces distributions of `I_energy(m_data)` for prokaryotes and eukaryotes that largely overlap, and no low band in `L_ref_euk` can be assigned to a broad eukaryote cluster without also including a comparable set of prokaryotes, then:

* the current specification of `Ref_energy_complexity`, `Energy_mismatch`, and the related components of `W*` is considered falsified as an encoding of Q079.

*Condition B: instability under refinement*
If small, pre specified refinements of `R_eval_energy` within `R_eval` cause large, unstructured swings in `I_energy(m_data)` for the same taxa, then:

* the encoding instance `E*_euk` is considered unstable at the effective layer and is rejected.

In both cases, falsification applies to this specific encoding instance, not to the canonical biological problem. Alternative encoding instances in `E_euk` may still be valid targets for future tests, but they must be fixed and logged as new `E*_euk` objects in `W*`.

*Semantics implementation note*
All quantities are implemented with hybrid semantics as declared in Block 0. Discrete components such as module identities and taxon labels are treated as elements of finite sets, and continuous components such as fluxes and sizes are treated as real valued fields. No additional semantic regime is introduced in this experiment.

*Boundary note*
Falsifying a TU encoding instance is not the same as solving the canonical biological problem. This experiment can reject specific designs of `Euk_energy_profile` and related functionals, but it does not by itself establish any particular historical scenario for eukaryote origins.

---

### Experiment 2: Reconstruction of endosymbiotic histories

*Goal*
Test whether a single fixed library and encoding instance can describe primary and secondary endosymbiotic events with moderate `Tension_euk(m)` values across lineages, rather than requiring lineage specific modules for each case.

*Setup*

* Input data external to TU:

  * genomic and structural summaries for lineages with:

    * mitochondria only,
    * plastids primary endosymbiosis,
    * secondary or tertiary plastids.

* Choose once, as part of `W*`:

  * a single library of modules `Lib_G_host`, `Lib_G_sym`, `Lib_C_comp`, `Lib_R_cpl`,
  * a fixed family `{Gamma_r}` in `E_euk_maps`,
  * a fixed evaluation subset `R_eval_sym` of `R_eval` relevant to organelle integration,
  * tension bands in `L_ref_euk`, including at least one moderate band for acceptable integration.

* All of these are fixed before computing any tension values.

*Protocol*

1. For each lineage, use `D*` to construct an effective state `m_lineage` in `M_euk_reg` by encoding:

   * an approximate host module configuration,
   * relevant symbiont modules, for example proto mitochondrion or proto plastid,
   * a compartment architecture descriptor,
   * environment and phenotype summaries.

2. For each `m_lineage` and each `r` in `R_eval_sym`, evaluate observables:

   * `Host_symbiont_conflict(m_lineage; r)`,
   * `Integration_modularity(m_lineage; r)`,
   * `DeltaS_euk(m_lineage; r)`.

3. Compute the global tension:

   ```txt
   Tension_euk(m_lineage) =
     max over r in R_eval_sym of DeltaS_euk(m_lineage; r)
   ```

4. Compare tension values across:

   * mitochondria only lineages,
   * primary plastid lineages,
   * secondary and tertiary plastid lineages.

*Metrics*

* Distribution of `Tension_euk(m_lineage)` for each class of lineages.
* Number of additional lineage specific modules required to keep tension within a chosen moderate band in `L_ref_euk`.
* Robustness of tension values under minor, pre declared regroupings of modules in the libraries.

*Falsification conditions*

*Condition A: lineage explosion*
If, in order to keep `Tension_euk(m_lineage)` inside a moderate band for all lineages, one must introduce many lineage specific modules that violate the original finite library design in `W*`, then:

* the encoding instance `E*_euk` is considered to have failed to capture reusable integration patterns and is rejected at the effective layer.

*Condition B: misaligned tension*
If obviously more complex endosymbiotic events, such as secondary plastids, do not show higher or at least comparable `Tension_euk` values than simpler cases like mitochondria only, without any clear structural explanation from the observables, then:

* the encoding instance is considered misaligned with its intended interpretation and is rejected.

As in Experiment 1, falsification applies to the encoding instance, not to the canonical biological problem.

*Semantics implementation note*
Discrete modules and lineage labels are treated as finite set elements. Continuous summaries such as sizes and rates are treated as real valued fields. This is consistent with the hybrid semantics declared in Block 0.

*Boundary note*
Falsifying a TU encoding instance is not the same as showing that all mechanistic models of eukaryogenesis are impossible. Success or failure of this experiment bears on the adequacy of the Q079 encoding instance, not directly on which historical endosymbiotic sequence actually occurred.

---

## 7. AI and WFGY engineering spec

This block describes how Q079 can be used as an engineering module for AI systems within the WFGY framework, at the effective layer.

All training signals and architectural patterns below are constructed from effective observables and functionals in `F` and parameters in `W*`. They do not access or assume any TU bottom layer objects.

### 7.1 Training signals

We define several training signals for models that reason about early evolution, symbiosis and cellular complexity.

1. `signal_euk_energy_consistency`

   * Definition: a scalar penalty proportional to `I_energy(m)` for internal states associated with eukaryogenesis contexts.
   * Purpose: encourage the model to maintain a coherent relationship between energy supply and complexity load when it assumes eukaryote like cells exist.

2. `signal_host_symbiont_conflict`

   * Definition: a scalar penalty derived from `Host_symbiont_conflict(m; r)` aggregated over relevant resolutions in `R_eval`.
   * Purpose: penalize internal representations that imply persistent, unresolved conflicts between host and symbiont modules in scenarios that are intended to reflect successful eukaryogenesis.

3. `signal_integration_modularity`

   * Definition: a reward proportional to `Integration_modularity(m; r)` when the context involves stable eukaryotic cells or organelles.
   * Purpose: encourage the emergence of modular internal representations of organelles and compartment structures.

4. `signal_euk_tension`

   * Definition: a penalty equal to or proportional to `Tension_euk(m)` when the model is asked to produce a coherent account of eukaryote origins under a low tension assumption.
   * Purpose: make the model explicitly track and reduce consistency_tension in its explanations across levels.

These signals are meant to be used as additional training or regularization terms in models that already possess basic biological knowledge. They do not define or constrain any bottom layer physics.

### 7.2 Architectural patterns

We outline module patterns that reuse Q079 structures without revealing any deep TU generative rules.

1. `EukaryogenesisHead`

   * Role: an auxiliary head attached to the model that maps internal embeddings for early evolution scenarios to:

     * effective summaries of `G_host`, `G_sym`, `C_comp`,
     * estimates of `Euk_energy_profile` and `Complexity_load`,
     * an estimate of `Tension_euk(m)`.

   * Interface:

     * Inputs: internal embeddings for sequences where the model is reasoning about early cells, symbiosis or organelle origins.
     * Outputs: a vector of observables and a scalar tension estimate.

2. `EndosymbiosisConsistencyFilter`

   * Role: a filter that scores candidate narratives or intermediate reasoning steps about eukaryote origins based on:

     * implied host symbiont conflict,
     * implied integration modularity,
     * implied energy complexity alignment.

   * Interface:

     * Inputs: candidate text spans or structured intermediate hypotheses.
     * Outputs: a score or mask indicating how consistent each candidate is with low `Tension_euk` under the chosen encoding instance.

3. `SymbiosisTransferBridge`

   * Role: a module that reuses the Q079 encoding when the model reasons about:

     * later host microbe partnerships,
     * microbiomes,
     * synthetic endosymbiosis in engineered systems.

   * Interface:

     * Inputs: embeddings and high level tags indicating that the context involves host microbe integration.
     * Outputs: mapped observables and tension estimates that can be fed into modules defined for Q077 or related nodes.

These patterns live entirely at the effective layer. They only consume and produce observables and tension values defined in this page and do not depend on any hidden TU machinery.

### 7.3 Evaluation harness

We suggest an evaluation harness for AI models augmented with Q079 related modules.

1. Task families

   * Explanatory tasks:

     * explain competing hypotheses for eukaryote origins, for example hydrogen hypothesis, syntrophy models, phagocytosis first models,
     * describe the role of mitochondria in enabling complex genomes.

   * Predictive tasks:

     * predict qualitative consequences of modifying host or symbiont energy metabolism,
     * predict which host symbiont combinations are more likely to produce stable eukaryote like cells.

2. Conditions

   * Baseline condition:

     * the model operates without explicit Q079 modules, only with general purpose reasoning.

   * TU encoded condition:

     * the model uses `EukaryogenesisHead` and `EndosymbiosisConsistencyFilter` during inference,
     * and may use `signal_euk_energy_consistency`, `signal_host_symbiont_conflict`, `signal_integration_modularity` and `signal_euk_tension` during fine tuning.

3. Metrics

   * Accuracy on questions where the scientific community has relatively clear consensus.

   * Internal consistency:

     * frequency of contradictions between answers given under low tension prompts and answers given under intentionally high tension prompts.

   * Structural coherence:

     * degree to which the model chain of thought, where accessible, respects:

       * energy constraints,
       * conflict resolution mechanisms,
       * modular compartment structure.

### 7.4 Sixty second reproduction protocol

A minimal protocol to let external users experience the impact of Q079 style encoding in an AI system.

*Baseline setup*

* Prompt example:

  * Explain how eukaryotic cells originated from prokaryotes. Include the role of endosymbiosis and mitochondria, but do not use any special framework.

* Observation:

  * record whether the explanation is fragmented,
  * record whether it mixes incompatible hypotheses,
  * and record whether it mentions energy constraints in a coherent way.

*TU encoded setup*

* Prompt example:

  * Explain how eukaryotic cells originated from prokaryotes. Structure your answer around host symbiont integration, compartmentalization into organelles, and the consistency between energy supply and genome complexity. Use this structure to talk about endosymbiosis and mitochondria.

* Observation:

  * record whether the explanation organizes itself along the three axes above,
  * check whether it uses a clear conflict and resolution structure for host symbiont interactions,
  * check whether energy and complexity constraints appear explicitly.

*Comparison metric*

* Use a simple rubric to rate:

  * clarity of the integration pattern,
  * explicit handling of tradeoffs and constraints,
  * alignment with known arguments about bioenergetics and complexity.

* Optionally, have readers with domain knowledge judge which explanation captures the structure of current scientific thinking more faithfully.

*What to log*

* The exact prompts and full responses for both setups.
* Any auxiliary observables and tension scores produced by Q079 modules in the TU encoded setup.
* This allows later inspection and comparison without exposing any TU bottom layer generative rule.

---

## 8. Cross problem transfer template

This block describes the reusable components produced by Q079 and how they transfer to other problems, at the effective layer.

### 8.1 Reusable components produced by this problem

1. ComponentName: `EukCompartment_field`

   * Type: `field`

   * Minimal interface:

     * Inputs:

       * `G_host_descriptor`
       * `G_sym_descriptor`
       * `R_coupling_descriptor`
       * `E_env_descriptor`

     * Outputs:

       * `C_comp_descriptor`
       * `DeltaS_euk_comp` a component of `DeltaS_euk` focused on compartment structure

   * Preconditions:

     * Host and symbiont descriptors must be consistent with a shared genetic code and basic compatibility of membranes and exchange processes.
     * Environment descriptor must fall within the range where endosymbiosis is biophysically plausible.

2. ComponentName: `Endosymbiosis_tension_functional`

   * Type: `functional`

   * Minimal interface:

     * Inputs:

       * `Euk_energy_profile`
       * `Complexity_load`
       * `Host_symbiont_conflict`
       * `Integration_modularity`

     * Outputs:

       * `Tension_euk` scalar

   * Preconditions:

     * Observables must be well defined and finite at the chosen evaluation resolutions.
     * A fixed reference class `Ref_euk` and weight vector `(w_energy, w_complexity, w_conflict, w_modularity)` must be specified in advance as part of `W*`.

3. ComponentName: `Host_symbiont_partnership_profile`

   * Type: `observable`

   * Minimal interface:

     * Inputs:

       * `G_host_descriptor`
       * `G_sym_descriptor`
       * `R_coupling_descriptor`
       * `E_env_descriptor`
       * optionally `P_euk_descriptor`

     * Outputs:

       * `stability_index` nonnegative scalar
       * `conflict_index` nonnegative scalar

   * Preconditions:

     * Encoded host and symbiont must have clearly defined replication and expression systems.
     * Environment descriptor must include at least a coarse description of resource availability.

These components are defined purely at the effective layer and may be used in other problems that share similar structures.

### 8.2 Direct reuse targets

1. Q080 (BH_BIO_BIOSPHERE_LIMITS_L3_080)

   * Reused components:

     * `EukCompartment_field`
     * `Endosymbiosis_tension_functional`

   * Why it transfers:

     * Biosphere level limits on complexity and diversity depend on how cells partition energy and structure complexity. The same field and tension functional can be reused to aggregate cell level constraints to ecosystem level.

   * What changes:

     * Inputs are aggregated over many cells and species, and the outputs feed into biosphere level observables such as total productivity and maximum achievable complexity.

2. Q077 (BH_BIO_MICROBIOME_L3_077)

   * Reused component:

     * `Host_symbiont_partnership_profile`

   * Why it transfers:

     * Large host microbiome systems can be viewed as extended host symbiont partnerships with many participants. Stability and conflict indices generalize naturally from two partner systems to multi partner consortia.

   * What changes:

     * Descriptors include multiple symbiont communities rather than a single symbiont type, and the environment descriptor is expanded to include host internal environments.

3. Q123 (BH_AI_INTERP_L3_123)

   * Reused components:

     * `Endosymbiosis_tension_functional` as a template
     * `Host_symbiont_partnership_profile` as a metaphorical mapping

   * Why it transfers:

     * Complex AI architectures can be interpreted as integrations of heterogeneous submodules under capacity and conflict constraints. The same functional form can be used to define tension between modules in an AI system.

   * What changes:

     * Inputs become descriptors of AI submodules, their couplings and resource budgets instead of biological genomes and energy fluxes. Outputs are interpreted as architectural tension rather than biological tension.

---

## 9. TU roadmap and verification levels

This block explains how Q079 is positioned along the TU verification ladder and what the next measurable steps are, at the effective layer.

### 9.1 Current levels

* E_level: E1

  * A coherent effective encoding of eukaryote origins has been specified in terms of:

    * a state space `M_euk`,
    * observables and invariants,
    * a global tension functional and band library,
    * a singular set and regular domain,
    * and explicit fairness rules for encoding instances.

  * At least two concrete experiment patterns with falsification conditions have been provided for testing specific encoding instances.

* N_level: N2

  * A narrative exists linking:

    * host and symbiont modules,
    * energy and complexity constraints,
    * conflict resolution and compartment formation,
    * and their expression as low tension versus high tension worlds.

  * Counterfactual worlds have been described in a way that can be instantiated in artificial or model scenarios.

### 9.2 Next measurable step toward E2

To move from E1 to E2, at least one of the following should be implemented in practice, for a concrete encoding instance `E*_euk`.

1. An open implementation of the Q079 encoding instance that, given comparative datasets on prokaryotes and eukaryotes, computes:

   * `Euk_energy_profile`,
   * `Complexity_load`,
   * `I_energy`,
   * `I_integration` and `Tension_euk`,

   and publishes both the code and the resulting tension profiles together with all components of `W*`.

2. A controlled study of mock model worlds for eukaryogenesis in which:

   * different mechanistic hypotheses are instantiated as synthetic data generating processes,
   * the same encoding instance `E*_euk` is applied to all worlds,
   * and the resulting tension profiles are analyzed to see which hypotheses naturally fall into low tension bands in `L_ref_euk`.

Both steps operate entirely at the effective layer, using observables and summaries. They do not require exposing any TU bottom layer generative rule.

### 9.3 Long term role in the TU program

In the longer term, Q079 is expected to serve as:

* the reference node for problems involving transitions from simple to complex cells,
* a template for hybrid encodings that mix discrete and continuous observables under a single tension framework,
* a bridge between:

  * evolutionary biology,
  * biosphere level ecology,
  * and systems style interpretations of AI architectures,

  all expressed in a shared language of consistency_tension across levels.

---

## 10. Elementary but precise explanation

This block gives an explanation suitable for non specialists, while remaining aligned with the effective layer description.

The basic biological question is:

> How did complex cells like ours, with nuclei and mitochondria, come from much simpler cells like bacteria and archaea?

The standard picture is that:

* there was a host cell, probably related to modern archaea,
* there was a bacterial partner that moved inside the host and became a permanent guest,
* over time, the guest turned into an organelle, the mitochondrion, and many genes moved from the guest to the host genome,
* the new cell type gained much more energy per gene, which made large complex genomes and complex structures possible.

In the Tension Universe view, we do not try to replay history step by step. Instead, we ask a more structural question.

* Is there a simple, reusable way to describe how host and guest fit together?
* Does this description stay consistent when we look at real data from many organisms?

To do this, we imagine a space of states. Each state summarizes:

* what the host genome and metabolism look like,
* what the symbiont genome and metabolism look like,
* how they interact,
* what compartments and organelles exist,
* what the environment provides,
* and what kind of eukaryotic cell is produced.

For each state, we measure at least three things.

1. How much energy the cell has, and how complex its genome and regulation are.

2. How much unresolved conflict remains between host and symbiont.

3. How clearly the cell is organized into modules like organelles, rather than a jumble of parts.

We then compare these measurements with a small set of reference patterns that represent well behaved eukaryote like cells. The more a state deviates from the references, the higher its eukaryogenesis tension.

Two extreme possibilities can be contrasted.

In a low tension world:

* there is a fairly simple pattern that describes how host and symbiont are compatible,
* similar rules apply in different lineages and different endosymbiotic events,
* the relationship between available energy and complexity is stable,
* and most real eukaryotes fit this pattern with only small deviations.

In a high tension world:

* each eukaryotic lineage would need its own special explanation,
* there would be no stable rule that ties energy and complexity together,
* conflicts between host and symbiont would be patched on a case by case basis,
* trying to reuse one compact description across lineages would always lead to large mismatches.

Q079, in this framework, is not a specific historical story. It is a way to ask and test a sharper question.

* Does the origin of eukaryotes behave like a reusable integration pattern with low tension?
* Or does it look more like a collection of one off accidents with high tension?

The answer depends on data and models, not on TU alone. What TU provides is a disciplined way to:

* define the relevant observables,
* construct tension measures that are fair and testable,
* design experiments that can falsify bad encoding instances,
* and reuse the resulting components in other biological and artificial systems.

---

## Tension Universe effective-layer footer

This page is part of the WFGY / Tension Universe S problem collection. It should be read as an effective layer encoding of Q079, not as a solution to the canonical biological problem.

### Scope of claims

* The goal of this document is to specify an effective layer encoding of the origin of eukaryotes as a consistency_tension problem inside TU.
* It does not claim to prove or disprove any canonical statement about the historical origin of eukaryotic cells.
* It does not introduce any new theorem about biology beyond what is already established in the cited literature.
* It should not be cited as evidence that the corresponding open problem has been solved.

### Effective-layer boundary

* All objects used here, such as state spaces `M_euk`, observables, invariants, tension scores and counterfactual worlds, live at the effective layer.
* No TU bottom layer axiom system, field equation or generative rule is specified or assumed to be unique.
* No explicit mapping from raw data to bottom layer TU fields is provided or required for the statements made here.
* Any implementation or experiment must respect this boundary and work only with effective observables and summaries.

### Encodings and fairness

* The encoding class `E_euk = (D, F, W, L)` is defined with explicit fairness constraints.
* A concrete encoding instance `E*_euk = (D*, F*, W*, L*)` must be fixed in advance before any evaluation or experiment.
* Libraries, evaluation sets, reference objects, weight vectors, thresholds and band libraries in `W*` must not be tuned after seeing tension results.
* Claims about low tension or high tension regimes are meaningful only relative to a fixed encoding instance and fixed bands in `L_ref_euk`.
* Falsifying an encoding instance means that its design is rejected as a description of Q079 at the effective layer. It does not, by itself, falsify any biological theory or solve the canonical problem.

This page should be read together with the following charters:

* [TU Effective Layer Charter](../Charters/TU_EFFECTIVE_LAYER_CHARTER.md)
* [TU Encoding and Fairness Charter](../Charters/TU_ENCODING_AND_FAIRNESS_CHARTER.md)
* [TU Tension Scale Charter](../Charters/TU_TENSION_SCALE_CHARTER.md)
* [TU Global Guardrails](../Charters/TU_GLOBAL_GUARDRAILS.md)
