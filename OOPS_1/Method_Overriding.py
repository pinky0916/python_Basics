class A:
    def show(self):
        print("Inside Parent class-A")
class B(A):
    def show(self):
        print("Inside child class-B")

s1=B()
s1.show()