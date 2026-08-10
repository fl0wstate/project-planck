# planck task — stereogenic-element census v2 (HARDENED) — ***2/2 PLATFORM KILL***

> **PLATFORM RESULT 2026-07-31: BOTH responses failed. Second 2/2 kill of the campaign.**
> Both returned **19** against golden **16**. Failure identification filed as Block 1 Response 1,
> Block 2 Response 1.
>
> **The shared error — one end checked, the other ignored.** Both counted a stereogenic axis wherever
> rotation was slow, without asking whether *both* ends of that axis are dissymmetric:
>
> | | returned | golden | error |
> |---|---|---|---|
> | D1 | 4 | **2** | counted the N–aryl axis, but the ring bears two *identical* ortho *tert*-butyls, so a 180° turn about the axis regenerates the same structure |
> | D4 | 2 | **1** | aryl end is fine (t-Bu vs Me), but the succinimide nitrogen carries two *identical* ring carbonyls, so that end is symmetric and the axis is not stereogenic |
>
> D2, D3, D5, D6, D7 were all correct. 4+2+4+2+3+1+3 = 19; golden 2+2+4+1+3+1+3 = 16.
>
> **Self-refuting, which strengthens the justification.** On D6 they applied the correct test and killed the
> biaryl axis on identical ortho methyls — then failed to apply that same test to D1. D4 was justified as
> *"stereogenic because the aryl ring has different ortho substituents"*, checking the aryl end only and never
> examining the nitrogen end. Restricted rotation is necessary but not sufficient for a stereogenic axis, so
> this is a scientific reasoning error, not an arithmetic slip.
>
> **The v2 hardening worked as designed.** Predicted branches were 20 (barrier heuristic everywhere) and 16
> (correct). The observed 19 is the barrier heuristic on D1 and D4 with the symmetry test correctly applied to
> D6 — inside the designed failure band.
>
> **METHODOLOGICAL WARNING — DO NOT RETIRE ON PROBE EVIDENCE ALONE.** Two cold probes solved this 2/2 by the
> *intended* two-ends route, at 58 s and 68 s, tool_uses = 0, and on that basis it was briefly retired. The
> platform then failed it 2/2. For shortcut-substitution levers the Opus proxy is strictly stronger than the
> platform responders, so a probe solving correctly does **not** predict a platform solve. Probe evidence
> stays decisive in one direction only: if a probe *names your mechanism as a trap*, the lever is dead.
>
> ---
>
> **RUN 2 — 2/2 AGAIN, different error combination** *(provisional: confirm this is a separate run and not a
> fuller view of run 1)*. Responses returned **20** and **19**.
>
> | | golden | run 2 A | run 2 B | run 1 |
> |---|---|---|---|---|
> | D1 | **2** | 4 ✗ | 4 ✗ | 4 ✗ |
> | D2 | 2 | 2 ✓ | 2 ✓ | 2 ✓ |
> | D3 | 4 | 4 ✓ | 4 ✓ | 4 ✓ |
> | D4 | **1** | 2 ✗ | 1 ✓ | 2 ✗ |
> | D5 | 3 | 3 ✓ | 3 ✓ | 3 ✓ |
> | D6 | **1** | 2 ✗ | 2 ✗ | 1 ✓ |
> | D7 | 3 | 3 ✓ | 3 ✓ | 3 ✓ |
> | sum | **16** | **20** | **19** | **19** |
>
> **Run 2 A hit the predicted primary branch exactly.** 20 is the top row of the wrong-branch table below —
> barrier heuristic everywhere, symmetry test nowhere, D1/D4/D6 each over-counted by one.
>
> **Run 2 B is the strongest single piece of evidence produced so far.** It *states the correct criterion
> itself* on D2 — *"the aryl ortho substituents are different and the nitrogen bears two different nonaryl
> substituents"* — then applies it at the nitrogen end of D4, correctly returning 1 with the reasoning *"the
> succinimide nitrogen is flanked by two equivalent carbonyl sides, so that bond is not a stereogenic axis
> here"* — and then fails to apply it at the aryl end of D1 and D6, where both ortho positions are identical.
> Knowledge complete, application partial. This is the appendix corollary demonstrated verbatim: do not test
> whether a model *knows* a rule, test whether it *applies* the category unprompted.
>
> **Three distinct failing responses across two runs, hitting three different error combinations** (D1+D4;
> D1+D6; D1+D4+D6). D1 has failed in all three. D6 has failed in two of three. The task does not depend on a
> single fragile fork.

**FINAL ANSWER: 16**

**Prompt chars: 1471 / 2000**

Supersedes `planck_task_stereogenic_census.md` (v1, answer 15), which was **solved** — but solved by a route that reveals the design fault precisely.

**Source:** Akimoto, N.; Takaya, K.; Kasashima, Y.; Watanabe, K.; Yoshida, Y.; Mino, T. *Beilstein J. Org. Chem.* **2025**, *21*, 1018-1023. doi:10.3762/bjoc.21.83, published 23 May 2025, CC BY 4.0. Concept borrowed only (a C(aryl)-N(amide) bond can carry a configurationally stable stereogenic axis); no compound, yield, ee value or barrier from the paper is used.

---

## V1 POST-MORTEM: RIGHT ANSWER, WRONG REASON

The responder reached 15 without ever applying the test the task was built around.

- On C1 it wrote: *"atropisomerism from rotation about the aryl-N bond is not stable enough here with only 2,6-dimethyl substitution, so those conformers are not counted separately."*
- On C5: *"the biaryl rotation is not hindered enough for the enantiomeric conformations to be isolable for hours."*

Both are **barrier** arguments. The intended reasoning is a **symmetry** argument: a ring bearing two *identical* ortho substituents cannot carry a stereogenic axis at any barrier height, because a 180 degree turn about that axis regenerates the same structure.

**The design fault:** in v1 the two judgments were *correlated*. The achiral-axis cases were built from 2,6-dimethyl groups, hindered weakly enough that "probably not locked" is a defensible read — and it yields the same verdict as the symmetry test. A cruder heuristic reproduced the answer, so the gate never fired.

**The v2 fix:** make hindrance *unarguable* in exactly the cases where the axis is achiral. Replace 2,6-dimethyl with 2,6-di-tert-butyl (D1) and with a tetra-ortho-substituted biphenyl (D6). Both are among the most rotationally locked motifs in organic chemistry — "not hindered enough" becomes untenable, and the solver is forced onto the symmetry question. The barrier heuristic that solved v1 now returns **20**.

**New judgment added (D4):** an axis needs *both* ends dissymmetric. D4's aryl ring is dissymmetric and the bond is locked, but the imide nitrogen carries two identical ring carbonyls, so the axis is achiral. This fails at the opposite end from D1/D6, catching solvers who check only the aromatic ring.

---

## PROMPT

```
For each compound below, give the number of stereoisomers that exist as separate species capable of being isolated and handled at $25\,^\circ\mathrm{C}$ over a period of hours. Report the sum of the seven numbers as a single integer.

D1: $N$-(2,6-di-tert-butylphenyl)-$N$-(1-phenylethyl)acetamide

D2: $N$-(2-tert-butyl-6-methylphenyl)-$N$-methylacetamide

D3: $N$-(2-tert-butyl-6-methylphenyl)-$N$-(1-phenylethyl)acetamide

D4: $N$-(2-tert-butyl-6-methylphenyl)succinimide

D5: benzene-1,4-dicarboxylic acid bis[$N$-(2-tert-butyl-6-methylphenyl)-$N$-methylamide]

D6: 2,2',6,6'-tetramethylbiphenyl

D7: 2,3-dibromobutane

Use the following rotational data as given. For the bond from the amide or imide nitrogen to the ortho-disubstituted ring in D1 to D5, and for the bond joining the two rings in D6, the half-life for rotation at $25\,^\circ\mathrm{C}$ exceeds ten years. For every amide and imide carbonyl-to-nitrogen bond, the half-life for rotation at $25\,^\circ\mathrm{C}$ is less than one second. Rotation about every other single bond is fast at $25\,^\circ\mathrm{C}$.

Take each compound to have the single constitution named: disregard tautomers, and disregard any process that makes or breaks a covalent bond. Two structures are to be counted as one species when they interconvert freely on the stated timescale, and as two when they do not. Assume dilute solution in an achiral solvent, no added chiral agent, and ordinary laboratory handling throughout.
```

---

## GOLDEN

| | analysis | count |
|---|---|---|
| **D1** | One stereocentre (the CH(CH_3)Ph carbon). The N-aryl bond is locked beyond dispute by two *tert*-butyl groups, but they are **identical**, so a 180 degree turn about the axis regenerates the same structure: the axis is not stereogenic. $2^1$ | **2** |
| **D2** | No stereocentre. Ortho substituents differ (*tert*-butyl vs methyl); N substituents differ (methyl vs acetyl); 2,6-disubstitution locks rotation. One stereogenic axis. | **2** |
| **D3** | D2's axis plus D1's stereocentre, independent. $2^2$ | **4** |
| **D4** | Aryl ring dissymmetric and rotation locked, **but** the imide nitrogen bears two identical carbonyls of the symmetric succinimide ring. The N end has a local mirror plane, so the axis is not stereogenic. No stereocentre. | **1** |
| **D5** | Two constitutionally identical stereogenic axes of the D2 type. (aR,aR) and (aS,aS) are enantiomers; (aR,aS) is **meso**, the ring's inversion centre exchanging the halves and converting aR into aS. | **3** |
| **D6** | Four ortho methyls make this one of the most rotationally locked biaryls known, yet **each** ring carries two identical ortho substituents, so the axis is not stereogenic. Achiral. | **1** |
| **D7** | Two identical stereocentres: (R,R), (S,S), meso (R,S). | **3** |

**Sum = 2 + 2 + 4 + 1 + 3 + 1 + 3 = 16.**

Amide and imide C(O)-N rotamers are excluded deductively by the stated timescale: barriers of roughly 15-20 kcal/mol give lifetimes of seconds at 25 degrees C, far short of hours.

---

## WRONG BRANCHES (computed; no collision with 16)

| value | route |
|---|---|
| **20** | **the observed v1 failure mode**: every hindered axis counted as stereogenic, no symmetry test applied anywhere. D1, D4 and D6 all over-counted |
| **22** | barrier heuristic and meso forms both missed |
| **19** | aryl end tested but the other end never tested (D4 missed), and meso missed |
| **18** | meso forms missed (D5 and D7 taken as $2^n$) |
| **18** | the other end tested but the aryl end never tested |
| **17** | aryl end tested, other end never tested: D4 counted as 2 |
| **12** | C-N axes omitted and meso missed |
| **11** | C-N axes omitted entirely - stereocentres and biaryl axes only |
| **11** | no axial stereogenicity recognised at all |

---

## WHY THE TWO JUDGMENTS NOW OPPOSE EACH OTHER

The three achiral-axis compounds are maximally hindered, so any barrier-based shortcut over-counts them (+1 each). The stereogenic-axis compounds (D2, D3, D5) are genuinely locked, so a solver who over-corrects toward "these are probably not isolable" under-counts them. There is no single heuristic that lands on 16 without performing the symmetry test on each end of each axis. That is the decorrelation v1 lacked.

## INDEPENDENT VERIFICATION

Script `scratchpad/stereo2.py` parametrises four independent judgments — whether C-N axes are enumerated at all, whether the aryl end is tested for dissymmetry, whether the other end is tested, whether meso relationships are recognised — and recomputes the total under every combination. Seven distinct wrong totals (11, 12, 17, 18, 19, 20, 22); none equals 16.

Hand checks: D1/D6 achirality by the 180-degree-rotation argument (a ring with two identical ortho substituents has a local mirror plane through the axis); D4 by the same argument applied to the imide nitrogen; D5 and D7 meso by direct analogy to tartaric acid; D2 stereogenic on both-ends-differ plus tetra-substitution-level hindrance; amide rotamers excluded against the hours timescale.

## COMPLIANCE

- **Nothing advertised**: no mention of chirality types, atropisomerism, axial chirality, rotation barriers, symmetry or stereogenic elements. Seven names and a counting question. Stating any rotation rule would cue axial chirality and hand back the inventory being tested.
- **No governing rule given** (rule 1): neither the both-ends-dissymmetric criterion nor the meso condition appears.
- **CURVD**: Contained; Unambiguous (every axis is either extremely hindered or absent, with no borderline barrier left to argue about - this is exactly what v1 got wrong; timescale stipulation settles rotamers; achiral solvent stated); Reduced; Verifiable; Discrete (16).
- **Heterogeneous cases**: seven compounds, seven different judgments - centre only; axis only; axis plus centre; axis failing at the nitrogen end; two identical axes with a meso form; biaryl axis failing at both rings; two centres with a meso form.
- **Deductive ground truth**: counts under stated idealisations are theorems about constitution, not contested empirical claims.

## STATUS

Verified. Not cold-probed (standing directive).

---

## QC RESPONSE (revision 3)

Six findings returned; all addressed. Answer unchanged at **16**.

**Finding 1 (MAJOR, self-containment) - accepted and fixed.** The prompt gave no rotational barriers, so the counts for D2, D3 and D5 rested on the unstated assumption that these axes survive hours at $25\,^\circ\mathrm{C}$. The reviewer is correct: that is a non-foundational assumption and it was load-bearing.

Barriers are now supplied as given data: $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$ for the nitrogen-to-ring bond in D1 to D5 and the ring-to-ring bond in D6, and $\Delta G^{\ddagger} = 17\,\mathrm{kcal\,mol^{-1}}$ for every amide and imide carbonyl-to-nitrogen bond, with all other rotation fast.

**This strengthens the task rather than weakening it.** Withholding the barrier was a deliberate anti-cue measure, but the v1 post-mortem had already exposed the failure it enables: the responder escaped the intended test by asserting "not hindered enough" and reached the right answer through a barrier heuristic it never had to justify. Supplying the barriers removes that escape and transfers the full weight onto the dissymmetry test of Step 8, which remains unstated and uncued. Condition (a) is now given; condition (b), the load-bearing one, is not.

Margins are decisive, so no borderline judgment survives:

| $\Delta G^{\ddagger}$ / $\mathrm{kcal\,mol^{-1}}$ | $t_{1/2}$ at $25\,^\circ\mathrm{C}$ |
|---|---|
| 17 | $0.32\,\mathrm{s}$ |
| 22.5 | $0.96\,\mathrm{h}$ (threshold set by the stated timescale) |
| 30 | 34.6 years |

**Findings 2 to 6 (MAJOR, math notation) - accepted and fixed.** The golden response is rewritten with strict LaTeX throughout: $25\,^\circ\mathrm{C}$ for every temperature, $\mathrm{sp}^{3}$ for hybridisation, $2^{1}$, $2^{2}$ and $2^{0}$ for all count expressions, $\mathrm{CH_3}$ and $\mathrm{C_6H_5}$ for formulae, $\mathrm{kcal\,mol^{-1}}$ for energies. Every Unicode superscript, subscript, degree sign, en dash and em dash removed, and the file checked programmatically for residuals.

Note on Finding 2: the quoted string `$25\, ^\circ\mathr{C}$` does not occur in the submitted file, which had plain-text `25 °C` at that point; the reviewer's rendering appears to have mangled it. The requested correction is right regardless and has been applied.

**Net effect on the lever: unchanged.** The omitted inventory member is still the C-N stereogenic axis, and the load-bearing judgment is still that a frozen bond generates isomerism only when both ends are dissymmetric. Three compounds now carry a bond explicitly frozen for decades that nonetheless contributes nothing, each failing for a different reason.

---

## QC RESPONSE (revision 4)

Five findings from the science judge. Answer unchanged at **16**.

Findings 1, 3 and 4 all rest on "the prompt gives no barriers", which describes the revision-2 prompt; revision 3 had already supplied barriers. Finding 3 nevertheless exposed a real gap that revision 3 left open, and the fix for it resolves all three at once.

**Finding 3 (self-containment) - accepted, and it drives the whole revision.** Revision 3 gave barriers in $\mathrm{kcal\,mol^{-1}}$, which forced the golden to convert them to lifetimes through the Eyring expression, using $k_{B}$, $h$ and $R$ - none of which the prompt supplies. Supplying three physical constants to close that gap would be clumsy and would push the prompt toward a substitution exercise.

Revision 4 removes the need entirely: the prompt now stipulates **half-lives directly** rather than energies. Rotation about the nitrogen-to-ring bonds in D1 to D5 and the ring-to-ring bond in D6 has a half-life exceeding ten years at $25\,^\circ\mathrm{C}$; rotation about every amide and imide carbonyl-to-nitrogen bond has a half-life below one second. No equation, no physical constants, and no unit conversion is required at any point.

**Finding 1 (scientific accuracy, reference verification) - resolved by the same change.** The judge is right that the cited paper reports $25.0\,\mathrm{kcal\,mol^{-1}}$ for its own ligand and does not validate a $30\,\mathrm{kcal\,mol^{-1}}$ figure for D1 to D6. That objection had force only while the golden presented the barrier as a physical claim about these compounds. The compounds are invented for this problem, and their kinetic data are now given as stipulations in the prompt, in the same way the problem stipulates planarity or an achiral solvent. Nothing in the golden now asserts an experimental barrier, so no literature support is required. The source paper is cited for the concept of C-N axial chirality only.

**Finding 4 (unambiguity) - resolved.** The judge's alternative reading, that the unsupported axes might interconvert freely and give a sum of 11, is no longer available: the prompt states directly which bonds are frozen and which are free, with half-lives separated by more than eight orders of magnitude against a stated timescale of hours.

**Finding 2 (scientific accuracy) - accepted and corrected.** The old Step 12 read "for two constitutionally identical two-state elements the count is 3, not 4", which is genuinely overgeneralised: constitutional identity alone does not force a meso collapse, and an operation exchanging the two elements is required. The rule is now split. Step 10 states both conditions and says explicitly that constitutional identity by itself is insufficient, leaving four distinct stereoisomers when no exchanging operation exists. Step 11 gives the reduction to 3 only when both conditions hold. Steps 23 and 28 now discharge the second condition explicitly for D5 (the inversion centre of the benzene-1,4-diyl core) and for D7 (the twofold rotation exchanging C2 and C3), and Step 18 notes that D3's two elements are *not* related by any operation, so the reduction does not apply there.

**Finding 5 (math notation) - no defect present.** The submitted file contains `\,` throughout, for example `$\Delta G^{\ddagger} = 17\,\mathrm{kcal\,mol^{-1}}$`; it contains no literal commas inside units, which was checked programmatically. The quoted string with commas is a rendering artefact on the review side, the third of its kind after `\mathr{C}` in the previous round. The point is moot in any case: revision 4 removes every energy unit from the golden.

**Net effect on the lever: unchanged.** The omitted inventory member is still the C-N stereogenic axis, and the load-bearing judgment is still Step 6, that a frozen bond generates isomerism only when both of its ends are dissymmetric. That criterion remains unstated and uncued in the prompt. Supplying the kinetics as given data removes the barrier-guessing escape route that the v1 responder used, and now removes the constants gap as well.

