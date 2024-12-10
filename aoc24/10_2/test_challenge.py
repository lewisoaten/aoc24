from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
0
""".strip()
    )
    # dict[tuple[int, int, int], list[tuple[int, int, int]]]
    assert input == {(0, 0, 0): []}


def test_parse_input2():
    input = challenge.parse_input(
        """
01
""".strip()
    )
    # dict[tuple[int, int, int], list[tuple[int, int, int]]]
    assert input == {
        (0, 0, 0): [(1, 0, 1, 0)],
        (1, 0, 1): [],
    }


def test_parse_input3():
    input = challenge.parse_input(
        """
0
1
""".strip()
    )
    # dict[tuple[int, int, int], list[tuple[int, int, int]]]
    assert input == {
        (0, 0, 0): [(0, 1, 1, 0)],
        (0, 1, 1): [],
    }


def test_parse_input4():
    input = challenge.parse_input(
        """
02

""".strip()
    )
    # dict[tuple[int, int, int], list[tuple[int, int, int]]]
    assert input == {
        (0, 0, 0): [],
        (1, 0, 2): [],
    }


def test_challenge1():
    input = challenge.parse_input(
        """
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
""".strip()
    )

    assert challenge.process(input) == 3


def test_challenge2():
    input = challenge.parse_input(
        """
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
""".strip()
    )

    assert challenge.process(input) == 13


def test_challenge3():
    input = challenge.parse_input(
        """
012345
123456
234567
345678
4.6789
56789.
""".strip()
    )

    assert challenge.process(input) == 227


def test_challenge4():
    input = challenge.parse_input(
        """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()
    )

    assert challenge.process(input) == 81
