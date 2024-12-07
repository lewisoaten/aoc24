from .. import tools


def is_possible(answer: int, remaining_values: list[int]) -> bool:
    # One value left, either correct or wrong
    if len(remaining_values) == 1:
        if answer == remaining_values[0]:
            return True
        else:
            return False

    next_value = remaining_values[-1]

    test_divide = answer / next_value
    if test_divide.is_integer() and is_possible(int(test_divide), remaining_values[:-1]):
        return True

    test_subtract = answer - next_value
    if test_subtract > 0 and is_possible(test_subtract, remaining_values[:-1]):
        return True

    if str(answer).endswith(str(next_value)) and answer != next_value and is_possible(int(str(answer).removesuffix(str(next_value))), remaining_values[:-1]):
        return True

    return False


def process(input: list[list[str]]):
    sum_possible = 0
    for calibration in input:
        if is_possible(calibration[0], calibration[1]):
            sum_possible += calibration[0]
    return sum_possible


def parse_input(input: str) -> tuple[tuple[int, tuple[int]]]:
    return tools.str_to_lines(
        input,
        process_line=tools.key_value_split,
        process_line_kwargs={
            "separator": ":",
            "process_key": int,
            "process_value": tools.item_split,
            "process_value_kwargs": {
                "separator": " ",
                "process_items": int,
            },
        },
    )


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/07_1.txt")))
