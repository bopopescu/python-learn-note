#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: response.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-10 13:02:01
############################

def sync_error(action_name, error, **kwargs):
    resp_dict = {}
    resp_dict['action'] = action_name
    resp_dict['is_success'] = False
    error = str(error) if isinstance(error, Exception) else error
    resp_dict['error'] = error

    if kwargs:
        resp_dict.update(kwargs)

def sync_ok(action_name, body, **kwargs):
    resp_dict = {}
    resp_dict['action'] = action_name
    resp_dict['is_success'] = True
    resp_dict['body'] = body

    if kwargs:
        resp_dict.update(kwargs)
    return resp_dict
