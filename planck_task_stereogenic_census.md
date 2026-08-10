# planck task — stereogenic-element census (answer 15)

**FINAL ANSWER: 15**

**Prompt chars: 955 / 2000**

**Source:** Akimoto, N.; Takaya, K.; Kasashima, Y.; Watanabe, K.; Yoshida, Y.; Mino, T. "Pd-Catalyzed asymmetric allylic amination with isatin using a P,olefin-type chiral ligand with C-N bond axial chirality." *Beilstein J. Org. Chem.* **2025**, *21*, 1018-1023. doi:10.3762/bjoc.21.83. Published **23 May 2025**, CC BY 4.0. Comfortably pre-cutoff (two months of margin, unlike bjoc.21.119 which sits exactly on 31 Jul 2025).

Borrowed: the concept only — that a C(aryl)-N(amide) bond can carry a configurationally stable stereogenic axis. None of the paper's compounds, yields, ee values or barriers appear. The catalysis content is not used at all.

---

## THE LEVER — a new one

The two prior kills both placed the inventory gap in the set of **improper symmetry operations** (a rotoreflection that no mirror plane or inversion centre supplies). This task keeps the proven mechanism but moves the gap to a different inventory: **the kinds of stereogenic element**.

The enumeration a competent solver brings to "how many stereoisomers?" is: stereocentres, then double-bond geometry, then — sometimes — biaryl atropisomerism. The habitually omitted member is the **C-N stereogenic axis** of an N-aryl amide. It is indisputably standard, with canonical archetypes (Curran's anilide atropisomers; Clayden's work on amide axial chirality), so it survives adversarial QC on the same footing S_n did.

**Why nothing is advertised.** The prompt names six compounds and asks for stereoisomer counts. There is no column, field, label or stated parameter pointing at bond rotation, axial chirality, or symmetry. Per the confirmed retrieval-cue law, this is the whole design: had the prompt stated a rule such as "rotation is slow when both ortho positions bear substituents", it would have cued axial chirality and handed back the very inventory the task is testing — exactly what killed the annulene-quadrant task 3/3. Hindrance is instead made unmistakable from the substitution patterns themselves.

**Second, independent judgment.** Hindrance and stereogenicity are deliberately decorrelated. An axis is stereogenic only if **both** ends are dissymmetric. C1 and C5 are maximally hindered yet achiral about the axis, because their aryl ring carries two *identical* ortho substituents and a 180 degree turn regenerates the same structure. A solver who equates "2,6-disubstituted, so rotation is locked" with "therefore atropisomeric" over-counts. This bites in the opposite direction to the primary gap, so the two errors cannot cancel.

**Third judgment, correlated outcomes (rule 3).** C4 carries two constitutionally identical stereogenic axes on a para-phenylene, so the naive $2^n$ gives 4 where the true count is 3 — the (aR,aS) form is meso, the inversion centre of the ring exchanging the two halves and inverting both descriptors. C6 supplies the same logic on ordinary stereocentres as a familiar anchor.

---

## PROMPT

```
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours. Report the sum of the six numbers as a single integer.

C1: $N$-(2,6-dimethylphenyl)-$N$-(1-phenylethyl)acetamide

C2: $N$-(2-tert-butyl-6-methylphenyl)-$N$-methylacetamide

C3: $N$-(2-tert-butyl-6-methylphenyl)-$N$-(1-phenylethyl)acetamide

C4: benzene-1,4-dicarboxylic acid bis[$N$-(2-tert-butyl-6-methylphenyl)-$N$-methylamide]

C5: 2,6-dimethyl-2'-nitrobiphenyl

C6: 2,3-dibromobutane

Take each compound to have the single constitution named: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely on the stated timescale, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
```

---

## GOLDEN (per compound)

| | analysis | count |
|---|---|---|
| **C1** | One stereocentre (the $N$-CH(CH_3)Ph carbon: N, CH_3, Ph, H all different). The N-aryl bond is strongly hindered, but the aryl ring bears **two identical** ortho methyls, so rotation by 180 degrees regenerates the same structure and the axis is **not** stereogenic. $2^1$ | **2** |
| **C2** | No stereocentre. The N-aryl axis has *tert*-butyl on one ortho position and methyl on the other (dissymmetric), the N end bears methyl and acetyl (dissymmetric), and 2,6-disubstitution makes rotation slow. One stereogenic axis. $2^1$ | **2** |
| **C3** | The C2 axis plus the C1 stereocentre, independent. $2^2$ | **4** |
| **C4** | Two constitutionally identical stereogenic axes of the C2 type. (aR,aR) and (aS,aS) are enantiomers; (aR,aS) is **meso**, since the para-phenylene's inversion centre exchanges the halves and converts aR into aS. | **3** |
| **C5** | No stereocentre. Three ortho substituents make rotation slow, but the 2,6-dimethyl ring has **two identical** ortho substituents, so the biaryl axis is not stereogenic. Achiral. | **1** |
| **C6** | Two stereocentres, constitutionally identical: (R,R), (S,S), and one meso (R,S). | **3** |

**Sum = 2 + 2 + 4 + 3 + 1 + 3 = 15.**

Amide C(O)-N rotamers are excluded by the stated timescale: tertiary-amide rotation barriers of roughly 15-20 kcal/mol give lifetimes of seconds at 25 degrees C, far below "hours". The stipulation resolves this deductively rather than leaving it to judgment.

---

## WRONG BRANCHES (all computed, no collision with 15)

| value | route |
|---|---|
| **10** | omit C-N axes entirely - PRIMARY predicted failure: stereocentres and biaryl C-C axes recognised, N-aryl axes never enumerated |
| **10** | no axial stereogenicity of any kind; stereocentres only |
| **11** | C-N axes omitted AND meso missed |
| **14** | C2 alone mis-scored: the sole stereogenic element missed, compound called achiral |
| **16** | C4 alone mis-scored: two axes multiplied to 4, meso form not recognised |
| **16** | C6 alone mis-scored: meso 2,3-dibromobutane counted as a fourth isomer |
| **16** | C5 alone mis-scored: 2,6-dimethyl ring treated as dissymmetric |
| **17** | meso forms missed: 2^n applied to C4 and C6 |
| **17** | C1 alone mis-scored: its 2,6-dimethyl ring treated as a stereogenic axis |
| **18** | hindrance taken to imply stereogenicity: every 2,6-disubstituted ring counted as an axis without testing whether its two ortho substituents differ |
| **20** | no dissymmetry test AND meso missed |

---

## INDEPENDENT VERIFICATION

Ground truth is a hand-checkable enumeration, cross-checked by script (`scratchpad/stereo.py`), which parametrises the three judgments — whether C-N axes are enumerated, whether the both-ends-dissymmetric test is applied, whether meso relationships are recognised — and recomputes the total under every combination. Seven distinct wrong totals arise (10, 11, 14, 16, 17, 18, 20); none equals 15.

Individually re-checked by hand:
- **C1/C5 achirality**: a ring with two identical ortho substituents possesses a local mirror plane through the axis, so no axial chirality regardless of barrier height. Verified by the 180-degree-rotation argument, which regenerates an identical structure.
- **C4 meso**: directly analogous to tartaric acid. Two equivalent stereogenic elements related by an improper operation of the connecting framework give 3 stereoisomers, not 4.
- **C2 axis genuinely stereogenic**: both ortho substituents differ (*tert*-butyl vs methyl) and both N substituents differ (methyl vs acetyl); 2,6-disubstituted anilides of this bulk are configurationally stable at room temperature.
- **Amide rotamer exclusion** confirmed against the stated hours timescale.

---

## COMPLIANCE

- **Nothing advertised**: no mention of chirality types, axial chirality, atropisomerism, rotation barriers, symmetry, or stereogenic elements. Six names and a counting question.
- **No governing rule given** (rule 1): neither the both-ends-dissymmetric criterion, nor any barrier rule, nor the meso condition appears.
- **CURVD**: Contained; Unambiguous (every compound is either clearly hindered or clearly free, with no borderline barrier; the timescale stipulation removes the amide-rotamer question; achiral solvent stated so enantiomers are counted as distinct species but no chiral-shift complication arises); Reduced (one integer); Verifiable (enumeration); Discrete (15).
- **Heterogeneous cases** (rule 11 caveat): six compounds requiring six different judgments — centre only; axis only; axis plus centre; two axes with a meso form; hindered-but-achiral axis; two centres with a meso form. No single predicate row covers them, so the set cannot be batched.
- **Deductive ground truth**: stereoisomer counts under stated idealisations are theorems about constitution, not contested empirical claims — the property that let the S_n task survive QC, and the reason aromaticity was abandoned as a host.
- **Timeless, no PII, pre-cutoff**: no dates, citations or names in the prompt. Anilide atropisomerism is decades-established.

## STATUS

Verified. Not cold-probed (standing directive).
