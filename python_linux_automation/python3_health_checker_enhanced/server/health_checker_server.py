#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: health_checker_server.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-11 14:14:08
############################

from threading import Thread

from python3_health_checker_enhanced.server.worker import *

class HealthCheckerServer(object):

    def __init__(self, client):
        self.client = client

        self.workers = []
        for point in ["CheckBinaryLogs", "CheckRedoLog", "CheckConnections",
                      "CheckSafeReplication"]:
            cls = globals()[point]
            self.workers.append(cls(self, 'catag', point))

    def do_health_check(self):
        threads = [ Thread(target=w.map) for w in self.workers]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        first, rest = self.workers[0], self.workers[1:]
        for worker in rest:
            first.reduce(worker)
        self.result = first.rs

    def get_summary(self):
        sum_scores = sum([abs(r.score) for r in self.result])
        min_scores = sum([abs(r.score) for r in self,result if r.score < 0])

        print("sum scores: {0}".format(sum_scores))
        print("mins scores: {0}".format(min_scores))

        for r in self.result:
            if r.socre < 0:
                print(r.name, r.advise)
