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
0123
1234
8765
9876
""".strip()
    )

    assert challenge.process(input) == 1


def test_challenge2():
    input = challenge.parse_input(
        """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
""".strip()
    )

    assert challenge.process(input) == 2


def test_challenge3():
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

    assert challenge.process(input) == 4


def test_challenge4():
    input = challenge.parse_input(
        """
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
""".strip()
    )

    assert challenge.process(input) == 3


def test_challenge5():
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

    assert challenge.process(input) == 36
