from typing import List
import re
from collections import Counter, defaultdict


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

    def find_operations_part1(self, data) -> int:
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, data)
        tot = sum(int(num1) * int(num2) for (num1, num2) in matches)
        return tot

    def find_operations_part2(self, data):
        data = "do()" + data + "don't()"
        # look for do() and negative look ahead for dont', match any other char between these (the dot)
        # the dot all is to include special characters such as \n in .
        get_between = re.findall(r"do\(\)(?:(?!don't\(\)).)*", data, re.DOTALL)
        return sum(self.find_operations_part1(match) for match in get_between)

    def search_word_part1(self, data: List[str]) -> int:
        tot = 0
        keyword = "XMAS"
        for i in range(len(data)):
            for j in range(len(data[0])):
                hor = data[i][j : j + 4]
                vert = "".join([row[j] for row in data[i : i + 4]])
                diag = "".join(
                    data[i + k][j + k]
                    for k in range(4)
                    if j + k < len(data[0]) and i + k < len(data)
                )
                diag_bac = "".join(
                    data[i + k][j - k]
                    for k in range(4)
                    if j - k >= 0 and i + k < len(data)
                )
                strings = [hor, vert, diag, diag_bac]
                tot += sum(map(lambda s: s == keyword or s == keyword[::-1], strings))

        return tot

    def search_word_part2(self, data) -> int:
        tot = 0
        key = "MAS"
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == "A":
                    left = "".join(
                        data[i - 1 + k][j - 1 + k]
                        for k in range(3)
                        if 0 <= j - 1 + k < len(data[0]) and 0 <= i - 1 + k < len(data)
                    )
                    right = "".join(
                        data[i - 1 + k][j + 1 - k]
                        for k in range(3)
                        if len(data[0]) > j + 1 - k >= 0 and 0 <= i - 1 + k < len(data)
                    )
                    strings = [left, right]
                    tot += 1 if all(s == key or s == key[::-1] for s in strings) else 0

        return tot

    def page_order_part1(self, rules, pages) -> int:
        tot = 0
        mid = 0

        for page in pages:
            mid = page[len(page) // 2]
            for i, num in enumerate(page):
                if num in rules:
                    exists = set(page[:i]) & set(rules[num])
                    if exists:
                        mid = 0
                        break
            tot += mid

        return tot


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


def day3():
    advent = Advent()
    data = []

    with open("input.txt", "r") as input:
        data = input.read()
        ans_part1 = advent.find_operations_part1(data)
        ans_part2 = advent.find_operations_part2(data)
        print(f"the part 1 answer is : {ans_part1}")
        print(f"the part 2 answer is : {ans_part2}")


def day4():
    advent = Advent()
    data = []

    with open("input.txt", "r") as input:
        for line in input:
            data.append(line)
        ans = advent.search_word_part1(data)
        print(f"Part1 answer is {ans}")
        ans = advent.search_word_part2(data)
        print(f"Part2 answer is {ans}")


def day5():
    advent = Advent()
    read_mode_rule = True
    pages = []
    rules = defaultdict(list)

    with open("input.txt", "r") as input:
        for line in input:
            line = line.strip()  # Remove leading/trailing whitespace, including newline
            if line == "":
                read_mode_rule = False
                continue

            if read_mode_rule:
                left, right = map(int, line.split("|"))
                rules[left].append(right)
            else:
                pages.append(list(map(int, line.split(","))))  # print(rules)
        ans = advent.page_order_part1(rules, pages)
        print(f"Part 1 answer is {ans}")


if __name__ == "__main__":
    day5()
