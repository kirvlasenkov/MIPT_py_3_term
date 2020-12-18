from scripts.ex_9 import maximize


def test_maximize():
    assert maximize([
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ], 1000) == 206

    assert maximize([[1]], 1) == 0
