from .. import tools


def mix(input: int, secret: int) -> int:
    # To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes
    #  the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    return input ^ secret


def prune(secret: int) -> int:
    # To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that
    #  operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    return secret % 16777216


def next_secret(secret: int) -> int:
    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret
    #  number. Finally, prune the secret number.
    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

    result = prune(mix(secret * 64, secret))
    result = prune(mix(result // 32, result))
    return prune(mix(result * 2048, result))


def nth_secret(secret: int, n: int) -> int:
    for _ in range(n):
        secret = next_secret(secret)
    return secret


def process(input: tuple[str]) -> int:
    secret_sum = 0
    for line in input:
        secret_sum += nth_secret(line, 2000)
    return secret_sum


def parse_input(input: str) -> tuple[str]:
    codes = tools.str_to_lines(input, process_line=int)

    return codes


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/22_1.txt")))
