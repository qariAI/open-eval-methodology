"""Run from repo root: python3 -I -m unittest discover -s scorer -p "test_*.py"
Synthetic data only; these are not Quran test cases."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from score import demographic_score, f1_and_naming  # noqa: E402


def mk(has_error, flagged, rule="r", out_rule="r"):
    return ({"has_error": has_error, "rule": rule}, {"flagged": flagged, "rule": out_rule})


class ScorerTests(unittest.TestCase):
    def test_perfect_phoneme(self):
        rows = [mk(True, True), mk(False, False)] * 5
        self.assertEqual(f1_and_naming(rows, "phoneme"), 100)

    def test_detects_nothing_scores_zero(self):
        rows = [mk(True, False), mk(False, False)] * 5
        self.assertEqual(f1_and_naming(rows, "phoneme"), 0)

    def test_false_positives_lower_score(self):
        rows = [mk(True, True), mk(False, True)] * 5
        self.assertLess(f1_and_naming(rows, "phoneme"), 100)

    def test_tajweed_naming_matters_and_capped(self):
        good = [mk(True, True)] * 4
        bad = [mk(True, True, out_rule="x")] * 4
        self.assertEqual(f1_and_naming(good, "tajweed"), 100)
        self.assertEqual(f1_and_naming(bad, "tajweed"), 50)

    def test_demographic_zero_everywhere_is_zero(self):
        self.assertEqual(demographic_score({"a": 0, "b": 0}), 0)

    def test_demographic_gap_penalty(self):
        self.assertAlmostEqual(demographic_score({"a": 90, "b": 50}), 30)
        self.assertEqual(demographic_score({"a": 80, "b": 80}), 80)


if __name__ == "__main__":
    unittest.main()
