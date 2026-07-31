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
    return {
        "hostname": get_hostname(),
        "operating_system": get_operating_system(),
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "uptime": get_uptime(),
        "failed_services": get_failed_services(),
    }

if __name__ == "__main__":
    app.run(debug=True)