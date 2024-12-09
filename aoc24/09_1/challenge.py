from copy import deepcopy

from .. import tools


def init_disk(disk_map: tuple[int]) -> list[int]:
    disk = []
    is_file = True
    file_id = 0

    for map_item in disk_map:
        if is_file:
            disk.extend([file_id] * map_item)
            file_id += 1
        else:
            disk.extend([None] * map_item)

        is_file = not is_file

    return disk


def checksum(disk: list[int]) -> int:
    disk = list(filter(lambda x: x is not None, disk))
    disk = list(zip(disk, range(len(disk))))
    disk = map(lambda x: x[0] * x[1], disk)
    return sum(disk)


def compact(disk: list[int]) -> list[int]:
    disk = deepcopy(disk)
    pointer_start = 0
    pointer_end = len(disk) - 1

    while pointer_start < pointer_end:
        if disk[pointer_start] is None:
            while disk[pointer_end] is None:
                pointer_end -= 1
            disk[pointer_start], disk[pointer_end] = disk[pointer_end], disk[pointer_start]
            pointer_end -= 1

        pointer_start += 1

    return disk


def process(input: tuple[int]):
    disk = init_disk(input)

    disk = compact(disk)

    return checksum(disk)


def parse_input(input: str) -> tuple[int]:
    return tools.str_to_int1d(input)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/09_1.txt")))
