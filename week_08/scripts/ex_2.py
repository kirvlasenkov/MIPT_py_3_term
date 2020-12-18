def fibonacci_generator(n):
    '''
    Simple generator, producing first
    n numbers of fibonacci row

    param n: limitation (maximum amount
    of numbers)
    '''
    first = 0
    second = 1
    i = 0

    while True:
        yield first
        first, second = second, first + second
        i += 1
        if i == n:
            raise StopIteration("You're in place")


class Fibo:
    '''
    Simple realization of fibo's row
    generator
    '''

    __slots__ = ["__first", "__second", "__limitation", "__counter"]

    def __init__(self, limitation: int):
        self.__first = 0
        self.__second = 1
        self.__limitation = limitation
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter == self.__limitation:
            raise StopIteration()

        self.__counter += 1
        previous = self.__first
        self.__first, self.__second = \
            self.__second, self.__first + self.__second
        return previous


if __name__ == "__main__":
    # primitive test for fibo function
    print("via function: ")
    activated_fibo = fibonacci_generator(7)
    while True:
        try:
            print(next(activated_fibo))
        except Exception:
            break

    print("\nvia class:")
    # primitive test for fibo class
    fibo_gen = iter(Fibo(limitation=7))
    while True:
        try:
            print(next(fibo_gen))
        except Exception:
            break
