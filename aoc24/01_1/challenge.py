from .. import tools


def process(input: str):
    list1 = []
    list2 = []

    for line in input.splitlines():
        values = line.split()
        assert len(values) == 2

        list1.append(int(values[0]))
        list2.append(int(values[1]))

    assert len(list1) == len(list2)

    list1.sort()
    list2.sort()

    combined = zip(list1, list2)

    total_distance = 0

    for a, b in combined:
        total_distance += abs(a - b)

    return total_distance


def challenge():
    return process(tools.read_to_string("./inputs/01_1.txt"))
