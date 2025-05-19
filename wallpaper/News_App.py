# import requests

# API_KEY = '9ee976d1a5d24218b1a41ce8c667ea73'  # Replace with your API key
# url = 'https://newsapi.org/v2/top-headlines'

# params = {
#     'country': 'us',            # Fetch top headlines from the US
#     'category': 'technology',   # Technology news
#     'apiKey': API_KEY
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     for article in data['articles']:
#         print("Title:", article['title'])
#         print("Description:", article['description'])
#         print("URL:", article['url'])
#         print("="*60)
# else:
#     print("Failed to fetch data:", response.status_code)





# import requests
# from tkinter import *
# class newsapp:
#   def __init__(self):
#     #fetch data
#     data=requests.get('file:///C:/Users/MD%20UMAR%20AHMED/Downloads/news%20-%20Search.html').json()
#     print(data)
#     #init GUI load
#     self.load_gui()
#     self.root.mainloop()
#     #load the 1st news item
    
#     def load_gui(self):
#       self.root=Tk()
#       self.root.geometry('350x600')
#       self.root.resizable(0,0)
#       self.root.configure(background='black')

# # obj=newsapp()

import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
class NewsApp:
    def __init__(self):
        # fetch data
        response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=07ce6431517e45c5b04b589c36e5bed6')
        self.data = response.json()
        if self.data.get("status") != "ok" or not self.data.get("articles"):
            print("Failed to load news articles.")
            print("Error:", self.data)
            return 
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('1000x1000')
        self.root.resizable(0, 0)
        self.root.title('Mera News App')
        self.root.configure(background='black')
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self, index):
        # clear the screen for the new news item
        self.clear()
        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        label = Label(self.root, image=photo)
        label.image = photo  # prevent garbage collection
        label.pack()
        heading = Label(
            self.root,
            text=self.data['articles'][index]['title'],
            bg='black',
            fg='white',
            wraplength=350,
            justify='center'
        )
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))
        details = Label(self.root,
            text=self.data['articles'][index]['description'],
            bg='black',fg='white',wraplength=350,justify='center'
        )
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)
        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)
        read = Button(frame, text='Read More', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)
        self.root.mainloop()
    def open_link(self, url):
        webbrowser.open(url)
obj = NewsApp()
