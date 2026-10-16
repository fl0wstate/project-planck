# Author review: pentalene_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/pentalene_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Pentalene's carbon skeleton is the bicyclic graph $P$ on eight vertices $C_1,\dots,C_8$ with edges $C_1C_2$, $C_2C_3$, $C_3C_4$, $C_4C_5$, $C_5C_6$, $C_6C_7$, $C_7C_8$, $C_8C_1$, and the ring-fusion edge $C_4C_8$ (two fused five-membered rings; $C_4$ and $C_8$ bear no hydrogen, the other six carbons bear one H each).

Construct substituted hydrocarbons as follows: choose two distinct H-bearing carbons $C_i$ and $C_j$ with $i,j \in \{1,2,3,5,6,7\}$ and attach to each one exocyclic $sp^2$ CH$_2$ carbon through a single C–C bond (each exocyclic carbon is bonded to its attachment carbon only). The conjugated $\pi$ system then comprises 10 centers (8 skeletal + 2 exocyclic), each contributing one $p_z$ orbital and one $\pi$ electron. Two attachment pairs $\{i,j\}$ and $\{k,l\}$ describe the same constitutional isomer if and only if some automorphism of the skeleton graph $P$ maps $\{i,j\}$ onto $\{k,l\}$.

Treat each symmetry-distinct isomer at the simple Hückel level: MO energies $E_m = \alpha + x_m\beta$ with $\beta < 0$, where $x_1 \ge x_2 \ge \cdots \ge x_{10}$ are the eigenvalues of the 10-center adjacency matrix. A Kekulé structure is a perfect matching of the 10-vertex $\pi$-bond graph. Place the 10 $\pi$ electrons by aufbau; the ground configuration is closed-shell if and only if $x_5 > x_6$ strictly (five doubly occupied MOs energetically separated from all vacant MOs).

Question: exactly how many symmetry-distinct constitutional isomers possess no Kekulé structure whatsoever and yet have a closed-shell Hückel ground configuration?

Give your answer as a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$1$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Automorphism group of $P$.** Only $C_4$ and $C_8$ have degree 3, so every automorphism preserves $\{C_4, C_8\}$. Exhaustive check gives the Klein four-group of order 4: identity; the $C_2$ rotation $(1\,5)(2\,6)(3\,7)(4\,8)$; the flip $(1\,7)(2\,6)(3\,5)$ fixing 4 and 8; the flip $(1\,3)(5\,7)(4\,8)$ fixing 2 and 6.

**Step 2 — Orbit count.** The $\binom{6}{2}=15$ unordered pairs from $\{1,2,3,5,6,7\}$ fall into 6 orbits under this group (Burnside: $(15+3+3+3)/4 = 6$), with representatives $\{1,2\}, \{1,3\}, \{1,5\}, \{1,6\}, \{1,7\}, \{2,6\}$.

**Step 3 — Kekulé screen.** In any perfect matching of the 10-vertex graph, each pendant CH$_2$ carbon must be matched along its unique bond, saturating $C_i$ and $C_j$. Hence a Kekulé structure exists iff $P-\{C_i,C_j\}$ (6 vertices) has a perfect matching. Checking representatives: $\{1,2\}$: 3–4, 5–6, 7–8 ✓. $\{1,5\}$: 2–3, 4–8, 6–7 ✓. $\{1,6\}$: 2–3, 4–5, 7–8 ✓. $\{1,7\}$: 2–3, 5–6, 4–8 ✓. $\{1,3\}$: $C_2$ loses both neighbors — isolated vertex, no matching ✗. $\{2,6\}$: forced 1–8 and 3–4 leave $C_5$ unmatchable ✗. Exactly two non-Kekulé classes: $\{1,3\}$ and $\{2,6\}$.

**Step 4 — Spectrum of the $\{2,6\}$ isomer.** Zero-eigenvector (neighbor-sum-zero) analysis: the pendant equations force $c_2 = c_6 = 0$; propagation leaves two independent solutions — nullity 2, a degenerate nonbonding pair at $x=0$. With four strictly bonding MOs below, the 10 electrons give $x_5 = x_6 = 0$: open shell (this is the tetramethyleneethane-like diradical motif of 2,5-linked pentalene couplers). Fails the closed-shell condition.

**Step 5 — Spectrum of the $\{1,3\}$ isomer.** The pendant equations force $c_1 = c_3 = 0$, and propagation around the odd rings kills all but one independent zero-mode: nullity 1 — not the value $n - 2m = 10 - 8 = 2$ predicted by the Longuet-Higgins count, because $P$ contains five-membered rings and the pairing theorem does not apply to non-alternant systems. Solving the characteristic polynomial (block-diagonalized by the surviving mirror symmetry $(1\,3)(5\,7)(4\,8)$): sorted eigenvalues $2.446, 1.575, 1.357, 0.515, 0.477, 0.000, -0.739, -1.525, -2.095, -2.000$. Thus $x_5 = +0.477 > x_6 = 0.000$ strictly: five bonding MOs hold all 10 electrons — closed shell, despite the absence of any Kekulé structure.

**Step 6 — Count.** Non-Kekulé AND closed-shell: only $\{1,3\}$.

**Final Answer:** $1$
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $1$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Identifies $\{1,3\}$ and $\{2,6\}$ as exactly the two non-Kekulé substitution classes.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Finds zero-mode nullity $2$ for the $\{2,6\}$ isomer, excluding it as open-shell.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Longuet-Higgins, H. C. *J. Chem. Phys.* **1950**, 18, 265–274. doi:10.1063/1.1747618 — NBMO counting in alternants (the rule whose applicability limit is the gate). *Required: False.*
2. Borden, W. T.; Davidson, E. R. *J. Am. Chem. Soc.* **1977**, 99, 4587–4594. doi:10.1021/ja00456a010 — disjoint/non-disjoint NBMO analysis. *Required: False.*
3. Santiago et al. *Chem. Sci.* **2025**, 16, 430–447. doi:10.1039/d4sc05225k (online 21 Nov 2024) — pentalene-coupled diradicals (inspiration). *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_pentalene_census.md](../../planck_task_pentalene_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
