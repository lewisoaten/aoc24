def read_to_string(file_path: str) -> str:
    with open(file_path) as file:
        return file.read().strip()


def read_to_int2d(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        return [[int(i) for i in line.split()] for line in file.read().splitlines()]
