# Publishing the Open Compliance Library — manual owner steps

This is a **local scaffold**. Nothing here is pushed anywhere automatically. Every step
below is performed by the owner (Laura). Do not push until the confidentiality wall is
confirmed (step 2).

## Pre-flight (in this workspace)

0. **Programs page live FIRST (ruled 2026-07-11).** The README funnels to
   `aerocert.org/programs` — do not push this repo until that page is live with a
   working MailerLite form (clear the TODO/BLOCKER comments in
   `C:/Workspace/website/programs.html`: real subscribe action, anti-spam
   field, sender-domain auth). Also verify the final URL matches the README link.

1. **Sync the checklist content.** After Task A (CTA reframe) lands and the 7 public
   `.md`/`.json` exports are regenerated, refresh the repo copy:
   ```bash
   python tools/publish_from_exports.py
   ```
   This copies only `*_Public_Checklist.{md,json}` into `checklists/` and runs a
   confidentiality backstop scan. (Add `--dry-run` to preview.)

2. **Confirm the confidentiality wall** on everything in `checklists/`:
   - No company names, no applicant-confidential data.
   - No verbatim RTCA text — section-level anchors only.
   - DO-330 referenced as DO-178C-only where tool qualification appears.
   The upstream `validate_checklist.py` (run in Task A on the `.xlsx`) is the
   authoritative check; the publish script's scan is a last-line backstop.

3. **Finalize the LICENSE.** Replace the placeholder `LICENSE` with the full CC BY 4.0
   legal code (see step 6 — easiest via GitHub's license picker).

## Create and publish the GitHub repo (owner)

4. **Create the org/repo** on GitHub:
   - Org: `<owner decides — e.g. aerocert>`
   - Repo name: `<owner decides — e.g. open-compliance-library>`
   - Visibility: **Public**
   - Description: "Free plain-language DO-178B/C compliance checklists for airborne software."

5. **Push this scaffold** as the initial commit:
   ```bash
   cd C:/Workspace/open-compliance-library
   git init && git add . && git commit -m "Initial public library"
   git branch -M main
   git remote add origin git@github.com:<org>/<repo>.git
   git push -u origin main
   ```
   (Decide whether to include `tools/publish_from_exports.py` — it's a maintainer helper
   that points at internal workspace paths. Exclude it via `.gitignore` if you'd rather
   not ship it.)

6. **Add the full license via GitHub** (guaranteed-correct legal text): repo → Add file →
   Create new file → name it `LICENSE` → "Choose a license template" → **Creative Commons
   Attribution 4.0** → commit. This overwrites the placeholder.

7. **Sanity-check the rendered repo:** README renders, checklists render, license is
   detected by GitHub ("CC-BY-4.0" badge on the repo home).

## Ongoing

- The website stays the primary front door; this repo is a secondary distribution channel.
- When a checklist changes upstream, re-run `tools/publish_from_exports.py` and push.
