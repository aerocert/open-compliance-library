# AeroCert Open Compliance Library

Free, high-level compliance checklists for teams building **airborne software** under
[RTCA DO-178B/DO-178C](https://en.wikipedia.org/wiki/DO-178C) and the associated FAA
guidance. Written in plain language for small businesses and startups that don't yet have
an in-house Designated Engineering Representative (DER).

Advancing aviation safety for the public good.

Follow [AeroCert Institute on LinkedIn](https://www.linkedin.com/company/133357306/) for new checklists and plain-language articles, or visit [aerocert.org](https://www.aerocert.org/).

## What's here

Seven plain-language checklists (88 checkpoints total), one per major certification topic:

| Checklist | Checkpoints |
|---|---|
| PSAC / SAS (plans & summary of compliance) | 18 |
| Tool Qualification | 14 |
| Software Plans | 15 |
| Requirements, Design & Code | 10 |
| Software Verification | 11 |
| Configuration Management & Delivery | 10 |
| Reviews, Data & Schedules | 10 |

Each checklist ships in two formats in [`checklists/`](checklists/):

- **`.md`** — human-readable, renders on GitHub.
- **`.json`** — machine-readable (one record per checkpoint) for tooling and retrieval.

## How to use

Work through each checkpoint and answer **Yes / Not yet / Unsure**. A "Not yet" or
"Unsure" is a signal of where to focus your certification effort. Each section states its
regulatory anchor (e.g. *"Based on DO-178B/C §11.1"*) so you can trace it back to the
standard.

## Get them by email

Everything here is free to use as-is, right from this repo. If you'd also like the
library delivered to your inbox — with a link back here plus occasional plain-language
guides on navigating the FAA certification process — sign up via the
[AeroCert Programs page](https://aerocert.org/programs).

## Two tiers

This library is the **free / public tier**: high-level sanity checks, free to use and
share. Regulatory anchors are given at the section level, not per item — that's
intentional. It tells you *whether* you're broadly on track, not the item-level actions
needed to fully close each objective.

The **comprehensive tier** — the detailed, item-level review checklists with the specific
compliance actions and per-item citations, kept current as the standards change — is
available from AeroCert: contact [support@aerocert.org](mailto:support@aerocert.org).

> Use these checklists, share them, and tell us how they worked for you — open an issue
> right here, or write to [support@aerocert.org](mailto:support@aerocert.org).

## Contributing & inquiries

Corrections, clarifications, and suggestions are welcome — open an issue or a pull
request. For certification questions, the master checklists, or engagement inquiries,
contact **support@aerocert.org** — and follow us on [LinkedIn](https://www.linkedin.com/company/133357306/) to hear when new material lands.

Nothing in this library is applicant-confidential or company-specific, and it does not
reproduce copyrighted RTCA text — regulatory anchors are cited at the section level only.
These checklists are guidance, not a substitute for a qualified DER or an FAA finding of
compliance.

## License

Content is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
You may share and adapt it, including commercially, with attribution to AeroCert.
