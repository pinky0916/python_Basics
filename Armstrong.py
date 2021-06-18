

def armstrong_check(num_var):
    sum=0
    num=int(num_var)
    digits=len(num_var)
    for i in num_var:
        num1=int(i)
        sum=sum+pow(num1,digits)

    if sum==int(num_var):
        print(f'{sum} is an armstrong number')
    else:
        print(f'{num} is not an armstrong number')


num_var=(input('Enter a number:'))

armstrong_check(num_var)
