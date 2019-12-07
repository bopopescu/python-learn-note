#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: mysql_context_manager.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 17:12:47
############################

import pymysql as db
from contextlib import contextmanager

@contextmanager
def get_conn(**kwargs):
    conn = db.connect(host=kwargs.get('host', 'localhost'),
                        user=kwargs.get('user'),
                        passwd=kwargs.get('passwd'),
                        port=kwargs.get('port', 3306),
                        db=kwargs.get('db'))
    try:
        yield conn
    finally:
        if conn:
            conn.close()

conn_args = dict(host='47.99.123.29', user='ykyk', passwd='123456',
                 port=3306, db='mysql_test_ykyk')

# print(conn_args)
with get_conn(**conn_args) as conn:
    with conn as cur:
        try:
            cur.execute('select version()')
            result = cur.fetchone();
            print(result)
        except:
            raise SystemExit('db error')
