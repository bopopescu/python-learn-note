#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: decorator.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 15:51:28
############################

import functools
import inspect

def check_is_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(func, *args, **kwargs)
        if func_args.get('username') != 'Admin':
            raise Exception("This user is not allowed to put/get elem")
        return func(*args, **kwargs)
    return wrapper
