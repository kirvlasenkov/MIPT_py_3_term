from itertools import permutations


def get_permutations(s, n):
    return sorted(["".join(letters) for letters in permutations(s, n)])


if __name__ == "__main__":
    print("OK" if get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"] else "NOT OK")
