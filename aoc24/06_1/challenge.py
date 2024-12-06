from enum import StrEnum

from .. import tools


class Direction(StrEnum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def calculate_next_position(map: list[list[str]], x: int, y: int, direction: Direction) -> tuple[int, int, Direction]:
    if direction == Direction.UP:
        # Going off map
        if y == 0:
            return None

        # Hitting a wall
        if map[y - 1][x] == "#":
            return x, y, Direction.RIGHT

        # Continue
        return x, y - 1, direction

    elif direction == Direction.DOWN:
        # Going off map
        if y == len(map) - 1:
            return None

        # Hitting a wall
        if map[y + 1][x] == "#":
            return x, y, Direction.LEFT

        # Continue
        return x, y + 1, direction

    elif direction == Direction.LEFT:
        # Going off map
        if x == 0:
            return None

        # Hitting a wall
        if map[y][x - 1] == "#":
            return x, y, Direction.UP

        # Continue
        return x - 1, y, direction

    elif direction == Direction.RIGHT:
        # Going off map
        if x == len(map[y]) - 1:
            return None

        # Hitting a wall
        if map[y][x + 1] == "#":
            return x, y, Direction.DOWN

        # Continue
        return x + 1, y, direction


def find_guard(map: list[list[str]]) -> tuple[int, int, Direction]:
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
                return x, y, Direction(cell)
    return None


def count_steps(map: list[list[str]]) -> int:
    return sum([line.count("X") for line in map])


def process(input: list[list[str]]):
    guard_x, guard_y, guard_direction = find_guard(input)

    input[guard_y][guard_x] = "X"  # Mark the guard's starting position
    off_map = False
    while not off_map:
        guard_x, guard_y, guard_direction = calculate_next_position(input, guard_x, guard_y, guard_direction) or (None, None, None)
        if guard_x is None:
            off_map = True
            break
        input[guard_y][guard_x] = "X"

    return count_steps(input)


def challenge():
    return process(tools.read_to_char2d("./inputs/06_1.txt"))
