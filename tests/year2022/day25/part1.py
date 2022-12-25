#!/usr/bin/env python3

from src.year2022.day25.part1 import snafu_to_decimal, decimal_to_snafu

import unittest

#   Decimal          SNAFU
#         1              1
#         2              2
#         3             1=
#         4             1-
#         5             10
#         6             11
#         7             12
#         8             2=
#         9             2-
#        10             20
#        15            1=0
#        20            1-0     10  -1,  only, 0, 1, 2
#      2022         1=11-2
#     12345        1-0---0
# 314159265  1121-1110-1=0
#


class TestSnafuToDecimal(unittest.TestCase):
    CASES = [
        #   Decimal           SNAFU
         (1, '1'),
         (2, '2'),
         (3, '1='),
         (4, '1-'),
         (5, '10'),
         (6, '11'),
         (7, '12'),
         (8, '2='),
         (9, '2-'),
         (10, '20'),
         (15, '1=0'),
         (20, '1-0'),  # 10  -1,  only, 0, 1, 2
         (2022, '1=11-2'),
        #  3125   625    125  25  5   1
        #          3      1    0  4   2
        #       1875    2000    20   2
        #    1    =       1    1 -    2
        (12345, '1-0---0'),  #  to fix
        (314159265, '1121-1110-1=0'),  # to fix
        #                        2   3
        #  13
        #  25  -10   15,  -2
    ]

    # 2=
    # 1 3
    # 5 + 3

    def test_snafu_to_decimal(self):
        for case in self.CASES:
            self.assertEqual(case[0], snafu_to_decimal(case[1]))

    def test_decimal_to_snafu(self):
        for case in self.CASES:
            self.assertEqual(case[1], decimal_to_snafu(case[0]))
