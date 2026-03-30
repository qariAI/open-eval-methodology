# Dimension 3: Timing & Prosody

**Weight: 15% of overall score**

This dimension tests whether an AI tool correctly evaluates the timing, rhythm, and prosodic features of Quranic recitation — beyond individual phoneme or tajweed rule errors.

---

## What Is Tested

### 1. Madd Duration Accuracy
Madd (elongation) rules specify exact durations in harakaat. This tests whether the tool can measure and flag incorrect durations.

| Madd Type | Correct Duration | Common Error |
|-----------|-----------------|--------------|
| Tabee'i | 2 harakaat | Extended to 3+ |
| Munfasil | 4–5 harakaat | Shortened to 2 |
| Muttasil | 4–5 harakaat | Shortened to 2 |
| Lazim | 6 harakaat | Shortened to 4 |

### 2. Waqf (Stopping Rules)
Correct stopping points at end of ayah and mid-ayah waqf marks.
- **Mandatory stop (م):** Tool should flag if reciter continues
- **Prohibited stop (لا):** Tool should flag if reciter stops
- **Preferred stop (قلى):** Optional but should be recognized
- **Common error:** Stopping mid-word or at grammatically incorrect positions

### 3. Sukoon Timing
Letters with sukoon should have no vowel sound. Duration of sukoon should be consistent.

### 4. Rhythm Consistency
Overall rhythm should be consistent — neither rushed nor artificially slowed. Evaluated relative to the reciter's own established tempo.

---

## Test Case Format

```json
{
  "id": "timing-001",
  "type": "madd_duration",
  "madd_type": "muttasil",
  "surah": 1,
  "ayah": 4,
  "word": "مَالِكِ",
  "expected_duration_harakaat": 5,
  "correct_recording": "recordings/timing-001-correct.mp3",
  "error_recording": "recordings/timing-001-error-short.mp3",
  "error_description": "Madd shortened to 2 harakaat",
  "expected_detection": true
}
```

---

## Scoring Rubric

| Score | Criteria |
|-------|----------|
| 100 | Correctly identifies timing error, specifies correct duration |
| 75 | Identifies error exists but gives imprecise duration guidance |
| 50 | Detects major errors (50%+ too short/long) but misses subtle ones |
| 25 | Only detects gross timing violations |
| 0 | No timing evaluation capability |

---

## Notes

Timing evaluation is inherently more subjective than phoneme or tajweed evaluation. Scores should be interpreted in context of the recitation style (Murattal vs. Mujawwad).
