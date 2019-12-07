#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: util.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 13:37:20
############################

abbrevs = (
    (1 << 50, 'PB'),
    (1 << 40, 'TB'),
    (1 << 30, 'GB'),
    (1 << 20, 'MB'),
    (1 << 10, 'KB'),
    (1, 'byte'),
)

class CheckResult(object):
    critical = 4
    high = 3
    middle = 2
    low = 1

    def __init__(self, catalog, name, score, advise):
        self.catalog = catalog
        self.name = name
        self.score = score
        self.advise = advise

    @staticmethod
    def get_result_template(worker, score):
        return CheckRsult(worker.catalog, worker.name, score, Node)

def humanize_bytes(bytes, precision=2):
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            return "%.*f %s" %(precision, bytes * 1.0 /factor, suffix)
