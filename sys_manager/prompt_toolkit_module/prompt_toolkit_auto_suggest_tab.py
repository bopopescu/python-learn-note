from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter

'''
    自动提示功能
    tab 补全
'''
SQLCompleter = WordCompleter(['select', 'from', 'insert', 'update', 'delete',
                              'drop'], ignore_case = True)

while True:
    user_input = prompt('>>>',
                       history = FileHistory('history.txt'),
                       auto_suggest = AutoSuggestFromHistory(),
                       completer = SQLCompleter,
                       )
    print(user_input)
