# Author review: osmotic_polymersome

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/osmotic_polymersome/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
We assemble polysarcosine–poly(benzyl glutamate) polymersomes by solvent exchange and then deflate them by osmotic shock to drive the stomatocyte transformation. I'm trying to predict how far a batch should shrink before I book cryo-TEM time.

The vesicles come out of assembly as spheres of outer radius $260.0$ nm, suspended in the assembly buffer, which is $0.900$ mM NaCl in water. The same buffer fills the vesicle lumen, so the suspension starts perfectly isotonic. Treat NaCl as fully dissociated and treat every solute as ideal and obeying van 't Hoff behaviour.

To apply the shock I take $495.0\ \mu$L of that vesicle suspension and stir in $5.00\ \mu$L of a polysarcosine solution at $400.0$ mg/mL, made up in pure water. The polysarcosine is a laboratory batch from our own ring-opening polymerisation; light scattering puts its weight-average molar mass at $2.60$ kg/mol, and the GPC trace gives a dispersity of $1.30$. Polysarcosine is non-ionic.

After the addition the system is held at $70\ ^\circ$C and allowed to reach osmotic equilibrium. The vesicle membrane is permeable to water but completely impermeable to sodium ions, chloride ions, and polysarcosine, so the amount of NaCl trapped inside each vesicle is fixed. The vesicles are dilute enough that the water they expel does not measurably change the composition of the external medium, and the membrane is floppy enough to exert negligible tension, so equilibrium is reached when the total solute osmolarity is equal on the two sides of the membrane. The vesicles stay spherical throughout, and the membrane volume itself is negligible.

What is the outer radius of the vesicles at osmotic equilibrium? Give your answer in nanometres, rounded to the nearest whole nanometre.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$203$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 0}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Colligative averaging.** Osmotic pressure counts particles, so the relevant average is the *number*-average molar mass: $M_n = M_w/Đ = 2.60/1.30 = 2.00$ kg/mol.

**Step 2 — Temperature cancels.** Van 't Hoff gives $\Pi = icRT$; the same $RT$ appears on both sides, so equilibrium is equality of total osmolarity. The 70 °C is not needed.

**Step 3 — External NaCl after dilution.** Volumes additive: $495.0+5.00 = 500.0\ \mu$L. $0.900\ \text{mM} \times (495.0/500.0) = 0.891$ mM; fully dissociated ($i=2$) → $1.782$ mOsm/L.

**Step 4 — External polysarcosine.** Mass $= 5.00\ \mu\text{L} \times 400.0\ \text{mg/mL} = 2.00$ mg, in $500.0\ \mu$L → $4.00$ g/L. Non-ionic ($i=1$): $4.00/2000 = 2.00\times10^{-3}$ M → $2.000$ mOsm/L.

**Step 5 — Total external osmolarity.** $1.782 + 2.000 = 3.782$ mOsm/L (fixed; vesicles dilute).

**Step 6 — Interior.** Trapped NaCl fixed in amount, so osmolarity scales as $1/V$. Initial interior $= 0.900 \times 2 = 1.800$ mOsm/L.

**Step 7 — Balance.** $1.800\,(V_0/V_1) = 3.782 \Rightarrow V_1/V_0 = 0.47594$.

**Step 8 — Radius.** $R_1/R_0 = 0.47594^{1/3} = 0.78076$; $R_1 = 260.0 \times 0.78076 = 203.0$ nm.

**Final Answer: 203**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $203$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Uses number-average molar mass $M_n=2.00\,\mathrm{kg\,mol^{-1}}$ for the polymer's osmotic contribution.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains total external osmolarity $3.782\,\mathrm{mOsm\,L^{-1}}$.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Peters, R.; Charleston, L. A.; van Eck, K.; van Berlo, T.; Wilson, D. A. *Beilstein J. Org. Chem.* **2025**, *21*, 47–54. doi:10.3762/bjoc.21.5 (published 08 January 2025) — PSar osmotic shock, stomatocyte morphogenesis. *Required: False.*
2. van 't Hoff, J. H. *Z. Phys. Chem.* **1887**, *1*, 481–508 — osmotic pressure law. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_osmotic_polymersome.md](../../planck_task_osmotic_polymersome.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
