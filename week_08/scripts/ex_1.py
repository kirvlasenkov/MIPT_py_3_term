def print_map(function, iterable):
    mapped_container = iter(map(function, iterable))
    while True:
        try:
            print(next(mapped_container))
        except StopIteration:
            break

if __name__ == "__main__":
    print_map(lambda x: x ** 2, [1, 2, 3, 4, 5])
