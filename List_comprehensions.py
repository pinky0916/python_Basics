#to add the elements to a list

my_string='Hello'
list1=[]
for a in my_string:
    list1.append(a)
print(list1)
print('********************************************************')
#This is the traditional method instead of this can use list comprehensions
list2=[]
list2=[number for number in my_string]
print(list2)
print('********************************************************')
my_list=[x for x in 'Wordnkmk']
print(my_list)
print(list2)
print('********************************************************')
#Creating list from range of values
my_list_num=[x for x in range(0,10)]
print(my_list_num)
print('********************************************************')
#Creating list from range of values
sq_num=[x**2 for x in range(0,10)]
print(sq_num)
print('********************************************************')
#can also add conditions
even_num=[num**2 for num in range(0,12) if num%2==0]
print(even_num)
print('********************************************************')
#to convert degree to Farenheit
celsius=[0,10,20,34.5]
farenheit=[((9/5)*temp+32) for temp in celsius]
print(farenheit)
print('********************************************************')
#list comprehensions with if and else:- order is changed
list3=[x if x%2==0 else 'ODD' for x in range(1,12)]
print(list3)
print('********************************************************')
#List comprehensions with for and inner for loop
list4=[x*y for x in (1,2,3) for y in (1,10,100)]
print(list4)



