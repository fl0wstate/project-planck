"""Mechanically migrate legacy Planck tasks; never generate scientific content."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

from rubrics import rubric_for


ROOT = Path(__file__).resolve().parents[1]
CATALOG = """
adiabatic_regime|1.373|Physical chemistry|3
annulene_quadrant|9|Organic chemistry|
battery_cycle|29|Physical chemistry / electrochemistry|
battery_v3|18|Physical chemistry / electrochemistry|
belt_census|12|Organic chemistry|
coordination_census|22|Inorganic / coordination chemistry|
debye_screening|2.80|Physical chemistry|2
directional_cube|12|Inorganic / coordination chemistry|
homoaromatic_sum|30|Organic chemistry|
hopf_shift_census|39.75|Optimization & Numerical Mathematics|2
ink_census|5|Physical chemistry|
mixed_stereo_census|18|Organic chemistry|
oligoester_census|3|Organic chemistry|
oligoester_census_v2|6|Organic chemistry|
organic_v3|35.0|Organic chemistry|1
osmotic_polymersome|203|Physical chemistry|0
pentalene_census|1|Physical chemistry / theoretical chemistry|
porphyrin_census|41|Inorganic / stereochemistry|
rotaxane_chirality|9|Organic chemistry|
rotaxane_chirality_v2|16|Organic chemistry|
speciation_optionalfork|12.567|Physical chemistry / coordination equilibria|3
stereogenic_census|15|Organic chemistry|
stereogenic_census_v2|16|Organic chemistry|
tetraradical_gap|3.85|Physical chemistry / magnetochemistry|2
tetraradical_v2|3.85|Physical chemistry / magnetochemistry|2
twistane_final|6|Organic chemistry|
""".strip()
GOLDENS = {
    "porphyrin_census": "planck_task_porphyrin_census_golden.md",
    "rotaxane_chirality_v2": "planck_task_rotaxane_v2_golden.md",
    "stereogenic_census_v2": "planck_task_stereogenic_census_v2_golden.md",
}
SOURCES = {
    "rotaxane_chirality_v2": "planck_task_rotaxane_v2_sources.md",
    "stereogenic_census_v2": "planck_task_stereogenic_census_v2_sources.md",
}


def sections(text):
    headings = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
    return [
        (heading.group(1), text[heading.end():headings[index + 1].start()
         if index + 1 < len(headings) else len(text)].strip())
        for index, heading in enumerate(headings)
    ]


def first_section(text, prefix):
    return next((body for heading, body in sections(text)
                 if heading.lower().startswith(prefix.lower())), "")


def trim_section(body):
    body = re.sub(r"\n---\s*$", "", body).strip()
    fenced = re.fullmatch(r"```(?:text)?\n(.*?)\n```", body, re.DOTALL)
    return fenced.group(1) if fenced else body


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def build(destination):
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Output is not empty; use a fresh --output to protect edits.")
    destination.mkdir(parents=True, exist_ok=True)
    revision = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    records = []
    for row in CATALOG.splitlines():
        slug, answer, subdomain, digits = row.split("|")
        source = ROOT / f"planck_task_{slug}.md"
        original = source.read_text()
        prompt = trim_section(first_section(original, "prompt"))
        prompt = re.sub(r"\n\*\(~[\d,]+ chars\)\*\s*$", "", prompt)
        solution = trim_section(first_section(original, "golden"))
        inputs = [source]
        if slug in GOLDENS:
            golden = ROOT / GOLDENS[slug]
            golden_text = golden.read_text()
            solution = (first_section(golden_text, "Step-by-Step Solution") or
                        re.split(r"^## ", golden_text, maxsplit=1,
                                 flags=re.MULTILINE)[0].split("\n", 1)[1].strip())
            inputs.append(golden)
        references = trim_section(first_section(original, "references"))
        if not references:
            references = "\n".join(line for line in original.splitlines()
                                   if re.match(r"\*\*Source", line))
        if slug in SOURCES:
            reference_source = ROOT / SOURCES[slug]
            references = reference_source.read_text()
            inputs.append(reference_source)
        if not prompt or not solution:
            raise ValueError(f"Missing source section: {slug}")
        task = {
            "domain": "mathematics" if slug == "hopf_shift_census" else "chemistry",
            "subdomain": subdomain,
            "modality": "text_only",
            "taskType": "not_applicable",
            "imageCreationTool": "",
            "imageNecessityExplanation": "",
            "questionText": prompt,
            "answerType": "exact_match",
            "finalAnswer": [f"${answer}$"],
            "acceptableAnswerVariants": [],
            "multipleChoiceOptions": [],
            "answerPrecision": {"kind": "decimal_places", "digits": int(digits)}
            if digits else {"kind": "none"},
            "solution": solution,
            "references": references,
            "rubric": rubric_for(slug, f"${answer}$"),
        }
        folder = destination / slug
        folder.mkdir()
        write_json(folder / "task.json", {
            "schema_version": "summit-task-package-v1", "task": task,
        })
        review = {
            "status": "complete_for_ai_permitted_workflow",
            "rubric_authorship": "AI-assisted, derived from the existing solution; authorized for a workflow permitting AI-authored rubrics.",
            "source_commit": revision,
            "sources": [{"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
                        for path in inputs],
            "question_source": prompt.split("\n"),
            "solution_source": solution.split("\n"),
            "answer_source": "Explicit existing answer key; no answer verification performed.",
            "source_title": original.splitlines()[0],
            "legacy_wrong_branches": trim_section(first_section(original, "wrong branches")
                                                  or first_section(original, "distinct wrong")),
            "required_author_actions": [
                "Use only in a workflow that permits AI-assisted content; these packages do not satisfy the archived Summit human-authorship rule.",
                "Confirm assigned domain and text-only allowance; no image asset exists in the source repository.",
                "Review the preserved question, answer units, LaTeX, numbered solution, and references against the supplied requirements.",
                "Confirm originality, graduate difficulty and suitability; old platform/probe results do not establish Summit acceptance.",
                "Optionally transfer unambiguous wrong answers from legacy_wrong_branches and supply equivalent accepted answer forms.",
            ],
        }
        write_json(folder / "review.json", review)
        records.append({"id": slug, "task": f"{slug}/task.json",
                        "review": f"{slug}/review.json", "status": review["status"]})
    expected = {f"planck_task_{row.split('|')[0]}.md" for row in CATALOG.splitlines()}
    actual = {path.name for path in ROOT.glob("planck_task_*.md")
              if not path.stem.endswith(("_golden", "_sources"))}
    if actual != expected:
        raise ValueError(f"Catalog mismatch: {actual ^ expected}")
    write_json(destination / "manifest.json", {
        "source_repository": "https://github.com/fl0wstate/project-planck",
        "source_commit": revision, "count": len(records), "tasks": records,
    })
    print(f"Converted {len(records)} source tasks into {destination}")


def structural_errors(package):
    errors = []
    if package.get("schema_version") != "summit-task-package-v1":
        errors.append("schema_version")
    task = package["task"]
    for field, limit in (("questionText", 20000), ("solution", 30000)):
        if not isinstance(task.get(field), str) or not 0 < len(task[field]) <= limit:
            errors.append(field)
    answers = task.get("finalAnswer", [])
    if len(answers) != 1 or not isinstance(answers[0], str) or not 0 < len(answers[0]) <= 5000:
        errors.append("finalAnswer")
    if task.get("answerType") != "exact_match":
        errors.append("answerType: this migration supports exact_match only")
    if task.get("modality") != "text_only" or task.get("taskType") != "not_applicable" or "image" in task:
        errors.append("modality: this migration supports text_only only")
    if task.get("domain") not in {"chemistry", "mathematics"}:
        errors.append("domain")
    precision = task.get("answerPrecision", {})
    if precision.get("kind") not in {"none", "decimal_places", "significant_figures"}:
        errors.append("answerPrecision")
    elif precision["kind"] != "none" and (
        type(precision.get("digits")) is not int or precision["digits"] < 0
        or precision["kind"] == "significant_figures" and precision["digits"] == 0
    ):
        errors.append("answerPrecision.digits")
    criteria = task.get("rubric", {}).get("criteria", [])
    if not isinstance(criteria, list) or not 3 <= len(criteria) <= 5:
        errors.append("rubric must contain 3–5 criteria")
    elif any(not isinstance(item, dict) or not isinstance(item.get("description"), str)
             or not item["description"].strip() or type(item.get("points")) is not int
             or item["points"] <= 0 or type(item.get("isFinalAnswer")) is not bool
             or not isinstance(item.get("id"), str) or not item["id"] for item in criteria):
        errors.append("rubric criterion fields")
    else:
        if sum(item["points"] for item in criteria) != 10:
            errors.append("rubric points must total 10")
        if len({item["id"] for item in criteria}) != len(criteria):
            errors.append("rubric criterion IDs must be unique")
        final = [item for item in criteria if item["isFinalAnswer"]]
        if len(final) != 1:
            errors.append("rubric needs exactly one final-answer criterion")
        elif len(answers) == 1:
            if answers[0] not in final[0]["description"]:
                errors.append("final-answer criterion must state the key")
            if any(item["points"] >= final[0]["points"] for item in criteria if not item["isFinalAnswer"]):
                errors.append("final-answer criterion must carry the most points")
    normalize = lambda value: value.strip().strip("$").strip().casefold()
    accepted = task.get("acceptableAnswerVariants", [])
    wrong = task.get("rubric", {}).get("commonWrongAnswers", [])
    if not isinstance(accepted, list) or not isinstance(wrong, list) or any(
        not isinstance(value, str) or not value.strip() or len(value) > 5000
        for value in accepted + wrong
    ):
        errors.append("answer variants and wrong answers must be string arrays")
    elif set(map(normalize, wrong)) & set(map(normalize, answers + accepted)):
        errors.append("common wrong answers include an accepted answer")
    return errors


def check(destination):
    manifest = json.loads((destination / "manifest.json").read_text())
    for record in manifest["tasks"]:
        package = json.loads((destination / record["task"]).read_text())
        errors = structural_errors(package)
        if errors:
            raise ValueError(f"{record['id']}: {errors}")
        review = json.loads((destination / record["review"]).read_text())
        for review_field, task_field in (("question_source", "questionText"),
                                        ("solution_source", "solution")):
            lines = review.get(review_field)
            if not isinstance(lines, list) or not all(
                isinstance(line, str) and "\n" not in line for line in lines
            ):
                raise ValueError(f"{record['id']}: {review_field} must be an array of text lines")
            if "\n".join(lines) != package["task"][task_field]:
                raise ValueError(f"{record['id']}: {review_field} does not match {task_field}")
        for source in review["sources"]:
            if digest(ROOT / source["path"]) != source["sha256"]:
                raise ValueError(f"Source changed: {source['path']}")
    print(f"{len(manifest['tasks'])} tasks passed structure, rubric, review-text and source checks. "
          "These local checks do not certify scientific correctness or platform acceptance.")


def complete(destination):
    manifest_path = destination / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    for record in manifest["tasks"]:
        path = destination / record["task"]
        package = json.loads(path.read_text())
        task = package["task"]
        if not task.get("rubric", {}).get("criteria"):
            task["rubric"] = rubric_for(record["id"], task["finalAnswer"][0])
        errors = structural_errors(package)
        if errors:
            raise ValueError(f"{record['id']}: {errors}")
        write_json(path, package)
        review_path = destination / record["review"]
        review = json.loads(review_path.read_text())
        review["status"] = record["status"] = "complete_for_ai_permitted_workflow"
        review["rubric_authorship"] = "AI-assisted, derived from the existing solution; authorized for a workflow permitting AI-authored rubrics."
        review["required_author_actions"] = [
            "Use only in a workflow that permits AI-assisted content; these packages do not satisfy the archived Summit human-authorship rule.",
            "Confirm your assigned domain and text-only eligibility in the receiving platform.",
            "Review the imported rendering and scientific content before pressing Submit; platform acceptance is not certified by the package checks.",
        ]
        write_json(review_path, review)
    manifest["workflow"] = "AI-assisted content permitted; complete package fields, not a platform acceptance certification."
    write_json(manifest_path, manifest)
    package_drafts(destination)


def package_drafts(destination):
    check(destination)
    manifest = json.loads((destination / "manifest.json").read_text())
    archive_folder = destination.parent / "packages"
    archive_folder.mkdir(exist_ok=True)
    for record in manifest["tasks"]:
        with zipfile.ZipFile(archive_folder / f"{record['id']}.zip", "w",
                             compression=zipfile.ZIP_DEFLATED) as archive:
            info = zipfile.ZipInfo("task.json", date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (destination / record["task"]).read_bytes())
    with zipfile.ZipFile(archive_folder / "all-questions.zip", "w",
                         compression=zipfile.ZIP_DEFLATED) as bundle:
        entries = {
            "README.txt": (
                "Summit question import packages\n\n"
                "Extract this bundle, then import one question ZIP at a time.\n"
                "Each question ZIP contains task.json at its root, including the question, "
                "answer key and solution.\n\n"
                "All packages include a 10-point rubric with one final-answer criterion.\n"
                "Rubrics are AI-assisted, based on the existing solutions. Use these packages "
                "only in a workflow that permits AI-assisted content. They do not satisfy the "
                "archived Summit human-authorship restriction.\n"
                "After import, inspect the form and submit each question individually. "
                "Confirm assigned domain and text-only eligibility. Local package validation "
                "does not certify scientific correctness or platform acceptance.\n"
            ).encode(),
        }
        entries.update({f"{record['id']}.zip":
                        (archive_folder / f"{record['id']}.zip").read_bytes()
                        for record in manifest["tasks"]})
        for name, content in entries.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, content)
    base = "https://github.com/fl0wstate/project-planck/raw/refs/heads/main/summit/packages/"
    download_lines = [
        "# Download individual question packages", "",
        "Each ZIP contains a complete `task.json`: question, answer, solution and a 10-point rubric. Download one ZIP and import it, then review the form and press Submit. Do not upload the all-questions bundle as one task.", "",
        "**AI-permitted workflows only.** Rubrics are AI-assisted. These packages do not meet the archived Summit human-authorship restriction. Platform acceptance, scientific correctness and your assigned domain/text-only eligibility are not certified by local checks.", "",
        f"[Download all {len(manifest['tasks'])} ZIPs together]({base}all-questions.zip) (extract before importing).", "",
        "| Question | Individual ZIP |", "|---|---|",
    ]
    for record in manifest["tasks"]:
        slug = record["id"]
        download_lines.append(f"| {slug.replace('_', ' ')} | [Download ZIP]({base}{slug}.zip) |")
    (destination.parent / "DOWNLOADS.md").write_text("\n".join(download_lines) + "\n")
    print(f"Created {len(manifest['tasks'])} complete AI-permitted packages and download index.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["build", "check", "package", "complete"])
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "drafts")
    arguments = parser.parse_args()
    {"build": build, "check": check, "package": package_drafts, "complete": complete}[arguments.command](arguments.output)
