# Tool Qualification Public Checklist

## Section 1 — Deciding Which Tools Need Qualification

_Based on DO-178B/C §12.2, have you worked out which tools need qualification:_
- **(1)** Have you identified every tool whose output you rely on without independently checking it, so a tool error could put a fault into your software or let one slip past your verification?
- **(2)** For each such tool, have you decided whether it is a development tool (its output ends up in the airborne software) or a verification tool (it could fail to catch an error)?
- **(3)** Have you assigned each tool a Tool Qualification Level (TQL) based on how it is used and your software level?
## Section 2 — Your Tool Qualification Plan

_Based on DO-178B/C §12.2 (and, for DO-178C projects, DO-330):_
- **(1)** Do you have a plan describing how each tool will be qualified, at a rigor matching its TQL?
- **(2)** Does the plan capture the tool operational requirements — what the tool must do, in your environment, for you to trust it?
- **(3)** Have you agreed the qualification approach with the certification authority (for example, stated it in your PSAC)?
## Section 3 — Building the Tool Qualification Data

_For DO-178C projects, DO-330 sets the tool life-cycle data:_
- **(1)** For higher-TQL tools, do you have the tool requirements, design, and configuration data your plan calls for?
- **(2)** Are the standards used to develop or configure the tool identified?
## Section 4 — Showing the Tool Actually Works

_Based on DO-178B/C §12.2 (and DO-330 for DO-178C projects):_
- **(1)** Have you verified the tool against its operational requirements — that it does what you need, in your real environment?
- **(2)** For higher-TQL tools, have you verified the tool's own requirements, design, and code to the extent required?
- **(3)** Do the results show every planned qualification case was run and passed, with any failures resolved?
## Section 5 — Controlling and Summarizing the Tool

_Based on DO-178B/C §7 and §12.2 (and DO-330 for DO-178C projects):_
- **(1)** Is the tool under configuration management — a known version, with its environment recorded so a result can be reproduced later?
- **(2)** Is there quality-assurance oversight of the tool qualification activity?
- **(3)** Do you have a tool configuration index and a summary that record what was qualified and how it meets its objectives?
  - Note: This free checklist is a high-level sanity check — free to use and share. It doesn't include the item-level actions needed to fully close each objective; those live in AeroCert's comprehensive checklist, kept current as the standards change and available through donations. We'd love to hear how it worked for you — tell us at support@aerocert.org.
