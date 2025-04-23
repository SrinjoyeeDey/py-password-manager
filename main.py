from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#Password Generator Project

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
          letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
          numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
          symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

          nr_letters = random.randint(8, 10)
          nr_symbols = random.randint(2, 4)
          nr_numbers = random.randint(2, 4)

          letters_list=[random.choice(letters) for _ in range(nr_letters)]
          numbers_list=[random.choice(numbers) for _ in range(nr_numbers)]
          symbols_list=[random.choice(symbols) for _ in range(nr_symbols)]

          password_list=letters_list+numbers_list+symbols_list

          random.shuffle(password_list)

          password = "".join(password_list)
          password_input.insert(0,password)
          pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if not website or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Email: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")  # Use a 200x200 lock image
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "youremail@example.com")  # You can change this

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()