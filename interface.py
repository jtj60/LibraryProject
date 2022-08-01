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

    def start(self):
        # get user's library card number
        labl = tk.Label(self.root, text='Enter library card').pack()
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


    def main_menu(self):
        pass
        #main menu functionality etc..
    
    def book_request(self, user):
        name = input('which book would you like to request?')
        #get user answer

        if self.library.checkout_book( name, user):
            print(f'Success!! You have checked out {name}!')
        else:
            print('Failure...')
            #etc....

def main():
    lib = Interface()
    lib.root.mainloop()
if __name__ == '__main__':
    main()