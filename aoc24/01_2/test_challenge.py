from . import challenge


def test_challenge():
    input = """
3   4
4   3
2   5
1   3
3   9
3   3""".strip()
    assert challenge.process(input) == 31
