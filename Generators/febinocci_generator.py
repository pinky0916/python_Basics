def febinocci_series(num):

    feb_list=[]

    for i in range(0,num):
        if i==0:
           current=0
           feb_list.append(current)
        elif i==1:
           current=1
           feb_list.append(current)
        else:
           current=feb_list[i-1]
           previous=feb_list[i-2]
           sum=current+previous
           feb_list.append(sum)
    print(feb_list)



num=int(input("Enter the no for which you want the feb series:"))
febinocci_series(num)
