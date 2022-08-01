# basic user class to hold library memeber attributes

class  User:
	def __init__(self):
		self.name = "New User"
		self.address = "N/A"
		self.age = "N/A"
		self.phone_number = "N/A"
		self.card_number = "N/A"
		self.checked_out = []

	def setUser(self, name, addr, age, phone, card, items):
		self.setName(name)
		self.setAddress(addr)
		self.setAge(age)
		self.setPhoneNumber(phone)
		self.setCardNumber(card)
		self.setCheckedOut(items)
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
		self.age = age
	def setPhoneNumber(self, num):
		self.phone_number
	def setCardNumber(self, num):
		self.card_number = num
	def setCheckedOut(self, items):
		if type(items) == list:
			for item in items:
				self.checked_out.append(item)
		else:
			self.checked_out.append(items)
	def __str__(self):
		return f'Name: {self.name} Address: {self.address} Age: {self.age} Phone: {self.phone_number} CID: {self.card_number} Borrowing: {self.checked_out}'


def main():
	user = User()
	user.setUser('alex','home','22', '972....', '123', None)
	print(user)
if __name__ == '__main__':
	main()