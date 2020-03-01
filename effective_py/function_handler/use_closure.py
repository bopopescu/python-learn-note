'''
    python 支持闭包（closure）,闭包是一种定义在某个作用域中的函数，这种函数引用了那个
    作用域里面的变量

    python的函数是一级对象，也就是说，我们可以直接引用函数，把函数赋给变量，把函数当成
    参数传给其他函数，并通过表达式及if语句对其进行比较和判断，等等

    Python使用特殊的规则来比较两个元组。他首先比较各元组中下标为0的对应元素，如果相等，
    再比较下表为1的对应元素，如果还是相等，那就继续比较下标为2的元素，依次类推
'''

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}


def sort_priority(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


# found = sort_priority(numbers, group)
# print("found", found)
# print(numbers)

'''
    当表达式中引入变量时，Python解释器将按照如下顺序遍历各个作用域，以解析该引用：
        1) 当前函数的作用域
        2) 任何外围的作用域（例如，包含当前函数的其他函数）
        3) 包含当前代码的那个模块的作用域（也叫做全局作用域，global scope）
        4) 内置作用域（也就是包含len及str等函数的作用域）
        
    如果上面这些地方都没有定义过名称相符的变量，那么就抛出NameError异常

'''


# 获取闭包函数数据


def sort_priority1(numbers, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


# found = sort_priority(numbers, group)
# print("found", found)
# print(numbers)


'''
    nonlocal 语句清楚地表明，如果在闭包内给该变量赋值，那么修改的其实是闭包外那个作用域的变量

    这与global语句互为补充，global 用来表明对该变量的赋值操作，将会直接修改模块作用域里的那个
    变量

    不建议滥用nonlocal

    如果使用nonlocal的那些代码，已经写的越来越复杂，那就应该将相关状态封装成辅助类

'''


class Sorter(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)

numbers.sort(key=sorter)
assert sorter.found is True

"""
    对于定义在某作用域内的闭包来说，它可以引用这些作用域中的变量，
    使用默认方式对闭包内的变量赋值，不会影响外围作用域中的同名变量
    在Python3中， 程序可以在闭包内用nonlocal语句来修饰某个名称，使该闭包能够修改外围作用域中
    的同名变量

    在Python2中， 程序可以使用可变值（例如包含单个元素的列表），来实现与nonlocal相仿的机制

    除了比较简单的函数， 尽量不要使用nonlocal语句
"""
