# Golden Solution — porphyrin atropisomer census (answer 41)

**Step 1.** Count a structure as a separate stereoisomer only if it is isolable at $25\,^\circ\mathrm{C}$ over a period of hours, and count enantiomers as distinct.

**Step 2.** The stated barrier for rotation about each meso-carbon–aryl bond is $\Delta G^{\ddagger} \geq 30\,\mathrm{kcal\,mol^{-1}}$, which at $25\,^\circ\mathrm{C}$ gives a half-life of decades, so every aryl orientation is frozen on that timescale.

**Step 3.** Each ortho-substituted aryl group therefore contributes one binary variable: its ortho substituent points towards one face of the macrocycle or towards the other.

**Step 4.** A meso position bearing hydrogen contributes no variable.

**Step 5.** Write the state of a molecule as the list of face labels at positions 5, 10, 15, 20.

**Step 6.** Two states are the same stereoisomer exactly when some symmetry operation of the framework that preserves the pattern of aryl identities carries one state into the other.

**Step 7.** Restrict that set to *proper rotations* only: improper operations relate a molecule to its mirror image, and enantiomers are counted as distinct here.

**Step 8.** The idealised planar porphine framework has proper rotation group $D_4$, of order 8 — $E$, $C_4$, $C_4^2$, $C_4^3$ about the axis normal to the mean plane; two $C_2$ axes in the plane through opposite meso carbons; two $C_2$ axes in the plane through opposite pyrrole units.

**Step 9.** The $C_4^k$ rotations permute the meso positions cyclically and leave every face label unchanged, since the normal axis maps each face to itself.

**Step 10.** Each in-plane $C_2$ turns the macrocycle over, so it permutes the meso positions *and* inverts every face label.

**Step 11.** The nickel is four-coordinate with no axial ligand, so the two faces are genuinely equivalent and the operations of Step 10 are true symmetries of the molecule.

**Step 12.** Label the meso positions $p_1, p_2, p_3, p_4$ for 5, 10, 15, 20, and record each operation as a permutation plus a face-inversion flag:

| operation | permutation | inverts faces |
|---|---|---|
| $E$ | — | no |
| $C_4$, $C_4^3$ | 4-cycle | no |
| $C_4^2$ | $(p_1p_3)(p_2p_4)$ | no |
| $C_2(\mathrm{A})$, through 5–15 | fixes $p_1,p_3$; swaps $p_2,p_4$ | yes |
| $C_2(\mathrm{B})$, through 10–20 | fixes $p_2,p_4$; swaps $p_1,p_3$ | yes |
| $C_2(\mathrm{C})$, through pyrroles bisecting 5–10 and 15–20 | $(p_1p_2)(p_3p_4)$ | yes |
| $C_2(\mathrm{D})$, through pyrroles bisecting 10–15 and 20–5 | $(p_2p_3)(p_1p_4)$ | yes |

**Step 13.** For each case, keep only the operations preserving the aryl identity pattern, then count orbits of the state set by Burnside's lemma: orbits $= \frac{1}{|G|}\sum_{g \in G}(\text{states fixed by } g)$.

---

**Step 14.** Q1 has Ar1 at $p_1,p_3$ and Ar2 at $p_2,p_4$; the operations preserving this pattern are $E$, $C_4^2$, $C_2(\mathrm{A})$ and $C_2(\mathrm{B})$, so $|G| = 4$.

**Step 15.** Q1 has $2^4 = 16$ states, and $E$ fixes all 16.

**Step 16.** $C_4^2$ fixes the states with $b_1 = b_3$ and $b_2 = b_4$: 4 states.

**Step 17.** $C_2(\mathrm{A})$ leaves $p_1$ and $p_3$ in place while inverting their labels, requiring $b = \neg b$, so it fixes 0; $C_2(\mathrm{B})$ fixes 0 for the same reason at $p_2, p_4$.

**Step 18.** Q1 count $= (16 + 4 + 0 + 0)/4 = \mathbf{5}$.

**Step 19.** Q2 has Ar1 at $p_1,p_2$ and Ar2 at $p_3,p_4$; the only nontrivial operation preserving this is $C_2(\mathrm{C})$, which swaps $p_1 \leftrightarrow p_2$ and $p_3 \leftrightarrow p_4$ within each identical pair, so $|G| = 2$.

**Step 20.** $E$ fixes all 16 states.

**Step 21.** $C_2(\mathrm{C})$ fixes the states with $b_1 = \neg b_2$ and $b_3 = \neg b_4$: $2 \times 2 = 4$ states.

**Step 22.** Q2 count $= (16 + 4)/2 = \mathbf{10}$.

**Step 23.** Q3 has Ar1 at $p_1,p_3$ and hydrogen at $p_2,p_4$, so only two labels vary and there are $2^2 = 4$ states; the preserving operations are $E$, $C_4^2$, $C_2(\mathrm{A})$, $C_2(\mathrm{B})$, so $|G| = 4$.

**Step 24.** $E$ fixes 4, and $C_4^2$ swaps $p_1 \leftrightarrow p_3$ without inversion, fixing the states with $b_1 = b_3$: 2.

**Step 25.** $C_2(\mathrm{A})$ holds $p_1$ and $p_3$ in place while inverting, fixing 0; $C_2(\mathrm{B})$ swaps $p_1 \leftrightarrow p_3$ *and* inverts, fixing the states with $b_1 = \neg b_3$: 2.

**Step 26.** Q3 count $= (4 + 2 + 0 + 2)/4 = \mathbf{2}$.

**Step 27.** Q4 has four different aryl groups, so no nontrivial rotation preserves the pattern and $|G| = 1$.

**Step 28.** Q4 count $= 2^4/1 = \mathbf{16}$.

**Step 29.** Q5 has Ar1 at $p_1,p_2,p_3$ and Ar2 at $p_4$; any preserving operation must hold $p_4$ fixed, leaving only $E$ and $C_2(\mathrm{B})$, so $|G| = 2$.

**Step 30.** $E$ fixes 16, and $C_2(\mathrm{B})$ holds $p_2$ and $p_4$ in place while inverting their labels, which is impossible, so it fixes 0.

**Step 31.** Q5 count $= (16 + 0)/2 = \mathbf{8}$.

**Step 32.** Sum the five counts: $5 + 10 + 2 + 16 + 8$.

**Final Answer: 41**

---

## CHECKS

- **Textbook control.** Four identical ortho-substituted aryl groups returns 4 under this group — the standard $\alpha\alpha\alpha\alpha$, $\alpha\alpha\alpha\beta$, $\alpha\alpha\beta\beta$, $\alpha\beta\alpha\beta$ atropisomer set. Under the truncated group it returns 6, so the control discriminates.
- **Q4 relationship.** 16 under proper rotations and 8 under the full group, the expected factor of two for 8 enantiomeric pairs.
- **Q1 by hand.** Burnside worked independently in Steps 15–18, matching the script.
- **Script.** `scratchpad/porph2.py`, `porph3.py` — all sixteen framework operations represented as (permutation, face-inversion flag, proper/improper flag), orbits by union-find, run under four group choices.

## OBSERVED PLATFORM FAILURES (2026-07-31, 2/2)

Both responses truncated the proper rotation group to order 4, keeping $C_2(z)$ and the meso-axis $C_2$'s while dropping $C_4$, $C_4^3$, $C_2(\mathrm{C})$ and $C_2(\mathrm{D})$.

| | golden | R1 | R2 |
|---|---|---|---|
| Q1 | 5 | 5 | 5 |
| Q2 | **10** | 16 | 16 |
| Q3 | 2 | 2 | 2 |
| Q4 | 16 | 16 | 16 |
| Q5 | **8** | 16 | 8 |
| sum | **41** | **55** | **47** |

Step 12's $C_2(\mathrm{C})$ is the operation both missed, and Step 22 is where it changes the count. Step 29's $C_2(\mathrm{B})$ is the one R1 additionally missed. Every Burnside sum in both responses is internally correct given its own wrong group, so these are errors in constructing the symmetry group, not arithmetic slips.
