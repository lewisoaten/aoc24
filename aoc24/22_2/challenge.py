from collections import defaultdict
from itertools import pairwise

from .. import tools


def mix(input: int, secret: int) -> int:
    # To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes
    #  the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    return input ^ secret


def prune(secret: int) -> int:
    # To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that
    #  operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    return secret % 16777216


def next_secret(secret: int, limit: int) -> int:
    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret
    #  number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    result = secret
    for _ in range(limit):
        result = prune(mix(result * 64, result))
        result = prune(mix(result // 32, result))
        result = prune(mix(result * 2048, result))
        yield result


def nth_secret(secret: int, n: int) -> int:
    *_, nth = next_secret(secret, n)
    return nth


def get_prices(secret: int, n: int) -> list[int]:
    return [secret % 10] + [x % 10 for x in next_secret(secret, n - 1)]


def get_diffs(prices: list[int]) -> list[int]:
    return [price_a - price_b for price_a, price_b in pairwise(prices)]


def calculate_patterns(
    diffs: list[int], prices: list[int], seen: set[tuple[int, int, int, int]], patterns: dict[tuple[int, int, int, int], int]
) -> dict[tuple[int, int, int, int], int]:
    for i in range(len(prices) - 4):
        pattern = tuple(diffs[i : i + 4])  # noqa: E203
        if pattern not in seen:
            patterns[pattern] += prices[i + 4]
            seen.add(pattern)


def process(input: tuple[str]) -> int:
    patterns = defaultdict(int)

    for line in input:
        seen = set()
        prices = get_prices(line, 2000)
        diffs = get_diffs(prices)
        calculate_patterns(diffs, prices, seen, patterns)

    return max(patterns.values())


def parse_input(input: str) -> tuple[str]:
    codes = tools.str_to_lines(input, process_line=int)

    return codes


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/22_1.txt")))
