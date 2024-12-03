import re

from .. import tools


def process(input: str):
    output = 0
    enabled = True
    regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    matches = re.finditer(regex, input)

    for match in matches:
        if "do()" in match.group(0):
            enabled = True
            continue

        if "don't()" in match.group(0):
            enabled = False
            continue

        if enabled:
            values = match.group(0)[4:-1].split(",")
            output += int(values[0]) * int(values[1])

    return output


def challenge():
    return process(tools.read_to_string("./inputs/03_1.txt"))
