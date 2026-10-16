# Author review: tetraradical_v2

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/tetraradical_v2/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A tetraradical $\mathbf{T}$ has four carbon-centered $S=1/2$ radical sites labeled 1–4: sites 1,2 form arm A; sites 3,4 form the identical arm B; a bridge connects site 2 to site 3; sites 1 and 4 lie on the far ends. $\mathbf{T}$ is conformationally rigid and held at one fixed nuclear geometry; at this geometry the local arm and bridge fragments coincide with the triplet-state geometries of the pair models below. The spin-Hamiltonian couplings must reproduce the pair gaps at this fixed geometry.

Broken-symmetry (BS) DFT pair-model results:
(i) arm pair 1–2, at the triplet geometry: $E_{\mathrm{BS}}-E_{\mathrm{T}}=+7.20$ kcal/mol, $\langle S^2\rangle_{\mathrm{BS}}=0.00$, $\langle S^2\rangle_{\mathrm{T}}=2.00$.
(ii) arm pair 1–2, second calculation in which each spin state's geometry was independently optimized: $E_{\mathrm{BS}}-E_{\mathrm{T}}=+5.60$ kcal/mol, same $\langle S^2\rangle$ values.
(iii) bridge pair 2–3, at the triplet geometry: $E_{\mathrm{BS}}-E_{\mathrm{T}}=-2.40$ kcal/mol, $\langle S^2\rangle_{\mathrm{BS}}=1.00$, $\langle S^2\rangle_{\mathrm{T}}=2.00$.
(iv) remote pair 1–4, at the triplet geometry: $E_{\mathrm{BS}}-E_{\mathrm{T}}=-0.15$ kcal/mol, $\langle S^2\rangle_{\mathrm{BS}}=1.00$, $\langle S^2\rangle_{\mathrm{T}}=2.00$.

The BS protocol's numerical convergence threshold is $0.20$ kcal/mol: any pair result with $|E_{\mathrm{BS}}-E_{\mathrm{T}}|<0.20$ kcal/mol is not distinguishable from zero, and the corresponding coupling must be set to exactly zero.

Convert each usable pair result to that pair's singlet–triplet gap $\Delta E_{\mathrm{ST}}=E_{\mathrm{S}}-E_{\mathrm{T}}$ (positive = triplet ground state) using the standard approximate spin projection based on the computed $\langle S^2\rangle$ values. Describe $\mathbf{T}$ by an isotropic Heisenberg model containing pair couplings 1–2, 3–4 (arms, equal by symmetry), 2–3 (bridge), and 1–4 (remote), each fixed by its pair result; couplings 1–3 and 2–4 are absent. No anisotropy, no zero-field splitting.

Treating the four coupled spins exactly (do not assume each arm is a rigid $S=1$ unit), compute the energy of the lowest total-spin $S=2$ (quintet) level of $\mathbf{T}$ above its ground level. Report the value in kcal/mol, rounded to two decimal places.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$3.85$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 2}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Select the usable data.** The couplings must reproduce pair gaps at $\mathbf{T}$'s single fixed geometry, which matches the pair models' triplet geometries. Result (ii) is an adiabatic gap (each state at its own relaxed geometry) and does not correspond to this fixed geometry: discard. Result (iv) has $|E_{\mathrm{BS}}-E_{\mathrm{T}}| = 0.15 < 0.20$ kcal/mol: by the stated convergence rule, $J_{14} = 0$ exactly. Usable: (i) and (iii).

**Step 2 — Projection, arm pair.** $\Delta E_{\mathrm{ST}} = 2(E_{\mathrm{BS}}-E_{\mathrm{T}})/(\langle S^2\rangle_{\mathrm{T}}-\langle S^2\rangle_{\mathrm{BS}}) = 2(+7.20)/2.00 = +7.20$ kcal/mol. With $\langle S^2\rangle_{\mathrm{BS}}=0$ the BS determinant is the pure singlet: projection factor 1. Triplet ground pair; by symmetry the 3–4 pair is identical.

**Step 3 — Projection, bridge pair.** $2(-2.40)/(2.00-1.00) = -4.80$ kcal/mol. $\langle S^2\rangle_{\mathrm{BS}}=1$: disjoint magnetic orbitals, full factor 2. Singlet ground pair.

**Step 4 — Heisenberg couplings.** With $\hat H=\sum J_{ij}\hat{\vec S}_i\cdot\hat{\vec S}_j$ and pair relation $E_S-E_T=-J$: $J_a = -7.20$ (bonds 1–2, 3–4), $J_b = +4.80$ (bond 2–3), $J_{14}=0$.

**Step 5 — Quintet energy.** In the fully stretched $S=2$ state every coupled pair is triplet-aligned, $\langle\vec S_i\cdot\vec S_j\rangle = 1/4$: $E_Q = 2\cdot\tfrac{J_a}{4} + \tfrac{J_b}{4} = -3.60+1.20 = -2.40$ kcal/mol.

**Step 6 — Singlet sector.** Recoupled basis $|S_{12},S_{34};S\rangle$: diagonal $\langle 1,1;0| = J_a/2 - J_b/2 = -6.00$, $\langle 0,0;0| = -3J_a/2 = +10.80$; off-diagonal $(\sqrt3/4)J_b = 1.2\sqrt3$. Eigenvalues $2.40 \pm \sqrt{70.56+4.32} = 2.40 \pm \sqrt{74.88}$. Ground singlet $E_0 = 2.40 - \tfrac{12}{5}\sqrt{13} = -6.2533$ kcal/mol.

**Step 7 — Triplet check.** Lowest $S=1$ level $-5.5267$ kcal/mol, above $E_0$: ground state is the singlet.

**Step 8 — Gap.** $E_Q - E_0 = -2.40 + 6.2533 = 2.4(\sqrt{13}-2) = 3.8533$.

**Final Answer:** $3.85$ kcal/mol
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $3.85$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Rejects result (ii) as an adiabatic gap unsuitable for the specified fixed-geometry couplings.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Sets $J_{14}=0$ because result (iv) is below the stated convergence threshold.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Yamaguchi, K. et al. *Chem. Phys. Lett.* **1988**, 149, 537–542. doi:10.1016/0009-2614(88)80378-6. *Required: True.*
2. Noodleman, L. *J. Chem. Phys.* **1981**, 74, 5737–5743. doi:10.1063/1.440939. *Required: False.*
3. Santiago et al. *Chem. Sci.* **2025**, 16, 430–447. doi:10.1039/d4sc05225k (online 21 Nov 2024). *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_tetraradical_v2.md](../../planck_task_tetraradical_v2.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
