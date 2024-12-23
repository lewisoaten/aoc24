from .. import tools


def find_triangular_communities(edges: tuple[tuple[str, str]]) -> list[tuple[str, str, str]]:
    edges = sorted(edges)

    triangles = set()
    for i in range(0, len(edges)):
        for j in range(i + 1, len(edges)):
            node1 = edges[i]
            node2 = edges[j]
            if node1[0] == node2[0]:
                if (node1[1], node2[1]) in edges or (node2[1], node1[1]) in edges:
                    triangles.add(tuple(sorted((node1[0], node1[1], node2[1]))))
            elif node1[0] == node2[1]:
                if (node1[1], node2[0]) in edges or (node2[0], node1[1]) in edges:
                    triangles.add(tuple(sorted((node1[0], node1[1], node2[0]))))

    return sorted(triangles)


def process(input: tuple[tuple[str, str]]) -> int:
    triangular_communities = find_triangular_communities(input)
    return sum(map(lambda x: 1 if "t" in (x[0][0], x[1][0], x[2][0]) else 0, triangular_communities))


def parse_input(input: str) -> tuple[tuple[str, str]]:
    edges = tools.str_to_lines(input, process_line=tools.item_split, process_line_kwargs={"separator": "-"})
    return edges


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/23_1.txt")))
