# Author review: speciation_optionalfork

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/speciation_optionalfork/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
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
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$12.567$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 3}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
1. **Nernst invariant:** $\ln(x/y)=(0.7600-0.7700)/(RT/F)$, $RT/F=0.0256928$ V → $x/y=0.677587$.
2. **Side-reaction coefficients:** $x=C_{III}/\alpha_{III}$, $y=C_{II}/\alpha_{II}$ where $\alpha_{III}=1+10^3\ell+10^8\ell^2+10^9 h\ell+5\times10^{-6}/h$ (the $10^9 h\ell$ term IS M(HL), since $[HL^-]=10^7 h\ell$) and $\alpha_{II}=1+3\times10^5\ell+5\times10^8\ell^2$. Target: $\alpha_{II}/\alpha_{III}=3(0.677587)=2.03276$.
3. **Ligand balance** closes $\ell$ at each pH: $L_T=\ell(1+10^7 h+10^{11}h^2)+x\ell(10^3+2\times10^8\ell+10^9 h)+y\ell(3\times10^5+10^9\ell)$.
4. **Curve shape:** $\alpha_{II}/\alpha_{III}$ rises from ~1, peaks ~pH 6, collapses at high pH (hydrolysis $5\times10^{-6}/h$ inflates $\alpha_{III}$) → crosses target **twice**.
5. **Roots:** rising side pH 4.349; falling side pH 8.218. **Sum = 12.567.**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $12.567$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains the Nernst free-ion ratio $x/y\approx0.677587$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Includes $10^9h\ell$ in $\alpha_{III}$ to account for the protonated ligand complex.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Ringbom, A. *Complexation in Analytical Chemistry*, Wiley, 1963 — side-reaction (alpha) coefficients, conditional constants. *Required: False.*
2. Martell & Motekaitis, *Determination and Use of Stability Constants*, VCH, 1992 — protonated-complex speciation. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_speciation_optionalfork.md](../../planck_task_speciation_optionalfork.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
