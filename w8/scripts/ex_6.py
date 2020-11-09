from itertools import combinations


def get_combinations(s, n):
    ans = (sorted(["".join(sorted(elem)) for i in range(1, n + 1) for elem in combinations(s, i)]))
    ans.sort(key=lambda x: len(x))
    return ans


if __name__ == "__main__":
    print("OK" if get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"] else "NOT OK")
