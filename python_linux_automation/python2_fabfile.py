#!/usr/bin/python/
# -*- coding:utf-8 -*-
############################
#File Name: fabric_usage.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-07 15:51:04
############################

from fabric.api import run, sudo
from fabric.api import env
from fabric.api import execute, runs_once, task

env.hosts = ['47.104.148.179']
env.port = 22
env.user = 'root'

def hostname():
    run('hostname')

def ls(path='.'):
    run('ls {}'.format(path))

def tail(path='/etc/password', line=10):
    sudo('tail -n {0} {1}'.format(line, path))

def hello():
    print("hello ykyk")

def test():
    execute(hello)
    execute(hello)

