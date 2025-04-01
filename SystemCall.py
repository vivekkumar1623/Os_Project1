import logging
import time
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Set up logging configuration
logging.basicConfig(filename='syscall.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Auth:
    def __init__(self):
        self.users = {
            "admin": "password123",  # Example user
            "user1": "mypassword",    # Another example user
        }

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True
