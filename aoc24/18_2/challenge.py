from collections import deque

from .. import tools


def find_steps(maze: tuple[tuple[str]]) -> int:
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    if maze[0][0] == "#" or maze[rows - 1][cols - 1] == "#":
        return -1

    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = set()
    visited.add((0, 0))

    while queue:
        r, c, steps = queue.popleft()

        if (r, c) == (rows - 1, cols - 1):
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == "." and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))

    return -1  # No path found


def add_byte(maze: list[list[str]], byte: tuple[int, int], width: int, height: int) -> list[int]:
    x, y = byte
    assert y < height
    assert x < width
    maze[y][x] = "#"


def plot_maze(maze: tuple[int, int], width: int, height: int, end: int) -> list[list[str]]:
    plot = [["." for _ in range(width)] for _ in range(height)]

    for i, byte in enumerate(maze):
        add_byte(plot, byte, width, height)
        if i >= end - 1:
            break

    return list(list(row) for row in plot)


def process(input: tuple[int, int], width=71, height=71, end=1024) -> str:
    maze = plot_maze(input, width, height, end)
    assert find_steps(maze) != -1

    for byte in input[end:]:
        add_byte(maze, byte, width, height)

        if find_steps(maze) == -1:
            return f"{byte[0]},{byte[1]}"

    return None


def parse_input(input: str) -> tuple[int, int]:
    maze = tools.str_to_lines(input, process_line=tools.item_split, process_line_kwargs={"separator": ",", "process_items": int})

    return maze


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/18_1.txt")))
