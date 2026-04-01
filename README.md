# QariAI Open Evaluation Methodology

**An open benchmark for evaluating AI systems that analyze Quranic recitation.**

> Developed by QariAI (https://qariai.app) and released under CC BY 4.0 to establish transparent, reproducible standards for assessing Tajweed-aware AI systems.

---

## Canonical References

This repository defines the **technical specification** of the evaluation methodology.

For a conceptual overview:
https://www.qariai.app/quran-learning-methodology-evaluation

For the applied framework (QAEF):
https://www.qariai.app/qaef

---

## 1. Purpose and Scope

There is currently no standardized framework for evaluating AI-driven Quranic recitation tools. Existing systems are assessed using inconsistent, non-transparent criteria, making meaningful comparison impossible.

This repository defines a **multi-dimensional evaluation methodology** grounded in:

- Arabic phonetics (makharij and sifaat)  
- Tajweed rule systems  
- Temporal recitation structure (prosody)  
- Pedagogical feedback quality  
- Cross-demographic robustness  

The goal is to enable:
- Reproducible benchmarking  
- Transparent comparison across tools  
- Community-driven standardization  

---

## 2. Evaluation Philosophy

A valid Quranic recitation evaluation system must satisfy five conditions:

1. Phonetic fidelity — accurate recognition of articulation and sound properties  
2. Rule compliance — correct detection of Tajweed rules within context  
3. Temporal precision — alignment with prescribed durations and pauses  
4. Instructional usefulness — feedback that is accurate and actionable  
5. Robustness — consistent performance across diverse speakers  

---

## 3. Evaluation Dimensions

| # | Dimension | Operational Definition |
|---|----------|----------------------|
| 1 | [Phoneme Accuracy](tests/phoneme-accuracy/) | Correct classification of Arabic phonemes based on articulation point (makhraj) and phonetic features (sifaat) |
| 2 | [Tajweed Rule Detection](tests/tajweed-detection/) | Identification of Tajweed rule application (ghunnah, idghaam, ikhfaa, qalqalah, madd, etc.) within valid context |
| 3 | [Timing & Prosody](tests/timing-prosody/) | Measurement of recitation timing including madd duration, waqf (pauses), and rhythm |
| 4 | [Feedback Quality](tests/feedback-quality/) | Degree to which system feedback is accurate, specific, and pedagogically actionable |
| 5 | [Demographic Robustness](tests/demographic-robustness/) | Stability of performance across accents, age groups, and genders |

---

## 4. Repository Structure
