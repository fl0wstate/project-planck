# Author review: porphyrin_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/porphyrin_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Five nickel(II) porphyrins are described below. In each, the nickel is four-coordinate and carries no axial ligand, and the macrocycle is to be taken as planar with the framework geometry of unsubstituted porphine, with the four meso positions numbered 5, 10, 15 and 20 in order around the ring, so that 5 lies opposite 15 and 10 lies opposite 20.

Every meso aryl group named below is ortho-monosubstituted and lies perpendicular to the mean plane of the macrocycle, so that its ortho substituent points towards one face of the macrocycle or towards the other. Take the barrier to rotation about each bond joining a meso carbon to an aryl group to be $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$, and rotation about every other single bond to be fast at $25\,^\circ\mathrm{C}$. A meso position bearing hydrogen offers no such choice.

$\mathrm{Ar1} = $ 2-methylphenyl, $\mathrm{Ar2} = $ 2-methoxyphenyl, $\mathrm{Ar3} = $ 2-chlorophenyl, $\mathrm{Ar4} = $ 2-bromophenyl.

Q1: $\mathrm{Ar1}$ at 5 and 15; $\mathrm{Ar2}$ at 10 and 20.

Q2: $\mathrm{Ar1}$ at 5 and 10; $\mathrm{Ar2}$ at 15 and 20.

Q3: $\mathrm{Ar1}$ at 5 and 15; hydrogen at 10 and 20.

Q4: $\mathrm{Ar1}$ at 5, $\mathrm{Ar2}$ at 10, $\mathrm{Ar3}$ at 15, $\mathrm{Ar4}$ at 20.

Q5: $\mathrm{Ar1}$ at 5, 10 and 15; $\mathrm{Ar2}$ at 20.

For each porphyrin, count the stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Disregard tautomers and any process that makes or breaks a covalent bond. Report the sum of the five counts as a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$41$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1.** Count a structure as a separate stereoisomer only if it is isolable at $25\,^\circ\mathrm{C}$ over a period of hours, and count enantiomers as distinct.

**Step 2.** The stated barrier for rotation about each meso-carbon–aryl bond is $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$, which at $25\,^\circ\mathrm{C}$ gives a half-life of decades, so every aryl orientation is frozen on that timescale.

**Step 3.** Each ortho-substituted aryl group therefore contributes one binary variable: its ortho substituent points towards one face of the macrocycle or towards the other.

**Step 4.** A meso position bearing hydrogen contributes no variable.

**Step 5.** Write the state of a molecule as the list of face labels at positions 5, 10, 15, 20.

**Step 6.** Two states are the same stereoisomer exactly when some symmetry operation of the framework that preserves the pattern of aryl identities carries one state into the other.

**Step 7.** Restrict that set to *proper rotations* only: improper operations relate a molecule to its mirror image, and enantiomers are counted as distinct here.

**Step 8.** The idealised planar porphine framework has proper rotation group $D_4$, of order 8 — $E$, $C_4$, $C_4^2$, $C_4^3$ about the axis normal to the mean plane; two $C_2$ axes in the plane through opposite meso carbons; two $C_2$ axes in the plane through opposite pyrrole units.

**Step 9.** The $C_4^k$ rotations permute the meso positions cyclically and leave every face label unchanged, since the normal axis maps each face to itself.

**Step 10.** Each in-plane $C_2$ turns the macrocycle over, so it permutes the meso positions *and* inverts every face label.

**Step 11.** The nickel is four-coordinate with no axial ligand, so the two faces are genuinely equivalent and the operations of Step 10 are true symmetries of the molecule.

**Step 12.** Label the meso positions $p_1, p_2, p_3, p_4$ for 5, 10, 15, 20, and record each operation as a permutation plus a face-inversion flag:

| operation | permutation | inverts faces |
|---|---|---|
| $E$ | — | no |
| $C_4$, $C_4^3$ | 4-cycle | no |
| $C_4^2$ | $(p_1p_3)(p_2p_4)$ | no |
| $C_2(\mathrm{A})$, through 5–15 | fixes $p_1,p_3$; swaps $p_2,p_4$ | yes |
| $C_2(\mathrm{B})$, through 10–20 | fixes $p_2,p_4$; swaps $p_1,p_3$ | yes |
| $C_2(\mathrm{C})$, through pyrroles bisecting 5–10 and 15–20 | $(p_1p_2)(p_3p_4)$ | yes |
| $C_2(\mathrm{D})$, through pyrroles bisecting 10–15 and 20–5 | $(p_2p_3)(p_1p_4)$ | yes |

**Step 13.** For each case, keep only the operations preserving the aryl identity pattern, then count orbits of the state set by Burnside's lemma: orbits $= \frac{1}{|G|}\sum_{g \in G}(\text{states fixed by } g)$.

---

**Step 14.** Q1 has Ar1 at $p_1,p_3$ and Ar2 at $p_2,p_4$; the operations preserving this pattern are $E$, $C_4^2$, $C_2(\mathrm{A})$ and $C_2(\mathrm{B})$, so $|G| = 4$.

**Step 15.** Q1 has $2^4 = 16$ states, and $E$ fixes all 16.

**Step 16.** $C_4^2$ fixes the states with $b_1 = b_3$ and $b_2 = b_4$: 4 states.

**Step 17.** $C_2(\mathrm{A})$ leaves $p_1$ and $p_3$ in place while inverting their labels, requiring $b = \neg b$, so it fixes 0; $C_2(\mathrm{B})$ fixes 0 for the same reason at $p_2, p_4$.

**Step 18.** Q1 count $= (16 + 4 + 0 + 0)/4 = \mathbf{5}$.

**Step 19.** Q2 has Ar1 at $p_1,p_2$ and Ar2 at $p_3,p_4$; the only nontrivial operation preserving this is $C_2(\mathrm{C})$, which swaps $p_1 \leftrightarrow p_2$ and $p_3 \leftrightarrow p_4$ within each identical pair, so $|G| = 2$.

**Step 20.** $E$ fixes all 16 states.

**Step 21.** $C_2(\mathrm{C})$ fixes the states with $b_1 = \neg b_2$ and $b_3 = \neg b_4$: $2 \times 2 = 4$ states.

**Step 22.** Q2 count $= (16 + 4)/2 = \mathbf{10}$.

**Step 23.** Q3 has Ar1 at $p_1,p_3$ and hydrogen at $p_2,p_4$, so only two labels vary and there are $2^2 = 4$ states; the preserving operations are $E$, $C_4^2$, $C_2(\mathrm{A})$, $C_2(\mathrm{B})$, so $|G| = 4$.

**Step 24.** $E$ fixes 4, and $C_4^2$ swaps $p_1 \leftrightarrow p_3$ without inversion, fixing the states with $b_1 = b_3$: 2.

**Step 25.** $C_2(\mathrm{A})$ holds $p_1$ and $p_3$ in place while inverting, fixing 0; $C_2(\mathrm{B})$ swaps $p_1 \leftrightarrow p_3$ *and* inverts, fixing the states with $b_1 = \neg b_3$: 2.

**Step 26.** Q3 count $= (4 + 2 + 0 + 2)/4 = \mathbf{2}$.

**Step 27.** Q4 has four different aryl groups, so no nontrivial rotation preserves the pattern and $|G| = 1$.

**Step 28.** Q4 count $= 2^4/1 = \mathbf{16}$.

**Step 29.** Q5 has Ar1 at $p_1,p_2,p_3$ and Ar2 at $p_4$; any preserving operation must hold $p_4$ fixed, leaving only $E$ and $C_2(\mathrm{B})$, so $|G| = 2$.

**Step 30.** $E$ fixes 16, and $C_2(\mathrm{B})$ holds $p_2$ and $p_4$ in place while inverting their labels, which is impossible, so it fixes 0.

**Step 31.** Q5 count $= (16 + 0)/2 = \mathbf{8}$.

**Step 32.** Sum the five counts: $5 + 10 + 2 + 16 + 8$.

**Final Answer: 41**

---
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $41$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $10$ stereoisomers for Q2 using its face-inverting pyrrole-axis rotation.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $8$ stereoisomers for Q5 using its face-inverting meso-axis rotation.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** Cribbin, L.; Twamley, B.; Buga, N.; O'Brien, J. E.; Buehler, R.; Fischer, R. A.; Senge, M. O. "C-C Coupling in sterically demanding porphyrin environments." *Beilstein J. Org. Chem.* **2024**, *20*, 2784-2798. doi:10.3762/bjoc.20.234. Published **04 Nov 2024**, CC BY 4.0. Nine months of cutoff margin.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_porphyrin_census.md](../../planck_task_porphyrin_census.md)
- [planck_task_porphyrin_census_golden.md](../../planck_task_porphyrin_census_golden.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
