
from tkinter import *
from PIL import Image, ImageTk
import os
def rotate_image():
    global counter
    img_label.config(image=img_array[counter % len(img_array)])
    counter += 1
counter = 1
root = Tk()
root.title('Wallpaper Viewer')
root.geometry('250x400')
root.configure(background='black')

# Only load valid image files
files = [f for f in os.listdir('wallpaper') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
img_array = []
for file in files:
    img_path = os.path.join('wallpaper', file)
    img = Image.open(img_path)
    resize_img = img.resize((200, 300))
    photo = ImageTk.PhotoImage(resize_img)
    img_array.append(photo)

if img_array:
    img_label = Label(root, image=img_array[0])
    img_label.pack(pady=(15, 10))
    next_btn = Button(root, text='Next',bg='white',fg='black',width=25,height=2,command=rotate_image)
    next_btn.pack()
else:
    img_label = Label(root, text="No valid images found.", fg='white', bg='black')
    img_label.pack(pady=20)

root.mainloop()
