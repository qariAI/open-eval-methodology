# Methodology Design

## Guiding Principles

1. **Transparency** — all test cases, scoring rubrics, and results are public
2. **Scholar grounding** — evaluation criteria are derived from established Tajweed science, not AI conventions
3. **Community governance** — the benchmark evolves through pull requests, not unilateral decisions by QariAI
4. **Equity** — performance must be measured across the full diversity of the Muslim community
5. **Honesty** — QariAI publishes its own scores, including unfavorable results

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

Current version: **1.0.0**

## Limitations

- This methodology covers Hafs 'an 'Asim only (the most widely used riwayah). Other riwayaat are out of scope for v1.
- Audio quality of test recordings affects results — all reference recordings use the same equipment and conditions.
- This is not a comprehensive Quran recitation curriculum — it tests AI tools, not human reciters.
