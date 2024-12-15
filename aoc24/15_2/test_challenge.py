from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()
    )
    assert input == (
        (
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", "#", ".", ".", ".", ".", "[", "]", ".", ".", ".", ".", "[", "]", ".", ".", "[", "]", "#", "#"],
            ["#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "[", "]", ".", ".", "#", "#"],
            ["#", "#", ".", ".", "[", "]", "[", "]", ".", ".", ".", ".", "[", "]", ".", ".", "[", "]", "#", "#"],
            ["#", "#", ".", ".", ".", ".", "[", "]", "@", ".", ".", ".", ".", ".", "[", "]", ".", ".", "#", "#"],
            ["#", "#", "[", "]", "#", "#", ".", ".", ".", ".", "[", "]", ".", ".", ".", ".", ".", ".", "#", "#"],
            ["#", "#", "[", "]", ".", ".", ".", ".", "[", "]", ".", ".", ".", ".", "[", "]", ".", ".", "#", "#"],
            ["#", "#", ".", ".", "[", "]", "[", "]", ".", ".", "[", "]", ".", ".", "[", "]", "[", "]", "#", "#"],
            ["#", "#", ".", ".", ".", ".", ".", ".", ".", ".", "[", "]", ".", ".", ".", ".", ".", ".", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ),
        (
            "<",
            "v",
            "v",
            ">",
            "^",
            "<",
            "v",
            "^",
            ">",
            "v",
            ">",
            "^",
            "v",
            "v",
            "^",
            "v",
            ">",
            "v",
            "<",
            ">",
            "v",
            "^",
            "v",
            "<",
            "v",
            "<",
            "^",
            "v",
            "v",
            "<",
            "<",
            "<",
            "^",
            ">",
            "<",
            "<",
            ">",
            "<",
            ">",
            ">",
            "v",
            "<",
            "v",
            "v",
            "v",
            "<",
            ">",
            "^",
            "v",
            "^",
            ">",
            "^",
            "<",
            "<",
            "<",
            ">",
            "<",
            "<",
            "v",
            "<",
            "<",
            "<",
            "v",
            "^",
            "v",
            "v",
            "^",
            "v",
            ">",
            "^",
            "v",
            "v",
            "v",
            "<",
            "<",
            "^",
            ">",
            "^",
            "v",
            "^",
            "^",
            ">",
            "<",
            "<",
            ">",
            ">",
            ">",
            "<",
            ">",
            "^",
            "<",
            "<",
            ">",
            "<",
            "^",
            "v",
            "v",
            "^",
            "^",
            "<",
            ">",
            "v",
            "v",
            "v",
            "<",
            ">",
            ">",
            "<",
            "^",
            "^",
            "v",
            ">",
            "^",
            ">",
            "v",
            "v",
            "<",
            ">",
            "v",
            "<",
            "<",
            "<",
            "<",
            "v",
            "<",
            "^",
            "v",
            ">",
            "^",
            "<",
            "^",
            "^",
            ">",
            ">",
            ">",
            "^",
            "<",
            "v",
            "<",
            "v",
            ">",
            "<",
            ">",
            "v",
            "v",
            ">",
            "v",
            "^",
            "v",
            "^",
            "<",
            ">",
            ">",
            "<",
            ">",
            ">",
            ">",
            ">",
            "<",
            "^",
            "^",
            ">",
            "v",
            "v",
            ">",
            "v",
            "<",
            "^",
            "^",
            "^",
            ">",
            ">",
            "v",
            "^",
            "v",
            "^",
            "<",
            "^",
            "^",
            ">",
            "v",
            "^",
            "^",
            ">",
            "v",
            "^",
            "<",
            "^",
            "v",
            ">",
            "v",
            "<",
            ">",
            ">",
            "v",
            "^",
            "v",
            "^",
            "<",
            "v",
            ">",
            "v",
            "^",
            "^",
            "<",
            "^",
            "^",
            "v",
            "v",
            "<",
            "<",
            "<",
            "v",
            "<",
            "^",
            ">",
            ">",
            "^",
            "^",
            "^",
            "^",
            ">",
            ">",
            ">",
            "v",
            "^",
            "<",
            ">",
            "v",
            "v",
            "v",
            "^",
            ">",
            "<",
            "v",
            "<",
            "<",
            "<",
            ">",
            "^",
            "^",
            "^",
            "v",
            "v",
            "^",
            "<",
            "v",
            "v",
            "v",
            ">",
            "^",
            ">",
            "v",
            "<",
            "^",
            "^",
            "^",
            "^",
            "v",
            "<",
            ">",
            "^",
            ">",
            "v",
            "v",
            "v",
            "v",
            ">",
            "<",
            ">",
            ">",
            "v",
            "^",
            "<",
            "<",
            "^",
            "^",
            "^",
            "^",
            "^",
            "^",
            ">",
            "<",
            "^",
            ">",
            "<",
            ">",
            ">",
            ">",
            "<",
            ">",
            "^",
            "^",
            "<",
            "<",
            "^",
            "^",
            "v",
            ">",
            ">",
            ">",
            "<",
            "^",
            "<",
            "v",
            ">",
            "^",
            "<",
            "v",
            "v",
            ">",
            ">",
            "v",
            ">",
            ">",
            ">",
            "^",
            "v",
            ">",
            "<",
            ">",
            "^",
            "v",
            ">",
            "<",
            "<",
            "<",
            "<",
            "v",
            ">",
            ">",
            "v",
            "<",
            "v",
            "<",
            "v",
            ">",
            "v",
            "v",
            "v",
            ">",
            "^",
            "<",
            ">",
            "<",
            "<",
            ">",
            "^",
            ">",
            "<",
            "^",
            ">",
            ">",
            "<",
            ">",
            "^",
            "v",
            "<",
            ">",
            "<",
            "^",
            "v",
            "v",
            "v",
            "<",
            "^",
            "^",
            "<",
            ">",
            "<",
            "v",
            "<",
            "<",
            "<",
            "<",
            "<",
            ">",
            "<",
            "^",
            "v",
            "<",
            "<",
            "<",
            ">",
            "<",
            "<",
            "<",
            "^",
            "^",
            "<",
            "v",
            "<",
            "^",
            "^",
            "^",
            ">",
            "<",
            "^",
            ">",
            ">",
            "^",
            "<",
            "v",
            "^",
            ">",
            "<",
            "<",
            "<",
            "^",
            ">",
            ">",
            "^",
            "v",
            "<",
            "v",
            "^",
            "v",
            "<",
            "v",
            "^",
            ">",
            "^",
            ">",
            ">",
            "^",
            "v",
            ">",
            "v",
            "v",
            ">",
            "^",
            "<",
            "<",
            "^",
            "v",
            "<",
            ">",
            ">",
            "<",
            "<",
            ">",
            "<",
            "<",
            "v",
            "<",
            "<",
            "v",
            ">",
            "<",
            ">",
            "v",
            "<",
            "^",
            "v",
            "v",
            "<",
            "<",
            "<",
            ">",
            "^",
            "^",
            "v",
            "^",
            ">",
            "^",
            "^",
            ">",
            ">",
            ">",
            "<",
            "<",
            "^",
            "v",
            ">",
            ">",
            "v",
            "^",
            "v",
            ">",
            "<",
            "^",
            "^",
            ">",
            ">",
            "^",
            "<",
            ">",
            "v",
            "v",
            "^",
            "<",
            ">",
            "<",
            "^",
            "^",
            ">",
            "^",
            "^",
            "^",
            "<",
            ">",
            "<",
            "v",
            "v",
            "v",
            "v",
            "v",
            "^",
            "v",
            "<",
            "v",
            "<",
            "<",
            ">",
            "^",
            "v",
            "<",
            "v",
            ">",
            "v",
            "<",
            "<",
            "^",
            ">",
            "<",
            "<",
            ">",
            "<",
            "<",
            ">",
            "<",
            "<",
            "<",
            "^",
            "^",
            "<",
            "<",
            "<",
            "^",
            "<",
            "<",
            ">",
            ">",
            "<",
            "<",
            ">",
            "<",
            "^",
            "^",
            "^",
            ">",
            "^",
            "^",
            "<",
            ">",
            "^",
            ">",
            "v",
            "<",
            ">",
            "^",
            "^",
            ">",
            "v",
            "v",
            "<",
            "^",
            "v",
            "^",
            "v",
            "<",
            "v",
            "v",
            ">",
            "^",
            "<",
            ">",
            "<",
            "v",
            "<",
            "^",
            "v",
            ">",
            "^",
            "^",
            "^",
            ">",
            ">",
            ">",
            "^",
            "^",
            "v",
            "v",
            "v",
            "^",
            ">",
            "v",
            "v",
            "v",
            "<",
            ">",
            ">",
            ">",
            "^",
            "<",
            "^",
            ">",
            ">",
            ">",
            ">",
            ">",
            "^",
            "<",
            "<",
            "^",
            "v",
            ">",
            "^",
            "v",
            "v",
            "v",
            "<",
            ">",
            "^",
            "<",
            ">",
            "<",
            "<",
            "v",
            ">",
            "v",
            "^",
            "^",
            ">",
            ">",
            ">",
            "<",
            "<",
            "^",
            "^",
            "<",
            ">",
            ">",
            "^",
            "v",
            "^",
            "<",
            "v",
            "^",
            "v",
            "v",
            "<",
            ">",
            "v",
            "^",
            "<",
            "<",
            ">",
            "^",
            "<",
            "^",
            "v",
            "^",
            "v",
            ">",
            "<",
            "^",
            "<",
            "<",
            "<",
            ">",
            "<",
            "<",
            "^",
            "<",
            "v",
            ">",
            "<",
            "v",
            "<",
            ">",
            "v",
            "v",
            ">",
            ">",
            "v",
            ">",
            "<",
            "v",
            "^",
            "<",
            "v",
            "v",
            "<",
            ">",
            "v",
            "^",
            "<",
            "<",
            "^",
        ),
    )


def test_move_robot1():
    warehouse_map, instructions = challenge.parse_input(
        """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 306 + 308 + 406

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (10, 3)

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 305 + 307 + 406

    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 305 + 307 + 406

    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 305 + 307 + 406

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 305 + 307 + 406

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 305 + 307 + 406

    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 207 + 306

    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 207 + 306

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 207 + 306

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 207 + 306

    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 207 + 306

    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 105 + 207 + 306


def test_move_robot2():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#@O.#
#...#
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##@.[]..##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 104

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (2, 1)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 104
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 105
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 106
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##...@[]##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 106


def test_move_robot3():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#.O@#
#...#
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##..[]@.##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 104

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (6, 1)

    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert challenge.coordinate_count(warehouse_map) == 103
    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert challenge.coordinate_count(warehouse_map) == 102
    robot_position = challenge.move_robot(warehouse_map, robot_position, "<")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##[]@...##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 102


def test_move_robot4():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#.@.#
#.O.#
#...#
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##..@...##
##..[]..##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 204

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (4, 1)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 204
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert challenge.coordinate_count(warehouse_map) == 304
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##......##
##...@..##
##..[]..##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 304


def test_move_robot5():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#...#
#.O.#
#.@.#
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##......##
##..[]..##
##..@...##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 204

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (4, 3)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 204
    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert challenge.coordinate_count(warehouse_map) == 104
    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##..[]..##
##...@..##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 104


def test_move_robot6():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#.@.#
#OOO#
#.O.#
#...#
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##..@...##
##[][][]##
##..[]..##
##......##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 202 + 204 + 206 + 304

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (4, 1)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 202 + 204 + 206 + 304
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert challenge.coordinate_count(warehouse_map) == 202 + 304 + 206 + 404
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##......##
##[].@[]##
##..[]..##
##..[]..##
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 202 + 304 + 206 + 404


def test_move_robot7():
    warehouse_map, instructions = challenge.parse_input(
        """
######
#....#
#..O.#
#@OO.#
#.OOO#
#....#
######

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
############
##........##
##....[]..##
##@.[][]..##
##..[][][]##
##........##
############
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 206 + 304 + 306 + 404 + 406 + 408

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (2, 3)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 206 + 304 + 306 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 206 + 305 + 307 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert challenge.coordinate_count(warehouse_map) == 206 + 305 + 307 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert challenge.coordinate_count(warehouse_map) == 206 + 305 + 307 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 206 + 305 + 307 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 206 + 305 + 307 + 404 + 406 + 408
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert challenge.coordinate_count(warehouse_map) == 306 + 405 + 407 + 504 + 506 + 508
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    assert challenge.coordinate_count(warehouse_map) == 306 + 405 + 407 + 504 + 506 + 508
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
############
##........##
##....@...##
##....[]..##
##...[][].##
##..[][][]##
############
""".strip()
    )


def test_move_robot8_annoying_failure_case_argh():
    warehouse_map, instructions = challenge.parse_input(
        """
#####
#...#
#@O.#
#.OO#
#..##
#####

>
""".strip()
    )

    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##......##
##@.[]..##
##..[][]##
##....####
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 204 + 304 + 306

    robot_position = None

    robot_position = challenge.find_robot(warehouse_map)

    assert robot_position == (2, 2)

    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 204 + 304 + 306
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 205 + 304 + 306
    robot_position = challenge.move_robot(warehouse_map, robot_position, "^")
    assert challenge.coordinate_count(warehouse_map) == 205 + 304 + 306
    robot_position = challenge.move_robot(warehouse_map, robot_position, ">")
    assert challenge.coordinate_count(warehouse_map) == 205 + 304 + 306
    robot_position = challenge.move_robot(warehouse_map, robot_position, "v")
    # Should not move!
    assert (
        challenge.print_warehouse(warehouse_map).strip()
        == """
--- WAREHOUSE ---
##########
##...@..##
##...[].##
##..[][]##
##....####
##########
""".strip()
    )

    assert challenge.coordinate_count(warehouse_map) == 205 + 304 + 306


def test_challenge1():
    input = challenge.parse_input(
        """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()
    )

    assert challenge.process(input) == 9021


def test_challenge2():
    input = challenge.parse_input(
        """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""".strip()
    )

    assert challenge.process(input) == 618
