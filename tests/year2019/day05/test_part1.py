#!/usr/bin/env python3

from src.year2019.day05.part1 import diagnostic_program

import unittest


class TestDiagnosticProgram(unittest.TestCase):
    def test_process_input(self):
        cases = [
            ([1002, 4, 3, 4, 33], 1002)
        ]

        for case in cases:
            self.assertEqual(case[1], diagnostic_program(case[0]))
