my_list=[1,2,3,4,5,6,7,8,9,10]
sum=0;
for num in my_list:
    if(num%2==0):
        print(f'{num} is even')

    else:
       print(f'{num} is odd')

    sum=sum+num
print('*************************************')
print(f'Sum is :{sum}')

print('*************************************')
#For loop for string:
my_string='Hello'
for i in my_string:
    print(i)
print('*************************************')
#directly giving string in for loop instead of a variable
for i in 'World':
    print(i)
print('*************************************')
#if we just want to keep iterable without variable name:
for _ in 'Sunset':
    print("Sunset is cool")
print('*************************************')
#For loop in tuples
tup=(1,2,3)
for tup_num in tup:
    print(tup_num)
