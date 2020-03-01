'''
    Python有许多内置的api，允许调用者传入参数， 以定制其行为

    api在执行的时候，会通过这些钩子函数，回调函数的代码
    比如list类型的sort方法接受可选的key参数，用以指定每个索引位置上的值
    之间应该如果排序
'''

names = ["scorates", "archimedes", "plato", "aritotle"]

names.sort(key=lambda x: len(x))
print(names)

'''
    其他编程语言可能会用抽象类来定义挂钩，然而在Python中，很多钩子函数只是
    无状态的函数，这些函数有明确的参数及返回值，用函数做挂钩是比较合适的，因为
    他们很容易就能描述出这个挂钩的功能，而且比定义一个类要简单， python中的函数
    之所以能作为钩子，原因就在于它是一级对象，也就是说，函数与方法可以像语言中的
    其他值一样传递和引用

'''


def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}

increment = [
    ("red", 5),
    ('blue', 17),
    ('orange', 9)
]

result = defaultdict(log_missing, current)

print("before", dict(result))

for key, amount in increment:
    result[key] += amount

print("after", dict(result))


def increment_with_report(current, increment):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)

    for key, amount in increment:
        result[key] += amount

    return result, added_count


'''
    对于连接各种Python组件的简单接口来说，通常应该给其直接传入函数， 而不是
    先定义某个类，然后传入该类的实例

    Python中的函数和方法都可以像以及类那样引用，因此它们与其他类型的对象一样
    也能够放在表达式里面

    通过名为__call__ 方法的特殊方法，可以使用该类的实例能够像普通的Python函数
    那样得到调用

    如果要用函数来保存状态信息，那就应该定义新的类，并令其实现__call__方法，
    而不要定义带状态的闭包
'''
