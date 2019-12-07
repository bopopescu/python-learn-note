#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: generic_worker.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 13:55:11
############################

import logging
import time

LOG = logging.getLogger(__name__)

class GenericWorker(object):
    def __init__(self, server, catalog, name):
        self.server = server
        self.catalog = catalog
        self.name = name
        self.rs = []

    def print_start_info(self):
        self.start_time = time.time()
        LOG.info("begin to health check: {}".format(self.name))

    def print_end_info(self):
        elipse = time.time() - self.start_time
        LOG.info("finish for health check: {0} in {1}".format(self.name, elipse))

    def map(self):
        try:
            self.print_start_info()
            self.execute()
        except Exception as e:
            LOG.info('failed to health check: {0}, failed reason: {1}'.format(self.name, e))
        else:
            self.print_end_info()

    def execute(self):
        raise NotImplementedError("=====You did not implemented this function =====")

    def reduce(self, other):
        self.rs.extend(other.rs)
