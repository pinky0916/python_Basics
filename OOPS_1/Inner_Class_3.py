class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        #Object of inner class defined inside outer class
        self.lap1=self.Laptop()

    def show(self):
        print(f"Inside Outer show Method: {self.name}")
        self.lap1.show()

    class Laptop:
        def __init__(self):
            self.brand='Hp'

        def show(self):
           print(f"Inside Inner show Method: {self.brand}")


s1=Student('Arun',60)
print('Outer class:',s1.name,s1.marks)
print('Inner class:',s1.lap1.brand)


#Suppose if we want to create another object
'''
s3=s1.lap1
s4=s1.lap1
print(s3.brand)
'''
s1.show()
