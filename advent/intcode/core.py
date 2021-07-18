"""Handles running of Intcode programs."""


OPERATION_SIZE = 4


def run_program(program):
    running = True
    position = 0
    while(running):
        operation = program[position:position + OPERATION_SIZE]
        opcode = operation[0]
        if opcode == 1:
            add(operation[1], operation[2], operation[3], program)
        elif opcode == 2:
            multiply(operation[1], operation[2], operation[3], program)
        elif opcode == 99:
            running = False
        else:
            running = False
        position += OPERATION_SIZE


def add(input_1_pos, input_2_pos, output_pos, program):
    input_1 = program[input_1_pos]
    input_2 = program[input_2_pos]
    result = input_1 + input_2
    program[output_pos] = result


def multiply(input_1_pos, input_2_pos, output_pos, program):
    input_1 = program[input_1_pos]
    input_2 = program[input_2_pos]
    result = input_1 * input_2
    program[output_pos] = result
