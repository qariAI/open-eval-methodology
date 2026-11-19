# Dimension 2: Tajweed Rule Detection

**Weight: 30% of overall score**

This dimension tests whether an AI tool correctly identifies violations of Tajweed rules — the precise phonetic rules governing Quranic recitation as established by scholars of the Quran.

---

## Rules Under Test

### 1. Ghunnah (غنة)
Nasalization of ن and م when mushaddad (doubled); also present in idgham with ghunnah, ikhfaa, iqlab and ikhfaa shafawi.
- **Duration:** 2 harakaat
- **Common error:** Shortening or omitting the nasal resonance

### 2. Idghaam (إدغام)
Merging of noon sakinah or tanween into the following letter.
- **With ghunnah:** ي ن م و
- **Without ghunnah:** ل ر
- **Applies only across two words.** Exceptions: دنيا, قنوان, صنوان, بنيان (read with izhar).
- **Common error:** Pronouncing the noon clearly instead of merging

### 3. Ikhfaa (إخفاء)
Partial concealment of noon sakinah or tanween before 15 letters.
- **Common error:** Full pronunciation (Izhar) or full merging (Idghaam) instead of the middle state

### 4. Qalqalah (قلقلة)
Echo/bounce applied to ق ط ب ج د when sukoon or at end of word.
- **Levels:** Sughra (mid-word), Wusta (end of word when continuing), Kubra (end of word when stopping)
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
  "ayah": 6,
  "word": "إِنَّ",
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
Per rule, compute **recall**, **false-positive rate** and **rule-naming accuracy** (flagged violations labelled with the correct rule). Rule score = 100 × (0.5 × F1 + 0.5 × naming accuracy), capped at 100, with a 95% bootstrap CI. Quality of explanation is scored only in Dimension 4, not here.

---

## Scholar Validation

Test cases follow riwayat Hafs 'an 'Asim, tariq al-Shatibiyyah. Scholar review is **pending**; named reviewers and dates will be listed in `docs/reviewers.md` once complete. No case is considered validated before then.
