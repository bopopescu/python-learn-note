from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
# print(floats)
with open("floats.bin", 'wb') as f:
    floats.tofile(f)

floats2 = array('d')
with open("floats.bin", 'rb') as f1:
    floats2.fromfile(f1, 10 ** 7)

print(floats2[-1])
print(floats == floats2)
