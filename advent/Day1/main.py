from typing import List
from collections import Counter


class Advent:
    def __init__(self) -> None: ...

    def distance_calc(self, list1: List[int], list2: List[int]) -> int:
        total_distance: int = 0
        list1.sort()
        list2.sort()
        for i in range(len(list1)):
            total_distance += abs(list1[i] - list2[i])
        return total_distance

    def distance_calc_part2(self, list1: List[int], list2: List[int]) -> int:
        total_distance: int = 0
        count_list = Counter(list2)
        for val in list1:
            if val in count_list:
                total_distance += val * count_list[val]
        return total_distance


if __name__ == "__main__":
    advent = Advent()
    list1: List[int] = []
    list2: List[int] = []

    with open("input.txt", "r") as input:
        for line in input:
            (part1, part2) = line.strip().split()
            list1.append(int(part1))
            list2.append(int(part2))
    ans = advent.distance_calc(list1, list2)
    ans = advent.distance_calc_part2(list1, list2)
    print(f"the len of l1: {len(list1)}")
    print(f"the len of l2: {len(list2)}")
    print(f"the total distance is {ans}")
