from threading import Thread
from multiprocessing import Process, Queue
import time
import random
import numpy as np

from my_mathematics.linear_algebra import MyVector
import matplotlib.pylab as plt

# global variable for answer
RESULT = 0


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


def process_chunk_dot(left_chunk, right_chunk, queue):
    assert len(left_chunk) == len(right_chunk)

    queue.put(MyVector(len(left_chunk), *left_chunk) * MyVector(len(right_chunk), *right_chunk))


def thread_chunk_dot(left_chunk, right_chunk, dot_result):
    assert len(left_chunk) == len(right_chunk)

    dot_result += (MyVector(len(left_chunk), *left_chunk) * MyVector(len(right_chunk), *right_chunk))


def get_result(queue):
    result = 0
    while not queue.empty():
        result += queue.get()
    return result


def dot_product(lhs: "MyVector", rhs: "MyVector", mode, units_number):
    """
    Realization of a standard dot product from linear algebra

    :param lhs: first operand  of a dot product
    :param lhs: second operand  of a dot product
    :param mode: method of optimization. Allowed
     computing through multiprocessing or
     multithreading.
    :param units_number: quantity of processes or threads,
     using for computing (name of units
     depends on mode which you've chosen)

    :return: result of a dot product
    """
    assert len(lhs) == len(rhs)

    global RESULT
    computed_time = 0
    UNIT_NUM = units_number

    # practice, merely needed for using my own vector
    splited_lhs = split_array(rhs.args_as_np, UNIT_NUM)
    splited_rhs = split_array(rhs.args_as_np, UNIT_NUM)

    if mode == "multithreading":
        threads = []
        for left_chunk, right_chunk in zip(splited_lhs, splited_rhs):
            threads.append(Thread(target=thread_chunk_dot, args=(left_chunk, right_chunk, RESULT)))

        for thread in threads:
            thread.start()

        start_time = time.time()
        for thread in threads:
            thread.join()
        computed_time = time.time() - start_time

    elif mode == "multiprocessing":
        queue = Queue()
        processes = []
        for left_chunk, right_chunk in zip(splited_lhs, splited_rhs):
            processes.append(Process(target=process_chunk_dot, args=(left_chunk, right_chunk, queue)))

        for process in processes:
            process.start()

        start_time = time.time()
        for process in processes:
            process.join()
        computed_time = time.time() - start_time
        RESULT = get_result(queue)

    return RESULT, computed_time


if __name__ == "__main__":
    LEN = 10 ** 7
    units_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20]
    lhs = MyVector(LEN, *[random.random() * 10 ** 10 for _ in range(LEN)])
    rhs = MyVector(LEN, *[random.random() * 10 ** 10 for _ in range(LEN)])
    process_result = 0
    thread_result = 0

    processes_deltas = []

    for units in units_number:
        temp_time = []
        for i in range(3):
            process_result, computed_time = dot_product(lhs=lhs, rhs=rhs, mode="multiprocessing", units_number=units)
            temp_time.append(computed_time)

        processes_deltas.append(sum(temp_time) / 3)

    threads_deltas = []

    for units in units_number:
        temp_time = []
        for i in range(3):
            thread_result, computed_time = dot_product(lhs=lhs, rhs=rhs, mode="multithreading", units_number=units)
            temp_time.append(computed_time)

        threads_deltas.append(sum(temp_time) / 3)

    print("MULTIPROCESSING:")
    print("average time on processes:", np.mean(processes_deltas))
    print("result on process:", process_result)

    print("\nMULTITHREADING:")
    print("average time on threads:", np.mean(threads_deltas))
    print("result on threads", thread_result)

    fig, ax = plt.subplots(nrows=1, ncols=2)

    fig.set_figwidth(12)
    fig.set_figheight(6)
    fig.set_facecolor('floralwhite')
    ax[0].set_facecolor('seashell')
    ax[1].set_facecolor('seashell')
    ax[0].grid()
    ax[1].grid()

    ax[0].plot(units_number, processes_deltas)
    ax[0].scatter(units_number, processes_deltas, c="red")
    ax[0].set_xlabel("number of processes")
    ax[0].set_ylabel("time")
    ax[0].set_title("ratio $T(processes)$")

    ax[1].plot(units_number, threads_deltas)
    ax[1].scatter(units_number, threads_deltas, c="red")
    ax[1].set_xlabel("number of threads")
    ax[1].set_ylabel("time")
    ax[1].set_title("ratio $T(threads)$")

    plt.show()
    plt.close()
