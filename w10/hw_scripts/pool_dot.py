from multiprocessing import Pool
from matplotlib import pylab as plt
import time
import random
from numpy import mean

from my_mathematics.linear_algebra import MyVector


def chunk_dot(left_chunk, right_chunk):
    assert len(left_chunk) == len(right_chunk)

    return (MyVector(len(left_chunk), *left_chunk) * MyVector(len(right_chunk), *right_chunk))


def split_array(arr, pieces_number):
    """
    >>> split_array([1, 2, 3, 4], 2)
    >>> [1, 2], [3, 4]
    """
    step = len(arr) // pieces_number
    i = 0
    while i < pieces_number - 1:
        yield arr[step * i:step * (i + 1)]
        i += 1
    yield arr[step * i:]


def dot_product(lhs: MyVector, rhs: MyVector, worker_num):
    with Pool(processes=worker_num) as pool:
        start = time.time()
        result = sum(pool.apply(chunk_dot, (left_chunk, right_chunk)) for left_chunk, right_chunk in
                     zip(split_array(lhs.args_as_np, worker_num),
                         split_array(rhs.args_as_np, worker_num)))
        return result, time.time() - start


if __name__ == "__main__":
    LEN = 10 ** 7
    lhs = MyVector(LEN, *[random.random() * 10 ** 10 for _ in range(LEN)])
    rhs = MyVector(LEN, *[random.random() * 10 ** 10 for _ in range(LEN)])
    number_of_workers = range(1, 11)

    deltas = []

    for worker_num in number_of_workers:
        temp = []
        for i in range(3):
            result, temp_time = dot_product(lhs, rhs, worker_num)
            temp.append(temp_time)
        deltas.append(mean(temp))

    fig, ax = plt.subplots()

    fig.set_figwidth(12)
    fig.set_figheight(6)
    fig.set_facecolor('floralwhite')
    ax.set_facecolor('seashell')
    ax.grid()

    ax.plot(number_of_workers, deltas)
    ax.scatter(number_of_workers, deltas, c="red")
    ax.set_xlabel("number of processes")
    ax.set_ylabel("time")
    ax.set_title("ratio $T(process)$")

    plt.show()
    plt.close()
