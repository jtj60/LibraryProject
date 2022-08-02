class Material:
	def __init__(self, title, rating, checked_out, renewed, returned):
		self.title = None
		self.rating= None
		self.checked_out = False
		self.renewed = False
		self.returned = False
		self.due_date = None
		self.setMaterial(title, rating, checked_out, renewed, returned)
	def setMaterial(self, title, rating):
		self.setTitle(title)
		self.setRating(rating)
		self.checked_out = checked_out
		self.renewed = renewed
		self.returned = returned
	def setRating(self, rating):
		self.rating = rating if rating >= 0 else 0
	def setTitle(self, name):
		self.title = name
	def setDueDate(self, date):
		self.due_date = date
	def checkout(self, time):
		if not self.checked_out:
			print(f'checking out {self.title} for {self.rental_time} days')
			self.setDueDate(time)
			self.checked_out = True
	def checkin(self):
		if checked_out:
			print(f'checking in {self.title}')
			self.due_date = None
			self.checked_out = False
			self.renewed = False
	def renew(self):
		if not self.renewed:
			self.checkin()
			self.checkout()
			self.renewed = True

class Book(Material):
	rental_time = 21
	def __init__(self, title, author, genre, rating, best_seller, checked_out, renewed, reference, returned):
		super().__init__(title, rating, checked_out, renewed, returned)
		self.author = 'None'
		self.genre = 'None'
		self.best_seller = False
		self.reference = False
		self.setBook(author, genre, best_seller, reference)

	def setBook(self, author, genre, best_seller, reference):
		self.author = author
		self.genre = genre
		self.best_seller = best_seller
		self.reference = renference
		if self.best_seller:
			self.rental_time = 14
	
	def checkout(self):
		super().checkout(self.rental_time)
	

class Video(Material):
	rental_time = 14
	def __init__(self, title, rating, duration, checked_out, renewed, returned):
		super().__init__(title, rating, checked_out, renewed, returned)
		self.duration = None
		self.setVideo(duration)
	def setVideo(self, duration):
		self.duration = duration
	def checkout(self):
		super().checkout(self.rental_time)
class Audio(Video):
	def __init__(self):
		super().__init__(title, rating, checked_out, renewed, returned)
Title:, Genre:, Rating:, Duration:, Checked Out:, Renewed:, Returned:
def main():

if __name__ == '__main__':
	main()