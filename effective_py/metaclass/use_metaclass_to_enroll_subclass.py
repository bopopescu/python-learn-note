import json


class Serializable(object):

    def __init__(self, *args):
        self.args = args

    def serializer(self):
        return json.dumps({"args": self.args})


class Point2D(Serializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point2D({}, {})".format(self.x, self.y)


point = Point2D(5, 3)
print("Object: ", point)
print("Serializer: ", point.serializer())


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return "BetterPoint2D({}, {})".format(self.x, self.y)


better_point = BetterPoint2D(5, 3)
print("Before: ", better_point)
data = point.serializer()
print("Serialized: ", data)
after = BetterPoint2D.deserialize(data)
print("After: ", after)


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({
            "class": self.__class__.__name__,
            "args": self.args
        })

    def __repr__(self):
        return "BetterPoint2D({})".format(self.args)


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    print("Params: ", params)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class EventBetterPoint2D(BetterSerializable):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


register_class(EventBetterPoint2D)

print("*" * 20)
event_point = EventBetterPoint2D(5, 3)
print("Before: ", point)
event_data = event_point.serialize()
print("Serialized:", event_data)
after = deserialize(event_data)
print("After: ", after)


class Meta(type):

    def __new__(cls, *args, **kwargs):
        cls = type.__new__(cls, *args, **kwargs)
        register_class(cls)
        return cls


class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):

    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z


v3 = Vector3D(10, -7, 3)
print("Before: ", v3)
v_data = v3.serialize()
print("Serializer", v_data)
print("After: ", deserialize(v_data))
