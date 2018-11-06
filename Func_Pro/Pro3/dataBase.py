from item import Item
from user import User
import pandas as pd

class Database():

	def __init__(self):
		self.database = {}
		self.users = {}
		self.initDB()

	def initDB(self):
		fileToRead = open("inventory1.csv","r")
		for row in fileToRead:
			items = row.replace("\n","").split(",")
			self.addItem(items[0], float(items[1]), items[2], items[3], float(items[4]), items[5])
		fileToRead.close()
		# self.printInventory()

	# Adding Item
	def addItem(self, name, price, catagory, code, qty, unit):
		itemCode = catagory + code
		itemCode = itemCode
		self.database[itemCode] = Item(name,price, catagory, code, qty, unit)

	def addUser(self, userId, userName):
		self.users[userId] = User(userId, userName)

	# Getting data items
	def getItem(self, itemCode):
		return self.database[itemCode]

	def getUser(self, userId):
		if userId in self.users:
			return True
		else:
			return False

	def updateQty(self,itemCode,qty):
		self.database[itemCode].setQty(self.database[itemCode].getQty()-qty)

	def printUserList(self):
		print("userID\t\t\tuserName")
		for user in self.users:
			print(user.userId+"\t\t\t"+user.userName)

	def updateInventory(self):
		fileToWrite = open("inventory2.csv","w")
		for key in self.database.keys():
			lineToWrite = self.database[key].toString()
			fileToWrite.write(lineToWrite)
		fileToWrite.close()


	def printInventory(self):
		names = [self.database[key].getName() for key in self.database.keys()]
		prices = [self.database[key].getPrice() for key in self.database.keys()]
		qts = [self.database[key].getQty() for key in self.database.keys()]
		units = [self.database[key].getUnit() for key in self.database.keys()]
		dataFrame = pd.DataFrame({'Name':names, "Price":prices, "Quantity":qts, "Unit":units})
		print(dataFrame)

# def main():
# 	DB = Database()
# 	DB.updateInventory()
#
# main()
