'''
    用数量可变的位置参数减少视觉杂讯

    *args


'''


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("{}: {}".format(message, values_str))


log("My numbers ars", [1, 2])
log("hi there", [])


# 改进版本

def log2(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print("{}: {}".format(message, values_str))


"""
    接受可变的位置参数，会带来两个问题

    第一个问题是，变长参数在传给函数时， 总是要先转化成元组（tuple），
    这就意味着， 如果用带有*操作符的生成器为参数，来调用这种函数，那么
    Python就必须先把该生成器完整地迭代一轮，并把生成器所生成的每一个值
    ，都放入元组中，这可能会消耗大量内存，并导致程序崩溃
"""


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(*args)


it = my_generator()
my_func(*it)

'''
    只有当我们能够确定输入的参数个数比较少时，才应该令函数接受*args式的边长参数
    在需要把很多个字面量或者变量名称一起传给某个函数的场合，使用这种变长参数，是
    较为理想的

    使用*args参数的第二个问题就是，如果以后要给函数添加新的位置参数， 那就必须修
    改原来调用该函数的代码。

    若是只给函数列表前方添加新的位置参数， 而不更改现有的调用代码，就会产生难以调
    试的错误

    总结

        在def语句中使用*args，即可令该函数接受数量可变的位置参数

        调用函数时，可以采用*操作符，把序列中的元素当成位置参数，传给该函数

        对生成器使用*操作符，可能导致程序耗尽内存并崩溃

        在已经接受*args参数的函数上面继续添加位置参数，可能会产生难以调试的问题
'''
