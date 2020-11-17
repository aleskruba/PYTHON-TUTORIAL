class Shopping:
    def __init__(self,product,price,number):
        self.product = product
        self.price = price
        self.number = number
        self.total = self.price * self.number
        self.stock = 100

    def update_numbers(self,new_number):
        self.number = new_number
        self.total = new_number * self.price
        self.stock = self.stock - new_number
    def __str__(self):
         return "the price of {} item of the '{}'  product is price ${} ".format(self.number,self.product,self.total)

    def stock(self):
        return "stock is {}".format(self.stock)

p1 = Shopping('bread',3,1)
print(p1)
p2 = Shopping('Milk',1.3, 1)
print(p2)
print(f"stock: {p1.stock}/bread,   {p2.stock}/milk")
print("-------------------------------------------------")
print("first day")
print()
print("INFO FOR CUSTOMER")
p1.update_numbers(5)
print(p1)
p2.update_numbers(10)
print(p2)
p3 = p1.total + p2.total
print("Total price : ",p3)
print()
print("INFO FOR WAREHOUSE")
print("total price",p3)
print("Stock of  ",p1.product, "is", p1.stock)
print("Stock of  ",p2.product, "is", p2.stock)
print("-------------------------------------------------")
print("second day")
print()
print("INFO FOR CUSTOMER")
p1.update_numbers(5)
print(p1)
p2.update_numbers(5)
print(p2)
p3 = p1.total + p2.total
print("Total price : ",p3)
print()
print("INFO FOR WAREHOUSE")
print("total price",p3)
print("Stock of  ",p1.product, "is", p1.stock)
print("Stock of  ",p2.product, "is", p2.stock)
