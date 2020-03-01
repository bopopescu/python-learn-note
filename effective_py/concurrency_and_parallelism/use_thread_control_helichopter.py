import select
from threading import Thread
from time import time


def show_system_call():
    select.select([], [], [], 0.1)


start = time()
for _ in range(5):
    show_system_call()
end = time()

print("TIME: %.3f" % (end - start))

start = time()
threads = []
for _ in range(5):
    thread = Thread(target=show_system_call)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    print(index)


for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()
end = time()
print("TIME %.3f" % (end - start))
