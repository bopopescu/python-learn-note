#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_binary_logs.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 10:27:31
############################

import logging

from python3_health_checker_enhanced.client.env import Env
from python3_health_checker_enhanced.client.util import get_disk_capacity

class CheckBinaryLogs(object):
    def __init__(self, params):
        self.params = params

    def __call__(self):
        res = {}
        res['log_bin'] = Env.database.get_variables_value('log_bin')
        if res['log_bin'] == "ON":
            variables = ['binlog_format', 'sync_binlog', 'expire_logs_days']
            res.update(Env.database.get_multi_variables_value(*variables))
            res['binlog_size'] = Env.database.get_binlog_size()

        res['sync_binlog'] = int(res['sync_binlog'])
        res['expire_log_days'] = int(res['expire_logs_days'])

        res['disk_capacity'] = get_disk_capacity(res.pop('datadir'))

        return res
