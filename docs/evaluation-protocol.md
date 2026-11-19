# Evaluation Protocol (draft)

## Running a tool
1. Record tool name, version/build, model(s) used, date, and any prompt or configuration.
2. Feed each recording as provided (original format, no re-encoding unless the tool requires it; document any conversion).
3. For non-deterministic tools (e.g. LLM-based), run each recording 3 times at default settings and report the mean and the spread.
4. Do not tune the tool on the public cases and then report results on them as official; official results use the private holdout.

## Definition of "detected"
A violation counts as detected if the tool flags the correct word (or a window overlapping the error by at least 50%) within the recording. Extra flags on correct recordings are false positives.

## Private evaluation
Recordings that cannot be shared (children, consent-restricted) are evaluated by maintainers on tools submitted via API or a tool-supplied endpoint. Only aggregated scores are published.

## Metrics
- Detection: recall, false-positive rate, F1, with 95% bootstrap confidence intervals.
- Feedback quality: at least 3 blinded scholar reviewers per sample; report Krippendorff's alpha. Samples below alpha 0.6 are re-reviewed.

## Reporting
Use `results/TEMPLATE.md`. Attach raw outputs. Report unfavourable results.
