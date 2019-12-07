#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: util.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 10:09:34
############################

import inspect
import logging
import functools
import re
import psutil

LOG = logging.getLogger(__name__)

def lower_case_with_underscores(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def get_disk_capacity(path):
    return psutil.disk_usage(path).total

def check_required_args(parameters):
    def decorated(f):
        '''decorator'''
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            '''wrapper'''
            fun_args = inspect.getcallargs(f, *args, **kwargs)
            kwargs = func_args.get('kwargs')
            for item in parameters:
                if kwargs.get(item) is None:
                    message = 'check required args failed, `{0}` is not found \
                    in {1}'.format(item, f.__name__)
                    LOG.error(message)
                    raise Exception(message)
            return f(*args, **kwargs)
        return wrapper
    return decorated



