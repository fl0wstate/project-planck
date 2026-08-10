# planck task - porphyrin atropisomer census (answer 41) — ***2/2 PLATFORM KILL***

> **PLATFORM RESULT 2026-07-31: BOTH responses failed.** Response 1 returned **55**, Response 2 returned **47**,
> against golden **41**.
>
> | | golden | R1 | R2 |
> |---|---|---|---|
> | Q1 | 5 | 5 ✓ | 5 ✓ |
> | Q2 | **10** | 16 ✗ | 16 ✗ |
> | Q3 | 2 | 2 ✓ | 2 ✓ |
> | Q4 | 16 | 16 ✓ | 16 ✓ |
> | Q5 | **8** | 16 ✗ | 8 ✓ |
> | sum | **41** | **55** | **47** |
>
> **Shared root cause — the proper rotation group was truncated from D₄ (order 8) to D₂ (order 4).** Both kept
> $C_2(z)$ and the two meso-axis $C_2$ rotations, and both dropped $C_4$, $C_4^3$ and **the two in-plane $C_2$
> axes through opposite pyrrole units**. R2 states the truncation explicitly: *"the relevant proper rotational
> symmetries are the three $C_2$ operations"*.
>
> **Q2 is where it bites (both responses).** With Ar1 at 5,10 and Ar2 at 15,20, the pyrrole-axis $C_2$
> bisecting the 5–10 and 15–20 edges swaps 5↔10 and 15↔20 — preserving aryl identity exactly — while turning
> the macrocycle over and inverting all four face labels. Stabiliser order 2, not 1. Burnside: $E$ fixes 16,
> that $C_2$ fixes the 4 states with $b_5=\neg b_{10}$ and $b_{15}=\neg b_{20}$, so $(16+4)/2 = 10$. Both
> asserted no nontrivial rotation preserves the Q2 pattern; that claim is false.
>
> **Q5, R1 only.** The meso-axis $C_2$ through 10–20 fixes those positions, swaps 5↔15 (both Ar1) and inverts
> faces, giving $(16+0)/2 = 8$. R1 declared Q5 asymmetric. R2 found this one.
>
> **Both are conceptual errors, not arithmetic slips** — every Burnside sum either response wrote is internally
> correct *given its own wrong group*. Clean planck-valid failures.
>
> **THE DESIGNED LEVER DID NOT FIRE.** The task was built expecting the face-inverting in-plane $C_2$'s to be
> omitted wholesale (predicted branch 61). Both responses *included* face inversion and reasoned about turning
> the macrocycle over explicitly. What they missed was the other half of $D_4$ — the fourfold axis and the
> pyrrole-axis $C_2$'s. Neither 55 nor 47 appears in the wrong-branch table below. **Lesson: the omission is in
> group construction generally, not in the specific "faces are exchangeable" insight.** Solvers reach for the
> operations through the *decorated* positions (meso carbons, where the substituents are) and overlook the axes
> through the undecorated framework (pyrrole units). That is a sharper and more reusable target than the
> face-inversion gap this task was designed around.
>
> **PROBE STATUS CORRECTED.** A cold probe solved this 41 in 138 s (tool_uses = 0) and it was written off as a
> non-stump. The platform then failed it 2/2. See the same reversal on
> `planck_task_stereogenic_census_v2.md` the same day. A correct probe solve does not predict a platform solve.

**FINAL ANSWER: 41**

**Prompt chars: 1653 / 2000**

**Source:** Cribbin, L.; Twamley, B.; Buga, N.; O'Brien, J. E.; Buehler, R.; Fischer, R. A.; Senge, M. O. "C-C Coupling in sterically demanding porphyrin environments." *Beilstein J. Org. Chem.* **2024**, *20*, 2784-2798. doi:10.3762/bjoc.20.234. Published **04 Nov 2024**, CC BY 4.0. Nine months of cutoff margin.

Borrowed: the concept only, that ortho-substituted meso-aryl groups on a porphyrin are rotationally frozen and generate atropisomers designated by which face each aryl points towards. No compound, yield, barrier, crystal parameter or NMR value from the paper appears.

---

## THE LEVER - a third distinct inventory

Each meso-aryl group points to one face of the macrocycle or the other, giving $2^4 = 16$ arrangements to be reduced by the symmetry of the framework. The question is which operations belong in that reduction.

**The omitted member: the in-plane $C_2$ rotations that turn the macrocycle over.** These permute the meso positions *and* simultaneously swap every alpha label to beta. A solver who reduces using only the operations that leave the two faces distinct - the $C_4$ rotation about the axis normal to the ring, optionally with the vertical mirror planes - over-counts every case.

Why this is the right shape for the lever:

- **(a) Textbook archetype.** The four atropisomers of a tetra(ortho-substituted-aryl)porphyrin, designated $\alpha\alpha\alpha\alpha$, $\alpha\alpha\alpha\beta$, $\alpha\alpha\beta\beta$ and $\alpha\beta\alpha\beta$, are standard porphyrin chemistry; Collman's picket-fence porphyrin is built on the $\alpha_4$ isomer. Adversarial QC cannot call this obscure.
- **(b) The surface points the wrong way, and unusually sharply.** Turning a molecule over is not a chemical process and carries no energetic cost, so it does not present itself as an "operation" at all. Worse, the instruction to count enantiomers as distinct directs attention towards *mirror* operations, while the omitted operations are proper *rotations*. The cue actively points away from the gap.
- **(c) Load-bearing.** Omitting them changes four of the five counts and moves the total from 41 to 61.

**No retrieval cue.** The prompt names five substitution patterns and asks for stereoisomer counts. Nothing points at symmetry operations, faces, or the act of inverting the macrocycle.

**Recall defused.** The famous case is four identical aryl groups, whose answer of 4 is memorised. It is deliberately **excluded**: had it been included, a solver whose method gives 6 would notice the clash with the remembered 4 and repair the method, learning the flip. Every case here has a mixed substitution pattern whose answer must be derived.

**Two chemical details that matter, both load-bearing for the group.**

*Inner NH.* A free-base porphyrin carries two inner NH groups that lower the framework symmetry from fourfold to twofold, which would change the group and make the counts hinge on an NH-tautomerism argument. Metalation removes the inner hydrogens and makes the fourfold framework exact.

*Axial ligation (revision 2).* The first draft specified zinc(II), which was a genuine error. Zn(II) porphyrins are commonly five-coordinate, and an axial ligand bound to one face destroys the equivalence of the two faces: the in-plane $C_2$ rotations would no longer be symmetries, since they would carry the axial ligand to the opposite face. That does not merely blur the problem, it hands the primary wrong branch a valid defence, since 61 becomes the defensible answer for a five-coordinate complex. Nickel(II) is used instead, being reliably four-coordinate and square-planar in porphyrins, and the prompt states explicitly that the metal is four-coordinate with no axial ligand. The answer is unchanged at 41.

---

## PROMPT

```
Five nickel(II) porphyrins are described below. In each, the nickel is four-coordinate and carries no axial ligand, and the macrocycle is to be taken as planar with the framework geometry of unsubstituted porphine, with the four meso positions numbered 5, 10, 15 and 20 in order around the ring, so that 5 lies opposite 15 and 10 lies opposite 20.

Every meso aryl group named below is ortho-monosubstituted and lies perpendicular to the mean plane of the macrocycle, so that its ortho substituent points towards one face of the macrocycle or towards the other. Take the barrier to rotation about each bond joining a meso carbon to an aryl group to be $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$, and rotation about every other single bond to be fast at $25\,^\circ\mathrm{C}$. A meso position bearing hydrogen offers no such choice.

$\mathrm{Ar1} = $ 2-methylphenyl, $\mathrm{Ar2} = $ 2-methoxyphenyl, $\mathrm{Ar3} = $ 2-chlorophenyl, $\mathrm{Ar4} = $ 2-bromophenyl.

Q1: $\mathrm{Ar1}$ at 5 and 15; $\mathrm{Ar2}$ at 10 and 20.

Q2: $\mathrm{Ar1}$ at 5 and 10; $\mathrm{Ar2}$ at 15 and 20.

Q3: $\mathrm{Ar1}$ at 5 and 15; hydrogen at 10 and 20.

Q4: $\mathrm{Ar1}$ at 5, $\mathrm{Ar2}$ at 10, $\mathrm{Ar3}$ at 15, $\mathrm{Ar4}$ at 20.

Q5: $\mathrm{Ar1}$ at 5, 10 and 15; $\mathrm{Ar2}$ at 20.

For each porphyrin, count the stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Disregard tautomers and any process that makes or breaks a covalent bond. Report the sum of the five counts as a single integer.
```

---

## GOLDEN

Write the state of a porphyrin as the four face labels at positions 5, 10, 15, 20. Two states are the same stereoisomer exactly when some **proper rotation** of the framework that preserves the pattern of aryl identities carries one into the other. The relevant proper rotations are:

- $C_4^k$ about the axis normal to the macrocycle: permutes the meso positions cyclically, leaves every face label unchanged;
- $C_2$ about an in-plane axis through two opposite meso positions, and $C_2$ about an in-plane axis through two opposite pyrrole units: permutes the meso positions **and inverts every face label**, because the macrocycle has been turned over.

Improper operations are excluded because enantiomers are counted as distinct.

| case | pattern | allowed proper rotations | count |
|---|---|---|---|
| Q1 | Ar1 at 5,15; Ar2 at 10,20 | $E$, $C_4^2$, both meso-axis $C_2$ | **5** |
| Q2 | Ar1 at 5,10; Ar2 at 15,20 | $E$, one pyrrole-axis $C_2$ | **10** |
| Q3 | Ar1 at 5,15; H at 10,20 | $E$, $C_4^2$, both meso-axis $C_2$; only two positions carry a choice | **2** |
| Q4 | all four aryls different | $E$ only | **16** |
| Q5 | Ar1 at 5,10,15; Ar2 at 20 | $E$, one meso-axis $C_2$ | **8** |

**Sum $= 5 + 10 + 2 + 16 + 8 = 41$.**

Worked check on Q1 by Burnside, over $2^4 = 16$ states with a group of order 4: the identity fixes 16; $C_4^2$ (positions $i \to i+2$, labels unchanged) fixes those with $c_5 = c_{15}$ and $c_{10} = c_{20}$, i.e. 4; each meso-axis $C_2$ fixes a position while inverting its label, which is impossible, so 0. Orbits $= (16 + 4 + 0 + 0)/4 = 5$.

Q4 deserves note: with four different aryl groups no non-trivial rotation preserves the pattern, so all 16 arrangements are distinct stereoisomers. They form 8 enantiomeric pairs, related by the horizontal mirror - which is why reporting 8 here is the signature of having identified enantiomers.

---

## WRONG BRANCHES (computed; no collision with 41)

| value | route |
|---|---|
| **61** | **primary**: the face-inverting $C_2$ rotations omitted; reduction by $C_4$ about the normal only |
| **68** | as above, and meso-hydrogen positions wrongly given a face choice |
| **56** | only face-preserving operations used, and meso-hydrogens mishandled |
| **50** | reduction by all face-preserving operations, i.e. $C_4$ plus the vertical mirrors |
| **44** | correct group, but the meso-hydrogen positions of Q3 wrongly given a face choice |
| **30** | enantiomers identified and meso-hydrogens mishandled |
| **27** | enantiomers wrongly identified, i.e. atropisomer counts reported instead of stereoisomer counts |

Errors run in both directions: omitting the flip over-counts, identifying enantiomers under-counts. No combination reaches 41.

---

## INDEPENDENT VERIFICATION

Script `scratchpad/porph2.py`, `porph3.py`. All sixteen operations of the idealised framework point group are represented explicitly as (position permutation, face-inversion flag, proper/improper flag). For each case the script keeps only those operations that preserve the aryl identity pattern, then computes orbits of the $2^n$ face assignments by union-find, under four different group choices: proper rotations (correct), $C_4$ only, all face-preserving operations, and the full group.

Controls that the model is right rather than merely self-consistent:

- Four identical aryl groups returns **4** under the correct group, reproducing the textbook atropisomer count, and 6 under the truncation.
- Q1 independently confirmed by hand via Burnside, above.
- Q4 returns 16 under proper rotations and 8 under the full group, the expected relationship for 8 enantiomeric pairs.

---

## COMPLIANCE

- **Self-contained** (the finding that came back on the previous task): the rotation barrier is **given** as $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$ rather than left to be assumed, along with the temperature, the timescale, the planarity and framework geometry of the core, the perpendicular orientation of the aryl groups, the meso numbering and which positions are opposite, the statement that a meso hydrogen offers no choice, and the convention that enantiomers count as distinct. Nothing load-bearing is unstated.
- **No governing rule given**: the prompt states no symmetry criterion, names no operation, and never mentions faces being exchangeable.
- **CURVD**: Contained; Unambiguous (zinc complexes remove the inner-NH symmetry question; tautomers and bond-breaking excluded explicitly; the barrier margin is decisive, $30\,\mathrm{kcal\,mol^{-1}}$ giving $t_{1/2}$ of roughly 35 years against a stated timescale of hours); Reduced; Verifiable; Discrete (41).
- **Heterogeneous cases**: five patterns with five different stabilisers, of orders 4, 2, 4, 1 and 2, and one case where two positions carry no choice at all. No single predicate covers them.
- **Deductive ground truth**: an orbit count under a stated idealised geometry.
- **Timeless, no PII, pre-cutoff**: no dates, citations or names in the prompt.

## STATUS

Verified. Not cold-probed (standing directive).
