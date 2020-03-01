import os
import subprocess
import time

proc = subprocess.Popen(["echo", "hello from the child"], stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out.decode("utf-"))


# proc1 = subprocess.Popen(['sleep', '0.3'])
# while proc1.poll() is None:
#     print("working")
#
# print("Exit status", proc1.poll())

def run_sleep(period):
    print("running")
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


start = time.time()
procs = []
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

for proc in procs:
    proc.communicate()

end = time.time()
print("Finished in {} second".format(end - start))


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b"\xe24U\n\xd0Ql3S\x11"
    proc = subprocess.Popen(
        ["openssl", "enc", "-des3", "-pass", "env:password"],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)

for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])


def run_md5(input_stdin):
    proc = subprocess.Popen(
        ["md5sum"],
        stdin=input_stdin,
        stdout=subprocess.PIPE
    )
    return proc


input_procs = []
hash_procs = []

for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)

for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())
