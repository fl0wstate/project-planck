# Author review: mixed_stereo_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/mixed_stereo_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Report the sum of the eight numbers as a single integer.

F1: `OC1CCC(O)CC1`

F2: `CC(C)C(O)C(C)C`

F3: `CC(O)C(=O)OCCOC(=O)C(C)O`

F4: `OC1CC2CCC1C2`

F5: `CCCN(C)CC`

F6: `OC1CCCC(C)C1`

F7: `CC1CCCC=C1`

F8: `CC=C=C(C)C`

Each SMILES string specifies the full constitution and carries no stereochemical information; take each compound to have exactly the constitution shown: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely at $25\,^\circ\mathrm{C}$ over a period of hours, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$18$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1.** Count a structure as a separate stereoisomer only if it is isolable at $25\,^\circ\mathrm{C}$ over hours and does not interconvert freely with another on that timescale.

**Step 2.** An $\mathrm{sp}^3$ carbon is a stereocentre only when its four substituents are all different.

**Step 3.** Enantiomers are counted as two, as stated.

---

**Step 4.** F1: each substituted ring carbon is attached to H, OH and two ring paths that are identical, since the other hydroxyl sits at the opposite position, so neither is a stereocentre.

**Step 5.** F1 therefore has no stereocentre, but the two substituents can still sit on the same face or on opposite faces of the ring, giving cis and trans diastereomers.

**Step 6.** Each of those is achiral, having a mirror plane through the two substituted carbons, so neither adds an enantiomer. **F1 = 2.**

**Step 7.** F2: C3 carries OH, H and two isopropyl groups, which are constitutionally identical, so C3 is not a stereocentre.

**Step 8.** F2's C2 and C4 each carry two identical methyl groups, so neither is a stereocentre either, and no other element is present. **F2 = 1.**

**Step 9.** F3: each of the two lactate units carries a stereocentre at its CH(OH) carbon, giving four label combinations.

**Step 10.** F3's two halves are constitutionally identical and are exchanged by an internal operation across the symmetric $-\mathrm{OCH_2CH_2O}-$ linker, so the two mixed combinations are one achiral meso compound.

**Step 11.** F3 therefore has the (R,R)/(S,S) enantiomeric pair plus that meso form. **F3 = 3.**

**Step 12.** F4: the carbon bearing OH may have that OH on the exo or the endo face, which is a genuine choice.

**Step 13.** F4's two bridgehead carbons cannot be inverted independently — their configurations are imposed by the bicyclic framework, since inverting one would require breaking a bond.

**Step 14.** F4's substitution at C2 destroys both mirror planes of the parent cage, so each of the exo and endo diastereomers is chiral and exists as an enantiomeric pair. **F4 = 4.**

**Step 15.** F5: the nitrogen carries methyl, ethyl and propyl, three different groups, plus a lone pair, so it is a pyramidal centre with four different "substituents".

**Step 16.** F5's nitrogen nevertheless inverts through a planar transition state many times per second at $25\,^\circ\mathrm{C}$, so the two pyramidal forms interconvert freely and count as one species by Step 1. **F5 = 1.**

**Step 17.** F6: the ring bears OH at C1 and methyl at C3, so, as in F1, the two substituents may sit on the same face or on opposite faces, giving cis and trans diastereomers.

**Step 18.** F6, unlike F1, retains no internal mirror plane in either diastereomer: the only ring reflection that exchanges C1 and C3 would require the two substituents to be identical, and they differ, while every other reflection carries the methyl onto an unsubstituted carbon.

**Step 19.** Each F6 diastereomer is therefore chiral and exists as an enantiomeric pair. **F6 = 4.**

**Step 20.** F7: C3 carries a methyl, an H, and two different ring paths — one reaching the double bond in one bond, the other in three — so it is a stereocentre and gives an enantiomeric pair.

**Step 21.** F7's ring double bond cannot adopt a trans configuration, a six-membered ring being far too small to span it, so it contributes no further isomers. **F7 = 2.**

**Step 22.** F8: the axis has two cumulated double bonds, so its two ends are perpendicular and axial chirality is possible in principle.

**Step 23.** F8's $\mathrm{(CH_3)_2C{=}}$ end carries two identical methyl groups, so a $180^\circ$ turn about the axis regenerates the same structure and the axis is not stereogenic. **F8 = 1.**

**Step 24.** Sum the eight counts: $2 + 1 + 3 + 4 + 1 + 4 + 2 + 1$.

**Final Answer: 18**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $18$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $2$ stereoisomers for F1 from cis/trans geometry despite the absence of stereocentres.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $3$ stereoisomers for F3 after identifying its mixed configurations as one meso form.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** none. All eight compounds are chosen for this problem; no compound, measurement or claim is taken from any paper, so there is no cutoff exposure. Every principle used is textbook.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_mixed_stereo_census.md](../../planck_task_mixed_stereo_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
