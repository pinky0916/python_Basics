#**ARGS is to pass any no of elements to the function. Arbitary no of elements and it is returned as a tuple.
def args_func(*args):
    print(args)
    for item in args:
        print(item)

args_func(1,2,3,4)
print('****************KWARGS****************')
def kwargs_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
      print('My favourite fruit is {}'.format(kwargs['fruit']))
    else:
      print('I did not find any fruit')


kwargs_func(fruit='Apple',veggie='lettuce')

print('****************ARGS &&KWARGS****************')
def arg_kwarg(*args,**kwargs):
    print('Args value is {}'.format(args))
    print('Kwargs value is {}'.format(kwargs))
    print('I would like to eat {} {}'.format(args[0],kwargs['veggie']))

arg_kwarg(1,2,3,4,5,fruit='apple',veggie='cauli')


