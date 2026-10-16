# Author review: battery_cycle

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/battery_cycle/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
I've been running a printed Zn–MnO₂ microcell on the bench rig for a durability study and I'm trying to reconcile the fade data before our group meeting. The cell is sealed and was thoroughly de-aerated before cycling. We cycle it galvanostatically with no rest steps, starting with a discharge: each cycle is a full discharge — down to whatever capacity the cell can actually deliver at that point in its life — followed by a full recharge. We discharge at $1.0\ \mathrm{mA\,cm^{-2}}$, but we charge more gently, at $0.50\ \mathrm{mA\,cm^{-2}}$, to keep the zinc deposits smooth.

The cathode side is honestly the boring part: $10.0\ \mathrm{mg}$ of electrodeposited MnO$_2$ per square centimetre that reliably gives $120\ \mathrm{mAh}$ per gram of MnO$_2$, cycle after cycle, with no fade of its own — we've verified the electrolyte never depletes and neither kinetics nor ohmic drop matter at these currents. The anode is where things get interesting: the printed electrode carries $7.22\ \mathrm{mg}$ of metallic zinc per square centimetre (take zinc as $65.38\ \mathrm{g\,mol^{-1}}$ and use $F = 96485\ \mathrm{C\,mol^{-1}}$).

Post-mortem work on sister cells turned up exactly two parasitic processes, both active from the very first cycle. SEM showed that every time the anode strips during discharge, zinc equivalent to $4.0\%$ of that cycle's discharge capacity ends up electronically orphaned — permanently disconnected from the active inventory. And our online mass spec picked up a steady hydrogen stream of $17.28$ micromoles of H$_2$ per day per square centimetre of anode whenever the cell is operating — flat, regardless of state of charge or current direction. Nothing else is degrading.

The sensor team downstream needs at least $0.80\ \mathrm{mAh\,cm^{-2}}$ per discharge. During which numbered cycle does the delivered discharge capacity first drop below that? (Cycle 1 is the first discharge.) Give a single integer.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$29$
````

Current precision metadata: `{"kind": "none"}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Cathode ceiling.** $10.0\ \mathrm{mg} \times 120\ \mathrm{mAh/g} = 1.200\ \mathrm{mAh\,cm^{-2}}$ per discharge, every cycle.

**Step 2 — Zinc inventory.** $7.22\times10^{-3}/65.38 = 1.1043\times10^{-4}$ mol; 2 e⁻ per Zn: $Z_0 = 2(1.1043\times10^{-4})(96485)/3.6 = 5.9194\ \mathrm{mAh\,cm^{-2}}$.

**Step 3 — Corrosion rate in capacity units.** Each H₂ = 2 e⁻ = one Zn: $17.28\ \mu\mathrm{mol/day} \times 2F = 3.3345\ \mathrm{C/day} = 0.92626\ \mathrm{mAh\,day^{-1}\,cm^{-2}}$, i.e. $0.038594\ \mathrm{mAh}$ per operating hour.

**Step 4 — Cycle duration (the load-bearing step).** Discharge $Q$ at 1.0 mA → $Q$ h. Recharge: the capacity-fixed cathode is full after exactly $Q$ of charge; at 0.50 mA that takes $2Q$ h. Total operating time $= 3Q$ h per cycle. (Prolonging the charge beyond $2Q$ h to "restore the zinc reservoir" would overcharge the cathode, which the prompt fixes at 120 mAh/g reversible — inadmissible.)

**Step 5 — Per-cycle inventory loss.** Dead zinc $0.04Q$ + corrosion $0.038594 \times 3Q = 0.115782Q$; total $0.155782\,Q$.

**Step 6 — Plateau phase.** While Zn suffices, $Q = 1.200$: loss $= 0.186938$ mAh/cycle. $Z_n = 5.9194 - (n-1)(0.186938)$; the reservoir buffers ~26 full cycles (capacity fade is zero throughout the plateau).

**Step 7 — Fade phase.** Once zinc-limited, capacity decays geometrically at ratio $\approx 0.844$ per cycle (exact ratio depends on the intra-cycle convention; the crossing does not).

**Step 8 — Crossing.** Under every defensible convention the sequence passes 1.06 → 0.89 → 0.75 (±0.03 by convention): cycle 28 delivers $\ge 0.85$, cycle 29 delivers $\le 0.755 < 0.80$. First cycle below 0.80 = 29 in all cases.

**Final Answer:** $29$
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $29$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains total operating time $3Q$ hours per cycle when $Q$ is the numerical discharge capacity in $\mathrm{mAh\,cm^{-2}}$.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Obtains initial zinc capacity $Z_0\approx5.9194\,\mathrm{mAh\,cm^{-2}}$.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Tagliaferri et al. ACS Appl. Mater. Interfaces 2025, 17, 38215–38224. doi:10.1021/acsami.5c05599 (ChemRxiv 2024-12-31) — Zn-excess microbattery, dead-Zn and HER losses. *Required: False.*
2. Parker et al. Science 2017, 356, 415–418. doi:10.1126/science.aak9991 — Zn utilization and reservoir effects in rechargeable Zn cells. *Required: False.*
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_battery_cycle.md](../../planck_task_battery_cycle.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
