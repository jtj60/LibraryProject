from library import Library
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

        self.library.users.append({"card-number": '123',
            "checked-out": "none"})

    def start(self):
        # get user's library card number
        card_labl = tk.Label(self.root, text='Enter library card').pack()
        ent = tk.Entry(self.root)
        ent.pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.authenticate(ent)).pack()

    def authenticate(self, entry):

        # check if card number in system
        card_number = entry.get()
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
        checkout_book_but = tk.Button(self.root, text='CHECKOUT BOOK').pack(ipadx=10, ipady=10)
        #checkout video
        checkout_video_but = tk.Button(self.root, text='CHECKOUT VIDEO').pack(ipadx=10, ipady=10)
        #check items
        check_items = tk.Button(self.root, text='CHECK STATUS').pack(ipadx=10, ipady=10)
        #exit
        quit = tk.Button(self.root, text="EXIT", command=self.logout).pack(ipadx=10, ipady=10)
    
    def book_request(self, user):
        name = input('which book would you like to request?')
        #get user answer

        if self.library.checkout_book( name, user):
            print(f'Success!! You have checked out {name}!')
        else:
            print('Failure...')
            #etc....

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
    

def main():
    lib = Interface()
    lib.root.mainloop()
if __name__ == '__main__':
    main()