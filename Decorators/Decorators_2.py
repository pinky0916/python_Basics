#its passing one function to another function
def hello():
    print("Am inside hello")

def some_other_fun(func):
    print("inside some other func")
    print(func())

some_other_fun(hello)