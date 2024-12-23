from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
kh-tc
qp-kh
de-cg
ka-co
""".strip()
    )
    assert input == (
        ("kh", "tc"),
        ("qp", "kh"),
        ("de", "cg"),
        ("ka", "co"),
    )


def test_find_triangular_communities1():
    input = challenge.parse_input(
        """
de-ta
ka-de
ta-ka
""".strip()
    )
    assert challenge.find_triangular_communities(input) == [("de", "ka", "ta")]


def test_challenge1():
    input = challenge.parse_input(
        """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()
    )

    assert challenge.process(input) == 7
