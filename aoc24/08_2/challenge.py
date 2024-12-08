import math
from collections import defaultdict

from .. import tools


def create_antenna_map(map: tuple[tuple[str]]) -> dict[str, set[tuple[int, int]]]:
    antenna_map = defaultdict(set)
    for y, line in enumerate(map):
        for x, item in enumerate(line):
            if item != ".":
                antenna_map[item].add((x, y))
    return antenna_map


def points_on_line(x1, y1, x2, y2, x_max, y_max):
    dx = x2 - x1
    dy = y2 - y1

    divisor = math.gcd(dx, dy)
    step_x = dx // divisor
    step_y = dy // divisor

    points = set()

    # Generate forward direction
    x, y = x1, y1
    while 0 <= x <= x_max and 0 <= y <= y_max:
        points.add((x, y))
        x += step_x
        y += step_y

    # Generate backward direction
    x, y = x1 - step_x, y1 - step_y
    while 0 <= x <= x_max and 0 <= y <= y_max:
        points.add((x, y))
        x -= step_x
        y -= step_y

    return points


def process(input: list[list[str]]):
    antenna_map = create_antenna_map(input)
    antinodes = set()
    for frequency in antenna_map:
        for x1, y1 in antenna_map[frequency]:
            for x2, y2 in antenna_map[frequency]:
                if (x1, y1) == (x2, y2):
                    continue
                antinodes.update(points_on_line(x1, y1, x2, y2, len(input[0]) - 1, len(input) - 1))
    return len(antinodes)


def parse_input(input: str) -> tuple[tuple[str]]:
    return tools.str_to_char2d(input)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/08_1.txt")))
