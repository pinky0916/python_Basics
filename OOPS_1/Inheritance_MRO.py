class A:
    def __init__(self):
        print("A constructor")
    def methodA(self):
        print("A method:")
class B:
    def __init__(self):
        print("B constructor")
    def methodB(self):
        print("B method:")

class C(A,B):
    def __init__(self):
        print("C constructor")
        super().__init__()
    def methodC(self):
        print("C method:")
        #super().methodA()

c1=C()
c1.methodA()
