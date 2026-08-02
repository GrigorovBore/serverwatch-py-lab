# serverwatch-py-lab

## Project Overview

**serverwatch-py-lab** is a personal learning project where I'm building a small Python application to practice a complete DevOps workflow. The application collects basic Linux system metrics and is developed on Windows, and deployed to a self-hosted Ubuntu server.

---

## Project Goal

I built this project to practice the complete DevOps workflow—from writing the application to deploying it on a Linux server. Along the way, I'm gaining hands-on experience with Python, Docker, Git, and Linux while learning how these tools fit together in a real deployment workflow.

---

## Project Evolution

Eventually, I decided to remove Docker from the project. My initial intention was to create a program that reports on the health of the machine on which it is installed. To provide accurate data, it should run directly on the operating system it monitors. In that context, Docker was an important learning step, but it also had limitations: when the program ran inside a container, it couldn't accurately observe the host system. In this version I also added operating system detection and reporting of failed services.

---

## Features

* Hostname
* Operating system detection
* CPU usage
* Memory usage
* Disk usage
* System uptime
* Failed services (Linux)

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

---

## Future Improvements

Possible future enhancements include:

* Continuous monitoring mode
* Temperature monitoring
* Health status reporting
* Deployment automation

---