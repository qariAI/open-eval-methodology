# Dimension 1: Phoneme Accuracy

**Weight: 30% of overall score**

This dimension tests whether an AI tool can correctly distinguish Arabic phonemes that are frequently confused by non-native speakers or mispronounced in recitation.

---

## Why This Matters

Arabic contains phonemes absent in most other languages. Confusing ص and س, or ح and ه, or ط and ت changes the meaning of words and constitutes a recitation error. An AI tool that cannot reliably detect these errors provides false confidence to learners.

---

## Phoneme Pairs Under Test

| Pair | Description | Example Word |
|------|-------------|--------------|
| ص / س | Emphatic vs. plain sibilant | صِرَاطَ vs سِرَاط |
| ح / ه | Pharyngeal vs. glottal fricative | حَمْد vs هَمْد |
| ط / ت | Emphatic vs. plain plosive | طَرِيق vs تَرِيق |
| ذ / ز | Interdental vs. alveolar fricative | ذَلِك vs زَلِك |
| ظ / ض | Emphatic interdental vs. emphatic lateral | ظَلَم vs ضَلَم |
| ع / أ | Pharyngeal vs. glottal stop | عَالَم vs أَالَم |
| غ / خ | Voiced vs. voiceless uvular fricative | غَيب vs خَيب |
| ق / ك | Uvular vs. velar plosive | قُل vs كُل |

---

## Test Case Format

Each test case is a JSON file with the following structure:

```json
{
  "id": "phoneme-001",
  "surah": 1,
  "ayah": 2,
  "target_phoneme": "ص",
  "confusable_phoneme": "س",
  "word": "الصِّرَاطَ",
  "correct_recording": "recordings/phoneme-001-correct.mp3",
  "error_recording": "recordings/phoneme-001-error.mp3",
  "expected_detection": true,
  "notes": "Emphatic س replacing ص — common error among non-Arab reciters"
}
```

---

## Scoring Rubric

| Score | Criteria |
|-------|----------|
| 100 | Detects all errors in this pair across all test cases |
| 75 | Detects >75% of errors, no false positives |
| 50 | Detects >50% of errors OR has significant false positives |
| 25 | Detects <50% of errors |
| 0 | Does not detect this phoneme pair at all |

**Overall phoneme accuracy score** = average across all pairs, weighted by frequency in the Quran.

---

## Reference

Test cases reference recordings from the recitation of Sheikh Mahmoud Khalil Al-Hussary (Murattal) as the gold standard.
