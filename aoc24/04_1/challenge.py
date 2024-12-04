from enum import Enum
from enum import StrEnum

from .. import tools


class Direction(Enum):
    UP = 1
    UP_RIGHT = 2
    RIGHT = 3
    DOWN_RIGHT = 4
    DOWN = 5
    DOWN_LEFT = 6
    LEFT = 7
    UP_LEFT = 8


class Xmas(StrEnum):
    X = "X"
    M = "M"
    A = "A"
    S = "S"


def find_xmas(input: list[list[str]], x: int, y: int, on_char: Xmas, direction: Direction) -> bool:
    nextx = x
    nexty = y
    match direction:
        case Direction.UP:
            if y == 0:
                return False
            nexty -= 1
        case Direction.UP_RIGHT:
            if y == 0 or x == len(input[y]) - 1:
                return False
            nexty -= 1
            nextx += 1
        case Direction.RIGHT:
            if x == len(input[y]) - 1:
                return False
            nextx += 1
        case Direction.DOWN_RIGHT:
            if y == len(input) - 1 or x == len(input[y]) - 1:
                return False
            nexty += 1
            nextx += 1
        case Direction.DOWN:
            if y == len(input) - 1:
                return False
            nexty += 1
        case Direction.DOWN_LEFT:
            if y == len(input) - 1 or x == 0:
                return False
            nexty += 1
            nextx -= 1
        case Direction.LEFT:
            if x == 0:
                return False
            nextx -= 1
        case Direction.UP_LEFT:
            if y == 0 or x == 0:
                return False
            nexty -= 1
            nextx -= 1

    match on_char:
        case Xmas.X:
            next_char = Xmas.M
            if input[nexty][nextx] != next_char:
                return False
        case Xmas.M:
            next_char = Xmas.A
            if input[nexty][nextx] != next_char:
                return False
        case Xmas.A:
            next_char = Xmas.S
            if input[nexty][nextx] != next_char:
                return False
            return True
        case Xmas.S:
            print("Should never have got here?!")
            return False

    return find_xmas(input, nextx, nexty, next_char, direction)


def process(input: list[list[str]]):
    count_xmas = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == Xmas.X:
                if find_xmas(input, x, y, Xmas.X, Direction.UP):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.UP_RIGHT):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.RIGHT):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.DOWN_RIGHT):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.DOWN):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.DOWN_LEFT):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.LEFT):
                    count_xmas += 1
                if find_xmas(input, x, y, Xmas.X, Direction.UP_LEFT):
                    count_xmas += 1

    return count_xmas


def challenge():
    return process(tools.read_to_char2d("./inputs/04_1.txt"))
