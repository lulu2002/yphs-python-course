import make_changes


def test_make_change():
    assert make_changes.make_change(1000, 900, [100]) == [{
        "type": 100,
        "amount": 1
    }]
