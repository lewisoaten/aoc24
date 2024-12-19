from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
    )
    assert input == (
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0),
    )


def test_plot_maze1():
    input = challenge.parse_input(
        """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
    )

    plot = challenge.plot_maze(input, 7, 7, 5)

    assert plot == [
        [".", ".", ".", "#", ".", ".", "."],
        [".", ".", "#", ".", ".", ".", "."],
        [".", ".", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "#", "."],
        [".", ".", ".", ".", "#", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
    ]


def test_challenge1():
    input = challenge.parse_input(
        """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
    )

    assert challenge.process(input, width=7, height=7, end=12) == "6,1"
