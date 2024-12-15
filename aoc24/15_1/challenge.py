from .. import tools


def try_move(warehouse_map: tuple[list[str]], move_position: tuple[int, int], direction: str) -> bool:
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
    if warehouse_map[curr_y][curr_x] in ("O", "@") and try_move(warehouse_map, (next_x, next_y), direction):
        warehouse_map[next_y][next_x] = warehouse_map[curr_y][curr_x]
        warehouse_map[curr_y][curr_x] = "."
        return True

    # No move possible
    return False


def move_robot(warehouse_map: tuple[list[str]], robot_position: tuple[int, int], direction: str) -> tuple[int, int]:
    x, y = robot_position

    assert warehouse_map[y][x] == "@"  # Robot should be here

    if try_move(warehouse_map, (x, y), direction):
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
            if cell == "O":
                count += 100 * y + x

    return count


def process(input: tuple[dict[str, tuple[int, int]]]) -> int:
    warehouse_map, instructions = input

    robot_position = None

    for y, row in enumerate(warehouse_map):
        for x, cell in enumerate(row):
            if cell == "@":
                robot_position = (x, y)
                break

    print(print_warehouse(warehouse_map))

    for instruction in instructions:
        robot_position = move_robot(warehouse_map, robot_position, instruction)

    print(print_warehouse(warehouse_map))

    return coordinate_count(warehouse_map)


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

    def process_line(line: str) -> dict[str, tuple[int, int]]:
        position, velocity = line.split(" ", 1)
        return {
            "p": tools.item_split(position[2:], ",", process_items=int),
            "v": tools.item_split(velocity[2:], ",", process_items=int),
        }

    warehouse_map, instructions = tools.str_to_two_sections(input)

    return tools.str_to_char2d(warehouse_map), tuple(instructions.replace("\n", ""))


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/15_1.txt")))
