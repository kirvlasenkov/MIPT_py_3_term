import select
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))
sock.listen()

conn_1, addr_1 = sock.accept()
conn_2, addr_2 = sock.accept()

conn_1.setblocking(0)
conn_2.setblocking(0)

epoll = select.epoll

epoll_map = {
    conn_1.fileno(): conn_1,
    conn_2.fileno(): conn_2,
}


while True:
    events = epoll.poll(1)

    for fileno, event in events:
        if event and select.EPOLLIN:
            mess = epoll_map[fileno].recv(1024)
            print(mess.decode("utf-8"))

        if event and select.EPOLLOUT:
            mess = input().encode("utf-8")
            epoll_map[fileno].send(mess)
