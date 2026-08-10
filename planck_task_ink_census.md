# Planck Task — Zn-Ink Viability Census (case-volume, 16 cases)

**Domain:** Chemistry · **Subdomain:** Physical
**Answer type:** integer · **Final answer: 5** (viable: A, B, E, F, H)
**Source inspiration:** ChemRxiv 2024-5rhzp / ACS AMI 2025, 17, 38215 (doi:10.1021/acsami.5c05599) — printed Zn microbattery. Original numbers throughout.
**Design:** 16 cases × 2 conceptual subtests, single integer aggregate. Dropped/botched case = wrong integer = planck-valid "missing critical step." Gates: (1) momentum balance τ_w = PR/(2L) — never given; (2) plug AREA ≥ ½ means ratio ≥ 1/√2 = 0.7071, not 0.5 — cases I(0.55), J(0.60), K(0.65), L(0.68) planted in the radius-shortcut flip zone; (3) O, P have τ_y > τ_w — no flow at all despite "area fraction" ≥ ½ formally; (4) per-case Faraday n=2; (5) H₂ flux ↔ Zn loss is 1:1 molar (2e⁻ each side) — halving/doubling flips D or B,F,H.
**Verification:** independent enumeration script. T1 pass: A–H; T2 kills C(4.88>2.5), D(5.88>3.5), G(3.96>2.8). Viable 5. Margins all ≥8%.
**Proxy status:** Opus 4.8 solved, no tools, 36 s — batched the cases by pressure into interval checks. LESSON: homogeneous cases collapse under batching; platform responders (July-2025) still face the 1/√2 and clog gates.

---

## PROMPT

A direct-ink-writing lab screens 16 candidate zinc-anode inks (Zn powder + carbon black + PVA binder in water) for printed aqueous microbatteries. Each ink is a Bingham yield-stress fluid with yield stress $\tau_y$. Printing uses a cylindrical nozzle of inner radius $R = 150\ \mu\mathrm{m}$; the listed constant applied gauge pressure $P$ drops entirely across fully developed, steady laminar flow in the nozzle land of length $L = 12\ \mathrm{mm}$ (neglect gravity and entrance effects).

An ink is VIABLE only if it passes both tests.

T1 (printability): the ink must extrude under its listed pressure, and the unyielded plug core must carry at least half of the nozzle's cross-sectional area (otherwise shear destroys the percolated carbon-black network).

T2 (shelf life): a printed anode with zinc areal loading $m$ rests 500 h at open circuit in the gel electrolyte; corrosion must consume no more than 10% of the initial zinc mass. Hydrogen evolution is the sole cathodic corrosion process. Each ink's corrosion is characterized by exactly one exact measurement at this open-circuit condition: either the corrosion current density $i$ (in $\mu\mathrm{A\,cm^{-2}}$) or the steady hydrogen gas evolution flux $v$ (in $\mathrm{nmol\,s^{-1}\,cm^{-2}}$).

Data per ink — $\tau_y$ (Pa); $P$ (kPa); corrosion; $m$ (mg cm⁻²):
A: 225; 48; $i=3.0$; 30
B: 200; 40; $v=0.010$; 20
C: 336; 64; $i=8.0$; 25
D: 176; 32; $v=0.050$; 35
E: 315; 56; $i=2.0$; 15
F: 276; 48; $v=0.020$; 40
G: 190; 32; $i=6.5$; 28
H: 195; 40; $v=0.012$; 18
I: 165; 48; $i=1.0$; 30
J: 210; 56; $v=0.008$; 25
K: 130; 32; $i=2.5$; 20
L: 170; 40; $v=0.060$; 30
M: 160; 64; $i=1.5$; 35
N: 135; 48; $v=0.015$; 45
O: 220; 32; $i=2.0$; 30
P: 375; 48; $v=0.005$; 25

Constants: $F = 96485\ \mathrm{C\,mol^{-1}}$; $M_{\mathrm{Zn}} = 65.38\ \mathrm{g\,mol^{-1}}$; $1\ \mathrm{h} = 3600\ \mathrm{s}$.

How many of the 16 inks are viable? Answer with a single integer.

## GOLDEN RESPONSE (structure)

**Step 1 — Wall stress.** Force balance on the nozzle land: $\tau_w = PR/(2L) = 6.25\,P$ (τ_w in Pa, P in kPa). Per pressure: 32→200, 40→250, 48→300, 56→350, 64→400 Pa.

**Step 2 — T1 criterion.** Bingham flow exists only if $\tau_y < \tau_w$. The unyielded plug has radius $r_p = R\,\tau_y/\tau_w$; plug area fraction $= (\tau_y/\tau_w)^2 \ge 1/2 \Leftrightarrow \tau_y/\tau_w \ge 1/\sqrt2 = 0.7071$. So T1 ⇔ $0.7071 \le \tau_y/\tau_w < 1$.

**Step 3 — T1 sweep (ratios).** A 0.750✓ B 0.800✓ C 0.840✓ D 0.880✓ E 0.900✓ F 0.920✓ G 0.950✓ H 0.780✓ I 0.550✗ J 0.600✗ K 0.650✗ L 0.680✗ (area 0.462 < ½) M 0.400✗ N 0.450✗ O 1.100✗ (no flow) P 1.250✗ (no flow). Survivors: A–H.

**Step 4 — T2 conversions.** $t = 1.8\times10^6$ s. Current-type: $\Delta m = i\,t\,M_{\mathrm{Zn}}/(2F) = 0.6099\,i$ mg cm⁻² (n = 2). Flux-type: each H₂ takes 2 e⁻ = one Zn, so $\Delta m = v \times 10^{-9} \times 1.8\times10^6 \times 65.38\times10^3 = 117.7\,v$ mg cm⁻².

**Step 5 — T2 sweep (loss vs 0.1 m).** A 1.83≤3.0✓ B 1.18≤2.0✓ C 4.88>2.5✗ D 5.88>3.5✗ E 1.22≤1.5✓ F 2.35≤4.0✓ G 3.96>2.8✗ H 1.41≤1.8✓.

**Step 6 — Count.** Viable: A, B, E, F, H.

**Final Answer:** $5$

## Wrong branches

| Answer | Error |
|---|---|
| 8 | plug RADIUS fraction ≥ ½ instead of area (passes I, J, K) |
| 7 | misses the no-flow gate, passes O and P via formal area ≥ ½ |
| 10 | both errors above |
| 2 | 2 Zn per H₂ (electron double-count), fails B, F, H |
| 6 | ½ Zn per H₂, passes D |
| 3 | n = 1 in Faraday for i-type inks, fails A and E |
| 4 | one dropped/miscomputed case in either sweep |
| 9 | radius-shortcut + passes L too |

## References (pre-cutoff)

1. Tagliaferri et al. ACS Appl. Mater. Interfaces 2025, 17, 38215–38224. doi:10.1021/acsami.5c05599 (ChemRxiv 2024-12-31) — printed Zn ink rheology, corrosion quantification. *Required: False.*
2. Bird, R. B.; Dai, G. C.; Yarusso, B. J. Rev. Chem. Eng. 1983, 1, 1–70 — Bingham plug flow. *Required: False.*
