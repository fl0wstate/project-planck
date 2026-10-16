# Author review: stereogenic_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/stereogenic_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours. Report the sum of the six numbers as a single integer.

C1: $N$-(2,6-dimethylphenyl)-$N$-(1-phenylethyl)acetamide

C2: $N$-(2-tert-butyl-6-methylphenyl)-$N$-methylacetamide

C3: $N$-(2-tert-butyl-6-methylphenyl)-$N$-(1-phenylethyl)acetamide

C4: benzene-1,4-dicarboxylic acid bis[$N$-(2-tert-butyl-6-methylphenyl)-$N$-methylamide]

C5: 2,6-dimethyl-2'-nitrobiphenyl

C6: 2,3-dibromobutane

Take each compound to have the single constitution named: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely on the stated timescale, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$15$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
| | analysis | count |
|---|---|---|
| **C1** | One stereocentre (the $N$-CH(CH_3)Ph carbon: N, CH_3, Ph, H all different). The N-aryl bond is strongly hindered, but the aryl ring bears **two identical** ortho methyls, so rotation by 180 degrees regenerates the same structure and the axis is **not** stereogenic. $2^1$ | **2** |
| **C2** | No stereocentre. The N-aryl axis has *tert*-butyl on one ortho position and methyl on the other (dissymmetric), the N end bears methyl and acetyl (dissymmetric), and 2,6-disubstitution makes rotation slow. One stereogenic axis. $2^1$ | **2** |
| **C3** | The C2 axis plus the C1 stereocentre, independent. $2^2$ | **4** |
| **C4** | Two constitutionally identical stereogenic axes of the C2 type. (aR,aR) and (aS,aS) are enantiomers; (aR,aS) is **meso**, since the para-phenylene's inversion centre exchanges the halves and converts aR into aS. | **3** |
| **C5** | No stereocentre. Three ortho substituents make rotation slow, but the 2,6-dimethyl ring has **two identical** ortho substituents, so the biaryl axis is not stereogenic. Achiral. | **1** |
| **C6** | Two stereocentres, constitutionally identical: (R,R), (S,S), and one meso (R,S). | **3** |

**Sum = 2 + 2 + 4 + 3 + 1 + 3 = 15.**

Amide C(O)-N rotamers are excluded by the stated timescale: tertiary-amide rotation barriers of roughly 15-20 kcal/mol give lifetimes of seconds at 25 degrees C, far below "hours". The stipulation resolves this deductively rather than leaving it to judgment.
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $15$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains $2$ stereoisomers for C1 because its identical ortho substituents prevent axial stereogenicity.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $3$ stereoisomers for C4 after identifying the mixed axial configurations as one meso form.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** Akimoto, N.; Takaya, K.; Kasashima, Y.; Watanabe, K.; Yoshida, Y.; Mino, T. "Pd-Catalyzed asymmetric allylic amination with isatin using a P,olefin-type chiral ligand with C-N bond axial chirality." *Beilstein J. Org. Chem.* **2025**, *21*, 1018-1023. doi:10.3762/bjoc.21.83. Published **23 May 2025**, CC BY 4.0. Comfortably pre-cutoff (two months of margin, unlike bjoc.21.119 which sits exactly on 31 Jul 2025).
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_stereogenic_census.md](../../planck_task_stereogenic_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
