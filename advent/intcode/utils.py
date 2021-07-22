POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


def get_parameter_by_mode(parameter, program, relative_base, allow_position=True):
    param_value = 0
    if parameter[0] == POSITION_MODE and allow_position:
        param_value = program[parameter[1]]
    elif parameter[0] == IMMEDIATE_MODE:
        param_value = parameter[1]
    elif parameter[0] == RELATIVE_MODE:
        param_value = program[relative_base + parameter[1]]
    return param_value


def set_parameter_with_default_mode(parameter):
    return [POSITION_MODE, parameter]
