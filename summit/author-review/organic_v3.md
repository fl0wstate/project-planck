# Author review: organic_v3

[Back to the full checklist](../AUTHOR_REWRITE_GUIDE.md)

Package input: [task.json](../drafts/organic_v3/task.json).

These are the exact currently packaged values. This sheet does not identify what the detector flagged or certify authorship. Do not edit wording merely to conceal its origin.

## 1. Question — establish origin or independently replace in full

Field: `task.questionText`. Copied from legacy source; original authorship is not established by this migration. Includes every assumption, given value, definition and requested output shown below.

````text
A mixture of two enantiopure diastereomers of 2-(acetyloxy)cyclohexyl 4-bromobenzenesulfonate is solvolyzed in anhydrous acetic acid at 75 °C: 70.0 mol % is the trans diastereomer, $(1S,2S)$, and 30.0 mol % is the cis diastereomer, $(1R,2S)$. In both compounds the carbonyl oxygen of the acetate group is 100% $^{18}\text{O}$; every other oxygen in the system, including all solvent oxygens, is $^{16}\text{O}$.

Assume the following:
- Any substrate molecule for which intramolecular acetoxy participation is geometrically accessible reacts exclusively through the cyclic acetoxonium (1,3-dioxolan-2-ylium) pathway; solvent capture of the acetoxonium ion occurs exclusively at the ring carbons C1 and C2.
- Any substrate molecule for which such participation is not geometrically accessible reacts exclusively by direct one-step backside displacement of brosylate at C1 by acetic acid.
- Both diastereomers react to completion. The only product is 1,2-diacetoxycyclohexane; there is no elimination, no isotope exchange with solvent, and no internal return.

In an ester group $\text{C–O–C(=O)CH}_3$, the single-bonded oxygen is the "ether oxygen" and the double-bonded oxygen is the "carbonyl oxygen".

What percentage of all product molecules are the $(1R,2R)$ stereoisomer carrying $^{18}\text{O}$ in an ether-oxygen position? Give the answer in percent, rounded to 1 decimal place.
````

## 2. Answer — supply the result of your own derivation

Field: `task.finalAnswer[0]`. Copied from the legacy key. Keep or correct it according to your own work, not to make it appear different.

````text
$35.0$
````

Current precision metadata: `{"kind": "decimal_places", "digits": 1}`. Update it if your question asks for different precision.

## 3. Solution — establish origin or independently replace in full

Field: `task.solution`. Copied from legacy source; original authorship is not established by this migration. The full derivation, equations, tables and conclusion are included here, not only selected sentences.

````text
**Step 1 — Conformational gate for participation.** Acetoxy participation requires the acetate oxygen anti-periplanar to the C1–OBs bond, i.e. a trans-diaxial arrangement. On a cyclohexane ring, trans-1,2 substituents can be diaxial (ax,ax chair); cis-1,2 substituents are always ax,eq and can never be diaxial. Therefore the trans-$(1S,2S)$ substrate (70.0%) reacts via the acetoxonium pathway; the cis-$(1R,2S)$ substrate (30.0%) reacts only by direct displacement.

**Step 2 — Acetoxonium formation (trans feed).** The carbonyl oxygen ($^{18}$O) attacks C1 backside, expelling brosylate with inversion at C1. In the resulting 1,3-dioxolan-2-ylium ion, the ring oxygen bonded to C1 is $^{18}$O; the ring oxygen bonded to C2 is $^{16}$O (former ester ether oxygen).

**Step 3 — Ion symmetry.** Ignoring isotopes, the fused acetoxonium ion has a symmetry axis exchanging C1 and C2, so acetic acid captures at C1 and C2 with equal probability (isotopic substitution does not perturb the rates within the stated assumptions).

**Step 4 — Capture at C1 (35.0% of total).** Backside attack at C1 breaks C1–$^{18}$O with a second inversion at C1 → net retention at both centers → $(1S,2S)$ product. The released $^{18}$O becomes the carbonyl oxygen of the acetate on C2. Label = carbonyl position. Not the target species.

**Step 5 — Capture at C2 (35.0% of total).** Backside attack at C2 breaks C2–$^{16}$O with inversion at C2; C1 retains its single inversion from Step 2 → $(1R,2R)$ product. The acetate on C1 keeps C1–$^{18}$O intact as its ether oxygen; the released $^{16}$O becomes its carbonyl. Label = ether position. **Target species.**

**Step 6 — Direct pathway (cis feed, 30.0% of total).** Single inversion at C1 ($1R \to 1S$) → $(1S,2S)$ trans-diacetate; the C2 acetate untouched, $^{18}$O stays carbonyl. Contributes nothing to the target.

**Step 7 — CIP consistency.** At C1 and C2 the top-priority substituent is always the O-linked group (OBs or OAc), followed by the O-bearing ring carbon, the CH₂ ring carbon, then H — identical priority pattern before and after substitution, so spatial inversion ⇔ descriptor flip throughout.

**Step 8 — Tally.** Target = trans feed × capture-at-C2 fraction = $0.700 \times 0.500 = 0.350$.

**Final Answer:** $35.0$
````

## 4. Rubric — replace every criterion with your own writing

Confirmed assistant-generated in this chat. Replace all criterion descriptions, including the final-answer criterion. Choose criteria and weights yourself under the required 10-point format; do not just paraphrase these descriptions.

### c1 — 5 points — final answer

Field: `task.rubric.criteria[0].description`.

````text
Gives $35.0$ as the final answer in the units and precision requested by the question.
````

### c2 — 3 points

Field: `task.rubric.criteria[1].description`.

````text
Assigns acetoxonium participation to the trans-$(1S,2S)$ feed through its trans-diaxial conformation.
````

### c3 — 2 points

Field: `task.rubric.criteria[2].description`.

````text
Assigns equal capture probabilities $1/2$ to C1 and C2 of the acetoxonium intermediate.
````

## 5. References — review and supply your own source record

Field: `task.references`. Copied from legacy files. Source metadata is not evidence that the references meet the current submission rules.

````text
1. Winstein, S.; Buckles, R. E. *J. Am. Chem. Soc.* **1942**, 64, 2780–2786. doi:10.1021/ja01260a064 — neighboring acetoxy participation, trans vs cis. *Required: True.*
2. Clayden, Greeves, Warren, *Organic Chemistry*, 2nd ed., OUP — participation/rearrangement chapter. https://global.oup.com/ukhe/product/organic-chemistry-9780199270293 *Required: False.*
3. Bloembergen-free — no physics refs needed for this variant.
````

## 6. Fields that need no prose rewrite

`schema_version`, domain/subdomain identifiers, modality, task type, answer type and JSON syntax are technical metadata. Keep them only where they still describe your task accurately. No image is currently included; if your new task requires one, supply your own permitted image and identify which information it carries. Empty optional answer-variant and wrong-answer lists do not need filler.

## Source record

- [planck_task_organic_v3.md](../../planck_task_organic_v3.md)

## What to return

Provide your independently authored question, answer, numbered solution, rubric and references under those five headings. If you retain material you originally wrote, identify that material explicitly. Keep your original notes and derivation; the formatting work does not itself establish eligibility.

The assistant can transcribe your equations into LaTeX without changing content, map your supplied text into JSON, synchronize review line arrays and rebuild the ZIP. Neither the packages nor authorship records have been changed by this review-sheet export.
