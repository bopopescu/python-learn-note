import re

"""
    python3 re match function 
    match函数类似于字符串中的startswith函数，只是match应用在正则表达式中更加
    强大，更富有表现力，match函数用以匹配字符串的开始部分，如果模式匹配成功，
    返回一个SRE_Match对象，如果模式匹配失败，返回一个None，因此，对于普通的前
    缀匹配，用法和startswith一样
    match匹配成功时返回SRE_Match类型的对象，该对象包含了相关的模式和原始字符串
    模式匹配成功的子串起始位置和结束位置，也可以通过该对象获取匹配的字符串
"""
n [1]: import re

In [2]: r = re.match('\d+', '123 is one hundred and twenty-three')

In [3]: r.start()
Out[3]: 0

In [4]: r.end()
Out[4]: 3

In [5]: r.re
Out[5]: re.compile(r'\d+', re.UNICODE)

In [6]: r.string
Out[6]: '123 is one hundred and twenty-three'

In [7]: r.group()
Out[7]: '123'
