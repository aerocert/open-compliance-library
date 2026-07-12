# Software Verification Public Checklist

## Section 1 — Your Test Cases and Procedures

_Based on DO-178B/C §6 and §11.13, do your test cases and procedures:_
- **(1)** Come from your requirements (requirements-based testing), rather than just from the code?
- **(2)** Include normal-range cases that check the software works as intended?
- **(3)** Include robustness cases that check it behaves safely with invalid, unexpected, or boundary inputs?
- **(4)** Define the test environment, so someone else could reproduce your testing?
## Section 2 — Your Verification Results

_Based on DO-178B/C §11.14, do your verification results:_
- **(1)** Show that every planned test, review, and analysis was actually run?
- **(2)** Record anything that failed as a problem report, and show it was resolved or dispositioned?
## Section 3 — Your Verification Analyses

_Based on DO-178B/C §6.3 and §6.4, have you:_
- **(1)** Reviewed and analyzed the requirements, design, and code (not only tested them) for correctness and consistency?
- **(2)** Analyzed requirements-based test coverage — that your tests cover every requirement?
- **(3)** Analyzed structural coverage — that your tests exercised the code to the level your software level demands (statement, decision, or MC/DC)?
- **(4)** Explained or resolved any code or data your tests did not cover?
## Section 4 — Traceability

_Based on DO-178B/C §6:_
- **(1)** Can you trace requirements to test cases to results, so you can show each requirement was verified?
  - Note: This free checklist is a high-level sanity check — free to use and share. It doesn't include the item-level actions needed to fully close each objective; those live in AeroCert's comprehensive checklist, kept current as the standards change and available through donations. We'd love to hear how it worked for you — tell us at support@aerocert.org.
