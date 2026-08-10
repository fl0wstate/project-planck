# planck task - cyclic oligoester chirality census v2 (HARDENED, answer 6)

**FINAL ANSWER: 6**

**Prompt chars: 1625 / 2000**

Supersedes `planck_task_oligoester_census.md` (v1, answer 3), which scored **1/2**.

**Source:** Lam, N. Y. S.; Dhankhar, J.; Lahdenpera, A. S. K.; Phipps, R. J. *J. Am. Chem. Soc.* **2024**, *146*, 33302-33308. doi:10.1021/jacs.4c13919. Published 26 Nov 2024, CC BY 4.0, open access via PMC. Concept borrowed only.

---

## V1 POST-MORTEM: THE DESIGNED GAP NEVER FIRED, AND SOMETHING ELSE DID

v1 targeted the closed checklist "achiral iff there is a mirror plane or an inversion centre". **Neither responder used it.** Both wrote the problem as a cyclic string and asked whether the complement is a *rotation* of the original, which searches every shift automatically. The representation repaired the gap before it could open: once the descriptors are a cyclic sequence, "is the complement a rotation?" is the natural question, and no two-item checklist is ever consulted.

The 1/2 came from a different judgment entirely.

- Responder A: *"the relevant relabelings are the dihedral symmetries of the ring: rotations of the cyclic list; reversal of the cyclic order."* Allowed reversal, called G5 achiral, answered **2**.
- Responder B: *"because every residue is connected in the same ester direction all the way around the ring, the sequence can be relabeled only by a cyclic rotation of the residues. A reversal of the order is not an allowed identity relabeling here."* Answered **3**.

So the live fork is **backbone directionality**: reversing the cyclic order corresponds to traversing the ring against the ester sense, mapping the ester oxygen onto the carbonyl carbon, and is therefore not a relabelling of the same compound. Exactly one case in v1 (G5) tested it.

**Why v2 does not simply add more reversal-sensitive cases.** They are one judgment applied repeatedly: a solver either allows reversal or does not, uniformly. More such cases enlarge the error but do not make it more likely, and the score depends only on whether the answer is wrong. Instead v2 adds a **second, independent fork**, so that two separate judgments must both be made correctly.

## THE TWO FORKS

**Fork 1, directionality (proven live).** Reversal of the cyclic order is not permitted. Load-bearing in G5 and G6, which are chiral but become "achiral" the moment reversal is allowed. Reversal-sensitive sequences are rare, existing only for even $n \geq 6$; G5 is the unique one at $n = 6$ and G6 one of two at $n = 8$.

**Fork 2, residue identity (new).** A relabelling must also carry each residue onto a residue of the same kind, so mixing X and Y restricts the permitted shifts to those preserving the residue pattern. For alternating X, Y only even shifts survive.

This yields the pair that carries the task:

> **G1 and G8 have the identical descriptor list R, S, R, S.** G1 (all residues X) is **achiral**, because the shift by one satisfies the condition. G8 (residues alternating X, Y) is **chiral**, because the shift by one no longer preserves the residue pattern and no even shift works.

Same descriptors, opposite verdicts, decided solely by whether residue identity was carried through the analysis. G9 is the control that stops the lazy inverse rule: it also has mixed residues, yet the shift by two preserves both the residue pattern and the complement relation, so it is genuinely achiral.

---

## PROMPT

```
Nine cyclic oligoesters are described. In each, every residue is one of two kinds: residue X, derived from 2-hydroxybutanoic acid, contributing $-\mathrm{O}-\mathrm{CH}(\mathrm{C_2H_5})-\mathrm{C(O)}-$ to the ring, or residue Y, derived from 2-hydroxypropanoic acid, contributing $-\mathrm{O}-\mathrm{CH}(\mathrm{CH_3})-\mathrm{C(O)}-$. The residues are joined so that the sequence oxygen, then alkyl-bearing carbon, then carbonyl carbon runs the same way round the whole macrocycle. Every residue therefore carries one stereocentre, at the carbon bearing its alkyl group.

Each compound is specified by listing its residues in order with the configuration of each, read round the ring in the direction running from the ester oxygen of a residue to the carbonyl carbon of that same residue. Each list is cyclic, the residue following the last being the first.

G1: X(R) X(S) X(R) X(S)

G2: X(R) X(R) X(R) X(S)

G3: X(R) X(R) X(S)

G4: X(R) X(S) X(R) X(S) X(R) X(S)

G5: X(R) X(R) X(S) X(R) X(S) X(S)

G6: X(R) X(R) X(R) X(S) X(R) X(S) X(S) X(S)

G7: X(R) Y(S) X(R) Y(S) X(R) Y(S)

G8: X(R) Y(S) X(R) Y(S)

G9: X(R) Y(R) X(S) Y(S) X(R) Y(R) X(S) Y(S)

Take every macrocycle to be conformationally mobile, with all ring conformations freely accessible, and take the configuration at every stereocentre to be fixed. Regard a compound as chiral when no accessible conformation of it can be superimposed on its mirror image. Disregard any process that makes or breaks a covalent bond, and assume dilute solution in an achiral solvent with no added chiral agent.

How many of the nine compounds are chiral? Report a single integer.
```

---

## GOLDEN

Write the descriptors as a cyclic sequence $c_0 \ldots c_{n-1}$ and the residue kinds as $t_0 \ldots t_{n-1}$. The mirror image has the same constitution with every descriptor inverted. Two specifications denote the same compound exactly when one is carried onto the other by a shift $k$ that preserves the residue pattern, $t_{i+k} = t_i$ for all $i$; reversal of the order is not available, because the ester sense runs one way round the ring. Hence

> the compound is **achiral** exactly when there is a shift $k$ with $t_{i+k} = t_i$ and $c_{i+k} = \bar{c_i}$ for every $i$.

| | $n$ | residues | descriptors | permitted shifts | achiral? |
|---|---|---|---|---|---|
| G1 | 4 | XXXX | R S R S | 0,1,2,3 | achiral, $k=1$ |
| G2 | 4 | XXXX | R R R S | 0,1,2,3 | **chiral** |
| G3 | 3 | XXX | R R S | 0,1,2 | **chiral** |
| G4 | 6 | XXXXXX | R S R S R S | 0..5 | achiral, $k=1$ |
| G5 | 6 | XXXXXX | R R S R S S | 0..5 | **chiral** (fork 1) |
| G6 | 8 | XXXXXXXX | R R R S R S S S | 0..7 | **chiral** (fork 1) |
| G7 | 6 | XYXYXY | R S R S R S | 0,2,4 | **chiral** (fork 2) |
| G8 | 4 | XYXY | R S R S | 0,2 | **chiral** (fork 2) |
| G9 | 8 | XYXYXYXY | R R S S R R S S | 0,2,4,6 | achiral, $k=2$ |

**Chiral: G2, G3, G5, G6, G7, G8. Answer = 6.**

Two structural facts the solution should state:

- **Odd ring size forces chirality (G3).** Applying a shift $k$ that satisfies the condition $n$ times inverts the descriptors an odd number of times while returning every index to itself, giving $c_i = \bar{c_i}$, which is impossible. No odd-membered ring in this family is ever achiral.
- **G5 and G6 are chiral although their mirror images are reversals of themselves.** That relationship is not a symmetry of a directional macrocycle, which is precisely the point of fork 1.

---

## WRONG BRANCHES (computed; no collision with 6)

| **4** | reversal wrongly allowed - the observed 1/2 failure mode |
| **4** | residue identity ignored when testing relabellings |
| **2** | both forks failed |
| **2** | 'equal numbers of R and S implies achiral' |
| **5** | 'alternating descriptors implies achiral, otherwise chiral' |
| **5** | odd ring size assumed achiral |
| **0** | improper operations assumed not to invert descriptors |
| **7** | 'two different residues present implies chiral' |
| **2** | reversal allowed AND equal-count rule |
| **8** | only a mirror plane and an inversion centre considered |

Six distinct wrong totals. The two forks err in the same direction, both inflating the achiral count, but the remaining shortcuts err the other way, so no combination returns 6.

## INDEPENDENT VERIFICATION

Script `scratchpad/oligo3.py`, `oligo4.py`. The criterion is implemented as a search over shifts constrained by the residue pattern, with optional flags to allow reversal or to ignore residue identity, so each shortcut is evaluated against the same nine compounds.

Controls:

- **Reversal-sensitive sequences enumerated exhaustively** for $n = 4$ to $12$: none exist at odd $n$ or at $n = 4$; exactly one at $n = 6$, two at $n = 8$, six at $n = 10$, thirteen at $n = 12$. G5 and G6 are drawn from that set, so fork 1 is genuinely load-bearing rather than incidental.
- **Convention independence** confirmed for v1 under reversal of the reading direction, global exchange of R and S, and rotation of the starting point; the same invariances hold here by construction, since the criterion is stated in shift-invariant form.
- **The G1/G8 pair** verified directly: identical descriptors, permitted shift sets $\{0,1,2,3\}$ and $\{0,2\}$, verdicts achiral and chiral respectively.

## COMPLIANCE

- **Nothing advertised.** Scanned programmatically: the prompt contains no occurrence of symmetry, mirror plane, inversion, rotation, reversal, operation, axis or meso. Only "mirror image" appears, being the definition of chirality.
- **No governing rule given.** Neither the shift criterion, nor the directionality argument, nor the residue-preservation condition appears in the prompt. The traversal sense is stated as a fact of constitution, not as a rule about which relabellings are permitted.
- **Self-contained with no kinetic data.** Configurations cannot interconvert, so no barriers, half-lives or physical constants are required, which removes the entire class of self-containment findings raised against the earlier stereogenic census.
- **CURVD**: Contained; Unambiguous; Reduced; Verifiable; Discrete (6).
- **Heterogeneous cases**: nine compounds, six distinct judgments - rotoreflection-type achirality, inversion-type achirality, plain chirality, odd-ring chirality, directionality-sensitive chirality, and residue-restricted chirality with its achiral control.
- **Deductive ground truth**, no contested empirical content. **Timeless, no PII, pre-cutoff.**

## STATUS

Verified. Cold probe recommended: fork 1 is confirmed live at 1 in 2, and fork 2 is untested.
