# Dimension 2: Tajweed Rule Detection

**Weight: 30% of overall score**

This dimension tests whether an AI tool correctly identifies violations of Tajweed rules — the precise phonetic rules governing Quranic recitation as established by scholars of the Quran.

---

## Rules Under Test

### 1. Ghunnah (غنة)
Nasalization applied to ن and م when mushaddad (doubled), or when followed by specific letters.
- **Duration:** 2 harakaat
- **Common error:** Shortening or omitting the nasal resonance

### 2. Idghaam (إدغام)
Merging of noon sakinah or tanween into the following letter.
- **With ghunnah:** ي ن م و
- **Without ghunnah:** ل ر
- **Common error:** Pronouncing the noon clearly instead of merging

### 3. Ikhfaa (إخفاء)
Partial concealment of noon sakinah or tanween before 15 letters.
- **Common error:** Full pronunciation (Izhar) or full merging (Idghaam) instead of the middle state

### 4. Qalqalah (قلقلة)
Echo/bounce applied to ق ط ب ج د when sukoon or at end of word.
- **Levels:** Minor (mid-word), Major (end of word/ayah)
- **Common error:** Missing the echo entirely or applying it incorrectly

### 5. Madd (مد)
Elongation of vowels — multiple types with specific durations.
- **Madd Tabee'i:** 2 harakaat (natural)
- **Madd Munfasil:** 4–5 harakaat
- **Madd Muttasil:** 4–5 harakaat (obligatory)
- **Madd Lazim:** 6 harakaat
- **Common error:** Wrong duration, especially shortening obligatory madd

### 6. Laam Shamsiyyah / Qamariyyah (لام شمسية / قمرية)
Solar letters assimilate the laam of ال; lunar letters do not.
- **Common error:** Pronouncing the laam before solar letters

---

## Test Case Format

```json
{
  "id": "tajweed-001",
  "rule": "ghunnah",
  "surah": 2,
  "ayah": 7,
  "word": "خَتَمَ",
  "context": "Full ayah text",
  "correct_recording": "recordings/tajweed-001-correct.mp3",
  "error_recording": "recordings/tajweed-001-error.mp3",
  "error_type": "shortened_ghunnah",
  "severity": "Major",
  "expected_detection": true
}
```

---

## Scoring Rubric

| Score | Criteria |
|-------|----------|
| 100 | Correctly identifies rule violation, names the rule, gives actionable feedback |
| 75 | Identifies violation but misnames rule or gives vague feedback |
| 50 | Identifies something is wrong but cannot specify the rule |
| 25 | Inconsistent detection (catches <50% of violations) |
| 0 | Does not detect this rule category |

**Bonus:** +10 points if the tool correctly explains the rule in learner-friendly language.

---

## Scholar Validation

All test cases in this dimension have been reviewed against the rules of Hafs 'an 'Asim by the riwayah of Shatibiyyah.
