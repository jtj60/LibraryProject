import csv

Class Library():
    def __init__(self):

        self.users = []
        self.books = []
        self.audio = []
        self.video = []
    
    def add_user(self):
        if self.checkUser(name):
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


    def check_user(self):
        for user in self.users:
            if user['name'].lower() == name.lower():
                return True
        return False


    def checkout_book(self):

    
    def checkout_audio(self):

    
    def checkout_video(self):

    
