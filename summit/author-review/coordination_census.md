# Author review: coordination_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/coordination_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Ligands, as SMILES: ammonia `N`; pyridine `c1ccncc1`; chloride `[Cl-]`; bromide `[Br-]`; ethane-1,2-diamine `NCCN`; glycinate `NCC(=O)[O-]`; oxalate `[O-]C(=O)C(=O)[O-]`; 2,2':6',2''-terpyridine `c1ccc(nc1)-c1cccc(n1)-c1ccccn1`.

For each complex below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Report the sum of the six numbers as a single integer.

H1: square-planar Pt(II) bound to two ammonia and two chloride

H2: tetrahedral Zn(II) bound to one ammonia, one pyridine, one chloride and one bromide

H3: octahedral Co(III) bound to one ethane-1,2-diamine, one ammonia, one pyridine, one chloride and one bromide

H4: square-planar Pt(II) bound to one glycinate, one ammonia and one chloride

H5: octahedral Co(III) bound to two ethane-1,2-diamine, one ammonia and one chloride

H6: octahedral Ru(II) bound to one terpyridine, one oxalate and one chloride

Every ligand binds through the donor atoms of the structure shown, and each ligand binds to one metal centre only. Take each complex to be configurationally stable: no ligand dissociates, exchanges or migrates, and no bond is made or broken. Count only stereoisomers of the coordination composition given; disregard linkage and ionisation isomers. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$22$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1.** Count a structure as a separate stereoisomer only if it is isolable at $25\,^\circ\mathrm{C}$ over hours; enantiomers count as two, as stated.

**Step 2.** A chelating ligand can only bridge two coordination sites that are mutually cis, since its donor atoms are held a fixed short distance apart and trans sites lie on opposite sides of the metal.

**Step 3.** A structure is chiral when no improper symmetry operation maps it onto itself; for a coordination compound this must be tested arrangement by arrangement, not inferred from whether ligands are cis or trans.

---

**Step 4.** H1: the four donors lie in one plane with the metal, and that plane is a mirror plane for every arrangement, so no square-planar arrangement of this composition can be chiral.

**Step 5.** H1's two chlorides may be mutually cis or mutually trans, giving two diastereomers and no enantiomers. **H1 = 2.**

**Step 6.** H2: a tetrahedral centre carrying four different ligands has no improper symmetry operation, exactly as an sp³ carbon with four different substituents does not.

**Step 7.** H2 therefore exists as one enantiomeric pair. **H2 = 2.**

**Step 8.** H3: ethane-1,2-diamine is a chelate, so by Step 2 it occupies one of the twelve mutually-cis site pairs (the twelve edges of the octahedron), and the four remaining sites carry four different ligands in $4! = 24$ ways.

**Step 9.** H3 therefore has $12 \times 24 = 288$ labelled arrangements, and the octahedron has 24 proper rotations, giving $288/24 = 12$ distinct structures provided no arrangement is fixed by a non-trivial rotation — which none is, since the four monodentate ligands are all different.

**Step 10.** H3: none of the twelve retains any improper operation either, because a mirror would have to fix the chelate and exchange monodentate ligands that are all different. Every one is chiral, forming six enantiomeric pairs. **H3 = 12.**

**Step 11.** H4: glycinate chelates through its nitrogen and one carboxylate oxygen, two *different* donors, and by Step 2 occupies two adjacent sites of the square plane.

**Step 12.** H4's remaining two sites carry ammonia and chloride, and the two arrangements differ by which is trans to nitrogen and which is trans to oxygen; both are achiral by Step 4. **H4 = 2.**

**Step 13.** H5: the two chelates occupy four sites, leaving ammonia and chloride either mutually trans or mutually cis.

**Step 14.** H5's trans arrangement has a mirror plane containing both monodentate ligands and is achiral; the cis arrangement has none and forms an enantiomeric pair. **H5 = 3.**

**Step 15.** H6: terpyridine's three pyridine rings are joined directly at their 2- and 6-positions, so the three nitrogen donors are held in one plane in a fixed near-linear array.

**Step 16.** H6: that rigid geometry allows only a meridional arrangement — the two terminal nitrogens must be mutually trans — since a facial arrangement would require the terminal donors to be cis, which the ligand's fused framework cannot reach.

**Step 17.** H6: with terpyridine meridional, the three remaining sites are one trans to the central nitrogen and two trans to the terminal nitrogens; those latter two are mutually trans, so by Step 2 oxalate cannot span them.

**Step 18.** H6: oxalate must therefore use the site trans to the central nitrogen plus one of the other two, and those two choices are related by a symmetry of the rest of the structure, so they give the same compound; chloride takes the last site, and the result has a mirror plane. **H6 = 1.**

**Step 19.** Sum the six counts: $2 + 2 + 12 + 2 + 3 + 1$.

**Final Answer: 22**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $22$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $12$ distinct stereoisomers for H3, counting enantiomers separately.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $2$ distinct arrangements for H4 from the inequivalent N and O chelate donors.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** none. All six complexes are chosen for this problem; no compound, measurement or claim is taken from any paper, so there is no cutoff exposure. Every principle used is textbook coordination chemistry.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_coordination_census.md](../../planck_task_coordination_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
