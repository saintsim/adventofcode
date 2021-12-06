#!/usr/bin/env python3

from src.year2019.day01.part2 import fuel_required

import unittest


class TestFuelRequired(unittest.TestCase):
    def test_fuel_required(self):
        cases = [
            (['14'], 2),
            (['1969'], 966),
            (['100756'], 50346)
        ]

        for case in cases:
            self.assertEqual(case[1], fuel_required(case[0]))
