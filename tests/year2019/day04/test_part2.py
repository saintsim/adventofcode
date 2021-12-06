#!/usr/bin/env python3

from src.year2019.day04.part2 import password_cracker

import unittest


class TestPassword(unittest.TestCase):
    def test_process_input(self):
        cases = [
            (112233, 112233, 1),
            (123444, 123444, 0),
            (111122, 111122, 1)
        ]

        for case in cases:
            self.assertEqual(case[2], password_cracker(case[0], case[1]))
