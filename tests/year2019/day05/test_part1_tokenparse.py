#!/usr/bin/env python3

from src.year2019.day05.part1 import token_parse

import unittest


class TestTokenParse(unittest.TestCase):
    def test_token_parse(self):
        cases = [
            (2, (0, 0, 0, 2)),
            (1002, (0, 1, 0, 2)),
            (101, (0, 0, 1, 1)),
            (99, (0, 0, 0, 99)),
        ]

        for case in cases:
            self.assertEqual(case[1], token_parse(case[0]))
