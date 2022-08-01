# This code is not working or functional or tested, although that will change tonight or tomorrow. 
# It's mostly here as demonstration; feel free to change things as you see fit


import csv

class Library():
    def __init__(self):

        self.users = []
        self.staff = []
        self.books = []
        self.audio = []
        self.videos = []
    

    #not really something to implement in the interface, more to just showcase what everything will look like
    def add_user(self, name):
        if self.check_user(name):
            return False

        user = {
            "name": name,
            "address": address,
            "age": age,
            "phone-number": phone_number,
            "card-number": card_number,
            "checked-out": checked_out,
        }
        self.users.append(user)

        with open('user.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([user.name, user.address, user.age, user.phone_number, user.card_number, user.checked_out])
            csvfile.close()

        return True

    def get_user(self, card_number):
        for user in self.users:
            if user['card-number'] == card_number:
                return user
        return None

    def check_user(self, name):
        for user in self.users:
            if user['name'].lower() == name.lower():
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
    
    def check_user_status(self, user):
        if user["age"] <= 12:
            if user["items_amount"] < 5:
                return True
            return False
        return True


    def check_book_status(self, book):
        if book["checked_out"] == 'yes' and book["renewed"] == 'yes':
            return False
        
        if book["reference"] == 'yes':
            return False

        else:
            return True
    
    def check_audio_status(self, audio):
        pass

    
    def check_video_status(self, video):
        pass

    
    def request_book(self, book, user):
        if self.check_book(book["name"]):
            if self.check_book_status(book):
                return True
            return False
        return False


    def request_audio(self, audio, user):
        pass

    
    def request_video(self, video, user):
        pass


    def checkout_book(self, book, user):
        if self.check_book_status(book):
            if self.check_user_status(user):
                with open('user.csv', 'w') as csvfile:
                    writer = csv.writer(csvfile)
                    #edit csvs
                return True
            return False
        return False

    
    def checkout_audio(self):
        pass

    
    def checkout_video(self):
        pass

    
