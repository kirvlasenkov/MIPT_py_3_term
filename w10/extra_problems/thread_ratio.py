from threading import Thread, Lock
import time
import urllib.request

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]

lock = Lock()


def read_url(url):
    with lock:
        with urllib.request.urlopen(url) as u:
            return u.read()


start = time.time()
threads = [Thread(target=read_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# I have no idea how to outsmart HTTP Error 429 :(
print(time.time() - start)
