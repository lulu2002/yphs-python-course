import divination as div


def test_divination():
    assert div.calculate(1, 1) == "普通"
    assert div.calculate(1, 2) == "吉"
