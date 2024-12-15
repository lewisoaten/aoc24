from .. import tools


def try_move(warehouse_map: tuple[list[str]], move_position: tuple[int, int], direction: str, dry_run: bool = True) -> bool:
    curr_x, curr_y = move_position

    # Can just move here
    if warehouse_map[curr_y][curr_x] == ".":
        return True

    # Wall, no can do
    if warehouse_map[curr_y][curr_x] == "#":
        return False

    next_x, next_y = curr_x, curr_y
    if direction == "^":
        next_y = curr_y - 1
    elif direction == "v":
        next_y = curr_y + 1
    elif direction == "<":
        next_x = curr_x - 1
    elif direction == ">":
        next_x = curr_x + 1

    # At the end of the map, how did we get through a wall?
    if next_y < 0 or next_y >= len(warehouse_map):
        assert False
    if next_x < 0 or next_x >= len(warehouse_map[next_y]):
        assert False

    # Pallate or robot, can we push into next space?
    if direction in ("<", ">"):
        if warehouse_map[curr_y][curr_x] in ("[", "]", "@") and try_move(warehouse_map, (next_x, next_y), direction, dry_run=dry_run):
            if not dry_run:
                warehouse_map[next_y][next_x] = warehouse_map[curr_y][curr_x]
                warehouse_map[curr_y][curr_x] = "."
            return True
    elif direction in ("^", "v"):
        if warehouse_map[curr_y][curr_x] == "@" and try_move(warehouse_map, (next_x, next_y), direction, dry_run=dry_run):
            if not dry_run:
                warehouse_map[next_y][next_x] = warehouse_map[curr_y][curr_x]
                warehouse_map[curr_y][curr_x] = "."
            return True
        if (
            warehouse_map[curr_y][curr_x] == "["
            and try_move(warehouse_map, (next_x, next_y), direction, dry_run=dry_run)
            and try_move(warehouse_map, (next_x + 1, next_y), direction, dry_run=dry_run)
        ):
            if not dry_run:
                warehouse_map[next_y][next_x] = warehouse_map[curr_y][curr_x]
                warehouse_map[next_y][next_x + 1] = warehouse_map[curr_y][curr_x + 1]
                warehouse_map[curr_y][curr_x] = "."
                warehouse_map[curr_y][curr_x + 1] = "."
            return True
        if (
            warehouse_map[curr_y][curr_x] == "]"
            and try_move(warehouse_map, (next_x, next_y), direction, dry_run=dry_run)
            and try_move(warehouse_map, (next_x - 1, next_y), direction, dry_run=dry_run)
        ):
            if not dry_run:
                warehouse_map[next_y][next_x] = warehouse_map[curr_y][curr_x]
                warehouse_map[next_y][next_x - 1] = warehouse_map[curr_y][curr_x - 1]
                warehouse_map[curr_y][curr_x] = "."
                warehouse_map[curr_y][curr_x - 1] = "."
            return True

    # No move possible
    return False


def move_robot(warehouse_map: tuple[list[str]], robot_position: tuple[int, int], direction: str) -> tuple[int, int]:
    x, y = robot_position

    assert warehouse_map[y][x] == "@"  # Robot should be here

    if try_move(warehouse_map, (x, y), direction, dry_run=True):
        try_move(warehouse_map, (x, y), direction, dry_run=False)
        if direction == "^":
            return x, y - 1
        elif direction == "v":
            return x, y + 1
        elif direction == "<":
            return x - 1, y
        elif direction == ">":
            return x + 1, y
    else:
        return x, y


def print_warehouse(warehouse_map: tuple[list[str]]) -> str:
    return "\n--- WAREHOUSE ---\n" + "\n".join("".join(row) for row in warehouse_map)


def coordinate_count(warehouse_map: tuple[list[str]]) -> int:
    count = 0
    for y, row in enumerate(warehouse_map):
        for x, cell in enumerate(row):
            if cell == "[":
                count += 100 * y + x

    return count


def find_robot(warehouse_map: tuple[list[str]]) -> tuple[int, int]:
    robot_position = None

    for y, row in enumerate(warehouse_map):
        for x, cell in enumerate(row):
            if cell == "@":
                robot_position = (x, y)
                break

    assert robot_position is not None
    return robot_position


def process(input: tuple[dict[str, tuple[int, int]]]) -> int:
    warehouse_map, instructions = input

    print(f"Number of instructions: {len(instructions)}")

    robot_position = find_robot(warehouse_map)

    warehouse_string = print_warehouse(warehouse_map)
    box_count = warehouse_string.count("[]")
    wall_count = warehouse_string.count("#")

    print(warehouse_string)

    for n, instruction in enumerate(instructions):
        robot_position = move_robot(warehouse_map, robot_position, instruction)

    warehouse_string = print_warehouse(warehouse_map)
    assert box_count == warehouse_string.count("[]")
    assert wall_count == warehouse_string.count("#")
    assert warehouse_string.count("[.") == 0
    assert warehouse_string.count("[#") == 0
    assert warehouse_string.count("[[") == 0
    assert warehouse_string.count(".]") == 0
    assert warehouse_string.count("#]") == 0
    assert warehouse_string.count("]]") == 0

    print(warehouse_string)

    return coordinate_count(warehouse_map)


def enlargen_warehouse(warehouse_map: tuple[list[str]]) -> tuple[list[str]]:
    # If the tile is #, the new map contains ## instead.
    # If the tile is O, the new map contains [] instead.
    # If the tile is ., the new map contains .. instead.
    # If the tile is @, the new map contains @. instead.
    new_map = []
    for row in warehouse_map:
        new_row = []
        for cell in row:
            if cell == "#":
                new_row.append("#")
                new_row.append("#")
            elif cell == "O":
                new_row.append("[")
                new_row.append("]")
            elif cell == ".":
                new_row.append(".")
                new_row.append(".")
            elif cell == "@":
                new_row.append("@")
                new_row.append(".")
        new_map.append(new_row)
    return tuple(new_map)


# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########


# <^^>>>vv<v>>v<<
def parse_input(input: str) -> tuple[tuple[list[str]], tuple[str]]:
    warehouse_map, instructions = tools.str_to_two_sections(input)

    return enlargen_warehouse(tools.str_to_char2d(warehouse_map)), tuple(instructions.replace("\n", ""))


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/15_1.txt")))
