# 1. Imports

import socket
import psutil
import os
import time
import platform
import subprocess

# 2. Functions

def get_hostname():
    return socket.gethostname()

def get_operating_system():
    return f"{platform.system()} {platform.release()}"

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

def get_failed_services():
    if platform.system() != "Linux":
        return "Not supported on this operating system"

    result = subprocess.run(
        ["systemctl", "--failed", "--no-legend", "--no-pager"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return "Unable to check failed services"

    if result.stdout.strip() == "":
        return "No failed services"

    return result.stdout.strip()

# 3. Main Program

print('================')
print('ServerWatch v1.0')
print('================')

print(f'1. Hostname:         {get_hostname()}')
print(f'2. OS:               {get_operating_system()}')
print('Measuring CPU usage (5 seconds)...')
print(f'3. CPU usage:        {get_cpu_usage()}%')
print(f'4. Memory used:      {get_memory_usage()}%')
print(f'5. Disk used:        {get_disk_usage()}%')
print(f'6. Uptime:           {get_uptime()}')
print(f'7. Failed services:\n{get_failed_services()}')