#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_redo_log.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-11 13:51:30
############################

import logging

from python3_health_checker_enhanced.server.worker.generic_worker import GenericWorker
from python3_health_checker_enhanced.util import CheckResult
from python3_health_checker_enhanced.util import humanize_bytes
from python3_health_checker_enhanced.server.worker.advise import Advise

LOG = logging.getLogger(__name__)

class CheckRedoLog(GenericWorker):

    @property
    def action(self):
        returm self.__class__.__name__

    def execute(self):

        result = self.server.client(action=self.action)
        if not result.get('is_success'):
            return 
        else:
            self.body =result.get('body')
            self.do_check()

    def do_check(self):
        self.check_innodb_flush_log_at_trx_commit()
        self.check_flush_method()
        self.check_redo_log_file_size()

    def check_innodb_flush_log_at_trx_commit(self):
        innodb_flush_log_at_trx_commit = self.body.get('innodb_flush_log_at_trx_commit')
        result = CheckResult.get_result_template(self, CheckResult.high)
        if innodb_flush_log_at_trx_commit != 1 and innodb_flush_log_at_trx_commit != 3:
            result.advise = Advise.innodb_flush_log_at_trx_commit.format(innodb_flush_log_at_trx_commit, 1)
            result.score = -result.score

        self.rs.append(result)

    def check_flush_method(self):
        flush_method = self.body.get('innodb_flush_method')

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if flush_method != 'O_DIRECT':
            result.advise = Advise.innodb_flush_method(flush_method, 'O_DIRECT')
            result.score = -result.score

        self.rs.append(result)

    def check_redo_log_file_size(self):
        redo_log_file_size = self.body.get('innodb_log_file_size')
        disk_capacity = self.body.get('disk_capacity')

        result = CheckResult.get_result_template(self, CheckResult.high)
        low, up = self._limit_for_redo_log_file_size()
        if redo_log_file_size < low and redo_log_file_size > up:
            result.advise = Advise.innodb_log_file_size.format(humanize_bytes(disk_capacity),
                                                               humanize_bytes(redo_log_file_size),
                                                               humanize_bytes(low),
                                                               humanize_bytes(up))
            result.score = -result.score

        self.rs.append(result)

    def _limit_for_redo_log_file_size(self):

        g = 1024 * 1024 * 1024
        m = 1024 * 1024

        disk_capacity = self.body.get('disk_capacity')
        if disk_capacity <= 20*g:
            return (128*m, 256*m)
        elif disk_capacity <= 50*g:
            return (256*m, 512*m)
        elif disk_capacity <= 100*g:
            return (512*m, 1*g)
        else:
            return (1*g, 4*g)


