#!/usr/bin/env python3

from src.year2019.day13.part2 import print_tiles

import unittest


class TestBlocks(unittest.TestCase):
    def test_process_input(self):
        cases = [
            # 3 = paddle, 4 = ball
            ([1, 2, 3, 6, 5, 4], 1)
        ]

        for case in cases:
            self.assertEqual(case[1], print_tiles(case[0]))
