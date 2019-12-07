import re
from prompt_toolkit import prompt

"""
    match ip address
"""

while True:
    user_input = prompt(">>> ")
    print(user_input)
    result = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', user_input)
    print(result)


