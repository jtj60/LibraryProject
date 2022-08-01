class  User:
	def __init__(self):
		self.name = "New User"
		self.address = "N/A"
		self.age = "N/A"
		self.phone_number = "N/A"
		self.card_number = "N/A"
		self.checked_out = []

	def setName(self, n):
		self.name = n
	def setAddress(self, addr):
		self.address = addr
	def setAge(self, a):
		self.age = a
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
