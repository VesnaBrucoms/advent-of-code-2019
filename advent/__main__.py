from .day_one import calculate_fuel_for_mass, calculate_fuel_for_fuel
from .intcode.core import run_program


def day_1():
    masses = _read_puzzle_file('day_1.txt')
    fuel_total = 0
    for mass in masses:
        calculated_fuel = calculate_fuel_for_mass(mass)
        calculated_fuel += calculate_fuel_for_fuel(calculated_fuel)
        fuel_total += calculated_fuel
    print(f"Day 1: {fuel_total}")


def day_2():
    program = _read_puzzle_program_file('day_2.txt')
    program = _convert_program_int(program)
    print(program)
    run_program(program)
    print(program)


def _read_puzzle_file(filename):
    inputs = []
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as puzzle_input:
        for line in puzzle_input:
            inputs.append(int(line))
    return inputs


def _read_puzzle_program_file(filename):
    program = ""
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as program_file:
        program = program_file.read()
    return program.split(',')


def _convert_program_int(program):
    converted = []
    for value in program:
        converted.append(int(value))
    return converted


if __name__ == '__main__':
    day_1()
    day_2()
