num = int(input("Enter a number to check if its prime or not:"))
print(num)
prime_list = [2, 3, 5, 7]
prime_flag = True
if num in prime_list:
    print("The given number {} is prime".format(num))
else:
    for i in prime_list:

        if num % i == 0:
            prime_flag = False
            #break
    else:
         print("A")
         print("The given number {} is prime".format(num))


if prime_flag == False:
    print("Not Prime")