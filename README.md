# Simple Password Strength Tester

A simple desktop password strength checker built with Python and Tkinter.

The program lets you enter a password, check how strong it is, and see why it may be considered weak or medium.

It also includes a password visibility toggle so you can show or hide the password while typing.

## Features

- Tests password strength
- Checks password length
- Detects passwords containing only letters
- Detects passwords containing only numbers
- Gives feedback explaining why a password is weak
- Shows Weak, Medium, or Strong results
- Show/hide password button
- Simple graphical interface
- Runs locally on your computer
- Does not save or send passwords anywhere

## How It Works

The program currently uses a few simple rules:

### Weak Password

A password is considered weak if it has fewer than 8 characters.

Example:

```text
hello
12345
abc123
