# Dimension 4: Feedback Quality

**Weight: 15% of overall score**

This dimension evaluates the quality of the AI tool's feedback to the user — not just whether it detected an error, but whether its explanation is accurate, actionable, and useful for a learner.

---

## Why This Matters

An AI tool can detect an error and still give feedback that is:
- Technically wrong (mislabeling the rule)
- Too vague to act on ("your recitation needs improvement")
- Overwhelming (listing 10 issues when only 2 are significant)
- Culturally inappropriate for a learner of the Quran

Feedback quality is evaluated by human reviewers, including scholars with ijazah.

---

## Evaluation Criteria

### 1. Accuracy (0–25 points)
Is the feedback technically correct?
- 25: Perfectly accurate — correct rule name, correct explanation
- 15: Mostly accurate with minor terminology errors
- 5: Identifies the area but gives wrong rule or incorrect description
- 0: Factually incorrect feedback

### 2. Actionability (0–25 points)
Can a learner act on this feedback?
- 25: Specific, concrete instruction ("Hold the waw for 4 counts, not 2")
- 15: General guidance ("Extend the madd here")
- 5: Vague ("Work on your pronunciation")
- 0: No actionable guidance

### 3. Completeness (0–25 points)
Does the feedback cover the most important errors without overwhelming?
- 25: Prioritizes critical errors, ignores negligible ones
- 15: Covers main errors but includes minor distractions
- 5: Misses critical errors or overwhelms with minor ones
- 0: No meaningful coverage of actual errors

### 4. Clarity (0–25 points)
Is the feedback understandable to a learner at the stated proficiency level?
- 25: Language and concepts appropriate for the learner's level
- 15: Mostly clear with some technical jargon
- 5: Heavy jargon without explanation
- 0: Incomprehensible or contradictory

---

## Scholar Review Process

Feedback samples are submitted to reviewers with the following credentials:
- Minimum: Completion of Quran memorization with ijazah
- Preferred: Teaching experience with students at multiple proficiency levels
- Blinded: Reviewers do not know which tool produced the feedback

---

## Test Case Format

```json
{
  "id": "feedback-001",
  "recitation_error": "Qalqalah missing on ق at end of ayah",
  "tool_feedback": "The feedback text the AI tool produced",
  "reciter_level": "Beginner",
  "scholar_score": {
    "accuracy": 20,
    "actionability": 15,
    "completeness": 20,
    "clarity": 25,
    "total": 80,
    "reviewer_notes": "Correct identification but could be more specific about qalqalah technique"
  }
}
```

---

## Submitting for Scholar Review

If you have ijazah and wish to participate as a reviewer, open an issue with the label `scholar-reviewer`. Your reviews will be credited by name (or anonymously, by your choice).
