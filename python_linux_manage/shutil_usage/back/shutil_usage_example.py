#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: shutil_usage_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 11:09:31
############################

In [10]: ls
a  coding_time  python_linux_manage/  sys_back/  sys_manager/

In [11]: shutil.copytree('sys_manager', 'sys_manager_bak')
Out[11]: 'sys_manager_bak'

In [12]: ls
a  coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [13]: ls
a  coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [14]: shutil.move('a','b')
Out[14]: 'b'

In [15]: ls
b  coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [16]: shutil.move('b','sys_manager_bak')
Out[16]: 'sys_manager_bak/b'

In [17]: ls
coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [18]: clear

In [19]: ls
coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [20]: ls sys_manager_bak/
argument_parse/             Click_module/         Jinja2_template/
prompt_toolkit_module/  re_template/
b                           configParse_example/  logger/
read_from_fileinput.py
character_support_temlate/  getpass_example.py    mock_mysql_client.py
read_stdin.py

In [23]: ls
coding_time  python_linux_manage/  sys_back/  sys_manager/  sys_manager_bak/

In [24]: os.removedirs('sys_manager_bak')
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
<ipython-input-24-155368cf1085> in <module>
----> 1 os.removedirs('sys_manager_bak')

/usr/python/lib/python3.7/os.py in removedirs(name)
237
238
239     rmdir(name)
240     head, tail = path.split(name)
241     if not tail:

OSError: [Errno 39] Directory not empty: 'sys_manager_bak'

In [25]: shutil.rmtree('sys_manager_bak')

In [26]: ls
coding_time  python_linux_manage/  sys_back/  sys_manager/
