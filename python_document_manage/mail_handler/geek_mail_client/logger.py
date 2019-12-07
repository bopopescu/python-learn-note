#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: logger.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 13:22:31
############################

import logging

def get_logger(log_level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s [emcli] [%(levelname)s] : %(message)s', "%Y-%m-%d %H:%M:%S")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.handlers = [handler]

    return logger

