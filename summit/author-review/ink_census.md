# Author review: ink_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/ink_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
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
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$5$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Wall stress.** Force balance on the nozzle land: $\tau_w = PR/(2L) = 6.25\,P$ (τ_w in Pa, P in kPa). Per pressure: 32→200, 40→250, 48→300, 56→350, 64→400 Pa.

**Step 2 — T1 criterion.** Bingham flow exists only if $\tau_y < \tau_w$. The unyielded plug has radius $r_p = R\,\tau_y/\tau_w$; plug area fraction $= (\tau_y/\tau_w)^2 \ge 1/2 \Leftrightarrow \tau_y/\tau_w \ge 1/\sqrt2 = 0.7071$. So T1 ⇔ $0.7071 \le \tau_y/\tau_w < 1$.

**Step 3 — T1 sweep (ratios).** A 0.750✓ B 0.800✓ C 0.840✓ D 0.880✓ E 0.900✓ F 0.920✓ G 0.950✓ H 0.780✓ I 0.550✗ J 0.600✗ K 0.650✗ L 0.680✗ (area 0.462 < ½) M 0.400✗ N 0.450✗ O 1.100✗ (no flow) P 1.250✗ (no flow). Survivors: A–H.

**Step 4 — T2 conversions.** $t = 1.8\times10^6$ s. Current-type: $\Delta m = i\,t\,M_{\mathrm{Zn}}/(2F) = 0.6099\,i$ mg cm⁻² (n = 2). Flux-type: each H₂ takes 2 e⁻ = one Zn, so $\Delta m = v \times 10^{-9} \times 1.8\times10^6 \times 65.38\times10^3 = 117.7\,v$ mg cm⁻².

**Step 5 — T2 sweep (loss vs 0.1 m).** A 1.83≤3.0✓ B 1.18≤2.0✓ C 4.88>2.5✗ D 5.88>3.5✗ E 1.22≤1.5✓ F 2.35≤4.0✓ G 3.96>2.8✗ H 1.41≤1.8✓.

**Step 6 — Count.** Viable: A, B, E, F, H.

**Final Answer:** $5$
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $5$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Derives the flow-and-plug criterion $1/\sqrt{2}\leq\tau_y/\tau_w<1$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains the corrosion conversion $\Delta m\approx117.7v\,\mathrm{mg\,cm^{-2}}$ for the numerical hydrogen flux $v$ in the question's units.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Tagliaferri et al. ACS Appl. Mater. Interfaces 2025, 17, 38215–38224. doi:10.1021/acsami.5c05599 (ChemRxiv 2024-12-31) — printed Zn ink rheology, corrosion quantification. *Required: False.*
2. Bird, R. B.; Dai, G. C.; Yarusso, B. J. Rev. Chem. Eng. 1983, 1, 1–70 — Bingham plug flow. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_ink_census.md](../../planck_task_ink_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
