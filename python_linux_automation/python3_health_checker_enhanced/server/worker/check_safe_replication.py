#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: check_safe_replication.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 14:36:11
############################

from python3_health_checker_enhanced.server.worker.generic_worker import GenericWorker
from python3_health_checker_enhanced.server.util import CheckResult
from python3_health_checker_enhanced.server.worker.advise import Advise

class CheckSafeReplication(GenericWorker):

    @property
    def action(self):
        return self.__class__.__name__

    def execute(self):
        result = self.server.client(actioin=self.action)
        if not result.get('is_success'):
            return
        else:
            self.body = result.get('body')
            is_subordinate = self.body.get('is_subordinate')
            if not is_subordinate:
                return
            else:
                self.do_check()

    def do_check(self):
        self.check_io_thread()
        self.check_sql_thread()
        self.check_relay_log_info_repository()
        self.check_relay_log_recovery()

    def check_io_thread(self):
        subordinate_io_running = self.body.get('subordinate_io_running')
        last_io_error = self.body.get('last_io_error')

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if subordinate_io_running.lower() != 'yes':
            result.advise = Advise.subordinate_io_running_error
            result.score = -result.score

        self.rs.append(result)

        result = CheckResult.get_result_template(self, CheckResult.middle)
        if last_sql_error:
            result.advise = Advise.last_sql_error
            result.score = -result.score

        self.rs.append(result)

    def check_relay_log_recovery(self):
        relay_log_recovery = self.body.get("relay_log_recovery")
        result = CheckResult.get_result_template(self, CheckResult.middler)
        if relay_log_recovery != 'ON':
            result.advise = Advise.relay_log_recovery(relay_log_recovery, "ON")
            result.score = -result.score

        self.rs.append(result)

    def check_relay_log_info_repository(self):
        relay_log_info_repository = self.body.get('relay_log_info_repository')
        result = CheckResult.get_result_template(self.CheckResult.middle)
        if relay_log_info_repository != 'TABLE':
            result.advise = Advise.relay_log_info_repository(relay_log_info_repostory, 'TABLE')
            result.score = -result.score

        self.rs.append(result)
