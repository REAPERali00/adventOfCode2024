from typing import List
import re
from collections import Counter


class Advent:
    def __init__(self) -> None: ...

    def distance_calc(self, list1: List[int], list2: List[int]) -> int:
        list1.sort()
        list2.sort()
        # total_distance: int = 0
        # for i in range(len(list1)):
        #     total_distance += abs(list1[i] - list2[i])
        # return total_distance
        return sum(abs(l - r) for l, r in zip(list1, list2))

    def distance_calc_part2(self, list1: List[int], list2: List[int]) -> int:
        total_distance: int = 0
        count_list = Counter(list2)
        for val in list1:
            total_distance += val * count_list[val]
        return total_distance

    def analys_report_part1(self, data: List[List[int]]) -> int:
        tot_safe = 0
        for row in data:
            difs = []
            for i in range(len(row) - 1):
                difs.append(row[i] - row[i + 1])
            tot_safe += (
                1
                if all(1 <= x <= 3 for x in difs) or all(-3 <= x <= -1 for x in difs)
                else 0
            )
        return tot_safe

    def is_safe(self, data: List[int]):
        diffs = [data[i] - data[i - 1] for i in range(1, len(data))]
        check_dec = (
            diffs[0] > 0
        )  # check the first, and see if the rest are all the same
        return all(1 <= abs(x) <= 3 for x in diffs) and all(
            (d > 0) == check_dec for d in diffs[1:]
        )

    def analys_report_part2(self, data):
        # check if original is safe, if not check if removing any index will make the solution safe
        return self.is_safe(data) or any(
            self.is_safe(data[:i] + data[i + 1 :]) for i in range(len(data))
        )


def day1():
    advent = Advent()
    list1: List[int] = []
    list2: List[int] = []

    with open("input.txt", "r") as input:
        for line in input:
            # print(nums(line))
            (part1, part2) = line.strip().split()
            list1.append(int(part1))
            list2.append(int(part2))
    ans = advent.distance_calc(list1, list2)
    ans = advent.distance_calc_part2(list1, list2)
    print(f"the len of l1: {len(list1)}")
    print(f"the len of l2: {len(list2)}")
    print(f"the total distance is {ans}")


def day2():
    advent = Advent()
    data = []

    with open("input.txt", "r") as input:
        # map will apply the int function to all strings
        data = [list(map(int, line.split())) for line in input]
        print(f"Part 1 soution: {sum(advent.is_safe(r) for r in data)}")
        print(f"Part 2 soution: {sum(advent.analys_report_part2(r) for r in data)}")


if __name__ == "__main__":
    day2()
