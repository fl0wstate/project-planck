# Planck Task — Adiabatic Equilibrium with Silent Boiling Pin

**Domain:** Chemistry · **Subdomain:** Physical · **Answer: 1.373** (mol L⁻¹, 3 dp)
**Cutoff:** SAFE (classical thermodynamics; all numbers original).
**Mechanism attacked:** *chain-local verification*. The naive adiabatic solve is fully self-consistent — Q(ξ) = K(T) to machine precision, mass balance exact, direction sensible — yet globally impossible, because it predicts a liquid solution 4.7 K above its boiling point at 1 atm. Every check a solver naturally runs **confirms the wrong answer**.

**Verification (independent script):**
| Path | [C] | note |
|---|---|---|
| **CORRECT** — T pins at bp 351.44 K, equilibrium at K(Tb)=3.4925 | **1.373** | ξ_eq 1.373 > ξ_bp 1.163, so boiling genuinely occurs; 18.5 kJ beyond onset |
| naive adiabatic, no phase check | 1.265 | predicts T = 356.15 K = 4.71 K above bp — impossible |
| isothermal at 298.15 K | 1.949 | ignores self-heating |

Rounding margin 0.000496 (dead mid-bin). Separation correct-vs-naive 0.108 M.

## PROMPT

I'm scaling up a reversible association A + B ⇌ C for a colleague and I need the equilibrium yield before I book the calorimeter.

The charge is $1.000$ L of ethanol containing $2.000$ mol of A and $2.000$ mol of B and no C. Ethanol data: molar mass $46.07$ g mol⁻¹, density $0.789$ g mL⁻¹ at 298 K, normal boiling point $351.44$ K. The flask is heavily insulated, so no heat is exchanged with the surroundings through the walls, and it is held open to the atmosphere at $1.000$ atm through a drying tube. The contents start at $298.15$ K.

For the reaction, take $\Delta H^\circ = -88.00$ kJ mol⁻¹ and $\Delta S^\circ = -240.0$ J mol⁻¹ K⁻¹, both independent of temperature. The equilibrium constant is $K = [\mathrm{C}]/([\mathrm{A}][\mathrm{B}])$ with all concentrations in mol L⁻¹ referred to a $1$ mol L⁻¹ standard state, and $\ln K = -\Delta G^\circ/(RT)$ with $R = 8.3145$ J mol⁻¹ K⁻¹.

Take the liquid volume as fixed at $1.000$ L throughout, and the heat capacity of the whole charge as constant at $1.920$ kJ K⁻¹. Assume the solution behaves ideally and that A, B, and C are non-volatile.

The mixture is left to reach equilibrium with no stirring input and no cooling.

What is the equilibrium concentration of C, in mol L⁻¹, rounded to three decimal places?

## GOLDEN RESPONSE

1. **K(T):** $\ln K = \dfrac{88000 - 240.0\,T}{8.3145\,T} = \dfrac{10583.9}{T} - 28.8653$.
2. **Adiabatic ramp:** with $x$ = mol C formed in 1.000 L, $T = 298.15 + \dfrac{88.00x}{1.920} = 298.15 + 45.833x$.
3. **Boundary:** the flask is open at 1.000 atm, so the liquid cannot exceed $351.44$ K. That temperature is reached at $x = (351.44-298.15)/45.833 = 1.1627$ mol.
4. **Is the boundary actually crossed?** At $x = 1.1627$: $Q = 1.1627/(0.8373)^2 = 1.659$, while $K(351.44) = 3.4925$. Since $Q < K$ the reaction is not yet at equilibrium when the boiling point is reached, so it must continue.
5. **Regime change:** beyond that point the released enthalpy goes into latent heat, not sensible heat; $T$ is pinned at $351.44$ K. Equilibrium is therefore set by $K$ at $351.44$ K.
6. **Solve:** $x/(2.000-x)^2 = 3.49254 \Rightarrow 3.49254x^2 - 14.97016x + 13.97016 = 0$; discriminant $28.9403$, $\sqrt{} = 5.37962$; $x = (14.97016-5.37962)/6.98508 = 1.37300$. (Other root > 2, unphysical.)
7. **Check:** $1.3730/(0.6270)^2 = 3.492$ ✓.

**Final Answer: 1.373**

## Wrong branches

| Answer | Error |
|---|---|
| **1.265** | solves the adiabatic energy balance and equilibrium simultaneously with no phase-boundary check — predicts 356.15 K, above the boiling point |
| **1.949** | isothermal at 298.15 K; ignores self-heating |
| 2.000 | assumes K(298) ≈ 760 drives essentially complete conversion |
| 1.163 | stops the reaction at the boiling-point onset instead of continuing to equilibrium there |
| ~1.15 | uses ΔG° at 298 K but the adiabatic T in the exponent inconsistently |
| ~1.94 | sign error on ΔS° |

## References (pre-cutoff)

1. Denbigh, K. *The Principles of Chemical Equilibrium*, 4th ed., CUP, 1981 — van 't Hoff / adiabatic reaction equilibria. *Required: False.*
2. Smith, Van Ness, Abbott, *Introduction to Chemical Engineering Thermodynamics*, 7th ed., McGraw-Hill, 2005 — adiabatic reactor energy balance, boiling constraint. *Required: False.*

## Honest assessment — solved by proxy in 61 s

The proxy found it, and the trace shows the exact defeating heuristic: **it bounded the problem before solving.** It computed full conversion → 176 kJ → ~390 K, compared that to 351.44 K immediately, and the pin fell out. Extreme-case bounding is routine in its method, so concealing a boundary crossing does not work — the boundary is found by a check that costs nothing.

Still a strong submittable task: genuine PhD-level regime reasoning, three well-separated branches, boundary-safe, original, cutoff-safe.
