num = int(input("Enter the number "))
prime_list = [2, 3, 5, 7]
flag = False

if num not in prime_list:
    for i in prime_list:
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("not Prime")
else:
    print("Prime")

