# serverwatch-py-lab

## Project Overview

**serverwatch-py-lab** is a personal learning project where I'm building a small Python application to practice a complete DevOps workflow. The application collects basic Linux system metrics and exposes them as JSON through a Flask web service. It is developed on Windows and deployed to a self-hosted Ubuntu server, with Nginx acting as a reverse proxy.

ServerWatch runs directly on the Ubuntu host so that it can collect metrics from the operating system it is monitoring. Requests follow this path: 
Client → Nginx (port 80) → Flask (127.0.0.1:5000) → monitor.py → Linux system metrics
Nginx acts as a reverse proxy and forwards incoming HTTP requests to the Flask web service. Flask then collects the current system metrics through the monitoring module and returns them as JSON.

---

## Project Goal

I built this project to practice the complete DevOps workflow—from writing the application to deploying it on a Linux server. Along the way, I'm gaining hands-on experience with Python, Docker, Git, Linux, Flask, virtual environments, and Nginx while learning how these tools fit together in a real deployment workflow.

---

## Project Evolution

Eventually, I decided to remove Docker from the project. My initial intention was to create a program that reports on the health of the machine on which it is installed. To provide accurate data, it should run directly on the operating system it monitors. In that context, Docker was an important learning step, but it also had limitations: when the program ran inside a container, it couldn't accurately observe the host system. In this version I also added operating system detection and reporting of failed services. The application was later extended with a Flask web service that exposes the collected metrics as JSON, with Nginx configured as a reverse proxy on the Ubuntu server.

---

## Features

* Hostname
* Operating system detection
* CPU usage
* Memory usage
* Disk usage
* System uptime
* Failed services (Linux)
* JSON metrics endpoint
* Nginx reverse proxy

---

## Development & Deployment Environment

### Development Machine

* Lenovo T14 Gen 6
* Windows 11 Pro
* Python
* Git
* Docker Desktop
* Visual Studio Code

### Production Server

* Dell PowerEdge R330
* Ubuntu Server 26.04 LTS
* Python 3
* Python virtual environment
* Flask
* Nginx

---

## Future Improvements

Possible future enhancements include:

* Continuous monitoring mode
* Temperature monitoring
* Health status reporting
* Deployment automation

---