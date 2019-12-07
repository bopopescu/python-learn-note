#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: use_dnspython_qurey.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 21:12:41
############################

from __future__ import print_function
import dns.resolver

res = dns.resolver.query('dnspython.org', 'NS')
for item in res.response.answer:
    print(item)
