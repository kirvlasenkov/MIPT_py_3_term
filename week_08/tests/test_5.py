from scripts.ex_5 import get_permutations


def test_permutations():
    assert get_permutations("ba", 2) == ["ab", "ba"]
    assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]
    assert get_permutations("abcd", 1) == ["a", "b", "c", "d"]
    assert get_permutations("", 0) == [""]