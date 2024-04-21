import os
import pickle
from datetime import datetime

def create_user(name: str, data: str, password: str, log_file='logs.txt'):
    user_file = f"{name}.pkl"

    if os.path.exists(user_file):
        log(f"Attempted creation of existing user {name} at", log_file)
        return

    user_data = {'name': name, 'data': data, 'password': password, 'last_changed': datetime.now()}

    with open(user_file, 'wb') as file:
        pickle.dump(user_data, file)

    log(f"Created user {name} at", log_file)

def login(name: str, password: str, log_file='logs.txt'):
    user_file = f"{name}.pkl"

    log(f"Attempted login for user {name} at", log_file)

    if os.path.exists(user_file):
        with open(user_file, 'rb') as file:
            user_data = pickle.load(file)
            if user_data['password'] == password:
                log(f"Login successful for user {name} at", log_file)
                return user_data['data']
            else:
                log(f"Login failed for user {name} at", log_file)
                return None
    else:
        log(f"Attempted login for non-existing user {name} at", log_file)
        return None

def change_password(name: str, old_password: str, new_password: str, log_file='logs.txt'):
    user_file = f"{name}.pkl"

    log(f"Attempted password change for user {name} at", log_file)

    if os.path.exists(user_file):
        with open(user_file, 'rb') as file:
            user_data = pickle.load(file)
            if user_data['password'] == old_password:
                user_data['password'] = new_password
                user_data['last_changed'] = datetime.now()

                with open(user_file, 'wb') as file:
                    pickle.dump(user_data, file)

                log(f"Password change successful for user {name} at", log_file)
            else:
                log(f"Password change failed for user {name} at", log_file)
    else:
        log(f"Attempted password change for non-existing user {name} at", log_file)

def log(message: str, log_file: str):
    with open(log_file, 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        file.write(f"{message} {current_time}\n")

