import random
from cart import Cart
def clearScreen():
	for i in range(0,100):
		print("\n")

def main():
	input = 0
	name = raw_input("Enter Your Name:\n")
	cart = Cart(random.randint(100,1000), name)
	clearScreen()
	print("Welcome to WWM " + name) 
	while not input == 5:
		try:
			print("Enter Your Choice:\n1.Add Item\n2.Remove Item\n3.Check Out\n4.View Cart\n5.Cancle Transaction")
			input = int(raw_input())
			if input == 1:
				itemCode = int(raw_input("Enter Item Code:\n"))
				qty = int(raw_input("Enter Quantity:\n"))
				clearScreen()
				cart.addItem(itemCode, qty)
			elif input == 2:
				print "Case 2"
				itemCode1 = int(raw_input("Enter Item Code:\n"))
				clearScreen()
				cart.removeItem(itemCode1)				
			elif input == 3:
				clearScreen()
				cart.calcSubTotal()
				print("Thank you for shopping at WWM")
				print("\n\n")
				break
			elif input == 4:
				clearScreen()
				cart.printList()
			elif input == 5:
				clearScreen()
				cart.printDataBase()
				print("Transaction cancelled. Thanks for visiting WWM")
			else:
				print("Wrong Choice Try Again...!!!")
		except Exception as e:
			print e
			print("Something went wrong try again...")	

if __name__ == "__main__": 
	main()
