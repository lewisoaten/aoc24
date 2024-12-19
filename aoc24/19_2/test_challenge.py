from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()
    )
    assert input == (
        ("r", "wr", "b", "g", "bwu", "rb", "gb", "br"),
        (
            "brwrr",
            "bggr",
            "gbbr",
            "rrbgbr",
            "ubwu",
            "bwurrg",
            "brgr",
            "bbrgwb",
        ),
    )


def test_challenge1():
    input = challenge.parse_input(
        """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()
    )

    assert challenge.process(input) == 16
