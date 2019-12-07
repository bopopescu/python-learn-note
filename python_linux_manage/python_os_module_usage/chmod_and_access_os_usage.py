#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: chmod_and_access_os_usage.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 13:17:56
############################

from __future__ import print_function
import os
import sys

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + "does not exist")
    elif not os.access(filename, os.R_OK):
        os.chmod(filename, '0777')
    else:
        with open(filename) as f:
            print(f.read())


if __name__ == '__main__':
    main()
