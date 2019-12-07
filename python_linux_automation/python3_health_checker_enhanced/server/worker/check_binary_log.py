#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_binary_log.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-11 13:17:44
############################

import logging

from python3_health_checker_enhanced.server.worker.generic_worker import GenericWorker
from python3_health_checker_enhanced.server.worker.advise import Advise
from python3_health_checker_enhanced.server.util import CheckResult
from python3_health_checker_enhanced.server.util import humanize_bytes

LOG = logging.getLogger(__name__)

class CheckBinaryLogs(GenericWorker):
    @property
    def action(self):
        return  self.__class__.__name__

    def execute(self):
        result = self,server.clien(action=self.action)
        if not result.get('is_success'):
            return 
        else:
            self.body = result.get('body')
            log_bin = self.body.get('log_bin')
            if log_bin == "OFF":
                LOG.info('log_bin is OFF, skip {0}'.format(self.action))
            else:
                self.do_check()

    def do_check(self):
        self.check_binlog_format()
        self.check_sync_binlog()
        self.check_expire_logs_days()
        self.check_binlog_size()

    def check_binlog_format(self):
        binlog_format = self.body.get('binlog_format')

        result = CheckResult.get_result_template(self, CheckResult.high)

        if binlog_format != 'ROW':
            result.advise = Advise.binlog_format_warning.format(binlog_format, 'ROW')
            result.score = -result.score

        self.rs.append(result)

    def check_sync_binlog(self):
        sync_binlog = self.body.get('sync_binlog')

        result = CheckResult.get_result_template(self, CheckResult.high)

        if sync_binlog == 0:
            result.advise = Advise.sync_binlog_warning.format(sync_binlog, 1)
            result.score = -result.score

        self.rs.append(result)

    def check_expire_logs_days(self):
        expire_logs_days = self.body.get('expire_logs_days')
        result = CheckResult.get_result_template(self, CheckResult.middle)

        if expire_logs_days == 0 or expire_logs_days > 7:
            result.advise = Advise.expire_binlog_days_warning.format(expire_logs_days, 7)
            result.score = -result.score

        self.rs.append(result)

    def check_binlog_size(self):
        binlog_size = self.body.get('binlog_size')
        disk_capacity = self.body.get('disk_capacity')
        percent = 20.0

        result = CheckResult.get_result_template(self, CheckResult.high)

        if binlog_size > disk_capacity * percent / 100:
            result.advise = Advise.binlog_size_too_large.format(humanize_bytes(disk_capacity),
                                                                humanize_bytes(binlog_size),
                                                                percent)
            result.score = -result.score

        self.rs.append(result)



