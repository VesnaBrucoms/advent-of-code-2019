from .day_one import calculate_fuel_for_mass, calculate_fuel_for_fuel


def day_1():
    masses = _read_puzzle_file('day_1.txt')
    fuel_total = 0
    for mass in masses:
        calculated_fuel = calculate_fuel_for_mass(mass)
        calculated_fuel += calculate_fuel_for_fuel(calculated_fuel)
        fuel_total += calculated_fuel
    print(f"Day 1: {fuel_total}")


def day_2():
    pass


def _read_puzzle_file(filename):
    inputs = []
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as puzzle_input:
        for line in puzzle_input:
            inputs.append(int(line))
    return inputs


if __name__ == '__main__':
    day_1()
    day_2()
