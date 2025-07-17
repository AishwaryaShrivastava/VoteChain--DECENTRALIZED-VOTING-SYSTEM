import json
import os
import bcrypt

# Always resolve the path relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

# Load users from file
def load_users():
    if not os.path.exists(USERS_FILE):
        return []

    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save users to file
def save_users(users):
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)  # ✅ Create folder if needed
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Register user
def register_user(username, password, role, wallet, private_key):
    users = load_users()

    for user in users:
        if user["username"] == username:
            return False, "Username already exists"

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    new_user = {
        "username": username,
        "password": hashed_pw,
        "role": role,
        "wallet": wallet,
        "private_key": private_key
    }

    users.append(new_user)
    save_users(users)
    return True, "User registered successfully"

# Authenticate login
def authenticate_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and bcrypt.checkpw(password.encode(), user["password"].encode()):
            return True, user
    return False, "Invalid username or password"
