# Question packaging

[Download individual question ZIPs](DOWNLOADS.md).

All 26 packages now include the question, answer key, existing solution and an AI-assisted rubric with three criteria worth 5, 3 and 2 points. The final-answer criterion explicitly states the answer. Optional wrong-answer and accepted-variant lists may be empty.

These are field-complete packages for a workflow permitting AI-assisted content. They do not satisfy the archived Summit human-authorship restriction. Scientific correctness, originality, difficulty, domain assignment, text-only eligibility and platform acceptance are not certified by the local checks.

## Files

- `packages/<id>.zip`: one question, with `task.json` at the ZIP root.
- `packages/all-questions.zip`: convenience bundle of the individual ZIPs plus usage instructions; extract before importing.
- `DOWNLOADS.md`: direct GitHub download links for all questions.
- `drafts/<id>/task.json`: editable package source, including the completed rubric.
- `drafts/<id>/review.json`: full question and solution as line arrays, source paths and hashes, and AI-assisted rubric provenance. Join each line array with a newline to recover the task text.
- `drafts/manifest.json`: task inventory and package status.
- `rubrics.py`: task-specific AI-assisted grading criteria derived from the existing solutions.
- `requirements.txt`: original supplied Summit instructions, preserved verbatim as historical requirements.
- `convert.py`: migration, completion, validation and packaging commands.

The original Planck Markdown files remain unchanged. All 26 primary tasks are retained, including historical versions and retired candidates. Supporting golden/source files are not independent tasks. The active battery-cycle revision uses answer 29, not the superseded answer 40. Three dedicated golden solutions and two dedicated source documents are reused. No source images exist, so packages use `text_only` and `not_applicable`.

## Rebuild and validate

From the repository root:

```sh
python3 summit/convert.py check
python3 summit/convert.py package
```

Checks cover field sizes, answer precision, rubric count/points/IDs/final-answer alignment, wrong-answer collisions, matching review text, and source hashes. Packaging writes the individual ZIPs, bundle and download index. These checks do not run Summit's quality/difficulty checks or verify the science.

`python3 summit/convert.py complete` fills missing rubrics from the AI-assisted criteria, preserves already-populated rubrics, updates package metadata and rebuilds archives. Edit `task.json` to revise a rubric; edit `rubrics.py` as well if the revision should apply to fresh migrations. When changing a question or solution, synchronize its review line array.

To reproduce into a fresh location:

```sh
python3 summit/convert.py build --output /tmp/planck-summit-new/drafts
python3 summit/convert.py complete --output /tmp/planck-summit-new/drafts
```

Build refuses nonempty destinations. JSON requires escaped backslashes for LaTeX; they decode to the original characters. Import one question ZIP, inspect the rendered fields, and submit through the receiving platform.
