# 解析配置文件

import ConfigParser

cf = ConfigParser.ConfigParser(allow_no_value=True)

In [1]: import ConfigParser

In [2]: cnf = ConfigParser.ConfigParser(allow_no_value=True)

In [3]: cnf.read("example_my.cnf")
Out[3]: ['example_my.cnf']

In [4]: cnf.sectionsOut[4]: <bound method ConfigParser.sections of
<ConfigParser.ConfigParser instance at 0x24c9f38>>

In [5]: cnf.sections()
Out[5]: ['client', 'mysqld']

In [6]: cnf.has_section("client")
Out[6]: True

In [8]: cnf.options("client")
Out[8]: ['port', 'user', 'password', 'host']

In [9]: cnf.has_option("client","user")
Out[9]: True

In [10]: cnf.get('client','user')
Out[10]: 'mysql'

n [11]: cnf.getint('client', 'port')
Out[11]: 3306

In [11]: cnf.getint('client', 'port')
Out[11]: 3306

In [12]: cnf.remove_section('client')
Out[12]: True

In [13]: cnf.add_section('mysql')

In [14]: cnf.set('mysql','host','127.0.0.1')

In [15]: cnf.set('mysql','port','3307')

In [16]: cnf.write(open('after_changed_example_my.cnf','w'))

