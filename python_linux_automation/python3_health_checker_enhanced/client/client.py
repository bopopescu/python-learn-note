#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: client.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 13:19:09
############################

import logging
import traceback

from python3_health_checker_enhanced.client.handler import SyncMsgHandler
from python3_health_checker_enhanced.client.repsone import sync_ok, sync_error

LOG = logging.getLogger(__name__)

class Client(object):
    def __init__(self):
        self.msg_handler = SyncMsgHandler()

    def __call__(self, **kwargs):
        action = kwargs.get('action', 'invalid')
        params = kwargs.get('params', {})

        try:
            result = self.msg_handler.execute(action, params)
            LOG.info("do action {0} successful".format(action))
            return sync_ok(action, result)
        except Exception as e:
            LOG.error("catch exception when handle action: {0}, err_msg: {1}".format(actioin, e))
            LOG.error(traceback.format_exc())
            return sync_error(action, e)

