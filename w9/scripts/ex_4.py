from random import shuffle


def coroutine(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        c.send(None)
        return c

    return wrapper


def transform_user_data(user_data):
    user_data = shuffle(user_data) # He-he-he


def connect_user(user_data, file):
    user_data = transform_user_data(user_data)

    with open(file, "w") as file:
        yield from write_to_file(file)


class Disconnect(Exception):
    pass


class Connect(Exception):
    pass


def write_to_file(file):
    while True:
        try:
            line = yield
        except Disconnect:
            print("Stop working with the server!!!")
            break
        else:
            file.writelines(line)
            file.writelines("\n")


@coroutine
def command_manager(file):
    data_base = list()
    while True:
        try:
            data = yield
            data_base.append(data)
        except Connect:
            yield from connect_user(data_base, file)


if __name__ == "__main__":
    server_system = command_manager("example.txt")
    server_system.send(["Vasya"])
    server_system.send(["Petya"])

    server_system.throw(Connect)

    server_system.send("Hello, i\'m the first line!!")
    server_system.send("Nice to meet u, first line ,i\'m the second line!!")
    server_system.send("Boys, u so weird...(written by the third line)")

    server_system.throw(Disconnect)
