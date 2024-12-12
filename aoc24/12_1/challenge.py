from .. import tools


def expand_plot(map: tuple[list[str]], x: int, y: int, plant: str, plot: list[tuple[int, int]]) -> set[tuple[int, int]]:
    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return plot
    if (x, y) in plot:
        return plot
    if map[y][x] == plant:
        plot.add((x, y))
        plot = expand_plot(map, x - 1, y, plant, plot)
        plot = expand_plot(map, x + 1, y, plant, plot)
        plot = expand_plot(map, x, y - 1, plant, plot)
        plot = expand_plot(map, x, y + 1, plant, plot)
    return plot


def plot_perimiter(plot: set[tuple[int, int]]) -> int:
    # Find perimeter size for plot coordinates
    perimeter = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in plot:
        for dx, dy in directions:
            if (x + dx, y + dy) not in plot:
                perimeter += 1

    return perimeter


def plot_price(perimeter: int, plot_size: int) -> int:
    # Calculate price for plot
    return perimeter * plot_size


def process(input: tuple[list[str]]) -> int:
    visited = set()

    total_price = 0

    for y, row in enumerate(input):
        for x, value in enumerate(row):
            if (x, y) not in visited:
                plot = expand_plot(input, x, y, value, set())
                visited.update(plot)

                total_price += plot_price(plot_perimiter(plot), len(plot))

    return total_price


def parse_input(input: str) -> tuple[list[str]]:
    return tools.str_to_char2d(input)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/12_1.txt")))
