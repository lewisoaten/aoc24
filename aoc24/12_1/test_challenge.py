from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
AB
CD
""".strip()
    )
    assert input == (["A", "B"], ["C", "D"])


def test_expand_plot1():
    input = challenge.parse_input(
        """
AAAA
BBCD
BBCC
EEEC
""".strip()
    )

    assert challenge.expand_plot(input, 0, 0, "A", set()) == {(0, 0), (1, 0), (2, 0), (3, 0)}
    assert challenge.expand_plot(input, 0, 1, "B", set()) == {(0, 1), (1, 1), (0, 2), (1, 2)}
    assert challenge.expand_plot(input, 2, 1, "C", set()) == {(2, 1), (2, 2), (3, 2), (3, 3)}
    assert challenge.expand_plot(input, 3, 1, "D", set()) == {(3, 1)}
    assert challenge.expand_plot(input, 2, 3, "E", set()) == {(0, 3), (1, 3), (2, 3)}


def test_challenge1():
    input = challenge.parse_input(
        """
AAAA
BBCD
BBCC
EEEC
""".strip()
    )

    A = 4 * 10
    B = 4 * 8
    C = 4 * 10
    D = 1 * 4
    E = 3 * 8

    assert challenge.process(input) == A + B + C + D + E


def test_challenge2():
    input = challenge.parse_input(
        """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""".strip()
    )

    assert challenge.process(input) == 772


def test_challenge3():
    input = challenge.parse_input(
        """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()
    )

    assert challenge.process(input) == 1930
