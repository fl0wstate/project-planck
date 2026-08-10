# planck task — case-volume (planck_task_belt_census.md)

**Source inspiration:** Cardenas, A.; Jin, Z.; Ni, Y.; Wu, J.; Xia, Y.; Ramirez, F. J.; Casado, J. *Beilstein J. Org. Chem.* **2025**, *21*, 277-285. doi:10.3762/bjoc.21.20 (pub 05 Feb 2025, CC BY 4.0). Physics borrowed only (local vs global ring currents, Huckel bookkeeping failing in both directions); no number, compound or claim reused.

**FINAL ANSWER: 12**   — independently re-verified in main thread: 12

**Prompt chars: 1709 / 2000**

## PROMPT

```
A survey of 16 idealised monocyclic conjugated "belts" is carried out. In every belt each ring atom is trigonal ($sp^2$) with its p orbital normal to the local ribbon surface, and overlap is uniform all the way round the circuit (no bond-length localisation, no substituents, no ion pairing); the one exception is the saturated $sp^3$ CH$_2$ group in B16. Net charge is of $\pi$ origin throughout (electrons removed from, or added to, the conjugated circuit). Each entry lists, in order: the ring atoms as counts by type; the number of half-turns the ribbon makes before closing on itself ($0$, $1$ or $2$); the net charge; and the electronic state considered, either $S_0$ (closed-shell singlet ground state) or $T_1$ (lowest $\pi\pi^*$ triplet). Notation: N(=) = imine-type ring nitrogen (part of a ring C=N unit); N(H) = ring nitrogen bearing one H; B(H) = three-coordinate ring boron bearing one H; O = divalent ring oxygen; C(+) = H-free ring carbon of formal charge $+1$; C(-) = H-free ring carbon of formal charge $-1$.

B1: 20 CH | 0 | 0 | $S_0$
B2: 16 CH | 1 | 0 | $S_0$
B3: 18 CH | 2 | 0 | $S_0$
B4: 24 CH | 0 | 0 | $T_1$
B5: 18 CH | 0 | 0 | $S_0$
B6: 22 CH | 0 | 0 | $T_1$
B7: 20 CH | 0 | $+2$ | $S_0$
B8: 16 CH | 2 | $-2$ | $S_0$
B9: 22 CH | 1 | 0 | $S_0$
B10: 16 CH + 1 N(H) | 0 | 0 | $S_0$
B11: 16 CH + 2 N(=) | 0 | 0 | $S_0$
B12: 16 CH + 1 B(H) | 0 | 0 | $T_1$
B13: 14 CH + 1 C(-) | 1 | $-1$ | $S_0$
B14: 20 CH + 1 C(+) | 0 | $+1$ | $T_1$
B15: 14 CH + 1 O | 1 | 0 | $S_0$
B16: 18 CH + 1 $sp^3$ CH$_2$ | 0 | 0 | $S_0$

In how many of these 16 belts does the state specified sustain a net diatropic (diamagnetic) ring current around the complete macrocyclic circuit? Answer with a single integer.
```

## GOLDEN

Four independent decisions per belt: (i) is the circuit continuous? (ii) how many pi electrons are in the circuit? (iii) does ribbon topology invert the count rule (odd number of half-turns = Moebius; even, including 2, = Hueckel)? (iv) does the electronic state invert it (Baird: in the lowest pi-pi* triplet, 4n is aromatic/diatropic and 4n+2 is antiaromatic/paratropic)? Unit contributions to the circuit: CH 1; imine-type N(=) 1 (lone pair in-plane); N(H) 2; divalent O 2; three-coordinate B(H) 0 (empty p, conjugation NOT broken); C(+) 0 (empty p, tropylium-type); C(-) 2 (p-type lone pair, cyclopentadienide-type); sp3 CH2 has no p orbital and severs the circuit.

Per belt (pi count n_pi; n_pi mod 4; topology; state; verdict):
B1 20; 0; flat; S0 -> 4n, Hueckel-antiaromatic -> paratropic. NO
B2 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B3 18; 2; two half-turns (even -> Hueckel topology); S0 -> diatropic. YES
B4 24; 0; flat; T1 -> Baird 4n triplet -> diatropic. YES
B5 18; 2; flat; S0 -> diatropic. YES
B6 22; 2; flat; T1 -> Baird 4n+2 triplet -> paratropic. NO
B7 20 CH minus 2e = 18; 2; flat; S0 -> diatropic. YES
B8 16 CH plus 2e = 18; 2; two half-turns (Hueckel); S0 -> diatropic. YES
B9 22; 2; one half-turn; S0 -> Moebius 4n+2 -> paratropic. NO
B10 16+2 = 18; 2; flat; S0 -> diatropic. YES
B11 16 + 2x1 = 18; 2; flat; S0 -> diatropic. YES
B12 16+0 = 16; 0; flat; T1 -> Baird 4n -> diatropic. YES
B13 14+2 = 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B14 20+0 = 20; 0; flat; T1 -> Baird 4n -> diatropic. YES
B15 14+2 = 16; 0; one half-turn; S0 -> Moebius 4n -> diatropic. YES
B16 circuit severed by the sp3 centre; the 18 sp2 CH form an open polyene, no closed circuit -> no macrocyclic ring current (the apparent "18 pi, 4n+2" is a decoy). NO

Diatropic: B2, B3, B4, B5, B7, B8, B10, B11, B12, B13, B14, B15 = 12. Paratropic/none: B1, B6, B9, B16 = 4.

Literature anchors for each judgement: [16]annulene paratropic and its dianion (18 pi) diatropic; Heilbronner/Herges Moebius annulene (odd half-twist inverts); lemniscular/figure-eight expanded porphyrins (even half-twist = Hueckel); Baird 1972 and subsequent T1-aromaticity work (T1 of benzene paratropic, T1 of 4n rings diatropic); borepin/borole (B contributes 0 while sustaining conjugation); tropylium (C+ 0); cyclopentadienide (C- 2); pyrrole (N-H 2) vs pyridine (N= 1); furan (O 2).

## WHY IT SHOULD STUMP

The hidden gate is an INVENTORY GAP, not a trap: the complete criterion set for "does this circuit sustain a diatropic current" is {circuit continuity, Hueckel count, Moebius twist parity, Baird spin inversion}. Solvers habitually truncate to Hueckel, or to Hueckel + Moebius (the twist column is visibly a topology cue and invites it). The $T_1$ column reads as a spectroscopic detail - "the state at which the property was evaluated" - not as a rule-switching variable, and nothing in the prompt states that spin multiplicity inverts the count rule (per the mandatory/optional-fork inversion, the resolving condition is deliberately never stated). Three of the four triplet belts carry 4n counts (24, 16, 20), which a Hueckel-only reader confidently calls antiaromatic, and the fourth (22 pi) is 4n+2, which the same reader confidently calls aromatic - so the Baird omission is load-bearing four times and does not self-cancel (net -2). The surface reading points the wrong way in each case: the count itself "explains" the naive verdict, so chain-local self-verification returns consistent and no extreme-case bounding exists to expose the omission.
Layered on top is case volume with heterogeneous subtests: 16 belts, each needing a DIFFERENT judgement - imine vs amine-type nitrogen (1 vs 2 electrons), an empty p orbital that does not break conjugation (B(H), C(+) contribute 0), a carbanion lone pair that does (C(-) contributes 2), a divalent oxygen, two redox-shifted counts (dication, dianion), twist parity 1 vs 2, and one severed circuit whose 18 sp2 CH advertise a false 4n+2. Because each case demands a different chemical decision the grid cannot be compressed into one predicate table, and a single dropped or mis-typed unit shifts the integer.

## WRONG BRANCHES

- 10 - Baird omitted entirely (T1 treated like S0): B4, B12, B14 wrongly called paratropic and B6 wrongly called diatropic; net -2. This is the primary predicted failure.
- 10 - ribbon topology ignored (twists treated as cosmetic): B2, B13, B15 lost, B9 gained; net -2.
- 10 - twist parity botched (two half-turns treated as still inverting, i.e. 'any twist = Moebius'): B3 and B8 wrongly called paratropic.
- 10 - net charge not propagated into the pi count (atom count used directly): B7 read as 20 pi and B8 as 16 pi, both wrongly paratropic.
- 8 - pure Hueckel reading: both Baird and all topology inversions dropped (B2, B4, B12, B13, B14, B15 lost; B6, B9 gained).
- 9 - pure Hueckel plus treating B16 as a continuous 18-pi aromatic circuit (sp3 centre not recognised as severing the circuit).
- 13 - everything right except B16, whose 18 sp2 CH are counted as a closed 4n+2 circuit.
- 13 - Baird direction over-applied ('any triplet is aromatic'), so B6 is added; or Moebius over-applied ('any twisted belt is aromatic'), so B9 is added.
- 14 - both over-applications at once (all triplets and all twisted belts called diatropic).
- 11 - one unit-contribution slip anywhere: B(H) taken as a 2-electron donor (B12), C(+) as 2 (B14), C(-) as 0 (B13), O as 0 (B15), each N(=) as 2 (B11), or N(H) as 1 (B10) - each single slip flips exactly one belt.
- 6 - Hueckel-only plus inverted twist-parity convention (odd treated as Hueckel, even as Moebius).
- 5 - Hueckel-only plus systematic mis-assignment of heteroatom/charged-centre contributions (all of B11-B15 flipped).

## VERIFICATION (design agent's plan — NOT trusted, see main-thread check)

Ground truth is a finite rule-based enumeration and was verified by script (already executed; /private/tmp/claude-501/-Users-flowstate-work-project-planck/92102628-7431-4537-9453-119480abd2d7/scratchpad/belts.py):
1. Encode each belt as (unit multiset, half-turns t, net charge q, state). Compute n_pi = sum over units of {CH:1, N(=):1, N(H):2, O:2, B(H):0, C(+):0, C(-):2} minus q for the belts whose charge is delocalised (B7, B8); belts B13/B14 carry the charge in the named unit so no double counting. Verified counts: B1 20, B2 16, B3 18, B4 24, B5 18, B6 22, B7 18, B8 18, B9 22, B10 18, B11 18, B12 16, B13 16, B14 20, B15 16, B16 18 (severed).
2. Set aromatic = (n_pi mod 4 == 2); invert once if t is odd; invert once if state is T1; force False if the circuit contains an sp3 centre. Sum -> 12 (diatropic set B2, B3, B4, B5, B7, B8, B10, B11, B12, B13, B14, B15).
3. Misread audit (already run): every SINGLE deviation from the correct criterion set gives 8, 9, 10, 11, 13 or 14 - never 12, so no single plausible error reaches the answer. Reaching 12 by a wrong route requires at least two simultaneous, independent errors of different type (e.g. treating B16 as conjugated AND mis-assigning one heteroatom); the largest single lever (Baird, -2) has no equal-magnitude positive partner. Contradictory combinations (ignore twists AND over-apply twists) were excluded.
4. Independent cross-check of each unit rule and each topology/spin rule against textbook exemplars: [16]annulene / [16]annulene dianion; Herges' Moebius annulene; lemniscular expanded porphyrins (even twist = Hueckel); Baird's rule for the lowest pi-pi* triplet (T1 of benzene paratropic; T1 of 4n rings diatropic); borepin/borole boron (0 electrons, conjugation retained); tropylium (0); cyclopentadienide (2); pyrrole (2) vs pyridine (1); furan (2). No numerical tolerance is involved - the answer is an exact integer.

## COMPLIANCE (design agent's self-audit)

Self-containment: every symbol, unit type, column and state is defined in the prompt; no formula, count rule, criterion name or governing model is supplied (rule 1), and no rejection/resolution condition is stated (rules 10, 13, 15 - the Baird switch is never signposted, the T1 entries are presented as plain data columns alongside charge and topology). Geometry idealisation (uniform overlap, no bond-length localisation, no ion pairing, charges of pi origin) is pinned only where multiple defensible physical readings would otherwise exist (rule 5), and is stated as structure, not as a rule.
CURVD: one question, one exact integer (12). Contained - 16 explicitly specified belts. Unambiguous - each belt's circuit, count, topology and state are fully determined; no figure-only or literature-dependent data. Reduced - single aggregate. Verifiable - script enumeration plus per-case checklist, exhaustive misread audit executed. Discrete - integer, so no rounding boundary exists (rule 4 rounding hazard not applicable; no decimals anywhere). >= 6 distinct plausible wrong outcomes: 5, 6, 8, 9, 10, 11, 13, 14 (twelve mechanisms listed), and no single misread lands on 12.
Mandated angle satisfied: 16 independent cases, each with a DIFFERENT conceptual subtest (Hueckel count; Moebius parity 1 vs 2; Baird inversion in both directions; oxidative and reductive count shifts; imine vs amine-type nitrogen; empty-p boron; empty-p carbenium; carbanion lone pair; divalent oxygen; severed circuit with a decoy 4n+2 count) - heterogeneous, so the grid resists the batching/predicate-table compression that collapsed earlier homogeneous censuses (rule 11 caveat). One dropped or mis-typed case moves the integer.
Originality: no [3]naphthylene, no fused aromatic/antiaromatic amalgam, no naphthalenoid/cyclobutadienoid units, no force constants, no NICS-XY or Raman numbers, no redox potentials, no linear-vs-angular isomer pair; nothing from the paper is restated. Only the paper's physics is borrowed (charge state and circuit topology, not electron count alone, decide whether a current is diatropic; a formally 4n system can be diatropic).
Timelessness / provenance: no dates, no names, no citations, no PII, no post-2025-07-31 content; every rule invoked (Hueckel, Moebius/Heilbronner, Baird, conjugation continuity, standard heteroatom and charged-centre pi contributions) is decades-old textbook material, so rule 7 is met - hard even for a solver who knows every fact, because the difficulty is completeness of the criterion inventory times 16 heterogeneous judgements.
Prompt length: 1710 characters, under the 2000 limit. All mathematics in LaTeX; no Unicode math symbols.
Known residual (documented, structural to single-integer censuses): pairs of independent errors can cancel to 12 (e.g. B16 mis-read as conjugated together with one heteroatom mis-assignment). These require two unrelated mistakes of different type; no single error and no self-consistent single mindset reaches 12.
