# planck task — rotaxane chirality census v2

**Supersedes** `planck_task_rotaxane_chirality.md` (v1, answer 9, scored **1/2** on platform).

**FINAL ANSWER: 16**

**Prompt chars: 1890 / 2000**

**Source inspiration:** Yu, W.; Yang, Z.; Yu, C.; Li, X.; Yuan, L. Beilstein J. Org. Chem. **2025**, 21, 179-188. doi:10.3762/bjoc.21.10 (published 17 Jan 2025, CC BY 4.0). Borrowed: the *idea* of a head-to-tail hydrogen-bonded aromatic-amide macrocycle threaded by a directional guest. No number, compound, measurement or claim from the paper is used. Full source statement in `planck_task_rotaxane_v2_sources.md`.

---

## WHY v2 EXISTS — v1 platform post-mortem

v1 asked for 16 rotaxanes (4 macrocycles x 4 dumbbells), answer 9. Two responders differed on **exactly one case, M4A3**:

- Responder 1 -> M4A3 achiral -> **8** (wrong). It carried ONE boolean per component ("M4 is achiral") instead of two. A3's achirality is rescued only by sigma_h (the ring mean plane, which swaps the axle ends and maps R -> S). M4 has no sigma_h — the responder had already derived that fact ("the strap makes the faces different") and never propagated it. Chain-local reasoning, no global consistency check.
- Responder 2 -> M4A3 chiral -> **9** (correct). It named the operation: "the R,S axle would need a symmetry that swaps the two ends, but the one-face strap destroys the mirror plane through the macrocycle plane."

The failure is a **valid conceptual error** (not arithmetic), so v1 = 1/2 = planck "revise for difficulty".

**Root cause of v1's weakness:** the shortcut *"chiral iff a component is intrinsically chiral"* is correct in 14 of v1's 16 cases. Its only two exceptions were M1A2 (the canonical textbook mechanically-planar-chiral rotaxane — recalled, not derived) and M4A3. So v1 contained exactly **one non-canonical exception**, i.e. one coin flip. 1/2 is the expected score.

**v2 design principle:** adding more exceptions of the *same kind* does not help — they are correlated by framework (Responder 2's framework gets all sigma_v/sigma_h exceptions at once). v2 instead adds exceptions that **kill different frameworks**, so that no single framework survives the whole grid.

---

## PROMPT

```
All 30 [2]rotaxanes obtained by threading one of six macrocycles $M1$-$M6$ onto one of five dumbbells $A1$-$A5$ are isolable.

$M1$-$M5$ are rings of six 1,3-disubstituted benzene residues joined by six secondary amide bonds.
$M1$: every residue is a 3-aminobenzoyl unit, so all six $\mathrm{C(O)NH}$ linkages point the same way round the ring; no further substituents.
$M2$: three isophthaloyl and three benzene-1,3-diamine residues alternate, so the amides meet head-to-head and tail-to-tail; no further substituents.
$M3$-$M5$: as $M2$, plus one $-\mathrm{CH_2OCH_2}-$ strap joining the 5-positions of two residues and arching over one face; the strap cannot reach the other face. The two strapped residues are diametrically opposite in $M3$, in a 1,3-relationship in $M4$, and adjacent in $M5$.
$M6$: as $M1$ but built from eight such residues and eight amides, with the eight benzene rings locked alternately above and below the mean plane of the ring.

Each dumbbell has the core $-\mathrm{O(CH_2)_6O}-$ bearing two end groups, with $\mathrm{Ar}=3,5$-di-tert-butylphenyl, $\mathrm{Ad}=1$-adamantyl, $\mathrm{Bin}=1,1'$-binaphthalen-2-yl.
$A1$: $-\mathrm{CH_2Ar}$ at both ends.
$A2$: $-\mathrm{CH_2Ar}$ at one end, $-\mathrm{CH_2Ad}$ at the other.
$A3$: $-\mathrm{CH(CH_3)Ar}$ at both ends, one $(R)$ and one $(S)$.
$A4$: $-\mathrm{CH(CH_3)Ar}$ at both ends, both $(R)$.
$A5$: $-\mathrm{CH_2Bin}$ at both ends, one $(R_a)$ and one $(S_a)$.

Assume free rotation about all single bonds, planar trans-amides, no atropisomerism other than the specified binaphthyl axes, no inversion of the alternation in $M6$, and free shuttling and pirouetting of the macrocycle, which cannot pass over an end group. A rotaxane counts as achiral if any accessible conformation/co-conformation is superimposable on its mirror image.

How many of the 30 rotaxanes are chiral? Answer with a single integer.
```

---

## GOLDEN

**Framework.** Any symmetry operation of a [2]rotaxane must map each component onto itself and preserve the axle axis. The improper operations that can do so split into exactly two classes:

- **Class V** — sigma_v, a mirror plane *containing* the axle axis. Keeps each stopper on its own side and each ring face on its own side. Requires: macrocycle has sigma_v **and** the axle has a mirror plane containing its own axis.
- **Class H** — sigma_h (the ring mean plane) and every S_n about the ring axis (S_n = C_n . sigma_h). All of these **swap the two axle halves and the two ring faces**. Requires: macrocycle maps onto itself under sigma_h *or some S_n* **and** the axle's two ends are exchangeable by an improper operation. (The C_n part is absorbed by free pirouetting; achirality only needs *some* accessible co-conformation.)

Proper operations (C_2 in-plane, rotations about the axis) are irrelevant.

> **achiral iff (mac has sigma_v AND axle has sigma_v) OR (mac is class-H-symmetric AND axle ends improperly exchangeable)**

**Macrocycle analysis** — write (v, h):

- **M1** head-to-tail hexa-amide. Going round the ring every amide reads N->C in one sense; any sigma_v reverses that sense, so it is constitutionally forbidden. Planar, two equivalent faces -> sigma_h. **(F, T)**, point group C6h — achiral but *orientated*.
- **M2** alternating diacyl/diamine. The three vertex mirror lines through opposite residue pairs map acyl onto acyl and amine onto amine and preserve the amide pattern -> sigma_v. Planar -> sigma_h. **(T, T)**, D3h. Note it has only *vertex* mirrors; edge mirrors would map acyl onto amine and do not exist.
- **M3** = M2 + strap across two **diametrically opposite** residues. The vertex mirror through those two residues fixes both and leaves the strap on its own face -> sigma_v survives. One-face strap kills sigma_h and i. **(T, F)**.
- **M4** = M2 + strap across a **1,3** pair. Both strapped residues are the same type; the vertex mirror through the residue *between* them **swaps** 1 and 3 and maps the strap onto itself -> sigma_v survives. **(T, F)**. This is the case that punishes "the mirror must fix the strapped residues".
- **M5** = M2 + strap across **adjacent** residues. Pairing two adjacent residues requires an *edge* mirror, and the alternating ABABAB pattern has none. Checked against all three vertex mirrors: through (1,4) sends 1-2 -> 1-6; through (2,5) sends 1-2 -> 3-2; through (3,6) sends 1-2 -> 5-4. All fail. sigma_h dead by the one-face strap; i sends 1-2 -> 4-5; S_3 sends 1-2 -> 3-4. **(F, F) — M5 is an intrinsically chiral macrocycle**, from the same base ring and the same strap as M3 and M4.
- **M6** orientated **octa**-amide, aryl rings locked alternately above/below the mean plane. sigma_v killed by orientation. sigma_h killed by the alternation. i sends residue 1 (up) to position 5 (up) with a face flip -> mismatch, absent. But **S_8 = C_8 . sigma_h survives**: C_8 preserves the amide sense, and the reflection converts residue 1 (up) into position 2, which is down. **(F, T)** — achiral, and class-H-symmetric, but its *only* improper operation is S_8.

**Dumbbell analysis** — write (v, imp). A stereocentre or a chiral axis can never lie on a mirror plane, so any axle carrying one has no sigma_v.

- **A1** identical achiral ends: sigma_v yes; ends exchanged by the midpoint mirror. **(T, T)**
- **A2** different stoppers: sigma_v yes; ends not exchangeable at all. **(T, F)**
- **A3** (R) and (S) ends, constitutionally identical = meso axle: no sigma_v; the midpoint mirror exchanges the ends *and* converts R into S. **(F, T)**
- **A4** (R),(R): no sigma_v; the two ends are exchanged only by a **proper** C2 — a mirror would demand R opposite S. Chiral axle. **(F, F)**
- **A5** (Ra) and (Sa) binaphthyl ends: axial rather than central chirality, same predicate as A3. **(F, T)**

**30-case grid** (chiral cases listed):

| ring | (v,h) | chiral with | n |
|---|---|---|---|
| M1 | (F,T) | A2, A4 | 2 |
| M2 | (T,T) | A4 | 1 |
| M3 | (T,F) | A3, A4, A5 | 3 |
| M4 | (T,F) | A3, A4, A5 | 3 |
| M5 | (F,F) | all five | 5 |
| M6 | (F,T) | A2, A4 | 2 |

**Total chiral = 2 + 1 + 3 + 3 + 5 + 2 = 16.**

---

## THE TWO NEW FORKS, AND WHY THEY KILL OPPOSITE FRAMEWORKS

| case | component-shortcut (killed v1's Responder 1) | two-mirror predicate (saved v1's Responder 2) | truth |
|---|---|---|---|
| M3A3, M4A3, M4A5, M3A5 | achiral (wrong) | chiral (right) | chiral |
| M6A1, M6A3, M6A5 | achiral (right) | chiral (wrong) | achiral |
| M5A1, M5A2 | chiral (right, if M5 spotted) | chiral only if M5's sigma_v loss is spotted | chiral |

- **M6 (the S_8 fork)** punishes exactly the framework that *survived* v1. A responder who enumerates only sigma_v and sigma_h concludes M6 is an intrinsically chiral macrocycle and calls all five M6 rotaxanes chiral. Truth: S_8 does sigma_h's job, so M6 behaves identically to M1. Cost of the miss: **+3**.
- **M5 (the strap-position fork)** punishes anyone who has memorised "one-face strap -> face-dissymmetric" as a single rule with a single consequence. M3, M4 and M5 are the *same base ring with the same strap in three different positions*, and only the adjacent one is chiral. There is no slogan available; it has to be done by checking the three vertex mirror lines. Cost of the miss: **-2**.
- The **1,3 case (M4)** is the sub-trap inside the split: its mirror does not fix the strapped residues, it *swaps* them. Responders who require the strapped pair to lie on the mirror line call M4 chiral (**+2**).
- The magnitudes are deliberately unequal (+3 vs -2 vs +2) so the two headline errors cannot cancel.

---

## WRONG BRANCHES (all verified by script)

| value | route |
|---|---|
| **10** | pure component-shortcut: only M5 (chiral ring) and A4 (chiral axle) generate chirality; no emergent mechanical chirality at all |
| **11** | as above plus the recalled canonical case M1A2 |
| **14** | component-shortcut with M6 also misread as a chiral macrocycle (S_8 missed) |
| **14** | correct framework but M5 credited with sigma_v (adjacent strap assumed equivalent to the other two) |
| **15** | component-shortcut + M6 misread + M1A2 recalled |
| **17** | correct framework except M2A2 called chiral (unsymmetrical axle assumed sufficient) |
| **18** | correct framework except M4 called chiral (requires the mirror to *fix* the strapped residues rather than swap them) |
| **19** | **the two-mirror framework — v1's winning framework — run cleanly on v2**: M6 misread as chiral |
| **20** | "any one-face strap makes the ring chiral": M3 and M4 both misread |
| **22** | A3 and A5 read as chiral axles (meso relationship between the two ends missed) |
| **23** | one-face-strap error + M6 error together |
| **25** | axle symmetry ignored: every ring lacking sigma_v or sigma_h taken to give chiral rotaxanes throughout |

Note **19**: the framework that scored correct on v1 now lands 3 off.

---

## INDEPENDENT VERIFICATION (main thread)

1. **Predicate derived from scratch**, not inherited: the two improper-operation classes above, with S_n folded into class H because S_n = C_n . sigma_h and the sigma_h factor is what swaps axle ends.
2. **Component symmetry checked case by case**, in particular:
   - M2 has vertex mirrors only (ABABAB admits no edge mirror) — this is what makes the three strap positions inequivalent.
   - M3 (opposite) mirror *fixes* both strapped residues; M4 (1,3) mirror *swaps* them; M5 (adjacent) has no surviving mirror. All three explicitly tested against all three vertex mirrors plus sigma_h, i and S_3.
   - M6: S_8 present, sigma_v/sigma_h/i all absent. i checked explicitly (residue 1 up -> position 5 up, face flip mismatches). An **eight**-residue ring was chosen over four so that (a) the cavity is large enough for the -O(CH2)6O- axle to be chemically plausible and (b) S_8 is far less recognisable than the textbook S_4 case.
3. **Grid computed by script** over the 6x5 predicate table -> 16.
4. **Anchors pass**: M1A2 reproduces the textbook mechanically planar chiral rotaxane; M2A2 reproduces the standard achiral negative control; M1A3 and M1A5 are meso rotaxanes. The predicate is not tuned to the answer.
5. **Collision audit**: every subset of eight plausible component misreads was enumerated and its total computed (see `scratchpad/v2b.py`).

## RESIDUAL RISK (documented, not hidden)

The audit found that the answer 16 is reachable by three misread *pairs*: {M5 keeps sigma_v} combined with any one of {M4 chiral}, {M3 chiral}, {M2 lacks sigma_h}. Each pair is a -2 error cancelling a +2 error.

This cancellation is **structural** — flipping a macrocycle's sigma_v bit always costs exactly (number of axles with sigma_v) = 2, so any two opposite sigma_v misreads cancel in any pure census of this form. It cannot be designed away without abandoning the single-integer format.

It is mitigated rather than eliminated, on the grounds that the two halves of each pair are **contradictory beliefs**: "M5 keeps sigma_v" requires believing the ring has more mirror lines than it does (edge mirrors), while "M3/M4 is chiral" requires believing it has fewer (only strap-fixing mirrors). A responder holding both simultaneously is being inconsistent within one derivation. The natural single-error versions land on 14 and 18 respectively, both clean.

The M6 fork (+3) has **no** cancelling partner anywhere in the audit.

## COMPLIANCE

- **Self-contained**: all six macrocycles and all five dumbbells fully specified by constitution and configuration; Ar, Ad, Bin defined inline; every idealisation stated once (free single-bond rotation, planar trans-amides, no atropisomerism beyond the binaphthyl axes, locked M6 alternation, free shuttling/pirouetting, no passage over an end group, achirality criterion).
- **No governing rule given**: the prompt states no symmetry criterion, no chirality rule, no group theory, and never mentions mechanical planar chirality. The predicate is exactly what has to be derived.
- **CURVD**: Contained (one question); Unambiguous (every component property is constitutional or configurational, hence conformation-independent; all opposite pairs, all 1,3 pairs and all adjacent pairs are rotation-equivalent in the ABABAB ring, so "two residues" is well defined in each case); Reduced (one integer); Verifiable (predicate table + script, both reproduced above); Discrete (integer, no rounding).
- **Timelessness / cutoff / PII**: no dates, citations, authors or post-2025-07-31 content. Mechanically interlocked stereochemistry and cyclic aramide macrocycles are long-established.
- **Not contrived**: cyclo[n]aramides, strapped macrocycles, binaphthyl stoppers and adamantyl stoppers are all standard rotaxane building blocks.

## STATUS

Verified, not cold-probed (standing directive). Ready to bundle.
