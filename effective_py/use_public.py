class MyParentObject(object):

    def __init__(self):
        self._private_field = 11


class MyChildObject(MyParentObject):

    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
print(baz.__dict__)
print(baz.__dict__.get("_private_field"))

"""
python编译器无法严格保证private字段的私密性
不要盲目地将属性设置为private，二十应该从一开就做好规划，并允许子类更多地访问超类的内部API
应该多用protected属性，并在文档中把这些字段合理用法告诉子类的开发者，而不要试图用private属性来限制子类访问这些字段
只有当子类不受自己控制时，才可以考虑用private属性来避免名称冲突
"""
