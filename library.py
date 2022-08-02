# This code is not working or functional or tested, although that will change tonight or tomorrow. 
# It's mostly here as demonstration; feel free to change things as you see fit


import csv
from user import User
from library_util import Utilities


class Library():
    def __init__(self):

        self.users = []
        self.staff = []
        self.books = []
        self.audio = []
        self.videos = []
        self.setUsers()
        self.setBooks()

    def setUsers(self):
        self.users = Utilities.getUsers('user.csv')
    def setBooks(self):
        self.books = Utilities.getBooks('books.csv')
    def getBooks(self):
        return self.books

    #not really something to implement in the interface, more to just showcase what everything will look like
    def add_user(self, name):
        if self.check_user(name):
            return False

        user = User()
        user.setUser(name,address,age,phone_number,card_number,checked_out,password) #need password to add new user!!
        
        self.users.append(user)

        # NEED TO UPDATE CSV TO HOLD PASSWORD OR NEED SEPERATE DB
        with open('user.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([user.name, user.address, user.age, user.phone_number, user.card_number, user.checked_out])
            csvfile.close()

        return True



    #Getter helper functions
    def get_user(self, card_number):
        for user in self.users:
            if user.card_number == card_number:
                return user
        return None
    
    def get_book(self, name):
        for book in self.books:
            if book['name'] == name:
                return book
        return None

    def get_audio(self, name):
        for audio in self.audio:
            if audio['name'] == name:
                return audio
        return None

    def get_video(self, name):
        for video in self.videos:
            if video['name'] == name:
                return video
        return None



    #returns materials checked out by the user
    def get_user_checked_out(self, user):
        # can be changed to desired output... must return either str or list
        return user.getCheckedOut()



    #helper functions to check if objects exsist 
    def check_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return True
        return False
    
    def check_book(self, name):
        for book in self.books:
            if book['name'].lower() == name.lower():
                return True
        return False

    def check_audio(self, name):
        for audio in self.audio:
            if audio['name'].lower() == name.lower():
                return True
        return False

    def check_video(self, name):
        for video in self.videos:
            if videos['name'].lower() == name.lower():
                return True
        return False
    


    # checks user age for the under-12 requirement
    def check_user_status(self, user):
        if user["age"] <= 12:
            if user["items_amount"] < 5:
                return True
            return False
        return True



    # Helper functions to check material statuses 
    def check_book_status(self, name):
        if book["checked_out"] == 'yes' and book["renewed"] == 'yes':
            return False
        if book["reference"] == 'yes':
            return False
        else:
            return True
    
    def check_audio_status(self, audio):
        if audio["checked_out"] == 'yes' and audio["renewed"] == 'yes':
            return False
        if audio["reference"] == 'yes':
            return False
        else:
            return True
    
    def check_video_status(self, video):
        if video["checked_out"] == 'yes' and video["renewed"] == 'yes':
            return False     
        if video ["reference"] == 'yes':
            return False
        else:
            return True


    
    # material requests
    def request_book(self, book, user):
        if self.check_book(book["name"]):
            if self.check_book_status(book):
                return True
            return False
        return False

    def request_audio(self, audio, user):
        if self.check_audio(audio["name"]):
            if self.check_audio_status(audio):
                return True
            return False
        return False

    def request_video(self, video, user):
        if self.check_video(video["name"]):
            if self.check_video_status(video):
                return True
            return False
        return False



    # functions for users to check out materials
    def checkout_book(self, name, user):
        if self.check_book_status(book):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, book['name'])
                return True
            return False
        return False
    
    def checkout_audio(self):
        if self.check_audio_status(book):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, audio['name'])
                return True
            return False
        return False
    
    def checkout_video(self):
        if self.check_video_status(book):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, video['name'])
                return True
            return False
        return False



    # updates user's checked out materials
    def update_user_checked_out_materials(self, user, name):
        pass



    # log-in methods for interface 
    def log_in(self, user, password):
        if user in self.users:
            if self.authenticate(user, password):
                return True
        return False
    
    def authenticate(self, user, password):
        if user.password == password:
            return True
        return False