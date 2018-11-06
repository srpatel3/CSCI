class User():
	def __init__(self, uName, uID):
		self.userName = uName
		self.userID = uID

	# Setters
	def setUserName(self, uName):
		self.userName = uName

	def setuserID(self,uID):
		self.userID = uID
	
	# Getters
	def getUserName(self):
		return self.userName
	
	def getuserID(self):
		return self.userID
	
	def toString(self):
		return self.userName +"\t\t"+str(self.userID)