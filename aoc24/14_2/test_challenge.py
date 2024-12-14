from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()
    )
    assert input == (
        {"p": (0, 4), "v": (3, -3)},
        {"p": (6, 3), "v": (-1, -3)},
        {"p": (10, 3), "v": (-1, 2)},
        {"p": (2, 0), "v": (2, -1)},
        {"p": (0, 0), "v": (1, 3)},
        {"p": (3, 0), "v": (-2, -2)},
        {"p": (7, 6), "v": (-1, -3)},
        {"p": (3, 0), "v": (-1, -2)},
        {"p": (9, 3), "v": (2, 3)},
        {"p": (7, 3), "v": (-1, 2)},
        {"p": (2, 4), "v": (2, -3)},
        {"p": (9, 5), "v": (-3, -3)},
    )


def test_challenge1():
    input = challenge.parse_input(
        """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()
    )

    assert challenge.process(input, grid_max=(11, 7)) == 12


def test_calculate_safety_factor1():
    input = (
        {"p": (0, 0), "v": (0, 0)},
        {"p": (4, 0), "v": (0, 0)},
        {"p": (0, 4), "v": (0, 0)},
        {"p": (4, 4), "v": (0, 0)},
        {"p": (2, 2), "v": (0, 0)},
        {"p": (2, 0), "v": (0, 0)},
        {"p": (0, 2), "v": (0, 0)},
    )
    challenge.print_tile(input, grid_max=(5, 5))
    assert challenge.calculate_safety_factor(input, grid_max=(5, 5)) == 1


def test_recalculate_position1():
    grid = (3, 3)
    robots = ({"p": (0, 0), "v": (1, 0)},)
    challenge.print_tile(robots, grid_max=grid)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (1, 0), "v": (1, 0)},)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (2, 0), "v": (1, 0)},)
    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))

    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (0, 0), "v": (1, 0)},)


def test_recalculate_position2():
    grid = (3, 3)
    robots = ({"p": (0, 0), "v": (-1, 0)},)
    challenge.print_tile(robots, grid_max=grid)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (2, 0), "v": (-1, 0)},)


def test_recalculate_position3():
    grid = (3, 3)
    robots = ({"p": (0, 0), "v": (-1, 0)},)
    challenge.print_tile(robots, grid_max=grid)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 2, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (1, 0), "v": (-1, 0)},)


def test_recalculate_position4():
    grid = (3, 3)
    robots = ({"p": (0, 0), "v": (0, 1)},)
    challenge.print_tile(robots, grid_max=grid)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (0, 1), "v": (0, 1)},)

    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))
    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (0, 2), "v": (0, 1)},)
    robots = tuple(map(lambda robot: robot | {"p": challenge.recalculate_position(robot, 1, grid_max=grid)}, robots))

    challenge.print_tile(robots, grid_max=grid)
    assert robots == ({"p": (0, 0), "v": (0, 1)},)
