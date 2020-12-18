from itertools import product


def get_cartesian_product(a, b):
    ans = []
    for elem in product(a, b):
        ans.append(elem)

    # by the way: returning of list(product(...)) also will lead to the desired result
    return ans


if __name__ == "__main__":
    print("OK" if get_cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)] else "NOT OK")
