from collections import defaultdict
from functools import cmp_to_key

from .. import tools


def create_adjacency_list(edges: tuple[tuple[str, str]]) -> dict[str, set[str]]:
    adjacency_matrix = defaultdict(set)
    for a, b in edges:
        adjacency_matrix[a].add(b)
        adjacency_matrix[b].add(a)
    return adjacency_matrix


def find_maximal_cliques(adjacency_list: dict[str, set[str]]) -> list[list[str]]:
    def bron_kerbosch(R, P, X):
        """Recursive function for finding maximal cliques using the Bron-Kerbosch algorithm."""
        if not P and not X:
            # Found a maximal clique
            cliques.append(tuple(sorted(R)))
            return

        for v in list(P):
            bron_kerbosch(R | {v}, P & adjacency_list[v], X & adjacency_list[v])
            P.remove(v)
            X.add(v)

    # Initialize variables for the algorithm
    cliques = []
    bron_kerbosch(set(), set(adjacency_list.keys()), set())

    return sorted(cliques)


def process(input: tuple[tuple[str, str]]) -> int:
    graph = create_adjacency_list(input)

    cliques = find_maximal_cliques(graph)
    cliques = sorted(cliques, key=cmp_to_key(lambda x, y: len(y) - len(x)))

    return ",".join(sorted(cliques[0]))


def parse_input(input: str) -> tuple[tuple[str, str]]:
    edges = tools.str_to_lines(input, process_line=tools.item_split, process_line_kwargs={"separator": "-"})
    return edges


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/23_1.txt")))
