# Author review: directional_cube

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/directional_cube/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
An ideal cubic $M_8L_{12}$ coordination cage has one metal at each cube vertex and one rigid linker on every edge. Each linker is constitutionally directional: one end binds through a neutral pyridyl-N donor and the other through a monoanionic carboxylate-O donor; it has no other orientational state.

Each metal also carries the same neutral facial tridentate cap, leaving three equivalent cis sites for its incident edge linkers. An allowed capped node is either $M^{II}$ with one O and two N edge donors or $M^{III}$ with two O and one N; nodes with zero or three O donors are excluded. Donor orientations and formal valences are frozen, and no linker dissociates.

Retain only cages in which the $M^{III}$ vertices form one edge-connected domain. Count valence-linkage topologies, not conformers. Two topologies are identical exactly when a rigid rotation of the complete cube maps all N/O ends and metal valences; reflection alone is not an equivalence.

How many retained topologies exist? Report one exact integer.
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
Direct every edge toward its carboxylate-O end. Its endpoint indegree is then the number of incident O donors. An $M^{II}$ vertex has indegree 1 and an $M^{III}$ vertex has indegree 2.

If $h$ vertices are $M^{III}$, summing indegrees over the twelve directed edges gives

$$
2h+(8-h)=12,
$$

so $h=4$.

The connected four-vertex subsets of a cube and their compatible edge orientations are:

| induced $M^{III}$ domain | embedded subsets | orientations per subset | labeled states |
|---|---:|---:|---:|
| square face $C_4$ | 6 | 4 | 24 |
| corner star $K_{1,3}$ | 8 | 6 | 48 |
| skew path $P_4$ | 24 | 6 | 144 |

Thus the identity fixes $24+48+144=216$ states.

For the 24 proper rotations of the cube, the fixed-state counts are:

| rotation class | operations | fixed states per operation |
|---|---:|---:|
| identity | 1 | 216 |
| $C_4^{\pm1}$ through face centers | 6 | 8 |
| $C_2$ through face centers | 3 | 8 |
| $C_3^{\pm1}$ through opposite vertices | 8 | 0 |
| $C_2$ through opposite edge midpoints | 6 | 0 |

For a face-centered $C_4$, the two opposite face cycles may each circulate in either direction, and all four connecting edges have either common direction: $2\cdot2\cdot2=8$. For a face-centered $C_2$, connectivity again forces the four connecting edges to have one common direction, while each face has two compatible half-turn-invariant orientations, also giving 8.

A vertex-centered $C_3$ forces all three edges at each axial vertex inward or outward, producing forbidden indegree 3 or 0. An edge-centered $C_2$ exchanges the endpoints of an edge on its axis and therefore cannot preserve that linker's N/O direction.

Burnside's lemma gives

$$
\frac{216+6(8)+3(8)}{24}=\boxed{12}.
$$

The twelve proper-rotation orbits independently split into eight of size 24 and four of size 6, accounting for all 216 labeled states.
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
Derives that exactly $4$ vertices have formal valence $M^{III}$ from $2h+(8-h)=12$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $216$ labelled admissible states before quotienting by rotations.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source:** none. The cage, linker, valence rule, and connectivity condition are original idealized constructions. The underlying donor-charge bookkeeping and proper-rotation equivalence are standard coordination chemistry and molecular symmetry.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_directional_cube.md](../../planck_task_directional_cube.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
