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
    
    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False

class Logger:
    def log(self, message):
        logging.info(message)

class SyscallInterface:
    def __init__(self):
        self.auth = Auth()
        self.logger = Logger()
        self.root = tk.Tk()
        self.root.title("User  - Friendly System Call Interface")
        self.root.geometry("600x400")
        self.root.configure(bg="Skyblue")  # Green background

        # Create a welcome label
        welcome_label = tk.Label(self.root, text="Welcome to the System Call Interface", bg="#4CAF50", fg="white", font=("Arial", 18, "bold"))
        welcome_label.pack(pady=20)

        # Create a frame for buttons
        button_frame = tk.Frame(self.root, bg="White")
        button_frame.pack(pady=10)
