import unittest
from src.day2 import Day2


class AoC2024Day2Test(unittest.TestCase):
    def setUp(self):
        self.day2 = None

    def test_is_safe(self):
        self.day2 = Day2()

        input_strings = ["7 6 4 2 1\n", "1 2 7 8 9\n", "9 7 6 2 1\n", "1 3 2 4 5\n", "8 6 4 4 1\n", "1 3 6 7 9\n"]

        expected_safe = [True, False, False, False, False, True]
        actual_safe = []

        for report in input_strings:
            actual_safe.append(self.day2.is_safe(report))

        self.assertListEqual(expected_safe, actual_safe, "Safe list is not correct")

    def test_is_safe_problem_dampener(self):
        self.day2 = Day2()

        input_strings = ["7 6 4 2 1\n", "1 2 7 8 9\n", "9 7 6 2 1\n", "1 3 2 4 5\n", "8 6 4 4 1\n", "1 3 6 7 9\n"]

        expected_safe = [True, False, False, True, True, True]
        actual_safe = []

        for report in input_strings:
            actual_safe.append(self.day2.is_safe(report, True))

        self.assertListEqual(expected_safe, actual_safe, "Safe list is not correct")
    