# planck task - cyclic oligoester chirality census (answer 3)

**FINAL ANSWER: 3**

**Prompt chars: 1373 / 2000**

**Source:** Lam, N. Y. S.; Dhankhar, J.; Lahdenpera, A. S. K.; Phipps, R. J. "Catalytic Enantioselective Hydrogen Atom Abstraction Enables the Asymmetric Oxidation of Meso Diols." *J. Am. Chem. Soc.* **2024**, *146*, 33302-33308. doi:10.1021/jacs.4c13919. Published **26 Nov 2024**, CC BY 4.0, open access and mirrored on PMC. Eight months of cutoff margin.

Borrowed: the concept only, that a compound carrying paired stereocentres may be achiral through an internal relationship between them, so that the two halves are enantiotopic rather than independent. No compound, yield, ee value or substrate from the paper appears.

---

## WHY THIS CONFIGURATION

Four probes and two platform results now separate cleanly by **question type**, not by domain or difficulty:

| task | question | result |
|---|---|---|
| rotaxane chirality census | *is it chiral?* | **2/2 kill** |
| stereogenic-element census | *is this axis stereogenic?* | wrong answer returned |
| aramide belt | *count distinct environments* | solved, 143 s |
| porphyrin atropisomers | *count distinct isomers* | solved, 138 s |
| adiabatic equilibrium | *what is the concentration?* | solved, boundary check generated unprompted |

The solves all share one behaviour: the model **generated the missing check itself**. It asked "which operations are even possible?", it tabulated face inversion, it opened by bounding the temperature. Open-ended checks get completed. The single kill came from a **closed** rule: "achiral if and only if there is a mirror plane or an inversion centre" is stated as an iff, so it terminates and invites no continuation.

This task therefore uses the one configuration with a demonstrated kill: a **classification** question resting on that **closed** shortcut. It deliberately avoids the counting frame, which forces explicit enumeration and thereby repairs the gap.

**And it abandons the small-molecule scaffold.** An earlier draft placed the same shortcut on meso diols. That was wrong: small-molecule stereocentre chirality is over-drilled, the superimposability test can be run concretely atom by atom, and any $S_4$-only small molecule risks matching a memorised textbook species. The porphyrin probe demonstrated that solvers regenerate familiar anchors unprompted, so an unfamiliar scaffold is not optional. A cyclic oligoester of 2-hydroxybutanoic acid matches no memorised species while remaining ordinary chemistry.

## THE GAP

The ester backbone is directional: traversing the ring gives $\mathrm{O} \to \mathrm{CH} \to \mathrm{C(O)}$ throughout. Any operation reversing that traversal is therefore excluded, which kills every $\sigma_v$ and every in-plane $C_2$. The only improper operations left are $\sigma_h$ and the rotoreflections $C_n^k \cdot \sigma_h$, and each of these inverts every stereocentre descriptor.

So, writing the descriptors as a cyclic sequence $c_0 \ldots c_{n-1}$:

> the compound is **achiral** exactly when there exists some shift $k$ with $c_{i+k} = \bar{c_i}$ for every $i$.

The habitual checklist tests only two of the $n$ available shifts: $k = 0$, which is the mirror plane $\sigma_h$, and $k = n/2$, which is the inversion centre. Every other shift is a genuine rotoreflection and is skipped.

**The arithmetic that decides it.** For an alternating sequence the inversion centre exists **iff $n/2$ is odd**. So E4 ($n=6$) hands the checklist an inversion centre and is correctly called achiral, while E1 ($n=4$) and E6 ($n=8$) are achiral through a rotoreflection alone and are wrongly called chiral. E1, E4 and E6 are described in visually identical language.

**Requirement (b) is satisfied by the framing itself.** The prompt's phrase "superimposed on its mirror image" is the unavoidable definition of chirality, and it points the solver straight at the mirror-plane checklist, which is the trap.

---

## PROMPT

```
Eight cyclic oligoesters are described. Each is a macrocyclic ester built from $n$ identical residues of 2-hydroxybutanoic acid, so that the ring consists of the unit $-\mathrm{O}-\mathrm{CH}(\mathrm{C_2H_5})-\mathrm{C(O)}-$ repeated $n$ times and traversed the same way round the whole macrocycle. Every residue therefore carries one stereocentre, at the carbon bearing the ethyl group.

For each compound the configurations of those stereocentres are listed in order, read round the ring in the direction running from the ester oxygen of a residue to the carbonyl carbon of that same residue. Each list is cyclic, the residue following the last being the first.

E1: $n = 4$; R, S, R, S

E2: $n = 4$; R, R, S, S

E3: $n = 4$; R, R, R, S

E4: $n = 6$; R, S, R, S, R, S

E5: $n = 6$; R, R, S, R, S, S

E6: $n = 8$; R, S, R, S, R, S, R, S

E7: $n = 3$; R, R, S

E8: $n = 8$; R, R, S, S, R, R, S, S

Take every macrocycle to be conformationally mobile, with all ring conformations freely accessible, and take the configuration at every stereocentre to be fixed. Regard a compound as chiral when no accessible conformation of it can be superimposed on its mirror image. Disregard any process that makes or breaks a covalent bond, and assume dilute solution in an achiral solvent with no added chiral agent.

How many of the eight compounds are chiral? Report a single integer.
```

---

## GOLDEN

| | $n$ | sequence | achiral? | via | checklist says |
|---|---|---|---|---|---|
| E1 | 4 | R S R S | achiral | $S_4$ only ($k=1$) | chiral **(missed)** |
| E2 | 4 | R R S S | achiral | inversion centre ($k=2$) | achiral |
| E3 | 4 | R R R S | **chiral** | none | chiral |
| E4 | 6 | R S R S R S | achiral | inversion centre ($k=3$) | achiral |
| E5 | 6 | R R S R S S | **chiral** | none | chiral |
| E6 | 8 | R S R S R S R S | achiral | $S_8$ only ($k=1$) | chiral **(missed)** |
| E7 | 3 | R R S | **chiral** | none | chiral |
| E8 | 8 | R R S S R R S S | achiral | rotoreflection ($k=2$) | chiral **(missed)** |

**Chiral: E3, E5, E7. Answer = 3.**

Two structural facts worth stating in the solution:

- **Odd ring size forces chirality (E7).** If $c_{i+k} = \bar{c_i}$ for all $i$, applying the shift $n$ times inverts the descriptors an odd number of times while returning every index to itself, giving $c_i = \bar{c_i}$, which is impossible. So no odd-membered ring of this family is ever achiral, whatever its sequence.
- **E5 is the control that kills the counting shortcut.** It has three R and three S, equal numbers, yet no shift satisfies the condition, so it is chiral. Any rule of the form "equal numbers of R and S implies achiral" fails here.

---

## WRONG BRANCHES (computed; no collision with 3)

| value | route |
|---|---|
| **6** | **primary**: the closed checklist, testing only the mirror plane and the inversion centre; E1, E6 and E8 wrongly called chiral |
| **8** | only a mirror plane sought; since $\sigma_h$ alone can never work here, every compound is called chiral |
| **5** | "alternating implies achiral, otherwise chiral" |
| **5** | odd ring size assumed achiral, even ring size decided by the checklist |
| **4** | any rotationally repeating pattern assumed achiral |
| **2** | "equal numbers of R and S implies achiral" (E5 wrongly called achiral) |
| **2** | the checklist combined with the equal-count rule |
| **0** | improper operations assumed not to invert descriptors, so every compound is called achiral |

Errors run in both directions, so nothing cancels.

## INDEPENDENT VERIFICATION

Script `scratchpad/oligo.py`, `oligo2.py`. The chirality criterion is implemented directly as a search over all $n$ shifts, and each of the eight sequences is evaluated under the correct rule and under seven alternative rules representing plausible shortcuts.

Controls:

- **Convention independence.** The count is 3 under the sequence as written, under reversal of the reading direction, under global exchange of R and S, and under rotation of the starting point by one or by two positions. The reading-direction and starting-point stipulations in the prompt are therefore belt-and-braces rather than load-bearing, and no convention can be disputed into a different answer.
- **The arithmetic condition was verified independently** for $n = 4, 6, 8, 10, 12$: the alternating sequence is always achiral, and the inversion centre is present exactly when $n/2$ is odd.
- **Equal-count chiral sequences were enumerated exhaustively** to confirm E5 is genuinely one of them (12 such sequences exist for $n = 6$).

## COMPLIANCE

- **Nothing advertised.** Scanned programmatically: the prompt contains no occurrence of symmetry, mirror plane, inversion, rotation, operation, axis, face, meso or atropisomer. Only "mirror image" appears, which is the definition of chirality and points at the trap rather than away from it.
- **No governing rule given.** Neither the shift criterion, nor the directionality argument, nor the $n/2$ parity condition appears.
- **Self-contained, and needing no kinetic data at all.** Configurations at stereocentres cannot interconvert, so unlike the previous three tasks this one requires no barriers, no half-lives and no physical constants. Stated explicitly: the repeat unit and its traversal sense, the reading direction, the cyclic nature of each list, free conformational mobility, fixed configuration, the chirality criterion, and the achiral-solvent condition.
- **CURVD**: Contained; Unambiguous (verified invariant to all four conventions above); Reduced (one integer); Verifiable (exhaustive shift search); Discrete (3).
- **Heterogeneous cases**: eight compounds needing five different judgments - rotoreflection-only achirality at two ring sizes, inversion-centre achirality, a non-alternating rotoreflection case, an equal-count chiral case, an odd-ring case, and plain chirality.
- **Deductive ground truth**: a statement about constitution and configuration, with no contested empirical content.
- **Timeless, no PII, pre-cutoff**: no dates, citations or names in the prompt.

## STATUS

Verified. Cold probe recommended before submission, since this is a direct test of the one surviving lever.
