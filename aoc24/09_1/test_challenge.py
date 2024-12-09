from . import challenge


def test_challenge():
    input = challenge.parse_input("2333133121414131402")

    assert challenge.process(input) == 1928


def test_init_disk():
    input = challenge.parse_input("2333133121414131402")

    assert challenge.init_disk(input) == [
        0,
        0,
        None,
        None,
        None,
        1,
        1,
        1,
        None,
        None,
        None,
        2,
        None,
        None,
        None,
        3,
        3,
        3,
        None,
        4,
        4,
        None,
        5,
        5,
        5,
        5,
        None,
        6,
        6,
        6,
        6,
        None,
        7,
        7,
        7,
        None,
        8,
        8,
        8,
        8,
        9,
        9,
    ]


def test_checksum():
    disk = [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    assert challenge.checksum(disk) == 1928
