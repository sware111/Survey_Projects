import hashlib
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def log_activity(username, action):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {username} - {action}\n")