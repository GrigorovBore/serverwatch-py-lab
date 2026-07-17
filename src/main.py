# 1. Imports

import socket
import psutil

# 2. Functions

def get_hostname():
    return socket.gethostname()

def get_cpu_usage():
    return psutil.cpu_percent(interval=5)

def get_memory_usage():
    return psutil.virtual_memory().percent

# 3. Main Program

print("ServerWatch v1.0")
print("================")

print(f'Hostname:      {get_hostname()}')
print('Measuring CPU usage... please wait 5 seconds.')
print(f'CPU usage:     {get_cpu_usage()}%')
print(f'Memory used:   {get_memory_usage()}%')


# print(f"Disk:     {get_disk_usage()}%")
# print(f"Uptime:   {get_uptime()}")