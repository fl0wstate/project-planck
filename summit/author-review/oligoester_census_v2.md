# Author review: oligoester_census_v2

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/oligoester_census_v2/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Nine cyclic oligoesters are described. In each, every residue is one of two kinds: residue X, derived from 2-hydroxybutanoic acid, contributing $-\mathrm{O}-\mathrm{CH}(\mathrm{C_2H_5})-\mathrm{C(O)}-$ to the ring, or residue Y, derived from 2-hydroxypropanoic acid, contributing $-\mathrm{O}-\mathrm{CH}(\mathrm{CH_3})-\mathrm{C(O)}-$. The residues are joined so that the sequence oxygen, then alkyl-bearing carbon, then carbonyl carbon runs the same way round the whole macrocycle. Every residue therefore carries one stereocentre, at the carbon bearing its alkyl group.

Each compound is specified by listing its residues in order with the configuration of each, read round the ring in the direction running from the ester oxygen of a residue to the carbonyl carbon of that same residue. Each list is cyclic, the residue following the last being the first.

G1: X(R) X(S) X(R) X(S)

G2: X(R) X(R) X(R) X(S)

G3: X(R) X(R) X(S)

G4: X(R) X(S) X(R) X(S) X(R) X(S)

G5: X(R) X(R) X(S) X(R) X(S) X(S)

G6: X(R) X(R) X(R) X(S) X(R) X(S) X(S) X(S)

G7: X(R) Y(S) X(R) Y(S) X(R) Y(S)

G8: X(R) Y(S) X(R) Y(S)

G9: X(R) Y(R) X(S) Y(S) X(R) Y(R) X(S) Y(S)

Take every macrocycle to be conformationally mobile, with all ring conformations freely accessible, and take the configuration at every stereocentre to be fixed. Regard a compound as chiral when no accessible conformation of it can be superimposed on its mirror image. Disregard any process that makes or breaks a covalent bond, and assume dilute solution in an achiral solvent with no added chiral agent.

How many of the nine compounds are chiral? Report a single integer.
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
Write the descriptors as a cyclic sequence $c_0 \ldots c_{n-1}$ and the residue kinds as $t_0 \ldots t_{n-1}$. The mirror image has the same constitution with every descriptor inverted. Two specifications denote the same compound exactly when one is carried onto the other by a shift $k$ that preserves the residue pattern, $t_{i+k} = t_i$ for all $i$; reversal of the order is not available, because the ester sense runs one way round the ring. Hence

> the compound is **achiral** exactly when there is a shift $k$ with $t_{i+k} = t_i$ and $c_{i+k} = \bar{c_i}$ for every $i$.

| | $n$ | residues | descriptors | permitted shifts | achiral? |
|---|---|---|---|---|---|
| G1 | 4 | XXXX | R S R S | 0,1,2,3 | achiral, $k=1$ |
| G2 | 4 | XXXX | R R R S | 0,1,2,3 | **chiral** |
| G3 | 3 | XXX | R R S | 0,1,2 | **chiral** |
| G4 | 6 | XXXXXX | R S R S R S | 0..5 | achiral, $k=1$ |
| G5 | 6 | XXXXXX | R R S R S S | 0..5 | **chiral** (fork 1) |
| G6 | 8 | XXXXXXXX | R R R S R S S S | 0..7 | **chiral** (fork 1) |
| G7 | 6 | XYXYXY | R S R S R S | 0,2,4 | **chiral** (fork 2) |
| G8 | 4 | XYXY | R S R S | 0,2 | **chiral** (fork 2) |
| G9 | 8 | XYXYXYXY | R R S S R R S S | 0,2,4,6 | achiral, $k=2$ |

**Chiral: G2, G3, G5, G6, G7, G8. Answer = 6.**

Two structural facts the solution should state:

- **Odd ring size forces chirality (G3).** Applying a shift $k$ that satisfies the condition $n$ times inverts the descriptors an odd number of times while returning every index to itself, giving $c_i = \bar{c_i}$, which is impossible. No odd-membered ring in this family is ever achiral.
- **G5 and G6 are chiral although their mirror images are reversals of themselves.** That relationship is not a symmetry of a directional macrocycle, which is precisely the point of fork 1.
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
Classifies G5 as chiral because sequence reversal is not an allowed equivalence of the directional ester ring.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Classifies G7 as chiral because its residue-preserving shifts are only $0,2,4$, none of which inverts every descriptor.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** Lam, N. Y. S.; Dhankhar, J.; Lahdenpera, A. S. K.; Phipps, R. J. *J. Am. Chem. Soc.* **2024**, *146*, 33302-33308. doi:10.1021/jacs.4c13919. Published 26 Nov 2024, CC BY 4.0, open access via PMC. Concept borrowed only.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_oligoester_census_v2.md](../../planck_task_oligoester_census_v2.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
