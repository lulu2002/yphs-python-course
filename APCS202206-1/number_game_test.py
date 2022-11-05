import number_game as ng


def test_calculate():
    assert ng.calculate(6, 6, 6) == [3, 6]
    assert ng.calculate(7, 9, 7) == [2, 9, 7]
    assert ng.calculate(4, 1, 8) == [1, 8, 4, 1]
