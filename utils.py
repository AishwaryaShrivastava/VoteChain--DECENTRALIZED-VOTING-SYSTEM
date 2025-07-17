import json
import os
from datetime import datetime

# Resolve path relative to current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIT_FILE = os.path.join(BASE_DIR, "audit_log.json")

# Format timestamp
def format_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log actions with timestamp
def log_action(action_type, username, description):
    log_entry = {
        "time": format_time(),
        "user": username,
        "action": action_type,
        "details": description
    }

    logs = []
    if os.path.exists(AUDIT_FILE):
        try:
            with open(AUDIT_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append(log_entry)

    os.makedirs(os.path.dirname(AUDIT_FILE), exist_ok=True)  # ✅ Ensure directory exists
    with open(AUDIT_FILE, "w") as f:
        json.dump(logs, f, indent=4)
