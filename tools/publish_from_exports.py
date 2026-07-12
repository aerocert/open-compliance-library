#!/usr/bin/env python3
"""Copy the 7 PUBLIC-tier checklist exports into the Open Compliance Library repo layout.

Selects only `*_Public_Checklist.{md,json}` from the workspace exports dir (master exports
and *_CHANGELOG.md are left behind) and copies them into ../checklists/. Runs a light
confidentiality gate on every file it copies; refuses to copy a file that trips it.

The real company-name / applicant-confidential wall is enforced upstream by
validate_checklist.py on the .xlsx masters — this gate is a last-line backstop, not a
replacement for it.

Usage:
    python publish_from_exports.py                 # default source, dry run off
    python publish_from_exports.py --src <dir> --dry-run
"""
import argparse, pathlib, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_SRC = HERE.parent.parent.parent / "work-in-progress" / "exports"
DEST = HERE.parent / "checklists"

# ponytail: minimal backstop denylist — obvious confidential markers only.
# The authoritative company-name wall is validate_checklist.py on the .xlsx.
DENYLIST = ["confidential", "proprietary", "company confidential", "not for distribution"]


def gate(text):
    low = text.lower()
    return [term for term in DENYLIST if term in low]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=pathlib.Path, default=DEFAULT_SRC)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    src = a.src.resolve()
    files = sorted(p for ext in ("md", "json")
                   for p in src.glob(f"*_Public_Checklist.{ext}"))
    if not files:
        sys.exit(f"No *_Public_Checklist.(md|json) found in {src}")

    md = [f for f in files if f.suffix == ".md"]
    print(f"Found {len(md)} public checklists ({len(files)} files) in {src}")

    tripped = False
    for f in files:
        hits = gate(f.read_text(encoding="utf-8"))
        if hits:
            tripped = True
            print(f"  BLOCKED {f.name}: confidentiality markers {hits}")
    if tripped:
        sys.exit("Refusing to publish: confidentiality gate tripped. Review the files above.")

    if a.dry_run:
        print("Dry run — would copy:")
        for f in files:
            print(f"  {f.name}")
        return

    DEST.mkdir(parents=True, exist_ok=True)
    for f in files:
        shutil.copy2(f, DEST / f.name)
    print(f"Copied {len(files)} files -> {DEST}")


if __name__ == "__main__":
    main()
