# 1. Imports

import socket

# 2. Functions

def get_hostname():
    return socket.gethostname()

# 3. Main Program

print("ServerWatch v1.0")
print("================")

print(f'Hostname: {get_hostname()}')