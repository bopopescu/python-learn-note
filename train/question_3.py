"""
使用递归和迭代两种方式实现生成斐波那契数列，计算出第100个数字并比较差异。（可选：使用yield关键字完成任务）

"""


def fib_recusive(n):
    if n < 3:
        return 1
    else:
        return fib_recusive(n - 1) + fib_recusive(n - 2)


def fib(n):
    return fib_iter(1, 0, n)


def fib_iter(a, b, n):
    if n == 1:
        return a
    else:
        return fib_iter(a + b, a, n - 1)


def fib_loop(n):
    a = 1
    b = 0
    result = 0
    i = 0
    while i < n:
        a = a + b
        result = a + b
        i = i + 1
    return result




if __name__ == "__main__":

    r_result = fib(7)
    print(fib_recusive(7))
    print(fib_loop(7))
