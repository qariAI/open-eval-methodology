# Governance

## Status
Draft. QariAI currently maintains this repository and is also an evaluated tool. That is a conflict of interest, handled as follows.

## Rules
- Changes to weights, rubrics or scoring formulas (major version) need approval from at least two maintainers, at least one not employed by QariAI, plus a 14-day public comment period.
- QariAI may not approve changes that affect its own score in the same release it is scored in.
- Test-case changes need review by a qualified scholar (ijazah in Hafs 'an 'Asim). Reviewer names and dates are listed in `docs/reviewers.md`.
- A private holdout set (maintained by non-QariAI maintainers) is used for official results; public cases are for development only.
- Any result must be accompanied by raw tool outputs, tool version, run settings and date. Results without them are marked "unverified".
- Conflicts and disputes: open an issue labelled `methodology`; decisions are recorded in the issue.

## Maintainers
- QariAI: Nabil (founder)
- Independent maintainers: *seeking at least one scholar and one researcher*
