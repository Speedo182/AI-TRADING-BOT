import hashlib
import os
import time

class Login():
    def __init__(self):
        self.users = {}
        self.session_duration = 86400 # 24 hours in seconds
        self.logged_in_users = {}

    def add_user(self, username, password):
        # Hash the password using sha256
        password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = password

    def login(self, username, password):
        # Hash the password using sha256
        password = hashlib.sha256(password.encode()).hexdigest()
        
        # Check if the username and password match
        if username in self.users and self.users[username] == password:
            # Set the login time
            self.logged_in_users[username] = int(time.time())
            return True
        else:
            return False

    def logout(self, username):
        if username in self.logged_in_users:
            del self.logged_in_users[username]

    def check_session(self, username):
        if username in self.logged_in_users:
            # Check if the session has expired
            if int(time.time()) - self.logged_in_users[username] > self.session_duration:
                del self.logged_in_users[username]
                return False
            else:
                return True
        else:
            return False
