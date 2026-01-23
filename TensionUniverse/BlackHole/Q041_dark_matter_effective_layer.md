# Q041 Nature of dark matter (TU effective entry)

## 0. Metadata and effective layer disclaimer

### 0.1 Metadata

- Problem ID: Q041  
- Title: Nature of dark matter  
- BH Code: BH_COSMO_DARKMATTER_L1_041  
- Domain: Cosmology  
- Family: Dark sector  
- Rank: S  
- Model semantics: continuous manifold semantics  
- Field type: matter and gravitational fields on a spacetime manifold  
- Tension type: spectral and geometric tension between mass distribution and observables  
- Projection dominance: P primary, I and C secondary, M auxiliary  

### 0.2 Model semantics declaration

- Spacetime is modeled as a four dimensional differentiable manifold S with metric g_mu_nu compatible with standard cosmology.  
- Spatial slices at fixed cosmological time are modeled as a three dimensional Riemannian manifold (Sigma, h_ij).  
- All continuous fields below are defined on Sigma or on S with appropriate restrictions.  
- Gradients, divergences, and Laplacians are understood in the Riemannian sense on (Sigma, h_ij).  
- Time derivatives d/dt are interpreted as finite differences Delta/Delta t unless explicitly stated as smooth limits.

### 0.3 Effective layer disclaimer

All statements in this entry are made strictly at the effective layer.

- Only observables, effective fields, constraints, tension indices, and extremality patterns are specified.  
- No underlying axiom system, no generative rules, and no constructive mapping from raw data into internal TU fields are given.  
- Whenever a mapping or a model is mentioned, it is stated in existence form, not constructed explicitly.  
- No unique microscopic mechanism for dark matter is claimed in this document.

This is a semantic tension description of the dark matter problem, not a constructive proof or a unique fundamental theory.

---

## 1. Canonical problem and status

### 1.1 Canonical formulation

Let g_mu_nu be a spacetime metric solving Einstein field equations with total energy momentum tensor T_tot_mu_nu. Let T_vis_mu_nu denote the contribution from observed baryonic matter and radiation, constructed from luminous and baryonic tracers.

Canonical dark matter problem:

Explain the persistent discrepancy between

- gravitational effects inferred from g_mu_nu through galaxy rotation curves, gravitational lensing, cluster dynamics, and large scale structure, and  
- the contribution that can be accounted for by T_vis_mu_nu,

by finding a physically well defined additional component or modification such that

$$
T_tot_mu_nu = T_vis_mu_nu + T_dm_mu_nu + T_mod_mu_nu
$$

with

- T_dm_mu_nu a non luminous component, and / or  
- T_mod_mu_nu an effective term encoding modified dynamics,

that simultaneously matches all robust dark matter phenomenology across relevant scales.

### 1.2 Current status

- Multiple independent observational channels support the existence of a missing component or of a modification of gravity at galactic, cluster, and cosmological scales.  
- Cold dark matter within LambdaCDM provides a successful global fit to many observables, but small scale tensions and alternative frameworks remain under active investigation.  
- No single microphysical model is universally accepted as the final answer for the nature of dark matter.

This entry does not attempt to resolve the microphysical nature. It encodes the effective tension structure of the problem.

### 1.3 Authoritative sources

Examples of authoritative sources include:

- Standard cosmology textbooks covering LambdaCDM and dark matter phenomenology.  
- Review articles on galaxy rotation curves, gravitational lensing, cluster dynamics, and large scale structure formation.  
- Precision cosmology reports based on CMB and large scale structure surveys.

Concrete bibliographic details can be added in a later revision. The effective layer construction below does not depend on a particular choice of review.

---

## 2. Position in the BlackHole graph

### 2.1 Local neighborhood

Within the BlackHole set of S problems, Q041 is located in the cosmology and dark sector cluster and is directly related to:

- Q042 Nature of dark energy  
- Q043 Origin of cosmic inflation  
- Q045 Large scale structure formation  
- Q046 Cosmic microwave background anomalies  
- Q048 Hubble constant tension  
- Q049 Missing baryons problem  

These problems share observables, data sets, or large scale dynamical structures with Q041.

### 2.2 Cross domain links

Q041 has structural connections to:

- problems where effective potentials and spectral gaps appear as emergent fields in the tension formalism,  
- information theoretic questions involving compressed descriptions of large scale cosmological data sets,  
- AI problems dealing with global consistency of field like internal representations.

Cross problem transfer is detailed in Section 8.

---

## 3. Tension Universe encoding at the effective layer

### 3.1 State space and fields

We introduce the following effective level objects.

- Physical spacetime manifold S with metric g_mu_nu.  
- Semantic state space M containing high level semantic states X that encode macroscopic configurations of matter, observers, and modeling assumptions.  
- On a spatial slice Sigma:

  - visible matter density field rho_vis(x), derived from luminous tracers,  
  - total dynamical mass density field rho_dyn(x), inferred from gravitational observables,  
  - an effective dark sector field rho_dm(x) or, more generally, a dark sector stress energy contribution T_dm_mu_nu(x).

- Observables O_k(x) that represent measurable quantities, including for example:

  - rotation velocity profiles v_rot(r),  
  - lensing convergence maps kappa_lens(theta),  
  - cluster velocity dispersions,  
  - large scale structure statistics.

We treat M as a semantic manifold equipped with a metric g_ij that supports both distance and energy geometry roles, consistent with the TU Core contract.

### 3.2 TU effective statement for Q041

At the effective layer, the dark matter problem is encoded as the existence and structure of a low tension configuration that links

- visible sector fields rho_vis and related observables, and  
- dark sector contributions T_dm_mu_nu or effective modifications,

such that all robust gravitational observables belong to a single TU consistent family.

TU effective statement:

Assume there exists a family of TU compatible models in which:

1. There is a mapping that associates to each semantic state X in M

   - a visible mass density field rho_vis(x; X),  
   - a total dynamical mass density field rho_dyn(x; X),  
   - a dark sector contribution T_dm_mu_nu(x; X) or effective modification T_mod_mu_nu(x; X), and  
   - a set of observables O_k(X),

   satisfying standard consistency conditions of cosmology.

2. There exists an effective tension functional T_dm_total on pairs (rho_vis, rho_dyn) such that observed configurations minimize T_dm_total within admissible uncertainty classes, when T_dm_mu_nu is appropriately included.

3. Any TU compatible encoding of dark matter must preserve specified invariants of the gravitational field and large scale structure across the data sets considered.

The explicit mapping from raw observational data into M and into the fields above is not constructed here. Only existence and consistency conditions at the effective level are stated.

### 3.3 Four projections P, I, M, C

#### 3.3.1 Physical projection P

- Focus: gravitational dynamics in galaxies, clusters, and the cosmic web.  
- Objects: g_mu_nu, rho_vis, rho_dyn, and T_dm_mu_nu.  
- Key observable tension: mismatch between the gravitational potential implied by rho_vis and the one reconstructed from rotation curves and lensing, integrated over relevant scales.

#### 3.3.2 Information projection I

- Focus: description length and information content of the universe under different modeling choices.  
- Objects: compressed encodings of large data sets such as CMB maps, galaxy surveys, and lensing catalogs.  
- Key observable tension: difference in information complexity between models with and without a unified dark matter description that fits all robust data.

#### 3.3.3 Mind projection M

- Focus: cognitive load for an idealized model building mind that maintains a globally consistent picture of cosmic structure.  
- Objects: semantic states X representing modeling schemes and parameterizations.  
- Key observable tension: cognitive and structural cost of tracking a patchwork of unrelated phenomenological fixes compared to a unified dark sector.

#### 3.3.4 Civilisational projection C

- Focus: long horizon bets made by a scientific civilisation that treats the dark sector as a real component in its physical ontology.  
- Objects: research programs, experimental infrastructure, and resource allocation patterns.  
- Key observable tension: stability of such programs under changing data as a function of how unified the dark matter description is.

### 3.4 Projection coherence note

In the TU encoding, these projections are different readings of the same underlying tension field.

- Projection P describes the gravitational mismatch in terms of field level quantities.  
- Projection I describes the compression structure of the same data sets.  
- Projection M describes the internal cost for a model building agent to track these structures.  
- Projection C describes the long term stability of scientific and technological commitments based on specific dark sector hypotheses.

TU compatible models for Q041 must maintain coherence across these projections. A proposal that removes tension in P but produces unbounded or highly irregular tension in I or M is treated as incomplete at the effective layer.

---

## 4. Tension principle for Q041

### 4.1 Tension indices and functionals

We introduce an effective scalar tension index on Sigma:

$$
DeltaS_grav(x) >= 0
$$

that measures local mismatch between gravitational observables and predictions from visible matter alone. At each spatial point x,

$$
DeltaS_grav(x) = f(rho_dyn(x) - rho_vis(x))
$$

for a suitable nonnegative function f, or more generally a combination of differences in derived quantities such as circular velocities or lensing convergence.

A global spectral geometric tension functional is defined by

$$
T_dm_total[rho_vis, rho_dyn]
= \int_Omega w(x) DeltaS_grav(x) dV(x)
$$

with a weight function w(x) that encodes observational reliability and scale selection, and with Omega a subset of Sigma defined in Section 6.

In the TU Core notation, this functional is compatible with a canonical stress tensor of the form

$$
T_ij = S_i C_j DeltaS lambda kappa
$$

where indices i, j range over appropriate directions in the semantic state space, and DeltaS is associated with DeltaS_grav at the effective level.

### 4.2 Extremality principle

The effective dark matter tension principle for Q041 is:

- admissible configurations of rho_vis, rho_dyn, and dark sector contributions are compared via T_dm_total, and  
- observed configurations are close to low tension extremal points of T_dm_total within declared uncertainty sets.

Configurations requiring many unrelated local fixes to match data correspond to high T_dm_total. Configurations where a single coherent dark sector contribution brings T_dm_total into a controlled band are preferred at the effective layer.

This is an extremality statement about tension, not a microphysical claim about the underlying dark sector.

---

## 5. Counterfactual tension worlds

### 5.1 World T: unified low tension dark sector

Assume there exists a family of TU compatible models U_T where:

- a single class of dark sector fields T_dm_mu_nu with a stable effective equation of state explains all robust dark matter phenomenology across scales, and  
- for each observed system, the corresponding configuration is a low tension extremal point of T_dm_total in the admissible set.

In this world:

- Projection P exhibits a consistent pattern of gravitational potentials derived from a unique dark sector law.  
- Projection I shows that data sets can be compressed using a relatively simple parameterization of the dark sector, with controlled residuals.  
- Projection M shows reduced cognitive tension for an idealized modeller, since a single scheme covers many systems.  
- Projection C supports stable long term research and engineering programs based on unified dark sector assumptions.

### 5.2 World F: no unified low tension dark sector

Assume there is no TU compatible model with a unified dark sector class that keeps T_dm_total in a controlled band across all robust data sets. Instead, explaining observations requires a patchwork of system dependent corrections.

In this world:

- Projection P exhibits system specific effective modifications that do not fit into a single dark sector field class.  
- Projection I shows that compression of the combined data requires many additional parameters and ad hoc structures.  
- Projection M shows high cognitive load for an idealized modeller that needs to maintain many local rules.  
- Projection C shows unstable scientific commitments, with frequent large revisions of dark sector assumptions as new data accumulate.

This counterfactual analysis does not decide which world is actual. It encodes how tension patterns would differ if the canonical unification view fails at the effective layer.

---

## 6. Falsifiability and discriminating experiments

### 6.1 Singularity and exceptional sets

Define S_sing as the subset of Sigma where gravitational observables are presently too uncertain or non regular for DeltaS_grav to be well defined. We adopt option (a) from the TU contract:

- work on Omega = Sigma \ S_sing, where observables and densities are sufficiently regular and bounded for the definitions above, and  
- explicitly track the dependence of results on the choice of Omega.

### 6.2 Discriminating test for the TU encoding

We require at least one discriminating test that targets the TU encoding of Q041, not the full microphysical resolution of dark matter.

Test DM_TU_1: scale coherent tension band.

1. Choose a set of systems {X_i} spanning galaxy, group, and cluster scales where both rho_vis and rho_dyn can be reconstructed to declared accuracy.  
2. For each system, compute an effective DeltaS_grav(x; X_i) on Omega_i.  
3. For a given TU encoding, predict a band [L_i, U_i] for the spatially averaged tension index

$$
DeltaS_bar_grav(X_i)
=
(1 / V(Omega_i)) \int_Omega_i DeltaS_grav(x; X_i) dV(x)
$$

as a function of a small parameter set shared by the family.  
4. If observed values of DeltaS_bar_grav(X_i) systematically fall outside the predicted bands across several scales, the TU encoding of Q041 is falsified at the effective layer, independent of whether dark matter is ultimately particle like or a modification of gravity.

This test is implementable in principle using continuous manifold semantics and standard gravitational reconstructions. It is a test of the tension structure and its claimed scale coherence, not of a specific particle model.

### 6.3 Relation to the underlying problem

Falsifying a particular TU encoding of Q041 means that the chosen tension functional T_dm_total and its extremality claims are incompatible with data. It does not solve the dark matter problem and does not rule out all possible dark sector theories. It only rules out that specific effective tension structure.

---

## 7. AI and WFGY engineering specification

### 7.1 Training signals

Q041 induces tension based training or regularization signals for AI systems.

- Define a model output field rho_dyn_hat(x) predicted from visible sector inputs and internal representations.  
- Construct a tension based loss

$$
L_dm = \int_Omega w(x) DeltaS_grav_model(x) dV(x)
$$

with

$$
DeltaS_grav_model(x)
=
f(rho_dyn_hat(x) - rho_dyn_obs(x))
$$

where rho_dyn_obs(x) is the reconstructed dynamical density.  
- Combine with standard data fitting losses to produce a WFGY compatible training objective that penalizes high tension configurations.

These signals are defined at the effective layer and do not require access to any TU Deep structure.

### 7.2 Architectural patterns

Q041 suggests that useful AI architectures for cosmology and related tasks include:

- field based memory representations that store rho_vis, inferred potentials, and associated uncertainties on grids or graphs,  
- modules that enforce or check global consistency of gravitational fields across multiple systems,  
- mechanisms that implement a form of low tension search in the space of dark sector parameterizations.

The precise design of these modules is an engineering choice. The TU encoding provides constraints and evaluation criteria rather than a fixed architecture.

### 7.3 Evaluation harness

A Q041 based evaluation harness for AI and WFGY systems can be constructed as follows.

- Input: catalogues of galaxies, clusters, and lensing systems with visible tracers and reconstructed dynamical mass profiles.  
- Task: given visible sector information, reconstruct dynamical profiles and predict tension indices DeltaS_grav and global T_dm_total.  
- Metrics:
  - accuracy of reconstructed dynamical fields,  
  - distribution of tension indices compared to observed values,  
  - stability of performance under synthetic perturbations of visible sector data.

This harness tests the ability of AI systems to internalize and manipulate field level structures in a tension aware manner.

---

## 8. Cross problem transfer template

### 8.1 Reusable components

From the Q041 encoding, we obtain reusable components:

- a gravitational tension index DeltaS_grav(x) based on mismatch between different ways to infer fields,  
- a global functional T_dm_total integrating local tension with weights,  
- a pattern where a unified low tension extremal configuration is contrasted with patchwork high tension configurations,  
- an evaluation harness template where field reconstructions are judged by their tension profile.

These components can be imported into other BlackHole problems that involve field mismatches or multiple observational channels.

### 8.2 Target problems for transfer

Direct transfer targets include:

- Q042 dark energy, where similar tension indices can be defined between expansion history and gravitational field reconstructions,  
- Q045 large scale structure, where tension indices compare clustering statistics under different modeling assumptions,  
- Q048 Hubble constant tension, where multiple measurements of a single parameter induce an effective tension functional in parameter space,  
- Q049 missing baryons, where tension indices compare baryon census predictions and observations.

The same pattern extends to non cosmological domains where fields and observables can be compared through tension indices.

---

## 9. TU roadmap and verification levels

### 9.1 TU penetration level

For Q041, the current document is assigned:

- TU penetration level E1:

  - state space and effective fields are defined,  
  - tension indices and functionals are specified at an abstract level,  
  - qualitative extremality principles are given.

The target progression is:

- E2:
  - concretize DeltaS_grav and T_dm_total for explicit data sets,  
  - produce numerical predictions for tension band distributions under candidate encodings.  
- E3:
  - implement PDE or agent based models that use these tension structures and demonstrate empirical advantages in reconstructing dark matter related fields compared to baseline methods.

### 9.2 Internal maturity level

For the present entry:

- internal maturity level N1:

  - conceptual mapping and structural definitions are present,  
  - no concrete data pipeline or public implementation is attached yet.

Future revisions may raise the level to N2 or higher as numerical experiments and implementations are added.

---

## 10. Elementary but precise explanation

This section is for a reader with basic scientific literacy.

- Observations of galaxies and clusters show that visible matter is not enough to explain the way things move and the way light bends. Something else or some change in the rules is needed.  
- In this document, the problem is rewritten using a language of tension. There is a quantity DeltaS_grav that measures how badly visible matter alone fails to match the gravitational effects we see.  
- A global tension index T_dm_total is defined by adding up these mismatches over space. Configurations that need many unrelated fixes to match data have high T_dm_total. Configurations where a single dark sector description brings T_dm_total down into a narrow band are low tension.  
- Two effective worlds are considered. In one world, a unified dark sector makes the tension index small and regular across many systems. In the other world, no such unified description exists, and the tension index is irregular and large.  
- The document proposes a concrete way to test whether a given tension based encoding is compatible with data. This test can in principle falsify the encoding even if the ultimate nature of dark matter remains unknown.  
- For AI and WFGY, this problem becomes a training and evaluation ground. Systems are asked to reconstruct gravitational fields and dark sector effects in a way that reduces the tension index while remaining consistent with observations.

This is an effective level description. It does not specify what dark matter is made of. It specifies how a consistent picture should behave when viewed through the lens of tension.
