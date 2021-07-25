class Class_Demo:
    '''__init__ method- This is a special method used to initiate the variable.
It gets called automatically when the object gets created
It will be called once with each object.If there are two objects ,it will be called twice
'''
    def __init__(self,cpu,ram):
        print("Inside Init")
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Inside method-config")
        print(f'Config of the object is of ram :{self.ram} and cpu:{self.cpu}')



# Object is getting created c1 and c2 of the same class
c1=Class_Demo('i5',500)
c2=Class_Demo('i9',250)

#Calling the methods for the object
c1.config()
c2.config()

