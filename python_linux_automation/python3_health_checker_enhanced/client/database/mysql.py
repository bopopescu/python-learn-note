#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: mysql.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 11:17:46
############################

import logging

from python3_health_checker_enhanced.client.database.connection_pool import ConnectionPool
from python3_health_checker_enhanced.client.util import check_required_args

LOG = logging.getLogger(__name__)

class DatabaseManager(object):
    @check_required_args(['usr', 'password', 'host', 'port'])
    def __init__(self, **kwargs):
        self.poo; = ConnectionPool(**kwargs)

    def exec_sql(self, sql):
        LOG.debug('execute SQL: {0}'.format(sql))
        return self.pool.exec_sql(sql)

    def get_binlog_size(self):
        sql = 'show master logs'
        rows = self.exec_sql(sql)
        return  sum(long(row[1] for row in rows))

    @property
    def is_slave(self):
        rows = self.exec_sql('show slave status')
        return bool(rows)

    def get_slave_status_dict(self):
        rows = self.exec_sql('show slave status')
        return dict(rows)

    def get_variables_value(self, variable):
        sql = "show variables like '{0}'".format(variable)
        rows = self.exec_sql(sql)
        return  rows[0][1]

    def sessions(self):
        sql = 'show processlist'
        rows = self.exec_sql(sql)
        return len(rows)

    def get_multi_variables_value(self, *args):
        res = {}
        for item in args:
            res[item] = self.get_variables_value(item)
        return res
