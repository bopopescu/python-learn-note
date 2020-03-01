'''
    在参数上面迭代时，要多加小心

    函数在输入的参数上面迭代时要多加小心，如果参数时迭代器，那么可能会导致奇怪的行为并错失某些值

    Python的迭代器协议，描述了容器和迭代器应该如何与iter和next内置函数、for循环以及相关表达式相
    互配合

    把__iter__ 方法实现为生成器，即可定义自己的容器类型

    想判断某个值是迭代器还是容器，可以拿该值为参数，两次调用iter函数，若结果相同，则是迭代器，调
    用内置的next韩剧是，即可令迭代器前进一步
'''


def normalize_func(get_iter):
    total = sum(get_iter)
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


# 定义一个迭代器容器类


class ReadVisits(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


path = "/tmp/path"
visits = ReadVisits(path)
percentags = normalize_func(visits)
print(percentags)
