#Multiple level inheritance
class A:
    def feature1(self):
        print("Inside Super class method-1")
    def feature2(self):
        print("Inside super class method-2")
class B:
    def feature3(self):
        print("Inside Sub class method-1")
    def feature4(self):
        print("Inside sub class method-2")

class C(A,B):
    def feature5(self):
        print("Inside Sub class-C method-1")



#Creating Class C object
s4=C()
s4.feature1()
