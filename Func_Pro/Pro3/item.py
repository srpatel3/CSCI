class Item():
    def __init__(self, name, price, catagory, code, qty, unit):
        self.name = name
        self.qty = qty
        self.price = price
        self.catagory = catagory
        self.code = code
        self.unit = unit

    # Setter Methods
    def setName(self,name):
        self.name = name

    def setPrice(self, price):
        self.price = price
    
    def setCatagory(self,catagory):
        self.catagory = catagory
    
    def setCode(self, code):
        self.code = code
    
    def setQty(self, qty):
        self.qty = qty

    def setUnit(self,unit):
        self.unit = unit

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCatagory(self):
        return self.catagory

    def getCode(self):
        return self.code

    def getQty(self):
        return self.qty

    def getUnit(self):
        return self.unit 

    def toString(self):
        return self.name+","+str(self.price)+","+self.catagory+","+self.code+","+str(self.qty)+","+self.unit+"\n"
