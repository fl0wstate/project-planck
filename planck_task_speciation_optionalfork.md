# Planck Task — Redox Speciation, Optional-Fork + Two-Root (HARDEST VERIFIED)

**Domain:** Chemistry · **Subdomain:** Physical (analytical / coordination equilibria)
**Answer type:** decimal (sum of pH roots, 3 dp) · **Final answer: 12.567**
**Cutoff:** SAFE — pure equilibrium/Nernst, timeless. All numbers original.
**Design:** stacks two vectors — (1) OPTIONAL FORK: a protonated adduct M(HL) with a small-looking formation constant (10² vs 10³ for ML) that is actually the 2nd-largest M(III) species at the acidic root, because [HL⁻] ≈ 630·[L²⁻] there; a solver comparing formation constants drops it → clean wrong sum. (2) NON-MONOTONIC two-root E(pH); sum-framing hides the count and forces finding both.
**Verification:** independent script. Correct roots 4.349 + 8.218 = 12.567, all mass balances exact. M(HL)=9.71×10⁻⁵ M at acidic root > ML+ML₂+MOH combined.
**Proxy status:** Opus 4.8 solved cold — 12.567 — but took **34 minutes** (longest of the entire campaign, 5–6× any other probe). It included M(HL); the omission fork did not catch this (strongest) proxy. Live for weaker platform responders.

---

## PROMPT

```
I am modelling a synthetic $\mathrm{M^{III}}/\mathrm{M^{II}}$ redox mediator equilibrated at $25.00\,^\circ\mathrm{C}$ with a diprotic chelator $\mathrm{H_2L}$, which grips the metal through its fully deprotonated form $\mathrm{L^{2-}}$. Activities are equal to molar concentrations and the ionic strength is held constant. The total concentrations are $C_{\mathrm{III}} = 0.5000\,\mathrm{mM}$, $C_{\mathrm{II}} = 1.5000\,\mathrm{mM}$ and $L_{\mathrm{T}} = 5.0000\,\mathrm{mM}$.

Ligand acidity: $\mathrm{H_2L} \rightleftharpoons \mathrm{H^+} + \mathrm{HL^-}$, $K_{a1} = 1.000\times10^{-4}\,\mathrm{M}$; $\mathrm{HL^-} \rightleftharpoons \mathrm{H^+} + \mathrm{L^{2-}}$, $K_{a2} = 1.000\times10^{-7}\,\mathrm{M}$.

Write $\ell = [\mathrm{L^{2-}}]$, $h = [\mathrm{H^+}]$, $x = [\mathrm{M^{III}}]$ and $y = [\mathrm{M^{II}}]$, every concentration being in $\mathrm{M}$. The metal-binding equilibria available are

$[\mathrm{M^{III}L}] = 10^{3}\,x\ell$ and $[\mathrm{M^{III}L_2}] = 10^{8}\,x\ell^{2}$;

$[\mathrm{M^{II}L}] = 3.000\times10^{5}\,y\ell$ and $[\mathrm{M^{II}L_2}] = 5.000\times10^{8}\,y\ell^{2}$;

and a weak protonated adduct $[\mathrm{M^{III}(HL)}] = 10^{2}\,x\,[\mathrm{HL^-}]$.

Only free $\mathrm{M^{III}}$ hydrolyses: $[\mathrm{MOH^{2+}}]\,h/x = 5.000\times10^{-6}\,\mathrm{M}$. Hydrolysed metal does not bind $\mathrm{L}$.

Enforce both metal mass balances and the full ligand balance, counting each $\mathrm{L_2}$ complex as two ligand equivalents, and $\mathrm{M^{III}(HL)}$ and each mono complex as one.

The electrode responds only to free ions: $E = E^{\circ} + \frac{RT}{F}\ln(x/y)$, with $E^{\circ} = 0.7700\,\mathrm{V}$, $R = 8.3145\,\mathrm{J\,mol^{-1}\,K^{-1}}$, $T = 298.15\,\mathrm{K}$ and $F = 96485\,\mathrm{C\,mol^{-1}}$.

Over the range $2.000 \leq \mathrm{pH} \leq 9.000$ there are exactly two pH values at which $E = 0.7600\,\mathrm{V}$. Report the sum of those two pH values, rounded to three decimal places.
```

## FINAL ANSWER: **12.567**

Roots: pH 4.349 (acidic, M(HL)-dominated) + pH 8.218 (basic, hydrolysis-dominated).

## GOLDEN RESPONSE (structure)

1. **Nernst invariant:** $\ln(x/y)=(0.7600-0.7700)/(RT/F)$, $RT/F=0.0256928$ V → $x/y=0.677587$.
2. **Side-reaction coefficients:** $x=C_{III}/\alpha_{III}$, $y=C_{II}/\alpha_{II}$ where $\alpha_{III}=1+10^3\ell+10^8\ell^2+10^9 h\ell+5\times10^{-6}/h$ (the $10^9 h\ell$ term IS M(HL), since $[HL^-]=10^7 h\ell$) and $\alpha_{II}=1+3\times10^5\ell+5\times10^8\ell^2$. Target: $\alpha_{II}/\alpha_{III}=3(0.677587)=2.03276$.
3. **Ligand balance** closes $\ell$ at each pH: $L_T=\ell(1+10^7 h+10^{11}h^2)+x\ell(10^3+2\times10^8\ell+10^9 h)+y\ell(3\times10^5+10^9\ell)$.
4. **Curve shape:** $\alpha_{II}/\alpha_{III}$ rises from ~1, peaks ~pH 6, collapses at high pH (hydrolysis $5\times10^{-6}/h$ inflates $\alpha_{III}$) → crosses target **twice**.
5. **Roots:** rising side pH 4.349; falling side pH 8.218. **Sum = 12.567.**

## Wrong branches (≥6)

| Answer | Error |
|---|---|
| 12.413 | drops M(HL) as "negligible" (formation constant 10× smaller than ML) — the optional fork; shifts acidic root 4.349→4.195 |
| 12.560 | includes M(HL) in metal balance but forgets it as a ligand equivalent |
| 4.298 | drops hydrolysis → high-pH root vanishes, reports only one root |
| ~12.41 | uses [HL⁻]=ℓ (wrong protonation factor) — reduces to near-omission |
| single value ~4.35 or ~8.22 | finds one root, misses the non-monotonic second |
| 3.74/etc | ionic/stoichiometric slips in ligand balance |
| 8.218 | reports only the basic root (monotonic assumption) |

## References (pre-cutoff)

1. Ringbom, A. *Complexation in Analytical Chemistry*, Wiley, 1963 — side-reaction (alpha) coefficients, conditional constants. *Required: False.*
2. Martell & Motekaitis, *Determination and Use of Stability Constants*, VCH, 1992 — protonated-complex speciation. *Required: False.*

## Honest assessment

Hardest verified task of the campaign — proxy needed 34 min. The M(HL) optional fork is a genuine, classic, ≥6-branch trap (protonated complexes dominate at low pH despite small formation constants), but the strongest proxy included it. Consistent with the campaign finding: rigorous frontier models don't voluntarily truncate given data. Value for submission: (a) it is genuinely PhD-hard and clean; (b) the omission branch (12.413) is exactly the error a weaker or hurried responder makes — and your platform pair has shown slips at far easier problems, so a 1/2 or 2/2 here is plausible in a way it wasn't for the clean forward tasks. Submit and read the traces.
