from array import array

numbers = array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast("B")
print(memv_oct.tolist())
print(numbers)
memv_oct[5] = 4
print(numbers)


def calculate_element(sequence):
    res = {}
    for e in set(sequence):
        res[e] = sequence.count(e)
    return res


def compare_number(x, y):
    if bool(int(x) - int(y)):
        return False
    return True


def compare_number_2(x, y):
    if bool(int(x) ^ int(y)):
        return False
    return True

