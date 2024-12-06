from collections import defaultdict
from enum import StrEnum

from .. import tools


class Direction(StrEnum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


def calculate_next_position(map: tuple[tuple[str]], x: int, y: int, direction: Direction) -> tuple[int, int, Direction]:
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


def find_guard(map: tuple[tuple[str]]) -> tuple[int, int, Direction]:
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
                return x, y, Direction(cell)
    return None


def test_route(map: tuple[tuple[str]], guard_x: int, guard_y: int, guard_direction: Direction) -> (bool, bool, dict[set[Direction]]):
    visited = defaultdict(set)

    visited[(guard_y, guard_x)].add(guard_direction)  # Mark the starting position as visited
    off_map = False
    loop = False
    while not off_map and not loop:
        guard_x, guard_y, guard_direction = calculate_next_position(map, guard_x, guard_y, guard_direction) or (None, None, None)
        if guard_x is None:
            off_map = True
            break

        if (guard_y, guard_x) in visited and guard_direction in visited[(guard_y, guard_x)]:
            loop = True
            break

        visited[(guard_y, guard_x)].add(guard_direction)

    return off_map, loop, visited


def process(input: list[list[str]]):
    input_tuple = tuple(map(tuple, input))
    guard_x, guard_y, guard_direction = find_guard(input_tuple)

    _, _, original_route = test_route(input_tuple, guard_x, guard_y, guard_direction)

    loops = 0

    for location in original_route:
        if location == (guard_y, guard_x):
            continue

        updated_map = list(map(list, input_tuple))
        updated_map[location[0]][location[1]] = "#"
        updated_map = tuple(map(tuple, updated_map))

        _, loop, _ = test_route(updated_map, guard_x, guard_y, guard_direction)

        if loop:
            loops += 1

    return loops


def challenge():
    return process(tools.read_to_char2d("./inputs/06_1.txt"))
