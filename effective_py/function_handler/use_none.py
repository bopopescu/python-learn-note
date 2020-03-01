from datetime import datetime
from time import sleep
import json


def log(message, when=datetime.now()):
    print("{}: {}".format(when, message))


log("hi there")
sleep(0.1)
log("hi again")
'''
    在Python中若想正确实现动态默认值，习惯上是把默认值设为None，并在文档字符串
    （docstring）里面把None所对应的实际行为描述出来，编写函数代码时，如果发现
    该参数的值是None， 那就将其设为实际的默认值

'''


def log2(message, when=None):
    """
        Log a message with a timestamp

        Args:
            message: Message to print
            when: datetime of when the message occurred.
                Defaults to the present time.
    """
    when = datetime.now() if when is None else when
    print("{}: {}".format(when, message))


log2("hi there")
sleep(0.1)
log2("hi again")

"""
    如果参数的实际默认值是可变类型（mutable）， 那就一定要记得用None作为形式上的
    默认值。例如， 从编码为Json格式的叔叔中载入某个值，若解码数据时失败，则返回默认
    返回空的字典, 可能会采用下面这种办法来实现此功能
"""


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


'''
    这种写法的错误和刚才的datatime.now()类似，由于default参数的默认值只会在模块
    加载时评估一次，所以凡是以默认形式来调用decode函数的代码，都将共享同一份字典
    会引发奇怪的行为
'''

foo = decode("bad data")
foo['stuff'] = 5
bar = decode("also bad")
bar["meep"] = 1
print("foo: ", foo)
print("bar: ", bar)

'''
    本以为foo和bar会标识两份不同的字典，每个字典里面都有一对键值对，但是实际上 
    修改了其中一个之后，另外一个似乎也会受到影响，这种错误的根本原因是：foo和bar
    其实都等同于在写default参数默认值的那个字典，他们都是表示的是同一个字典对象
'''

assert foo is bar


# 解决办法 把关键子参数的默认值设置为None，并在函数的文档字符串中描述它的实际行为

def decode2(data, default=None):
    """
    Load JSON data from a string
    Args:
        data: JSON data to decode
        default: Value to retunr if decoding fails,
            Defaults to an empty dictionary.
    """

    if default is None:
        default = {}

    try:
        return json.loads(data)
    except ValueError:
        return default


"""
    参数的默认值，只会在程序加载模块并读取到本函数的定义时评估一次，对于{}或者[]
    等动态的值，这可能会导致奇怪的行为

    对于动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为None，并在
    函数的文档字符串里面描述该默认值所对应的实际行为
"""
