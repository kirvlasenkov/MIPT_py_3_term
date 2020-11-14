from itertools import groupby


def compress_string(s):
    keys = []
    groups = []
    for key, group in groupby(s):
        keys.append(int(key))
        groups.append(len(list(group)))

    # print(keys, groups)
    return list(zip(groups, keys))


if __name__ == "__main__":
    # print(compress_string("111132222111132323"))
    print("OK" if compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)] else "NOT OK")
