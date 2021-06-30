list1=[1,2,3,999,5,100,0]
min_value=min(list1)
max_value=max(list1)
print(f'Minimum value is :{min_value}')
print(f'Maximum value is :{max_value}')
print('********************************')

from random import shuffle
shuffle(list1) #shuffle happens in in place
print(list1)
print('********************************')
#randominteger

from random import randint
random_num=randint(0,100)
print(f'Random integer is:{random_num}')


