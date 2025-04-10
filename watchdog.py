#!/usr/bin/env python3

import os
import time
import smtplib
import socket
import subprocess
from email.mime.text import MIMEText

# === Config ===
TARGET_HOST = "192.19.161.250"   # your home IP, domain, or device
TARGET_PORT = 22                              # port to test (like SSH)
CHECK_INTERVAL = 60                           # seconds between checks
EMAIL_FROM = "ericbotcher@gmail.com"        # dummy sender
LOG_FILE = "/home/alien/watchdog.log"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ALERT_EMAILS = [
    "14156466696@tmomail.net",
    "ericbotcher@gmail.com"
]

if not EMAIL_PASSWORD:
    raise RuntimeError("EMAIL_PASSWORD environment variable not set")

# === Core ===
def is_reachable(host, _=None):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "2", host], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def send_alert(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("ericbotcher@gmail.com", EMAIL_PASSWORD)
        for email in ALERT_EMAILS:
            msg = MIMEText(message)
            msg["From"] = EMAIL_FROM
            msg["To"] = email
            msg["Subject"] = "🚨 Home Network Alert"
            server.sendmail(EMAIL_FROM, [email], msg.as_string())

def log(message):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")

# === Loop ===
alerted = False  # Tracks if we've already alerted for current state
was_unreachable = False  # Tracks last known state

while True:
    if is_reachable(TARGET_HOST, TARGET_PORT):
        log(f"✅ {TARGET_HOST}:{TARGET_PORT} reachable")
        if was_unreachable:
            # Recovery detected
            recovery_msg = f"✅ {TARGET_HOST}:{TARGET_PORT} is BACK ONLINE!"
            send_alert(recovery_msg)
            log(recovery_msg)
        alerted = False
        was_unreachable = False
    else:
        msg = f"🚨 {TARGET_HOST}:{TARGET_PORT} UNREACHABLE!"
        log(msg)
        if not alerted:
            send_alert(msg)
            alerted = True
        was_unreachable = True
    time.sleep(CHECK_INTERVAL)