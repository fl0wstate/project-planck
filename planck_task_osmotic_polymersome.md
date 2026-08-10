# Planck Task — Polymersome Osmotic Deflation (colligative Mn/Mw fork)

**Domain:** Chemistry · **Subdomain:** Physical
**Answer type:** integer (nm) · **Final answer: 203**
**Source inspiration:** Peters, Charleston, van Eck, van Berlo, Wilson, *Beilstein J. Org. Chem.* **2025**, 21, 47–54, doi:10.3762/bjoc.21.5 (published 08 Jan 2025 — PRE-CUTOFF, open access, primary text verified directly). Paper used for context only (PSar osmotic shock driving stomatocyte formation); all numbers original, no paper value load-bearing.
**Cutoff:** SAFE.
**Verification:** independent script. V/V₀ = 1.800/3.782 = 0.47594; R = 260.0 × 0.47594^(1/3) = 202.997 → **203 nm**. Boundary margin 0.497 nm (dead-centre of the rounding bin). All wrong branches ≥ 9 nm away.

---

## PROMPT (submission version)

We assemble polysarcosine–poly(benzyl glutamate) polymersomes by solvent exchange and then deflate them by osmotic shock to drive the stomatocyte transformation. I'm trying to predict how far a batch should shrink before I book cryo-TEM time.

The vesicles come out of assembly as spheres of outer radius $260.0$ nm, suspended in the assembly buffer, which is $0.900$ mM NaCl in water. The same buffer fills the vesicle lumen, so the suspension starts perfectly isotonic. Treat NaCl as fully dissociated and treat every solute as ideal and obeying van 't Hoff behaviour.

To apply the shock I take $495.0\ \mu$L of that vesicle suspension and stir in $5.00\ \mu$L of a polysarcosine solution at $400.0$ mg/mL, made up in pure water. The polysarcosine is a laboratory batch from our own ring-opening polymerisation; light scattering puts its weight-average molar mass at $2.60$ kg/mol, and the GPC trace gives a dispersity of $1.30$. Polysarcosine is non-ionic.

After the addition the system is held at $70\ ^\circ$C and allowed to reach osmotic equilibrium. The vesicle membrane is permeable to water but completely impermeable to sodium ions, chloride ions, and polysarcosine, so the amount of NaCl trapped inside each vesicle is fixed. The vesicles are dilute enough that the water they expel does not measurably change the composition of the external medium, and the membrane is floppy enough to exert negligible tension, so equilibrium is reached when the total solute osmolarity is equal on the two sides of the membrane. The vesicles stay spherical throughout, and the membrane volume itself is negligible.

What is the outer radius of the vesicles at osmotic equilibrium? Give your answer in nanometres, rounded to the nearest whole nanometre.

## GOLDEN RESPONSE

**Step 1 — Colligative averaging.** Osmotic pressure counts particles, so the relevant average is the *number*-average molar mass: $M_n = M_w/Đ = 2.60/1.30 = 2.00$ kg/mol.

**Step 2 — Temperature cancels.** Van 't Hoff gives $\Pi = icRT$; the same $RT$ appears on both sides, so equilibrium is equality of total osmolarity. The 70 °C is not needed.

**Step 3 — External NaCl after dilution.** Volumes additive: $495.0+5.00 = 500.0\ \mu$L. $0.900\ \text{mM} \times (495.0/500.0) = 0.891$ mM; fully dissociated ($i=2$) → $1.782$ mOsm/L.

**Step 4 — External polysarcosine.** Mass $= 5.00\ \mu\text{L} \times 400.0\ \text{mg/mL} = 2.00$ mg, in $500.0\ \mu$L → $4.00$ g/L. Non-ionic ($i=1$): $4.00/2000 = 2.00\times10^{-3}$ M → $2.000$ mOsm/L.

**Step 5 — Total external osmolarity.** $1.782 + 2.000 = 3.782$ mOsm/L (fixed; vesicles dilute).

**Step 6 — Interior.** Trapped NaCl fixed in amount, so osmolarity scales as $1/V$. Initial interior $= 0.900 \times 2 = 1.800$ mOsm/L.

**Step 7 — Balance.** $1.800\,(V_0/V_1) = 3.782 \Rightarrow V_1/V_0 = 0.47594$.

**Step 8 — Radius.** $R_1/R_0 = 0.47594^{1/3} = 0.78076$; $R_1 = 260.0 \times 0.78076 = 203.0$ nm.

**Final Answer: 203**

## Wrong branches

| Answer (nm) | Error |
|---|---|
| **212** | uses $M_w$ directly (colligative averaging error — the primary fork) |
| **176** | treats NaCl as $i=1$ (not dissociated) |
| **187** | both of the above |
| **54** | uses the 400 mg/mL stock concentration, ignoring dilution into 500 µL |
| 260 | concludes no net flux (misses that PSar raises external osmolarity) |
| ~228 | applies the volume ratio to the radius directly (omits the cube root) |
| 203 (via 202.68) | ignores the 495/500 dilution of NaCl — same rounded answer, harmless |

## References (pre-cutoff)

1. Peters, R.; Charleston, L. A.; van Eck, K.; van Berlo, T.; Wilson, D. A. *Beilstein J. Org. Chem.* **2025**, *21*, 47–54. doi:10.3762/bjoc.21.5 (published 08 January 2025) — PSar osmotic shock, stomatocyte morphogenesis. *Required: False.*
2. van 't Hoff, J. H. *Z. Phys. Chem.* **1887**, *1*, 481–508 — osmotic pressure law. *Required: False.*

## Honest assessment — NOT a verified stump

Two cold probes, both solved, and this is the decisive finding:

- **Variant A** (gave both $M_n$ and $M_w$): solved in **35 s**. The probe wrote *"This is where the GPC data earns its keep"* and named the $M_w$ error unprompted.
- **Variant B** (gave only $M_w$ and Đ, forcing $M_n = M_w/Đ$ — intended as the hardening): solved in **25 s**, *faster*, opening with the literal words **"Key trap first:"** and disposing of both the colligative fork and the temperature red herring before doing any arithmetic.

Hardening made it *easier*. The proxy approaches these problems as trap-hunting exercises by default, so making a fork more consequential simply makes it more findable. This is the same pattern seen across ~21 tasks in this campaign: **any fork legible enough to be load-bearing is legible enough to be spotted.**

Value for submission: genuinely PhD-level, clean, original, cutoff-safe, with a real classic error ($M_w$ for a colligative property) that weaker or hurried responders do commit. Submit as a quality/diversity entry — not with an expectation of 2/2.
