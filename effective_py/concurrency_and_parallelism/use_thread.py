from threading import Thread
import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


'''



start = time.time()

for number in numbers:
    list(factorize(number))
end = time.time()
print("TIME: %.3f"  % (end - start))
'''


class FactorizeThread(Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self) -> None:
        self.factors = list(factorize(self.number))


numbers = [2134343, 123443, 34234, 17856543]
start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print("TIME: %.3f" % (end - start))

"""
Python处理多线程的一个重要理由，就是处理阻塞式的I/O操作
"""
