#If we have two list to map the values between two list we use zip
#if the no of elements are not consistent across lists,it will not throw error but rather takes the minimum count
list1=[1,2,3,4,5]
list2=['a','b','c','d','e','f','g','h']
list3=[100,200,300,400,500]
for i in zip(list1,list2,list3):
    print(i)

print('***************************************')
#for unpacking:
for x,y,z in zip(list1,list2,list3):
    print(y)
print('***************************************')
#to put this tuple as a list
print(list(zip(list1,list2,list3)))