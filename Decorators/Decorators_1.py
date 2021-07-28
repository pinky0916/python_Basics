#functions returning another function
def hello(name='Jose'):
    print("The hello() func is executed")

    def greet():
        return "\t This is the greet () func inside hello"


    def welcome():
        return '\t This is welcome() inside hello'

    #print(greet())
    #print(welcome())
    print(name)
    if name=='Jose':
        return greet
    else:
        return welcome


welcome=hello('AA')
print(welcome())