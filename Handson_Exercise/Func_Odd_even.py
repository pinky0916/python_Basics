def odd_even(num):
    if num%2==0:
        print(f'The number {num} is even')
    else:
        print(f'The number {num} is odd')

odd_even(21)
print('*****************************************')


def list_even_check(list1):
    for num in list1:
        if num%2==0:
            even_flag=1
            break
        else:
            even_flag=0
    if even_flag==1:
        print("The list has even numbers")
    else:
        print('The list has only odd numbers')

list1=[1,1,3,5,7,9999,10]
even_flag=0
list_even_check(list1)

print('*****************************************')

def even_check(list2,even_list):
    for num in list2:
        if num%2==0:
            even_list.append(num)
            continue
        else:
            pass
    return even_list
list2=[1,5,7,9,11,999,100]
even_list=[]
even_list_final=even_check(list2,even_list)
print(even_list_final)
