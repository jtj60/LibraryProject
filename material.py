class Material:
	def __init__(self, title, rating, checked_out, renewed, returned):
		self.title = None
		self.rating= None
		self.checked_out = False
		self.renewed = False
		self.returned = False
		self.due_date = None
		self.setMaterial(title, rating, checked_out, renewed, returned)
	def setMaterial(self, title, rating, checked_out, renewed, returned):
		self.setTitle(title)
		self.setRating(rating)
		self.setCheckedOut(checked_out)
		self.setRenewed(renewed)
		self.setReturned(returned)
	def setCheckedOut(self, checked_out):
		self.checked_out = checked_out
	def setRenewed(self, renewed):
		self.renewed = renewed
	def setReturned(self, returned):
		self.returned = returned
	def setRating(self, rating):
		self.rating = rating
	def setTitle(self, name):
		self.title = name
	def setDueDate(self, date):
		self.due_date = date
	def checkout(self, time):
		if not self.checked_out:
			print(f'checking out {self.title} for {self.rental_time} days')
			self.setDueDate(time)
			self.setCheckedOut(True)
	def checkin(self):
		if self.checked_out:
			print(f'checking in {self.title}')
			self.due_date = None
			self.setCheckedOut(False)
			self.setRenewed(False)
	def renew(self):
		if not self.renewed:
			self.checkin()
			self.checkout()
			self.setRenewed(True)
		else:
			print('Already renewed!!!')

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
		self.setBestSeller(best_seller)
		self.reference = reference
		if self.best_seller:
			self.rental_time = 14
	def setBestSeller(self, best_seller):
		best_seller = str(best_seller).lower()
		if best_seller == 'true' or best_seller == 'yes':
			self.best_seller = True
		else:
			self.best_seller = False
	def checkout(self):
		super().checkout(self.rental_time)
	def __str__(self):
		return f'Title: {self.title} Author: {self.author} Genre: {self.genre} Rating: {self.rating} Available: {not self.checked_out}'
	
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
	def __init__(self, title, genre, rating, duration, checked_out, renewed, returned):
		super().__init__(title, rating, duration, checked_out, renewed, returned)
		self.genre = None
		self.setAudio(genre)
	def setAudio(genre):
		self.genre = genre

def main():
	# title, author, genre, rating, best_seller, checked_out, renewed, reference, returned):
	b = Book('Greenlights', 'Mathew McConahey', 'Autobiography', '5', True, False, False, False, False)
	b.checkout()
	b.renew()
	b.renew()
if __name__ == '__main__':
	main()