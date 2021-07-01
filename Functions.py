def function_name(name):
    '''This function is to know the syntax-Multi line comments'''
    print("My name is: "+name)


function_name("Jose")
print('********************************************************')
#functions with return
def sum_func(num1,num2):
    return num1+num2


result=sum_func(5,5)
print(result)
print('********************************************************')
#Taking up the default value if the parameters are not passed during function call
def say_hello(name='Default'):
    print(f'Hello {name},Goodmorning')

say_hello('nancy')
say_hello() # Not passing anything