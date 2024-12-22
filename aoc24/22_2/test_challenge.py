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
    result = challenge.next_secret(123, 10)
    assert next(result) == 15887950
    assert next(result) == 16495136
    assert next(result) == 527345
    assert next(result) == 704524
    assert next(result) == 1553684
    assert next(result) == 12683156
    assert next(result) == 11100544
    assert next(result) == 12249484
    assert next(result) == 7753432
    assert next(result) == 5908254


def test_nth_secret():
    assert challenge.nth_secret(123, 1) == 15887950
    assert challenge.nth_secret(123, 2) == 16495136
    assert challenge.nth_secret(123, 10) == 5908254


def test_get_prices():
    assert challenge.get_prices(123, 10) == [3, 0, 6, 5, 4, 4, 6, 4, 4, 2]


def test_challenge1():
    input = challenge.parse_input(
        """
1
2
3
2024
""".strip()
    )

    assert challenge.process(input) == 23
