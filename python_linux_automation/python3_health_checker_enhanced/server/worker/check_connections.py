#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_connections.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 14:02:56
############################

import logging

from python3_health_checker_enhanced.server.worker.generic_worker import GenericWorker
from python3_health_checker_enhanced.server.util import CheckResult
from python3_health_checker_enhanced.server.worker.advise import Advise
from python3_health_checker_enhanced.util import humanize_bytes

class CheckConnections(GenericWorker):

    @property
    def action(self):
        return self.__class__.__name__

    def execute(self):
        result = self.server.client(action=self.action)
        if not result.get('is_success'):
            return
        else:
            self.body = result.get('body')
            self.do_check()

    def do_check(self):
        self.check_max_connections()

    def check_max_connections(self):
        innodb_buffer_pool_size = self.body.get('innodb_buffer_pool_size')
        innodb_buffer_pool_size_in_M = innodb_buffer_pool_size / 1024 / 1024
        low, up = innodb_buffer_pool_size_in_M / 5.12, innodb_buffer_pool_size_in_M / 2.56
        recommend = innodb_biffer_pool_size_in_M / 3.41

        result = CheckResult.get_result_template(self, CheckResult.high)
        max_connections = self.body.get('max_connections')
        if max_connections < low or max_connections > up:
            result.advise =
            Advise.max_connection_warning.format(max_connections,humanize_bytes(innodb_buffer_pool_size),
                                                int(low), int(up),
                                                 int(recommend))
            result.score = -result.score
        self.rs.append(result)
