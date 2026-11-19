# Methodology Design

## Guiding Principles

1. **Transparency** — all test cases, scoring rubrics, and results are public
2. **Scholar grounding** — evaluation criteria are derived from established Tajweed science, not AI conventions
3. **Community governance** — the benchmark evolves through pull requests, not unilateral decisions by QariAI
4. **Equity** — performance must be measured across the full diversity of the Muslim community
5. **Honesty** — QariAI publishes its own scores, including unfavorable results. As of v1.0.0 no scores are published yet because the test suite is incomplete.

## Design Decisions

### Why 5 Dimensions?
The five dimensions cover the full pipeline of a recitation evaluation tool:
- Input quality (phoneme recognition)
- Rule application (tajweed detection)
- Temporal accuracy (timing)
- Output quality (feedback)
- Generalization (demographics)

### Why Weighted Scoring?
Phoneme accuracy and tajweed detection are weighted highest (30% each) because they represent the core function of any recitation tool. Timing and feedback quality are secondary but important. Demographic robustness is lower-weighted but a minimum bar — a tool that scores zero here should not be considered production-ready.

### Why Scholar Review for Feedback Quality?
AI metrics cannot evaluate whether feedback is Islamically appropriate, pedagogically sound, or culturally sensitive. Human reviewers with ijazah are the authoritative source for this dimension.

## Versioning

This methodology uses semantic versioning:
- **Major version:** Change in dimension weights or scoring rubrics
- **Minor version:** Addition of new test cases
- **Patch:** Corrections to existing test cases

Current version: **1.0.0** (draft: specification only; see CHANGELOG.md)

## Limitations

- This methodology covers Hafs 'an 'Asim only (the most widely used riwayah). Other riwayaat are out of scope for v1.
- Audio quality of test recordings affects results — reference recordings come from varied sources (e.g. archival Murattal) and recording conditions are documented per file in the case metadata.
- This is not a comprehensive Quran recitation curriculum — it tests AI tools, not human reciters.
