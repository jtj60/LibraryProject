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
        self.setVideos()
        self.setAudios()

    def setUsers(self):
        self.users = Utilities.getUsers('user.csv')
    def setBooks(self):
        self.books = Utilities.getBooks('books.csv')
    def getBooks(self):
        return self.books
    def setVideos(self):
        self.videos = Utilities.getVideos('video.csv')
    def getVideos(self):
        return self.videos
    def setAudios(self):
        self.audio = Utilities.getAudios('audio.csv')
    def getAudio(self):
        return self.audio

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
            if book.title == name:
                return book
        return None

    def get_audio(self, name):
        for audio in self.audio:
            if audio.title == name:
                return audio
        return None

    def get_video(self, name):
        for video in self.videos:
            if video.title == name:
                return video
        return None



    #returns materials checked out by the user
    def get_user_checked_out(self, user):
        # can be changed to desired output... must return either str or list
        return user.getCheckedOut()



    #helper functions to check if objects exsist 
    def check_user(self, user):
        if user in self.users:
            if user.num_checked_out < user.max_items:
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
        if user.max_items > user.num_checked_out:
            return True
        return Flase



    # Helper functions to check material statuses 
    def check_material_status(self, mat):
        if mat.checked_out and mat.renewed:
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
    def checkout_book(self, book, user):
        book = self.get_book(book)
        if book and self.check_material_status(book):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, book)
                return True
            return False
        return False
    
    def checkout_audio(self, audio, user):
        audio = self.get_audio(audio)
        if audio and self.check_material_status(audio):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, audio)
                return True
            return False
        return False
    
    def checkout_video(self, video, user):
        video = self.get_video(video)
        if self.check_material_status(video):
            if self.check_user_status(user):
                self.update_user_checked_out_materials(user, video)
                return True
            return False
        return False



    # updates user's checked out materials
    def update_user_checked_out_materials(self, user, material):
        user.addCheckout(material)
        material.checkout()



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