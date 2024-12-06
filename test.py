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

    def test_day2_part1(self):
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertEqual(self.advent.analys_report_part1(data), 2)

    def test_day2_part2(self):
        data = [
            [7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9],
        ]
        self.assertEqual(sum(self.advent.analys_report_part2(r) for r in data), 4)

    def test_day3_part1(self):
        data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        self.assertEqual(self.advent.find_operations_part1(data), 161)

    def test_day3_part2(self):
        data = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        self.assertEqual(self.advent.find_operations_part2(data), 48)

    def test_day4_part1(self):
        data = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(self.advent.search_word_part1(data), 18)

    def test_day4_part2(self):
        data = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        self.assertEqual(self.advent.search_word_part2(data), 9)

    def test_day5_part1(self):
        rules = {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        }

        pages = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]
        self.assertEqual(self.advent.page_order_part1(rules, pages), 143)

    def test_day5_part2(self):
        rules = {
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        }

        pages = [
            [75, 47, 61, 53, 29],
            [97, 61, 53, 29, 13],
            [75, 29, 13],
            [75, 97, 47, 61, 53],
            [61, 13, 29],
            [97, 13, 75, 29, 47],
        ]
        self.assertEqual(self.advent.page_order_part2(rules, pages), 143)


if __name__ == "__main__":
    unittest.main()
