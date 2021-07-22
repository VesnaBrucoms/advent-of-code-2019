from .day_one import calculate_fuel_for_mass, calculate_fuel_for_fuel
from .intcode.core import run_program


def day_1():
    masses = _read_puzzle_file('day_1.txt')
    fuel_total = 0
    for mass in masses:
        calculated_fuel = calculate_fuel_for_mass(mass)
        calculated_fuel += calculate_fuel_for_fuel(calculated_fuel)
        fuel_total += calculated_fuel
    print(f'Day 1: {fuel_total} units of fuel required')


def day_2():
    program = _read_puzzle_program_file('day_2.txt')
    program = _convert_program_int(program)
    _adjust_program_state(program, 12, 2)
    run_program(program)
    result = program[0]
    print(f'Day 2: Program result is {result}')


def day_2_part_2(noun, verb):
    program = _read_puzzle_program_file('day_2.txt')
    program = _convert_program_int(program)
    _adjust_program_state(program, noun, verb)
    run_program(program)
    return program[0]


def day_5():
    program = _read_puzzle_program_file('day_5.txt')
    program = _convert_program_int(program)
    # _adjust_program_state(program, 12, 2)
    run_program(program)
    # result = program[0]
    print(f'Day 5: Program result is {result}')


def day_9():
    program = _read_puzzle_program_file('day_9.txt')
    program = _convert_program_int(program)
    program = _allocate_extra_memory(program, 512)
    run_program(program)


def _read_puzzle_file(filename):
    inputs = []
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as puzzle_input:
        for line in puzzle_input:
            inputs.append(int(line))
    return inputs


def _read_puzzle_program_file(filename):
    program = ''
    with open(f'./tests/puzzle_inputs/{filename}', 'r') as program_file:
        program = program_file.read()
    return program.split(',')


def _convert_program_int(program):
    converted = []
    for value in program:
        converted.append(int(value))
    converted.extend([0] * 256)
    return converted


def _allocate_extra_memory(program, amount):
    program.extend([0] * amount)
    return program


def _adjust_program_state(program, noun, verb):
    program[1] = noun
    program[2] = verb


if __name__ == '__main__':
    # day_1()
    # day_2()
    # for noun in range(0, 100):
    #     for verb in range(0, 100):
    #         result = day_2_part_2(noun, verb)
    #         if result == 19690720:
    #             print(f'Day 2 part 2: Program result is {result}')
    #             print(f'Noun of {noun}, verb of {verb}')
    #             noun_and_verb = (100 * noun) + verb
    #             print(f'Final result {noun_and_verb}')
    day_9()
