from prompt_toolkit import prompt
'''
    交互式程序，避免了backspace不能用等问题
'''
while True:
    user_input = prompt('>>>')
    print(user_input)
