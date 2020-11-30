import socket
with socket.create_connection(("127.0.0.1", 10001)) as sock:

    sock.settimeout(2)
    try:
        data = input().encode("utf-8")
        sock.sendall(data)
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)