import unittest

from advent.entry import _calculate_fuel_for_fuel
from advent.entry import _calculate_fuel_for_mass


class TestEntry(unittest.TestCase):

    def test_calculate_fuel_for_mass_scenario_one(self):
        example_mass = 12

        fuel = _calculate_fuel_for_mass(example_mass)

        expected_fuel = 2
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_mass_scenario_two(self):
        example_mass = 14

        fuel = _calculate_fuel_for_mass(example_mass)

        expected_fuel = 2
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_mass_scenario_three(self):
        example_mass = 1969

        fuel = _calculate_fuel_for_mass(example_mass)

        expected_fuel = 654
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_mass_scenario_four(self):
        example_mass = 100756

        fuel = _calculate_fuel_for_mass(example_mass)

        expected_fuel = 33583
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_mass_scenario_five(self):
        example_mass = 2

        fuel = _calculate_fuel_for_mass(example_mass)

        expected_fuel = 0
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_fuel_scenario_one(self):
        example_mass = 654

        fuel = _calculate_fuel_for_fuel(example_mass)

        expected_fuel = 312
        self.assertEqual(expected_fuel, fuel)

    def test_calculate_fuel_for_fuel_scenario_two(self):
        example_mass = 33583

        fuel = _calculate_fuel_for_fuel(example_mass)

        expected_fuel = 16763
        self.assertEqual(expected_fuel, fuel)
