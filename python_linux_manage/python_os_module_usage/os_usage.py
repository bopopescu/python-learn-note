#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: os_usage.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 11:30:14
############################

In [24]: import os

In [25]: os.getcwd()
Out[25]: '/home'

In [26]: os.path.expanduser('~')
Out[26]: '/root'

In [27]: os.path.expanduser('~ykyk')
Out[27]: '/home/ykyk'

In [28]: os.path.expanduser('~ykyk/test')
Out[28]: '/home/ykyk/test'

In [29]: os.path.abspath('.')
Out[29]: '/home'

In [30]: cd /home/ykyk/test/
/home/ykyk/test

In [31]: os.path.abspath('.')
Out[31]: '/home/ykyk/test'

In [32]: os.path.abspath('../test/a.py')
Out[32]: '/home/ykyk/test/a.py'

In [33]: os.path.join('~','test','a.py')
Out[33]: '~/test/a.py'

In [36]: os.path.join(os.path.expanduser('~ykyk'), 'test','a.py')
Out[36]: '/home/ykyk/test/a.py'

In [37]: os.path.isabs('/home/ykyk/test/a.py')
Out[37]: True

In [38]: os.path.isabs('.')
Out[38]: False



