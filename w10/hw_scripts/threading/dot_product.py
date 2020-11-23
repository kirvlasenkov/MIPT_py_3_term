from threading import Thread
from multiprocessing import Process
import time
import random

from my_mathematics.linear_algebra import MyVector
import matplotlib.pylab as plt


# stolen from seminar
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


def chunk_dot(left_chunk, right_chunk, dot_result):
    assert len(left_chunk) == len(right_chunk)

    dot_result += MyVector(len(left_chunk), *left_chunk) * MyVector(len(right_chunk), *right_chunk)


def dot_product(lhs: "MyVector", rhs: "MyVector", mode, units_number):
    """
    Realization of a standard dot product from linear algebra

    :param lhs: first operand  of a dot product
    :param lhs: second operand  of a dot product
    :param mode: method of optimization. Allowed
     computing through multiprocessing or
     multithreading.
    :param units_number: quantity of processes or threads,
     using for computing (depends on mode which you've chosen)

    :return: result of a dot product
    """
    assert len(lhs) == len(rhs)
    dot_result = 0
    UNIT_NUM = units_number

    # practice, merely needed for using my own vector
    splited_lhs = split_array(rhs.args_as_np, UNIT_NUM)
    splited_rhs = split_array(rhs.args_as_np, UNIT_NUM)

    if mode == "multithreading":
        threads = []
        for left_chunk, right_chunk in zip(splited_lhs, splited_rhs):
            threads.append(Thread(target=chunk_dot, args=(left_chunk, right_chunk, dot_result)))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    elif mode == "multiprocessing":
        processes = []
        for left_chunk, right_chunk in zip(splited_lhs, splited_rhs):
            processes.append(Process(target=chunk_dot, args=(left_chunk, right_chunk, dot_result)))

        for process in processes:
            process.start()
        for process in processes:
            process.join()

    return dot_result


if __name__ == "__main__":
    LEN = 10 ** 6
    units_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lhs = MyVector(LEN, *[random.random() * 10 for _ in range(LEN)])
    rhs = MyVector(LEN, *[random.random() * 10 for _ in range(LEN)])

    processes_deltas = []

    for units in units_number:
        start = time.time()
        result = dot_product(lhs=lhs, rhs=rhs, mode="multiprocessing", units_number=units)
        processes_deltas.append(time.time() - start)

    threads_deltas = []

    for units in units_number:
        start = time.time()
        result = dot_product(lhs=lhs, rhs=rhs, mode="multithreading", units_number=units)
        threads_deltas.append(time.time() - start)

    print(processes_deltas)
    print(threads_deltas)

    fig, axes = plt.subplots(nrows=1, ncols=2)

    fig.set_figwidth(12)
    fig.set_figheight(6)
    fig.set_facecolor('floralwhite')
    axes[0].set_facecolor('seashell')
    axes[1].set_facecolor('seashell')
    axes[0].grid()
    axes[1].grid()

    axes[0].plot(units_number, processes_deltas)
    axes[0].scatter(units_number, processes_deltas, c="red")
    axes[0].set_xlabel("number of processes")
    axes[0].set_ylabel("time")
    axes[0].set_title("ratio $T(processes)$")

    axes[1].plot(units_number, threads_deltas)
    axes[1].scatter(units_number, threads_deltas, c="red")
    axes[1].set_xlabel("number of threads")
    axes[1].set_ylabel("time")
    axes[1].set_title("ratio $T(threads)$")

    plt.show()
