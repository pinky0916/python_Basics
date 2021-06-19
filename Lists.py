#Ordered sequence of elements and it can have mixed object type
#Support slicing and indexing
a=[1,2,3]
b=[1,'STRING',23.55]

# to check the length of the string
print(len(b))

#Concatenate lists
listA=[1,2,3]
listB=['VARI','SHTAJA',6]
listC=listA+listB
print('Old list:{}'.format(listC))

#Lists are mutable
#Can change the elements of the list
listC[5]='Changed element'
print('New list:{}'.format(listC))

#to append the new list
listC.append(7)
print('Appended list:{}'.format(listC))

#to remove elements from the list
listC.pop(0)
print('Poped list:{}'.format(listC))
listC.pop()
print('Poped list2:{}'.format(listC))

#Sorting the list-sorts in place doesnt return anything
my_list=[5,3,1]
my_list.sort()
print(my_list)


#Reverse the list:
list2=[1,2,3]
list2.reverse()
print(list2)

#How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
a=[1,1,[1,2]]
print(a[2][1])