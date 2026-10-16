# Author review: adiabatic_regime

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/adiabatic_regime/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
I'm scaling up a reversible association A + B ⇌ C for a colleague and I need the equilibrium yield before I book the calorimeter.

The charge is $1.000$ L of ethanol containing $2.000$ mol of A and $2.000$ mol of B and no C. Ethanol data: molar mass $46.07$ g mol⁻¹, density $0.789$ g mL⁻¹ at 298 K, normal boiling point $351.44$ K. The flask is heavily insulated, so no heat is exchanged with the surroundings through the walls, and it is held open to the atmosphere at $1.000$ atm through a drying tube. The contents start at $298.15$ K.

For the reaction, take $\Delta H^\circ = -88.00$ kJ mol⁻¹ and $\Delta S^\circ = -240.0$ J mol⁻¹ K⁻¹, both independent of temperature. The equilibrium constant is $K = [\mathrm{C}]/([\mathrm{A}][\mathrm{B}])$ with all concentrations in mol L⁻¹ referred to a $1$ mol L⁻¹ standard state, and $\ln K = -\Delta G^\circ/(RT)$ with $R = 8.3145$ J mol⁻¹ K⁻¹.

Take the liquid volume as fixed at $1.000$ L throughout, and the heat capacity of the whole charge as constant at $1.920$ kJ K⁻¹. Assume the solution behaves ideally and that A, B, and C are non-volatile.

The mixture is left to reach equilibrium with no stirring input and no cooling.

What is the equilibrium concentration of C, in mol L⁻¹, rounded to three decimal places?
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$1.373$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 3}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
1. **K(T):** $\ln K = \dfrac{88000 - 240.0\,T}{8.3145\,T} = \dfrac{10583.9}{T} - 28.8653$.
2. **Adiabatic ramp:** with $x$ = mol C formed in 1.000 L, $T = 298.15 + \dfrac{88.00x}{1.920} = 298.15 + 45.833x$.
3. **Boundary:** the flask is open at 1.000 atm, so the liquid cannot exceed $351.44$ K. That temperature is reached at $x = (351.44-298.15)/45.833 = 1.1627$ mol.
4. **Is the boundary actually crossed?** At $x = 1.1627$: $Q = 1.1627/(0.8373)^2 = 1.659$, while $K(351.44) = 3.4925$. Since $Q < K$ the reaction is not yet at equilibrium when the boiling point is reached, so it must continue.
5. **Regime change:** beyond that point the released enthalpy goes into latent heat, not sensible heat; $T$ is pinned at $351.44$ K. Equilibrium is therefore set by $K$ at $351.44$ K.
6. **Solve:** $x/(2.000-x)^2 = 3.49254 \Rightarrow 3.49254x^2 - 14.97016x + 13.97016 = 0$; discriminant $28.9403$, $\sqrt{} = 5.37962$; $x = (14.97016-5.37962)/6.98508 = 1.37300$. (Other root > 2, unphysical.)
7. **Check:** $1.3730/(0.6270)^2 = 3.492$ ✓.

**Final Answer: 1.373**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $1.373$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Identifies the equilibrium temperature as the boiling point, $351.44\,\mathrm{K}$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $K(351.44\,\mathrm{K})\approx3.4925$.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Denbigh, K. *The Principles of Chemical Equilibrium*, 4th ed., CUP, 1981 — van 't Hoff / adiabatic reaction equilibria. *Required: False.*
2. Smith, Van Ness, Abbott, *Introduction to Chemical Engineering Thermodynamics*, 7th ed., McGraw-Hill, 2005 — adiabatic reactor energy balance, boiling constraint. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_adiabatic_regime.md](../../planck_task_adiabatic_regime.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
