# Author review: belt_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/belt_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A survey of 16 idealised monocyclic conjugated "belts" is carried out. In every belt each ring atom is trigonal ($sp^2$) with its p orbital normal to the local ribbon surface, and overlap is uniform all the way round the circuit (no bond-length localisation, no substituents, no ion pairing); the one exception is the saturated $sp^3$ CH$_2$ group in B16. Net charge is of $\pi$ origin throughout (electrons removed from, or added to, the conjugated circuit). Each entry lists, in order: the ring atoms as counts by type; the number of half-turns the ribbon makes before closing on itself ($0$, $1$ or $2$); the net charge; and the electronic state considered, either $S_0$ (closed-shell singlet ground state) or $T_1$ (lowest $\pi\pi^*$ triplet). Notation: N(=) = imine-type ring nitrogen (part of a ring C=N unit); N(H) = ring nitrogen bearing one H; B(H) = three-coordinate ring boron bearing one H; O = divalent ring oxygen; C(+) = H-free ring carbon of formal charge $+1$; C(-) = H-free ring carbon of formal charge $-1$.

B1: 20 CH | 0 | 0 | $S_0$
B2: 16 CH | 1 | 0 | $S_0$
B3: 18 CH | 2 | 0 | $S_0$
B4: 24 CH | 0 | 0 | $T_1$
B5: 18 CH | 0 | 0 | $S_0$
B6: 22 CH | 0 | 0 | $T_1$
B7: 20 CH | 0 | $+2$ | $S_0$
B8: 16 CH | 2 | $-2$ | $S_0$
B9: 22 CH | 1 | 0 | $S_0$
B10: 16 CH + 1 N(H) | 0 | 0 | $S_0$
B11: 16 CH + 2 N(=) | 0 | 0 | $S_0$
B12: 16 CH + 1 B(H) | 0 | 0 | $T_1$
B13: 14 CH + 1 C(-) | 1 | $-1$ | $S_0$
B14: 20 CH + 1 C(+) | 0 | $+1$ | $T_1$
B15: 14 CH + 1 O | 1 | 0 | $S_0$
B16: 18 CH + 1 $sp^3$ CH$_2$ | 0 | 0 | $S_0$

In how many of these 16 belts does the state specified sustain a net diatropic (diamagnetic) ring current around the complete macrocyclic circuit? Answer with a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$12$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
Four independent decisions per belt: (i) is the circuit continuous? (ii) how many pi electrons are in the circuit? (iii) does ribbon topology invert the count rule (odd number of half-turns = Moebius; even, including 2, = Hueckel)? (iv) does the electronic state invert it (Baird: in the lowest pi-pi* triplet, 4n is aromatic/diatropic and 4n+2 is antiaromatic/paratropic)? Unit contributions to the circuit: CH 1; imine-type N(=) 1 (lone pair in-plane); N(H) 2; divalent O 2; three-coordinate B(H) 0 (empty p, conjugation NOT broken); C(+) 0 (empty p, tropylium-type); C(-) 2 (p-type lone pair, cyclopentadienide-type); sp3 CH2 has no p orbital and severs the circuit.

Per belt (pi count n_pi; n_pi mod 4; topology; state; verdict):
B1 20; 0; flat; S0 -> 4n, Hueckel-antiaromatic -> paratropic. NO
B2 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B3 18; 2; two half-turns (even -> Hueckel topology); S0 -> diatropic. YES
B4 24; 0; flat; T1 -> Baird 4n triplet -> diatropic. YES
B5 18; 2; flat; S0 -> diatropic. YES
B6 22; 2; flat; T1 -> Baird 4n+2 triplet -> paratropic. NO
B7 20 CH minus 2e = 18; 2; flat; S0 -> diatropic. YES
B8 16 CH plus 2e = 18; 2; two half-turns (Hueckel); S0 -> diatropic. YES
B9 22; 2; one half-turn; S0 -> Moebius 4n+2 -> paratropic. NO
B10 16+2 = 18; 2; flat; S0 -> diatropic. YES
B11 16 + 2x1 = 18; 2; flat; S0 -> diatropic. YES
B12 16+0 = 16; 0; flat; T1 -> Baird 4n -> diatropic. YES
B13 14+2 = 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B14 20+0 = 20; 0; flat; T1 -> Baird 4n -> diatropic. YES
B15 14+2 = 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B16 circuit severed by the sp3 centre; the 18 sp2 CH form an open polyene, no closed circuit -> no macrocyclic ring current (the apparent "18 pi, 4n+2" is a decoy). NO

Diatropic: B2, B3, B4, B5, B7, B8, B10, B11, B12, B13, B14, B15 = 12. Paratropic/none: B1, B6, B9, B16 = 4.

Literature anchors for each judgement: [16]annulene paratropic and its dianion (18 pi) diatropic; Heilbronner/Herges Moebius annulene (odd half-twist inverts); lemniscular/figure-eight expanded porphyrins (even half-twist = Hueckel); Baird 1972 and subsequent T1-aromaticity work (T1 of benzene paratropic, T1 of 4n rings diatropic); borepin/borole (B contributes 0 while sustaining conjugation); tropylium (C+ 0); cyclopentadienide (C- 2); pyrrole (N-H 2) vs pyridine (N= 1); furan (O 2).
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $12$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Classifies B12 as diatropic with $16$ circuit electrons in its triplet state.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Excludes B16 because its $\mathrm{sp}^3$ centre severs the cyclic conjugated circuit.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source inspiration:** Cardenas, A.; Jin, Z.; Ni, Y.; Wu, J.; Xia, Y.; Ramirez, F. J.; Casado, J. *Beilstein J. Org. Chem.* **2025**, *21*, 277-285. doi:10.3762/bjoc.21.20 (pub 05 Feb 2025, CC BY 4.0). Physics borrowed only (local vs global ring currents, Huckel bookkeeping failing in both directions); no number, compound or claim reused.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_belt_census.md](../../planck_task_belt_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
