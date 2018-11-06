from dataBase import Database
from item import Item
from user import User
import pandas as pd

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
		for item in self.itemList:
			if item.getCatagory()+item.getCode() == str(itemCode):
				if item.getQty()+qty < temp.getQty():
					item.setQty(item.getQty()+qty)
					item.setPrice(item.getPrice() + qty*temp.getPrice())
					self.printList()
					print("\n\n\n")
					return
				else:
					print("Do not have enought Quantity | Can not add item to cart")
					print("\n")
					self.printList()
					print("\n\n\n")
					return
		item = Item(temp.getName(), temp.getPrice(), temp.getCatagory(), temp.getCode(), temp.getQty(), temp.getUnit())
		if temp.getQty() > qty:
			item.setQty(qty)
			item.setPrice(qty * item.getPrice())
			self.itemList.append(item)
			self.printList()
			print("\n\n\n")
		else:
			print("Do not have enought Quantity | Can not add item to cart")
			print("\n")
			self.printList()
			print("\n\n\n")

	def getUnit(self, itemCode):
		return Cart.database.getItem(itemCode).getUnit()

	def printList(self):
		names = [item.getName() for item in self.itemList]
		qts = [item.getQty() for item in self.itemList]
		units = [item.getUnit() for item in self.itemList]
		cost = [item.getPrice() for item in self.itemList]
		dataFrame = pd.DataFrame({"Name":names, "Quantity": qts, "Unit":units, "Cost":cost},columns=["Name","Quantity","Unit","Cost"])
		print(dataFrame)

	def removeItem(self, itemCode):
		for item in self.itemList:
			if str(item.getCatagory())+str(item.getCode()) == str(itemCode):
				self.itemList.remove(item)
				break
		self.printList()
		print("\n\n\n")

	def getTaxes(self,amt):
		return amt*0.07

	def calcSubTotal(self):
		total = 0
		self.printList()
		print("--------------------------------------")
		for item in self.itemList:
			itemCode = str(item.catagory) + str(item.code)
			Cart.database.updateQty(itemCode, item.qty)
			total += item.price
		print("\t\tSub Total\t"+str(total))
		tax = self.getTaxes(total)
		print("\t\tTax\t\t"+str(tax))
		total += tax
		print("\t\tAmount Due\t"+str(total))
		print("\n\n\n")
		self.updateDataBase()

	def printDataBase(self):
		Cart.database.printInventory()
	def updateDataBase(self):
		Cart.database.updateInventory()
