from typing import List

INVALID_TYPE_EXCEPTION = "Invalid data type given"


class AoC2024Day1Exception(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Day1:
    seperator: str = "   "

    def __init__(self):
        self._total_distance: int = 0
        self._total_similarity_score: int = 0
        self._similarity_scores: List[int] = []
        self._distances: List[int] = []
        self._left_list: List[int] = []
        self._right_list: List[int] = []

    def reset(self):
        self._total_distance = 0
        self._total_similarity_score = 0
        self._similarity_scores: List[int] = []
        self._distances = []
        self._left_list = []
        self._right_list = []

    def get_total_distance(self) -> int:
        return self._total_distance

    def get_total_similarity_score(self) -> int:
        return self._total_similarity_score

    def get_distances(self) -> List[int]:
        return self._distances

    def get_similarity_scores(self) -> List[int]:
        return self._similarity_scores

    def get_left_list(self) -> List[int]:
        return self._left_list

    def get_right_list(self) -> List[int]:
        return self._right_list

    def generate_lists(self, input_list: List[str]):
        for line in input_list:
            split_line = line.strip().split(self.seperator)

            self._left_list.append(int(split_line[0]))
            self._right_list.append(int(split_line[-1]))

    def calc_total_distance(self):
        left_list = self._left_list.copy()
        right_list = self._right_list.copy()
        left_list.sort()
        right_list.sort()

        for left, right in zip(left_list, right_list):
            self._distances.append(abs(right - left))
            self._total_distance += self._distances[-1]

    def calc_similarity_score(self):
        for left in self._left_list:
            self._similarity_scores.append(left * self._right_list.count(left))
            self._total_similarity_score += self._similarity_scores[-1]


if __name__ == "__main__":

    day1_file_path = "test/input_data/day1_input.txt"

    with open(day1_file_path, "r") as input_file:
        input_data = input_file.readlines()

    day1 = Day1()

    day1.generate_lists(input_data)
    day1.calc_total_distance()

    print("--- Day 1: Historian Hysteria ---")
    print(
        "Part A Total distance between left list and right list: %d" % day1.get_total_distance()
    )

    day1.calc_similarity_score()

    print(
        "Part B Total similarity score between left list and right list: %d" % day1.get_total_similarity_score()
    )