from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    return sorted("".join(sorted(letters)) for letters in combinations_with_replacement(s, n))


if __name__ == "__main__":
    print("OK" if get_combinations_with_r("cat", 2) == ["aa", "ac", "at", "cc", "ct", "tt"] else "NOT OK")
