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

    def test_scenario_three(self):
        example_mass = 1969

        fuel = _calculate_fuel(example_mass)

        expected_fuel = 654
        self.assertEqual(expected_fuel, fuel)

    def test_scenario_four(self):
        example_mass = 100756

        fuel = _calculate_fuel(example_mass)

        expected_fuel = 33583
        self.assertEqual(expected_fuel, fuel)
