# Planck Task — Tetraradical Quintet Gap (from stump-from-paper workflow)

**Domain:** Chemistry · **Subdomain:** Physical (computational/magnetochemistry)
**Answer type:** decimal, 2 dp · **Final answer: 3.85 kcal/mol** (exact $2.4(\sqrt{13}-2) = 3.8533$; safe margin from rounding boundary)
**Source inspiration:** Chem. Sci. 2025, 16, 430 (doi:10.1039/d4sc05225k) — paper has no tetraradical, no four-spin model, none of these numbers. 100% original.
**Two stacked gates:** (1) heterogeneous Yamaguchi projection — the two pair models sit in OPPOSITE overlap regimes (⟨S²⟩_BS = 0 → factor 1 vs ⟨S²⟩_BS = 1 → factor 2); uniform treatment gives clean wrong answers. (2) non-additivity — rigid-S=1-arm shortcut gives 3.60; exact 4-spin treatment mixes |1,1;0⟩ with |0,0;0⟩ and depresses only the singlet, enlarging the gap to 3.85.
**Verification:** independent 16-dim exact diagonalization (numpy ED + closed form): ground S=0 at −6.253323, quintet at −2.400000, gap 3.853323 = 2.4(√13−2) to 1e-12.
**Proxy status:** Opus 4.8 solved cold, no tools, 376 s (hardest clean solve of session).

---

## PROMPT

A design study in the spirit of pentalene-coupled high-spin diradicals considers a tetraradical $\mathbf{T}$ with four carbon-centered $S=1/2$ radical sites labeled 1–4. Sites 1 and 2 form arm A (two radical centers on one antiaromatic coupler); sites 3 and 4 form the identical arm B; a bridge connects site 2 to site 3. Broken-symmetry (BS) DFT on two pair-model systems gives:

(i) isolated arm (a 1–2 pair): $E_{\mathrm{BS}}-E_{\mathrm{T}}=+7.20$ kcal/mol, with $\langle S^2\rangle_{\mathrm{BS}}=0.00$ and $\langle S^2\rangle_{\mathrm{T}}=2.00$ (strongly overlapping magnetic orbitals);

(ii) bridge contact (a 2–3 pair only): $E_{\mathrm{BS}}-E_{\mathrm{T}}=-2.40$ kcal/mol, with $\langle S^2\rangle_{\mathrm{BS}}=1.00$ and $\langle S^2\rangle_{\mathrm{T}}=2.00$ (essentially disjoint, localized magnetic orbitals).

Convert each BS result to that pair's singlet–triplet gap $\Delta E_{\mathrm{ST}}=E_{\mathrm{S}}-E_{\mathrm{T}}$ (positive means triplet ground state) using the standard approximate spin projection based on the computed $\langle S^2\rangle$ expectation values.

Describe $\mathbf{T}$ by an isotropic Heisenberg spin model containing only the pair interactions 1–2 and 3–4 (arm coupling) and 2–3 (bridge coupling), each coupling fixed so that the corresponding isolated pair would reproduce its projected $\Delta E_{\mathrm{ST}}$; no other pair couplings, no anisotropy, no zero-field splitting.

Treating the four coupled spins exactly (do not assume each arm acts as a rigid $S=1$ unit), compute the energy of the lowest total-spin $S=2$ (quintet) level of $\mathbf{T}$ above its ground level. Report the value in kcal/mol, rounded to two decimal places.

## GOLDEN RESPONSE

**Step 1 — Yamaguchi projection, arm pair.** The standard ⟨S²⟩-based projection is $\Delta E_{\mathrm{ST}} = 2(E_{\mathrm{BS}}-E_{\mathrm{T}})/(\langle S^2\rangle_{\mathrm{T}}-\langle S^2\rangle_{\mathrm{BS}})$. Arm: $2(+7.20)/(2.00-0.00) = +7.20$ kcal/mol — the strong-overlap limit ($\langle S^2\rangle_{\mathrm{BS}}=0$: the BS determinant is already the closed-shell singlet, projection factor 1). Triplet ground pair.

**Step 2 — Yamaguchi projection, bridge pair.** $2(-2.40)/(2.00-1.00) = -4.80$ kcal/mol — the disjoint limit ($\langle S^2\rangle_{\mathrm{BS}}=1$: the BS determinant is a 50/50 singlet-triplet mixture, full factor-2 correction). Singlet ground pair. The two pairs sit in opposite projection regimes; a uniform factor corrupts one of them.

**Step 3 — Map to Heisenberg couplings.** With $\hat H=\sum_{\langle ij\rangle} J_{ij}\,\hat{\vec S}_i\cdot\hat{\vec S}_j$, an isolated spin-½ pair satisfies $E_S - E_T = -J$. Hence $J_a = -7.20$ kcal/mol (ferromagnetic, bonds 1–2 and 3–4) and $J_b = +4.80$ kcal/mol (antiferromagnetic, bond 2–3). (Any convention gives the same spectrum because the couplings are fixed through the observable pair gaps.)

**Step 4 — $S=2$ sector.** In the recoupled basis $|S_{12},S_{34};S\rangle$ the unique quintet is $|1,1;2\rangle$: $E_Q = \tfrac{J_a}{2}+\tfrac{J_a}{2}\cdot 0 \; \Rightarrow \; E_Q = J_a/2 + J_b/4 = -3.60 + 1.20 = -2.40$ kcal/mol (using $\vec S_1\cdot\vec S_2 = \tfrac14$ in each triplet arm and $\langle \vec S_2\cdot\vec S_3\rangle = \tfrac14$ in the stretched state).

**Step 5 — $S=0$ sector (2×2).** Basis $|1,1;0\rangle$, $|0,0;0\rangle$. Diagonal elements: $J_a/2 - J_b/2 = -6.00$ and $-3J_a/2 = +10.80$. Off-diagonal: $(\sqrt3/4)J_b = 1.2\sqrt3$ (so $v^2 = 4.32$). Eigenvalues $2.40 \pm \sqrt{8.40^2 + 4.32} = 2.40 \pm \sqrt{74.88}$; ground singlet $E_0 = 2.40 - \tfrac{12}{5}\sqrt{13} = -6.2533$ kcal/mol.

**Step 6 — $S=1$ check.** The three triplet levels lie at $-5.5267, +3.1267, +4.80$ kcal/mol; all above $E_0$. Ground state is the singlet — the AFM bridge wins over rigid ferromagnetic arms precisely because the $|0,0;0\rangle$ admixture depresses only the singlet.

**Step 7 — Gap.** $E_Q - E_0 = -2.40 - (2.40 - \sqrt{74.88}) = \sqrt{74.88} - 4.80 = 2.4(\sqrt{13}-2) = 3.8533$ kcal/mol.

**Final Answer:** $3.85$ kcal/mol

## Wrong branches (≥6)

| Answer | Error |
|---|---|
| 3.74 | factor-2 projection applied to BOTH pairs (the frontier-model default) |
| 1.87 | factor-1 applied to both / no projection at all |
| 1.84 | regimes swapped (arm ×2, bridge ×1) |
| 3.60 | rigid-S=1 arms + correct projection factor — the additivity trap |
| 14.40 | rigid triplets with bare J_b (missing ¼ spin-projection factor) |
| 7.71 | Heisenberg convention slip (−2J form), doubles spectrum |
| 0.73 | reports gap to lowest S=1 level instead of quintet |
| ≤0 | sign error on bridge ΔE_ST, predicts quintet ground state |

## References (pre-cutoff)

1. Yamaguchi, K. et al. *Chem. Phys. Lett.* **1988**, 149, 537–542. doi:10.1016/0009-2614(88)80378-6 — ⟨S²⟩-based spin projection. *Required: True.*
2. Noodleman, L. *J. Chem. Phys.* **1981**, 74, 5737–5743. doi:10.1063/1.440939 — broken-symmetry method. *Required: False.*
3. Santiago et al. *Chem. Sci.* **2025**, 16, 430–447. doi:10.1039/d4sc05225k (online 21 Nov 2024) — S_ab≈1 projection choice for strongly overlapping diradicals (inspiration). *Required: False.*
