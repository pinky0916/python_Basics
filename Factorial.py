num=6
factorial=num
mf=1
if num<0:
    print("Input a positive number to find factorial")
elif (num==1):
    factorial=1
else:
   while (num!=1):
        mf=num-1
        factorial=factorial*mf
        num=num-1
   print(f'Factorial of the number is {factorial}')
