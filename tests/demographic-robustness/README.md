# Dimension 5: Demographic Robustness

**Weight: 10% of overall score**

This dimension tests whether an AI tool performs consistently across reciters of different backgrounds — accents, ages, and genders. A tool that works well for Arab adult males but fails for South Asian women or young children is not fit for the global Muslim community.

---

## Why This Matters

The global Muslim population is 1.8 billion people across dozens of linguistic backgrounds. AI tools trained primarily on professional Arab male reciters will systematically disadvantage:
- Non-Arab Muslims (the majority of Muslims globally)
- Children learning to recite
- Women reciters
- Elderly reciters

This dimension holds tools accountable for equitable performance.

---

## Demographic Groups Under Test

### By Accent/Linguistic Background
| Group | Description |
|-------|-------------|
| Native Arabic (Gulf) | Gulf Arabic L1 speakers |
| Native Arabic (Levantine) | Syrian, Lebanese, Palestinian L1 speakers |
| Native Arabic (Egyptian) | Egyptian Arabic L1 speakers |
| South Asian | Urdu/Hindi, Bengali, Pashto L1 speakers |
| Southeast Asian | Malay, Indonesian L1 speakers |
| Western | English, French L1 speakers |
| African | Hausa, Swahili, Somali L1 speakers |
| Turkish/Central Asian | Turkish, Uzbek L1 speakers |

### By Age
| Group | Description |
|-------|-------------|
| Children (6–12) | Learning stage, developing pronunciation |
| Teens (13–17) | Intermediate, often memorizing |
| Adults (18–50) | Primary learner demographic |
| Elderly (50+) | May have established habits, voice changes |

### By Gender
- Male reciters
- Female reciters

---

## Scoring Method

For each demographic group, run the full phoneme + tajweed test suite and record the score. The demographic robustness score measures **consistency** across groups, not absolute performance.

**Score = 100 − (max_group_score − min_group_score)**

A tool that scores 80 for all groups gets 100 (perfectly consistent).
A tool that scores 90 for Arab males and 50 for South Asian women gets 60 (40-point gap).

---

## Test Case Format

```json
{
  "id": "demo-001",
  "reciter_id": "anon-001",
  "linguistic_background": "South Asian (Urdu L1)",
  "age_group": "adult",
  "gender": "female",
  "recording": "recordings/demo-001.mp3",
  "ground_truth_errors": ["ikhfaa_missed", "madd_shortened"],
  "tool_detected": ["madd_shortened"],
  "detection_rate": 0.5,
  "false_positive_count": 0
}
```

---

## Ethical Guidelines

- All recordings are collected with explicit informed consent
- Reciter identities are anonymized
- No recordings of children are shared publicly — only aggregated scores
- Results are reported per demographic group, not per individual

---

## Call for Contributions

We especially need recordings from underrepresented groups. If you can contribute anonymized recordings or connect us with community members who can, please open an issue labeled `recordings-needed`.
