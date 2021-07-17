import math


def run():
    masses = [12, 14]
    for mass in masses:
        fuel = _calculate_fuel(mass)
        print(f'For {mass} mass, {fuel} fuel is required')


def _calculate_fuel(mass):
    return math.floor(mass / 3) - 2
