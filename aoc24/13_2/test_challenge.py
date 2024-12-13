from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()
    )
    assert input == (
        {"Button A": (94, 34), "Button B": (22, 67), "Prize": (8400, 5400)},
        {"Button A": (26, 66), "Button B": (67, 21), "Prize": (12748, 12176)},
        {"Button A": (17, 86), "Button B": (84, 37), "Prize": (7870, 6450)},
        {"Button A": (69, 23), "Button B": (27, 71), "Prize": (18641, 10279)},
    )


def test_challenge1():
    input = challenge.parse_input(
        """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()
    )

    assert challenge.process(input) == 875318608908


def test_calculate_button_presses():
    assert challenge.calculate_button_presses({"Button A": (94, 34), "Button B": (22, 67), "Prize": (8400, 5400)}) is None
    assert challenge.calculate_button_presses({"Button A": (26, 66), "Button B": (67, 21), "Prize": (12748, 12176)}) == (118679050709, 103199174542)
    assert challenge.calculate_button_presses({"Button A": (17, 86), "Button B": (84, 37), "Prize": (7870, 6450)}) is None
    assert challenge.calculate_button_presses({"Button A": (69, 23), "Button B": (27, 71), "Prize": (18641, 10279)}) == (102851800151, 107526881786)


def test_calculate_cost():
    assert challenge.calculate_cost((118679050709, 103199174542)) == 459236326669
    assert challenge.calculate_cost(None) == 0
    assert challenge.calculate_cost((102851800151, 107526881786)) == 416082282239
