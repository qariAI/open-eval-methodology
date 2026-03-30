# QariAI Open Evaluation Methodology

**An open-source benchmark for AI Quranic recitation analysis tools.**

> This methodology was authored by [QariAI](https://qariai.app) and is published openly under CC BY 4.0. We believe the Muslim community and AI research community benefit from transparent, shared standards — including for tools that compete with ours.

---

## Why This Exists

There is no shared standard for evaluating AI tools that analyze Quranic recitation. Each tool is evaluated differently, making comparison impossible and allowing misleading claims to go unchecked.

This repository defines five evaluation dimensions, each with test cases, scoring rubrics, and reference recordings. We invite scholars, researchers, and developers — including competitors — to use, critique, and improve it.

---

## Evaluation Dimensions

| # | Dimension | What It Tests |
|---|-----------|---------------|
| 1 | [Phoneme Accuracy](tests/phoneme-accuracy/) | Correct identification of Arabic phonemes (ص vs س, ح vs ه, ط vs ت, etc.) |
| 2 | [Tajweed Rule Detection](tests/tajweed-detection/) | Ghunnah, Idghaam, Ikhfaa, Qalqalah, Madd, Laam Shamsiyyah/Qamariyyah |
| 3 | [Timing & Prosody](tests/timing-prosody/) | Madd lengths (2, 4, 6 harakaat), waqf, pause placement |
| 4 | [Feedback Quality](tests/feedback-quality/) | Actionability, accuracy, and clarity of AI coaching — reviewed by scholars with ijazah |
| 5 | [Demographic Robustness](tests/demographic-robustness/) | Performance across accents (Arab, South Asian, Western, African), ages, and genders |

---

## Repository Structure

```
open-eval-methodology/
├── docs/                          # Methodology design documents
├── tests/
│   ├── phoneme-accuracy/          # Test cases for Arabic phoneme discrimination
│   ├── tajweed-detection/         # Tajweed rule detection benchmarks
│   ├── timing-prosody/            # Timing and prosody evaluation
│   ├── feedback-quality/          # Feedback quality rubrics and scholar reviews
│   └── demographic-robustness/    # Accent, age, and gender robustness tests
├── results/                       # Submitted evaluation results
├── CONTRIBUTING.md
└── LICENSE
```

---

## Scoring

Each dimension uses a 0–100 scale. An overall score is the weighted average:

| Dimension | Weight |
|-----------|--------|
| Phoneme Accuracy | 30% |
| Tajweed Rule Detection | 30% |
| Timing & Prosody | 15% |
| Feedback Quality | 15% |
| Demographic Robustness | 10% |

---

## How to Use This

1. Run your AI tool against the test cases in each `tests/` subfolder
2. Score your results using the rubric in each folder's README
3. Submit results to `results/` via pull request (see [CONTRIBUTING.md](CONTRIBUTING.md))

---

## Disclosure

This methodology was created by QariAI. We run our own tool against these benchmarks and publish our scores in `results/qariai.md`. We do not control the benchmark — pull requests from the community govern its evolution.

---

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)

You are free to use, share, and adapt this methodology for any purpose, including commercial use, as long as you give appropriate credit.
