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


def plot_maze(maze: tuple[int, int], width: int, height: int, end: int) -> tuple[tuple[str]]:
    plot = [["." for _ in range(width)] for _ in range(height)]

    for i, byte in enumerate(maze):
        x, y = byte
        assert y < height
        assert x < width
        plot[y][x] = "#"
        if i >= end - 1:
            break

    return tuple(tuple(row) for row in plot)


def process(input: tuple[int, int], width=71, height=71, end=1024) -> int:
    maze = plot_maze(input, width, height, end)

    return find_steps(maze)


def parse_input(input: str) -> tuple[int, int]:
    maze = tools.str_to_lines(input, process_line=tools.item_split, process_line_kwargs={"separator": ",", "process_items": int})

    return maze


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/18_1.txt")))
