"""Handles running of Intcode programs."""
from .utils import get_input_parameter_by_mode, get_output_parameter_by_mode
from .utils import set_parameter_with_default_mode


ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJ = 9
HALT = 99


POINTER = 0
RELATIVE_BASE = 0


def run_program(program):
    running = True
    global POINTER
    while(running):
        param_modes, opcode = get_opcode_and_param_modes(program[POINTER])
        if opcode == ADD:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            add(parameters[0], parameters[1], parameters[2], program)
            POINTER += instruction_size
        elif opcode == MULTIPLY:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            multiply(parameters[0], parameters[1], parameters[2], program)
            POINTER += instruction_size
        elif opcode == INPUT:
            instruction_size = 2
            parameter_1 = set_parameter_with_default_mode(program[POINTER + 1])
            parameter_1[0] = param_modes[0]
            input_op(parameter_1, program)
            POINTER += instruction_size
        elif opcode == OUTPUT:
            instruction_size = 2
            parameter_1 = set_parameter_with_default_mode(program[POINTER + 1])
            parameter_1[0] = param_modes[0]
            output(parameter_1, program)
            POINTER += instruction_size
        elif opcode == JUMP_IF_TRUE:
            instruction_size = 3
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            pointer_unchanged, POINTER = jump_if_true(parameters[0], parameters[1], program, POINTER)
            if pointer_unchanged:
                POINTER += instruction_size
        elif opcode == JUMP_IF_FALSE:
            instruction_size = 3
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            pointer_unchanged, POINTER = jump_if_false(parameters[0], parameters[1], program, POINTER)
            if pointer_unchanged:
                POINTER += instruction_size
        elif opcode == LESS_THAN:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            less_than(parameters[0], parameters[1], parameters[2], program)
            POINTER += instruction_size
        elif opcode == EQUALS:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 2]))
            parameters.append(set_parameter_with_default_mode(program[POINTER + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            equals(parameters[0], parameters[1], parameters[2], program)
            POINTER += instruction_size
        elif opcode == ADJ:
            instruction_size = 2
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[POINTER + 1]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            adjust_relative_base(parameters[0], program)
            POINTER += instruction_size
        elif opcode == HALT:
            running = False
        else:
            print(f'INVALID OPCODE {opcode}')
            running = False


def get_opcode_and_param_modes(opcode_and_param_modes):
    opcode = 99
    param_modes = [0]
    string_form = str(opcode_and_param_modes)
    if len(string_form) <= 2:
        opcode = opcode_and_param_modes
    else:
        opcode = string_form[-2:]
        str_param_modes = list(string_form[0:-2])
        param_modes = []
        for mode in str_param_modes:
            param_modes.append(int(mode))
    return (param_modes, int(opcode))


def add(param_1, param_2, param_3, program):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)
    output = get_output_parameter_by_mode(param_3, program, RELATIVE_BASE)

    result = input_1 + input_2
    program[output] = result


def multiply(param_1, param_2, param_3, program):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)
    output = get_output_parameter_by_mode(param_3, program, RELATIVE_BASE)

    result = input_1 * input_2
    program[output] = result


def input_op(param_1, program):
    user_input = input('-> ')
    global RELATIVE_BASE
    address = get_output_parameter_by_mode(param_1, program, RELATIVE_BASE)
    program[address] = int(user_input)


def output(param_1, program):
    global RELATIVE_BASE
    output = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    print(output)


def jump_if_true(param_1, param_2, program, pointer):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)

    return (False, input_2) if input_1 != 0 else (True, pointer)


def jump_if_false(param_1, param_2, program, pointer):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)

    return (False, input_2) if input_1 == 0 else (True, pointer)


def less_than(param_1, param_2, param_3, program):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)
    output = get_output_parameter_by_mode(param_3, program, RELATIVE_BASE)

    result = 1 if input_1 < input_2 else 0
    program[output] = result


def equals(param_1, param_2, param_3, program):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)
    input_2 = get_input_parameter_by_mode(param_2, program, RELATIVE_BASE)
    output = get_output_parameter_by_mode(param_3, program, RELATIVE_BASE)

    result = 1 if input_1 == input_2 else 0
    program[output] = result


def adjust_relative_base(param_1, program):
    global RELATIVE_BASE
    input_1 = get_input_parameter_by_mode(param_1, program, RELATIVE_BASE)

    RELATIVE_BASE += input_1
