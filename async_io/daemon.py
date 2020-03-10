import atexit
import os
import sys
import time
from signal import SIGTERM


class Daemon(object):

    def __init__(self, pid_file="py_daemon.pid", stdin="/dev/null", stdout="py_daemon.log", stderr="py_daemon.log"):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pid_file = pid_file

    def daemonic(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork #1 failed: {} ({})\n".format(e.errno, e.strerror))
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork #2 failed: {} ({})\n".format(e.errno, e.strerror))
            sys.exit(1)

        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        so = open(self.stdout, 'a+')
        se = open(self.stderr, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        atexit.register(self.del_pid)
        pid = str(os.getpid())
        open(self.pid_file, "w+").write("{}\n".format(pid))

    def del_pid(self):
        os.remove(self.pid_file)

    def start(self):
        try:
            pf = open(self.pid_file, "r")
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pid file {} already exist. Daemon already running?\n"
            sys.stderr.write(message.format(self.pid_file))
            sys.exit(1)

        self.daemonic()
        self.run()

    def stop(self):
        try:
            pf = open(self.pid_file, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        if not pid:
            message = "pid file {} does not exist. Daemon not running?\n"
            sys.stderr.write(message.format(self.pid_file))
            return

        try:
            while True:
                os.kill(pid, SIGTERM)
                time.sleep(1)
        except OSError as err:
            e = str(err)
            if e.find("No such process") > 0:
                if os.path.exists(self.pid_file):
                    os.remove(self.pid_file)
            else:
                print(e)
                sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        raise NotImplementedError
