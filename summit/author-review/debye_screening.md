# Author review: debye_screening

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/debye_screening/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A short cationic peptide segment carries three protonated lysine side-chain charges that I model as three point charges of $+1e$ each, held in a fixed collinear arrangement with a uniform nearest-neighbour spacing of $0.70\ \mathrm{nm}$ (so the three pairwise separations are $0.70\ \mathrm{nm}$, $0.70\ \mathrm{nm}$, and $1.40\ \mathrm{nm}$). The segment sits in bulk water, treated as a uniform dielectric continuum with relative permittivity $78.4$ at the working temperature of $298.15\ \mathrm{K}$.

The electrostatic interaction between any two of these charges is screened by the surrounding electrolyte and is described by the Debye–Hückel screened Coulomb (Yukawa) potential, with the Debye screening length computed from the total ionic strength of the electrolyte in the usual way (ionic strength $I = \tfrac{1}{2}\sum_i c_i z_i^2$, summed over all mobile ionic species, molar concentrations).

The electrolyte is a mixed aqueous solution containing $50\ \mathrm{mM}$ NaCl and $15\ \mathrm{mM}$ MgCl$_2$. The peptide's own charges do not contribute to the ionic strength.

Constants: elementary charge $e = 1.602176634\times10^{-19}\ \mathrm{C}$; vacuum permittivity $\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$; Boltzmann constant $k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$; Avogadro constant $N_A = 6.02214076\times10^{23}\ \mathrm{mol^{-1}}$.

Compute the total electrostatic interaction energy of the three-charge assembly (the sum over all three unique pairs) under these conditions. Report the answer in kJ/mol, rounded to 2 decimal places.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$2.80$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 2}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Ionic strength.** Na⁺ 0.050 (z²=1), Cl⁻ 0.050+0.030=0.080 (z²=1), Mg²⁺ 0.015 (z²=4). $I = \tfrac12(0.050 + 0.080 + 0.015\cdot4) = \tfrac12(0.190) = 0.095\ \mathrm{M} = 95\ \mathrm{mol\,m^{-3}}$.

**Step 2 — Debye length.** $\kappa^2 = 2 N_A e^2 I/(\varepsilon_0 \varepsilon_r k_B T) = 1.0279\times10^{18}\ \mathrm{m^{-2}}$; $\kappa = 1.01384\times10^{9}\ \mathrm{m^{-1}}$; $\kappa^{-1} = 0.9863\ \mathrm{nm}$.

**Step 3 — Prefactor.** $e^2/(4\pi\varepsilon_0\varepsilon_r) = 2.94269\times10^{-30}\ \mathrm{J\,m}$ (Bjerrum length 0.715 nm).

**Step 4 — Pairwise (Yukawa $U=\frac{e^2}{4\pi\varepsilon_0\varepsilon_r}\frac{e^{-\kappa r}}{r}$).** r=0.70 nm: $\kappa r=0.7097$, $U=2.0674\times10^{-21}$ J (×2). r=1.40 nm: $\kappa r=1.4194$, $U=5.0838\times10^{-22}$ J.

**Step 5 — Total.** $2(2.0674\times10^{-21}) + 5.0838\times10^{-22} = 4.6433\times10^{-21}$ J $\times N_A = 2796.2$ J/mol.

**Final Answer:** $2.80$ kJ/mol.
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $2.80$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains ionic strength $I=0.095\,\mathrm{mol\,L^{-1}}$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains Debye length $\kappa^{-1}\approx0.9863\,\mathrm{nm}$.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Debye, P.; Hückel, E. *Physikalische Zeitschrift* **1923**, 24, 185–206 — screened potential, Debye length. *Required: False.*
2. Israelachvili, J. *Intermolecular and Surface Forces*, 3rd ed., Academic Press, 2011 — Yukawa/DLVO electrostatics, ionic strength. https://www.elsevier.com/books/intermolecular-and-surface-forces/israelachvili/978-0-12-375182-9 *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_debye_screening.md](../../planck_task_debye_screening.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
