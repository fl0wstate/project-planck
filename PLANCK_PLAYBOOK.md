# Project Planck — Stump Playbook (consolidated learnings)

Campaign to date: **~23 tasks built, verified, and platform-tested. Exactly one failure mode ever observed.**
Everything else returned 0/2. This file is the durable record so nothing is re-derived.

---

## 1. How the responders actually reason (from ~23 traces)

Their method is a six-step pipeline. **Each step is a defense**, and each one killed a specific attack of mine:

| # | Behavior | Evidence | Attack it kills |
|---|---|---|---|
| 1 | **Trap-hunt before solving** | literally wrote *"Key trap first:"* | any single distinguished fork |
| 2 | **Bound the problem / check extremes** | "full conversion → 390 K, above bp 351 K" — found the boiling pin for free | concealed boundary crossings |
| 3 | **Pivot on an early invariant** | every speciation solve fixed `x/y` from Nernst first | forcing a hard coupled solve |
| 4 | **Compress regular structure** | 16-ink census → 5 interval checks; 16 cycles → closed-form series | case-volume / length |
| 5 | **Enumerate interpretations, check convergence** | ChatGPT: computed all 3 conventions, noted they agree | ambiguity forks, red herrings |
| 6 | **Self-verify chain-locally** | mass balances, direction, unit checks | arithmetic-slip hopes |

### The real weakness
**Verification is chain-local, not global.** They confirm *"did I compute my chain correctly"* — never *"was this the right chain."*
The single observed failure was an over-eager **local causal chain** overrunning a **global constraint**:
> H₂ consumes charging current → so plating is slower → so the charge step must run longer
…which silently overcharged a capacity-fixed cathode. Not a hidden fact. Not a labeled trap. An inference that felt locally obligatory.

---

## 2. What has been tried and failed (do not repeat)

| Attack | Result |
|---|---|
| Substitution chains / given equations | solved. *Formula given = reasoning given.* |
| Canonical mechanisms + stereo/isotope bookkeeping (Winstein) | solved, pattern-matched cold |
| Cage symmetry / ¹³C counting incl. SMILES parity | solved |
| Graph enumeration + Hückel spectra (non-alternant gate) | solved — operational definitions became an executable spec |
| BS-DFT projection + exact spin diagonalization | solved, both Heisenberg conventions |
| Stated red herrings, threshold-rejection rules | solved — **they name the trap and step around it** |
| 16-case homogeneous census | solved by batching |
| Structure elucidation with rich correlation data | solved (correlations = adjacency list) |
| Multi-root non-monotonic E(pH) | solved — "largest" wording revealed multiplicity |
| Colligative Mₙ vs M𝓌 fork | solved at **both** tiers; hardening made it *faster* (25 s, "Key trap first:") |
| Silent boiling-point pin (false-confirming chain) | solved via extreme-case bounding |
| Optional-fork speciation (protonated adduct) | solved, but **34 min** — hardest artifact produced |

### Two structural traps in planck's own rules
1. **Unambiguity forces consequence-free forks.** If every reading must give the same answer, no reading can be an error. Wrong branches must be **errors** (violate a stated constraint), never **interpretations**.
2. **Legibility.** Any fork load-bearing enough to matter is legible enough to be spotted. Never *announce* a rule; never make the trap the distinguished difficulty.

---

## 3. The only thing that has ever worked

**Battery charge-prolongation** — reproducible across two separate platform runs, **~25% per response**, 1/2 both times.
Properties that made it work, all four necessary:
- The fork was **optional** — the correct path never had to consider it. (When v2 made it *mandatory*, both responders engaged carefully and solved it. **Optional forks kill; mandatory forks instruct.**)
- The wrong model was a **locally-compelling causal chain**, not a data choice.
- It **completed cleanly** — no downstream contradiction to trigger backtracking.
- The wrong answer was **adjacent** (28 vs 29), so no sanity check fired.

Verified defense: the faradaic reading *with the correct endpoint* gives the same answer. Only the overcharge changes it → it is an error, not an interpretation.

---

## 4. The strategic math (this reframes everything)

Per-fork catch rate ≈ 0.25. With *k* **independent** forks:

| k | P(one response fails) | **P(2/2)** |
|---|---|---|
| 1 | 25% | **6%** ← every task so far |
| 3 | 58% | 33% |
| 4 | 68% | **47%** |
| 5 | 76% | 58% |

Every task built this campaign had **one** fork. The observed hit rate matches the 6% row exactly.
**Stop hunting one clever trap. Build fork density.** The 2000-char cap allows ~3–4.

---

## 5. Improvements to make — ranked, with rationale

### R1 · Fork density (evidence-backed, do this first)
3–4 **independent** optional forks, none of them the distinguished difficulty. Each must satisfy the four properties in §3. Target P(2/2) ≈ 47%.

### R2 · Decoy trap as attention sink (new, untested, high value)
They open by trap-hunting and find **one** trap. Plant an obvious, satisfying, resolvable trap — let them find and correctly dispose of it. Trap-hunting is then *satisfied* and they proceed confidently. The real fork sits elsewhere disguised as routine bookkeeping. Directly exploits defense #1 by feeding it.

### R3 · Defeat extreme-case bounding with an interior violation (new, untested, high value)
Their step-2 check tests **endpoints**. It gives a false all-clear whenever the constraint is violated only at an **interior** point of the trajectory while both endpoints are fine. Design a process whose intermediate state crosses a limit but whose start and end states do not. Bounding says "no problem"; only tracking the trajectory reveals the excursion. This is the precise complement of the boiling-pin task, which failed *because* the violation was monotonic and endpoint-visible.

### R4 · Two-route disagreement
Make the problem solvable by two independent routes that agree only if a subtlety is handled. They run one route and self-verify within it (defense #6). The second route is the check they never run.

### R5 · Non-monotonic without signalling multiplicity
Never use words like "largest", "all", or "sum of" — those reveal that multiple solutions exist. Ask for a quantity that is single-valued but whose computation requires knowing the trajectory shape.

### Combination to build next
**R2 + R3 + R1**: a decoy trap absorbing the trap-hunt, a real error that is an interior constraint excursion invisible to endpoint bounding, plus two further optional forks. Four independent catch opportunities, none distinguished.

---

## 6. Resource triage — strict gate (one tool call, immediate verdict)

**REJECT immediately if any of these hold:**
- Published **after 2025-07-31** (fails Reference Cutoff Checker; findings become post-cutoff knowledge). *Killed: JACS Au 2026 SepF paper.*
- Full text not directly verifiable (paywalled, proxy-reader only) → numbers not ground-truth grade. *Same paper.*
- **Teaching material**: lab manual, textbook, problem set, course notes. Undergraduate ceiling, maximal training-data familiarity. *Killed: Cheronis 1942 Semimicro Organic Chemistry.*
- **Purely qualitative** with no quantitative relationships and no regime/validity discussion.
- Review article with no primary data.

**ACCEPT — high value:**
- Method-comparison tables (DFT vs CC vs experiment across a series) → conflicting numbers = real forks
- **Regime maps / crossovers / breakdown of an approximation** → interior-violation material (R3)
- Validity-boundary discussions ("this treatment fails when…")
- Non-monotonic behavior, inverted intuitions
- Congener series in SI (12+ entries, heterogeneous)
- Datasets with known-bad or excluded points

**Best source so far:** Chem. Sci. 2025, 16, 430 (diradicals) — five genuine inversions.
**Also good:** Beilstein J. Org. Chem. 2025, 21, 47 — non-monotonic stiffness optimum, inverted heating intuition.

---

## 7. Verified assets (submittable now)

| File | Answer | Notes |
|---|---|---|
| `planck_task_battery_v3.md` | 18 | amplified proven attractor + cathode fade; **best kill odds** |
| `planck_task_battery_cycle.md` | 29 (v2) / 40 (v1) | v1 scored **1/2 twice** |
| `planck_task_speciation_optionalfork.md` | 12.567 | hardest artifact (34 min proxy) |
| `planck_task_adiabatic_regime.md` | 1.373 | false-confirming chain |
| `planck_task_osmotic_polymersome.md` | 203 | 0/2 platform |
| `planck_task_twistane_final.md` | 6 | symmetry |
| `planck_task_debye_screening.md` | 2.80 | clean, forward |
| `planck_task_pentalene_census.md` | 1 | 0/2 platform |
| `planck_task_ink_census.md` | 5 | 0/2 platform |
| `planck_task_tetraradical_v2.md` | 3.85 | v1 burned 0/2 |

---

## 8. Process rules
- **Never** trust a design agent's own verification — re-verify with my own script.
- Cold-probe only on request; forbid tools in the probe prompt **and** confirm `tool_uses: 0`.
- Probe **duration** is the difficulty signal, not pass/fail (34 min = hardest; 25 s = trivial).
- Never park an answer near a rounding boundary — planck excludes arithmetic slips as failures, and boundary answers invite grading disputes.
- Keep every constant original; cite only pre-cutoff sources; never let a source's own value be load-bearing.
