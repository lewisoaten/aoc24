from . import challenge


def test_parse_input1():
    input = challenge.parse_input(
        """
1
10
100
2024
""".strip()
    )
    assert input == (
        1,
        10,
        100,
        2024,
    )


def test_next_secret():
    result = 123
    assert (result := challenge.next_secret(result)) == 15887950
    assert (result := challenge.next_secret(result)) == 16495136
    assert (result := challenge.next_secret(result)) == 527345
    assert (result := challenge.next_secret(result)) == 704524
    assert (result := challenge.next_secret(result)) == 1553684
    assert (result := challenge.next_secret(result)) == 12683156
    assert (result := challenge.next_secret(result)) == 11100544
    assert (result := challenge.next_secret(result)) == 12249484
    assert (result := challenge.next_secret(result)) == 7753432
    assert (result := challenge.next_secret(result)) == 5908254


def test_nth_secret():
    assert challenge.nth_secret(123, 1) == 15887950
    assert challenge.nth_secret(123, 10) == 5908254


def test_challenge1():
    input = challenge.parse_input(
        """
1
10
100
2024
""".strip()
    )

    assert challenge.process(input) == 37327623
