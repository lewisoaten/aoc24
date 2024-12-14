from .. import tools

GRID_MAX = (101, 103)
# GRID_MAX = (11, 7)


def recalculate_position(robot: dict[str, tuple[int]], time: int, grid_max=GRID_MAX) -> tuple[int, int]:
    old_x, old_y = robot["p"]
    vx, vy = robot["v"]
    max_x, max_y = grid_max

    new_x = (old_x + vx * time) % max_x
    new_y = (old_y + vy * time) % max_y
    return new_x, new_y


def calculate_safety_factor(robots: tuple[dict[str, tuple[int, int]]], grid_max=GRID_MAX) -> int:
    mid_width = grid_max[0] // 2
    mid_height = grid_max[1] // 2

    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0

    for robot in robots:
        x, y = robot["p"]
        if x < mid_width and y < mid_height:
            top_left += 1
        if x > mid_width and y < mid_height:
            top_right += 1
        if x < mid_width and y > mid_height:
            bottom_left += 1
        if x > mid_width and y > mid_height:
            bottom_right += 1

    return top_left * top_right * bottom_left * bottom_right


def print_tile(robots: tuple[dict[str, tuple[int, int]]], grid_max=GRID_MAX, quadrants=False, positions=False) -> str:
    mid_col = grid_max[0] // 2
    mid_row = grid_max[1] // 2

    grid = [[0 for _ in range(grid_max[0])] for _ in range(grid_max[1])]
    image = [["." for _ in range(grid_max[0])] for _ in range(grid_max[1])]

    for robot in robots:
        x, y = robot["p"]
        grid[y][x] += 1

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if quadrants and (x == mid_col or y == mid_row):
                image[y][x] = " "
            elif positions:
                image[y][x] = "#" if col > 0 else "."
            else:
                image[y][x] = str(col) if col > 0 else "."

    return "\n".join("".join(row) for row in image)


def process(input: tuple[dict[str, tuple[int, int]]], grid_max=GRID_MAX) -> int:
    iterations = 0
    while True:
        iterations += 1
        robots = tuple(map(lambda robot: {"p": recalculate_position(robot, iterations, grid_max=grid_max), "v": robot["v"]}, input))
        bathroom = print_tile(robots, grid_max=grid_max, positions=True)
        if "#######" in bathroom:
            break

    print("--- TILE ---")
    print(print_tile(robots, grid_max=grid_max, positions=True))
    return iterations


def parse_input(input: str) -> tuple[dict[str, tuple[int, int]]]:

    def process_line(line: str) -> dict[str, tuple[int, int]]:
        position, velocity = line.split(" ", 1)
        return {
            "p": tools.item_split(position[2:], ",", process_items=int),
            "v": tools.item_split(velocity[2:], ",", process_items=int),
        }

    return tools.str_to_lines(input, process_line=process_line)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/14_1.txt")))
