import importlib
import unittest
import src.day1


class AoC2024Day1Test(unittest.TestCase):
    def setUp(self):
        self.day1 = None

    def test_calc_total_distance_part_a(self):
        self.day1 = day1.Day1()

        input_strings = ["3   4\n", "4   3\n", "2   5\n", "1   3\n", "3   9\n", "3   3\n"]

        expected_left_list = [3, 4, 2, 1, 3, 3]
        expected_right_list = [4, 3, 5, 3, 9, 3]
        expected_distances = [2, 1, 0, 1, 2, 5]
        expected_similarity_scores = [9, 4, 0, 0, 9, 9]

        expected_total_distance = 11
        expected_total_similarity_score = 31

        expected_init_ints = 0
        expected_init_list = []

        self.assertEqual(expected_init_ints, self.day1.get_total_distance())
        self.assertEqual(expected_init_ints, self.day1.get_total_similarity_score())
        self.assertEqual(expected_init_list, self.day1.get_distances())
        self.assertEqual(expected_init_list, self.day1.get_similarity_scores())
        self.assertEqual(expected_init_list, self.day1.get_left_list())
        self.assertEqual(expected_init_list, self.day1.get_right_list())

        self.day1.generate_lists(input_strings)

        self.assertListEqual(expected_left_list, self.day1.get_left_list(), "Left list is not correct")
        self.assertListEqual(expected_right_list, self.day1.get_right_list(), "Right list is not correct")

        self.day1.calc_total_distance()
        self.assertListEqual(expected_distances, self.day1.get_distances(), "Expected distances are not correct")
        self.assertEqual(expected_total_distance, self.day1.get_total_distance())

        self.day1.calc_similarity_score()
        self.assertListEqual(expected_similarity_scores, self.day1.get_similarity_scores(),
                             "Expected similarity scores are not correct")
        self.assertEqual(expected_total_similarity_score, self.day1.get_total_similarity_score())

        self.day1.reset()
        self.assertEqual(expected_init_ints, self.day1.get_total_distance())
        self.assertEqual(expected_init_ints, self.day1.get_total_similarity_score())
        self.assertEqual(expected_init_list, self.day1.get_distances())
        self.assertEqual(expected_init_list, self.day1.get_similarity_scores())
        self.assertEqual(expected_init_list, self.day1.get_left_list())
        self.assertEqual(expected_init_list, self.day1.get_right_list())