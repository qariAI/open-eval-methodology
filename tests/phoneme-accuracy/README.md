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
| ص / س | Emphatic vs. plain sibilant | صَارَ vs سَارَ |
| ح / ه | Pharyngeal vs. glottal fricative | حَلَّ vs هَلَّ |
| ط / ت | Emphatic vs. plain plosive | طِين vs تِين |
| ذ / ز | Interdental vs. alveolar fricative | ذَلَّ vs زَلَّ |
| ظ / ض | Emphatic interdental vs. emphatic lateral | ظَلَّ vs ضَلَّ |
| ع / أ | Pharyngeal vs. glottal stop | عَلِمَ vs أَلِمَ |
| غ / خ | Voiced vs. voiceless uvular fricative | غَابَ vs خَابَ |
| ق / ك | Uvular vs. velar plosive | قُل vs كُل |

Example words are real Arabic minimal pairs; scholar review of the final list is pending.

---

## Test Case Format

Each test case is a JSON file with the following structure:

```json
{
  "id": "phoneme-001",
  "surah": 1,
  "ayah": 6,
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
Per pair, compute **recall** (errors detected / error recordings) and **false-positive rate** (flags on correct recordings / correct recordings). Pair score = 100 × F1, with a 95% bootstrap confidence interval reported. A tool that detects nothing scores 0.

**Overall phoneme accuracy score** = average across all pairs, weighted by frequency in the Quran.

---

## Reference

Test cases reference recordings from the recitation of Sheikh Mahmoud Khalil Al-Hussary (Murattal) as the gold standard.
