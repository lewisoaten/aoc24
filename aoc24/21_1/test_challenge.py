from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
029A
980A
179A
456A
379A
""".strip()
    )
    assert input == (
        "029A",
        "980A",
        "179A",
        "456A",
        "379A",
    )


def test_find_all_shortest_paths_keypad():
    assert challenge.find_all_shortest_paths(challenge.KEYPAD_PATHS, "A", "0") == [
        ["A", "0"],
    ]

    assert challenge.find_all_shortest_paths(challenge.KEYPAD_PATHS, "A", "5") == [
        ["A", "0", "2", "5"],
        ["A", "3", "2", "5"],
        ["A", "3", "6", "5"],
    ]


def test_find_all_shortest_paths_dpad():
    assert challenge.find_all_shortest_paths(challenge.DPAD_PATHS, "A", "^") == [
        ["A", "^"],
    ]

    assert challenge.find_all_shortest_paths(challenge.DPAD_PATHS, "A", "<") == [
        ["A", "^", "v", "<"],
        ["A", ">", "v", "<"],
    ]


def test_calculate_movement1():
    assert challenge.calculate_movement("A", "0", ("keypad",)) == "<A"
    assert challenge.calculate_movement("0", "2", ("keypad",)) == "^A"
    assert challenge.calculate_movement("2", "9", ("keypad",)) == ">^^A"
    assert challenge.calculate_movement("9", "A", ("keypad",)) == "vvvA"


def test_calculate_full_movement1():
    assert challenge.calculate_full_movement("029A", ("keypad",)) == "<A^A>^^AvvvA"


def test_calculate_full_movement2():
    assert len(challenge.calculate_full_movement("029A", ("keypad", "dpad"))) == len("v<<A>>^A<A>AvA<^AA>A<vAAA>^A")


def test_calculate_full_movement3():
    assert len(challenge.calculate_full_movement("029A", ("keypad", "dpad", "dpad"))) == len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
    assert len(challenge.calculate_full_movement("980A", ("keypad", "dpad", "dpad"))) == len("<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A")
    assert len(challenge.calculate_full_movement("179A", ("keypad", "dpad", "dpad"))) == len("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")
    assert len(challenge.calculate_full_movement("456A", ("keypad", "dpad", "dpad"))) == len("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A")
    assert len(challenge.calculate_full_movement("379A", ("keypad", "dpad", "dpad"))) == len("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")


def test_challenge1():
    input = challenge.parse_input(
        """
029A
980A
179A
456A
379A
""".strip()
    )

    assert challenge.process(input) == 126384
