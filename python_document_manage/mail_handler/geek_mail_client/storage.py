#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: storage.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 13:26:24
############################

class Storage(dict):

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError[k]

    def __repr__(self):
        return '<Storage' + dict.__repr__(self) + '>'
