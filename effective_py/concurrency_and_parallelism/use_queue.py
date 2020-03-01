import time
from collections import deque
from threading import Lock, Thread


class MeQueue(object):

    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()


class Worker(Thread):

    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self) -> None:
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


def download(item):
    print("download", item)


def resize(item):
    print("resize", item)


def upload(item):
    print("upload", item)


download_queue = MeQueue()
resize_queue = MeQueue()
upload_queue = MeQueue()
done_queue = MeQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(1000):
    download_queue.put(object())

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print("Processed {} items after polling {} times".format(processed, polled))
