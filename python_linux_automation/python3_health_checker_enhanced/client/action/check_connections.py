#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_connections.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 10:52:22
############################

import logging

from python_health_checker_enhanced.clent.env import Env

LOG = logging.getLogger(__name__)

class CheckConnections(object):
    def __init__(self, params):
        self.params = params

    def __call__(self):
        res = Env.database.get_multi_variables_value('max_connections', 'innodb_buffer_pool_size')
        res['max_connections'] = int(res['max_connections'])
        res['innodb_buffer_pool_size'] = int(res['innodb_buffer_pool_size'])

    return res
