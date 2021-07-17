import unittest

from advent.entry import _calculate_fuel


class TestEntry(unittest.TestCase):

    def test_scenario_one(self):
        example_mass = 12

        fuel = _calculate_fuel(example_mass)

        expected_fuel = 2
        self.assertEqual(expected_fuel, fuel)

    def test_scenario_two(self):
        example_mass = 14

        fuel = _calculate_fuel(example_mass)

        expected_fuel = 2
        self.assertEqual(expected_fuel, fuel)
