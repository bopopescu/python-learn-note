'''
 
用Python完成以下任务（要求一个脚本文件完成a,b任务，另一个脚本文件完成c,d任务，并将变量参数化）：
a.	创建文件夹（文件夹名称参数化，运行的时候指定，没指定的时候设置默认名称）
b.	在此目录下生成文件，文件中有N行的长度为L的随机字符串（建议L小于5，N为10e5）
c.	选择一个hash函数，将这些字符串散列到10个文件里（hash函数使得相同的字符串在同一个文件里）
d.	构建大小为10的最小堆，来维护字符串重复次数最多的字符串，依次分析10个文件，获取出现最多的字符串及其次数。

'''

import argparse
import random
import os
import sys

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
    with open(folder_name + '/' + file_name, 'w+') as f:
        for i in range(100000):
            random_string = \
                    ''.join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()', 5))
            print(random_string + '\n')
            f.write(random_string +  '\n')
    

if __name__ == "__main__":
    
    generate_folder_and_file()

