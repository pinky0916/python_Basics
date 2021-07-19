num='STRING'
while (num.isdigit()==False) or (num not in range(1,11)) :

    num=input('Enter a number between 1-10:')

    if num.isdigit()==False:
        print("Sorry you have entered non number:")

    if (num.isdigit()==True) and (int(num) not in range(1,11)) :
        print('OOPS,enter between 1 and 10')
    elif (num.isdigit()==True) and (int(num) in range(1,11)):
            print(f'The {num} entered is within range of 1 and 10')
            break

print("Exit")



