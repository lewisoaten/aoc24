from . import challenge
from .. import tools


def test_challenge():
    input = tools.str_to_lines(
        """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
    """.strip()
    )

    assert input[0] == "190: 10 19"

    input = challenge.parse_input(
        """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
    """.strip()
    )

    print(input)

    assert input[1][0] == 3267
    assert input[1][1][1] == 40

    assert challenge.process(input) == 3749
