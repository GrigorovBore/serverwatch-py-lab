from flask import Flask
from monitor import (
    get_hostname,
    get_operating_system,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_uptime,
    get_failed_services
)

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"1. Hostname:  {get_hostname()}<br>"
        f"2. OS:        {get_operating_system()}<br>"
        f"3. CPU usage: {get_cpu_usage()}%<br>"
        f"4. Memory usage: {get_memory_usage()}%<br>"
        f"5. Disk usage: {get_disk_usage()}%<br>"
        f"6. Uptime: {get_uptime()}<br>"
        f"7. Failed services: {get_failed_services()}"

    )

if __name__ == "__main__":
    app.run(debug=True)

