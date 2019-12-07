"""
    执行这段程序，系统会自动默认编辑器，进入编辑器后，就可以在编辑器中输入内容
    功能类似''fc'
"""

from __future__ import print_function
import click

message = click.edit()
print(message, end='')

