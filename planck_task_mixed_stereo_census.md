# planck task — mixed-mechanism stereoisomer census (v4, SMILES representation)

**FINAL ANSWER: 18**

> **v1 PLATFORM RESULT (answer 14): 1/2.** Response 1 → **12**: on F4 it wrote *"they are not
> enantiomers"* and counted only exo/endo (2, not 4) — never checking that 2-substitution destroys both
> mirror planes of the norbornane cage. Response 2 → 14, correct. Per planck, 1/2 = revise for difficulty.
>
> **The confirmed live fork:** the second-layer question *"is each diastereomer itself chiral?"*.
> R1 asked it at F1 (*"neither form is a resolvable enantiomeric pair"* — correct), then never asked it
> again at F4. The question was in inventory, applied once, skipped under the cage's visual complexity.
> Fourth instance of the attention-distribution mechanism.
>
> **v2 change:** one added compound (new F6, 3-methylcyclohexan-1-ol = 4) transplanting the same
> second-layer skip into the plainest possible clothing, placed away from its 1,4-twin so pattern-matching
> "another ring alcohol → cis/trans → 2" is available. Everything else untouched — the fork that bit is
> not made more prominent (optional forks kill; mandatory forks instruct).
>
> ---
>
> **v2 PLATFORM RESULT (answer 18): 1/2, by cancellation.** R1 → **16**: F4 chirality-skip again
> (*"Each is achiral."*), everything else right. R2 → **18 by error cancellation**: F4 wrong the same way
> (−2, *"Each is achiral here"*) **and** F1 wrong (+2, *"neither has an internal symmetry element that
> collapses an enantiomeric pair"* — false: the 1,4-mirror contains both substituted carbons). Right
> answer, so no failure under planck rules. **F4 has now bitten 3 of 4 responses across two runs.**
>
> **Two lessons.** (1) F6 was bypassed, not survived: both responders got 4 via stereocentre counting,
> a clean alternative route that never asks the second-layer question. The skip-catch bites only where
> that route is blocked — F4's cage couples the centres; F6's ring does not. (2) The audit defense
> "cancellation requires contradictory beliefs" is empirically dead: R2 held both beliefs, because
> solvers apply local slogans per case, not consistent frameworks. F6's "different substituents → no
> meso → 4" slogan contaminated F1. Only magnitude asymmetry defends against cancellation.
>
> **v4 change (structural finding):** compounds now given as SMILES in backticks, not IUPAC names in math mode, per the Chemistry-domain representation requirement. Constitutions and all counts unchanged. Every string re-parsed and re-screened: formulas C6H12O2, C7H16O, C8H14O6, C7H12O, C6H15N, C7H14O, C7H12, C6H10; counts 2, 1, 3, 4, 1, 4, 2, 1.
>
> **v3 change:** F1 swapped to **cyclohexane-1,4-diol** (`OC1CCC(O)CC1`) (count unchanged at 2, sum unchanged at 18).
> Identical substituents make the imported slogan inapplicable, closing the +2 channel that rescued R2.
> F4's −2 is now unpartnered: the same pair of responses under v3 scores 2/2 (16 and 16).

**Subdomain: Chemistry - Organic**

**Source:** none. All eight compounds are chosen for this problem; no compound, measurement or claim is taken from any paper, so there is no cutoff exposure. Every principle used is textbook.

---

## THE LEVER — EIGHT COMPOUNDS, NO SHARED GOVERNING PRINCIPLE

This task is built on the one property shared by the census that scored **2/2 twice** (`stereogenic_census_v2`) and absent from every census that was solved.

**What kills: having to choose which test applies.** The scoring set mixed anilides, an imide, a biaryl and plain 2,3-dibromobutane. No single rule covers it, so the solver must decide *per compound* which question to ask. That is where attention fragmented — one response stated the both-ends criterion correctly, applied it at the nitrogen end of the imide, and never thought to run it against the biaryl in the same list.

**What fails: a themed set.** `cumulene_census` (answer 13) re-used the same predicate in seven costumes and was solved 2/2. Both responses opened by writing out the complete rule block unprompted — *"Use these rules:"*, *"Use these stereochemical facts:"* — then walked the compounds mechanically. Identical signature to `annulene_quadrant`, solved 3/3. **Structural variety is not diversity if one sentence resolves every case.** That is the sibling of the parameter-list law: a shared *governing rule* hands over the axis of variation just as a shared *parameter column* does.

Accordingly no two compounds here are decided by the same principle:

| | compound | the question that decides it | count |
|---|---|---|---|
| F1 | cyclohexane-1,4-diol | can a ring carry cis/trans isomers with no stereocentre at all? | **2** |
| F2 | 2,4-dimethylpentan-3-ol | are those two branches constitutionally identical? | **1** |
| F3 | ethane-1,2-diyl bis(2-hydroxypropanoate) | are the two halves related by an internal operation? | **3** |
| F4 | bicyclo[2.2.1]heptan-2-ol | are the bridgehead configurations independent, or fixed by the cage? | **4** |
| F5 | N-ethyl-N-methylpropan-1-amine | is that pyramidal centre configurationally stable? | **1** |
| F6 | 3-methylcyclohexan-1-ol | does any mirror plane survive in either diastereomer? | **4** |
| F7 | 3-methylcyclohex-1-ene | is a trans double bond possible in a ring that size? | **2** |
| F8 | 4-methylpenta-2,3-diene | are both ends of the axis dissymmetric? | **1** |

A solver cannot write a preamble that answers this set. Each entry requires recognising which of the unrelated stereochemical questions is the live one, and every other question is irrelevant to the compound at hand. The one deliberate near-repeat, F1/F6, differs in outcome — the same surface pattern demands opposite verdicts, so even that pair cannot be resolved by a single slogan.

**F4 is the primary catch and carries the A17 lever.** The bridgehead carbons C1 and C4 are the *undecorated* framework, and their configurations are fixed by the cage — only the exo/endo choice at C2 is free. Counting them as independent stereocentres is exactly the error RDKit itself makes on this scaffold class, which is direct evidence of how natural it is.

---

## PROMPT

```
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours, counting enantiomers as distinct stereoisomers. Report the sum of the eight numbers as a single integer.

F1: `OC1CCC(O)CC1`

F2: `CC(C)C(O)C(C)C`

F3: `CC(O)C(=O)OCCOC(=O)C(C)O`

F4: `OC1CC2CCC1C2`

F5: `CCCN(C)CC`

F6: `OC1CCCC(C)C1`

F7: `CC1CCCC=C1`

F8: `CC=C=C(C)C`

Each SMILES string specifies the full constitution and carries no stereochemical information; take each compound to have exactly the constitution shown: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely at $25\,^\circ\mathrm{C}$ over a period of hours, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
```

---

## GOLDEN

**Step 1.** Count a structure as a separate stereoisomer only if it is isolable at $25\,^\circ\mathrm{C}$ over hours and does not interconvert freely with another on that timescale.

**Step 2.** An $\mathrm{sp}^3$ carbon is a stereocentre only when its four substituents are all different.

**Step 3.** Enantiomers are counted as two, as stated.

---

**Step 4.** F1: each substituted ring carbon is attached to H, OH and two ring paths that are identical, since the other hydroxyl sits at the opposite position, so neither is a stereocentre.

**Step 5.** F1 therefore has no stereocentre, but the two substituents can still sit on the same face or on opposite faces of the ring, giving cis and trans diastereomers.

**Step 6.** Each of those is achiral, having a mirror plane through the two substituted carbons, so neither adds an enantiomer. **F1 = 2.**

**Step 7.** F2: C3 carries OH, H and two isopropyl groups, which are constitutionally identical, so C3 is not a stereocentre.

**Step 8.** F2's C2 and C4 each carry two identical methyl groups, so neither is a stereocentre either, and no other element is present. **F2 = 1.**

**Step 9.** F3: each of the two lactate units carries a stereocentre at its CH(OH) carbon, giving four label combinations.

**Step 10.** F3's two halves are constitutionally identical and are exchanged by an internal operation across the symmetric $-\mathrm{OCH_2CH_2O}-$ linker, so the two mixed combinations are one achiral meso compound.

**Step 11.** F3 therefore has the (R,R)/(S,S) enantiomeric pair plus that meso form. **F3 = 3.**

**Step 12.** F4: the carbon bearing OH may have that OH on the exo or the endo face, which is a genuine choice.

**Step 13.** F4's two bridgehead carbons cannot be inverted independently — their configurations are imposed by the bicyclic framework, since inverting one would require breaking a bond.

**Step 14.** F4's substitution at C2 destroys both mirror planes of the parent cage, so each of the exo and endo diastereomers is chiral and exists as an enantiomeric pair. **F4 = 4.**

**Step 15.** F5: the nitrogen carries methyl, ethyl and propyl, three different groups, plus a lone pair, so it is a pyramidal centre with four different "substituents".

**Step 16.** F5's nitrogen nevertheless inverts through a planar transition state many times per second at $25\,^\circ\mathrm{C}$, so the two pyramidal forms interconvert freely and count as one species by Step 1. **F5 = 1.**

**Step 17.** F6: the ring bears OH at C1 and methyl at C3, so, as in F1, the two substituents may sit on the same face or on opposite faces, giving cis and trans diastereomers.

**Step 18.** F6, unlike F1, retains no internal mirror plane in either diastereomer: the only ring reflection that exchanges C1 and C3 would require the two substituents to be identical, and they differ, while every other reflection carries the methyl onto an unsubstituted carbon.

**Step 19.** Each F6 diastereomer is therefore chiral and exists as an enantiomeric pair. **F6 = 4.**

**Step 20.** F7: C3 carries a methyl, an H, and two different ring paths — one reaching the double bond in one bond, the other in three — so it is a stereocentre and gives an enantiomeric pair.

**Step 21.** F7's ring double bond cannot adopt a trans configuration, a six-membered ring being far too small to span it, so it contributes no further isomers. **F7 = 2.**

**Step 22.** F8: the axis has two cumulated double bonds, so its two ends are perpendicular and axial chirality is possible in principle.

**Step 23.** F8's $\mathrm{(CH_3)_2C{=}}$ end carries two identical methyl groups, so a $180^\circ$ turn about the axis regenerates the same structure and the axis is not stereogenic. **F8 = 1.**

**Step 24.** Sum the eight counts: $2 + 1 + 3 + 4 + 1 + 4 + 2 + 1$.

**Final Answer: 18**

---

## WRONG BRANCHES AND COLLISION AUDIT

Deltas from 18:

| misjudgment | affected | delta |
|---|---|---|
| bridgehead carbons treated as independent stereocentres | F4 → 8 | **+4** |
| **the observed v1 failure**: diastereomers found, chirality of each never checked | F4 → 2 | **−2** |
| the same skip on the plain ring alcohol ("another cis/trans pair") | F6 → 2 | **−2** |
| substituted ring carbons read as stereocentres — blocked in v3: identical substituents make the slogan inapplicable | F1 → 4 | (+2, closed) |
| the two isopropyl branches read as different | F2 → 2 | +1 |
| meso relationship missed | F3 → 4 | +1 |
| pyramidal nitrogen treated as configurationally stable | F5 → 2 | +1 |
| the allylic stereocentre missed | F7 → 1 | −1 |
| the dead axis counted as stereogenic | F8 → 2 | +1 |

The v1 responder's exact route (chirality layer skipped at the cage) now costs −2 at F4 **and** −2 at F6, landing on 14 — four away from the truth, with no compensating error available in the same belief system: a solver who skips the chirality check on diastereomers cannot simultaneously invent extra enantiomer pairs elsewhere.

**Cancellation, after v3.** The F1(+2)/F4(−2) channel fired in a real v2 response — proof that "requires contradictory beliefs" is no defense, since solvers apply local slogans per case rather than consistent frameworks. v3 closes it by making F1's substituents identical, so the slogan that generated the +2 ("different substituents mean no collapse") has no purchase. Remaining pairs: F2 (+1) against F7 (−1) requires reading two identical branches as different and two different ring paths as identical; F5 (+1) against F7 (−1) requires a nitrogen treated as configurationally stable alongside a missed allylic stereocentre. Both are ±1 side-channels; the dominant catches (F4 at −2 skip / +4 bridgehead, twice bitten) have no partner of matching magnitude.

**The F1/F6 pair after the swap.** Both are disubstituted cyclohexanes with cis and trans forms; F1 (1,4, identical substituents) gives 2 and F6 (1,3, different substituents) gives 4. The surface still invites "another ring diol/alcohol → cis/trans → 2", which loses 2 at F6 for a solver who never asks the chirality question there — though v2 showed most reach F6's 4 by stereocentre counting instead. F6's remaining role is heterogeneity and the −2 skip channel; the load-bearing catch is F4.

---

## VERIFICATION

Ground truth is hand-derived per compound in Steps 4–20, each in two or three sentences, checkable by inspection.

Independently screened with RDKit for the seven atom-centred cases (F1–F7), which returned 2, 1, 3, 4, 1, 4, 2 — matching the hand derivation on every one, cyclohexane-1,4-diol included, including F4, where the enumeration correctly filters bridgehead inversions once geometric embedding is required.

**F8 is hand-derived only, deliberately.** RDKit's stereo model is atom-centred and unreliable for axial chirality: it returns 1 stereoisomer for spiro[3.3]heptane-2,6-diol and 1 for spiro[5.5]undecane-3,9-diol, both of which are classic axially chiral spiranes. InChI shares the same model and reproduces the error, so agreement between them is not independent confirmation. F8's count rests on Steps 22–23, not on any library.

**F5 likewise rests on the inversion argument plus the prompt's interconversion clause**, not on software, since cheminformatics tools do not model nitrogen inversion kinetics.

---

## COMPLIANCE

- **Self-contained**: constitutions are given as unambiguous IUPAC names; the temperature, the timescale, the treatment of freely interconverting structures, the enantiomer convention and the achiral-solvent condition are all stated. No barrier, constant or conversion is required — the nitrogen case is settled by the general interconversion clause, which names no process.
- **No governing rule given**: none of the deciding principles appears in the prompt.
- **Nothing advertised**: the prompt contains no occurrence of chirality, axial, symmetry, mirror, meso, stereocentre, stereogenic, bridgehead or inversion. It names eight compounds and asks for a count. "Enantiomers" appears once, in the counting convention, which is required for unambiguity and appeared in the same role in the 2/2-scoring task.
- **No shared rule block**: eight compounds, seven distinct deciding questions, and the single near-repeat pair (F1/F6) resolves in opposite directions. A preamble of rules cannot be written for this set — the property that separates the scoring census from every solved one.
- **No tabulable parameter (A18)**: nothing varies along a single axis; there is no column, series or sequence.
- **CURVD**: Contained; Unambiguous; Reduced; Verifiable; Discrete (18).
- **Deductive ground truth**: counts under stated idealisations, not contested empirical claims.
- **Timeless, no PII, no citations, no cutoff exposure.**

## STATUS

Built 2026-07-31. Ground truth hand-derived and independently screened; collision audit complete and monotone. **Not cold-probed, deliberately** — probe outcomes were shown today to predict platform outcomes in neither direction.
