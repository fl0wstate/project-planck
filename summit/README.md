# Summit migration

Existing Planck content mapped into `summit-task-package-v1`. These are **incomplete drafts**, not approved or submission-ready questions. Original files remain unchanged.

## Contents

- `requirements.txt`: the supplied Summit instructions, preserved verbatim.
- `drafts/manifest.json`: every migrated question, its source revision, and review status.
- `drafts/<id>/task.json`: Summit fields populated from existing source material.
- `drafts/<id>/review.json`: full question text in `question_source` and full solution text in `solution_source`, each stored as an array with one original text line per entry. Empty strings preserve blank lines. Joining each array with `\n` reproduces the corresponding `task.json` text exactly. Source paths and hashes remain in `sources`, alongside legacy wrong-answer material and author actions.
- `drafts/draft-zips/<id>.zip`: optional form-import packages containing `task.json` at the ZIP root. Each ZIP is one question; do not upload the whole drafts directory.
- `drafts/all-question-imports.zip`: download bundle containing all 26 individual question ZIPs and a completion notice. Extract it first, then import each individual ZIP; the bundle itself is not a Summit import package.
- `convert.py`: repeatable, standard-library-only migration and structural checks.

## Mapping decisions

All 26 primary task files are retained, including old versions and retired candidates. Related `_golden` and `_sources` files are supporting material, not separate questions. The original `planck.md`, playbook, scripts, and historical notes remain in the repository; they are not copied into question stems.

The first PROMPT and GOLDEN sections are selected. In particular, `battery_cycle` uses the explicitly active v2 prompt and answer **29**, not the obsolete answer 40 later in the file. Three dedicated golden solutions and two dedicated source documents are reused. Prompt wrapper fences and a character-count annotation are removed; scientific prose is preserved. Numeric answer keys are transcribed from existing explicit keys and wrapped in LaTeX. Precision follows each question, including zero decimal places for whole nanometres. Subdomains are descriptive metadata, not scientific rewrites.

No image assets exist in this checkout. Every migrated task is therefore `text_only` / `not_applicable`. This does not establish eligibility under an assigned category's text-only allowance.

No legacy rubric exists. `rubric.criteria` is deliberately empty: the supplied instructions prohibit LLM-written rubrics, questions, answers, and solution prose. The author must supply 3–5 objective criteria totaling 10 points, with exactly one final-answer criterion stating the actual answer and carrying the most points. Common-wrong-answer tables are preserved in review metadata because they also contain explanations, approximate values, ranges, and historical alternatives. They are not blindly imported as answer strings.

Legacy material includes AI/probe histories and references that may not meet the new source rules. Mechanical conversion does not establish original human authorship, scientific correctness, graduate-level difficulty, peer review of citations, image eligibility, or Summit acceptance. Some solutions also need author formatting and content review. Historical platform results do not satisfy the new difficulty test. No model-based answer verification was performed.

## Use

From the repository root:

```sh
python3 summit/convert.py check
python3 summit/convert.py package
```

These commands check migration structure/source hashes and rebuild import-only draft ZIPs. They are local data checks, not Summit's automated quality or difficulty checks. Import a single ZIP, complete the missing author-written fields, inspect the rendered form, and submit yourself when eligible. Empty rubrics must be completed before submission.

To reproduce without overwriting edits:

```sh
python3 summit/convert.py build --output /tmp/planck-summit-new
python3 summit/convert.py check --output /tmp/planck-summit-new
```

Build refuses a nonempty destination. Edit the existing `task.json` files directly to complete drafts and synchronize the corresponding review line arrays when question or solution text changes; rebuilding is intended for fresh output only. The checker rejects non-array review fields and any text mismatch. JSON still requires escaped LaTeX backslashes within each line; these decode to the original characters. Package generation does not claim readiness and never submits anything.
