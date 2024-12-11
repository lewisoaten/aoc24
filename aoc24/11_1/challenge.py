from .. import tools


def blink(stones: list[int]):
    # Simultaneously modify each item in the list to the following rules:
    # - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    # - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    #   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
    #   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            new_stones.append(int(str(stone)[:half]))
            new_stones.append(int(str(stone)[half:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


def process(input: list[int], blinks: int):
    for i in range(blinks):
        input = blink(input)
    return len(input)


def parse_input(input: str) -> list[int]:
    return list(tools.item_split(input, separator=" ", process_items=int))


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/11_1.txt")), 25)
