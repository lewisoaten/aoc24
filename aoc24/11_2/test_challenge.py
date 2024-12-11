from . import challenge


def test_parse_input1():
    input = challenge.parse_input("0 1 10 99 999")
    assert input == [0, 1, 10, 99, 999]


def test_challenge1():
    input = challenge.parse_input("0 1 10 99 999")

    assert challenge.process(input, 1) == 7


def test_challenge2():
    input = challenge.parse_input("125 17")

    assert challenge.process(input, 1) == 3
    assert challenge.process(input, 2) == 4
    assert challenge.process(input, 3) == 5
    assert challenge.process(input, 4) == 9
    assert challenge.process(input, 5) == 13
    assert challenge.process(input, 6) == 22
    assert challenge.process(input, 25) == 55312
