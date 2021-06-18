#2 Methods
#1.format method
#2.f-string method
#***********************
#.format-Method 1
print('The format method is  {} very helpful {}'.format('INSERT1','INSERT2'))

#.format-Method 2- to add the order
print('The format method is  {1} very helpful {0}'.format('INSERT1','INSERT2'))

#.format-Method 3- to add the order
print('The format method is {a} very helpful {b}'.format(a='INSERT1',b='INSERT2'))

print('The format method is {b} very helpful {a}'.format(a='INSERT1',b='INSERT2'))

#FLOAT FORMATTING: {value:width.precisionf}
result=100/777
print('The result is {p:1.3f}'.format(p=result))
print('The result is {p:10.3f}'.format(p=result))

#***********************************************************************************************/
#f String method
x='apple'
print(f'The format string is {x}')
#f String method-Multiple values

name='Sam'
age=23
print(f'{name} is {age} years old')
