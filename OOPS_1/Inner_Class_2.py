#Creating objects of inner class  in outer class
class Student:
    def __init__(self):
        self.name='ALEX'
        self.age=28

        #Creating objects of inner class-lap1-Method-1
        self.lap=self.Laptop()

    def display(self):
        print(f'Outer class method is:{self.name} and {self.age}')
        self.lap.display()

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'

        def display(self):
            print(f'Inner class method is:{self.brand} and {self.cpu}')


s1=Student()
s1.display()

#Creating objects with outer class object.inner class object defined within outer classs
#lap1=s1.lap
#lap1.display()



