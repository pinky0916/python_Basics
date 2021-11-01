class Computer:
    #Attributes
    def __init__(self):
        self.ram='8 GB'
        self.cpu='i5'

    #Methods
    def update(self):
        self.cpu='i9'

    def compare(self,other):
        if self.cpu==other.cpu:
            return True
        else:
            return False

c1=Computer()
c2=Computer()

c2.cpu='i8'
c1.update()
value=c1.compare(c2)
print(value)



print("C1:",c1.cpu,c1.ram)
print("C2:",c2.cpu,c2.ram)

