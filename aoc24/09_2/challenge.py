from copy import deepcopy

from .. import tools


def init_disk_index(disk_map: tuple[int]) -> list[tuple[int, int]]:
    disk = []
    is_file = True
    file_id = 0

    for map_item in disk_map:
        if is_file:
            disk.append((file_id, map_item, False))
            file_id += 1
        else:
            disk.append((None, map_item, False))

        is_file = not is_file

    return disk


def init_disk(disk_index: list[tuple[int, int]]) -> list[int]:
    disk = []

    for file_id, map_item, _ in disk_index:
        if file_id is not None:
            disk.extend([file_id] * map_item)
        else:
            disk.extend([None] * map_item)

    return disk


def checksum(disk: list[int]) -> int:
    disk = list(zip(disk, range(len(disk))))
    disk = list(filter(lambda x: x[0] is not None, disk))
    disk = map(lambda x: x[0] * x[1], disk)
    return sum(disk)


def compact(disk_index: list[tuple[int, int]]) -> list[tuple[int, int]]:
    disk_index = deepcopy(disk_index)
    file_index = len(disk_index) - 1
    while file_index > 0:
        # print(f"file_index: {file_index}")
        if disk_index[file_index][0] is not None and disk_index[file_index][2] is False:
            # Data to defragment
            for space_index in range(file_index):
                if disk_index[space_index][0] is not None:
                    # File, not empty space
                    continue

                if disk_index[file_index][1] == disk_index[space_index][1]:
                    # Same size
                    disk_index[space_index] = (disk_index[file_index][0], disk_index[file_index][1], True)
                    disk_index[file_index] = (None, disk_index[file_index][1], False)
                    break

                if disk_index[file_index][1] < disk_index[space_index][1]:
                    disk_index[space_index] = (None, disk_index[space_index][1] - disk_index[file_index][1], False)
                    file_to_insert = (disk_index[file_index][0], disk_index[file_index][1], True)
                    disk_index[file_index] = (None, disk_index[file_index][1], False)
                    disk_index.insert(space_index, file_to_insert)
                    file_index += 1
                    break
        file_index -= 1
    return disk_index


def process(input: tuple[int]):
    disk_index = init_disk_index(input)
    size_before_compact = len(init_disk(disk_index))

    disk_index = compact(disk_index)

    disk = init_disk(disk_index)
    size_after_compact = len(disk)
    print(f"size_before_compact: {size_before_compact}")
    print(f"size_after_compact: {size_after_compact}")

    return checksum(disk)


def parse_input(input: str) -> tuple[int]:
    return tools.str_to_int1d(input)


def challenge():
    return process(parse_input(tools.read_to_string("./inputs/09_1.txt")))
