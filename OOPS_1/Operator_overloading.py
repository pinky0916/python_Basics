class Book:
    def __init__(self,price):
        self.price=price
    def __add__(self, other):
        return self.price+other.price

    def __lt__(self, other):
        if (self.price>other.price):
            print("Object b1 has higher price")
        elif (self.price<other.price):
            print("Object b2 has higher price")
        else:
            print("Both are equal")
b1=Book(100)
b2=Book(20)
total_price=b1+b2
print(total_price)
compare=b1<b2

