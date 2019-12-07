import argparse

"""
[root@ykyk argument_parse]# python ArgumentParse.py 
Namespace(boolean_switch=False, server='localhost')
('host = ', 'localhost')
('boolean_switch = ', False)
[root@ykyk argument_parse]# python ArgumentParse.py --host 127.0.0.1 -t
Namespace(boolean_switch=True, server='127.0.0.1')
('host = ', '127.0.0.1')
('boolean_switch = ', True)
[root@ykyk argument_parse]# python ArgumentParse.py --help
usage: ArgumentParse.py [-h] [--host SERVER] [-t]

This is description

optional arguments:
      -h, --help     show this help message and exit
        --host SERVER  connect to host
          -t             Set a switch to True
"""

def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('--host', action='store', dest='server', 
                        default='localhost', help='connect to host') 
    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch', help='Set a switch to True')
    return parser.parse_args()

def main():
    parser = _argparse()
    print(parser)
    print("host = ", parser.server)
    print("boolean_switch = ", parser.boolean_switch)

if __name__ == '__main__':
    main()



