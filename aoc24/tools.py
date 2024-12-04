def read_to_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read().strip()


def read_to_int2d(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        return [[int(i) for i in line.split()] for line in file.read().splitlines()]


def read_to_char2d(file_path: str) -> list[list[str]]:
    with open(file_path) as file:
        return [list(line) for line in file.read().splitlines()]


def str_to_char2d(input: str) -> list[list[str]]:
    return [list(line) for line in input.splitlines()]
