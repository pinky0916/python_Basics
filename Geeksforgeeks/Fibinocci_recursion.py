def feb_rec(num):
    feb_list=[]
    for i in range(0,num):
        if(i==0):
            feb_list.append(0)
        elif(i==1):
            feb_list.append(1)
        else:
            sum=feb_list[-1]+feb_list[-2]
            feb_list.append(sum)
    return feb_list


num=0
while (num==0):
   num=int(input("Enter the number:"))
feb_list=feb_rec(num)
print(feb_list)

