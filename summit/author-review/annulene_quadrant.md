# Author review: annulene_quadrant

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/annulene_quadrant/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
Thirteen isolable macrocyclic $\pi$ systems are characterised below. Each is a single continuous monocyclic circuit of conjugated carbon atoms (no fused rings, no substituents, no heteroatoms); every ring atom is an sp$^2$ CH unless a saturated unit is specified, and any charge is delocalised over the whole circuit. For each entry the electronic state to be interrogated is stated: $S_0$ (closed-shell ground state) or $T_1$ (lowest triplet, EPR-characterised at 10 K).

Where a value of $\tau$ is quoted the macrocycle is non-planar, and $\tau$ is the total rotation of the local $p_z$ axis about the ring tangent accumulated on traversing the circuit once. That rotation is smooth and unidirectional, and in every non-planar case the $\pi$ circuit remains continuous and fully delocalised (overlap is attenuated, never interrupted). Treat all thirteen as idealised: neglect substituent, solvent, counter-ion and temperature effects.

1. $\mathrm{C_{18}H_{18}}$, planar, $S_0$
2. $\mathrm{C_{20}H_{20}}$, planar, $S_0$
3. $\mathrm{[C_{16}H_{16}]^{2-}}$, planar, $S_0$
4. $\mathrm{C_{12}H_{12}}$, planar, $T_1$
5. $\mathrm{C_{18}H_{18}}$, $\tau = 180^\circ$, $S_0$
6. $\mathrm{C_{16}H_{16}}$, $\tau = 180^\circ$, $S_0$
7. $\mathrm{C_{14}H_{14}}$, planar, $T_1$
8. $\mathrm{C_{22}H_{22}}$, $\tau = 360^\circ$, $S_0$
9. $\mathrm{C_{24}H_{24}}$, planar, $T_1$
10. $\mathrm{C_{19}H_{20}}$, one ring atom being a saturated sp$^3$ $\mathrm{CH_2}$ unit, planar, $S_0$
11. $\mathrm{C_{18}H_{18}}$, $\tau = 180^\circ$, $T_1$
12. $\mathrm{C_{24}H_{24}}$, $\tau = 540^\circ$, $S_0$
13. $\mathrm{[C_{15}H_{15}]^{+}}$, planar, $S_0$

In how many of the thirteen entries does the specified electronic state sustain a net diatropic ring current around the macrocyclic circuit? Report a single integer.
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
GATE (must be settled before any counting): the electron-count rule that predicts a diatropic (aromatic-type) perimeter current is not a single rule but a composition of three independent binary facts per entry — (i) the number of pi electrons in the circuit, (ii) the topology of the circuit (Huckel vs Mobius, set by the PARITY of half-twists, i.e. by tau/180 being even or odd, NOT by whether the ring is twisted), (iii) the spin of the interrogated state (Baird's rule: the count rule inverts in T1). Each of (ii) and (iii) inverts the reference Huckel-singlet rule, so

  diatropic  <=>  [ n_pi = 4n+2 ]  XOR  [ tau/180 odd ]  XOR  [ triplet ],
  and only if the cyclic conjugated circuit is unbroken.

Two inversions cancel: a Mobius triplet obeys the same 4n+2 criterion as a planar singlet.

Step 1 - pi counts. Neutral C_mH_m all-sp2 ring: m pi electrons. Charges shift the count: [C16H16]2- = 18; [C15H15]+ = 14. Entry 10 has one sp3 CH2, so the 18 sp2 carbons form an OPEN 18-pi polyene: there is no closed conjugated circuit and hence no macrocyclic ring current at all, whatever the count.
Step 2 - topology. tau = 0 or 360 deg => even number of half-twists (0 or 2) => Huckel topology (phase-continuous). tau = 180 or 540 deg => 1 or 3 half-twists, odd => Mobius topology (one phase inversion, Heilbronner). Entry 8 (tau = 360) is strongly twisted yet topologically Huckel.
Step 3 - apply the composed rule entry by entry.

 #  n_pi  n_pi mod 4  topology (tau/180)  state  inversions  criterion  verdict
 1   18      2        Huckel (0)          S0     0           4n+2       DIATROPIC
 2   20      0        Huckel (0)          S0     0           4n+2       not (paratropic/bond-alternating)
 3   18      2        Huckel (0)          S0     0           4n+2       DIATROPIC
 4   12      0        Huckel (0)          T1     1 (Baird)   4n         DIATROPIC
 5   18      2        Mobius (1)          S0     1 (Mobius)  4n         not
 6   16      0        Mobius (1)          S0     1 (Mobius)  4n         DIATROPIC
 7   14      2        Huckel (0)          T1     1 (Baird)   4n         not
 8   22      2        Huckel (2)          S0     0           4n+2       DIATROPIC
 9   24      0        Huckel (0)          T1     1 (Baird)   4n         DIATROPIC
10   18      2        circuit BROKEN      S0     -           -          not (acyclic polyene)
11   18      2        Mobius (1)          T1     2 (cancel)  4n+2       DIATROPIC
12   24      0        Mobius (3)          S0     1 (Mobius)  4n         DIATROPIC
13   14      2        Huckel (0)          S0     0           4n+2       DIATROPIC

Diatropic: entries 1, 3, 4, 6, 8, 9, 11, 12, 13 = 9. Not diatropic: 2, 5, 7, 10 = 4.

ANSWER 9.

Robustness note: the question asks only whether the current is DIATROPIC, so the antiaromatic/nonaromatic distinction for entries 2, 5, 7 (large 4n rings may bond-alternate to a nonaromatic ground state rather than remain paratropic) does not change any verdict. Rule provenance for the golden: Huckel (4n+2, closed-shell); Baird, J. Am. Chem. Soc. 1972, 94, 4941-4948 (published 19 July 1972) - 4n aromatic in T1; Heilbronner, Tetrahedron Lett. 1964, 5, 1923-1928 - 4n aromatic for a singly phase-inverted (Mobius) circuit; the full Huckel/Baird/Mobius grid, including the doubly inverted Mobius-triplet 4n+2 entry, is tabulated in M. Sola et al., "Aromaticity rules", Nature Chemistry 2022, 14, 585-590 (published 25 May 2022). Even-half-twist ("Huckel-topology twisted") macrocycles retaining 4n+2 diatropicity and triply twisted (3 half-twist) Mobius-aromatic macrocycles are both experimentally established motifs in twisted expanded porphyrins.
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
Classifies entry 8, with $360^\circ$ twist, as having Hückel topology.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Excludes entry 10 from macrocyclic ring-current counting because its $\mathrm{sp}^3$ centre breaks the conjugated circuit.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source inspiration:** Cardenas, A.; Jin, Z.; Ni, Y.; Wu, J.; Xia, Y.; Ramirez, F. J.; Casado, J. *Beilstein J. Org. Chem.* **2025**, *21*, 277-285. doi:10.3762/bjoc.21.20 (pub 05 Feb 2025, CC BY 4.0). Physics borrowed only (local vs global ring currents, Huckel bookkeeping failing in both directions); no number, compound or claim reused.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_annulene_quadrant.md](../../planck_task_annulene_quadrant.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
