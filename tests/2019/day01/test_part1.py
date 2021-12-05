#!/usr/bin/env python3

import

import part1

from


import unittest


class TestFuelRequired(unittest.TestCase):
    def test_fuel_required(self):
        cases = [
            (['12'], 2),
            (['14'], 2),
            (['1969'], 654),
            (['100756'], 33583)
        ]

        for case in cases:
            self.assertEqual(case[1], part1.fuel_required(case[0]))
