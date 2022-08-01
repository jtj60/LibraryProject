from library import Library
import tkinter as tk

class Interface():
    root = tk.Tk()
    root.title('Library App')
    root.geometry('700x400')
    library = None
    def __init__():
        library = Library()
        self.start()

    def start(self):
        labl = tk.Label(self.root, text='Enter library card').pack()
        ent = tk.Entry(self.root).pack()
        enter_button = tk.Button(self.root, text='ENTER', width=15, command=lambda:self.authenticate(ent)).pack()

    def authenticate(self, entry):
        print(entry.get())


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