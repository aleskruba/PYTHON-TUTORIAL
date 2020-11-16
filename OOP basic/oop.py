class Shopping:
    def __init__(self,product,price,number):
        self.product = product
        self.price = price
        self.number = number
        self.total = self.price * self.number

    def update_numbers(self,new_number):
        self.number = new_number
        self.total = new_number * self.price

    def __str__(self):
         return "{} items of product '{}' /1 colli ${}/ . price ${} ".format(self.number,self.product,self.price,self.total)


p1 = Shopping('bread',3,3)
print(p1)
p2 = Shopping('Milk',1.3, 5)
print(p2)
print()
p3 = p1.total + p2.total
print("total price",p3)
print()
p1.update_numbers(5)
print(p1)
p2.update_numbers(8)
print(p2)

p3 = p1.total + p2.total
print("total price",p3)