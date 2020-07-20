#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_safe_replication.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 11:08:57
############################

import logging

from python3_health_checker_enhanced.client.env import Env

LOG = logging.getLogger(__name__)

class CheckSafeReplication(object):
    def __init__(self, params):
        self.params = params

    def get_subordinate_status(self):
        res = {}
        subordinate_status_dict = Env.database.get_subordinate_status_dict()
        res['subordinate_io_running'] = subordinate_status_dict['Subordinate_IO_Running']
        res['subordinate_sql_running'] = subordinate_status_dict['Subordinate_SQL_Running']
        res['last_io_error'] = subordinate_status_dict['Last_IO_Error']
        res['last_sql_error'] = subordinate_status_dict['Last_SQL_Error']

        returnr res

    def __call__(self):
        res = dict(is_subordinate=Env.database.is_subordinate)

        if Env.database.is_subordinate:
            res.update(Env.database.get_multi_variables_value('relay_log_recovery',
                                                             'relay_log_info_repository'))
            res.update(self.get_subordinate_status())

        return res
