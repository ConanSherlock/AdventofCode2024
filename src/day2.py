import os
from typing import List

INVALID_TYPE_EXCEPTION = "Invalid data type given"


class AoC2024Day2Exception(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Day2:
    _seperator: str = " "
    _max_diff: int = 3
    _min_diff: int = 1

    def __init__(self):
        self._safe: bool = False
        self._ascending:bool = False
        self._descending:bool = False
        self._levels_list: List[int] = []
        self._safe_reports: int = 0

    def reset(self):
        self._safe = False
        self._ascending = False
        self._descending = False
        self._levels_list = []
        self._safe_reports = 0

    def _parse_list(self, report:str):
        self._levels_list = list((int(x) for x in report.strip().split(self._seperator)))

    def _check_safety(self):

        for i, level in enumerate(self._levels_list[1:]):
            levels_diff = self._levels_list[i] - level
            if not self._min_diff <= abs(levels_diff) <= self._max_diff:
                # Unsafe Step
                self._safe = False
                return

            if levels_diff > 0 and not self._ascending:
                self._descending = True
            elif levels_diff < 0 and not self._descending:
                self._ascending = True
            else:
                # Unsafe swap in ascending/descending
                self._safe = False
                return 
        
        self._safe = True
        self._safe_reports += 1
        return


    def is_safe(self, report:str)-> bool:
        self._safe = False
        self._ascending = False
        self._descending = False

        self._parse_list(report)
        self._check_safety()

        return self._safe
    
    def get_safe_reports(self)-> int:
        return self._safe_reports


if __name__ == "__main__":

    day2_file_path = "test/input_data/day2_input.txt"
    day2 = Day2()

    with open(day2_file_path, "r") as input_file:
        input_data = input_file.readlines()

    for report in input_data:
        day2.is_safe(report)

    print("--- Day 2: Red-Nosed Reports ---")
    print(
        "Part A Total number of safe reports: %d" % day2.get_safe_reports()
    )

    # day2.calc_similarity_score()

    # print(
    #     "Part A Total similarity score between left list and right list: %d" % day2.get_total_similarity_score()
    # )