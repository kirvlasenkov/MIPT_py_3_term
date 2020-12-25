from scripts.ex_6 import get_combinations


def test_permutations():
    assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]
    assert get_combinations("ab", 2) == ["a", "b", "ab"]
    assert get_combinations("", 0) == []
