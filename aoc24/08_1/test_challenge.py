from . import challenge


def test_challenge():
    input = challenge.parse_input(
        """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
    """.strip()
    )

    assert challenge.process(input) == 14


def test_get_intersection_points1():
    assert challenge.find_opposite_point(*(4, 3), *(5, 5)) == (3, 1)


def test_get_intersection_points2():
    assert challenge.find_opposite_point(*(5, 5), *(4, 3)) == (6, 7)