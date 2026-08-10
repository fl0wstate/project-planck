# Planck Task — Zn Microcell Fade v3 (amplified attractor + cathode-fade fork)

**Domain:** Chemistry · **Subdomain:** Physical (electrochemistry)
**Answer type:** integer · **Final answer: 18**
**Lineage:** v1 (Ic=0.50, TH=0.80) scored **1/2** on platform twice-run (one responder → 28 via charge-prolongation, one → 29). v2 (mandatory fork) → 0/2. v3 amplifies the *proven* attractor rather than adding new mechanisms.

## What the platform traces showed

- **Responder failure mode (reproducible, ~25%/response):** treats the H₂ stream as a faradaic partition of the charging current, computes "net plating current = I_c − i_H₂", then **prolongs the charge step** to fully restore the zinc reservoir. This overcharges a capacity-fixed cathode. At Ic=0.50 it produced 28 vs correct 29.
- **Why it is an ERROR, not an interpretation (verified):** the faradaic reading with the *correct* (cathode-set) charge endpoint gives the **same** answer as the chemical-corrosion reading. Only the overcharge changes the number. Airtight rebuttal for any UNAMBIGUITY finding.

## v3 changes (each targets the observed failure)

1. **Charge current 1.0 → 0.20 mA/cm².** H₂ is now **19.3%** of the charging current (was 7.7%) — the "net plating current" reasoning becomes highly salient, maximising pull toward the proven wrong model.
2. **Cathode fade added (0.80% of original per completed cycle).** Second independent fork: ignoring it gives 17. Also forces a genuine `min(cathode, zinc)` branch-switch (cathode-limited through cycle 16, zinc-limited from 17).
3. **Narrative priming** — "the same flux shows up right through those long slow charge steps" — draws attention to charge-step gas without stating a mechanism (surface ambiguity, deep determinacy).

**Ambiguity-safety:** all four fade formalizations (linear ×(n−1), linear ×n, compounding, compounding ×n) give **18**. Margins fat: cycle 17 Q=0.944 (above 0.85), cycle 18 Q=0.706 (below). No rounding boundary.

## PROMPT (SUBMIT THIS)

I've been running a printed Zn–MnO₂ microcell on the bench rig for a durability study and I need to reconcile the fade data before our group meeting. The cell is sealed and was thoroughly de-aerated before assembly. We cycle it galvanostatically with no rest steps, starting with a discharge: each cycle is a full discharge — down to whatever capacity the cell can actually deliver at that point in its life — followed by a full recharge. We discharge at $1.0\ \mathrm{mA\,cm^{-2}}$, but we charge at only $0.20\ \mathrm{mA\,cm^{-2}}$, a fifth of the discharge rate, because anything faster gives us mossy zinc.

The cathode is $10.0\ \mathrm{mg}$ of electrodeposited MnO$_2$ per square centimetre. Fresh, it gives $120\ \mathrm{mAh}$ per gram of MnO$_2$, but Mn dissolution costs it $0.80\%$ of that original specific capacity with every completed cycle. Apart from that steady fade the cathode behaves perfectly: the electrolyte never depletes, and neither kinetics nor ohmic drop matter at these currents. The anode carries $7.22\ \mathrm{mg}$ of metallic zinc per square centimetre (take zinc as $65.38\ \mathrm{g\,mol^{-1}}$ and use $F = 96485\ \mathrm{C\,mol^{-1}}$).

Post-mortem work on sister cells turned up exactly two parasitic processes at the anode, both active from the very first cycle. SEM showed that every time the anode strips during discharge, zinc equivalent to $4.0\%$ of that cycle's discharge capacity ends up electronically orphaned — permanently disconnected from the active inventory. And our online mass spec picks up a steady hydrogen stream of $17.28$ micromoles of H$_2$ per day per square centimetre of anode the whole time the cell is operating — the trace is flat and doesn't care about state of charge or which way the current is flowing, so the same flux shows up right through those long slow charge steps. Nothing else is degrading.

The sensor team downstream needs at least $0.85\ \mathrm{mAh\,cm^{-2}}$ per discharge. During which numbered cycle does the delivered discharge capacity first drop below that? (Cycle 1 is the first discharge.) Give a single integer.

## GOLDEN RESPONSE

1. **Cathode ceiling:** $Q_{cat}(n) = 1.200(1 - 0.0080(n-1))$ mAh cm⁻² (10.0 mg × 120 mAh/g = 1.200 fresh).
2. **Zinc inventory:** $7.22\times10^{-3}/65.38 = 1.10431\times10^{-4}$ mol; ×2F/3.6 → $Z_1 = 5.9194$ mAh cm⁻².
3. **Corrosion in capacity units:** $17.28\ \mu$mol/day × 2F = 3.3345 C/day = 0.92626 mAh/day = **0.038594 mAh per operating hour** (2 e⁻ per H₂ = one Zn).
4. **Cycle duration — the load-bearing step:** discharge of $Q$ at 1.0 mA takes $Q$ h; the capacity-fixed cathode is full after exactly $Q$ of charge, which at 0.20 mA takes $5Q$ h. Total $6Q$ h. (Prolonging beyond $5Q$ h to restore the zinc reservoir would overcharge the cathode — inadmissible.)
5. **Per-cycle inventory loss:** orphaning $0.040Q$ + corrosion $0.038594 \times 6Q = 0.231564Q$ → **$0.271564\,Q$**.
6. **Delivered capacity:** $Q_n = \min\!\big(Q_{cat}(n),\ Z_n/1.078594\big)$, where $1.078594 = 1 + 0.04 + 0.038594/1.0$ is the inventory a discharge of $Q$ must cover.
7. **March:** cycles 1–16 cathode-limited (1.200 → 1.056). Zinc entering cycle 17 ≈ 1.018 mAh → cycle 17 is the first zinc-limited one, $Q_{17} = 0.944$ (above spec). Cycle 18: $Q_{18} = 0.706 < 0.85$.

**Final Answer: 18**

## Wrong branches

| Answer | Error |
|---|---|
| **15** | prolongs charge to restore the zinc reservoir (overcharges capacity-fixed cathode) — **the observed platform failure mode** |
| **17** | ignores the cathode fade entirely |
| **38** | symmetric cycle time: uses $2Q$ h despite the 0.20 mA charge current |
| ~44 | 1 e⁻ per H₂ |
| ~56 | corrosion counted only during discharge |
| ~4 | CE-compounding from cycle 1, no reservoir plateau |
| 16 / 19 | off-by-one at the crossing or plateau end |

## ALTERNATIVE (Option B) — preserve the exact proven-kill configuration

Keep discharge 1.0 / **charge 0.50** mA cm⁻², cathode fade **0.60%**/cycle, threshold **0.85**: **correct = 31**, prolong = 29, ignore-fade = 28, symmetric = 42. Same two forks, but the charge current is left at the value that actually produced the 1/2 kill. Choose this if you would rather not change the variable that demonstrably worked.

## References (pre-cutoff)

1. Tagliaferri et al. *ACS Appl. Mater. Interfaces* **2025**, 17, 38215–38224. doi:10.1021/acsami.5c05599 (ChemRxiv 2024-12-31). *Required: False.*
2. Parker et al. *Science* **2017**, 356, 415–418. doi:10.1126/science.aak9991 — Zn utilization/reservoir effects. *Required: False.*

## Honest assessment

Proxy (Opus-tier) solved v3 → 18 in 80 s, and explicitly named the corrosion-timing trap. So this does **not** stump a top-tier model. But the target is your platform pair, and the evidence there is specific and encouraging: one of them has now twice demonstrated the charge-prolongation error at a 7.7% steal fraction. v3 raises that to 19.3% and adds a second independent fork (cathode fade). If per-response failure was ~25% with one fork, two roughly-independent forks put it materially higher — that is the honest mechanism by which 2/2 becomes plausible. It is a probability play, not a guarantee; no design in this campaign has guaranteed a frontier-model failure.
