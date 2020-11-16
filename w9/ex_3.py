import numpy as np


class Var(Exception):
    pass


class Mean(Exception):
    pass


class Len(Exception):
    pass


class DataReceiver:
    def __init__(self, activated: bool = False):
        self.activated = activated
        if self.activated:
            self.__data = []

    def catch_signal(self, *data):
        self.__data.append(data)

    @property
    def data(self):
        return self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def mean(self):
        return np.mean(self.__data)

    def var(self):
        return np.var(self.__data)

    def __len__(self):
        return len(self.__data)


def coroutine(func):
    def wrapper(*args, **kwargs):
        cor = func(*args, **kwargs)
        cor.send(None)
        return cor

    return wrapper


@coroutine
def signal_coroutine():
    receiver = DataReceiver(activated=True)
    while True:
        try:
            signal = yield
            receiver.catch_signal(signal)
        except Var:
            yield receiver.var()
        except Mean:
            yield receiver.mean()
        except Len:
            yield len(receiver)


if __name__ == "__main__":
    activated_coroutine = signal_coroutine()
    for i, j in zip(range(5), range(20, 25)):
        activated_coroutine.send([i, j])
        if i % 3 == 0:
            print(f"Mean for step {i}: ", activated_coroutine.throw(Mean))
        elif i % 3 == 1:
            print(f"Length for step {i}: ", activated_coroutine.throw(Len))
        elif i % 3 == 2:
            print(f"Variance for step {i}: ", activated_coroutine.throw(Var))

        print("\n")
