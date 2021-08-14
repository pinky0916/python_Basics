def Biggest(list1):

    return list1[-1]

def Smallest(list1):
    return list1[0]

def secondlargest(list1):
    for i in range(0,len(list1)):
        if i==0:
           max_value=list1[i]
           min_value=list1[i]
           break
        elif i>0:
            if list1[i]>max_value:
               max_value=list1[i]
            elif list1[i]<max_value:
               pass
    return max_value

list1=[]
num=int(input("Enter the no: of elemnts in the list"))

for i in range(1,num+1):
    n1=int(input("Enter the elements:"))
    list1.append(n1)
print(list1)
list1.sort()
largest=Biggest(list1)
print(f'Largest Element is:{largest}')

smallest=Smallest(list1)
print(f'smallest Element is:{smallest}')

secondlargest_value=secondlargest(list1)
print(f'secondlargest:{secondlargest_value}')

