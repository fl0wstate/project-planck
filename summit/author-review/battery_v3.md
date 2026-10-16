# Author review: battery_v3

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/battery_v3/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
I've been running a printed Zn–MnO₂ microcell on the bench rig for a durability study and I need to reconcile the fade data before our group meeting. The cell is sealed and was thoroughly de-aerated before assembly. We cycle it galvanostatically with no rest steps, starting with a discharge: each cycle is a full discharge — down to whatever capacity the cell can actually deliver at that point in its life — followed by a full recharge. We discharge at $1.0\ \mathrm{mA\,cm^{-2}}$, but we charge at only $0.20\ \mathrm{mA\,cm^{-2}}$, a fifth of the discharge rate, because anything faster gives us mossy zinc.

The cathode is $10.0\ \mathrm{mg}$ of electrodeposited MnO$_2$ per square centimetre. Fresh, it gives $120\ \mathrm{mAh}$ per gram of MnO$_2$, but Mn dissolution costs it $0.80\%$ of that original specific capacity with every completed cycle. Apart from that steady fade the cathode behaves perfectly: the electrolyte never depletes, and neither kinetics nor ohmic drop matter at these currents. The anode carries $7.22\ \mathrm{mg}$ of metallic zinc per square centimetre (take zinc as $65.38\ \mathrm{g\,mol^{-1}}$ and use $F = 96485\ \mathrm{C\,mol^{-1}}$).

Post-mortem work on sister cells turned up exactly two parasitic processes at the anode, both active from the very first cycle. SEM showed that every time the anode strips during discharge, zinc equivalent to $4.0\%$ of that cycle's discharge capacity ends up electronically orphaned — permanently disconnected from the active inventory. And our online mass spec picks up a steady hydrogen stream of $17.28$ micromoles of H$_2$ per day per square centimetre of anode the whole time the cell is operating — the trace is flat and doesn't care about state of charge or which way the current is flowing, so the same flux shows up right through those long slow charge steps. Nothing else is degrading.

The sensor team downstream needs at least $0.85\ \mathrm{mAh\,cm^{-2}}$ per discharge. During which numbered cycle does the delivered discharge capacity first drop below that? (Cycle 1 is the first discharge.) Give a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$18$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
1. **Cathode ceiling:** $Q_{cat}(n) = 1.200(1 - 0.0080(n-1))$ mAh cm⁻² (10.0 mg × 120 mAh/g = 1.200 fresh).
2. **Zinc inventory:** $7.22\times10^{-3}/65.38 = 1.10431\times10^{-4}$ mol; ×2F/3.6 → $Z_1 = 5.9194$ mAh cm⁻².
3. **Corrosion in capacity units:** $17.28\ \mu$mol/day × 2F = 3.3345 C/day = 0.92626 mAh/day = **0.038594 mAh per operating hour** (2 e⁻ per H₂ = one Zn).
4. **Cycle duration — the load-bearing step:** discharge of $Q$ at 1.0 mA takes $Q$ h; the capacity-fixed cathode is full after exactly $Q$ of charge, which at 0.20 mA takes $5Q$ h. Total $6Q$ h. (Prolonging beyond $5Q$ h to restore the zinc reservoir would overcharge the cathode — inadmissible.)
5. **Per-cycle inventory loss:** orphaning $0.040Q$ + corrosion $0.038594 \times 6Q = 0.231564Q$ → **$0.271564\,Q$**.
6. **Delivered capacity:** $Q_n = \min\!\big(Q_{cat}(n),\ Z_n/1.078594\big)$, where $1.078594 = 1 + 0.04 + 0.038594/1.0$ is the inventory a discharge of $Q$ must cover.
7. **March:** cycles 1–16 cathode-limited (1.200 → 1.056). Zinc entering cycle 17 ≈ 1.018 mAh → cycle 17 is the first zinc-limited one, $Q_{17} = 0.944$ (above spec). Cycle 18: $Q_{18} = 0.706 < 0.85$.

**Final Answer: 18**
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $18$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains total operating time $6Q$ hours per cycle when $Q$ is the numerical discharge capacity in $\mathrm{mAh\,cm^{-2}}$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains $Q_{\mathrm{cat}}(n)=1.200[1-0.0080(n-1)]\,\mathrm{mAh\,cm^{-2}}$.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Tagliaferri et al. *ACS Appl. Mater. Interfaces* **2025**, 17, 38215–38224. doi:10.1021/acsami.5c05599 (ChemRxiv 2024-12-31). *Required: False.*
2. Parker et al. *Science* **2017**, 356, 415–418. doi:10.1126/science.aak9991 — Zn utilization/reservoir effects. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_battery_v3.md](../../planck_task_battery_v3.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
