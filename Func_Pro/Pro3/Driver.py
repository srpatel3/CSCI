import random
from cart import Cart
def clearScreen():
	for i in range(0,100):
		print("\n")

def main():
	inFromKey = 0
	name = input("Enter Your Name:\n")
	cart = Cart(random.randint(100,1000), name)
	clearScreen()
	print("Welcome to WWM " + name)
	while not inFromKey == 5:
		try:
			print("Enter Your Choice:\n1.Add Item\n2.Remove Item\n3.Check Out\n4.View Cart\n5.Cancle Transaction")
			inFromKey = int(input())
			if inFromKey == 1:
				itemCode = input("Enter Item Code:\n")
				unit = cart.getUnit(itemCode)
				qty = float(input("Enter Quantity in " +unit+":\n"))
				clearScreen()
				cart.addItem(itemCode, qty)
			elif inFromKey == 2:
				itemCode1 = input("Enter Item Code:\n")
				clearScreen()
				cart.removeItem(itemCode1)
			elif inFromKey == 3:
				clearScreen()
				cart.calcSubTotal()
				print("Thank you for shopping at WWM")
				print("\n\n")
				break
			elif inFromKey == 4:
				clearScreen()
				cart.printList()
				print("\n\n\n")
			elif inFromKey == 5:
				clearScreen()
				print("Transaction cancelled. Thanks for visiting WWM")
			else:
				print("Wrong Choice Try Again...!!!")
		except Exception as e:
			# print e
			print("Something went wrong try again...")

if __name__ == "__main__":
	main()
