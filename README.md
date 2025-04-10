# 🛡️ Watchdog Network Monitor

A simple Python-based watchdog that monitors network connectivity to a target IP and sends alerts via email (and optionally SMS). Designed to run as a systemd service.

---

## 🚀 Features

- Monitors connectivity to a host and port
- Sends email/SMS alerts when the target becomes unreachable or recovers
- Runs as a systemd service
- Simple log output to local files
- Secure credential handling via environment variables

---

## 📦 Setup

### 1. Clone the repo

```bash
git clone https://github.com/capt-alien/watchdog-monitor.git
cd watchdog-monitor