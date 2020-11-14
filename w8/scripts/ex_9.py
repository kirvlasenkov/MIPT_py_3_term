from itertools import accumulate


def maximize(lists, m):
    list_of_max_squared = [max(lst) ** 2 for lst in lists]
    maxim = list(accumulate(list_of_max_squared))[-1]
    return maxim % m


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]

if __name__ == "__main__":
    print("OK" if maximize(lists, m=1000) == 206 else "NOT OK")
