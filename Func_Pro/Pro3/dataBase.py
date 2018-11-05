from item import Item
from user import User

class Database():
	
	def __init__(self):
		self.database = {}
		self.users = {}
		self.addItem("Apple", 2, 11, 2222, 100)
		self.addItem("Apple1", 2, 12, 2223, 100)
		self.addItem("Apple2", 2, 13, 2224, 100)

	# Getting Item 
	def addItem(self, name, price, catagory, code, qty):
		itemCode = str(catagory) + str(code)
		itemCode = int(itemCode)
		self.database[itemCode] = Item(name,price, catagory, code, qty) 

	def getItem(self, itemCode):
		return self.database[itemCode]

	def updateQty(self, itemCode, Qty):
		self.database[itemCode].qty -= Qty

	def addUser(self, userId, userName):
		self.users[userId] = User(userId, userName)

	def getUser(self, userId):
		if userId in self.users:
			return True
		else:
			return False
	def printUserList(self):
		print("userID\t\t\tuserName")
		for user in self.users:
			print(user.userId+"\t\t\t"+user.userName)

	def printInventory(self):
		for item in self.database.keys():
			print(str(self.database[item].name)+"\t\t"+str(self.database[item].qty))
