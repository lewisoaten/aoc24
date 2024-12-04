from . import challenge
from .. import tools


def test_challenge():
    input = tools.str_to_char2d(
        """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
    """.strip()
    )
    assert challenge.process(input) == 9


def test_simple_challenge():
    input = tools.str_to_char2d(
        """
M.S
.A.
M.S
""".strip()
    )
    assert challenge.process(input) == 1
