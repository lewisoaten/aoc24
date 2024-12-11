from functools import cache
from math import floor
from math import log10

from .. import tools


@cache
def blink(stone: int, remaining_blinks: int) -> int:  # Return count
    # Simultaneously modify each item in the list to the following rules:
    # - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    #   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
    #   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

    if remaining_blinks == 0:
        return 1

    if stone == 0:
        return blink(1, remaining_blinks - 1)

    length = floor(log10(stone)) + 1
    if length % 2 == 0:
        return blink(stone // 10 ** (length // 2), remaining_blinks - 1) + blink(stone % 10 ** (length // 2), remaining_blinks - 1)

    return blink(stone * 2024, remaining_blinks - 1)


def process(input: list[int], blinks: int):
    return sum(map(lambda x: blink(x, blinks), input))


def parse_input(input: str) -> list[int]:
    return list(tools.item_split(input, separator=" ", process_items=int))


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/11_1.txt")), 75)
