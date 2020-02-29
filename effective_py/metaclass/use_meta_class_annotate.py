class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = "_" + self.name

    def __get__(self, instance, owner):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer(object):
    first_name = Field("first_name")
    last_name = Field("last_name")
    prefix = Field("prefix")
    suffix = Field("suffix")


foo = Customer()
print("Before: ", repr(foo.first_name), foo.__dict__)
foo.first_name = "Euclid"
print("After: ", repr(foo.first_name), foo.__dict__)


class Meta(type):

    def __new__(cls, *args, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = "_" + key
        cls = type.__new__(cls, *args, **kwargs)
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


class NewField(object):

    def __init__(self):
        self.name = None
        self.internal_name = None


class BetterCustomer(DatabaseRow):
    first_name = NewField()
    last_name = NewField()
    prefix = NewField()
    suffix = NewField()


print("-" * 100)
new_foo = BetterCustomer()
print("Before:", repr(new_foo.first_name), foo.__dict__)
foo.first_name = "Euler"
print("After: ", repr(new_foo.first_name), foo.__dict__)
