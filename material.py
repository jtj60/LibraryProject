class Material:
	def __init__(self):
		self.name = 'No name'
		self.due_date = None
	def setName(self, name):
		self.name = name
	def setDueDate(self, date):
		self.due_date = date
	def checkout(self, time):
		self.setDueDate(time)
		print(f'checking out {self.name} for {self.rental_time} days')
	def checkin(self):
		print(f'checking in {self.name}')
		self.due_date = None
	def renew(self):
		self.checkin()
		self.checkout()

class Book(Material):
	rental_time = 21
	def __init__(self):
		super().__init__()
	def checkout(self):
		super().checkout(self.rental_time)
	
class BestSeller(Book):
	rental_time = 14
	def __init__(self):
		super().__init__()
		#self.retal_time = retal_time

class Video(Material):
	rental_time = 14
	def __init__(self):
		super().__init__()
	def checkout(self):
		super().checkout(self.rental_time)
class Audio(Video):
	def __init__(self):
		super().__init__()

def main():
	bs = BestSeller()
	bs.setName('Twilight')
	bs.checkout()
	bs.renew()
	
	bk = Book()
	bk.setName('Bear Bears')
	bk.checkout()
	bk.checkin()

	vd = Video()
	vd.setName('3 Stooges')
	vd.checkout()
	vd.renew()

if __name__ == '__main__':
	main()