from parameterized import parameterized
import unittest

from advent.day_one import calculate_fuel_for_fuel
from advent.day_one import calculate_fuel_for_mass


class TestEntry(unittest.TestCase):

    @parameterized.expand([
        ("simple_one", 12, 2),
        ("simple_two", 14, 2),
        ("typical_one", 1969, 654),
        ("typical_two", 100756, 33583),
        ("negative", 2, 0)
    ])
    def test_calculate_fuel_for_mass(self, name, given_mass, expected_fuel):
        fuel = calculate_fuel_for_mass(given_mass)

        self.assertEqual(expected_fuel, fuel)

    @parameterized.expand([
        ("small", 654, 312),
        ("large", 33583, 16763),
    ])
    def test_calculate_fuel_for_fuel(self, name, given_mass, expected_fuel):
        fuel = calculate_fuel_for_fuel(given_mass)

        self.assertEqual(expected_fuel, fuel)
