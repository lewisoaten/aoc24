import heapq
from enum import IntEnum

from .. import tools


class Direction(IntEnum):
    East = 0
    South = 1
    West = 2
    North = 3


def create_maze_graph(maze: tuple[list[str]], graph: dict[tuple[int, int, Direction], dict[tuple[int, int, Direction], int]], position: tuple[int, int, Direction]):
    directions = [Direction.East, Direction.South, Direction.West, Direction.North]

    queue = [position]

    while queue:
        position = queue.pop(0)
        if position not in graph:
            graph[position] = {}

        for next_direction in directions:
            if next_direction == position[2]:
                # Already facing this direction
                if next_direction == Direction.East:
                    next_position = (position[0] + 1, position[1], Direction.East)
                elif next_direction == Direction.South:
                    next_position = (position[0], position[1] + 1, Direction.South)
                elif next_direction == Direction.West:
                    next_position = (position[0] - 1, position[1], Direction.West)
                elif next_direction == Direction.North:
                    next_position = (position[0], position[1] - 1, Direction.North)

            else:
                # Turn
                if next_direction == Direction.East:
                    if position[2] == Direction.West:
                        # Can't turn 180 degrees
                        continue
                    next_position = (position[0], position[1], Direction.East)
                elif next_direction == Direction.South:
                    if position[2] == Direction.North:
                        # Can't turn 180 degrees
                        continue
                    next_position = (position[0], position[1], Direction.South)
                elif next_direction == Direction.West:
                    if position[2] == Direction.East:
                        # Can't turn 180 degrees
                        continue
                    next_position = (position[0], position[1], Direction.West)
                elif next_direction == Direction.North:
                    if position[2] == Direction.South:
                        # Can't turn 180 degrees
                        continue
                    next_position = (position[0], position[1], Direction.North)

            if next_position[0] < 0 or next_position[0] >= len(maze[0]) or next_position[1] < 0 or next_position[1] >= len(maze):
                # Out of maze bounds
                continue

            if maze[next_position[1]][next_position[0]] == "#":
                # Wall
                continue

            if next_position in graph[position]:
                # Already visited from this location
                continue

            if next_position[2] == position[2]:
                # Same direction
                graph[position][next_position] = 1
            else:
                # Turn
                graph[position][next_position] = 1000

            if next_position not in graph:
                queue.append((next_position[0], next_position[1], next_direction))

    return graph


def find_position(maze: tuple[list[str]], symbol: str) -> tuple[int, int]:
    position = None

    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == symbol:
                position = (x, y)
                break

    return position


def find_shortest_route_cost(graph: dict[tuple[int, int, Direction], dict[tuple[int, int, Direction], int]], start: tuple[int, int, Direction], end: tuple[int, int]) -> int:
    start_node = (start[0], start[1], Direction.East)

    queue = [(0, start_node)]
    distances = {start_node: 0}
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if (current_node[0], current_node[1]) == (end[0], end[1]):
            return current_distance

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return float("inf")


def process(input: tuple[list[str]]) -> int:
    start = find_position(input, "S")
    end = find_position(input, "E")

    graph = create_maze_graph(input, {}, (start[0], start[1], Direction.East))

    return find_shortest_route_cost(graph, start, end)


def parse_input(input: str) -> tuple[list[str]]:
    maze = tools.str_to_char2d(input)

    return maze


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/16_1.txt")))
