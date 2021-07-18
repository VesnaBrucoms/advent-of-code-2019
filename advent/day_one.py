import math


def calculate_fuel_for_fuel(fuel):
    running_total = 0
    calculated_fuel = calculate_fuel_for_mass(fuel)
    if calculated_fuel > 0:
        running_total += calculate_fuel_for_fuel(calculated_fuel)

    running_total += calculated_fuel
    return running_total


def calculate_fuel_for_mass(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel
