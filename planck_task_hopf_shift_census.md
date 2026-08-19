# Planck Task — Update-Procedure Stability Census v2 (composition paradox)

**Domain:** Mathematics · **Subdomain:** Optimization & Numerical Mathematics
**Answer type:** decimal, 2 dp · **Final answer: 39.75** (exact decimal; unbounded rounding margin)
**Lineage:** v2, hardening of the v1 threshold-sum census after the "too trivial" verdict. v1's fatal flaw: its ambiguity stipulation ("stability is decided by the linearization of the update map") *named the winning method*, reducing every row to mechanical 2×2 algebra. v2 removes the method handover entirely and moves the load onto a judgment that is never stated: **a composition of two individually stable procedures need not be stable.** Levers: **R1 (fork density, k≈5) + R4 (two-route disagreement) + the census/decorrelation structure of `planck_task_stereogenic_census_v2.md`** (2/2 platform kill).
**Source (concept only):** EuDML doc/125683, *Shift in Hopf bifurcations for a class of nonstandard numerical schemes* (2005) — a discrete update rule relocates the stability threshold of the underlying rate equations. All systems, parameters and the composition paradox instance are invented for this problem; nothing numeric is taken from the source.

## The design in one paragraph

Same disguised-classic kinetics as v1 ($f = 2-(b+1)u+u^2v$, $g = bu-u^2v$, fixed point $P=(2,b/2)$; the *flow* loses stability at $b=5$ — memorized bait). Four update procedures: **A** (simultaneous explicit, $\Delta=0.34$, true threshold $b_A=3.64$), **B** (sequential explicit, $\Delta=0.34$, true threshold $b_B=4.33987$, a $\mu=-1$ exit — different mechanism from A), **C** (strict alternation of A and B — **unstable from $b\approx3.3554$, strictly before either component fails**: the composition paradox), **D** (endpoint-averaged implicit, $\Delta=0.08$ — **zero shift at any step, $b_D=5$**). The question is a 7-value stability census: for each $b \in \{3.0, 3.5, 4.0, 4.5, 4.75, 5.2, 5.5\}$ and each procedure, is $P$ locally asymptotically stable? The answer aggregates as a **$b$-weighted sum over stable pairs**, which (unlike a plain count) makes compensating errors land off-golden — verified exhaustively.

## The judgment inventory (what each fork tests, nothing announced)

| Fork | Wrong rule | Flips | Effect on sum |
|---|---|---|---|
| **F1 · composition fallacy** | "A and B are both stable at $b=3.5$, so alternating them is stable" — locally compelling, completes cleanly, no contradiction fires | C@3.5 | $+3.5 \to 43.25$ |
| **F2 · flow recall** | "this is the classic system, threshold $b=5$ everywhere" | A@{4.0,4.5,4.75}, B@{4.5,4.75}, C@{3.5,4.0,4.5,4.75} | $+39.25 \to 79.00$; A-only $+13.25$, C-only $+16.75$ |
| **F3 · sequencing dismissed** | "B is A with cosmetic reordering" (drops the $\Delta^2$ term; threshold 3.64) | B@4.0 | $-4.0 \to 35.75$ |
| **F4 · D must shift** | "every other procedure shifted, so D does too" ($\pm 4\Delta$) | D@4.75 or D@5.2 | $-4.75$ or $+5.2$ |
| **F5 · determinant slip on B** | $\det M_B$ is negative for every $b$; forcing the oscillatory condition $|\det|=1$ gives threshold $6.229$ | B@{4.5,4.75,5.2,5.5} | $+19.95 \to 59.70$ |

Decorrelation: the flow heuristic is exactly right on the whole D column and wrong on nine other cells; the per-map linearization route (v1's whole content) is right on A, B, D and silently wrong on the entire C column; no single rule covers the grid. Every fork is an **error** against the stated stability definition, never an interpretation.

**Ambiguity-safety:** stability is defined in the prompt in plain sequence terms (stay near P, converge to P) — no method named, no "eigenvalue/linearization/bifurcation" vocabulary anywhere; the implicit procedure D carries an existence/uniqueness/smoothness stipulation (data, not test — the chemistry-census pattern); every cell sits at distance $\ge 0.14$ from its true threshold, so no borderline judgment exists; the answer $39.75$ is an exact decimal. **No root-finding is required**: the C column is decidable by evaluating the composite one step per grid value, so the task stays inside "standard linear algebra on a Jacobian".

## PROMPT (SUBMIT THIS)

A well-stirred reactor holds two species with concentrations $u$ and $v$, governed by the rate functions

$$f(u,v) = 2 - (b+1)u + u^2 v, \qquad g(u,v) = bu - u^2 v,$$

where $b > 0$ is a fixed control setting. The state is advanced in discrete steps. Writing $(u,v)$ for the current state and $(u',v')$ for the next, four update procedures are in use:

**Procedure A** ($\Delta = 0.34$): $u' = u + \Delta f(u,v)$ and $v' = v + \Delta g(u,v)$.

**Procedure B** ($\Delta = 0.34$): first $u' = u + \Delta f(u,v)$, then $v' = v + \Delta g(u',v)$.

**Procedure C**: the steps alternate — the first step follows the rule of procedure A, the second the rule of procedure B, the third A again, and so on.

**Procedure D** ($\Delta = 0.08$): $(u',v')$ is the solution of $u' = u + \tfrac{\Delta}{2}\left[f(u,v)+f(u',v')\right]$ and $v' = v + \tfrac{\Delta}{2}\left[g(u,v)+g(u',v')\right]$. Take as given that, at this step length, these equations have exactly one solution near the current state whenever the current state is near $P$, and that this solution depends smoothly on the current state.

Every procedure leaves the state $P = (2,\ b/2)$ unchanged. Call $P$ **stable** for a procedure at a given $b$ if every starting state sufficiently close to $P$ produces a sequence of states that remains near $P$ and converges to $P$.

Now consider the seven settings $b \in \{3.0,\ 3.5,\ 4.0,\ 4.5,\ 4.75,\ 5.2,\ 5.5\}$. For every pair (procedure, value of $b$) for which $P$ is stable, add that value of $b$ to a running total, so that one value of $b$ is added once for each procedure that is stable there. Report the final total, to two decimal places.

## GOLDEN RESPONSE

1. **Jacobian of the rates at $P$.** $f_u = b-1$, $f_v = 4$, $g_u = -b$, $g_v = -4$; $\operatorname{tr}J = b-5$, $\det J = 4$ for every $b$.

2. **Procedure A.** Update matrix $M_A = I + \Delta J$, eigenvalues $\mu = 1+\Delta\lambda$. For $|b-5|<4$ the $\lambda$ are a complex pair with $|\lambda|^2 = 4$, so $|\mu|^2 = 1 + \Delta(b-5) + 4\Delta^2$; with $\Delta = 0.34$, stability $\iff b < 5-4\Delta = \mathbf{3.64}$. (For $b \le 1$ the real eigenvalues stay inside the unit disc; single threshold.) Column A: stable at $3.0,\ 3.5$; unstable at the rest.

3. **Procedure B.** $M_B = \begin{pmatrix} 1+\Delta f_u & \Delta f_v \\ \Delta g_u(1+\Delta f_u) & 1+\Delta g_v + \Delta^2 g_u f_v\end{pmatrix}$. Here $\det M_B = (1+\Delta f_u)(1+\Delta g_v) = (0.66+0.34b)(-0.36) < 0$ — real eigenvalues of opposite sign for **every** $b$; the oscillatory route of A is unavailable. Stability by the unit-disc conditions: $\mu = 1$ is impossible ($1 - \operatorname{tr}M_B + \det M_B = 0.4624 > 0$ identically), and the binding exit is $\mu = -1$: $1 + \operatorname{tr}M_B + \det M_B = 1.0624 - 0.2448\,b = 0 \iff b = \mathbf{4.33987}$; $|\det M_B| < 1$ up to $b = 6.229$, not binding. Column B: stable at $3.0,\ 3.5,\ 4.0$; unstable at $4.5,\ 4.75,\ 5.2,\ 5.5$.

4. **Procedure C.** Stability of the alternation is governed by the composite $M_BM_A$ (the same spectrum as $M_AM_B$, so the starting phase is irrelevant) — and the spectrum of a product is **not** determined by the factors' spectra. Evaluating $M_BM_A$ at each grid value (numbers to 4 dp; each check is one $2\times2$ product and a quadratic):
   - $b=3.0$: eigenvalues $\mu \approx 0.568,\ -0.834$ — inside; **stable**.
   - $b=3.5$: $\mu \approx 0.593,\ -1.070$ — **unstable**, even though A ($3.5<3.64$) and B ($3.5<4.34$) are both individually stable there: each half overshoots in alternating directions, and the composed overshoot grows ($\mu < -1$) although each factor alone contracts.
   - $b=4.0,\ 4.5,\ 4.75,\ 5.2,\ 5.5$: spectral radius $1.33,\ 1.60,\ 1.74,\ 2.02,\ 2.21$ — all **unstable**.
   Column C: stable at $3.0$ only.

5. **Procedure D.** $M_D = (I-\tfrac{\Delta}{2}J)^{-1}(I+\tfrac{\Delta}{2}J)$: eigenvalues $\mu = \frac{1+\Delta\lambda/2}{1-\Delta\lambda/2}$, and $|\mu|<1 \iff \operatorname{Re}\lambda < 0 \iff b < 5$, for **every** step length — the averaged form relocates nothing. Column D: stable at $3.0,\ 3.5,\ 4.0,\ 4.5,\ 4.75$; unstable at $5.2,\ 5.5$.

6. **Census and total.**

   | $b$ | A | B | C | D | contribution |
   |---|---|---|---|---|---|
   | 3.0 | ✓ | ✓ | ✓ | ✓ | 12.00 |
   | 3.5 | ✓ | ✓ | ✗ | ✓ | 10.50 |
   | 4.0 | ✗ | ✓ | ✗ | ✓ | 8.00 |
   | 4.5 | ✗ | ✗ | ✗ | ✓ | 4.50 |
   | 4.75 | ✗ | ✗ | ✗ | ✓ | 4.75 |
   | 5.2 | ✗ | ✗ | ✗ | ✗ | 0 |
   | 5.5 | ✗ | ✗ | ✗ | ✗ | 0 |

   Total $= 12 + 10.5 + 8 + 4.5 + 4.75 = \mathbf{39.75}$.

**Final Answer: 39.75**

## Wrong branches (route-level; full cross-product verified collision-free)

| Total | Route |
|---|---|
| **43.25** | composition fallacy: C stable wherever A and B both are (the primary branch) |
| **79.00** | flow recall everywhere (stable $\iff b<5$ for all four columns) |
| **35.75** | B treated as A (sequencing cosmetic / $\Delta^2$ dropped) |
| **35.00** | D shifted down by $4\Delta$ (threshold 4.68) |
| **44.95** | D shifted up ($5.32$) |
| **59.70** | $|\det M_B|=1$ slip (B threshold 6.229) |

The verifier enumerates every combination of column-level routes (A: correct/flow; B: correct/as-A/flow/det-slip; C: correct/fallacy/as-A/average/flow; D: correct/down/up) — **120 combinations, 51 distinct totals, no total equals 39.75 except all-correct.** The $b$-weighted aggregation is what blocks compensation: with a plain count, fallacy ($+1$ cell) and D-shift ($-1$ cell) would cancel.

## Verification

`verify_hopf_shift.py` (no LLM in the loop):

1. per-procedure spectral-radius scan over $b \in (0,20]$: exactly one stability boundary each, located by bisection — $b_A = 3.64$, $b_B = 4.3398693$, $b_C = 3.3553925$, $b_D = 5$ — with exit mechanisms confirmed (A: complex pair on the unit circle; B, C: real $\mu=-1$; D: complex pair);
2. **paradox certificate**: at $b = 3.40$, $\rho(M_A) = 0.958$ and $\rho(M_B) = 0.869$ (both solidly stable) while $\rho(M_BM_A) = 1.022$ — genuinely stable factors, unstable alternation;
3. all 28 grid cells classified by eigenvalues **and** confirmed by simulating the nonlinear maps (Newton iteration for D; true alternation for C): contraction below, escape above, in every cell;
4. cell-margin guard: every grid $b$ at distance $\ge 0.14$ from the relevant true threshold;
5. golden weighted sum $= 39.75$ exactly; route cross-product (72 combinations) collision-free;
6. prompt length check ($< 2000$ chars).
