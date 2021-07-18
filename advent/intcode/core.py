"""Handles running of Intcode programs."""


INSTRUCTION_SIZE = 4


def run_program(program):
    running = True
    instruction_pointer = 0
    while(running):
        instruction = program[instruction_pointer:instruction_pointer + INSTRUCTION_SIZE]
        opcode = instruction[0]
        parameter_1 = instruction[1]
        parameter_2 = instruction[2]
        parameter_3 = instruction[3]
        if opcode == 1:
            add(parameter_1, parameter_2, parameter_3, program)
        elif opcode == 2:
            multiply(parameter_1, parameter_2, parameter_3, program)
        elif opcode == 99:
            running = False
        else:
            running = False
        instruction_pointer += INSTRUCTION_SIZE


def add(input_1_addr, input_2_addr, output_addr, program):
    input_1 = program[input_1_addr]
    input_2 = program[input_2_addr]
    result = input_1 + input_2
    program[output_addr] = result


def multiply(input_1_pos, input_2_pos, output_pos, program):
    input_1 = program[input_1_pos]
    input_2 = program[input_2_pos]
    result = input_1 * input_2
    program[output_pos] = result
