# Password Strength Tester

A simple password strength tester made with Python and Tkinter.

The program lets you enter a password, test its strength, and see whether it is considered weak, medium, or strong.

It also includes a show/hide password button.

## Features

- Checks password strength
- Shows Weak, Medium, or Strong
- Explains why a password may be weak
- Show/hide password option
- Simple graphical interface
- Runs locally on your computer
- Does not save or send your password anywhere

## How to Run

### 1. Install Python

You need Python installed on your computer.

Download Python from:

https://www.python.org/downloads/

If you are using Windows, make sure to check:

`Add Python to PATH`

during installation.

### 2. Download This Project

On GitHub, click `Code`, then click `Download ZIP`.

Extract the ZIP file somewhere on your computer.

You can also clone the repository using Git:

    git clone https://github.com/YOUR-USERNAME/password-strength-tester.git

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Open the Project Folder

Open the folder where you extracted or cloned the project.

It should look something like this:

    password-strength-tester/
    |
    |-- main.py
    |-- README.md

If your Python file has a different name, use that filename instead of `main.py`.

### 4. Open a Terminal

#### Windows

Open the project folder in File Explorer.

Click the address bar at the top, type:

    cmd

Then press Enter.

A Command Prompt window should open inside the project folder.

#### macOS or Linux

Open Terminal and navigate to the project folder:

    cd path/to/password-strength-tester

### 5. Check That Python Is Installed

Run:

    python --version

If that does not work, try:

    python3 --version

You should see something similar to:

    Python 3.12.0

### 6. Run the Program

If your file is called `main.py`, run:

    python main.py

If that does not work, try:

    python3 main.py

The Password Strength Tester window should now open.

## Tkinter

This program uses Tkinter for the graphical interface.

Tkinter is included with most standard Python installations, so you usually do not need to install anything extra.

If you are using Ubuntu or Debian and Tkinter is missing, install it with:

    sudo apt install python3-tk

## How to Use

1. Run the program.
2. Enter a password into the password box.
3. Click the eye icon to show or hide the password.
4. Click **Test Password**.
5. The program will display the password strength.

The result can be:

- Weak password
- Medium password
- Strong password

The program may also explain why the password is not considered strong.

## How Password Strength Is Checked

The program uses simple password rules.

A password is considered weak if it is shorter than 8 characters.

A password can be considered medium if it is at least 8 characters but contains only letters or only numbers.

A password can be considered strong if it is at least 8 characters and contains different types of characters.

This is a simple educational password checker and should not be treated as a professional security auditing tool.

## Privacy

Passwords are checked locally on your computer.

The program does not:

- Save your password
- Upload your password
- Send your password over the internet
- Store your password in a database

## Requirements

- Python 3
- Tkinter

No additional Python packages are required.

## Built With

- Python
- Tkinter
