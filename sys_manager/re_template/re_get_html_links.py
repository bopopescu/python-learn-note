#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: re_get_html_links.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 09:23:47
############################

import re
import requests

r = requests.get('https://news.ycombinator.com/')

result = re.findall('"(http?://.*?)"', r.content)


print(result)
