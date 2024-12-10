from .. import tools


def check_next_point(
    topo_map_graph: dict[tuple[int, int, int], list[tuple[int, int, int, int]]],
    start: tuple[int, int, int],
    visited: list[tuple[int, int, int]],
    all_routes: list[list[tuple[int, int, int]]],
) -> list[tuple[int, int, int]]:
    visited.append(start)
    if start in topo_map_graph:
        for vertex in topo_map_graph[start[0:3]]:
            vertex = vertex[0:3]
            if vertex not in visited:
                check_next_point(topo_map_graph, vertex, visited.copy(), all_routes)
        all_routes.append(visited)


def count_trailheads(topo_map_graph: dict[tuple[int, int, int], list[tuple[int, int, int, int]]], trailhead: tuple[int, int, int]) -> int:
    routes = [[]]
    check_next_point(topo_map_graph, trailhead, [], routes)

    reachable_end_points = set()
    for route in routes:
        reachable_end_points.update(filter(lambda a: a[2] == 9, route))

    return len(reachable_end_points)


def process(topo_map_graph: dict[tuple[int, int, int], list[tuple[int, int, int, int]]]):
    total_trailheads = 0

    for point in topo_map_graph:
        if point[2] == 0:
            total_trailheads += count_trailheads(topo_map_graph, point)

    return total_trailheads


def parse_input(input: str) -> dict[tuple[int, int, int], list[tuple[int, int, int, int]]]:
    topo_map = tools.str_to_2d(input, lambda point: int(point) if point != "." else None)
    return tools.graph_from_2d(topo_map, lambda a, b: 0 if type(a) is int and type(b) is int and int(b) - int(a) == 1 else None)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/10_1.txt")))
