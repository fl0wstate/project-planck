# Author review: tetraradical_gap

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/tetraradical_gap/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A design study in the spirit of pentalene-coupled high-spin diradicals considers a tetraradical $\mathbf{T}$ with four carbon-centered $S=1/2$ radical sites labeled 1–4. Sites 1 and 2 form arm A (two radical centers on one antiaromatic coupler); sites 3 and 4 form the identical arm B; a bridge connects site 2 to site 3. Broken-symmetry (BS) DFT on two pair-model systems gives:

(i) isolated arm (a 1–2 pair): $E_{\mathrm{BS}}-E_{\mathrm{T}}=+7.20$ kcal/mol, with $\langle S^2\rangle_{\mathrm{BS}}=0.00$ and $\langle S^2\rangle_{\mathrm{T}}=2.00$ (strongly overlapping magnetic orbitals);

(ii) bridge contact (a 2–3 pair only): $E_{\mathrm{BS}}-E_{\mathrm{T}}=-2.40$ kcal/mol, with $\langle S^2\rangle_{\mathrm{BS}}=1.00$ and $\langle S^2\rangle_{\mathrm{T}}=2.00$ (essentially disjoint, localized magnetic orbitals).

Convert each BS result to that pair's singlet–triplet gap $\Delta E_{\mathrm{ST}}=E_{\mathrm{S}}-E_{\mathrm{T}}$ (positive means triplet ground state) using the standard approximate spin projection based on the computed $\langle S^2\rangle$ expectation values.

Describe $\mathbf{T}$ by an isotropic Heisenberg spin model containing only the pair interactions 1–2 and 3–4 (arm coupling) and 2–3 (bridge coupling), each coupling fixed so that the corresponding isolated pair would reproduce its projected $\Delta E_{\mathrm{ST}}$; no other pair couplings, no anisotropy, no zero-field splitting.

Treating the four coupled spins exactly (do not assume each arm acts as a rigid $S=1$ unit), compute the energy of the lowest total-spin $S=2$ (quintet) level of $\mathbf{T}$ above its ground level. Report the value in kcal/mol, rounded to two decimal places.
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
**Step 1 — Yamaguchi projection, arm pair.** The standard ⟨S²⟩-based projection is $\Delta E_{\mathrm{ST}} = 2(E_{\mathrm{BS}}-E_{\mathrm{T}})/(\langle S^2\rangle_{\mathrm{T}}-\langle S^2\rangle_{\mathrm{BS}})$. Arm: $2(+7.20)/(2.00-0.00) = +7.20$ kcal/mol — the strong-overlap limit ($\langle S^2\rangle_{\mathrm{BS}}=0$: the BS determinant is already the closed-shell singlet, projection factor 1). Triplet ground pair.

**Step 2 — Yamaguchi projection, bridge pair.** $2(-2.40)/(2.00-1.00) = -4.80$ kcal/mol — the disjoint limit ($\langle S^2\rangle_{\mathrm{BS}}=1$: the BS determinant is a 50/50 singlet-triplet mixture, full factor-2 correction). Singlet ground pair. The two pairs sit in opposite projection regimes; a uniform factor corrupts one of them.

**Step 3 — Map to Heisenberg couplings.** With $\hat H=\sum_{\langle ij\rangle} J_{ij}\,\hat{\vec S}_i\cdot\hat{\vec S}_j$, an isolated spin-½ pair satisfies $E_S - E_T = -J$. Hence $J_a = -7.20$ kcal/mol (ferromagnetic, bonds 1–2 and 3–4) and $J_b = +4.80$ kcal/mol (antiferromagnetic, bond 2–3). (Any convention gives the same spectrum because the couplings are fixed through the observable pair gaps.)

**Step 4 — $S=2$ sector.** In the recoupled basis $|S_{12},S_{34};S\rangle$ the unique quintet is $|1,1;2\rangle$: $E_Q = \tfrac{J_a}{2}+\tfrac{J_a}{2}\cdot 0 \; \Rightarrow \; E_Q = J_a/2 + J_b/4 = -3.60 + 1.20 = -2.40$ kcal/mol (using $\vec S_1\cdot\vec S_2 = \tfrac14$ in each triplet arm and $\langle \vec S_2\cdot\vec S_3\rangle = \tfrac14$ in the stretched state).

**Step 5 — $S=0$ sector (2×2).** Basis $|1,1;0\rangle$, $|0,0;0\rangle$. Diagonal elements: $J_a/2 - J_b/2 = -6.00$ and $-3J_a/2 = +10.80$. Off-diagonal: $(\sqrt3/4)J_b = 1.2\sqrt3$ (so $v^2 = 4.32$). Eigenvalues $2.40 \pm \sqrt{8.40^2 + 4.32} = 2.40 \pm \sqrt{74.88}$; ground singlet $E_0 = 2.40 - \tfrac{12}{5}\sqrt{13} = -6.2533$ kcal/mol.

**Step 6 — $S=1$ check.** The three triplet levels lie at $-5.5267, +3.1267, +4.80$ kcal/mol; all above $E_0$. Ground state is the singlet — the AFM bridge wins over rigid ferromagnetic arms precisely because the $|0,0;0\rangle$ admixture depresses only the singlet.

**Step 7 — Gap.** $E_Q - E_0 = -2.40 - (2.40 - \sqrt{74.88}) = \sqrt{74.88} - 4.80 = 2.4(\sqrt{13}-2) = 3.8533$ kcal/mol.

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
Obtains bridge coupling $J_b=+4.80\,\mathrm{kcal\,mol^{-1}}$ under $\hat H=\sum J_{ij}\hat{\mathbf S}_i\cdot\hat{\mathbf S}_j$, or the equivalent physical coupling under another explicitly stated convention.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains quintet energy $E_Q=-2.40\,\mathrm{kcal\,mol^{-1}}$ with the solution's energy zero.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Yamaguchi, K. et al. *Chem. Phys. Lett.* **1988**, 149, 537–542. doi:10.1016/0009-2614(88)80378-6 — ⟨S²⟩-based spin projection. *Required: True.*
2. Noodleman, L. *J. Chem. Phys.* **1981**, 74, 5737–5743. doi:10.1063/1.440939 — broken-symmetry method. *Required: False.*
3. Santiago et al. *Chem. Sci.* **2025**, 16, 430–447. doi:10.1039/d4sc05225k (online 21 Nov 2024) — S_ab≈1 projection choice for strongly overlapping diradicals (inspiration). *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_tetraradical_gap.md](../../planck_task_tetraradical_gap.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
