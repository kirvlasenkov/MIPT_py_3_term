import threading
import subprocess


def get_ping(host):
    return subprocess.Popen(["ping", "-c", "1", "-n", host]).communicate()


if __name__ == "__main__":
    hosts = [
        "google.com",
        "yandex.ru",
        "vk.com",
        "habr.com",
        "python.org",
        "mipt.ru",
    ]

    threads = [threading.Thread(target=get_ping, args=(host,)) for host in hosts]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
