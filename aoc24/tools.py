from collections.abc import Callable


# Read from file
def read_to_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read().strip()


def str_to_lines(string: str, process_line: Callable = str, process_line_kwargs: dict = {}) -> tuple:
    return tuple(process_line(line, **process_line_kwargs) for line in string.splitlines())


def key_value_split(
    line: str, separator: str = "|", process_key: Callable = str, process_key_kwargs: dict = {}, process_value: Callable = str, process_value_kwargs: dict = {}
) -> tuple:
    key, values = line.split(separator, 1)
    return process_key(key, **process_key_kwargs), process_value(values, **process_value_kwargs)


def item_split(
    line: str,
    separator: str = "|",
    process_items: Callable = str,
    process_items_kwargs: dict = {},
) -> tuple:
    return tuple(process_items(value, **process_items_kwargs) for value in line.split(separator) if value is not None and value != "")


def read_to_two_sections(file_path: str) -> str:
    return str_to_two_sections(read_to_string(file_path))


def str_to_two_sections(string: str) -> list[str]:
    return string.split("\n\n")


# 2d array stuff
def read_to_int2d(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        return [[int(i) for i in line.split()] for line in file.read().splitlines()]


def str_to_char2d(input: str) -> tuple[tuple[str]]:
    return tuple(list(line) for line in input.splitlines())


def read_to_char2d(file_path: str) -> list[list[str]]:
    with open(file_path) as file:
        return str_to_char2d(file.read().strip())


def rotate_char2d(input: list[list[str]]) -> list[list[str]]:
    return list(zip(*input))[::-1]


def copy_char2d_sub(input: list[list[str]], x: int, y: int, width: int, height: int) -> list[list[str]]:
    return [line[x : x + width] for line in input[y : y + height]]  # noqa: E203
