class A:
    def feature1(self):
        print("Inside Super class method-1")
    def feature2(self):
        print("Inside super class method-2")
class B(A):
    def feature3(self):
        print("Inside Sub class method-1")
    def feature4(self):
        print("Inside sub class method-2")

class C(B):
    def feature5(self):
        print("Inside Sub class-C method-1")

class D(A,B): #Multiple inheritance
    def feature6(self):
        print("Inside Sub class-D method-1")

#Creating Class B object
s2=B()
s2.feature1()


#Creating Class C object
s3=C()
s3.feature1()

#Creating Class D object
s4=D()
s4.feature1
