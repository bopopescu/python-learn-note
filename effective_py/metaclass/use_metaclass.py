class Meta(type):

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        return type.__new__(cls, *args, **kwargs)


class MyClass(object, metaclass=Meta):
    stuff = 23

    def foo(self):
        pass


a = MyClass
print(a)


class ValidatePolygon(type):

    def __new__(cls, *args, **kwargs):
        if args[1] != (object,):
            if args[2].get("sides") < 3:
                raise ValueError("Polygons need 3+ sides")
        return type.__new__(cls, *args, **kwargs)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3


print("before class")


class Line(Polygon):
    print("Before sides")
    sides = 1
    print("After sides")


print("After class")

'''
通过元类， 我们可以在生成子类对象之前，先验证子类的定义是否合乎规范
Python系统把子类的整个class语句体处理完毕之后，就会调用其元类的__new__的方法
'''
