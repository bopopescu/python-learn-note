'''
将字符串"Life is short I use
Python"转换成数组，然后再将数组拼接成字符串，最后统计出每个字母的出现次数（不区分大小写）

'''
from collections import namedtuple

counts = namedtuple('counts', ['letter', 'times'])

STRING = "Life is short i use Python"


def string_convert(string):
    string_to_list = string.split()
    print(string_to_list)

    array_to_string = " ".join(string_to_list)
    print(array_to_string)

    count_data = {}

    for l in string.lower():
        if l not in count_data.keys():
            count_data[l] = 1
        else:
            count_data[l] += 1

    print(count_data)


if __name__ == "__main__":
    string_convert(STRING)
