'''
获取操作系统、内核、网卡等信息，以及磁盘、CPU、内存使用情况并写在文本文件里

'''

import os
import socket

write_file_template =  """
hostname:
    {hostname}

system info : 
    {system_info}

kernel: 
    {kernel_info}

cpu load:
    {cpu_load}

memory info:
    {memory_info}

disk info:
    {disk_info}

"""


def get_system_info():
    hostname = socket.gethostname()
    print(hostname)
    
    system_info = os.popen('uname -a').readlines()[0] or 'no data'
    print(system_info)

    kernel_info = os.popen('uname -r').readlines()[0] or 'no data'
    print(kernel_info)

    cpu_info = os.popen('uptime').readlines()[0] or 'no data'
    cpu_load = cpu_info.split("user,")[-1].strip()
    print(cpu_load)

    memory_info = os.popen("free -m ").read() or 'no data'
    print(memory_info)

    disk_info = os.popen('df -h').read() or 'no data'
    print(disk_info)
    
    data = {
        "hostname": hostname,
        "system_info": system_info,
        "kernel_info": kernel_info,
        "cpu_load": cpu_load,
        "memory_info": memory_info,
        "disk_info": disk_info
    }
    
    with open("./system_info", "w+") as f:
        f.write(write_file_template.format(**data))
    
if __name__ == "__main__":
    get_system_info()

