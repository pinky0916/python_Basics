''' Class B is inheriting from A
Case:2- Class B has no __init__ constructor-then if A has __init__ it will print that
Case:1- Class B has __init__ constructor-it will access B __init_constructor
Case:3- if A and B has __iniT__ and wants to access both A and B init


'''
#Both B and A exist-calls B
class A:
    def __init__(self):
        print("A constructor")
    def A_method(self):
        print("A method")
class B(A):
    def __init__(self):
        print("B constructor")
    def B_method(self):
        print("B method")


s1=B()

print ('**Case 2****')
# A exist B doesnt exist-calls A
# sub class constructor not there goes to super class
class A:
    def __init__(self):
        print("A constructor")
    def A_method(self):
        print("A method")

class B(A):
    #def __init__(self):
        #print("B constructor")
    def B_method(self):
        print("B method")


s1=B()

print('**Case 3****')


# Needs to access both __init__ constructor
class A:
    def __init__(self):
        print("A constructor")

    def a_method(self):
        print("A method")


class B(A):
     def __init__(self):
         print("B constructor")
         super().__init__()
     def b_method(self):
         print("B method")


s1 = B()
