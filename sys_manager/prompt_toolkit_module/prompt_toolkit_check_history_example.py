from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
'''
   查看历史记录功能 
'''
while True:
    user_input = prompt('>>>',
                       history = FileHistory('history.txt'),
                      )
    print(user_input)
