import os
import threading

'''
    在Python中，不仅对象支持多态，类也支持多态

    多态，使得继承体系中的多个类都能以各自独有的方式来实现某个方法，
    这些类，都满足相同的接口或者继承自相同的抽象类，但是却有着各自
    不同的功能

    实现一套MapReduce流程，需要定义公共类来表示输入的数据

'''


class InputData(object):

    def read(self):
        raise NotImplementedError


class PathInputData(InputData):

    def ___init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):

    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):

    def map(self):
        data = self.input_data.read()
        self.result = data.count("\n")

    def reduce(self, other):
        self.result += other.result


'''
    刚才这套Mapreduce的实现方式，看上去很好，但接下来却会遇到一个大问题，
    那就是如何把这些组件拼接起来

    上面那些类，都具备合理的接口与适当的抽象，但是我们必须把对象构建出来
    才能体现出那些类的意义，现在， 由谁来负责构建对象并协调MapReduce流程呢

    最简单的办法是手工构建相关对象，并为该目录下的每个文件创建一个PathInputData
    的实例
'''


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_worker(input_lists):
    workers = []
    for input_data in input_lists:
        workers.append(LineCountWorker(input_data))

    return workers


def execute(Workers):
    threads = [threading.Thread(target=w.amp) for w in Workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, rest = Workers[0], Workers[1:]
    for worker in rest:
        first.reduce(worker)

    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_worker(inputs)
    return execute(workers)


'''
    这个写法的问题在于， MapReduce函数不够通用，如果要编写其他的InputData或
    Worker子类，那就得重写generate_inputs、create_workders和mapreduce函数
    以便与之匹配

    若要解决这个问题，就需要以一种通用的方式来构建对象，
    在其他编程语言中，可以通过构造器多态来解决，也就是令每个InputData子类都
    提供特殊的构造器，使得协调MapReduce流程的那个辅助方法可以用它通用I地构造nputData
    对象，但是Python只允许名为__init__ 的构造器方法，所以我们不能要求每个
    InputData子类都提供兼容的容器


    解决这个问题的最佳方法，是使用@classmethod形式多态，这种多态形式，其实与InputData.read
    那样的实例方法多态非常相似，之不多它针对的是整个类，而不从该类构建
    出来对象

'''


class GenericInputDataClassmethod(object):

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class GenericWorker(object):

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


'''
    上面这段代码所要展示的重点，就是inpuy_class_generate_inputs
    它是个类级别的多态方法，此外我们还看到， create_worlkers方法
    用另外一种方式构造了GenericWorker对象，它是通过cls形式来构造的
    ，而不是像以前那样，直接使用__init__方法


    在Python中，每个类只能由一个构造器，也就是__init__方法
    通过@classmethod机制，可以用一种与构造器相仿的方式来构造类的对象
    通过类方法多态机制，我们能够以更加通用的方式来构造并拼接具体的子类
'''
