from dataBase import Database
from item import Item
from user import User

class Cart():
	database = Database()
	def __init__(self, userID, userName):
		if Cart.database.getUser(userID):
			Cart.database.addUser(userID, userName)
			self.user = Cart.database.getUser(userID)
		else:
			self.user = Cart.database.addUser(userID, userName)
			
		self.itemList = []

	def addItem(self, itemCode, qty):
		temp = Cart.database.getItem(itemCode)
		item = Item(temp.name, temp.price, temp.catagory, temp.code, temp.qty) 
		item.qty = qty
		item.price = qty * item.price
		self.itemList.append(item)
		self.printList()

	def printList(self):
		print("Item\t\tQty\t\tTotal")
		print("--------------------------------------")
		# print("\n")
		for item in self.itemList:
			# print item.name
			print(item.name+"\t\t"+str(item.qty)+"\t\t"+str(item.price))
		print("\n\n")
	
	def removeItem(self, itemCode):
		# print "Here"
		for item in self.itemList:
			# print str(item.catagory)
			# print str(item.code)
			if str(item.catagory)+str(item.code) == str(itemCode):
				self.itemList.remove(item)
				break	
		self.printList()
		
	def calcSubTotal(self):
		total = 0
		self.printList()
		print("--------------------------------------")
		for item in self.itemList:
			itemCode = str(item.catagory) + str(item.code)
			Cart.database.updateQty(int(itemCode), item.qty)
			total += item.price
		print("\t\tSub Total\t"+str(total)) 
		tax = 0.07*total
		print("\t\tTax\t\t"+str(tax)) 
		total += tax
		print("\t\tAmount Due\t"+str(total)) 
		print("\n\n")
		self.printDataBase()

	def printDataBase(self):
		Cart.database.printInventory()
