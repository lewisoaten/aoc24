from collections import Counter

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

    list2_counter = Counter(list2)

    return sum(map(lambda x: x * list2_counter[x], list1))


def challenge():
    return process(tools.read_to_string("./inputs/01_1.txt"))
