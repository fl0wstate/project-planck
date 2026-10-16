# Author review: twistane_final

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/twistane_final/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Compounds **A** and **B** are diastereomeric dimethyl derivatives of twistane (tricyclo[4.4.0.0³,⁸]decane), molecular formula $\text{C}_{12}\text{H}_{20}$. They are epimers: they differ only in the configuration of one methyl-bearing carbon. Their exact structures are given by these isomeric SMILES:

A: `C[C@@H]1C[C@H]2C[C@H]3[C@@H]1C[C@@H]2C[C@@H]3C`

B: `C[C@@H]1C[C@H]2C[C@H]3[C@@H]1C[C@@H]2C[C@H]3C`

Both are conformationally rigid, saturated cage hydrocarbons. The $^{13}\text{C}$ NMR spectra of pure A and pure B are recorded separately in an achiral solvent. Assume no accidental (coincidental) signal overlap: the number of observed $^{13}\text{C}$ signals equals the number of symmetry-distinct carbon environments. Let $N_A$ and $N_B$ be the numbers of distinct $^{13}\text{C}$ signals of A and B, respectively.

Compute $N_A - N_B$. Give the answer as a single integer.

````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$6$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Establish the constitution.** Both SMILES encode the same skeleton: the twistane cage (tricyclo[4.4.0.0³,⁸]decane, ten carbons: four methine CH and six methylene CH₂ in the parent) bearing two methyl groups on a pair of methylene carbons. Writing the SMILES heavy atoms in order as $c_0$ (methyl), $c_1 \ldots c_{10}$ (ring), $c_{11}$ (methyl), the two methyl-bearing ring carbons are $c_1$ and $c_{10}$. A and B differ only in the tetrahedral parity written at $c_{10}$ (`[C@@H]` in A vs `[C@H]` in B): they are epimers at that carbon, as stated.

**Step 2 — Symmetry framework.** For a rigid molecule, carbons give the same ¹³C signal exactly when they are exchanged by a symmetry operation of the molecule: a proper rotation (homotopic) or, in an achiral environment, an improper operation (enantiotopic). Diastereotopic carbons are inequivalent.

**Step 3 — Parent point group.** Twistane's point group is $D_2$: the identity and three mutually perpendicular $C_2$ axes, and no improper elements — the parent cage is chiral. Under $D_2$ (order 4) the ten cage carbons fall into three orbits: the four methines (orbit of 4), four methylenes (orbit of 4), and two methylenes lying on one $C_2$ axis-pair arrangement (orbit of 2) — consistent with the three observed ¹³C lines of the parent in ratio 4:4:2.

**Step 4 — Effect of the two methyls.** The two methylated carbons ($c_1$, $c_{10}$) belong to the methylene orbit of four. Within $D_2$, exactly one of the three $C_2$ operations exchanges $c_1$ with $c_{10}$; the other two map this pair onto the two *unsubstituted* carbons of that orbit and are therefore destroyed by the substitution pattern in both A and B. Hence each diastereomer can retain at most that single $C_2$.

**Step 5 — Which epimer retains the $C_2$.** A proper rotation maps each stereocenter onto a stereocenter of the *same* handedness. Carrying the exchange $c_1 \leftrightarrow c_{10}$ through the cage forces the full atom pairing
$$c_0 \leftrightarrow c_{11},\; c_1 \leftrightarrow c_{10},\; c_2 \leftrightarrow c_9,\; c_3 \leftrightarrow c_8,\; c_4 \leftrightarrow c_7,\; c_5 \leftrightarrow c_6 .$$
Checking tetrahedral parities under this mapping: for B, every stereocenter maps onto its partner with consistent handedness (the mapping is an automorphism of the stereo-labelled graph), so B possesses the $C_2$ axis and has point group $C_2$. For A, the parity at $c_{10}$ is inverted relative to the requirement (that is precisely the epimeric change), so the mapping fails and A has no symmetry beyond identity: point group $C_1$.

**Step 6 — Chirality check (no improper equivalences).** Both A and B are chiral (each is non-superimposable on its mirror image; the cage itself excludes internal mirror planes, and neither epimer's configuration set is self-mirror). Therefore no enantiotopic averaging applies, and signal counts equal orbit counts under proper rotations alone.

**Step 7 — Count orbits.**
- B ($C_2$): the twelve carbons pair up completely under the pairing of Step 5 — six two-carbon orbits → $N_B = 6$.
- A ($C_1$): only the identity remains; all twelve carbons are distinct → $N_A = 12$.

**Step 8 — Final synthesis.** $N_A - N_B = 12 - 6$.

**Final Answer:** $6$
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $6$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $N_A=12$ distinct carbon signals for A.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $N_B=6$ distinct carbon signals for B.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Whitlock, H. W., Jr. *J. Am. Chem. Soc.* **1962**, 84, 3412–3413. doi:10.1021/ja00876a041 — twistane synthesis, D₂ cage. *Required: False.*
2. Mislow, K.; Raban, M. *Top. Stereochem.* **1967**, 1, 1–38 — homotopic/enantiotopic/diastereotopic classification. *Required: False.*
3. Clayden, Greeves, Warren, *Organic Chemistry*, 2nd ed., OUP — NMR equivalence and symmetry. https://global.oup.com/ukhe/product/organic-chemistry-9780199270293 *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_twistane_final.md](../../planck_task_twistane_final.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
