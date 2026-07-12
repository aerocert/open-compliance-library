# Requirements Design and Code Public Checklist

## Section 1 — Your Software Requirements

_Based on DO-178B/C §5.1 and §11.9, do your high-level software requirements:_
- **(1)** Say what the software must do, developed from the system requirements allocated to software?
- **(2)** Read as verifiable, consistent, and conflict-free — so each one can actually be tested?
- **(3)** Capture derived requirements (ones that do not trace up to a system requirement) and feed them back to the system safety assessment?
## Section 2 — Your Design

_Based on DO-178B/C §5.2 and §11.10, does your design:_
- **(1)** Describe the software architecture and the low-level requirements from which code can be written?
- **(2)** Address how components interact — data flow, control flow, and scheduling?
- **(3)** Handle derived low-level requirements and feed them to the system safety assessment?
## Section 3 — Your Source Code

_Based on DO-178B/C §5.3 and §11.11, is your source code:_
- **(1)** Developed directly from the low-level requirements and the software architecture?
- **(2)** Compliant with your coding standards?
## Section 4 — Traceability Through the Chain

_Based on DO-178B/C §5 and §6:_
- **(1)** Can you trace from system requirements to software requirements to design to code — and back the other way?
- **(2)** Does every piece of code exist because a requirement asked for it, with no unintended or untraceable code?
  - Note: This free checklist is a high-level sanity check — free to use and share. It doesn't include the item-level actions needed to fully close each objective; those live in AeroCert's comprehensive checklist, kept current as the standards change and available through donations. We'd love to hear how it worked for you — tell us at support@aerocert.org.
