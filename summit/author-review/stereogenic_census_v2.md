# Author review: stereogenic_census_v2

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/stereogenic_census_v2/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours. Report the sum of the seven numbers as a single integer.

D1: $N$-(2,6-di-tert-butylphenyl)-$N$-(1-phenylethyl)acetamide

D2: $N$-(2-tert-butyl-6-methylphenyl)-$N$-methylacetamide

D3: $N$-(2-tert-butyl-6-methylphenyl)-$N$-(1-phenylethyl)acetamide

D4: $N$-(2-tert-butyl-6-methylphenyl)succinimide

D5: benzene-1,4-dicarboxylic acid bis[$N$-(2-tert-butyl-6-methylphenyl)-$N$-methylamide]

D6: 2,2',6,6'-tetramethylbiphenyl

D7: 2,3-dibromobutane

Use the following rotational data as given. For the bond from the amide or imide nitrogen to the ortho-disubstituted ring in D1 to D5, and for the bond joining the two rings in D6, the half-life for rotation at $25\,^\circ\mathrm{C}$ exceeds ten years. For every amide and imide carbonyl-to-nitrogen bond, the half-life for rotation at $25\,^\circ\mathrm{C}$ is less than one second. Rotation about every other single bond is fast at $25\,^\circ\mathrm{C}$.

Take each compound to have the single constitution named: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely on the stated timescale, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$16$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1.** Count a structure as a separate stereoisomer only if it stays distinct at $25\,^\circ\mathrm{C}$ for hours, with no bond made or broken.

**Step 2.** Rotation about every amide and imide carbonyl-to-nitrogen bond has a half-life under one second, so those rotamers interconvert freely and are never counted.

**Step 3.** Rotation about the nitrogen-to-ring bond in D1–D5, and about the ring-to-ring bond in D6, has a half-life over ten years, so those bonds are frozen and any distinct structures they generate are separate species.

**Step 4.** Only two kinds of stereogenic element can arise here: $\mathrm{sp}^3$ stereocentres, and the frozen bonds of Step 3.

**Step 5.** An $\mathrm{sp}^3$ carbon is a stereocentre when it carries four different substituents.

**Step 6.** A frozen bond is a stereogenic axis only if *each* of the two atoms it joins carries two different substituents.

**Step 7.** Reason for Step 6: if either atom carries two identical substituents, a $180^\circ$ turn about the bond regenerates the same structure, so the two supposed atropisomers are one compound. Barrier height is irrelevant to this test.

**Step 8.** Independent stereogenic elements multiply: $n$ of them give at most $2^n$ stereoisomers.

**Step 9.** When two stereogenic elements in one molecule are constitutionally equivalent, the two mixed combinations are the same structure, and that structure is achiral. The count is then 3, not 4.

---

**Step 10.** D1, stereocentre: the $\mathrm{CH}(\mathrm{CH_3})\mathrm{Ph}$ carbon carries H, $\mathrm{CH_3}$, phenyl and N — four different groups, so it is a stereocentre.

**Step 11.** D1, axis: the ring's two ortho positions both carry *tert*-butyl. They are identical, so by Step 6 the frozen N–aryl bond is not a stereogenic axis, despite the ten-year half-life.

**Step 12.** D1 total: one stereocentre, no axis, $2^1 = \mathbf{2}$.

**Step 13.** D2, stereocentre: none present.

**Step 14.** D2, ring end: the ortho positions carry *tert*-butyl and methyl — different.

**Step 15.** D2, nitrogen end: the nitrogen carries methyl and acetyl — different.

**Step 16.** D2, axis: both ends pass Step 6, so the frozen bond is a stereogenic axis giving two atropisomers.

**Step 17.** D2, check: the fast C–N rotation of Step 2 spins the acetyl group but never exchanges the nitrogen's two substituents, so it cannot erase this axis.

**Step 18.** D2 total: $\mathbf{2}$.

**Step 19.** D3, axis: the ring end (*tert*-butyl vs methyl) and the nitrogen end (1-phenylethyl vs acetyl) are both dissymmetric, so the axis is stereogenic.

**Step 20.** D3, stereocentre: the 1-phenylethyl carbon is a stereocentre, as in Step 10.

**Step 21.** D3 total: two independent elements, $2^2 = \mathbf{4}$.

**Step 22.** D4, ring end: *tert*-butyl vs methyl — different, so this end passes.

**Step 23.** D4, nitrogen end: the succinimide nitrogen's two substituents are the two carbonyl carbons of the same ring, which are identical.

**Step 24.** D4, axis: the nitrogen end fails Step 6, so the frozen bond is not a stereogenic axis.

**Step 25.** D4 total: no stereocentre, no axis, $\mathbf{1}$.

**Step 26.** D5, axes: the molecule carries two N–aryl bonds, each with a *tert*-butyl/methyl ring end and a methyl/acyl nitrogen end, so each is a stereogenic axis by Step 6.

**Step 27.** D5, combinations: the four labels are (aR,aR), (aS,aS), (aR,aS) and (aS,aR).

**Step 28.** D5, reduction: the two halves are constitutionally equivalent across the 1,4-phenylene linker, so (aR,aS) and (aS,aR) describe the same achiral structure; (aR,aR) and (aS,aS) remain an enantiomeric pair.

**Step 29.** D5 total: $\mathbf{3}$.

**Step 30.** D6, axis: each ring carries two identical ortho methyls, so both ends fail Step 6 and the frozen biaryl bond is not a stereogenic axis.

**Step 31.** D6 total: $\mathbf{1}$.

**Step 32.** D7, stereocentres: C2 and C3 each carry H, $\mathrm{CH_3}$, Br and the remaining carbon chain, so both are stereocentres.

**Step 33.** D7, reduction: the two stereocentres are constitutionally equivalent, so by Step 9 the count is (2R,3R), (2S,3S) and the meso (2R,3S).

**Step 34.** D7 total: $\mathbf{3}$.

**Step 35.** Sum the seven counts: $2 + 2 + 4 + 1 + 3 + 1 + 3$.

**Final Answer: 16**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $16$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $1$ stereoisomer for D4 because the imide nitrogen's two carbonyl substituents are equivalent.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $3$ stereoisomers for D5 after identifying its mixed axial configurations as one meso form.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
# Sources — stereogenic-element census v2 (answer 16)

## 1. Seed paper

Akimoto, N.; Takaya, K.; Kasashima, Y.; Watanabe, K.; Yoshida, Y.; Mino, T.
"Pd-Catalyzed asymmetric allylic amination with isatin using a P,olefin-type chiral ligand with C–N bond axial chirality."
*Beilstein J. Org. Chem.* **2025**, *21*, 1018–1023. doi:10.3762/bjoc.21.83
Published **23 May 2025**. Open access, CC BY 4.0. Full text freely verifiable.

**What was taken:** one concept — that a C(aryl)–N(amide) bond can carry a configurationally stable stereogenic axis, and that its stability is set by ortho substitution.

**What was NOT taken:** no compound, structure, yield, ee value, ligand, reaction or measured barrier from the paper appears in the prompt or the golden solution. The paper's actual subject — Pd-catalysed asymmetric allylic amination of isatin with a P,olefin ligand — is entirely absent. All seven compounds in the prompt are chosen for this problem.

**Cutoff status:** 23 May 2025, comfortably before 2025-07-31. (Deliberately preferred over bjoc.21.119, which is dated exactly 31 July 2025 and carries no margin.)

## 2. The ground truth does not depend on any citation

Worth stating plainly, because it is what makes this task QC-robust: the answer is *derived*, not looked up.

- The both-ends-dissymmetric requirement is proved in Step 6 of the golden from first principles — if either end of the axis carries two identical substituents, a 180° rotation maps the molecule onto itself, so the two putative rotamers are one compound. No barrier height can change this, and no literature source is needed to establish it.
- The timescale gate is computed from the Eyring equation (Section 4 below), not asserted.

The references in Section 3 therefore serve one purpose only: to establish that C–N axial chirality is *standard* chemistry, so that adversarial QC cannot dismiss the omitted inventory member as obscure trivia.

## 3. Concept grounding

**(a) C–N axial chirality in anilides and imides.** Curran and co-workers established in 1994 that sufficiently large ortho substituents adjacent to a C–N axis raise the rotational barrier enough to prevent racemisation at room temperature, working on axially twisted **amides and imides** — the two motifs used as D1–D5 here. Later work in the same programme: Curran, D. P.; Chen, C. H.-T.; Geib, S. J.; Lapierre, A. J. B. "Synthesis of Enantioenriched Axially Chiral Anilides from Atropisomerically Enriched Tartarate Ortho-Anilides." *J. Am. Chem. Soc.* **2001**, doi:10.1021/ja010467p.

Openly accessible secondary sources covering the same ground:
- "Atropisomers beyond the C–C axial chirality: Advances in catalytic asymmetric synthesis." *Chem* **2022**, *8*, 1855. (open PDF)
- "Stereoselective construction of atropisomers featuring a C–N chiral axis." *Green Synthesis and Catalysis* (ScienceDirect, open access).
- "Asymmetric Synthesis of Axially Chiral C–N Atropisomers." *Chem. Eur. J.* **2022**, doi:10.1002/chem.202104442.

*Verification note:* the 1994 JACS paper (doi:10.1021/ja00086a056, "Atroposelective Thermal Reactions of Axially Twisted Amides and Imides") is behind an ACS paywall and returned HTTP 403, so its title and DOI were confirmed from indexing rather than from the article itself. The open-access reviews above cover the same claim and can be checked directly.

**(b) Rotation barriers in tertiary aromatic amides.** Clayden and co-workers measured barriers for 40 tertiary aromatic amides by variable-temperature NMR and atropisomer interconversion, giving empirical guidelines for when an amide axis is configurationally stable: "Barriers to rotation about the chiral axis of tertiary aromatic amides," *Tetrahedron* **1998**. (Note this concerns the Ar–C(O) axis; the anilide work in (a) concerns the C(aryl)–N axis used here. The two should not be conflated.)

**(c) Meso relationships; the both-ends-dissymmetric criterion for axial chirality.** Standard stereochemistry: Eliel, E. L.; Wilen, S. H. *Stereochemistry of Organic Compounds*; Wiley: New York, 1994.

**(d) Tetra-ortho-substituted biphenyls are rotationally locked.** Long-established; this is why D6's hindrance is not arguable and the achirality must be decided on symmetry grounds.

## 4. The timescale gate, computed

Eyring at 298.15 K, k_B·T/h = 6.212 × 10^12 s^-1:

| ΔG‡ (kcal/mol) | half-life at 25 °C |
|---|---|
| 15 | 0.011 s |
| 18 | 1.7 s |
| 20 | 51 s |
| 21 | 4.6 min |
| 22 | 25 min |
| 23 | 2.2 h |
| 25 | 2.7 d |
| 26 | 14.8 d |

A half-life of one hour corresponds to ΔG‡ = 22.5 kcal/mol; six hours to 23.6; one day to 24.4.

This gives clean separation with no borderline case:
- **Amide/imide C(O)–N rotation** (≈15–21 kcal/mol) → half-lives from milliseconds to minutes → **excluded** by the stated "hours".
- **Anilide C(aryl)–N atropisomerism** with 2,6-disubstitution (≈25 kcal/mol and above) → half-lives of days → **counted**.

The gap between the two regimes is roughly 4 kcal/mol, a factor of several hundred in lifetime, so the prompt's "hours" stipulation partitions them unambiguously.

**Cross-check against the seed paper.** It reports ΔG‡_rac = 25.0 kcal/mol with a racemisation half-life of about 1.3 days. Eyring at 25.0 kcal/mol gives a *rotation* half-life of 2.73 days. The factor of two is expected and correct: racemisation approaches equilibrium between two enantiomers, so k_rac = 2·k_rot, giving t½(rac) = 1.37 days — matching the paper. This confirms both the arithmetic here and the paper's reported value, and it is the reason the prompt's own compounds sit safely inside the "isolable" regime.

## 5. Originality

The problem is original: not taken from, adapted from, or paraphrased from any published problem set, examination, or textbook exercise. The seed paper supplied one structural concept. The specific question — a stereoisomer census over seven named compounds in which three contain a rotationally locked but achiral axis, each failing for a different reason — does not appear in the literature. The answer 16 was derived here and verified by parametrised enumeration over the four independent judgments (`scratchpad/stereo2.py`).

````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_stereogenic_census_v2.md](../../planck_task_stereogenic_census_v2.md)
- [planck_task_stereogenic_census_v2_golden.md](../../planck_task_stereogenic_census_v2_golden.md)
- [planck_task_stereogenic_census_v2_sources.md](../../planck_task_stereogenic_census_v2_sources.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
