#Single Level and Multi level
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


#Creating Class B object
s2=B()
s2.feature1()

print("***Multi level inheritance*****")

#Creating Class C object
s3=C()
s3.feature2()

