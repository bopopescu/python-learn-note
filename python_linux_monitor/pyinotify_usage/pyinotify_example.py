#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: pyinotify_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-05 13:37:36
############################

'''监听/tmp目录下全部事件'''

import pyinotify

# Instanciate a new WatchManager
wm = pyinotify.WatchManager()

# Add a new watch on /tmp for ALL_EVENTS.
#wm.add_watch('/tmp', pyinotify.ALL_EVENTS)

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE
wm.add_watch('/tmp', mask)

# Associate this WatchManager with a Notifier

notifier = pyinotify.Notifier(wm)

#Loop forever and handler events
notifier.loop()


