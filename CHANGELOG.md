# Changelog

## Unreleased (spec fixes after audit)
- Corrected example cases (phoneme-001 ayah, timing-001 madd type, tajweed-001 ghunnah word) and replaced non-word phoneme examples with real minimal pairs.
- Scoring: replaced coarse bins with recall / false-positive rate / F1 with confidence intervals; removed tajweed +10 bonus and feedback double-counting.
- Demographic score now cannot reward uniformly poor tools; minimum group sizes added.
- Added GOVERNANCE.md, evaluation protocol, results template, reviewers list.
- Clarified that no scores or scholar validation exist yet.

## 1.0.0
- Initial specification.
