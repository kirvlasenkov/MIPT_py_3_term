import os
import re
import time
import threading

start = time.time()

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")


def goal(suffix):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])


threads = [threading.Thread(target=goal, args=(i,)) for i in range(20, 30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# WOW!!! better time more than 10 times!!!
print(f"elapsed: {time.time() - start}")
