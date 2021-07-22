"""Handles running of Intcode programs."""


POSITION_MODE = 0
IMMEDIATE_MODE = 1

ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99


def run_program(program):
    running = True
    pointer = 0
    while(running):
        param_modes, opcode = get_opcode_and_param_modes(program[pointer])
        if opcode == ADD:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            add(parameters[0], parameters[1], parameters[2], program)
            pointer += instruction_size
        elif opcode == MULTIPLY:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            multiply(parameters[0], parameters[1], parameters[2], program)
            pointer += instruction_size
        elif opcode == INPUT:
            instruction_size = 2
            parameter_1 = set_parameter_with_default_mode(program[pointer + 1])
            input_op(parameter_1, program)
            pointer += instruction_size
        elif opcode == OUTPUT:
            instruction_size = 2
            parameter_1 = set_parameter_with_default_mode(program[pointer + 1])
            parameter_1[0] = param_modes[0]
            output(parameter_1, program)
            pointer += instruction_size
        elif opcode == JUMP_IF_TRUE:
            instruction_size = 3
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            pointer_unchanged, pointer = jump_if_true(parameters[0], parameters[1], program, pointer)
            if pointer_unchanged:
                pointer += instruction_size
        elif opcode == JUMP_IF_FALSE:
            instruction_size = 3
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            pointer_unchanged, pointer = jump_if_false(parameters[0], parameters[1], program, pointer)
            if pointer_unchanged:
                pointer += instruction_size
        elif opcode == LESS_THAN:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            less_than(parameters[0], parameters[1], parameters[2], program)
            pointer += instruction_size
        elif opcode == EQUALS:
            instruction_size = 4
            parameters = []
            parameters.append(set_parameter_with_default_mode(program[pointer + 1]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 2]))
            parameters.append(set_parameter_with_default_mode(program[pointer + 3]))
            param_index = 0
            for mode in param_modes[::-1]:
                parameters[param_index][0] = mode
                param_index += 1
            equals(parameters[0], parameters[1], parameters[2], program)
            pointer += instruction_size
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


def set_parameter_with_default_mode(parameter):
    return [POSITION_MODE, parameter]


def add(param_1, param_2, param_3, program):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]

    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    result = input_1 + input_2
    program[param_3[1]] = result


def multiply(param_1, param_2, param_3, program):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]

    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    result = input_1 * input_2
    program[param_3[1]] = result


def input_op(param_1, program):
    user_input = input('System ID -> ')
    program[param_1[1]] = int(user_input)


def output(param_1, program):
    if param_1[0] == POSITION_MODE:
        output = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        output = param_1[1]
    print(output)


def jump_if_true(param_1, param_2, program, pointer):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]
    
    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    return (False, input_2) if input_1 != 0 else (True, pointer)


def jump_if_false(param_1, param_2, program, pointer):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]
    
    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    return (False, input_2) if input_1 == 0 else (True, pointer)


def less_than(param_1, param_2, param_3, program):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]

    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    result = 1 if input_1 < input_2 else 0
    program[param_3[1]] = result


def equals(param_1, param_2, param_3, program):
    if param_1[0] == POSITION_MODE:
        input_1 = program[param_1[1]]
    elif param_1[0] == IMMEDIATE_MODE:
        input_1 = param_1[1]

    if param_2[0] == POSITION_MODE:
        input_2 = program[param_2[1]]
    elif param_2[0] == IMMEDIATE_MODE:
        input_2 = param_2[1]

    result = 1 if input_1 == input_2 else 0
    program[param_3[1]] = result
