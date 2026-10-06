from tkinter import *

window = Tk()
window.geometry("1000x800")
window.title("Password Test")
window.config(background="#dbeafe")


# ---------------- TITLE ----------------

title = Label(
    window,
    text="Password Test",
    font=("arial", 30, "bold"),
    bg="#dbeafe",
    fg="#1e3a5f"
)
title.place(x=350, y=30)


# ---------------- MAIN BOX ----------------

box = Frame(
    window,
    bg="white",
    width=450,
    height=350,
    highlightbackground="#b5cbea",
    highlightthickness=2
)
box.place(x=275, y=160)


# ---------------- PASSWORD LABEL ----------------

enter_text = Label(
    box,
    text="Enter your password to test",
    font=("arial", 17, "bold"),
    bg="white",
    fg="#1e3a5f"
)
enter_text.place(x=73, y=38)


# ---------------- PASSWORD INPUT CONTAINER ----------------

password_frame = Frame(
    box,
    bg="white",
    width=310,
    height=35,
    highlightbackground="black",
    highlightthickness=2
)
password_frame.place(x=73, y=88)


# Password entry
input_pass = Entry(
    password_frame,
    font=("arial", 16),
    show="*",
    bd=0,
    relief="flat",
    bg="white",
    fg="#111827"
)
input_pass.place(
    x=5,
    y=2,
    width=260,
    height=29
)


# ---------------- EYE ICON ----------------

eye_canvas = Canvas(
    password_frame,
    width=35,
    height=29,
    bg="white",
    highlightthickness=0,
    cursor="hand2"
)
eye_canvas.place(x=270, y=1)


def draw_eye():
    eye_canvas.delete("all")

    # Eye outline
    eye_canvas.create_oval(
        8, 9,
        27, 20,
        outline="#1e3a5f",
        width=2
    )

    # Pupil
    eye_canvas.create_oval(
        14, 11,
        21, 18,
        fill="#1e3a5f",
        outline=""
    )


draw_eye()


def toggle_password(event=None):
    if input_pass.cget("show") == "*":
        input_pass.config(show="")

        # Add slash when password is visible
        eye_canvas.create_line(
            7, 6,
            28, 23,
            fill="#1e3a5f",
            width=2
        )

    else:
        input_pass.config(show="*")
        draw_eye()


eye_canvas.bind("<Button-1>", toggle_password)


# ---------------- PASSWORD TEST ----------------

def test_pass():
    password = input_pass.get()

    reasons = []

    if len(password) < 8:
        reasons.append("Password is less than 8 characters")

    if password.isalpha():
        reasons.append(
            "Password has no numbers or special characters"
        )

    if password.isdigit():
        reasons.append(
            "Password only contains numbers"
        )

    if len(password) < 8:

        result.config(
            text="Weak password",
            fg="#dc2626"
        )

        reason_text.config(
            text="Why is this weak?\n" + "\n".join(reasons),
            fg="#dc2626"
        )

    elif password.isalpha() or password.isdigit():

        result.config(
            text="Medium password",
            fg="#e68a00"
        )

        reason_text.config(
            text="Why is this not strong?\n" + "\n".join(reasons),
            fg="#e68a00"
        )

    else:

        result.config(
            text="Strong password",
            fg="#16a34a"
        )

        reason_text.config(
            text="Good length and character variety.",
            fg="#16a34a"
        )


# ---------------- TEST BUTTON ----------------

test_button = Button(
    box,
    text="Test Password",
    font=("arial", 15, "bold"),
    command=test_pass,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    bd=0,
    padx=20,
    pady=8,
    cursor="hand2"
)
test_button.place(x=135, y=148)


# ---------------- RESULT ----------------

result = Label(
    box,
    text="",
    font=("arial", 20, "bold"),
    bg="white"
)
result.place(x=115, y=225)


reason_text = Label(
    box,
    text="",
    font=("arial", 11),
    bg="white",
    justify="left"
)
reason_text.place(x=73, y=270)


# ---------------- SAFETY TEXT ----------------

safety_text = Label(
    window,
    text="🔒 This is a local only program. Your password is not saved or sent anywhere.",
    font=("arial", 12),
    bg="#dbeafe",
    fg="#36536f"
)
safety_text.place(x=220, y=740)


window.mainloop()