from monitor import (
    get_hostname,
    get_operating_system,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_uptime,
    get_failed_services,
)

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