'''
用Python完成以下任务（要求一个脚本文件完成a,b任务，另一个脚本文件完成c,d任务，并将变量参数化）：
a.创建文件夹（文件夹名称参数化，运行的时候指定，没指定的时候设置默认名称）
b.在此目录下生成文件，文件中有N行的长度为L的随机字符串（建议L小于5，N为10e5）
c.选择一个hash函数，将这些字符串散列到10个文件里（hash函数使得相同的字符串在同一个文件里）
d.构建大小为10的最小堆，来维护字符串重复次数最多的字符串，依次分析10个文件，获取出现最多的字符串及其次数。

    data = count_data_list

    data_length = list(count_data_list.keys())
    data_length_l = len(data_length)
    for i in range(10): 
        for j in range(i + 1, data_length_l): 
            if data[data_length[i]] < data[data_length[j]]: 
                data[data_length[i]], data[data_length[j]] = data[data_length[j]], data[data_length[i]] 

    print(data)
    print(list(data.keys())[:20]) 
'''

import random
import os
import sys
import heapq


def generate_folder_and_file():
    if len(sys.argv) == 2:
        folder_name = sys.argv[1]
    else:
        folder_name = 'test'

    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
    else:
        print("{} existed".format(folder_name))

    file_name = 'random.file'
    if os.path.exists(file_name):
        return folder_name + '/' + file_name
    with open(folder_name + '/' + file_name, 'w+') as f:
        for i in range(100000):
            random_string = \
                ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 5))
            f.write(random_string + '\n')

    return folder_name + '/' + file_name


def hash_to_file(file_path_and_file_name):
    print("file_path_and_file_name", file_path_and_file_name)
    read_data = read_file(file_path_and_file_name)

    while True:
        try:
            data = next(read_data)
            hash_value = hash(data)
            write_to_file(file_path_and_file_name + '_' + str(hash_value % 10),
                          data)
        except Exception:
            break
    print("hash done")


def read_file(file_name):
    with open(file_name, 'r') as f:
        line_data = f.readline()
        while line_data:
            yield line_data
            line_data = f.readline()


def write_to_file(file_name, data):
    with open(file_name, 'a+') as f:
        f.write(data)


def analysis_file(file_name):
    read_data = read_file(file_name)
    count_data_list = {}
    hash_map = {}
    while True:
        try:
            data = next(read_data).replace('\n', '')
            hash_map[data] = hash_map.get(data, 0) + 1
            data = next(read_data)
        except Exception:
            break
    index = heapq.nlargest(10, hash_map.items(), key = lambda x:x[1])
    return index

def analysis_files(base_file_name):
    for i in range(10):
        file_name = base_file_name + '_' + str(i)
        print('filename: {}, count: {}'.format(file_name, analysis_file(file_name)))

if __name__ == "__main__":

    file_name = generate_folder_and_file()
    hash_to_file(file_name)
    analysis_files(file_name)
