import leap_year


def test_should_true_if_was_base_by_4():
    assert leap_year.is_leap_year(1996) is True


def test_should_false_if_was_base_by_100():
    assert leap_year.is_leap_year(2100) is False


def test_should_true_if_was_base_by_400_even_its_base_by_100_also():
    assert leap_year.is_leap_year(2000) is True