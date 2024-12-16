from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()
    )
    assert input == (
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "E", "#"],
        ["#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#", ".", "#", ".", "#"],
        ["#", ".", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "S", ".", ".", "#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    )


def test_maze_graph1():
    input = challenge.parse_input(
        """
#####
#S.E#
#####
""".strip()
    )

    start = challenge.find_position(input, "S")

    graph = challenge.create_maze_graph(input, {}, (start[0], start[1], challenge.Direction.East))
    assert graph == {
        (1, 1, challenge.Direction.East): {(2, 1, challenge.Direction.East): 1, (1, 1, challenge.Direction.South): 1000, (1, 1, challenge.Direction.North): 1000},
        (2, 1, challenge.Direction.East): {(3, 1, challenge.Direction.East): 1, (2, 1, challenge.Direction.South): 1000, (2, 1, challenge.Direction.North): 1000},
        (3, 1, challenge.Direction.East): {(3, 1, challenge.Direction.South): 1000, (3, 1, challenge.Direction.North): 1000},
        (3, 1, challenge.Direction.South): {(3, 1, challenge.Direction.East): 1000, (3, 1, challenge.Direction.West): 1000},
        (3, 1, challenge.Direction.West): {(3, 1, challenge.Direction.South): 1000, (2, 1, challenge.Direction.West): 1, (3, 1, challenge.Direction.North): 1000},
        (2, 1, challenge.Direction.West): {(2, 1, challenge.Direction.South): 1000, (1, 1, challenge.Direction.West): 1, (2, 1, challenge.Direction.North): 1000},
        (2, 1, challenge.Direction.South): {(2, 1, challenge.Direction.East): 1000, (2, 1, challenge.Direction.West): 1000},
        (1, 1, challenge.Direction.West): {(1, 1, challenge.Direction.South): 1000, (1, 1, challenge.Direction.North): 1000},
        (1, 1, challenge.Direction.South): {(1, 1, challenge.Direction.East): 1000, (1, 1, challenge.Direction.West): 1000},
        (1, 1, challenge.Direction.North): {(1, 1, challenge.Direction.East): 1000, (1, 1, challenge.Direction.West): 1000},
        (2, 1, challenge.Direction.North): {(2, 1, challenge.Direction.East): 1000, (2, 1, challenge.Direction.West): 1000},
        (3, 1, challenge.Direction.North): {(3, 1, challenge.Direction.East): 1000, (3, 1, challenge.Direction.West): 1000},
    }


def test_maze_graph2():
    input = challenge.parse_input(
        """
#####
#S#E#
#...#
#####
""".strip()
    )

    start = challenge.find_position(input, "S")

    graph = challenge.create_maze_graph(input, {}, (start[0], start[1], challenge.Direction.East))
    assert graph == {
        (1, 1, challenge.Direction.East): {(1, 1, challenge.Direction.South): 1000, (1, 1, challenge.Direction.North): 1000},
        (1, 1, challenge.Direction.South): {(1, 1, challenge.Direction.East): 1000, (1, 2, challenge.Direction.South): 1, (1, 1, challenge.Direction.West): 1000},
        (1, 2, challenge.Direction.South): {(1, 2, challenge.Direction.East): 1000, (1, 2, challenge.Direction.West): 1000},
        (1, 2, challenge.Direction.East): {(2, 2, challenge.Direction.East): 1, (1, 2, challenge.Direction.South): 1000, (1, 2, challenge.Direction.North): 1000},
        (2, 2, challenge.Direction.East): {(3, 2, challenge.Direction.East): 1, (2, 2, challenge.Direction.South): 1000, (2, 2, challenge.Direction.North): 1000},
        (3, 2, challenge.Direction.East): {(3, 2, challenge.Direction.South): 1000, (3, 2, challenge.Direction.North): 1000},
        (3, 2, challenge.Direction.South): {(3, 2, challenge.Direction.East): 1000, (3, 2, challenge.Direction.West): 1000},
        (3, 2, challenge.Direction.West): {(3, 2, challenge.Direction.South): 1000, (2, 2, challenge.Direction.West): 1, (3, 2, challenge.Direction.North): 1000},
        (2, 2, challenge.Direction.West): {(2, 2, challenge.Direction.South): 1000, (1, 2, challenge.Direction.West): 1, (2, 2, challenge.Direction.North): 1000},
        (2, 2, challenge.Direction.South): {(2, 2, challenge.Direction.East): 1000, (2, 2, challenge.Direction.West): 1000},
        (1, 2, challenge.Direction.West): {(1, 2, challenge.Direction.South): 1000, (1, 2, challenge.Direction.North): 1000},
        (1, 2, challenge.Direction.North): {(1, 2, challenge.Direction.East): 1000, (1, 2, challenge.Direction.West): 1000, (1, 1, challenge.Direction.North): 1},
        (1, 1, challenge.Direction.North): {(1, 1, challenge.Direction.East): 1000, (1, 1, challenge.Direction.West): 1000},
        (1, 1, challenge.Direction.West): {(1, 1, challenge.Direction.South): 1000, (1, 1, challenge.Direction.North): 1000},
        (2, 2, challenge.Direction.North): {(2, 2, challenge.Direction.East): 1000, (2, 2, challenge.Direction.West): 1000},
        (3, 2, challenge.Direction.North): {(3, 2, challenge.Direction.East): 1000, (3, 2, challenge.Direction.West): 1000, (3, 1, challenge.Direction.North): 1},
        (3, 1, challenge.Direction.North): {(3, 1, challenge.Direction.East): 1000, (3, 1, challenge.Direction.West): 1000},
        (3, 1, challenge.Direction.East): {(3, 1, challenge.Direction.South): 1000, (3, 1, challenge.Direction.North): 1000},
        (3, 1, challenge.Direction.South): {(3, 1, challenge.Direction.East): 1000, (3, 2, challenge.Direction.South): 1, (3, 1, challenge.Direction.West): 1000},
        (3, 1, challenge.Direction.West): {(3, 1, challenge.Direction.South): 1000, (3, 1, challenge.Direction.North): 1000},
    }


def test_challenge1():
    input = challenge.parse_input(
        """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()
    )

    assert challenge.process(input) == 7036


def test_challenge2():
    input = challenge.parse_input(
        """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()
    )

    assert challenge.process(input) == 11048
