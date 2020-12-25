import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        try:
            self.__connection = socket.create_connection((host, port), timeout=timeout)
        except socket.error:
            raise ClientError

    def __parse_response(self):
        response = b""

        while not response.endswith(b"\n\n"):
            response += self.__connection.recv(1024)

        decoded_response_args = response.decode("utf-8").split("\n", 1)
        status_code = decoded_response_args[0]
        recv_data = decoded_response_args[1].strip()  # deletion of end of the line symbol

        if status_code == "error":
            raise ClientError

        elif status_code == "ok":
            return recv_data

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        message = f"put {key} {value} {timestamp}\n".encode("utf-8")

        try:
            self.__connection.sendall(message)
        except socket.error:
            raise ClientError

        self.__parse_response()

    def get(self, key):
        message = f"get {key}\n".encode("utf-8")

        try:
            self.__connection.sendall(message)
        except socket.error:
            raise ClientError

        data_dict = dict()
        data_response = self.__parse_response()

        if data_response == "":
            return data_dict

        try:
            for row in data_response.split("\n"):
                key, value, timestamp = row.split(" ")
                if key not in data_dict:
                    data_dict[key] = []

                data_dict[key].append((int(timestamp), float(value)))

        except Exception:
            raise ClientError

        for value in data_dict.values():  # sorted by the timestamp value
            value.sort(key=lambda x: x[0])

        return data_dict

    def close(self):
        try:
            self.__connection.close()
        except socket.error:
            raise ClientError


if __name__ == "__main__":
    client = Client('127.0.0.1', 8888)
    client.put("cpu", 102)
    print(client.get("hee"))

    client.close()
