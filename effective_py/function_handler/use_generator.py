'''
    考虑使用生成器来改写直接返回列表的函数

    如果函数要产生一系列结果， 那么最简单的做法就是把这些结果都放在一份列表里面，并将其返回给
    调用者

    例如我们要查出字符串中每个词的首字母，在整个字符串里的位置，示例代码

'''


def index_word(text):
    result = []

    if text:
        result.append(0)

    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)

    return result


address = "Four score and seven years ago..."

result = index_word(address)
print(result)
'''
    index_word 这个函数有两个问题，

    第一个问题是，这个代码写的有点拥挤，每次找到新的结果，都要调用append方法

    使用生成器会更好一点
'''


def index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


result = list(index_word_iter(address))
print(result)

'''
    第二个问题是，在函数返回前， 要先把所有的结果都放在列表里面，
    如果输入量非常大，那么程序就有可能耗尽内存并崩溃，相反， 用
    生成器改写够的版本，可以应对任意长度的输入数据
'''


def index_file(handler):
    offset = 0

    for line in handler:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == " ":
                yield offset


# 定义这种生成器函数的时候， 唯一需要留意的就是，函数返回的那个迭代器，是有状态的， 调用者
# 不应该反复使用它

"""
    使用生成器比把收集到的结果放入列表里返给给调用者更加清晰

    由生成器函数所返回的那个迭代器，可以把生成器函数体中，传给yield表达式的那些值，逐次产生
    出来

    无论输入量有多大，生成器都能产生一系列输入， 因为这些输入量和输入量， 都不会影响它在执行
    时所耗的内存
"""
