
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
# Function to handle login logic
def handle_login():
    email = email_input.get()
    password = password_input.get()
    if not email or not password:
        messagebox.showwarning("Warning", "Please fill in all fields")
        return
    if email == 'uth701@gmail.com' and password == '1234':
        messagebox.showinfo('Success', 'Login successful!')
    else:
        messagebox.showerror('Error', 'Login failed')
# Main window setup
root = Tk()
root.title('Reserve flight')
root.geometry('1366x768')
root.configure(background='white')
# Try loading and displaying image
try:
    original_img = Image.open("image.png")  # Ensure this file exists in the same folder
    resize_img = original_img.resize((100, 100))
    img = ImageTk.PhotoImage(resize_img)
    img_label = Label(root, image=img, bg='green')
    img_label.pack(pady=(10, 10))
except FileNotFoundError:
    img_label = Label(root, text="Image not found", fg="white", bg="green")
    img_label.pack(pady=(10, 10))
# Title label
text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC', font=('verdana', 24))
text_label.pack()
# Email label and entry
email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC', font=('verdana', 12))
email_label.pack(pady=(20, 5))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

# Password label and entry
password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC', font=('verdana', 12))
password_label.pack(pady=(10, 5))

password_input = Entry(root, show='*', width=50)
password_input.pack(ipady=6, pady=(1, 20))

# Login button
login_btn = Button(root, text='Login', bg='white', fg='#0096DC', width=30, height=2,
                   font=('verdana', 10), command=handle_login)
login_btn.pack(pady=(5, 3))

# Start the GUI loop
root.mainloop()


