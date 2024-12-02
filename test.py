import unittest
from main import Advent


class TestAdvent(unittest.TestCase):
    def setUp(self) -> None:
        self.advent = Advent()

    def test_day1_part1(self):
        l1 = [3, 4, 2, 1, 3, 3]
        l2 = [4, 3, 5, 3, 9, 3]
        ans = self.advent.distance_calc(l1, l2)
        self.assertEqual(ans, 11)

    def test_day1_part2(self):
        l1 = [3, 4, 2, 1, 3, 3]
        l2 = [4, 3, 5, 3, 9, 3]
        ans = self.advent.distance_calc_part2(l1, l2)
        self.assertEqual(ans, 31)

    def test_analyse_part1(self):
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertEqual(self.advent.analys_report_part1(data), 2)

    def test_analyse_part2(self):
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertEqual(self.advent.analys_report_part2(data), 4)


if __name__ == "__main__":
    unittest.main()
