import re

from .. import tools


def process(input: str):
    output = 0
    regex = r"mul\(\d+,\d+\)"

    matches = re.finditer(regex, input)

    for match in matches:
        values = match.group(0)[4:-1].split(",")

        output += int(values[0]) * int(values[1])

    return output


def challenge():
    return process(tools.read_to_string("./inputs/03_1.txt"))
