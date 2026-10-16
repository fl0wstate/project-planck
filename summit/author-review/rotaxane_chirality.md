# Author review: rotaxane_chirality

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/rotaxane_chirality/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
All 16 [2]rotaxanes obtained by threading one of four macrocycles $M1$-$M4$ onto one of four dumbbells $A1$-$A4$ are isolable.

Macrocycles: each is a shape-persistent ring of six 1,3-disubstituted benzene residues joined by six secondary amide bonds.
$M1$: every residue is a 3-aminobenzoyl unit, so all six $\mathrm{C(O)NH}$ linkages point the same way around the ring; no further substituents.
$M2$: three isophthaloyl and three benzene-1,3-diamine residues alternate, so the amides meet head-to-head and tail-to-tail; no further substituents.
$M3$: as $M1$, plus a $-\mathrm{CH_2OCH_2}-$ strap joining the 5-positions of two diametrically opposite residues and arching over one face of the ring; the strap cannot reach the other face.
$M4$: as $M2$, plus the same strap joining two diametrically opposite residues.

Dumbbells: each has the core $-\mathrm{O(CH_2)_6O}-$ bearing two end groups, with $\mathrm{Ar}=3,5$-di-tert-butylphenyl and $\mathrm{Ad}=1$-adamantyl.
$A1$: $-\mathrm{CH_2Ar}$ at both ends.
$A2$: $-\mathrm{CH_2Ar}$ at one end, $-\mathrm{CH_2Ad}$ at the other.
$A3$: $-\mathrm{CH(CH_3)Ar}$ at both ends, one $(R)$ and one $(S)$.
$A4$: $-\mathrm{CH(CH_3)Ar}$ at both ends, both $(R)$.

Assume free rotation about all single bonds, planar trans-amides, no atropisomerism, and free shuttling and pirouetting of the macrocycle, which cannot pass over a stopper. A rotaxane counts as achiral if any accessible conformation/co-conformation is superimposable on its mirror image.

How many of the 16 rotaxanes are chiral? Answer with a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$9$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
Set the axle along $z$; the macrocycle encircles it. Any symmetry operation of a [2]rotaxane must map each component onto itself and preserve the axle axis. The only candidate IMPROPER operations are therefore: (i) $\sigma_v$ = a mirror plane containing the axle axis (keeps each stopper on its own side, keeps each macrocycle face on its own side); (ii) $\sigma_h$ = the macrocycle's own mean plane, or any $S_n$ about $z$, all of which exchange the two halves of the axle AND exchange the two faces of the ring. In-plane $C_2$ and rotations about $z$ are proper and irrelevant. Hence:

achiral iff [macrocycle has a $\sigma_v$ AND axle has a mirror plane containing its axis] OR [macrocycle is face-symmetric ($\sigma_h$) AND the axle's two ends are exchangeable by an improper operation].

Component analysis (8 independent judgments).
Macrocycles:
- $M1$ (head-to-tail hexa-amide): going round the ring the amides all read $\mathrm{N}\to\mathrm{C}$ in one sense. A $\sigma_v$ (or an in-plane $C_2$) reverses that sense, so it is constitutionally forbidden: NO $\sigma_v$. The ring is planar with two chemically equivalent faces: HAS $\sigma_h$ (point group $C_{6h}$; the macrocycle itself is achiral, yet "orientated").
- $M2$ (alternating diacyl/diamine): mirror lines through opposite residues map acyl onto acyl and amine onto amine and preserve amide sense: HAS $\sigma_v$; planar, HAS $\sigma_h$ ($D_{3h}$).
- $M3$ ($M1$ + one-face strap): no $\sigma_v$ (orientation) and no $\sigma_h$ (strap on one face only) $\Rightarrow$ $C_1$, the macrocycle is itself CHIRAL (planar-chiral strapped ring).
- $M4$ ($M2$ + one-face strap): the mirror plane through the two strapped opposite residues survives (the strap is symmetric in it): HAS $\sigma_v$; strap kills $\sigma_h$ and $i$. Point group $C_s$: achiral, faces distinguishable. This is the trap case: distinguishable faces do NOT make a ring "orientated".
Dumbbells (a stereocentre can never lie on a mirror plane, so any axle bearing stereocentres has no $\sigma_v$):
- $A1$: identical ends, no stereocentres: has $\sigma_v$; ends exchangeable by an improper op (midpoint mirror).
- $A2$: different stoppers: has $\sigma_v$; ends NOT exchangeable.
- $A3$: constitutionally identical ends, $(R)$ and $(S)$ = meso axle: no $\sigma_v$; ends exchangeable improperly (midpoint $\sigma$/$i$, which inverts $R\to S$ correctly).
- $A4$: $(R),(R)$: no $\sigma_v$; the two ends are exchanged only by a PROPER $C_2$, never by an improper op (a mirror would demand $R$ opposite $S$). Chiral axle.

16-case table (achiral unless marked):
$M1A1$ achiral ($\sigma_h$); $M1A2$ CHIRAL (canonical mechanically planar chiral rotaxane); $M1A3$ achiral - $\sigma_h$ swaps the ends and inverts $R\leftrightarrow S$, so the mechanical element and the two centres form a meso rotaxane; $M1A4$ CHIRAL.
$M2A1$ achiral ($\sigma_v$); $M2A2$ achiral ($\sigma_v$: an unsymmetrical axle alone is not enough); $M2A3$ achiral ($\sigma_h$); $M2A4$ CHIRAL (chiral component).
$M3A1$-$M3A4$ all CHIRAL (a rotaxane containing a chiral component can have no improper operation).
$M4A1$ achiral ($\sigma_v$); $M4A2$ achiral ($\sigma_v$ survives despite distinguishable faces); $M4A3$ CHIRAL ($\sigma_v$ destroyed by the stereocentres, $\sigma_h$/$i$ destroyed by the strap); $M4A4$ CHIRAL.

Chiral count $=2+1+4+2=9$.
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $9$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Identifies M1 as lacking $\sigma_v$ but possessing $\sigma_h$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Identifies M4 as possessing $\sigma_v$ despite its distinguishable faces.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source inspiration:** Beilstein J. Org. Chem. 2025, 21, 10 (doi:10.3762/bjoc.21.10) — physics borrowed only, no numbers/compounds reused.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_rotaxane_chirality.md](../../planck_task_rotaxane_chirality.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
