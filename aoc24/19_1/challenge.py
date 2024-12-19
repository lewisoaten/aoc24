from .. import tools


def match_prefix(string: str, prefixes: tuple[str]) -> bool:
    for prefix in prefixes:
        if string.startswith(prefix):
            if len(string) == len(prefix) or match_prefix(string[len(prefix) :], prefixes):  # noqa: E203
                return True
    return False


def process(input: tuple[tuple[str], tuple[str]]) -> str:
    patterns, designs = input

    possible_designs = 0

    for design in designs:
        if match_prefix(design, patterns):
            possible_designs += 1
    return possible_designs


def parse_input(input: str) -> tuple[tuple[str], tuple[str]]:
    patterns, designs = tools.str_to_two_sections(input)

    return tools.item_split(patterns, separator=", ", process_items=str), tools.str_to_lines(designs, process_line=str)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/19_1.txt")))
