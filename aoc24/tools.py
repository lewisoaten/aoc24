# Read from file
def read_to_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read().strip()


def read_to_two_sections(file_path: str) -> str:
    return str_to_two_sections(read_to_string(file_path))


def str_to_two_sections(string: str) -> list[str]:
    return string.split("\n\n")


# 2d array stuff
def read_to_int2d(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        return [[int(i) for i in line.split()] for line in file.read().splitlines()]


def str_to_char2d(input: str) -> list[list[str]]:
    return [list(line) for line in input.splitlines()]


def read_to_char2d(file_path: str) -> list[list[str]]:
    with open(file_path) as file:
        return str_to_char2d(file.read().strip())


def rotate_char2d(input: list[list[str]]) -> list[list[str]]:
    return list(zip(*input))[::-1]


def copy_char2d_sub(input: list[list[str]], x: int, y: int, width: int, height: int) -> list[list[str]]:
    return [line[x : x + width] for line in input[y : y + height]]  # noqa: E203
