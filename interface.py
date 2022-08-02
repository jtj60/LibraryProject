from library import Library
from user import User
import tkinter as tk

class Interface():
    root = tk.Tk()
    root.title('Library App')
    root.geometry('800x450')
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
        tk.Label(self.root, text='Enter password').pack()
        pswd = tk.Entry(self.root)
        pswd.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.authenticate(ent.get(), pswd.get())).pack()

    def authenticate(self, entry, pswd):
        # check if card number in system
        card_number = entry
        user = self.library.get_user(card_number)

        # loggin if user exists
        if self.library.log_in(user, pswd):
            self.user = user
            self.main_menu()

        else:
            print('Credientials failed to authenticate.')

    def logout(self):
        self.clear()
        self.logged_in = False
        self.user = None
        self.start()

    def main_menu(self):
        self.clear()
        tk.Label(self.root, text=f'Welcome, {self.user.name}!').pack(ipadx=10, ipady=10)
        #profile
        profile_but = tk.Button(self.root, text='PROFILE', command=self.showUser).pack(ipadx=10, ipady=10)
        #see books
        books_but = tk.Button(self.root, text='SHOW BOOKS', command=self.showBooks).pack(ipadx=10, ipady=10)
        #checkout book
        checkout_book_but = tk.Button(self.root, text='CHECKOUT BOOK', command=self.book_request).pack(ipadx=10, ipady=10)
        #checkout video
        checkout_video_but = tk.Button(self.root, text='CHECKOUT VIDEO', command=self.video_request).pack(ipadx=10, ipady=10)
        #checkout audio
        checkout_audio_but = tk.Button(self.root, text='CHECKOUT AUDIO', command=self.audio_request).pack(ipadx=10, ipady=10)
        #check items
        check_items = tk.Button(self.root, text='CHECK STATUS', command=self.show_checked_out).pack(ipadx=10, ipady=10)
        #exit
        quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)
    
    def showBooks(self):
        self.clear()
        tk.Label(self.root, text='LIBRARY BOOKS:').pack()
        for book in self.library.getBooks():
            tk.Label(self.root, text=str(book), fg='red' if book.checked_out else 'green').pack()
        self.cont()
    def showBooksSmall(self):
        books = self.library.getBooks()
        names = [book.title for book in books if not book.checked_out]
        for name in names:
            tk.Label(self.root, text=name, fg='green').pack()
    def showVideos(self):
        videos = self.library.getVideos()
        avail = [video for video in videos if not video.checked_out]
        for video in videos:
            tk.Label(self.root, text=str(video), fg='green' if video in avail else 'red').pack()
    def showAudio(self):
        audios = self.library.getAudio()
        avail = [audio for audio in audios if not audio.checked_out]
        for audio in audios:
            tk.Label(self.root, text=str(audio), fg='green' if audio in avail else 'red').pack()
    def showUser(self):
        self.clear()
        user = self.user
        tk.Label(self.root, text=user.name).pack()
        tk.Label(self.root, text='Address: '+ user.address).pack()
        tk.Label(self.root, text = 'Age: '+str(user.age))
        tk.Label(self.root, text='Phone: '+user.phone_number).pack()
        self.show_checked_out(clear=False)
            
    def book_request(self):
        self.clear()
        tk.Label(self.root, text='which book would you like to request?').pack()
        self.showBooksSmall()
        book_input = tk.Entry(self.root)
        book_input.pack()
        #enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.printt(book_input.get(), self.user))).pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_book(book_input.get(), self.user))).pack()
        self.cont()

    def video_request(self):
        self.clear()
        tk.Label(self.root, text='which video would you like to request?').pack()
        self.showVideos()
        video_input = tk.Entry(self.root)
        video_input.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_video(video_input.get(), self.user))).pack()
        self.cont()

    def audio_request(self):
        self.clear()
        tk.Label(self.root, text='which audio would you like to request?').pack()
        self.showAudio()
        audio_input = tk.Entry(self.root)
        audio_input.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.request_ack(self.library.checkout_audio(audio_input.get(), self.user))).pack()
        self.cont()

    def show_checked_out(self, clear=True):
        if clear:
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
            self.cont()

    def request_ack(self, status):
        self.clear()
        if status:
            msg = 'Success!! You have checked out the item!'
        else:
            msg = 'ERROR... Try again'
        
        tk.Label(self.root, text=msg).pack()
        self.cont()
        

    def cont(self):
        cont = tk.Button(self.root, text="BACK", command = self.main_menu).pack(ipadx=10, ipady=10)
        quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
    

    def printt(self, x, v):
        print(x,v)

def main():
    lib = Interface()
    lib.root.mainloop()
if __name__ == '__main__':
    main()