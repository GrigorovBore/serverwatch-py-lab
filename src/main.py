# 1. Imports

import socket
import psutil
import os
import time

# 2. Functions

def get_hostname():
    return socket.gethostname()

def get_cpu_usage():
    return psutil.cpu_percent(interval=5)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage(os.path.abspath(os.sep)).percent

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return f'{days}d {hours}h {minutes}m'

# 3. Main Program

print('================')
print('ServerWatch v1.0')
print('================')

print(f'1. Hostname:      {get_hostname()}')
print('Measuring CPU usage (5 seconds)...')
print(f'2. CPU usage:     {get_cpu_usage()}%')
print(f'3. Memory used:   {get_memory_usage()}%')
print(f'4. Disk used:     {get_disk_usage()}%')
print(f'5. Uptime:        {get_uptime()}')