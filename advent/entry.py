import math


def run():
    masses = _read_file('day_1.txt')
    fuel_total = 0
    for mass in masses:
        calculated_fuel = _calculate_fuel_for_mass(mass)
        calculated_fuel += _calculate_fuel_for_fuel(calculated_fuel)
        fuel_total += calculated_fuel
    print(fuel_total)


def _read_file(filename):
    inputs = []
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as puzzle_input:
        for line in puzzle_input:
            inputs.append(int(line))
    return inputs


def _calculate_fuel_for_fuel(fuel):
    running_total = 0
    calculated_fuel = _calculate_fuel_for_mass(fuel)
    if calculated_fuel > 0:
        running_total += _calculate_fuel_for_fuel(calculated_fuel)

    running_total += calculated_fuel
    return running_total


def _calculate_fuel_for_mass(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel


if __name__ == '__main__':
    run()
