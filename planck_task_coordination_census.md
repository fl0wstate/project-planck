# planck task — mixed-geometry coordination isomer census

**FINAL ANSWER: 22**

**Subdomain: Chemistry - Inorganic**

**Source:** none. All six complexes are chosen for this problem; no compound, measurement or claim is taken from any paper, so there is no cutoff exposure. Every principle used is textbook coordination chemistry.

---

## THE LEVER

Two mechanisms, both confirmed on the platform this campaign.

**1. The clean shortcut route is blocked.** Chelate bite constraints forbid a bidentate from spanning trans positions, so naive site-permutation counting fails outright. This is the property that made `bicyclo[2.2.1]heptan-2-ol` bite **3 of 4 responses** in the organic census: when the obvious route is unavailable, the solver is forced onto the two-layer path — enumerate the arrangements, *then* ask which are chiral — and layer two is where attention fails. Entry H3 has twelve isomers and **every one of them is chiral**; a solver who enumerates diastereomers and stops returns 6.

**2. A rigid ligand that cannot do what its flexible analogue does.** H6's terpyridine is planar and rigid, so its three donors can only bind **meridionally** — it has no facial mode at all. Treated as a flexible tridentate it gives 4 isomers instead of 1. Nothing in the prompt mentions rigidity, facial or meridional binding; the constraint has to be read off the ligand's own structure, which the SMILES supplies.

**Deliberately no flexible-tridentate entry.** An obvious dien/terpy pair sharing co-ligands would advertise rigidity as the axis of variation, which is the retrieval-cue failure (A3/A18). Rigidity is load-bearing exactly once, with no comparison offered.

**Six entries, six different deciding questions** — the property separating the one census that scored from every one that was solved. A themed set fails: `cumulene_census` re-used one predicate in seven costumes and both responders opened by writing the rule block as a preamble, then ground through mechanically.

| | complex | the question that decides it | count |
|---|---|---|---|
| H1 | square-planar Pt, 2 NH₃ + 2 Cl | can a square-planar arrangement be chiral at all? | **2** |
| H2 | tetrahedral Zn, four different | four different donors on a tetrahedron | **2** |
| H3 | octahedral Co, en + four different | does *any* arrangement keep an improper operation? | **12** |
| H4 | square-planar Pt, glycinate + NH₃ + Cl | which donor of the unsymmetric chelate is trans to what? | **2** |
| H5 | octahedral Co, 2 en + NH₃ + Cl | the classic cis-chiral / trans-achiral case | **3** |
| H6 | octahedral Ru, terpy + oxalate + Cl | can this tridentate bind facially? | **1** |

H5 is the **decorrelator**: it is the one entry where the slogan "cis is chiral, trans is achiral" is true. A solver who carries that slogan into H3 or H1 is confidently wrong.

---

## PROMPT

```
Ligands, as SMILES: ammonia `N`; pyridine `c1ccncc1`; chloride `[Cl-]`; bromide `[Br-]`; ethane-1,2-diamine `NCCN`; glycinate `NCC(=O)[O-]`; oxalate `[O-]C(=O)C(=O)[O-]`; 2,2':6',2''-terpyridine `c1ccc(nc1)-c1cccc(n1)-c1ccccn1`.

For each complex below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Report the sum of the six numbers as a single integer.

H1: square-planar Pt(II) bound to two ammonia and two chloride

H2: tetrahedral Zn(II) bound to one ammonia, one pyridine, one chloride and one bromide

H3: octahedral Co(III) bound to one ethane-1,2-diamine, one ammonia, one pyridine, one chloride and one bromide

H4: square-planar Pt(II) bound to one glycinate, one ammonia and one chloride

H5: octahedral Co(III) bound to two ethane-1,2-diamine, one ammonia and one chloride

H6: octahedral Ru(II) bound to one terpyridine, one oxalate and one chloride

Every ligand binds through the donor atoms of the structure shown, and each ligand binds to one metal centre only. Take each complex to be configurationally stable: no ligand dissociates, exchanges or migrates, and no bond is made or broken. Count only stereoisomers of the coordination composition given; disregard linkage and ionisation isomers. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
```

---

## GOLDEN

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

---

## WRONG BRANCHES AND COLLISION AUDIT

Three independent error modes, computed in every combination:

| bite constraint ignored | terpy read as flexible | chirality layer skipped | per-entry | total |
|---|---|---|---|---|
| — | — | — | 2, 2, 12, 2, 3, 1 | **22 (truth)** |
| — | — | ✓ | 2, 1, 6, 2, 2, 1 | 14 |
| — | ✓ | — | 2, 2, 12, 2, 3, 4 | 25 |
| — | ✓ | ✓ | 2, 1, 6, 2, 2, 3 | 16 |
| ✓ | — | — | 2, 2, 15, 3, 5, 2 | 29 |
| ✓ | — | ✓ | 2, 1, 9, 3, 4, 2 | 21 |
| ✓ | ✓ | — | 2, 2, 15, 3, 5, 5 | 32 |
| ✓ | ✓ | ✓ | 2, 1, 9, 3, 4, 4 | 23 |

**All eight totals are distinct and only the correct combination gives 22.** The error modes interact non-additively — ignoring the bite constraint changes how many isomers there are *to* merge when the chirality layer is skipped — so the combinations were computed in full rather than by summing deltas.

Note the two catches were tuned against each other. Terpyridine paired with glycinate would have given a $+6$ branch, colliding exactly with the $-6$ from skipping the chirality layer on H3; oxalate gives $+3$ instead, which no combination of the other errors reaches.

---

## VERIFICATION

Ground truth by explicit group action, script `scratchpad/geom.py`. Each geometry is represented as labelled sites with its own rotation group; a configuration is (donor labels, chelate links); two configurations are the same isomer iff a proper rotation maps one to the other preserving both; a configuration is achiral iff an improper operation maps it into its own proper orbit. Chelate links are restricted to cis site pairs. **No stereocentre model is used anywhere**, which matters because RDKit's atom-centred perception is blind to metal-centred chirality entirely.

**Calibrated 7/7 against known results before use:** square-planar Ma₂b₂ = 2 and Mabcd = 3; tetrahedral Mabcd = 2 and Ma₂bc = 1; octahedral M(AA)₂b₂ = 3, M(AB)₃ = 4, and Mabcdef = 30.

**Hand-derived independently:** H6 in Steps 15–18, and H3 by the counting argument in Step 9 ($288/24 = 12$).

**One error caught by cross-checking**, worth recording: an early hand analysis of a flexible-tridentate entry gave 6 where the enumeration gave 9. The enumeration was right — I had assumed a C₂ exchanging the tridentate's two terminal donors survives as a symmetry, but it permutes the monodentate sites, and with three different monodentates it fixes nothing. That is the same error class this task is built to catch: assuming a symmetry survives labelling.

All ligand SMILES parsed and formulas confirmed, terpyridine as C₁₅H₁₁N₃.

---

## COMPLIANCE

- **Self-contained**: every ligand is given as a SMILES structure, every coordination geometry is stated, and configurational rigidity, the enantiomer convention, the exclusion of linkage and ionisation isomers, and the achiral-solvent condition are all stipulated. The two load-bearing facts — that a chelate spans only cis sites, and that terpyridine's fused framework permits only meridional binding — are derivable from the structures given, as domain knowledge should be.
- **No governing rule given**: neither the bite constraint nor the meridional restriction nor any chirality criterion appears in the prompt.
- **Nothing advertised**: the prompt contains no occurrence of chiral, enantiomer (except in the counting convention), meridional, facial, symmetry, mirror, rigid, bite or chelate.
- **No shared rule block**: six complexes, six distinct deciding questions across three coordination geometries.
- **No tabulable parameter (A18)**: nothing varies along a single axis; there is no column, series or sequence to manipulate.
- **CURVD**: Contained; Unambiguous; Reduced; Verifiable; Discrete (22).
- **Deductive ground truth**: orbit counts under stated idealised geometries, not contested empirical claims.
- **Timeless, no PII, no citations, no cutoff exposure.**

## STATUS

Built 2026-07-31. Ground truth computed by validated group action and hand-checked on two entries; full eight-way collision audit clean. **Not cold-probed** — probe outcomes were shown today to predict platform outcomes in neither direction.
