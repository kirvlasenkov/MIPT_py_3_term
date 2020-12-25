import socket
import threading
import multiprocessing
import os


def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("PID:", os.getpid())

        thread = threading.Thread(target=process_request, args=(conn, addr))
        thread.start()


def process_request(conn, addr):
    print("addr: ", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(data.decode("utf-8"))


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 10001))
        sock.listen(socket.SOMAXCONN)

        PROCESS_COUNT = 6
        process_list = [multiprocessing.Process(target=worker,
                                                args=(sock,)) for _ in range(PROCESS_COUNT)]

        for process in process_list:
            process.start()
        for process in process_list:
            process.join()
