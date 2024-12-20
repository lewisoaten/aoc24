from collections import defaultdict
from collections import deque
from copy import deepcopy

from .. import tools


def find_path(maze: tuple[list[str]], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    if maze[start[1]][start[0]] == "#" or maze[end[1]][end[0]] == "#":
        return -1

    queue = deque([(start, [start])])  # ((x,y), [steps], collision_disabled_time)

    while queue:
        pos, steps = queue.popleft()
        c, r = pos

        if (c, r) == end:
            return steps

        for dr, dc in directions:
            new_pos = c + dc, r + dr

            if 0 <= new_pos[1] < rows and 0 <= new_pos[0] < cols and new_pos not in steps and maze[new_pos[1]][new_pos[0]] in (".", "S", "E"):
                queue.append((new_pos, steps + [new_pos]))

    return []


def find_position(maze: tuple[list[str]], symbol: str) -> tuple[int, int]:
    position = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == symbol:
                position = (x, y)
                break

    return position


def print_maze(maze: tuple[list[str]], route: list[tuple[int, int]] = []):
    local_maze = deepcopy(maze)
    for x, y in route:
        local_maze[y][x] = "O"
    print(tools.char2d_to_str(local_maze))


def find_single_thickness_wall(pos: tuple[int, int], maze: tuple[list[str]]) -> dict[tuple[int, int], list[tuple[int, int]]]:
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]  # Right, Down, Left, Up
    mid_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    rows, cols = len(maze), len(maze[0])
    c, r = pos

    single_thickness_walls = defaultdict(list)

    for i, direction in enumerate(directions):
        dr, dc = direction
        new_pos = c + dc, r + dr
        if 0 <= new_pos[1] < rows and 0 <= new_pos[0] < cols and maze[new_pos[1]][new_pos[0]] in (".", "S", "E"):
            mid_dr, mid_dc = mid_direction[i]
            new_mid = c + mid_dc, r + mid_dr
            if maze[new_mid[1]][new_mid[0]] == "#":
                single_thickness_walls[pos].append(new_pos)

    return single_thickness_walls


def process(input: tuple[list[str]], save_picoseconds=100) -> int:
    start = find_position(input, "S")
    end = find_position(input, "E")

    route = find_path(input, start, end)
    route_length = len(route)

    single_thickness_walls = {}
    for pos in route:
        single_thickness_walls |= find_single_thickness_wall(pos, input)

    cheats = defaultdict(int)

    for start, ends in single_thickness_walls.items():
        before = route.index(start) + 1
        for end in ends:
            remaining = len(route) - route.index(end) + 1
            if before + remaining + save_picoseconds <= route_length:
                cheats[before + remaining] += 1

    return sum(cheats.values())


def parse_input(input: str) -> tuple[list[str]]:
    maze = tools.str_to_char2d(input)

    return maze


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/20_1.txt")))
