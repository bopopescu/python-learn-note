#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_redo_log.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 11:01:10
############################

import logging

from python3_health_checker_enhanced.client.env import Env
from python3_health_checker_enhanced.client.util import get_disk_capacity

LOG = logging.getLogger(__name__)

class CheckRedoLog(object):
    def __init__(self, params):
        self.params = params
        self.res = {}

    def __call__(self):
        res = {}
        variables = ['innodb_log_file_size', 'innodb_flush_log_at_trx_commit',
                    'innodb_flush_method', 'datadir']
        res.update(Env.database.get_multi_variables_value(*variables))
        res['disk_capacity'] = get_disk_capacity(res.pop('datadir'))
        res['innodb_flush_log_at_trx_commit'] = int(res['innodb_flush_log_at_trx_commit'])
        res['innodb_log_file_size'] = int(res['innodb_log_file_size'])

        return res
