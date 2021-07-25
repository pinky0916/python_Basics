class Student:

    def __init__(self):
        self.name="Ravi"
        self.age=28
    def compare(self,other):
        if (self.age==other.age):
            return True
        else:
            return False

c1=Student()
# changing the value of c1 object
c1.age=50
c2=Student()

if c1.compare(c2):
    print("They are same")
else:
    print("They are Different")

print(f'C1-Name is : {c1.name},age is {c1.age}')
print(f'C2-Name is : {c2.name},age is {c2.age}')
