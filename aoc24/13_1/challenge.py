from .. import tools


def calculate_button_presses(machine: tuple[dict[str, tuple[int]]]) -> tuple[int, int] | None:
    x_equation = (machine["Button A"][0], machine["Button B"][0], machine["Prize"][0])
    y_equation = (machine["Button A"][1], machine["Button B"][1], machine["Prize"][1])

    scaled_x_equation = (x_equation[0] * y_equation[0], x_equation[1] * y_equation[0], x_equation[2] * y_equation[0])
    scaled_y_equation = (y_equation[0] * x_equation[0], y_equation[1] * x_equation[0], y_equation[2] * x_equation[0])

    difference = (scaled_x_equation[1] - scaled_y_equation[1], scaled_x_equation[2] - scaled_y_equation[2])

    b_quotient, remainder = divmod(difference[1], difference[0])

    if remainder != 0:
        return None

    if x_equation[1] == 0:
        a_quotient, remainder = divmod((y_equation[2] - y_equation[1] * b_quotient), y_equation[0])
    else:
        a_quotient, remainder = divmod((x_equation[2] - x_equation[1] * b_quotient), x_equation[0])

    if remainder == 0 and a_quotient >= 0 and b_quotient >= 0:
        return a_quotient, b_quotient

    return None


def calculate_cost(button_presses: tuple[int, int]) -> int:
    if button_presses is None:
        return 0
    return 3 * button_presses[0] + button_presses[1]


def process(input: tuple[dict[str, tuple[int]]]) -> int:
    return sum(calculate_cost(calculate_button_presses(machine)) for machine in input)


def parse_input(input: str) -> tuple[dict[str, tuple[int]]]:
    def process_section(section: str) -> dict[str, tuple[int]]:
        machine = {}
        for line in section.splitlines():
            machine |= tools.key_value_split_dict(
                line, separator=": ", process_value=tools.item_split, process_value_kwargs={"separator": ", ", "process_items": lambda x: int(x[2:])}
            )
        return machine

    return tools.str_to_sections(input, process_sections=process_section)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/13_1.txt")))
