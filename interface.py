from library import Library
from user import User
import tkinter as tk

class Interface():
    root = tk.Tk()
    root.title('Library App')
    root.geometry('700x400')
    library = None
    
    def __init__(self):
        self.library = Library()
        self.logged_in = False
        self.user = None
        self.start()

    def start(self):
        # get user's library card number
        tk.Label(self.root, text='Enter library card').pack()
        ent = tk.Entry(self.root)
        ent.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.authenticate(ent.get())).pack()

    def authenticate(self, entry):
        # check if card number in system
        card_number = entry
        user = self.library.get_user(card_number)

        # loggin if user exists
        if user:
            self.user = user
            self.logged_in = True
            self.main_menu()
        else:
            print('USER DOESNT EXIST IN DB')

    def logout(self):
        self.clear()
        self.logged_in = False
        self.user = None
        self.start()

    def main_menu(self):
        self.clear()
        #checkout book
        checkout_book_but = tk.Button(self.root, text='CHECKOUT BOOK', command=self.book_request).pack(ipadx=10, ipady=10)
        #checkout video
        checkout_video_but = tk.Button(self.root, text='CHECKOUT VIDEO', command=self.video_request).pack(ipadx=10, ipady=10)
        #check items
        check_items = tk.Button(self.root, text='CHECK STATUS', command=self.show_checked_out).pack(ipadx=10, ipady=10)
        #exit
        quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)
    
    def book_request(self):
        self.clear()
        tk.Label(self.root, text='which book would you like to request?').pack()
        book_input = tk.Entry(self.root)
        book_input.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.printt(book_input.get(), self.user))).pack()
        #enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_book(book_input.get(), self.user))).pack()

    def video_request(self):
        self.clear()
        tk.Label(self.root, text='which video would you like to request?').pack()
        video_input = tk.Entry(self.root)
        video_input.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_video(video_input.get(), self.user))).pack()

    def audio_request(self):
        self.clear()
        tk.Label(self.root, text='which audio would you like to request?').pack()
        audio_input = tk.Entry(self.root)
        audio_input.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_audio(audio_input.get(), self.user))).pack()

    def show_checked_out(self):
        self.clear()
        tk.Label(self.root, text='CURRENT CHECKED OUT ITEMS:').pack()
        if not self.user:
            request_ack(0)
        else:
            items = self.library.get_user_checked_out(self.user)
            if items:
                labls = [tk.Label(self.root, text=item).pack() for item in items] if type(items) == list else tk.Label(self.root, text=items).pack()
            else:
                tk.Label(self.root, text="No items currently checked out...").pack()
            cont = tk.Button(self.root, text="CONTINUE", command = self.main_menu).pack(ipadx=10, ipady=10)
            quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)

    def request_ack(self, status):
        self.clear()
        if status:
            msg = 'Success!! You have checked out the item!'
        else:
            msg = 'ERROR... Try again'
        
        tk.Label(self.root, text=msg).pack()
        cont = tk.Button(self.root, text="CONTINUE", command = self.main_menu).pack(ipadx=10, ipady=10)
        quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)


    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
    

    def printt(self, x, v):
        print(x,v)

def main():
    lib = Interface()
    user = User()
    #setUser(self, name, addr, age, phone, card, items
    user.setUser('Trusted Member', 'Home', 22, 911, '123', ['Moby Dick', 'The Incredibles'])
    lib.library.users.append(user)
    lib.root.mainloop()
if __name__ == '__main__':
    main()