# own realization of map()
from typing import List, Any


def my_map(function, iterable):
    for item in iterable:
        yield function(item)


def my_enumerate(seq):
    ind = 0
    for item in seq:
        yield ind, item
        ind += 1


def my_zip(*iterables):
    list_of_iterables = [iter(iterable) for iterable in iterables]

    while True:
        iteration: List[int] = []
        try:
            for activated_iterable in list_of_iterables:
                iteration.append(next(activated_iterable))
            yield tuple(iteration)
        except Exception:
            break


if __name__ == "__main__":
    print("Result for map: ")
    for i in my_map(lambda x: x ** 2, [1, 2, 3, 4, 5]):
        print(i)

    print("\nResult for enumerate: ")
    for ind, i in my_enumerate([1, 2, 3, 4, 5]):
        print(f"ind - {ind}; element - {i}")

    print("\nResult for zip: ")
    for i, j, k in my_zip([1, 2, 3, 4], [2, 4, 5, 6], [35, 35, 45]):
        print(i, j, k, sep='    ')
