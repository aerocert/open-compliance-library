# Configuration Management and Delivery Public Checklist

## Section 1 — Your Software Configuration Index (SCI)

_Based on DO-178B/C §11.16, does your Software Configuration Index:_
- **(1)** Identify exactly what makes up the software — every component, version, and part number?
- **(2)** Identify the tools, settings, and environment needed to rebuild the software from scratch?
- **(3)** List the life-cycle data and its versions, so the build is fully reproducible?
## Section 2 — Configuration Management Discipline

_Based on DO-178B/C §7, in your day-to-day configuration management:_
- **(1)** Is everything under control uniquely identified, with changes recorded and traceable to problem reports?
- **(2)** Can you reproduce a released build exactly from the controlled data?
## Section 3 — First Article Inspection / Conformity

_Based on FAA software conformity and first-article-inspection expectations:_
- **(1)** Have you confirmed the software actually loaded on the hardware matches the released part number and version (a conformity check)?
- **(2)** Is the delivered media correctly labeled and formatted, with the right part numbers?
- **(3)** Do you have the acceptance records showing the article was inspected and accepted?
## Section 4 — Delivery

_Based on DO-178B/C §7.2.7 and §11.16, when you deliver:_
- **(1)** Do you deliver the controlled version together with its configuration index and the instructions to reproduce it?
- **(2)** For pre-production or engineering releases, is the release status clearly marked, so a development build is not mistaken for a certified one?
  - Note: This free checklist is a high-level sanity check — free to use and share. It doesn't include the item-level actions needed to fully close each objective; those live in AeroCert's comprehensive checklist, kept current as the standards change and available from AeroCert. We'd love to hear how it worked for you — tell us at support@aerocert.org.
