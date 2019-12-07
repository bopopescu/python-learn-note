#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: main.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-11 14:30:57
############################

import argparse
import logging
import logging.config
import os
import sys
import traceback

pkg_root = os.path.realpath(os.path.join(os.path.realpath(__file__),
                                        os.path.pardir,
                                        os.path.pardir))

sys.path.append(pkg_root)

from python3_health_checker_enhanced.client.env import Env
from python3_health_checker_enhanced.client.database import DatabaseManager
from python3_health_checker_enhanced.client import Client

from python3_health_checker_enhanced.server.health_checker_server import HealthCheckerServer

log_cnf = os.path.join(pkg_root, 'conf', 'logging.cnf')
logging.config.fileConfig(log_cnf, disable_existing_loggers=False)
LOG = logging.getLogger(__name__)

def _argparse():
    parser = argparse.ArgumentParser(description='Health checker for MySQL database')
    parser.add_argument('--host', action='store', dest='host', required=True,
                        help='connect to host')
    parser.add_argument('--user', action='store', dest='user', required=True,
                        help='user for login')
    parser.add_argument('--password', action='store', dest='password', required=True,
                        help='password to use when connecting to server')
    parser.add_argument('--conn_size', action='store', dest='conn_size',
                        default=5, type=int, 
                        help='how much connection for database usage')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.2')
    return parser.parse_args()

def main():
    try:
        parser = _argparse()
        Env.database = DatabaseManager(host=parser.host, user=parser.user,
                                       password=parser.password,
                                       port=parser.port)
        server = HealthCheckerServer(Client())
        server.do_health_check()
        server.get_summary()

    except Exception as exc:
        print(exc)
        LOG.error(traceback.format_exc())

if __name__ == '__main__':
    main()
