#Creating objects of inner class outside of Outer class
class College:
    def __init__(self):
        print("Outer class constructor")
    def displayC(self):
        print("Outer class Method")

    class Student:
        def __init__(self):
            print("Inner class constructor")
        def displayS(self):
            print("Inner class method")

# To access Outer class
c1=College()
c1.displayC()


#To access inner class methods-Method 1
s2=c1.Student()
s2.displayS()
print('**********Method2*******************')

#Method2:
s3=College().Student()
s3.displayS()
#s3.displayC()  -Throws Error
print('**********Method3*******************')
#Method 3
s4=College.Student()
s4.displayS()
