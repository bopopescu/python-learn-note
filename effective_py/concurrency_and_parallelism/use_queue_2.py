import time
from queue import Queue
from threading import Thread

queue = Queue()


def consumer():
    print("Consumer waiting")
    queue.get()
    print("Consumer done")


thread = Thread(target=consumer)
thread.start()

print("Producer putting")
queue.put(object())
thread.join()
print("Producer done")

queue_1 = Queue(1)


def consumer():
    time.sleep(0.1)
    queue_1.get()
    print("Consumer got 1")
    queue_1.get()
    print("Consumer got 2")


thread = Thread(target=consumer)
thread.start()

queue_1.put(object())
print("Producer put 1")
queue_1.put(object())
print("Producer put 2")
thread.join()
print("Producer done")

in_queue = Queue()


def consumer_new():
    print("Consumer waiting")
    work = in_queue.get()
    # Doing work
    print("work", work)
    # work done
    print("Consumer Done")
    in_queue.task_done()


Thread(target=consumer_new).start()
in_queue.put(object())
print("Producer waiting")
in_queue.join()
print("Producer done")


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):

    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


def download(item):
    print("download", item)


def resize(item):
    print("resize", item)


def upload(item):
    print("upload", item)


download_queue = ClosableQueue()
resize_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue)
]
