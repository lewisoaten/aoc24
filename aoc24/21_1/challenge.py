from collections import defaultdict
from collections import deque

from .. import tools

KEYPAD_PATHS = {
    "A": ["0", "3"],
    "0": ["A", "2"],
    "1": ["2", "4"],
    "2": ["0", "3", "5", "1"],
    "3": ["A", "2", "6"],
    "4": ["1", "5", "7"],
    "5": ["2", "4", "6", "8"],
    "6": ["3", "5", "9"],
    "7": ["4", "8"],
    "8": ["5", "7", "9"],
    "9": ["6", "8"],
}

KEYPAD_DIRS = {
    ("A", "0"): "<",
    ("A", "3"): "^",
    ("0", "A"): ">",
    ("0", "2"): "^",
    ("1", "2"): ">",
    ("1", "4"): "^",
    ("2", "0"): "v",
    ("2", "3"): ">",
    ("2", "5"): "^",
    ("2", "1"): "<",
    ("3", "A"): "v",
    ("3", "2"): "<",
    ("3", "6"): "^",
    ("4", "1"): "v",
    ("4", "5"): ">",
    ("4", "7"): "^",
    ("5", "2"): "v",
    ("5", "4"): "<",
    ("5", "6"): ">",
    ("5", "8"): "^",
    ("6", "3"): "v",
    ("6", "5"): "<",
    ("6", "9"): "^",
    ("7", "4"): "v",
    ("7", "8"): ">",
    ("8", "5"): "v",
    ("8", "7"): "<",
    ("8", "9"): ">",
    ("9", "6"): "v",
    ("9", "8"): "<",
}

DPAD_PATHS = {
    "A": [
        "^",
        ">",
    ],
    ">": [
        "A",
        "v",
    ],
    "^": [
        "A",
        "v",
    ],
    "v": ["<", "^", ">"],
    "<": ["v"],
}

DPAD_DIRS = {
    ("A", "^"): "<",
    ("A", ">"): "v",
    (">", "A"): "^",
    (">", "v"): "<",
    ("^", "A"): ">",
    ("^", "v"): "v",
    ("v", "<"): "<",
    ("v", "^"): "^",
    ("v", ">"): ">",
    ("<", "v"): ">",
}

GRAPHS = {
    "keypad": KEYPAD_PATHS,
    "dpad": DPAD_PATHS,
}

DIRS = {
    "keypad": KEYPAD_DIRS,
    "dpad": DPAD_DIRS,
}


def find_all_shortest_paths(graph, start, end):
    if start not in graph or end not in graph:
        return []

    # Queue for BFS: stores (current_node, path_so_far)
    queue = deque([(start, [start])])
    shortest_paths = []
    visited_levels = defaultdict(lambda: float("inf"))

    while queue:
        current_node, path = queue.popleft()

        # If we've found the target node
        if current_node == end:
            if not shortest_paths or len(path) == len(shortest_paths[0]):
                shortest_paths.append(path)
            elif len(path) < len(shortest_paths[0]):
                shortest_paths = [path]
            continue

        # Explore neighbors
        for neighbor in graph[current_node]:
            if len(path) + 1 <= visited_levels[neighbor]:
                visited_levels[neighbor] = len(path) + 1
                queue.append((neighbor, path + [neighbor]))

    return shortest_paths


def calculate_movement(start: str, end: str, graphs: tuple[str]) -> str:
    print(f"Calculating movement from {start} to {end} with graphs {graphs}")
    graph = GRAPHS[graphs[0]]
    dirs = DIRS[graphs[0]]

    print(f"    finding all shortest paths from {start} to {end} in {graphs[0]}")
    paths = find_all_shortest_paths(graph, start, end)
    print(f"    shorest paths: {paths}")

    remaining_graphs = graphs[1:]

    controlled_paths = []

    for path in paths:
        print(f"    Path: {path}")
        path_movement = "".join(map(lambda x: dirs[(x[0], x[1])], zip(path, path[1:]))) + "A"
        print(f"    Path movement: {path_movement}")

        if len(remaining_graphs) > 0:
            path_movement = tuple("A" + path_movement)
            controlled_paths.append("".join(map(lambda x: calculate_movement(x[0], x[1], remaining_graphs), zip(path_movement, path_movement[1:]))))
        else:
            controlled_paths.append("".join(path_movement))

    return min(controlled_paths, key=len)


def calculate_code_complexity(code: str, keypresses: str):
    sequence_length = len(keypresses)
    numeric_code = int("".join(filter(str.isdigit, code)))
    return sequence_length * numeric_code


def calculate_full_movement(keypresses: str, graphs: tuple[str]) -> str:
    keypresses = "A" + keypresses
    return "".join(map(lambda x: calculate_movement(x[0], x[1], graphs), zip(keypresses, keypresses[1:])))


def process(input: tuple[str]) -> int:
    sum_of_complexity = 0
    for code in input:
        keypresses = calculate_full_movement(code, ("keypad", "dpad", "dpad"))
        sum_of_complexity += calculate_code_complexity(code, keypresses)
    return sum_of_complexity


def parse_input(input: str) -> tuple[str]:
    codes = tools.str_to_lines(input)

    return codes


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/21_1.txt")))
