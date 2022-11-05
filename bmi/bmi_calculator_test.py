import bmi_calculator as cal


def test_calculate():
    assert cal.calculate(170, 65) == 22.5


def test_get_message():
    assert cal.get_message(18.4) == "LIGHT"
    assert cal.get_message(18.5) == "GOOD"
    assert cal.get_message(24) == "HEAVY"
    assert cal.get_message(27) == "FAT"
