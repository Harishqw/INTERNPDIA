import random
import string
from tkinter import *

def generate_password():
    password_length = int(password_length_entry.get())
    if password_length > 0:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_characters) for i in range(password_length))
        password_result_label.config(text=password)
    else:
        password_result_label.config(text="Invalid password length")

app = Tk()
app.title("Password Generator")

frame = Frame(app)
frame.pack(padx=35, pady=35)

password_length_label = Label(frame, text="Enter password length:")
password_length_label.grid(row=0, column=0)

password_length_entry = Entry(frame)
password_length_entry.grid(row=0, column=1)

generate_password_button = Button(frame, text="Generate Password", command=generate_password)
generate_password_button.grid(row=1, column=0, columnspan=2)

password_result_label = Label(frame, text=" Your password is ")
password_result_label.grid(row=3, column=0)

password_result_label= Label(frame)
password_result_label.grid(row=3, column=1)
app.mainloop()