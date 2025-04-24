# Os_Project1
# User-Friendly System Call Interface

## Overview

The **User -Friendly System Call Interface** is a Python application that provides a graphical user interface (GUI) for simulating system calls. Built using the Tkinter library, this application allows users to authenticate, perform various system operations, and manage user accounts in a straightforward manner.

## Features

- **User  Authentication**: Secure login for users with predefined credentials.
- **Simulated System Calls**: Perform operations such as:
  - Read
  - Write
  - Delete
  - List
  - Update
  - Info
- **User  Management**: Admin users can add or remove other users.
- **Logging**: All actions are logged to a file for auditing and tracking purposes.

## Requirements

To run this application, you need:

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation

https://github.com/vivekkumar1623/Os_Project1
Install Python: If you don't have Python installed, download it from python.org and follow the installation instructions.

Run the Application: Open your terminal or command prompt, navigate to the directory where the script is located, and run:
   
python syscall_interface.py

Usage
Launching the Application: After running the script, a GUI window will appear with a welcome message and several buttons.

Authentication:

Click on the Start button.
Enter your username and password when prompted. Default credentials are:
Username: admin, Password: password123
Username: user1, Password: mypassword
Performing System Calls:

After successful authentication, you can choose to perform a system call.
Enter the desired operation (e.g., read, write, delete, list, update, info) when prompted.
User Management:

Click on the User Management button to add or remove users.
Follow the prompts to enter the username and password for new users or to remove existing users.
Exiting the Application: Click the Exit button to close the application.

Logging
All actions, including authentication attempts and system calls, are logged in a file named syscall.log located in the same directory as the script. This log file records:

Successful and failed authentication attempts.
Actions performed by users (e.g., system calls, user management).
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This application utilizes the Tkinter library for GUI development.
Logging functionality is provided by Python's built-in logging module.
Contact
For any questions, feedback, or issues, please contact the author at [vk2448384@gmail.com].

Thank you for using the User-Friendly System Call Interface! We hope you find it useful.

Run

### Instructions for Use

1. **Replace** `[your-email@example.com]` with your actual email address or contact information.
2. **Update the GitHub URL** in the clone command to point to your repository if you plan to host it on GitHub.
3. **Save the file** as `README.md` in the same directory as your Python script.
4. This README file provides a comprehensive overview of the project, making it easier for users to understand how to use the application and contribute to it.
