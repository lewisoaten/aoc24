from collections import defaultdict

from .. import tools


def create_antenna_map(map: tuple[tuple[str]]) -> dict[str, set[tuple[int, int]]]:
    antenna_map = defaultdict(set)
    for y, line in enumerate(map):
        for x, item in enumerate(line):
            if item != ".":
                antenna_map[item].add((x, y))
    return antenna_map


def find_opposite_point(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    x3 = x1 - dx
    y3 = y1 - dy
    return x3, y3


def process(input: list[list[str]]):
    antenna_map = create_antenna_map(input)
    antinodes = set()
    for frequency in antenna_map:
        for x1, y1 in antenna_map[frequency]:
            for x2, y2 in antenna_map[frequency]:
                if (x1, y1) == (x2, y2):
                    continue
                x3, y3 = find_opposite_point(x1, y1, x2, y2)
                if x3 >= 0 and x3 < len(input[0]) and y3 >= 0 and y3 < len(input):
                    antinodes.add((x3, y3))
    return len(antinodes)


def parse_input(input: str) -> tuple[tuple[str]]:
    return tools.str_to_char2d(input)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/08_1.txt")))
