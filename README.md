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
```

### 2. Run the setup script

```bash
chmod +x setup.sh
./setup.sh
```

This will:

- Install the systemd service
- Create required log files
- Prompt you to set the `EMAIL_PASSWORD` in `/etc/watchdog.env`
- Enable and start the service

### 3. Edit your `.env` file

After install, update this file securely:

```bash
sudo nano /etc/watchdog.env
```

Set:

```ini
EMAIL_PASSWORD=your_app_password_here
```

Use an [App Password](https://support.google.com/accounts/answer/185833) if you're using Gmail.

---

## 🔍 Monitoring the Service

Check status:

```bash
sudo systemctl status watchdog.service
```

View logs:

```bash
tail -f ~/watchdog.out
tail -f ~/watchdog.err
```

---

## 🔐 Security Tips

- Do **not** commit `/etc/watchdog.env` or any secrets to Git.
- Use `.gitignore` to exclude logs and env files.

---

## 📜 License

MIT