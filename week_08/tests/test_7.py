from scripts.ex_7 import get_combinations_with_r


def test_combination_with_r():
    assert get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"]
    assert get_combinations_with_r("ca", 2) == ["aa", "ac", "cc"]
    assert get_combinations_with_r("", 1) == []