def maximum_value(list1):
    for i in range(0,len(list1)):
        if i==0:
           max_value=list1[i]
           min_value=list1[i]


        elif i>0:
            if list1[i]>=max_value:
               max_value=list1[i]
               #print(f'Max_value is {max_value}')
            elif list1[i]<min_value:
               min_value=list1[i]


    return max_value,min_value

list1=[]
num=int(input("Enter the no: of elemnts in the list"))

for i in range(1,num+1):
    n1=int(input("Enter the elements:"))
    list1.append(n1)
print(list1)


maximum_value1,minimum_value1=maximum_value(list1)
print(f'Maximum value:{maximum_value1}')
print(f'Minimum value:{minimum_value1}')
secondlargest1=secondlargest(maximum_value1,minimum_value1)