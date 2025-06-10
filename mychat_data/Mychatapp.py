import os
from tkinter import *
from tkinter import messagebox, simpledialog, scrolledtext
import datetime

APP_DIR = "mychat_data"
os.makedirs(APP_DIR, exist_ok=True)

class MyChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MyChatApp")
        self.root.geometry("600x700")
        self.root.configure(bg='lightblue')

        self.contacts = []  # list of saved contact numbers
        self.current_contact = None  # mobile number string

        # UI: Contacts frame
        self.contacts_frame = Frame(root, bg='white', bd=2, relief=RIDGE)
        self.contacts_frame.place(x=10, y=10, width=180, height=680)

        Label(self.contacts_frame, text="Contacts", bg='white', font=("verdana", 14, "bold")).pack(pady=5)
        self.contacts_listbox = Listbox(self.contacts_frame, font=("verdana", 12))
        self.contacts_listbox.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.contacts_listbox.bind("<<ListboxSelect>>", self.load_contact_chat)

        add_contact_btn = Button(self.contacts_frame, text="Add Contact", command=self.add_contact)
        add_contact_btn.pack(pady=10)

        # UI: Chat frame
        self.chat_frame = Frame(root, bg='white', bd=2, relief=RIDGE)
        self.chat_frame.place(x=200, y=10, width=380, height=680)

        self.chat_title = Label(self.chat_frame, text="Select a contact to start chatting", bg='white', font=("verdana", 16))
        self.chat_title.pack(pady=10)

        self.chat_display = scrolledtext.ScrolledText(self.chat_frame, state=DISABLED, font=("verdana", 12), wrap=WORD)
        self.chat_display.pack(padx=10, pady=5, fill=BOTH, expand=True)

        input_frame = Frame(self.chat_frame, bg='white')
        input_frame.pack(fill=X, padx=10, pady=10)

        self.message_input = Entry(input_frame, font=("verdana", 12))
        self.message_input.pack(side=LEFT, fill=X, expand=True, ipady=5, padx=(0,5))
        self.message_input.bind("<Return>", self.send_message)

        send_btn = Button(input_frame, text="Send", command=self.send_message, width=8)
        send_btn.pack(side=RIGHT)

        # Load saved contacts from file if exists
        self.load_contacts()

        # On close, save contacts
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def contacts_file(self):
        return os.path.join(APP_DIR, "contacts.txt")

    def load_contacts(self):
        try:
            with open(self.contacts_file(), "r") as f:
                self.contacts = [line.strip() for line in f if line.strip()]
            self.refresh_contacts_listbox()
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.contacts_file(), "w") as f:
            for contact in self.contacts:
                f.write(contact + "\n")

    def refresh_contacts_listbox(self):
        self.contacts_listbox.delete(0, END)
        for contact in self.contacts:
            self.contacts_listbox.insert(END, contact)

    def add_contact(self):
        new_contact = simpledialog.askstring("Add Contact", "Enter mobile number:")
        if new_contact:
            new_contact = new_contact.strip()
            if new_contact in self.contacts:
                messagebox.showinfo("Info", "Contact already exists!")
                return
            if not new_contact.isdigit() or len(new_contact) < 7:
                messagebox.showerror("Error", "Invalid mobile number!")
                return
            self.contacts.append(new_contact)
            self.contacts.sort()
            self.refresh_contacts_listbox()
            self.save_contacts()

    def chat_file(self, contact):
        return os.path.join(APP_DIR, f"chat_{contact}.txt")

    def load_contact_chat(self, event=None):
        selection = self.contacts_listbox.curselection()
        if selection:
            index = selection[0]
            contact = self.contacts[index]
            self.current_contact = contact
            self.chat_title.config(text=f"Chat with {contact}")
            self.chat_display.config(state=NORMAL)
            self.chat_display.delete(1.0, END)
            try:
                with open(self.chat_file(contact), "r", encoding="utf-8") as f:
                    content = f.read()
                    self.chat_display.insert(END, content)
            except FileNotFoundError:
                pass
            self.chat_display.config(state=DISABLED)
            self.chat_display.see(END)
            self.message_input.focus()

    def add_message(self, user, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        formatted_message = f"{user} [{timestamp}]: {message}\n"
        self.chat_display.config(state=NORMAL)
        self.chat_display.insert(END, formatted_message)
        self.chat_display.config(state=DISABLED)
        self.chat_display.see(END)

        # Save chat history
        with open(self.chat_file(self.current_contact), "a", encoding="utf-8") as f:
            f.write(formatted_message)

    def send_message(self, event=None):
        if not self.current_contact:
            messagebox.showwarning("Warning", "Select a contact to chat with.")
            return
        message = self.message_input.get().strip()
        if not message:
            messagebox.showwarning("Warning", "Please type a message")
            return
        self.add_message("You", message)
        self.message_input.delete(0, END)

        # Simulate a reply from contact (for demo)
        self.root.after(800, lambda: self.add_message(self.current_contact, f"Reply to: {message}"))

    def on_closing(self):
        self.save_contacts()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = MyChatApp(root)
    root.mainloop()
