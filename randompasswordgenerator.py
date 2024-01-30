import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("600x500")  # Set window dimensions

        self.label = tk.Label(root, text="Generated Password:")
        self.label.pack(pady=10)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, state='readonly', font=('Helvetica', 12))
        self.password_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

    def generate_password(self):
        min_length = 5
        max_length = 15

        password_length = random.randint(min_length, max_length)

        characters = string.ascii_letters + string.digits + string.punctuation

        generated_password = ''.join(random.choice(characters) for i in range(password_length))

        self.password_var.set(generated_password)
        messagebox.showinfo("Password Generated", f"Password has been generated with {password_length} characters.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
