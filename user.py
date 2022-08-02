# basic user class to hold library memeber attributes

class  User:
	def __init__(self):
		self.name = "New User"
		self.address = "N/A"
		self.age = "N/A"
		self.phone_number = "N/A"
		self.card_number = "N/A"
		self.checked_out = []
		self.password = 0
		self.max_items = 12
		self.num_checked_out = 0

	def setUser(self, name, addr, age, phone, card, items, pswd):
		self.setName(name)
		self.setAddress(addr)
		self.setAge(age)
		self.setPhoneNumber(phone)
		self.setCardNumber(card)
		self.setCheckedOut(items)
		self.setPassword(pswd)
		self.num_checked_out = self.getNumCheckedOut()
	def setName(self, n):
		self.name = n
	def setAddress(self, addr):
		self.address = addr
	def setAge(self, a):
		age = a
		if type(age) == str:
			try:
				age = float(age)
			except:
				age = 0
		# check for age requirement
		if age <= 12:
			self.max_items = 5
		self.age = age
	def setPhoneNumber(self, num):
		self.phone_number = num
	def setCardNumber(self, num):
		self.card_number = num
	def setCheckedOut(self, items):
		if type(items) != list:	
			items = items.split('-')
		for item in items:
				self.addCheckout(item)
	def setPassword(self, pswd):
		self.password = pswd
	def getCheckedOut(self):
		checked_out = None
		if self.checked_out:
			if self.checked_out[0] != None:
				checked_out = self.checked_out
		return checked_out
	def __str__(self):
		return f'Name: {self.name} Address: {self.address} Age: {self.age} Phone: {self.phone_number} CID: {self.card_number} Borrowing: {self.checked_out}, Pswd: {self.password}'
	def getNumCheckedOut(self):
		if self.checked_out[0] == None:
			return 0
		return len(self.checked_out)
	def addCheckout(self, item):
		self.checked_out.append(item)
		self.num_checked_out += 1
	def checkIn(self, item):
		if item in self.checked_out:
			self.checked_out.remove(item)
			self.num_checked_out -= 1
			return True
		else:
			return False


def main():
	user = User()
	user.setUser('alex','home','22', '972....', '123', None)
	print(user)
	user.setCheckedOut('a book')
	print(user)
if __name__ == '__main__':
	main()