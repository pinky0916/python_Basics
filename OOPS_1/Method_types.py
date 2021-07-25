class Student:
    #Defining a class/static variable
    school='Telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

# Below 3 methods are instance methods
    def avge(self):
        avg_mark=self.m1+self.m2+self.m3/3
        return avg_mark

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1=value
        return self.m1

#Class method- use cls instead of self
    @classmethod  # decorator shuld be used otherwise throws class_method() missing 1 required positional argument: 'cls'
    def class_method(cls):
       return cls.school
#Static method:
    @staticmethod
    def static_method():
       print("Inside Static method")

s1=Student(10,20,30)
s2=Student(20,20,30)

print(s1.avge())
print(s2.avge())

#calling the accessor and mutator methods
print(f'Get method is :{s1.get_m1()}')
print(f'Set method is :{s1.set_m1(100)}')

#Calling the Class method
print(f'Class method is : {Student.class_method()}')


#Calling the instance method:
print(f'Calling the static method : {Student.static_method()}')