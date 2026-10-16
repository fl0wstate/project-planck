# Author review: oligoester_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/oligoester_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Eight cyclic oligoesters are described. Each is a macrocyclic ester built from $n$ identical residues of 2-hydroxybutanoic acid, so that the ring consists of the unit $-\mathrm{O}-\mathrm{CH}(\mathrm{C_2H_5})-\mathrm{C(O)}-$ repeated $n$ times and traversed the same way round the whole macrocycle. Every residue therefore carries one stereocentre, at the carbon bearing the ethyl group.

For each compound the configurations of those stereocentres are listed in order, read round the ring in the direction running from the ester oxygen of a residue to the carbonyl carbon of that same residue. Each list is cyclic, the residue following the last being the first.

E1: $n = 4$; R, S, R, S

E2: $n = 4$; R, R, S, S

E3: $n = 4$; R, R, R, S

E4: $n = 6$; R, S, R, S, R, S

E5: $n = 6$; R, R, S, R, S, S

E6: $n = 8$; R, S, R, S, R, S, R, S

E7: $n = 3$; R, R, S

E8: $n = 8$; R, R, S, S, R, R, S, S

Take every macrocycle to be conformationally mobile, with all ring conformations freely accessible, and take the configuration at every stereocentre to be fixed. Regard a compound as chiral when no accessible conformation of it can be superimposed on its mirror image. Disregard any process that makes or breaks a covalent bond, and assume dilute solution in an achiral solvent with no added chiral agent.

How many of the eight compounds are chiral? Report a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$3$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
| | $n$ | sequence | achiral? | via | checklist says |
|---|---|---|---|---|---|
| E1 | 4 | R S R S | achiral | $S_4$ only ($k=1$) | chiral **(missed)** |
| E2 | 4 | R R S S | achiral | inversion centre ($k=2$) | achiral |
| E3 | 4 | R R R S | **chiral** | none | chiral |
| E4 | 6 | R S R S R S | achiral | inversion centre ($k=3$) | achiral |
| E5 | 6 | R R S R S S | **chiral** | none | chiral |
| E6 | 8 | R S R S R S R S | achiral | $S_8$ only ($k=1$) | chiral **(missed)** |
| E7 | 3 | R R S | **chiral** | none | chiral |
| E8 | 8 | R R S S R R S S | achiral | rotoreflection ($k=2$) | chiral **(missed)** |

**Chiral: E3, E5, E7. Answer = 3.**

Two structural facts worth stating in the solution:

- **Odd ring size forces chirality (E7).** If $c_{i+k} = \bar{c_i}$ for all $i$, applying the shift $n$ times inverts the descriptors an odd number of times while returning every index to itself, giving $c_i = \bar{c_i}$, which is impossible. So no odd-membered ring of this family is ever achiral, whatever its sequence.
- **E5 is the control that kills the counting shortcut.** It has three R and three S, equal numbers, yet no shift satisfies the condition, so it is chiral. Any rule of the form "equal numbers of R and S implies achiral" fails here.
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $3$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Classifies E1 as achiral through an $S_4$ operation.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Classifies E5 as chiral because no cyclic shift maps every descriptor to its opposite.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** Lam, N. Y. S.; Dhankhar, J.; Lahdenpera, A. S. K.; Phipps, R. J. "Catalytic Enantioselective Hydrogen Atom Abstraction Enables the Asymmetric Oxidation of Meso Diols." *J. Am. Chem. Soc.* **2024**, *146*, 33302-33308. doi:10.1021/jacs.4c13919. Published **26 Nov 2024**, CC BY 4.0, open access and mirrored on PMC. Eight months of cutoff margin.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_oligoester_census.md](../../planck_task_oligoester_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
