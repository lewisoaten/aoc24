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


def test_find_maximal_cliques1():
    input = challenge.parse_input(
        """
de-ta
ka-de
ta-ka
""".strip()
    )

    adj = challenge.create_adjacency_list(input)
    assert challenge.find_maximal_cliques(adj) == [("de", "ka", "ta")]


def test_find_maximal_cliques2():
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

    adj = challenge.create_adjacency_list(input)
    assert challenge.find_maximal_cliques(adj) == [
        ("aq", "cg", "yn"),
        ("aq", "vc", "wq"),
        ("cg", "de"),
        ("cg", "tb"),
        ("co", "de", "ka", "ta"),
        ("co", "tc"),
        ("ka", "tb"),
        ("kh", "qp", "ub"),
        ("kh", "ta"),
        ("kh", "tc"),
        ("qp", "td", "wh"),
        ("tb", "vc", "wq"),
        ("tc", "td", "wh"),
        ("td", "wh", "yn"),
        ("ub", "vc", "wq"),
    ]


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

    assert challenge.process(input) == "co,de,ka,ta"
