from functools import cache

from .. import tools


@cache
def match_prefix(string: str, prefixes: tuple[str]) -> int:
    if len(string) == 0:
        return 1

    matches = 0
    for prefix in prefixes:
        if string.startswith(prefix):
            matches += match_prefix(string[len(prefix) :], prefixes)  # noqa: E203

    return matches


def process(input: tuple[tuple[str], tuple[str]]) -> str:
    patterns, designs = input

    possible_designs = 0

    for design in designs:
        possible_designs += match_prefix(design, patterns)
    return possible_designs


def parse_input(input: str) -> tuple[tuple[str], tuple[str]]:
    patterns, designs = tools.str_to_two_sections(input)

    return tools.item_split(patterns, separator=", ", process_items=str), tools.str_to_lines(designs, process_line=str)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/19_1.txt")))
