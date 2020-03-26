def fib_iter(e, x=1, y=0):
    if e == 0:
        return y
    return fib_iter(e - 1, x + y, x)


def fib(e):
    return fib_iter(e, 1, 0)


if __name__ == '__main__':
    res = fib(5)
    print(res)
