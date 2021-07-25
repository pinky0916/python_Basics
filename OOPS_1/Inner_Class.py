class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        #defining the inner class object
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.age)

#Inner class
    class Laptop():
       def __init__(self):
           self.RAM='5TB'
           self.CPU=200

#Object created
s1=Student("Alex",60)
s2=Student("Tom",20)

s1.show()

# To access the inner class objects.
print(s1.lap.CPU)
