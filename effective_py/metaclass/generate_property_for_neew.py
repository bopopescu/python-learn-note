class LazyDB(object):

    def __init__(self):
        self.exists = 5

    def __getattr__(self, item):
        value = "Value for {}".format(item)
        setattr(self, item, value)
        return value


data = LazyDB()
print("Before: ", data.__dict__)
print("foo: ", data.foo)
print("After: ", data.__dict__)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, item):
        print("Called __getattr__({})".format(item))
        return super().__getattr__(item)


new_data = LoggingLazyDB()
print("exists: ", new_data.exists)
print("foo:    ", new_data.foo)
print("foo:    ", new_data.foo)


class ValidatingDB(object):

    def __init__(self):
        self.exists = 5

    def __getattribute__(self, item):
        print("Called __getattribute__({})".format(item))
        try:
            return super().__getattribute__(item)
        except AttributeError:
            value = "Value for {}".format(item)
            setattr(self, item, value)
            return value


validate_data = ValidatingDB()
print("exists: ", validate_data.exists)
print("foo:    ", validate_data.foo)
print("foo:    ", validate_data.foo)


class MissingProperty(object):

    def __getattr__(self, item):
        if item == "bad_name":
            raise AttributeError("{} is missing".format(item))
        value = "Value for {}".format(item)
        setattr(self, item, value)
        return value


'''

通过 __getattr__ 和 __setattr__, 我们可以用惰性的方式来加载并保存对象的属性
要理解 __getattr__ 与 __getattribute__ 的区别，前者只会在待访问的属性缺失时触发，而后者会在每次访问属性时触发
如果要在 __getattribute__ 和 __setattr__ 方法中访问实例属性，那么应该直接通过super() （也就是object类的同名方法）来做，以避免无限递归
'''

missing_data = MissingProperty()
print(missing_data.bad_name)
