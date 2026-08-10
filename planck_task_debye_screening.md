# Planck Task — Debye-Screened Lysine Repulsion (timeless physics, post-cutoff-safe)

**Domain:** Chemistry · **Subdomain:** Physical
**Answer type:** decimal (kJ/mol, 2 dp) · **Final answer: 2.80**
**Cutoff status:** SAFE. Inspired by JACS Au 2026 SepF salt-switch paper (post-cutoff, NOT cited, NOT required). Problem rests entirely on Debye–Hückel theory (1923) — timeless. Every number is original, none from the paper. Pre-cutoff references only.
**Difficulty tier:** HARD but NOT a verified stump — Opus 4.8 proxy solved it cold in 88 s, no tools. Submittable as a legitimate PhD physical-chemistry task; do NOT expect a 2/2 platform failure.
**Verification:** independent script. Answer 2.7962 → 2.80 kJ/mol. Wrong branches well-separated. εr sensitivity (78.0–78.5) negligible → no rounding-boundary hazard.

---

## PROMPT

A short cationic peptide segment carries three protonated lysine side-chain charges that I model as three point charges of $+1e$ each, held in a fixed collinear arrangement with a uniform nearest-neighbour spacing of $0.70\ \mathrm{nm}$ (so the three pairwise separations are $0.70\ \mathrm{nm}$, $0.70\ \mathrm{nm}$, and $1.40\ \mathrm{nm}$). The segment sits in bulk water, treated as a uniform dielectric continuum with relative permittivity $78.4$ at the working temperature of $298.15\ \mathrm{K}$.

The electrostatic interaction between any two of these charges is screened by the surrounding electrolyte and is described by the Debye–Hückel screened Coulomb (Yukawa) potential, with the Debye screening length computed from the total ionic strength of the electrolyte in the usual way (ionic strength $I = \tfrac{1}{2}\sum_i c_i z_i^2$, summed over all mobile ionic species, molar concentrations).

The electrolyte is a mixed aqueous solution containing $50\ \mathrm{mM}$ NaCl and $15\ \mathrm{mM}$ MgCl$_2$. The peptide's own charges do not contribute to the ionic strength.

Constants: elementary charge $e = 1.602176634\times10^{-19}\ \mathrm{C}$; vacuum permittivity $\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$; Boltzmann constant $k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$; Avogadro constant $N_A = 6.02214076\times10^{23}\ \mathrm{mol^{-1}}$.

Compute the total electrostatic interaction energy of the three-charge assembly (the sum over all three unique pairs) under these conditions. Report the answer in kJ/mol, rounded to 2 decimal places.

## GOLDEN RESPONSE (structure)

**Step 1 — Ionic strength.** Na⁺ 0.050 (z²=1), Cl⁻ 0.050+0.030=0.080 (z²=1), Mg²⁺ 0.015 (z²=4). $I = \tfrac12(0.050 + 0.080 + 0.015\cdot4) = \tfrac12(0.190) = 0.095\ \mathrm{M} = 95\ \mathrm{mol\,m^{-3}}$.

**Step 2 — Debye length.** $\kappa^2 = 2 N_A e^2 I/(\varepsilon_0 \varepsilon_r k_B T) = 1.0279\times10^{18}\ \mathrm{m^{-2}}$; $\kappa = 1.01384\times10^{9}\ \mathrm{m^{-1}}$; $\kappa^{-1} = 0.9863\ \mathrm{nm}$.

**Step 3 — Prefactor.** $e^2/(4\pi\varepsilon_0\varepsilon_r) = 2.94269\times10^{-30}\ \mathrm{J\,m}$ (Bjerrum length 0.715 nm).

**Step 4 — Pairwise (Yukawa $U=\frac{e^2}{4\pi\varepsilon_0\varepsilon_r}\frac{e^{-\kappa r}}{r}$).** r=0.70 nm: $\kappa r=0.7097$, $U=2.0674\times10^{-21}$ J (×2). r=1.40 nm: $\kappa r=1.4194$, $U=5.0838\times10^{-22}$ J.

**Step 5 — Total.** $2(2.0674\times10^{-21}) + 5.0838\times10^{-22} = 4.6433\times10^{-21}$ J $\times N_A = 2796.2$ J/mol.

**Final Answer:** $2.80$ kJ/mol.

## Wrong branches

| Answer | Error |
|---|---|
| 3.09 | uses z=1 for Mg²⁺ (misses z²=4), I=0.0725 M |
| 3.21 | treats total salt 65 mM as ionic strength directly |
| 3.48 | ignores MgCl₂ entirely, I=0.050 M |
| 2.49 | drops the 1.40 nm (1–3) pair |
| 3.74 | uses 0.70 nm for all three pairs |
| 6.33 | bare (unscreened) Coulomb, κ→0 |
| ~5.5 | forgets the ×2 on the two equal near pairs / other miscount |

## References (all pre-cutoff, timeless)

1. Debye, P.; Hückel, E. *Physikalische Zeitschrift* **1923**, 24, 185–206 — screened potential, Debye length. *Required: False.*
2. Israelachvili, J. *Intermolecular and Surface Forces*, 3rd ed., Academic Press, 2011 — Yukawa/DLVO electrostatics, ionic strength. https://www.elsevier.com/books/intermolecular-and-surface-forces/israelachvili/978-0-12-375182-9 *Required: False.*

## Honest assessment

Clean, self-contained, original, cutoff-safe, PhD-level — a solid SUBMITTABLE task. But it is a forward calculation: the proxy solved it in one pass. The "forks" (mixed ionic strength, three pairwise terms) are diligence checks a strong model passes. This is the submittable-quality tier, not the verified-stump tier. The salt-inversion conceptual insight from the source paper is *context* here, not load-bearing on the numeric answer — which is exactly why it does not stump. To weaponize the inversion would require a threshold/optimization framing (min salt to fold), which introduces transcendental hand-solving = arithmetic-slip risk that planck excludes. Recommend submitting as a difficulty-diverse entry, not as a stump attempt.
