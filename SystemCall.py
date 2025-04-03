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
        # Create buttons with enhanced appearance
        self.create_button(button_frame, "Start", self.run)
        self.create_button(button_frame, "User  Management", self.manage_users)
        self.create_button(button_frame, "Exit", self.root.quit)

        # Add a footer label
        footer_label = tk.Label(self.root, text="© 2025 System Call Interface", bg="white", fg="blue", font=("Arial", 10, "italic"))
        footer_label.pack(side=tk.BOTTOM, pady=10)

        self.root.mainloop()

    def create_button(self, parent, text, command):
        # Create a frame for the button with rounded corners
        button_frame = tk.Frame(parent, bg="blue", bd=0, relief="flat")
        button_frame.pack(side=tk.LEFT, padx=10)

        # Create a button label
        button_label = tk.Label(button_frame, text=text, bg="#FF4500", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        button_label.pack()

        # Bind hover effects
        button_frame.bind("<Enter>", lambda e: button_frame.config(bg="#C70039"))  # Darker red on hover
        button_frame.bind("<Leave>", lambda e: button_frame.config(bg="#FF4500"))  # Original red

        # Bind click event
        button_label.bind("<Button-1>", lambda e: command())

    def authenticate_user(self):
        username = simpledialog.askstring("Username", "Enter username:", parent=self.root)
        password = simpledialog.askstring("Password", "Enter password:", show='*', parent=self.root)
        
        if self.auth.authenticate(username, password):
            messagebox.showinfo("Authentication", "Authentication successful.", parent=self.root)
            self.logger.log(f"User  '{username}' authenticated successfully.")
            return username
        else:
            messagebox.showerror("Authentication", "Authentication failed.", parent=self.root)
            self.logger.log(f"Failed authentication attempt for user '{username}'.")
            return None

    def perform_syscall(self, username):
        syscall = simpledialog.askstring("System Call", "Enter system call to perform (e.g., 'read', 'write', 'delete', 'list', 'update', 'info'):", parent=self.root)
        if syscall == "read":
            self.simulate_read()
        elif syscall == "write":
            self.simulate_write()
        elif syscall == "delete":
            self.simulate_delete()
        elif syscall == "list":
            self.simulate_list()
        elif syscall == "update":
            self.simulate_update()
        elif syscall == "info":
            self.simulate_info()
        else:
            messagebox.showerror("Error", "Invalid system call.", parent=self.root)
            self.logger.log(f"Invalid system call '{syscall}' attempted by user '{username}'.")

    def simulate_read(self):
        messagebox.showinfo("Simulate Read", "Simulating read operation...", parent=self.root)
        time.sleep(1)  # Simulate time delay
        messagebox.showinfo("Read Operation", "Read operation completed.", parent=self.root)
        self.logger.log("Read operation executed.")
    def simulate_write(self):
        messagebox.showinfo("Simulate Write", "Simulating write operation...", parent=self.root)
        time.sleep(1)  # Simulate time delay
        messagebox.showinfo("Write Operation", "Write operation completed.", parent=self.root)
        self.logger.log("Write operation executed.")

    def simulate_delete(self):
        messagebox.showinfo("Simulate Delete", "Simulating delete operation...", parent=self.root)
        time.sleep(1)  # Simulate time delay
        messagebox.showinfo("Delete Operation", "Delete operation completed.", parent=self.root)
        self.logger.log("Delete operation executed.")
    
    def simulate_list(self):
        messagebox.showinfo("Simulate List", "Simulating list operation...", parent=self.root)
        time.sleep(1)  # Simulate time delay
        messagebox.showinfo("List Operation", "List operation completed.", parent=self.root)
        self.logger.log("List operation executed.")

    def simulate_update(self):
        messagebox.showinfo("Simulate Update", "Simulating update operation...", parent=self.root)
        time.sleep(1)  # Simulate time delay
        messagebox.showinfo("Update Operation", "Update operation completed.", parent=self.root)
        self.logger.log("Update operation executed.")
