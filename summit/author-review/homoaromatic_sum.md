# Author review: homoaromatic_sum

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/homoaromatic_sum/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A screening table lists six isolated, closed-shell (singlet ground state) conjugated species, each at its equilibrium geometry. For each species, decide whether its ground state sustains a net diatropic (aromatic) ring current. For every species that does, count the $\pi$ electrons delocalized in the cyclic circuit that carries that current; report the sum of those electron counts over the whole table (report $0$ if no species qualifies). Ignore counterions, solvent and temperature.

A. Nine-membered carbocycle, monoanion; all nine carbons $sp^2$, each bearing one H; planar, all-cis.

B. Twelve-membered carbocycle, dianion; all carbons $sp^2$, fully conjugated; planar.

C. Eight-membered carbocycle, monocation; one ring carbon is a saturated $\mathrm{CH}_2$ group, the other seven are $sp^2$, mutually conjugated, each bearing one H. The ring is not planar: it is folded at the $\mathrm{CH}_2$ carbon.

D. Sixteen-membered carbocycle, neutral; all carbons $sp^2$, fully conjugated; essentially planar.

E. Eighteen-membered carbocycle, neutral; saturated $\mathrm{CH}_2$ groups at ring positions 1 and 10, the remaining sixteen carbons $sp^2$ and forming two equivalent fully conjugated chains; essentially planar.

F. Nine-membered ring, neutral; one ring carbon carries an exocyclic $\mathrm{C}{=}\mathrm{O}$ group, the other eight ring carbons are $sp^2$ and each bear one H; essentially planar.

Answer with a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$30$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
Species-by-species tropicity call, then sum the pi-electron count of each diatropic circuit.

A. Nine sp2 CH carbons, monoanion = cyclononatetraenyl anion. Ring circuit: 4 C=C (8 e) + the carbanion lone pair in a p orbital (2 e) = 10 pi = 4n+2 (n=2), planar all-cis, monocyclic => strongly DIATROPIC. Contributes 10.

B. Twelve sp2 carbons, fully conjugated, dianion = [12]annulene dianion. Neutral perimeter carries 12 pi; the two extra electrons give 14 pi = 4n+2 (n=3), planar monocyclic => DIATROPIC (experimentally strongly diatropic: shielded inner, deshielded outer protons). Contributes 14.

C. THE LOAD-BEARING CASE. Eight-membered carbocyclic monocation with one saturated CH2 and seven mutually conjugated sp2 CH carbons = a homotropylium-type ion. Formal analysis: the seven sp2 carbons form a heptatrienyl (cycloheptatrienyl-like) cation fragment carrying 6 pi electrons; the sp3 CH2 interrupts through-bond conjugation, so there is no continuously conjugated cyclic array of p orbitals. The naive conclusion "not a closed conjugated cycle, and non-planar, therefore no ring current" is WRONG. Folding the ring at the sp3 carbon lifts the CH2 out of the plane of the heptatrienyl unit and brings its two termini (C1, C7) to ca. 2.0-2.3 A, giving direct through-space (homoconjugative) overlap that CLOSES the circuit: the species is a monohomoaromatic 6 pi-electron system. Archetype: the homotropylium ion (Winstein), whose diatropic ring current is one of the best-quantified in organic chemistry (the two C8 protons differ by ca. 5.8 ppm, the endo proton sitting deep in the shielding cone; NICS is strongly negative). 6 pi = 4n+2 (n=1) in a homoaromatic circuit => DIATROPIC. Contributes 6.

D. Sixteen sp2 carbons, neutral, fully conjugated, essentially planar = [16]annulene. 16 pi = 4n (n=4) => PARATROPIC (observed reversed shift pattern: deshielded inner, shielded outer protons). Contributes 0.

E. Eighteen-membered ring with sp3 CH2 groups at positions 1 and 10 and sixteen sp2 carbons in two equivalent conjugated chains (each an octatetraene segment, 8 pi). The two sp3 centres sit on opposite sides of an essentially PLANAR ring, so the chain termini are held far apart (ca. 2.5 A is impossible here; they are separated by full CH2 units across a wide, flat perimeter) and no through-space closure is available. No cyclic circuit at all => not diatropic. Even if one insisted on a homoconjugative perimeter, the count would be 16 pi = 4n, i.e. still not diatropic. Contributes 0. (This is the honest "interrupted conjugation" case, and it is why the shortcut used on C feels validated.)

F. Nine-membered ring, neutral, one ring carbon bearing an exocyclic C=O, the other eight sp2 CH carbons giving 4 C=C. The exocyclic carbonyl pi pair is orthogonal to the ring circuit in the sense that it does not enter the cyclic conjugation path; the ring circuit therefore holds 8 pi = 4n (n=2) => not diatropic (paratropic/non-aromatic). The polar oxyanion resonance form is no rescue: it would place 8 pi over nine centres, still 4n, so it is destabilizing rather than aromatizing (contrast tropone, where the same polarization gives a 6 pi tropylium circuit and IS stabilizing). Contributes 0.

Sum over diatropic species: A (10) + B (14) + C (6) = 30.
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $30$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Assigns species C a diatropic homoaromatic circuit contributing $6$ electrons.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Assigns species B a diatropic circuit contributing $14$ electrons.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source inspiration:** Cardenas, A.; Jin, Z.; Ni, Y.; Wu, J.; Xia, Y.; Ramirez, F. J.; Casado, J. *Beilstein J. Org. Chem.* **2025**, *21*, 277-285. doi:10.3762/bjoc.21.20 (pub 05 Feb 2025, CC BY 4.0). Physics borrowed only (local vs global ring currents, Huckel bookkeeping failing in both directions); no number, compound or claim reused.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_homoaromatic_sum.md](../../planck_task_homoaromatic_sum.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
