from .daemon import Daemon
import socket
import select
import time

import pdb
# __all__ = ["Net"]
DEBUG = True


class State(object):

    def __init__(self):
        self.state = "accept"
        self.have_read = 0
        self.need_read = 5
        self.have_write = 0
        self.need_write = 0

        self.buff_read = ""
        self.buff_write = ""
        self.socket_obj = ""

    def print_state(self):
        if DEBUG:
            print('\n - current state of fd: %d' % self.socket_obj.fileno())
            print(" - - state: %s" % self.state)
            print(" - - have_read: %s" % self.have_read)
            print(" - - need_read: %s" % self.need_read)
            print(" - - have_write: %s" % self.have_write)
            print(" - - need_write: %s" % self.need_write)
            print(" - - buff_write: %s" % self.buff_write)
            print(" - - buff_read:  %s" % self.buff_read)
            print(" - - sock_obj:   %s" % self.socket_obj)


class NetBase(object):

    def set_fd(self, sock):
        print("set fd start")
        temp_state = State()
        temp_state.socket_obj = sock
        self.conn_state[sock.fileno()] = temp_state
        self.conn_state[sock.fileno()].print_state()
        print("\n set fd end!")

    def accept(self, fd):
        print("accept start")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        conn.setblocking(0)
        return conn
