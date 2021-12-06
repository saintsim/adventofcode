#!/usr/bin/env python3

from src.year2019.day04.part1 import password_cracker

import unittest


class TestPassword(unittest.TestCase):
    def test_process_input(self):
        cases = [
            (111111, 111111, 1),
            (223450, 223450, 0),
            (123789, 123789, 0)
        ]

        for case in cases:
            self.assertEqual(case[2], password_cracker(case[0], case[1]))
