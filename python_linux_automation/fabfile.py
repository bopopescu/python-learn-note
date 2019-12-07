from fabric import task
from fabric import connection 
from invoke import Exit
from invocations.console import confirm

hosts = ['own']


@task#(hosts='own')
def test(c):
    with c.prefix('cd /root/python_linux_automation/redis-4.0.9'):
        result = c.run('make &&  make test', warn=True, pty=False)
        if result.failed and not confirm('Tests failed, continue anyway?'):
            raise SystemExit("Aborting at user requeset")
        else:
            print('All tests passed without errors')
            c.run('make clean', warn=True, pty=False, hide=True)
    # with c.prefix('cd /root/python_linux_automation/redis-4.0.9'):
        # c.run('make clean', warn=True, pty=False, hide=True)
    with c.prefix("cd /root/python_linux_automation/"):
        c.run('tar -czf redis-4.0.9.tar.gz redis-4.0.9')

@task
def deploy(c):
    c.put('redis-4.0.9.tar.gz', '/tmp/redis-4.0.9.tar.gz')
    with c.cd('/tmp'):
        c.run('tar xzf redis-4.0.9.tar.gz')
        with c.cd('redis-4.0.9'):
            c.run('make')
            with c.cd('src'):
                c.run('make install')

@task
def clean_file(c):
    with c.cd('/tmp'):
        c.run('rm -rf redis-4.0.9.tar.gz')
        c.run('rm -rf redis-4.0.9')

@task
def clean_local_file(c):
    with c.prefix('cd /root/python_linux_automation/'):
        c.run('rm -rf redis-4.0.9.tar.gz')

@task
def install(c):
    for host in hosts:
        c = connection.Connection('own')
        # test(c)
        # deploy(c)
        clean_file(c)
        clean_local_file(c)
