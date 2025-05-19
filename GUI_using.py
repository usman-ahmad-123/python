from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
def handle_login():
  email=email_input.get()
  password=password_input.get()
  print(email,password)
  if email == 'fornormaluse701@gmail.com' and password=='1234':
    messagebox.showinfo('yayayas','Login success')
  else:
    messagebox.showerror('Error','Login failed')
root = Tk()
root.title('Login Form')
# root.iconbitmap('favicon.ico')

root.geometry('350x500')
root.configure(background='red')

# Load and resize the image
original_img = Image.open("image.png")
resize_img = original_img.resize((100, 100))
img = ImageTk.PhotoImage(resize_img)

# Image label
img_label = Label(root, image=img, bg='green')
img_label.pack(pady=(10, 10))

# Title text
text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

# Email label and input
email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

# Password label and input
password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(10, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, show='*')
password_input.pack(ipady=6,pady=(1, 20))

# Login button
login_btn = Button(root, text='Login', bg='white', fg='#0096DC', width=30, height=5,command=handle_login)
login_btn.pack(pady=(5,3))
login_btn.config(font=('verdana',10))

# Start the main loop
root.mainloop()
