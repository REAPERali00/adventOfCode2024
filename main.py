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

    def is_valid(self, r: int, l: int, decreasing: bool):
        dif = r - l
        return (1 <= dif <= 3 and not decreasing) or (-3 <= dif <= -1 and decreasing)

    def is_valid_row(self, row: List[int]) -> bool:
        l, r, leng = 0, 1, len(row)
        decreasing = row[r] - row[l] < 0
        while r != leng - 1 and l != leng:
            if not self.is_valid(row[r], row[l], decreasing) and not self.is_valid(
                row[r + 1], row[l], decreasing
            ):
                return False
            l = r
            r += 1
        return True

    def analys_report_part2(self, data: List[List[int]]) -> int:
        tot_safe = 0
        for row in data:
            tot_safe += 1 if self.is_valid_row(row) else 0

        return tot_safe


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
        for line in input:
            data.append(list(map(int, re.findall(r"-?\d+", line))))
        print(f"the total data is: {len(data)}")
        print(
            f"the safe number of reports in part 1 is: {advent.analys_report_part1(data)}"
        )
        print(
            f"the safe number of reports in part 2 is: {advent.analys_report_part2(data)}"
        )


if __name__ == "__main__":
    day2()
