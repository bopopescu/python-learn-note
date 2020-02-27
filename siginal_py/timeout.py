import signal
import time


class TimeOutException(Exception):
    pass


def set_timeout(num, callback):
    def wrapper(func):
        def handler(signum, frame):
            raise TimeOutException("Program Time out")

        def todo(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(num)
                rs = func(*args, **kwargs)
                signal.alarm(0)
                return rs
            except TimeOutException:
                callback()

        return todo

    return wrapper


def do_something():
    print("nice")


@set_timeout(4, do_something)
def get_name():
    time.sleep(10)
    return ['a', 'b', 'c']


if __name__ == '__main__':
    a = get_name()
    print(a)
