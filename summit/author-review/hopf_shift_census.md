# Author review: hopf_shift_census

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/hopf_shift_census/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A well-stirred reactor holds two species with concentrations $u$ and $v$, governed by the rate functions

$$f(u,v) = 2 - (b+1)u + u^2 v, \qquad g(u,v) = bu - u^2 v,$$

where $b > 0$ is a fixed control setting. The state is advanced in discrete steps. Writing $(u,v)$ for the current state and $(u',v')$ for the next, four update procedures are in use:

**Procedure A** ($\Delta = 0.34$): $u' = u + \Delta f(u,v)$ and $v' = v + \Delta g(u,v)$.

**Procedure B** ($\Delta = 0.34$): first $u' = u + \Delta f(u,v)$, then $v' = v + \Delta g(u',v)$.

**Procedure C**: the steps alternate — the first step follows the rule of procedure A, the second the rule of procedure B, the third A again, and so on.

**Procedure D** ($\Delta = 0.08$): $(u',v')$ is the solution of $u' = u + \tfrac{\Delta}{2}\left[f(u,v)+f(u',v')\right]$ and $v' = v + \tfrac{\Delta}{2}\left[g(u,v)+g(u',v')\right]$. Take as given that, at this step length, these equations have exactly one solution near the current state whenever the current state is near $P$, and that this solution depends smoothly on the current state.

Every procedure leaves the state $P = (2,\ b/2)$ unchanged. Call $P$ **stable** for a procedure at a given $b$ if every starting state sufficiently close to $P$ produces a sequence of states that remains near $P$ and converges to $P$.

Now consider the seven settings $b \in \{3.0,\ 3.5,\ 4.0,\ 4.5,\ 4.75,\ 5.2,\ 5.5\}$. For every pair (procedure, value of $b$) for which $P$ is stable, add that value of $b$ to a running total, so that one value of $b$ is added once for each procedure that is stable there. Report the final total, to two decimal places.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$39.75$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 2}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
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
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $39.75$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Obtains the stability threshold $b<3.64$ for procedure A on the specified grid.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Classifies procedure C at $b=3.5$ as unstable from the composite update, despite both individual updates being stable there.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
**Source (concept only):** EuDML doc/125683, *Shift in Hopf bifurcations for a class of nonstandard numerical schemes* (2005) — a discrete update rule relocates the stability threshold of the underlying rate equations. All systems, parameters and the composition paradox instance are invented for this problem; nothing numeric is taken from the source.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_hopf_shift_census.md](../../planck_task_hopf_shift_census.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
