class Register(object):

    def __init__(self, ohms):
        self._ohms = ohms
        self.voltage = 0
        self.current = 0


# r1 = Register(50e3)
# r1.ohms += 5e3


class VoltageResistance(Register):

    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self._ohms


"""
    property: class func to class property
"""

r2 = VoltageResistance(1e3)
print("Before: %5r amp" % r2.current)

r2.voltage = 10
print("After: %5r amp" % r2.current)


class BoundedResistance(Register):

    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError("{} ohms must be > 0".format(ohms))
        self._ohms = ohms


# r3 = BoundedResistance(1e3)
# r3.ohms = 0


class FixedResistance(Register):

    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, "_ohms"):
            raise AttributeError("Can not set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
r4.ohms = 2e3
