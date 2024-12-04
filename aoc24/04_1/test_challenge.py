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
    assert challenge.process(input) == 18


def test_up_challenge():
    input = tools.str_to_char2d(
        """
S
A
M
X
""".strip()
    )
    assert challenge.process(input) == 1


def test_up_right_challenge():
    input = tools.str_to_char2d(
        """
IIIS
IIAI
IMII
XIII
""".strip()
    )
    assert challenge.process(input) == 1


def test_right_challenge():
    input = tools.str_to_char2d(
        """
XMAS
""".strip()
    )
    assert challenge.process(input) == 1


def test_down_right_challenge():
    input = tools.str_to_char2d(
        """
XIII
IMII
IIAI
IIIS
""".strip()
    )
    assert challenge.process(input) == 1


def test_down_challenge():
    input = tools.str_to_char2d(
        """
X
M
A
S
""".strip()
    )
    assert challenge.process(input) == 1


def test_down_left_challenge():
    input = tools.str_to_char2d(
        """
IIIX
IIMI
IAII
SIII
""".strip()
    )
    assert challenge.process(input) == 1


def test_left_challenge():
    input = tools.str_to_char2d(
        """
SAMX
""".strip()
    )
    assert challenge.process(input) == 1


def test_up_left_challenge():
    input = tools.str_to_char2d(
        """
SIII
IAII
IIMI
IIIX
""".strip()
    )
    assert challenge.process(input) == 1


def test_overlap_challenge():
    input = tools.str_to_char2d(
        """
XMAS
MMII
AIAI
SIIS
""".strip()
    )
    assert challenge.process(input) == 3
